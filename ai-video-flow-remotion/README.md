# AI视频创作流程 Remotion 样片

把 `AI视频1 - AI视频创作流程.md` 转成一条面向 AI 视频新手的横版解释动画。

## Commands

```powershell
npm.cmd install
npm.cmd run generate:voiceover
npm.cmd run typecheck
npm.cmd run still
npm.cmd run render
```

TTS 需要在 `.env` 中配置 `ELEVENLABS_API_KEY` 和 `ELEVENLABS_VOICE_ID`。
