import type { SceneId } from './sceneSpecs';

export type SceneVideoAsset = {
  sceneId: SceneId;
  src: string;
  durationInFrames: number;
};

export const sceneVideoAssets: SceneVideoAsset[] = [
  { sceneId: 'scene_01_hook', src: 'video/ai_video_flow/scene_01_hook_motion.mp4', durationInFrames: 243 },
  { sceneId: 'scene_02_core_shift', src: 'video/ai_video_flow/scene_02_core_shift_motion.mp4', durationInFrames: 272 },
  { sceneId: 'scene_03_structure', src: 'video/ai_video_flow/scene_03_structure_motion.mp4', durationInFrames: 302 },
  { sceneId: 'scene_04_emotion_to_visual', src: 'video/ai_video_flow/scene_04_emotion_to_visual_motion.mp4', durationInFrames: 302 },
  { sceneId: 'scene_05_director_skills', src: 'video/ai_video_flow/scene_05_director_skills_motion.mp4', durationInFrames: 272 },
  { sceneId: 'scene_06_editing_logic', src: 'video/ai_video_flow/scene_06_editing_logic_motion.mp4', durationInFrames: 302 },
  { sceneId: 'scene_07_takeaway', src: 'video/ai_video_flow/scene_07_takeaway_motion.mp4', durationInFrames: 243 },
];
