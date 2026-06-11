# 晴枝 · 连拍01《雏菊》 prompt v0.1

## 微故事

三张一组：她在小径上望见一丛雏菊（好奇）→ 俯身凑近，指尖悬停（温柔专注）→ 起身时手里多了一朵，被风吹乱头发后轻轻笑了（轻盈喜悦）。

情绪线：好奇 → 专注 → 喜悦。这是"刚刚重新喜欢上这个世界"的最小叙事单元。

## 连贯性锁定（三张共用）

- `--oref` 用核心锚点 R2-0，起步 `--ow 100`（脸漂提到 200，背景被锁死降到 50）
- moodboard / personalize 保持开启，不用 sref
- 服装统一：cream-white lightweight linen dress
- 光线统一：soft morning sunlight, leaf shadows
- 签名物：white daisies 贯穿三张，承担情绪媒介

## 镜头1 望见

```text
fine art portrait photography, adult East Asian young woman named Qingzhi pausing mid-step on a late spring garden path, same face and facial harmony as omni reference, soft oval face, almond-shaped phoenix eyes, bright gaze drawn to something just off the path, head slightly turned, unposed candid moment, long black hair lifted by a light breeze, cream-white lightweight linen dress, a small patch of white daisies glowing in sunlight at the lower foreground, garden path leading diagonally into soft green depth, foreground-midground-background layering, soft morning sunlight through trees, moving leaf shadows, quiet story feeling, lively but not childish, shallow depth of field, 50mm lens, natural color grading, subtle skin texture --ar 3:4 --v 8.1 --style raw --oref [R2_CORE_ANCHOR_IMAGE_URL] --ow 100 --no text, watermark, logo, blurry, low quality, child, teenager, schoolgirl, seductive, sensual, heavy makeup, plastic skin, influencer pose, exaggerated smile, crying, sadness
```

## 镜头2 俯身

```text
fine art portrait photography, adult East Asian young woman named Qingzhi crouching gracefully beside a patch of small white daisies in a late spring garden, same face and facial harmony as omni reference, soft oval face, almond-shaped phoenix eyes, gentle downward gaze full of quiet curiosity, three-quarter face view, fingertips hovering just above one daisy without picking it, long black hair slipping over one shoulder, cream-white lightweight linen dress gathered naturally, low camera angle close to the ground, daisies as soft foreground framing, uncluttered green background, dappled morning sunlight on her cheek and hands, intimate tender moment, lively but not childish, shallow depth of field, 85mm portrait lens, natural color grading, subtle skin texture --ar 3:4 --v 8.1 --style raw --oref [R2_CORE_ANCHOR_IMAGE_URL] --ow 100 --no text, watermark, logo, blurry, low quality, child, teenager, schoolgirl, seductive, sensual, heavy makeup, plastic skin, influencer pose, exaggerated smile, crying, sadness
```

## 镜头3 起身轻笑

```text
fine art portrait photography, adult East Asian young woman named Qingzhi standing up on a late spring garden path holding a single small white daisy loosely at her side, same face and facial harmony as omni reference, soft oval face, almond-shaped phoenix eyes, a slight unforced laugh as wind tousles her long black hair, gaze toward someone outside the frame, cream-white lightweight linen dress moving in the breeze, bright open garden background with soft negative space, off-center composition, light airy body language, soft morning sunlight, a few daisy petals drifting in the air, a young woman quietly returning to life, lively but not childish, shallow depth of field, 85mm portrait lens, natural color grading, subtle skin texture --ar 3:4 --v 8.1 --style raw --oref [R2_CORE_ANCHOR_IMAGE_URL] --ow 100 --no text, watermark, logo, blurry, low quality, child, teenager, schoolgirl, seductive, sensual, heavy makeup, plastic skin, influencer pose, exaggerated smile, crying, sadness
```

## 设计说明

| 维度 | 镜头1 | 镜头2 | 镜头3 |
|---|---|---|---|
| 景别 | 全身/中景，对角线小径 | 低机位近景，雏菊前景框景 | 中景，留白构图 |
| 视线 | 望向画外雏菊 | 低头看花 | 望向画外的人 |
| 情绪 | 好奇 | 温柔专注 | 轻盈喜悦 |
| 雏菊角色 | 远处的光点 | 触碰对象 | 手中信物+飘落花瓣 |

- 三张视线都不直视镜头，保持 candid 故事感，避免摆拍
- 镜头2 的 three-quarter face view 是为了 oref 锁脸留出可识别角度，出图若脸部偏移优先提 `--ow`
- 镜头3 的 `a few daisy petals drifting` 是轻量点缀，若画面变梦幻童话就删掉

## 验收标准

- 三张并排看，能不能不配文字就读出"发现→靠近→带走"
- 脸是否三张一致（对照 R2-0）
- 是否守住禁忌：不幼态、不甜腻、不摆拍
