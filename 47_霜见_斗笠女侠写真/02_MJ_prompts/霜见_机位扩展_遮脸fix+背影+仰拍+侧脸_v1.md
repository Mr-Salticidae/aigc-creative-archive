---
tags: [类型/prompt]
---
# 霜见 · 机位扩展 · 遮脸fix + 背影 + 仰拍 + 侧脸 · v1

> 2026-06-17 · 解决"正面太多单调":加仰拍/背影/纯侧脸,视线散向不同方向
> 挂载:图片点击挂,`--sw`/`--ow` 写 prompt;oref-on→v7 无 hd,oref-off→v8.1 可 hd

---

## #7-fix · 斗笠遮脸(oref-off / v8.1)

> 上版没遮住的原因:提到 `eyes` MJ 就把眼画出来。本版**低头+笠檐前压+略俯拍+不提眼+`--no visible eyes`**强制遮挡。

```
Museum level art portrait photography, a lone female swordswoman standing in a dim misty bamboo grove, head bowed low, her woven bamboo douli hat angled forward so the wide brim fully hides her eyes and upper face, only her lips, chin and pale neck visible below the brim, an east asian woman, cool porcelain skin, gentle light rose matte lips, a quiet mysterious mood. A thin crimson cord on the hat, long dark hair falling forward, flowing moon white silk hanfu robe, deep ink black sash, red cord jade pendant at collar. Close up, slightly high camera angle looking down onto the hat, off center, large negative space, deep shadow. Cool dim top light, heavy fog, 35mm film, deep shadow gradient, cool moon white and ink black tones with one crimson accent, Vogue China editorial style, cinematic still, fine art photography. --ar 3:4 --raw --hd --sw 100 --no text, watermark, logo, blurry, visible eyes, face fully lit
```

## 新A · 背影回首(oref-off / v8.1) — 视线:右后方远处

```
Museum level art portrait photography, a lone female swordswoman seen from behind in a misty bamboo grove, her back to the camera, turning her head just slightly over her shoulder to gaze away into the distance so only the edge of her cheek and lowered lashes show, an east asian woman, a woven bamboo douli hat with a thin crimson cord from behind, long dark hair down her back, flowing moon white silk hanfu robe, deep ink black sash, a red cord trailing. Medium full shot from behind, low camera, large negative space, atmospheric depth. Cool misty backlight, 35mm film, deep shadow gradient, cool moon white and ink black tones with one crimson accent, Vogue China editorial style, cinematic still, fine art photography. --ar 3:4 --raw --hd --sw 100 --no text, watermark, logo, blurry
```

## 新B · 仰拍英气(oref-on / v7) — 视线:俯视镜头外下方

```
Museum level art portrait photography, low angle hero shot looking up at a lone female swordswoman among tall bamboo, she gazes down and away to the side past the camera, chin slightly lifted, an east asian woman, delicate oval face, soft jawline, cool porcelain skin with faint natural crimson, almond shaped slightly drooping dark brown eyes looking downward, distant mountain eyebrows, gentle light rose matte lips, a cold proud aloof temperament. Woven bamboo douli hat tilted back with a thin crimson cord, long dark hair, flowing moon white silk hanfu robe, deep ink black sash, red cord jade pendant. Low angle medium shot, bamboo canopy and pale sky behind, negative space above. Cool overcast light, 35mm film, deep shadow gradient, cool moon white and ink black tones with one crimson accent, Vogue China editorial style, cinematic still, fine art photography. --ar 3:4 --v 7 --style raw --sw 100 --ow 100 --no text, watermark, logo, blurry
```

## 新C · 纯侧脸特写(oref-on / v7) — 视线:左侧远方

```
Museum level art portrait photography, a sharp side profile close up of a lone female swordswoman gazing far to the left, an east asian woman, delicate profile, soft jawline, small straight nose, cool porcelain skin with faint natural crimson, almond slightly drooping dark brown eye, distant mountain eyebrow, gentle light rose matte lips, a cold ethereal aloof temperament. Woven bamboo douli hat tilted back with a thin crimson cord, long dark hair with loose strands, flowing moon white silk hanfu robe, deep ink black sash, red cord jade pendant at collar. Strict profile close up, large negative space in front of her gaze, shallow depth of field, misty bamboo bokeh. Cool soft side light rimming her profile, 35mm film, deep shadow gradient, cool moon white and ink black tones with one crimson accent, Vogue China editorial style, cinematic still, fine art photography. --ar 3:4 --v 7 --style raw --sw 100 --ow 100 --no text, watermark, logo, blurry
```

---

## 机位/视线 自检(避免单调)

| 维度 | 本组覆盖 |
|---|---|
| 机位 | 平视(#1#4)、近景特写(#3)、**俯拍遮脸(#7)**、**仰拍(新B)**、**背影低机位(新A)** |
| 视线 | 直视(#1#4)、垂眸(#3)、**俯视下方(新B)**、**左远方侧脸(新C)**、**右后回首(新A)**、**完全遮挡(#7)** |

→ 一组里直视仍 ≤2(#1#4),其余全部岔开,不再正面堆叠。

## 关联

- 分镜表 v2:`../霜见_系列分镜规划_v1.md`
- 工具约束:[[oref与sref的工具版本与挂载方式]] · [[主体不看镜头律]]
