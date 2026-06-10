import React from 'react';
import { interpolate, useCurrentFrame } from 'remotion';
import { voiceoverTiming } from '../audio/generated/voiceoverTiming';
import { COLORS, FONT, TYPE } from '../design-tokens';

type Props = {
  sceneStartFrame: number;
};

export const NarrationCaption: React.FC<Props> = ({ sceneStartFrame }) => {
  const frame = useCurrentFrame();
  const globalFrame = sceneStartFrame + frame;
  const active = voiceoverTiming.beats.find(
    (beat) => globalFrame >= beat.startFrame && globalFrame < beat.startFrame + beat.durationInFrames,
  );
  const fallback = voiceoverTiming.beats.find((beat) => globalFrame < beat.startFrame + beat.durationInFrames);
  const beat = active ?? fallback;
  const opacity = active
    ? interpolate(globalFrame - active.startFrame, [0, 16], [0, 1], { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' })
    : 0.68;

  if (!beat) {
    return null;
  }

  return (
    <div
      style={{
        position: 'absolute',
        left: 180,
        right: 180,
        bottom: 118,
        minHeight: 104,
        padding: '24px 34px',
        borderRadius: 14,
        background: 'rgba(245,241,232,0.94)',
        border: `3px solid ${COLORS.ink}`,
        color: COLORS.ink,
        fontFamily: FONT.sans,
        fontSize: TYPE.caption,
        fontWeight: 800,
        lineHeight: 1.36,
        textAlign: 'center',
        opacity,
      }}
    >
      {beat.caption}
    </div>
  );
};
