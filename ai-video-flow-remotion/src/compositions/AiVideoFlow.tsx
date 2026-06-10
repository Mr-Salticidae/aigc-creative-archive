import React from 'react';
import { AbsoluteFill, Series } from 'remotion';
import { VoiceoverAudio } from '../components/VoiceoverAudio';
import { SceneRenderer } from '../components/SceneRenderer';
import { sceneSpecs } from '../data/sceneSpecs';
import { sceneDurationFor, sceneStartFor, totalFrames } from '../utils/timing';

export const TOTAL_FRAMES = totalFrames;

export const AiVideoFlow: React.FC = () => (
  <AbsoluteFill>
    <VoiceoverAudio />
    <Series>
      {sceneSpecs.map((scene) => (
        <Series.Sequence key={scene.id} durationInFrames={sceneDurationFor(scene.id)}>
          <SceneRenderer scene={scene} sceneStartFrame={sceneStartFor(scene.id)} />
        </Series.Sequence>
      ))}
      <Series.Sequence durationInFrames={45}>
        <SceneRenderer scene={sceneSpecs[sceneSpecs.length - 1]} sceneStartFrame={sceneStartFor('scene_07_takeaway')} />
      </Series.Sequence>
    </Series>
  </AbsoluteFill>
);
