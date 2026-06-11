# 晴枝 · 连拍01《雏菊》 prompt v0.3 — GPT Image 2 版

## 工具切换说明

| 维度 | Midjourney | GPT Image 2 |
|---|---|---|
| 锁脸 | `--oref` + `--ow` | 直接附上 R2-0 作为参考图，文字里声明"same person as the reference" |
| 负面词 | `--no` 列表 | 自然语言写进 Constraints 段 |
| 画幅 | `--ar 3:4` | 2:3 竖版（文字声明或 API 参数） |
| 风格控制 | moodboard/sref/--s | 描述 + 可附第二张风格参考图 |
| 连拍一致性 | 逐张 oref，靠运气 | 单次请求可出多张并保持角色一致（Thinking Mode 下最多 8 张） |

操作：每次生成都把 `04_精选成图/核心锚点/晴枝_核心锚点_R2-0.png` 作为参考图附上。

## 方案A（推荐先试）：一次出三连拍

把三个镜头写进一条 prompt，利用跨图一致性，三张脸天然统一：

```text
Using the attached reference image: keep the exact same face, facial proportions and hair of this adult East Asian young woman across all three photos.

Create a set of three 2:3 portrait photographs telling one quiet moment in a late spring garden, like consecutive frames from a film:

Photo 1 — She pauses mid-step on a garden path, head slightly turned, her gaze drawn to a small patch of white daisies glowing in morning sunlight at the lower foreground. Diagonal path leading into soft green depth.

Photo 2 — She crouches gracefully beside the daisies, gentle downward gaze full of quiet curiosity, fingertips hovering just above one flower without picking it. Low camera angle near the ground, daisies as soft foreground framing, dappled sunlight on her cheek and hands.

Photo 3 — She stands up holding a single daisy loosely at her side, a slight unforced laugh as wind tousles her long black hair, gaze toward someone outside the frame. Bright open background with soft negative space, a few petals drifting in the air.

Shared look: bare-faced natural look with no makeup, real unretouched skin with visible pores, long black hair moved by breeze, cream-white lightweight linen dress, soft morning sunlight through trees with moving leaf shadows, shallow depth of field, natural color grading, subtle film grain, candid documentary feel.

Constraints: she must read as the same person as the reference in every photo, an adult woman, not a teenager. No makeup, no airbrushed or porcelain skin, no beauty-filter look, no influencer posing, no exaggerated smile, no text, no watermark.
```

## 方案B：逐张精修（方案A某张不满意时替换单张）

### 镜头1 望见

```text
Scene: a quiet garden path in late spring, soft morning sunlight through trees, moving leaf shadows, diagonal path leading into soft green depth.

Subject: the adult East Asian young woman from the attached reference image — keep her exact face, facial proportions and hair. She pauses mid-step, head slightly turned, gaze drawn to a small patch of white daisies glowing in sunlight at the lower foreground.

Details: bare-faced natural look with no makeup, real unretouched skin with visible pores, long black hair lifted by a light breeze, cream-white lightweight linen dress. Candid documentary feel, like a film still, not a posed photo.

Output: a 2:3 portrait photograph, shallow depth of field, 50mm look, natural color grading, subtle film grain.

Constraints: same person as the reference; adult, not childish; no makeup, no airbrushed or porcelain skin, no beauty filter, no influencer posing, no exaggerated smile, no text or watermark.
```

### 镜头2 俯身

```text
Scene: a patch of small white daisies in a late spring garden, low camera angle close to the ground, daisies as soft foreground framing, uncluttered green background, dappled morning sunlight.

Subject: the adult East Asian young woman from the attached reference image — keep her exact face, facial proportions and hair, shown in three-quarter view. She crouches gracefully beside the daisies, gentle downward gaze full of quiet curiosity, fingertips hovering just above one flower without picking it.

Details: bare-faced natural look with no makeup, real unretouched skin with visible pores, long black hair slipping over one shoulder, cream-white lightweight linen dress gathered naturally, sunlight dappled on her cheek and hands.

Output: a 2:3 portrait photograph, shallow depth of field, 85mm look, natural color grading, subtle film grain, intimate tender moment.

Constraints: same person as the reference; adult, not childish; no makeup, no airbrushed or porcelain skin, no beauty filter, no influencer posing, no text or watermark.
```

### 镜头3 起身轻笑

```text
Scene: a late spring garden path, bright open background with soft negative space, soft morning sunlight, a few daisy petals drifting in the air.

Subject: the adult East Asian young woman from the attached reference image — keep her exact face, facial proportions and hair. She has just stood up, holding a single small white daisy loosely at her side, a slight unforced laugh as wind tousles her long black hair, gaze toward someone outside the frame.

Details: bare-faced natural look with no makeup, real unretouched skin with visible pores, cream-white lightweight linen dress moving in the breeze, light airy body language, off-center composition.

Output: a 2:3 portrait photograph, shallow depth of field, 85mm look, natural color grading, subtle film grain, the feeling of a young woman quietly returning to life.

Constraints: same person as the reference; adult, not childish; no makeup, no airbrushed or porcelain skin, no beauty filter, no influencer posing, no exaggerated smile, no text or watermark.
```

## 预期与风险

- GPT Image 2 写实和指令服从强，素颜/毛孔/胶片感这类要求会被认真执行——v0.2 的痛点应明显缓解
- 风险是"惊艳度"可能低于 MJ + moodboard 的审美底色；如果出图太平淡，第二步可以再附一张 R3 的成功图作为风格参考（多参考图它支持）
- 注意画幅从 3:4 变成 2:3，构图会稍微更瘦长
