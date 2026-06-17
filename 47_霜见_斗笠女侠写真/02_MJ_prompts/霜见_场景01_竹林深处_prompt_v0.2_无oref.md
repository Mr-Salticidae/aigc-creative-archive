---
tags: [类型/prompt]
---
# 霜见 · 场景01 竹林深处 · prompt v0.2(无 oref · 描述锚定)

> 工具:Midjourney v8.1
> 策略转向(2026-06-17):**弃用 oref**(刷三组翻车 + 塑料脸,见 [[晴枝发布复盘_oref污染与工具回归_2026-06-11]])。
> 改用 **sref(风格) + 满配五官骨相词块(气质/骨相) + 装扮签名(辨识度)** 三件套锚定。
> v0.1(带 oref)作废,保留备查。

---

## 锚定三件套(替代 oref)

1. **风格** → `--sref <SREF_URL>`(R2 静物锚点),`--sw` 80-120 试
2. **骨相 + 气质** → 满配[[东方美人五官堆叠基础句]]词块(下方已嵌)
3. **辨识度** → 装扮签名:斗笠 + 月白 + 墨黑 + 红绳玉佩(下方已嵌)

出图前只需上传 R2 静物图取 URL → 填 `<SREF_URL>`。**不再需要 oref。**

---

## 场景 A · 竹林深处 · 持剑独立(推荐首跑)

```
Museum level art portrait photography, a lone female swordswoman standing deep in a misty bamboo grove, holding a sheathed sword loosely at her side, an east asian woman, delicate oval face, soft jawline, slightly raised cheekbones, cool porcelain skin with faint natural crimson, almond shaped slightly drooping dark brown eyes with a dewy gaze, distant mountain eyebrows, small delicate nose bridge, gentle light rose matte lips, a cold and ethereal elegant temperament, a refined atmosphere. Woven bamboo douli hat tilted back with a thin crimson cord, long dark hair with loose breeze lifted strands, flowing moon white silk hanfu robe, deep ink black sash, red cord jade pendant at collar. Three quarter view looking quietly aside, medium shot, foreground bamboo framing, large negative space, atmospheric depth. 35mm film, deep shadow gradient, cool moon white and ink black tones with crimson accent, Vogue China editorial style, cinematic still, fine art photography. --sref <SREF_URL> --sw 100 --no text, watermark, logo, blurry --ar 3:4 --raw --hd
```

## 场景 B · 雪原独行 / 场景 C · 客栈灯下

场景句替换同 v0.1。注意 sref 是冷竹林调:
- 雪原想更亮白 → 加 `bright snowy daylight, high key`,`--sw` 降 70-80
- 客栈想保暖灯 → 加 `warm candlelight glow on her face`,`--sw` 降 60-80

---

## 微调速查(无 oref 版)

| 现象 | 调整 |
|---|---|
| 几张之间"不像同一个人" | 正常预期(无 oref);靠装扮签名维持辨识,或固定 `--seed` 求近似 |
| 五官/骨相飘 | 五官词块**逐字保持一致**,别改写;`a cold and ethereal elegant temperament` 是气质开关 |
| 风格不够胶片 | `--sw` 升到 120-150 |
| 场景被风格压死 | `--sw` 降到 60-80 |
| 塑料脸/浓妆 | 确认没误开 oref;加 `natural bare skin texture, minimal makeup` |
| 触发审核 | `--no` 只留 text/watermark/logo/blurry(见 [[负面词计入prompt浓度_v1]]) |

## 求"近似同脸"的额外手段(可选)

- **固定 seed**:挑一张满意的,记下其 seed,后续同 seed + 微调 prompt → 构图/脸更接近。
- **moodboard**:把几张满意的霜见脸做成 moodboard 拉力(美学优先项目晴枝实测有效),比 oref 软,不带塑料感。

## 关联

- 策略依据:[[oref污染美学律|晴枝发布复盘]] · [[装扮签名vs五官精度]]
- sref 锚点:`../03_出图记录/R2_sref锚点/`
- 角色卡:`../01_角色卡/霜见_角色卡_v0.1.md`
