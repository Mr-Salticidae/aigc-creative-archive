export const FPS = 30;
export const WIDTH = 1920;
export const HEIGHT = 1080;

export type SceneId =
  | 'scene_01_hook'
  | 'scene_02_core_shift'
  | 'scene_03_structure'
  | 'scene_04_emotion_to_visual'
  | 'scene_05_director_skills'
  | 'scene_06_editing_logic'
  | 'scene_07_takeaway';

export type SubjectType =
  | 'prompt'
  | 'theme'
  | 'script'
  | 'scene'
  | 'beat'
  | 'shot'
  | 'lens'
  | 'person'
  | 'color'
  | 'skill'
  | 'edit'
  | 'timeline'
  | 'spark';

export type MotionType = 'fade' | 'slide' | 'pop' | 'pulse' | 'shake' | 'connect' | 'compress';

export type SubjectSpec = {
  id: string;
  type: SubjectType;
  label: string;
  x: number;
  y: number;
  w: number;
  h: number;
  color: 'cyan' | 'blue' | 'orange' | 'yellow' | 'red' | 'green' | 'panel' | 'white';
};

export type MotionSpec = {
  targetId: string;
  type: MotionType;
  startFrame: number;
  durationFrames: number;
  direction?: 'left' | 'right' | 'up' | 'down';
};

export type SceneSpec = {
  id: SceneId;
  title: string;
  kicker: string;
  minDurationInFrames: number;
  layout: 'network' | 'funnel' | 'structure' | 'emotion' | 'triangle' | 'timeline' | 'ending';
  subjects: SubjectSpec[];
  motion: MotionSpec[];
};

