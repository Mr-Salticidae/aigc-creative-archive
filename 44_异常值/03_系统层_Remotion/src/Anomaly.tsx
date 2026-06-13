import React from 'react';
import {
  AbsoluteFill, Sequence, interpolate, spring,
  useCurrentFrame, useVideoConfig,
} from 'remotion';

// ── Design tokens：《异常值》终端档案版（覆盖卡片流默认蓝）──
const C = {
  void: '#050608',    // 近黑系统背景
  deep: '#0B1020',    // 深蓝黑数据空间
  amber: '#D6A84A',   // 暖黄终端文字
  amberDim: '#7A6230',// 暗一档：次要 / 未点亮
  gray: '#B8B6AE',    // 灰白
  red: '#8A1F1F',     // 异常值红（严格配给：每帧最多一个）
};
const MONO = '"JetBrains Mono","Fira Code","Noto Sans SC","PingFang SC",monospace';

// ── CRT 质感罩：扫描线 + 暗角 + 轻微亮度闪烁（终端美学核心，非装饰）──
const CRTOverlay: React.FC = () => {
  const frame = useCurrentFrame();
  const flicker = 0.96 + 0.04 * Math.sin(frame * 0.7) * Math.sin(frame * 0.13);
  return (
    <>
      <AbsoluteFill style={{
        backgroundImage:
          'repeating-linear-gradient(0deg, rgba(0,0,0,0) 0px, rgba(0,0,0,0) 2px, rgba(0,0,0,0.22) 3px)',
        pointerEvents: 'none', opacity: 0.5,
      }} />
      <AbsoluteFill style={{
        background: 'radial-gradient(ellipse at center, rgba(0,0,0,0) 55%, rgba(0,0,0,0.7) 100%)',
        pointerEvents: 'none',
      }} />
      <AbsoluteFill style={{ background: '#000', opacity: 1 - flicker, pointerEvents: 'none' }} />
    </>
  );
};

// ── 散文档案体：逐段缓慢浮现 ──
const fadeUp = (frame: number, fps: number, delay: number) => {
  const f = Math.max(0, frame - delay);
  const p = spring({ fps, frame: f, config: { damping: 30, stiffness: 50, mass: 1.2 }, durationInFrames: 40 });
  return { opacity: interpolate(p, [0, 1], [0, 1]), transform: `translateY(${interpolate(p, [0, 1], [16, 0])}px)` };
};

const OpeningTitle: React.FC = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const lines = [
    '2047 年，人生预测模型成为公共基础设施。',
    '每个人都会被生成一万种可能人生。',
    '大多数人，最终都会走向概率最高的那一条。',
  ];
  return (
    <AbsoluteFill style={{ background: C.void, justifyContent: 'center', alignItems: 'flex-start', padding: '0 220px' }}>
      <div style={{ maxWidth: 1320 }}>
        {lines.map((t, i) => (
          <div key={i} style={{
            ...fadeUp(frame, fps, i * 62),
            fontFamily: MONO, fontSize: 40, color: C.amber, lineHeight: 2.0,
            letterSpacing: 1, marginBottom: 20, textShadow: `0 0 8px ${C.amber}40`,
          }}>{t}</div>
        ))}
      </div>
      <CRTOverlay />
    </AbsoluteFill>
  );
};

// ── 终端状态读出：逐字打字 + 光标 ──
const TypeLine: React.FC<{ text: string; startFrame: number; cps?: number; color?: string }> = ({
  text, startFrame, cps = 26, color = C.amber,
}) => {
  const { fps } = useVideoConfig();
  const frame = useCurrentFrame();
  if (frame < startFrame) return <div style={{ height: '1.9em' }} />;
  const elapsed = frame - startFrame;
  const chars = Math.min(text.length, Math.floor((elapsed / fps) * cps));
  const done = chars >= text.length;
  const cursorOn = Math.floor(frame / 15) % 2 === 0;
  return (
    <div style={{ fontFamily: MONO, fontSize: 34, color, lineHeight: 1.9, letterSpacing: 1, textShadow: `0 0 6px ${color}55` }}>
      {text.slice(0, chars)}
      <span style={{ opacity: done ? (cursorOn ? 1 : 0) : 1 }}>█</span>
    </div>
  );
};

