import { Composition } from 'remotion';
import { AnomalyStyleTest } from './Anomaly';

export const RemotionRoot: React.FC = () => (
  <Composition
    id="AnomalyStyleTest"
    component={AnomalyStyleTest}
    durationInFrames={640}   // 240 + 200 + 200 ≈ 21.3s @30fps
    fps={30}
    width={1920}
    height={1080}
  />
);
