import React from 'react';
import { interpolate, spring, useCurrentFrame, useVideoConfig } from 'remotion';
import { COLORS, FONT } from '../design-tokens';
import type { MotionSpec, SubjectSpec } from '../data/sceneSpecs';

const colorFor = (color: SubjectSpec['color']) =>
  ({
    cyan: COLORS.cyan,
    blue: COLORS.blue,
    orange: COLORS.orange,
    yellow: COLORS.yellow,
    red: COLORS.red,
    green: COLORS.green,
    panel: COLORS.panel,
    white: COLORS.white,
  })[color];

const iconFor = (type: SubjectSpec['type']) =>
  ({
    prompt: '{}',
    theme: '◎',
    script: 'T',
    scene: 'S',
    beat: 'B',
    shot: '▣',
    lens: '◉',
    person: '人',
    color: '■',
    skill: 'SK',
    edit: '剪',
    timeline: '━',
    spark: '*',
  })[type];

type Props = {
  subject: SubjectSpec;
  motions: MotionSpec[];
};

export const Subject: React.FC<Props> = ({ subject, motions }) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const motion = motions.find((item) => item.targetId === subject.id);
  const local = Math.max(0, frame - (motion?.startFrame ?? 0));
  const progress = spring({
    frame: local,
    fps,
    config: { damping: motion?.type === 'pop' ? 16 : 24, stiffness: motion?.type === 'pop' ? 130 : 86, mass: 1 },
    durationInFrames: motion?.durationFrames ?? 30,
  });
  const baseColor = colorFor(subject.color);
  const opacity = motion ? interpolate(progress, [0, 1], [0, 1]) : 1;
  const slideDistance = interpolate(progress, [0, 1], [60, 0]);
  const shake = motion?.type === 'shake' && frame >= motion.startFrame ? Math.sin(local * 0.58) * interpolate(local, [0, motion.durationFrames], [14, 0], { extrapolateRight: 'clamp' }) : 0;
  const scale = motion?.type === 'pulse' ? 1 + Math.sin(local * 0.12) * 0.035 : interpolate(progress, [0, 1], [motion?.type === 'pop' ? 0.72 : 0.96, 1]);
  const translateX = motion?.type === 'slide' ? (motion.direction === 'right' ? slideDistance : motion.direction === 'left' ? -slideDistance : 0) : 0;
  const translateY = motion?.type === 'slide' ? (motion.direction === 'down' ? slideDistance : motion.direction === 'up' ? -slideDistance : 0) : 0;

  return (
    <div
      style={{
        position: 'absolute',
        left: `${subject.x}%`,
        top: `${subject.y}%`,
        width: subject.w,
        height: subject.h,
        marginLeft: -subject.w / 2,
        marginTop: -subject.h / 2,
        borderRadius: subject.type === 'spark' ? 999 : 16,
        background: subject.color === 'panel' || subject.color === 'white' ? baseColor : `${baseColor}E6`,
        border: `3px solid ${subject.color === 'panel' || subject.color === 'white' ? COLORS.ink : COLORS.white}`,
        boxShadow: `0 18px 0 rgba(0,0,0,0.18)`,
        opacity,
        transform: `translate(${translateX + shake}px, ${translateY}px) scale(${scale})`,
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'center',
        flexDirection: 'column',
        gap: 14,
      }}
    >
      <div
        style={{
          fontFamily: FONT.mono,
          fontSize: subject.type === 'person' ? 54 : 42,
          fontWeight: 900,
          color: subject.color === 'panel' || subject.color === 'white' || subject.color === 'yellow' ? COLORS.ink : COLORS.white,
          lineHeight: 1,
        }}
      >
        {iconFor(subject.type)}
      </div>
      <div
        style={{
          fontFamily: FONT.sans,
          fontSize: 26,
          fontWeight: 800,
          color: subject.color === 'panel' || subject.color === 'white' || subject.color === 'yellow' ? COLORS.ink : COLORS.white,
          textAlign: 'center',
          lineHeight: 1.18,
          padding: '0 18px',
        }}
      >
        {subject.label}
      </div>
    </div>
  );
};