const SystemReadout: React.FC = () => {
  const frame = useCurrentFrame();
  const header = interpolate(frame, [0, 18], [0, 1], { extrapolateRight: 'clamp' });
  return (
    <AbsoluteFill style={{ background: C.deep, justifyContent: 'center', alignItems: 'flex-start', padding: '0 220px' }}>
      <div>
        <div style={{ fontFamily: MONO, fontSize: 20, color: C.amberDim, letterSpacing: 4, marginBottom: 44, opacity: header }}>
          // SYSTEM LOG · ANOMALY / ARCHIVE
        </div>
        <TypeLine text="BEHAVIORAL SAMPLE COLLECTED"   startFrame={20}  />
        <TypeLine text="EMOTIONAL PATTERN STABLE"       startFrame={72}  />
        <TypeLine text="FUTURE PATHS GENERATED: 10,000" startFrame={124} />
      </div>
      <CRTOverlay />
    </AbsoluteFill>
  );
};

// ── 方块溶解 + 异常值红块（第四/五章母题，暗调）──
const seed = (n: number) => {
  const x = Math.sin(n * 127.1 + 311.7) * 43758.5453;
  return x - Math.floor(x);   // 确定性伪随机，保证逐帧不闪
};

const AnomalyDissolve: React.FC = () => {
  const frame = useCurrentFrame();
  const cols = 9, rows = 20, step = 42, sq = 30;
  const x0 = 960 - ((cols - 1) * step) / 2;
  const y0 = 150;

  const cells: React.ReactNode[] = [];
  for (let r = 0; r < rows; r++) {
    const presentProb = interpolate(r, [0, rows - 1], [1, 0.14]); // 顶实底散
    for (let c = 0; c < cols; c++) {
      const id = r * cols + c;
      const isRed = r === 15 && c === 5;                 // 唯一异常值红块
      if (seed(id) >= presentProb && !isRed) continue;

      const looseness = 1 - presentProb;
      const phase = seed(id + 99) * Math.PI * 2;
      const floatY = looseness * 9 * Math.sin(frame * 0.045 + phase);   // 松散块微浮
      const jitterX = (seed(id + 7) - 0.5) * looseness * 26;
      const g = Math.round(interpolate(r, [0, rows - 1], [232, 96]));   // 上白下灰
      const size = sq * (0.82 + seed(id + 3) * 0.3);
      const pulse = 0.7 + 0.3 * Math.sin(frame * 0.12);

      cells.push(
        <div key={id} style={{
          position: 'absolute',
          left: x0 + c * step + jitterX,
          top: y0 + r * step + floatY,
          width: size, height: size,
          background: isRed ? C.red : `rgb(${g},${g},${g})`,
          opacity: isRed ? pulse : interpolate(r, [0, rows - 1], [1, 0.5]),
          boxShadow: isRed ? `0 0 16px ${C.red}` : 'none',
        }} />
      );
    }
  }

  const cap = interpolate(frame, [30, 55], [0, 1], { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' });
  return (
    <AbsoluteFill style={{ background: C.deep }}>
      {cells}
      <div style={{
        position: 'absolute', bottom: 130, width: '100%', textAlign: 'center',
        fontFamily: MONO, fontSize: 26, letterSpacing: 3, color: C.amber,
        opacity: cap, textShadow: `0 0 8px ${C.amber}44`,
      }}>
        ANOMALY COMPRESSION ATTEMPT 03 &nbsp;—&nbsp; FAILED
      </div>
      <CRTOverlay />
    </AbsoluteFill>
  );
};

// ── 风格基底测试合成：散文屏 → 终端屏 → 方块溶解屏 ──
export const AnomalyStyleTest: React.FC = () => (
  <AbsoluteFill style={{ background: C.void }}>
    <Sequence durationInFrames={240}><OpeningTitle /></Sequence>
    <Sequence from={240} durationInFrames={200}><SystemReadout /></Sequence>
    <Sequence from={440} durationInFrames={200}><AnomalyDissolve /></Sequence>
  </AbsoluteFill>
);
