import React from 'react';
import { AbsoluteFill, interpolate, useCurrentFrame } from 'remotion';
import { COLORS } from '../design-tokens';
import type { SceneSpec } from '../data/sceneSpecs';

type Props = {
  layout: SceneSpec['layout'];
};

export const Background: React.FC<Props> = ({ layout }) => {
  const frame = useCurrentFrame();
  const drift = interpolate(frame, [0, 180], [0, 36], { extrapolateRight: 'extend' });
  const accent = layout === 'emotion' ? COLORS.red : layout === 'timeline' ? COLORS.orange : COLORS.cyan;

  return (
    <AbsoluteFill style={{ background: COLORS.bg, overflow: 'hidden' }}>
      <div
        style={{
          position: 'absolute',
          inset: 0,
          background:
            layout === 'ending'
              ? `linear-gradient(135deg, ${COLORS.bg} 0%, #151C18 55%, #1B1A12 100%)`
              : `linear-gradient(135deg, ${COLORS.bg} 0%, #15171E 58%, #171A1F 100%)`,
        }}
      />
      <div
        style={{
          position: 'absolute',
          left: 96,
          right: 96,
          top: 84,
          height: 2,
          background: COLORS.line,
          opacity: 0.78,
        }}
      />
      <div
        style={{
          position: 'absolute',
          left: 96,
          right: 96,
          bottom: 84,
          height: 2,
          background: COLORS.line,
          opacity: 0.5,
        }}
      />
      {Array.from({ length: 11 }).map((_, index) => (
        <div
          key={index}
          style={{
            position: 'absolute',
            left: 130 + index * 170,
            top: 180 + ((index % 3) * 90 + drift) % 270,
            width: 5,
            height: 5,
            borderRadius: 3,
            background: index % 4 === 0 ? accent : COLORS.line,
            opacity: index % 4 === 0 ? 0.65 : 0.34,
          }}
        />
      ))}
    </AbsoluteFill>
  );
};
