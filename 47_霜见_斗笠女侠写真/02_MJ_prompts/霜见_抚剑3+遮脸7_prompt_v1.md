---
tags: [类型/prompt]
---
# 霜见 · 分镜 #3 抚剑垂眸 + #7 斗笠遮脸 · prompt v1

> 2026-06-17 · 两张不直视图(冷艳距离感)
> 挂载约定:**图片点击挂载,权重 `--sw`/`--ow` 写进 prompt**(见 [[oref与sref的工具版本与挂载方式]])
> #3 = oref-on(v7,锁脸,`--sw`+`--ow`);#7 = oref-off(v8.1,遮脸不锁脸,仅 `--sw`)

---

## #3 · 抚剑垂眸 · 近景特写(oref-on / v7)

> UI 点挂 sref(R2 静物)+ oref(R1/R4 脸);权重见 prompt 尾

```
Museum level art portrait photography, a lone female swordswoman lowering her gaze to the sheathed sword she holds, fingers resting on the hilt wrapped with a crimson cord, an east asian woman, delicate oval face, soft jawline, slightly raised cheekbones, cool porcelain skin with faint natural crimson, almond shaped slightly drooping dark brown eyes cast downward, distant mountain eyebrows, small delicate nose bridge, gentle light rose matte lips, a cold aloof ethereal elegant temperament. Woven bamboo douli hat tilted back with a thin crimson cord, long dark hair with loose strands, flowing moon white silk hanfu robe, deep ink black sash, red cord jade pendant at collar. Close up, hands and face in frame, off center composition, shallow depth of field, soft misty bamboo bokeh. Cool soft side light, quiet shadow, 35mm film, deep shadow gradient, cool moon white and ink black tones with one crimson accent, Vogue China editorial style, cinematic still, fine art photography. --ar 3:4 --v 7 --style raw --sw 100 --ow 100 --no text, watermark, logo, blurry
```

## #7 · 斗笠遮脸张力 · 近景(oref-off / v8.1)

> UI 只点挂 sref(R2 静物),**不挂 oref**(遮脸不需锁脸);权重仅 `--sw`

```
Museum level art portrait photography, a lone female swordswoman standing still in a dim misty bamboo grove, a woven bamboo douli hat worn low, its wide brim casting deep shadow over the upper half of her face, only her gentle light rose matte lips and pale jaw catching the cool light, eyes hidden in shadow, an east asian woman, cool porcelain skin, a cold aloof mysterious temperament. A thin crimson cord on the hat, long dark hair falling past her shoulders, flowing moon white silk hanfu robe, deep ink black sash, red cord jade pendant at collar. Close up, off center composition, large negative space, deep shadow. Cool dim low key light, heavy drifting fog, 35mm film, deep shadow gradient, cool moon white and ink black tones with one crimson accent, Vogue China editorial style, cinematic still, fine art photography. --ar 3:4 --raw --hd --sw 100 --no text, watermark, logo, blurry
```

---

## 微调速查

| 张 | 关键 | 调 |
|---|---|---|
| #3 抚剑 | 手 + 脸同框、垂眸、侧光 | 手画崩:`--no` 加 deformed hands;脸不像:`--ow` 升 130 |
| #7 遮脸 | 笠檐压低、上半脸暗、只露唇颌 | 想更神秘:加 `face mostly in shadow`;露太多:`brim lower, covering the eyes` |

## 关联

- 分镜表:`../霜见_系列分镜规划_v1.md`(#3 正片 / #7 封底)
- 锚点:`../03_出图记录/`(R1/R4 脸 · R2 sref)
- 工具约束:[[oref与sref的工具版本与挂载方式]]
