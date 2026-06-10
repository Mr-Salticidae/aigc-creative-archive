import React from 'react';
import { interpolate, spring, useCurrentFrame, useVideoConfig } from 'remotion';
import { COLORS, FONT, TYPE } from '../design-tokens';

type Props = {
  title: string;
  kicker: string;
};

export const Label: React.FC<Props> = ({ title, kicker }) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const titleProgress = spring({ frame, fps, config: { damping: 24, stiffness: 82, mass: 1 }, durationInFrames: 28 });
  const kickerOpacity = interpolate(frame, [18, 48], [0, 1], { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' });

  return (
    <>
      <div
        style={{
          position: 'absolute',
          top: 112,
          left: 132,
          right: 132,
          fontFamily: FONT.sans,
          fontSize: TYPE.sceneTitle,
          lineHeight: 1.18,
          fontWeight: 800,
          color: COLORS.white,
          opacity: titleProgress,
          transform: `translateY(${interpolate(titleProgress, [0, 1], [20, 0])}px)`,
        }}
      >
        {title}
      </div>
      <div
        style={{
          position: 'absolute',
          top: 180,
          left: 134,
          right: 134,
          fontFamily: FONT.sans,
          fontSize: TYPE.label,
          lineHeight: 1.45,
          color: COLORS.panel,
          opacity: kickerOpacity,
        }}
      >
        {kicker}
      </div>
    </>
  );
};
