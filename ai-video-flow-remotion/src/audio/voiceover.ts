import type { SceneId } from '../data/sceneSpecs';

export type VoiceoverBeat = {
  id: string;
  sceneId: SceneId;
  caption: string;
  ttsText: string;
};

export const voiceover = {
  source: 'C:\\Users\\Administrator\\Downloads\\AI视频1 - AI视频创作流程.md',
  audioPublicDir: 'audio/ai_video_flow',
  manifestPublicPath: 'audio/ai_video_flow/voiceover.manifest.json',
};

export const voiceoverBeats: VoiceoverBeat[] = [
  {
    id: 'beat_01_hook',
    sceneId: 'scene_01_hook',
    caption: '你可能已经会用 AI 生成一个镜头，但问题是：为什么镜头很多，最后还是剪不成一条片子？',
    ttsText: '你可能已经会用 AI 生成一个镜头，但问题是：为什么镜头很多，最后还是剪不成一条片子？',
  },
  {
    id: 'beat_02_core_shift',
    sceneId: 'scene_02_core_shift',
    caption: '因为 AI 视频不是先堆模型和提示词，而是先想清楚主题、观点，再根据它写剧本。',
    ttsText: '因为 AI 视频不是先堆模型和提示词，而是先想清楚主题、观点，再根据它写剧本。',
  },
  {
    id: 'beat_03_structure',
    sceneId: 'scene_03_structure',
    caption: '一条影片可以拆成场、节拍和镜头。就像文章有段落、句子和词，结构先对，镜头才接得上。',
    ttsText: '一条影片可以拆成场、节拍和镜头。就像文章有段落、句子和词，结构先对，镜头才接得上。',
  },
  {
    id: 'beat_04_emotion',
    sceneId: 'scene_04_emotion_to_visual',
    caption: 'AI 不真的理解一个人很绝望。但你可以把绝望翻译成镜头晃动、推拉变焦、冷调色和暗调光。',
    ttsText: 'AI 不真的理解一个人很绝望。但你可以把绝望翻译成镜头晃动、推拉变焦、冷调色和暗调光。',
  },
  {
    id: 'beat_05_director',
    sceneId: 'scene_05_director_skills',
    caption: '所以合格的 AI 导演，要同时掌握三件事：编剧逻辑、视听语言，以及剪辑思维。',
    ttsText: '所以合格的 AI 导演，要同时掌握三件事：编剧逻辑、视听语言，以及剪辑思维。',
  },
  {
    id: 'beat_06_editing',
    sceneId: 'scene_06_editing_logic',
    caption: '剪辑不是为了炫技。快切、跳切、卡点、叠化，本质上都要服务内容：处理信息、组合信息、创造信息。',
    ttsText: '剪辑不是为了炫技。快切、跳切、卡点、叠化，本质上都要服务内容：处理信息、组合信息、创造信息。',
  },
  {
    id: 'beat_07_takeaway',
    sceneId: 'scene_07_takeaway',
    caption: '先想清楚影片要表达什么，再让 AI 帮你拍。工具负责生成镜头，导演负责让观众看懂。',
    ttsText: '先想清楚影片要表达什么，再让 AI 帮你拍。工具负责生成镜头，导演负责让观众看懂。',
  },
];