export const sceneSpecs: SceneSpec[] = [
  {
    id: 'scene_01_hook',
    title: '会生成镜头，不等于会做影片',
    kicker: 'AI 视频的第一道坎不是模型，而是导演思维',
    minDurationInFrames: 240,
    layout: 'network',
    subjects: [
      { id: 'prompt_a', type: 'prompt', label: '提示词', x: 25, y: 42, w: 260, h: 130, color: 'cyan' },
      { id: 'model', type: 'spark', label: '模型', x: 42, y: 33, w: 220, h: 120, color: 'blue' },
      { id: 'shot', type: 'shot', label: '单个镜头', x: 58, y: 44, w: 300, h: 160, color: 'yellow' },
      { id: 'broken', type: 'edit', label: '剪不成片', x: 72, y: 62, w: 300, h: 150, color: 'red' },
    ],
    motion: [
      { targetId: 'prompt_a', type: 'slide', startFrame: 0, durationFrames: 34, direction: 'left' },
      { targetId: 'model', type: 'pop', startFrame: 28, durationFrames: 28 },
      { targetId: 'shot', type: 'connect', startFrame: 60, durationFrames: 52 },
      { targetId: 'broken', type: 'shake', startFrame: 132, durationFrames: 70 },
    ],
  },
  {
    id: 'scene_02_core_shift',
    title: '先定主题，再写剧本',
    kicker: '不要从镜头开始，要从影片要表达什么开始',
    minDurationInFrames: 300,
    layout: 'funnel',
    subjects: [
      { id: 'prompt_1', type: 'prompt', label: '模型', x: 22, y: 34, w: 230, h: 110, color: 'cyan' },
      { id: 'prompt_2', type: 'prompt', label: '参数', x: 24, y: 56, w: 230, h: 110, color: 'blue' },
      { id: 'theme', type: 'theme', label: '主题 / 观点', x: 51, y: 46, w: 360, h: 180, color: 'yellow' },
      { id: 'script', type: 'script', label: '剧本', x: 74, y: 49, w: 260, h: 150, color: 'green' },
    ],
    motion: [
      { targetId: 'prompt_1', type: 'slide', startFrame: 0, durationFrames: 32, direction: 'left' },
      { targetId: 'prompt_2', type: 'slide', startFrame: 16, durationFrames: 32, direction: 'left' },
      { targetId: 'theme', type: 'compress', startFrame: 80, durationFrames: 70 },
      { targetId: 'script', type: 'connect', startFrame: 150, durationFrames: 70 },
    ],
  },
  {
    id: 'scene_03_structure',
    title: '场、节拍、镜头',
    kicker: '像写文章一样组织影片结构',
    minDurationInFrames: 360,
    layout: 'structure',
    subjects: [
      { id: 'scene', type: 'scene', label: '场', x: 25, y: 50, w: 260, h: 190, color: 'blue' },
      { id: 'beat', type: 'beat', label: '节拍 / 镜头组', x: 50, y: 50, w: 330, h: 190, color: 'orange' },
      { id: 'shot', type: 'shot', label: '镜头', x: 76, y: 50, w: 250, h: 190, color: 'cyan' },
    ],
    motion: [
      { targetId: 'scene', type: 'pop', startFrame: 0, durationFrames: 30 },
      { targetId: 'beat', type: 'pop', startFrame: 54, durationFrames: 30 },
      { targetId: 'shot', type: 'pop', startFrame: 108, durationFrames: 30 },
    ],
  },
  {
    id: 'scene_04_emotion_to_visual',
    title: '把情绪翻译成视听语言',
    kicker: 'AI 不懂绝望，但能执行镜头、光线和色彩',
    minDurationInFrames: 390,
    layout: 'emotion',
    subjects: [
      { id: 'person', type: 'person', label: '人物情绪', x: 26, y: 55, w: 260, h: 360, color: 'panel' },
      { id: 'lens', type: 'lens', label: '晃动 / 变焦', x: 50, y: 35, w: 300, h: 140, color: 'cyan' },
      { id: 'cold', type: 'color', label: '冷调色', x: 63, y: 56, w: 230, h: 130, color: 'blue' },
      { id: 'dark', type: 'color', label: '暗调光', x: 77, y: 66, w: 230, h: 130, color: 'red' },
    ],
    motion: [
      { targetId: 'person', type: 'fade', startFrame: 0, durationFrames: 36 },
      { targetId: 'lens', type: 'shake', startFrame: 82, durationFrames: 85 },
      { targetId: 'cold', type: 'slide', startFrame: 156, durationFrames: 36, direction: 'right' },
      { targetId: 'dark', type: 'slide', startFrame: 205, durationFrames: 36, direction: 'right' },
    ],
  },
  {
    id: 'scene_05_director_skills',
    title: '合格的 AI 导演',
    kicker: '编剧逻辑、视听语言、剪辑思维缺一不可',
    minDurationInFrames: 360,
    layout: 'triangle',
    subjects: [
      { id: 'writing', type: 'script', label: '编剧逻辑', x: 50, y: 30, w: 300, h: 150, color: 'yellow' },
      { id: 'visual', type: 'lens', label: '视听语言', x: 32, y: 64, w: 300, h: 150, color: 'cyan' },
      { id: 'editing', type: 'edit', label: '剪辑思维', x: 68, y: 64, w: 300, h: 150, color: 'orange' },
      { id: 'director', type: 'person', label: 'AI 导演', x: 50, y: 54, w: 220, h: 220, color: 'panel' },
    ],
    motion: [
      { targetId: 'director', type: 'pop', startFrame: 0, durationFrames: 32 },
      { targetId: 'writing', type: 'connect', startFrame: 64, durationFrames: 50 },
      { targetId: 'visual', type: 'connect', startFrame: 110, durationFrames: 50 },
      { targetId: 'editing', type: 'connect', startFrame: 156, durationFrames: 50 },
    ],
  },
  {
    id: 'scene_06_editing_logic',
    title: '剪辑手法服务内容',
    kicker: '处理信息、组合信息、创造信息，而不是炫技',
    minDurationInFrames: 360,
    layout: 'timeline',
    subjects: [
      { id: 'info_a', type: 'scene', label: '处理信息', x: 24, y: 40, w: 240, h: 120, color: 'cyan' },
      { id: 'info_b', type: 'beat', label: '组合信息', x: 42, y: 32, w: 240, h: 120, color: 'yellow' },
      { id: 'info_c', type: 'shot', label: '创造信息', x: 60, y: 42, w: 240, h: 120, color: 'green' },
      { id: 'timeline', type: 'timeline', label: '时间线', x: 52, y: 68, w: 780, h: 120, color: 'panel' },
    ],
    motion: [
      { targetId: 'info_a', type: 'slide', startFrame: 0, durationFrames: 34, direction: 'left' },
      { targetId: 'info_b', type: 'slide', startFrame: 62, durationFrames: 34, direction: 'up' },
      { targetId: 'info_c', type: 'slide', startFrame: 124, durationFrames: 34, direction: 'right' },
      { targetId: 'timeline', type: 'connect', startFrame: 190, durationFrames: 80 },
    ],
  },
  {
    id: 'scene_07_takeaway',
    title: '先想清楚表达，再让 AI 帮你拍',
    kicker: '跳蛛先生 / AI视频创作流程',
    minDurationInFrames: 240,
    layout: 'ending',
    subjects: [
      { id: 'theme', type: 'theme', label: '主题', x: 31, y: 52, w: 260, h: 150, color: 'yellow' },
      { id: 'ai', type: 'spark', label: 'AI 拍摄', x: 51, y: 52, w: 260, h: 150, color: 'cyan' },
      { id: 'film', type: 'timeline', label: '成片', x: 71, y: 52, w: 260, h: 150, color: 'green' },
    ],
    motion: [
      { targetId: 'theme', type: 'pop', startFrame: 0, durationFrames: 28 },
      { targetId: 'ai', type: 'connect', startFrame: 60, durationFrames: 48 },
      { targetId: 'film', type: 'connect', startFrame: 120, durationFrames: 48 },
    ],
  },
];
