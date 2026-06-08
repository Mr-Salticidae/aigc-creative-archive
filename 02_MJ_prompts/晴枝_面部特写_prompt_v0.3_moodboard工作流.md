# 晴枝 · 面部特写 Prompt v0.3

## 定位

这是 R2 成功后的修正版工作流，不是单纯改 prompt。核心是：prompt 负责内容，moodboard / personalize 负责账号审美底色。

## 使用前提

- 目标工具：Midjourney V8.1
- 必须开启：moodboard
- 建议开启：personalize
- 暂不使用：sref
- 暂不使用：oref，直到 R2 稳定复跑后再启用

## Copy-ready Prompt

```text
close-up fine art portrait photography, adult East Asian young woman named Qingzhi, refined East Asian beauty, face inspired by the same aesthetic lineage as Yanxia but warmer and springlike, soft oval face, clean natural facial features, almond-shaped slightly phoenix-like eyes, bright calm gaze with quiet curiosity, refined small nose, soft pale rose lips, natural sun-warmed skin tone with subtle blush, long black hair softly lifted by a spring breeze, a slight unforced smile, luminous but not retouched, graceful and memorable face, lively but not childish, clear relaxed presence, late spring garden atmosphere, pale flowers and fresh green leaves softly blurred in background, dappled morning sunlight, delicate leaf shadows across cheek and hair, shallow depth of field, 85mm portrait lens, natural color grading, subtle skin texture, quiet story feeling, a young woman quietly returning to life --ar 3:4 --v 8.1 --style raw --no text, watermark, logo, blurry, low quality, child, teenager, schoolgirl, seductive, sensual, heavy makeup, plastic skin, over-retouched face, western face, influencer makeup, exaggerated smile, crying, sadness, lolita
```

## 追加方式

在 Midjourney 中使用你的 moodboard / personalize 设置，不要只复制 prompt 裸跑。

## 复跑目标

同 prompt + 同 moodboard 复跑 4-8 张，观察：

- 是否稳定出现 R2 的五官和骨相优势
- 是否稳定保留春末初夏氛围
- 是否避免退回普通甜妹脸
- 是否比 R1 更接近账号 IP 审美

稳定后再进入 `--oref R2_favorite_晴枝_moodboard_face.png` 的扩展测试。
