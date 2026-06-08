# 晴枝 · 主视觉 Midjourney Prompt v0.1

## 测试目标

验证“晴枝”作为春末初夏花园写真角色是否成立：明亮、松弛、清醒、有生命力，同时保留轻故事感。

## 主视觉画面

晴枝在花园小径上迎着风走来，阳光、花影和轻微笑意一起出现。

## Copy-ready Prompt

```text
fine art portrait photography of an adult East Asian young woman named Qingzhi walking slowly toward the camera on a garden path in late spring and early summer, clean natural facial features, soft oval face, bright calm eyes with a hint of curiosity, natural skin tone with subtle sunlit warmth, long black or deep chestnut hair gently tousled by a light breeze, a slight unforced smile, relaxed and clear presence, lively but not childish, wearing a simple cream-white lightweight linen dress, natural silhouette, no glamour styling, one small white daisy held loosely in her hand, blooming flowers and fresh green leaves around the path, soft morning sunlight filtering through trees, moving leaf shadows across her face and dress, airy seasonal atmosphere, gentle wind, candid walking moment, elegant but effortless, shallow depth of field, soft foreground flower bokeh, 35mm film photography, natural color grading, refined composition, subtle skin texture, quiet story feeling, she looks like she has just started to love the world again --ar 3:4 --v 7 --style raw --no text, watermark, logo, blurry, low quality, child, teenage, schoolgirl, seductive, sensual, heavy makeup, lolita dress, wedding dress, princess dress, influencer pose, exaggerated smile, crying, sadness
```

## 拆解

| 目标 | Prompt 表达 | 作用 |
|---|---|---|
| 成年边界 | `adult East Asian young woman` | 避免幼态化 |
| 元气感 | `lively but not childish` | 保留生命力但不低龄 |
| 气质 | `relaxed and clear presence` | 区分普通甜妹 |
| 故事感 | `she looks like she has just started to love the world again` | 给画面留一个轻叙事底色 |
| 春末初夏 | `late spring and early summer`, `fresh green leaves`, `soft morning sunlight` | 锁季节空气 |
| 视觉签名 | `one small white daisy held loosely in her hand` | 轻量角色锚点 |
| 避免摆拍 | `candid walking moment`, `no glamour styling` | 降低网红感 |

## 参数说明

- `--ar 3:4`：竖版人像写真，适合小红书和作品集封面候选。
- `--v 7`：沿用当前常用 MJ 版本假设；如实际使用 v8.1，可再单独改版。
- `--style raw`：减少模型自动美化，保留真实摄影感。
- `--no`：重点排除幼态、性感化、网红摆拍、过度梦幻和悲伤氛围。

## 第一轮测试建议

1. 先连续跑 4 张，不加 `--oref`。
2. 选出最符合“晴枝”的一张作为候选基准图。
3. 如果脸、气质、服装都成立，再用该图进入 `--oref` 扩展测试。
4. 如果图太甜，下一轮强化 `quiet story feeling` 和 `not posing for the camera`。
5. 如果图太平，下一轮强化 `wind-touched hair`, `leaf shadows`, `walking toward camera`。
