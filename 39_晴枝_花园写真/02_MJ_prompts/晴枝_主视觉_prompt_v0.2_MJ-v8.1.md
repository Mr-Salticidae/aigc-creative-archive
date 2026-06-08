# 晴枝 · 主视觉 Midjourney Prompt v0.2

## 版本目标

- 工具：Midjourney
- 目标版本：V8.1
- 优化日期：2026-06-07

## Copy-ready Prompt

```text
fine art portrait photography, adult East Asian young woman named Qingzhi, walking slowly toward camera on a blooming garden path, late spring shifting into early summer, soft oval face, clean natural features, bright calm eyes with quiet curiosity, natural sun-warmed skin tone, long black hair gently lifted by a light breeze, slight unforced smile, relaxed clear presence, lively but not childish, simple cream-white lightweight linen dress, natural loose silhouette, holding one small white daisy loosely in her hand, fresh green leaves and pale yellow flowers along the path, soft morning sunlight through trees, moving leaf shadows on her face and dress, airy garden atmosphere, candid walking moment, not posing for the camera, elegant but effortless, shallow depth of field, soft foreground flower bokeh, 35mm film photography, natural color grading, subtle skin texture, quiet story feeling, a young woman quietly returning to life --ar 3:4 --v 8.1 --style raw --no text, watermark, logo, blurry, low quality, child, teenager, schoolgirl, seductive, sensual, heavy makeup, lolita, wedding dress, princess dress, influencer pose, exaggerated smile, crying, sadness
```

## 优化说明

v0.2 相比 v0.1 的调整：

- 将参数从 `--v 7` 改为 `--v 8.1`
- 保留 `--style raw`，减少自动美化和网红感
- 删除过度散文化长句，改成 MJ 更容易抓取的摄影描述符
- 将故事句压缩为 `a young woman quietly returning to life`
- 强化 `not posing for the camera`，避免花园摆拍感
- 保留成年边界与负面词，避免幼态化和性感化

## 第一轮测试

先跑 4 张，不加参考图、不加 `--oref`。第一轮只看晴枝是否成立：成人感、气质、风、花影、轻微笑意、春末初夏空气。

如果太甜：下一轮加入 `reserved expression`, `quiet confidence`, `documentary-style candid portrait`。

如果太平：下一轮加入 `wind-touched hair`, `sun patches`, `turning her head slightly while walking`。
