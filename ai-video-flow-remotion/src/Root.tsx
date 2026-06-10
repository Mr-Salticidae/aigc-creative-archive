import { Composition } from 'remotion';
import { AiVideoFlow, TOTAL_FRAMES } from './compositions/AiVideoFlow';
import { FPS, HEIGHT, WIDTH } from './data/sceneSpecs';

export const RemotionRoot: React.FC = () => (
  <Composition
    id="AiVideoFlow"
    component={AiVideoFlow}
    durationInFrames={TOTAL_FRAMES}
    fps={FPS}
    width={WIDTH}
    height={HEIGHT}
  />
);
