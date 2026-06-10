---
tags: [类型/工作区配置, 主题/skill索引]
---
# 工作区 Skill Index

> 目的：在 `E:\AIGC工作站` 预装 Skill 索引入口。开始具体任务时，先判断任务类型；只有匹配触发条件时，才读取对应 `SKILL.md` 辅助推进。

## 权威索引

- 主索引：`E:\knowledge-base\07_skill存档\SKILL_INDEX.md`
- 存档索引：`E:\knowledge-base\07_skill存档\07_skill存档索引.md`
- Skill 根目录：`E:\knowledge-base\07_skill存档\`

本文件只作为工作区快捷入口，不复制 Skill 正文。若知识库索引和本文件冲突，以知识库 `SKILL_INDEX.md` 与具体 `SKILL.md` 为准。

## 使用协议

1. 接到任务后，先判断是否需要 Skill。
2. 如果任务明显匹配某个 Skill，读取对应 `SKILL.md`，只加载完成任务所需的最小内容。
3. 如果任务只是普通文件整理、Git 同步、简单问答，不强行使用 Skill。
4. 如果多个 Skill 都可能适用，优先选最贴近任务产出的一个；必要时按顺序组合。
5. 产出必须落回当前项目目录或用户指定位置，不把知识库 Skill 正文复制进项目成果。

## 常用 Skill 快捷表

| 场景 | 优先 Skill | 文件路径 |
|---|---|---|
| 优化 Midjourney / Seedance / 图片视频 prompt | `aigc-prompt-optimizer` | `E:\knowledge-base\07_skill存档\aigc-prompt-optimizer\SKILL.md` |
| 写跨工具通用 prompt / Agent 指令 / Cursor 指令 | `prompt-master` | `E:\knowledge-base\07_skill存档\prompt-master\SKILL.md` |
| AI 短片灵感、剧作、可制作方案 | `ai-short-film-screenwriting` | `E:\knowledge-base\07_skill存档\ai-short-film-screenwriting\SKILL.md` |
| 分析 AI 短片结构、拉片、类型判断 | `ai-short-film-breakdown` | `E:\knowledge-base\07_skill存档\ai-short-film-breakdown\SKILL.md` |
| 创作复盘、测试复盘、比赛复盘 | `aigc-postmortem` | `E:\knowledge-base\07_skill存档\aigc-postmortem\SKILL.md` |
| Suno 歌曲 / 配乐 brief | `suno-music-brief` | `E:\knowledge-base\07_skill存档\suno-music-brief\SKILL.md` |
| MJ 角色一致性、sref / oref / moodboard | `character-consistency-mj` | `E:\knowledge-base\07_skill存档\character-consistency-mj\SKILL.md` |
| 内容发布前审计、平台适配、标题文案 | `content-publish-sop` | `E:\knowledge-base\07_skill存档\content-publish-sop\SKILL.md` |
| Remotion 科普解释视频 | `remotion-explainer-workflow` | `E:\knowledge-base\07_skill存档\remotion-skill\SKILL.md` |
| 歌曲 MV 字幕 / Demucs / WhisperX 自动化 | `song-caption-mv-workflow` | `E:\knowledge-base\07_skill存档\song-caption-mv-workflow\SKILL.md` |
| 子任务完成回执 / 收口简报 | `subtask-receipt-writer` | `E:\knowledge-base\07_skill存档\subtask-receipt-writer\SKILL.md` |

## 工作区默认判断

- 项目目录创建、归档、README、阶段同步：通常不用 Skill，按仓库结构规范执行。
- 需要写 prompt、视频脚本、分镜、发布文案、复盘文档时，先查本索引。
- 需要实际剪辑、字幕、Remotion、ffmpeg 时，优先加载 Codex 可执行类 Skill。
- 当用户明确说“用某个 Skill”时，直接读取该 Skill 的 `SKILL.md`。
