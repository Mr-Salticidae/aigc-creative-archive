import React from 'react';
import { AbsoluteFill } from 'remotion';
import { sceneVideoAssets } from '../data/sceneAssets';
import type { SceneSpec } from '../data/sceneSpecs';
import { Background } from './Background';
import { Label } from './Label';
import { NarrationCaption } from './NarrationCaption';
import { SceneVideoLayer } from './SceneVideoLayer';
import { Subject } from './Subject';

type Props = {
  scene: SceneSpec;
  sceneStartFrame: number;
};

export const SceneRenderer: React.FC<Props> = ({ scene, sceneStartFrame }) => {
  const hasVideoAsset = sceneVideoAssets.some((asset) => asset.sceneId === scene.id);

  return (
    <AbsoluteFill>
      <Background layout={scene.layout} />
      <SceneVideoLayer sceneId={scene.id} />
      {!hasVideoAsset &&
        scene.subjects.map((subject) => (
          <Subject key={subject.id} subject={subject} motions={scene.motion} />
        ))}
      <Label title={scene.title} kicker={scene.kicker} />
      <NarrationCaption sceneStartFrame={sceneStartFrame} />
    </AbsoluteFill>
  );
};
