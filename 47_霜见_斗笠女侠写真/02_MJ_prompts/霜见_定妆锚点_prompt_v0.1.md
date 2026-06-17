---
tags: [类型/prompt]
---
# 霜见 · 定妆锚点 prompt v0.1

> 用途:生成 R1 锚点定妆图(斗笠推后、脸清晰,用于 oref 锁脸)
> 工具:Midjourney v8.1
> 状态:✅ 实际生成版已回填(2026-06-17)。seed 未取(MJ 未显式提供)。

---

## 实际生成版 ✅(生成了 R1 锚点图)

> R1 锚点图 job id `3ab9e045-38c3-4ac8-8670-0d16ed89b0db` · 变体 `_2`

```
Museum level art portrait photography, a lone female swordswoman in a misty bamboo grove, East Asian woman, delicate oval face, soft jawline, slightly raised cheekbones, cool porcelain skin with faint natural crimson, almond shaped slightly drooping dark brown dewy eyes, distant mountain eyebrows, small delicate nose, gentle light rose matte lips, cold ethereal elegant temperament. Woven bamboo douli hat tilted back with a thin crimson cord, high tight ponytail with loose breeze lifted strands, flowing moon white silk hanfu robe, deep ink blue sash, red cord jade pendant at collar. Three quarter view, head slightly turned from camera, one hand lightly on hat brim, medium close up, large negative space, clean composition. 35mm film, deep shadow gradient, cool moon white and ink blue tones with crimson accent, Vogue China editorial style, cinematic still, fine art photography. --no text, watermark, logo, blurry --ar 3:4 --raw --hd
```

**与设计版的差异(实测有效写法)**:
- 用 `--raw --hd` 替代 `--style raw`(MJ v8.1 新写法,`--hd` 出高清)
- 句子用句号分组(五官 / 装扮 / 镜头 / 调色 四组),而非全逗号——分组更稳
- `--no` 只留 `text, watermark, logo, blurry`,印证 [[负面词计入prompt浓度_v1]],全程未触发审核
- seed 未取;后续若要复刻同帧不同情绪,补跑时记得开 seed

---

## 设计版 prompt(斗笠 · 锚点 A 版)

```
Museum level exquisite art portrait photography, a lone female swordswoman pausing in a misty bamboo grove, an east asian woman, delicate oval face, soft jawline, slightly raised cheekbones, cool porcelain skin with a faint natural crimson, almond shaped slightly drooping dark brown eyes with a dewy gaze, distant mountain eyebrows, small delicate nose bridge, gentle light rose matte lips, a cold and ethereal elegant temperament, a refined atmosphere, a woven bamboo traveler's hat douli tilted back off her face with a thin crimson cord tie, high tight ponytail with loose strands lifted by a soft breeze, flowing moon-white silk hanfu robe with a deep ink-blue sash, a red-cord jade pendant at her collar, three-quarter view turning her head slightly away from camera, one hand lightly resting on the hat brim, medium close-up, large negative space, clean composition, 35mm film, deep shadow gradient, cool moon-white and ink-blue tones with one crimson accent, fashionable editing, fashion editorial, vogue china editorial style, artistic portraiture, cinematic still, fine art photography --ar 3:4 --v 8.1 --style raw --no text, watermark, logo, blurry
```

## 关键约定(踩坑沉淀)

- `--no` 只留纯画质项 `text, watermark, logo, blurry`。**不要**加 `skin / facial / fingers / cosplay`——会推高浓度触发审核(见知识库 [[负面词计入prompt浓度_v1]])。
- 末尾过审神器:`fashion editorial / vogue china / artistic portraiture / fine art photography`(见 [[MJ审核避雷词表]])。
- 连撞审核时:停几分钟再跑(动态阈值冷却),或直接重试(image 端概率拦截)。

## B 氛围版(系列用,遮半脸,别拿来锁脸)

把斗笠句替换为:

```
a woven bamboo traveler's hat douli worn low, its wide brim casting a soft shadow over the upper half of her face, only her lips and jaw catching the light, eyes hidden in shadow, looking down and aside
```

## 关联

- 锚点分析:`../03_出图记录/R1_锚点定妆/R1_锚点分析.md`
- 角色卡:`../01_角色卡/霜见_角色卡_v0.1.md`
