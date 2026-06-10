import { sceneSpecs, type SceneId } from '../data/sceneSpecs';
import { voiceoverTiming } from '../audio/generated/voiceoverTiming';

export const sceneDurationFor = (sceneId: SceneId) => {
  const spec = sceneSpecs.find((scene) => scene.id === sceneId);
  const beats = voiceoverTiming.beats.filter((beat) => beat.sceneId === sceneId);
  const beatDuration = beats.reduce((sum, beat) => sum + beat.durationInFrames, 0);

  return Math.max(spec?.minDurationInFrames ?? 1, beatDuration);
};

export const sceneStartFor = (sceneId: SceneId) => {
  let start = 0;

  for (const scene of sceneSpecs) {
    if (scene.id === sceneId) {
      return start;
    }

    start += sceneDurationFor(scene.id);
  }

  return start;
};

export const totalFrames = sceneSpecs.reduce((sum, scene) => sum + sceneDurationFor(scene.id), 0) + voiceoverTiming.tailHoldFrames;
