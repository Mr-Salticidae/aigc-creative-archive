import React from 'react';
import { AbsoluteFill, Loop, OffthreadVideo, staticFile } from 'remotion';
import { sceneVideoAssets } from '../data/sceneAssets';
import type { SceneId } from '../data/sceneSpecs';

type Props = {
  sceneId: SceneId;
};

export const SceneVideoLayer: React.FC<Props> = ({ sceneId }) => {
  const asset = sceneVideoAssets.find((item) => item.sceneId === sceneId);

  if (!asset) {
    return null;
  }

  return (
    <AbsoluteFill style={{ background: '#101115' }}>
      <Loop durationInFrames={asset.durationInFrames}>
        <OffthreadVideo
          muted
          src={staticFile(asset.src)}
          style={{
            width: '100%',
            height: '100%',
            objectFit: 'cover',
          }}
        />
      </Loop>
      <AbsoluteFill
        style={{
          background: 'linear-gradient(180deg, rgba(16,17,21,0.14) 0%, rgba(16,17,21,0.02) 55%, rgba(16,17,21,0.18) 100%)',
          pointerEvents: 'none',
        }}
      />
    </AbsoluteFill>
  );
};
