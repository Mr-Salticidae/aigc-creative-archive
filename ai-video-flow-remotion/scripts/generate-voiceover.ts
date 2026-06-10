import { execFileSync } from 'node:child_process';
import { existsSync, mkdirSync, readFileSync, writeFileSync } from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { voiceover, voiceoverBeats } from '../src/audio/voiceover';
import { FPS } from '../src/data/sceneSpecs';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const projectRoot = path.resolve(__dirname, '..');
const envPath = path.join(projectRoot, '.env');
const audioDir = path.join(projectRoot, 'public', voiceover.audioPublicDir);
const manifestPath = path.join(audioDir, 'voiceover.manifest.json');
const timingPath = path.join(projectRoot, 'src', 'audio', 'generated', 'voiceoverTiming.ts');
const bundledFfprobePath = path.join(projectRoot, 'node_modules', '@remotion', 'compositor-win32-x64-msvc', 'ffprobe.exe');

type GeneratedBeat = {
  id: string;
  sceneId: string;
  caption: string;
  audioSrc: string;
  startFrame: number;
  durationInFrames: number;
  durationSeconds: number;
};

const loadLocalEnv = () => {
  if (!existsSync(envPath)) {
    return;
  }

  for (const line of readFileSync(envPath, 'utf8').split(/\r?\n/)) {
    const trimmed = line.trim();

    if (!trimmed || trimmed.startsWith('#')) {
      continue;
    }

    const separatorIndex = trimmed.indexOf('=');

    if (separatorIndex === -1) {
      continue;
    }

    const key = trimmed.slice(0, separatorIndex).trim();
    const rawValue = trimmed.slice(separatorIndex + 1).trim();
    const value = rawValue.replace(/^["']|["']$/g, '');

    if (key && process.env[key] === undefined) {
      process.env[key] = value;
    }
  }
};

const requiredEnv = (name: string) => {
  const value = process.env[name]?.trim();

  if (!value) {
    throw new Error(`${name} is required. Configure it in .env or the current environment.`);
  }

  return value;
};

const durationSecondsFor = (filePath: string) => {
  const ffprobeCommand = existsSync(bundledFfprobePath) ? bundledFfprobePath : 'ffprobe';
  const output = execFileSync(ffprobeCommand, ['-v', 'error', '-show_entries', 'format=duration', '-of', 'default=noprint_wrappers=1:nokey=1', filePath], {
    encoding: 'utf8',
  }).trim();
  const duration = Number(output);

  if (!Number.isFinite(duration) || duration <= 0) {
    throw new Error(`Unable to read duration for ${filePath}`);
  }

  return duration;
};

const writeTimingFile = (beats: GeneratedBeat[], totalFrames: number, tailHoldFrames: number) => {
  const content = `export type VoiceoverTimingBeat = {
  id: string;
  sceneId: string;
  caption: string;
  audioSrc: string;
  startFrame: number;
  durationInFrames: number;
  durationSeconds: number;
};

export const voiceoverTiming = {
  hasGeneratedAudio: true,
  fps: ${FPS},
  totalFrames: ${totalFrames},
  tailHoldFrames: ${tailHoldFrames},
  beats: ${JSON.stringify(beats, null, 4)} satisfies VoiceoverTimingBeat[],
};
`;

  writeFileSync(timingPath, content, 'utf8');
};

const main = async () => {
  loadLocalEnv();

  const apiKey = requiredEnv('ELEVENLABS_API_KEY');
  const voiceId = requiredEnv('ELEVENLABS_VOICE_ID');
  const modelId = process.env.ELEVENLABS_MODEL_ID?.trim() || 'eleven_v3';
  const outputFormat = 'mp3_44100_128';
  const generatedBeats: GeneratedBeat[] = [];
  let startFrame = 0;

  mkdirSync(audioDir, { recursive: true });

  for (const beat of voiceoverBeats) {
    const fileName = `${beat.id}.mp3`;
    const filePath = path.join(audioDir, fileName);

    if (!existsSync(filePath)) {
      const response = await fetch(`https://api.elevenlabs.io/v1/text-to-speech/${voiceId}?output_format=${outputFormat}`, {
        method: 'POST',
        headers: {
          'xi-api-key': apiKey,
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          text: beat.ttsText,
          model_id: modelId,
          voice_settings: {
            stability: 0.5,
            similarity_boost: 0.76,
            style: 0.25,
            use_speaker_boost: true,
          },
        }),
      });

      if (!response.ok) {
        const errorText = await response.text();
        throw new Error(`ElevenLabs TTS failed for ${beat.id} with status ${response.status}: ${errorText}`);
      }

      writeFileSync(filePath, Buffer.from(await response.arrayBuffer()));
    }

    const durationSeconds = durationSecondsFor(filePath);
    const durationInFrames = Math.max(120, Math.ceil(durationSeconds * FPS) + 18);

    generatedBeats.push({
      id: beat.id,
      sceneId: beat.sceneId,
      caption: beat.caption,
      audioSrc: `${voiceover.audioPublicDir}/${fileName}`,
      startFrame,
      durationInFrames,
      durationSeconds,
    });

    startFrame += durationInFrames;
  }

  const tailHoldFrames = 45;
  const totalFrames = startFrame + tailHoldFrames;

  writeTimingFile(generatedBeats, totalFrames, tailHoldFrames);
  writeFileSync(
    manifestPath,
    `${JSON.stringify(
      {
        provider: 'elevenlabs',
        modelId,
        voiceId,
        source: voiceover.source,
        outputFormat,
        fps: FPS,
        totalFrames,
        tailHoldFrames,
        createdAt: new Date().toISOString(),
        beats: generatedBeats,
      },
      null,
      2,
    )}\n`,
    'utf8',
  );

  console.log(
    JSON.stringify(
      {
        status: 'done',
        beatCount: generatedBeats.length,
        totalFrames,
        manifestPath,
      },
      null,
      2,
    ),
  );
};

main().catch((error) => {
  console.error(error instanceof Error ? error.message : String(error));
  process.exit(1);
});
