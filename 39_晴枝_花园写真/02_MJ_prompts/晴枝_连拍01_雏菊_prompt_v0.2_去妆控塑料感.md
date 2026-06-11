# 晴枝 · 连拍01《雏菊》 prompt v0.2 — 去妆 & 控塑料感

## v0.1 → v0.2 改动

症状：磨皮塑料感 + 异常浓妆。

| 变量 | v0.1 | v0.2 | 理由 |
|---|---|---|---|
| stylize | 默认 | `--s 50` | 压 MJ 自动美化，塑料感最大来源 |
| 画面类型 | fine art portrait photography | candid natural light portrait photography | 去掉修图感、海报感 |
| 素颜锁定 | 无 | bare-faced fresh natural look, no visible makeup, natural unretouched skin with visible pores, subtle film grain | 正面强制 |
| 负面词 | heavy makeup（太弱） | 点名 makeup, eyeliner, false eyelashes, glossy lips, airbrushed skin, porcelain skin, beauty filter, doll-like face, 3D render | 挡淡妆和磨皮 |
| 五官描述 | 长串保留 | 删除，只留 same face as omni reference + 眼神情绪 | 文字描脸和 oref 打架，是"脸怪"的潜在来源 |

不动：oref R2-0、`--ow 100`、服装、晨光、雏菊、构图、`--ar 3:4 --v 8.1 --style raw`。

## 镜头1 望见

```text
candid natural light portrait photography, adult East Asian young woman named Qingzhi pausing mid-step on a late spring garden path, same face and facial harmony as omni reference, bright gaze drawn to something just off the path, head slightly turned, unposed candid moment, bare-faced fresh natural look with no visible makeup, natural unretouched skin with visible pores, long black hair lifted by a light breeze, cream-white lightweight linen dress, a small patch of white daisies glowing in sunlight at the lower foreground, garden path leading diagonally into soft green depth, foreground-midground-background layering, soft morning sunlight through trees, moving leaf shadows, subtle film grain, quiet story feeling, lively but not childish, shallow depth of field, 50mm lens, natural color grading --ar 3:4 --v 8.1 --style raw --s 50 --oref [R2_CORE_ANCHOR_IMAGE_URL] --ow 100 --no text, watermark, logo, blurry, low quality, child, teenager, schoolgirl, seductive, sensual, makeup, eyeliner, false eyelashes, glossy lips, airbrushed skin, porcelain skin, beauty filter, doll-like face, 3D render, plastic skin, influencer pose, exaggerated smile, crying, sadness
```

## 镜头2 俯身

```text
candid natural light portrait photography, adult East Asian young woman named Qingzhi crouching gracefully beside a patch of small white daisies in a late spring garden, same face and facial harmony as omni reference, gentle downward gaze full of quiet curiosity, three-quarter face view, fingertips hovering just above one daisy without picking it, bare-faced fresh natural look with no visible makeup, natural unretouched skin with visible pores, long black hair slipping over one shoulder, cream-white lightweight linen dress gathered naturally, low camera angle close to the ground, daisies as soft foreground framing, uncluttered green background, dappled morning sunlight on her cheek and hands, subtle film grain, intimate tender moment, lively but not childish, shallow depth of field, 85mm portrait lens, natural color grading --ar 3:4 --v 8.1 --style raw --s 50 --oref [R2_CORE_ANCHOR_IMAGE_URL] --ow 100 --no text, watermark, logo, blurry, low quality, child, teenager, schoolgirl, seductive, sensual, makeup, eyeliner, false eyelashes, glossy lips, airbrushed skin, porcelain skin, beauty filter, doll-like face, 3D render, plastic skin, influencer pose, exaggerated smile, crying, sadness
```

## 镜头3 起身轻笑

```text
candid natural light portrait photography, adult East Asian young woman named Qingzhi standing up on a late spring garden path holding a single small white daisy loosely at her side, same face and facial harmony as omni reference, a slight unforced laugh as wind tousles her long black hair, gaze toward someone outside the frame, bare-faced fresh natural look with no visible makeup, natural unretouched skin with visible pores, cream-white lightweight linen dress moving in the breeze, bright open garden background with soft negative space, off-center composition, light airy body language, soft morning sunlight, a few daisy petals drifting in the air, subtle film grain, a young woman quietly returning to life, lively but not childish, shallow depth of field, 85mm portrait lens, natural color grading --ar 3:4 --v 8.1 --style raw --s 50 --oref [R2_CORE_ANCHOR_IMAGE_URL] --ow 100 --no text, watermark, logo, blurry, low quality, child, teenager, schoolgirl, seductive, sensual, makeup, eyeliner, false eyelashes, glossy lips, airbrushed skin, porcelain skin, beauty filter, doll-like face, 3D render, plastic skin, influencer pose, exaggerated smile, crying, sadness
```

## A/B 定位实验（可选但推荐）

用镜头2跑两组对照，定位浓妆来源：

- A组：moodboard/personalize 开（默认）
- B组：moodboard/personalize 关

若 B 组素颜正常 → 浓妆来自 moodboard 审美底色，后续晴枝项目的 moodboard 需要清理掉浓妆样本，或降低其权重；若两组都浓妆 → 来源是 prompt/模型层，继续在负面词上加码。

## 升级路径

- 还有塑料感：`--s 50` → `--s 20`，或试 `--exp 5`
- 脸开始漂（素颜后五官跑偏）：`--ow 100` → `--ow 200`
- 太素、气色差：删 `no visible makeup` 留 `bare-faced fresh natural look`，加回 `natural sun-warmed skin tone with subtle blush`
