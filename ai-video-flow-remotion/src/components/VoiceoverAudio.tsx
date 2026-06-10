import React from 'react';
import { Audio, Sequence, staticFile } from 'remotion';
import { voiceoverTiming } from '../audio/generated/voiceoverTiming';

export const VoiceoverAudio: React.FC = () => {
  if (!voiceoverTiming.hasGeneratedAudio) {
    return null;
  }

  return (
    <>
      {voiceoverTiming.beats.map((beat) => (
        <Sequence key={beat.id} from={beat.startFrame} durationInFrames={beat.durationInFrames}>
          <Audio src={staticFile(beat.audioSrc)} />
        </Sequence>
      ))}
    </>
  );
};
