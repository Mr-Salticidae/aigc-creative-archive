---
tags: [类型/prompt]
---
# 霜见 · 场景01 竹林深处 · prompt v0.1（四层叠用首发）

> ℹ️ **oref-on 路径(2026-06-17 修正)**:oref 高方差但可用——R3 已抽到合格图。用本版需**抽卡 8-12 张 + 逐张过素颜/无异常验收**。
> 想要稳定无塑料的基线见 `霜见_场景01_竹林深处_prompt_v0.2_无oref.md`(oref-off)。两条路径并存,按需选。

> 工具:Midjourney v8.1
> 这是第一张"四层金字塔全叠"的图:sref(风格) + oref(锁脸) + 描述词锁定(装扮) + 单图参数
> 出图前先填两个占位:`<SREF_URL>` = R2 静物锚点图URL,`<OREF_URL>` = R1 定妆锚点图URL

---

## 出图前准备

1. **提 sref**:把 `R2_sref锚点_霜见_静物.png` 上传 MJ,拿到图片 URL → 填 `<SREF_URL>`。
2. **备 oref**:把 `R1_锚点_霜见_斗笠定妆.png` 上传 MJ,拿到 URL → 填 `<OREF_URL>`。
3. 两个权重起始值:`--sw 100`(风格)、`--ow 100`(锁脸),按结果微调。

---

## 场景 A · 竹林深处 · 持剑独立(推荐首跑)

```
Museum level art portrait photography, a lone female swordswoman standing deep in a misty bamboo grove, holding a sheathed sword loosely at her side, East Asian woman, delicate oval face, soft jawline, cool porcelain skin, almond slightly drooping dark brown dewy eyes, distant mountain eyebrows, gentle light rose matte lips, cold ethereal elegant temperament. Woven bamboo douli hat tilted back with a thin crimson cord, long dark hair with loose breeze lifted strands, flowing moon white silk hanfu robe, deep ink black sash, red cord jade pendant at collar. Three quarter view looking quietly aside, medium shot, foreground bamboo framing, large negative space, atmospheric depth. 35mm film, deep shadow gradient, cool moon white and ink black tones with crimson accent, Vogue China editorial style, cinematic still, fine art photography. --sref <SREF_URL> --sw 100 --oref <OREF_URL> --ow 100 --no text, watermark, logo, blurry --ar 3:4 --raw --hd
```

## 场景 B · 雪原独行(苍茫远景)

把场景句换成:

```
a lone female swordswoman walking across a vast snowfield under a pale grey sky, wind blowing snow and her robe, distant bare trees, wide shot, small figure in large empty space
```

⚠️ sref 来自竹林静物,色温会往冷竹林拉;雪原想要更白更亮,可加 `bright snowy daylight, high key` 并把 `--sw` 降到 70-80,削弱风格压制。

## 场景 C · 客栈灯下(暖冷对比)

```
a lone female swordswoman sitting alone at a wooden table in a dim ancient inn at night, a warm oil lamp beside her, a wine cup on the table, half body, intimate close framing
```

⚠️ 暖灯 vs 冷底盘冲突,sref 冷调可能压暖光;想保暖灯就加 `warm candlelight glow on her face` 并 `--sw 60-80`。

---

## 微调速查

| 现象 | 调整 |
|---|---|
| 脸不够像 R1 | `--ow` 升到 130-150 |
| 风格被脸带跑、不够胶片 | `--sw` 升到 130-150 |
| 场景被风格压死(雪原/客栈出不来) | `--sw` 降到 60-80 |
| 又触发审核 | 检查 `--no` 是否混入人体词;只留 text/watermark/logo/blurry |

## 关联

- sref 锚点:`../03_出图记录/R2_sref锚点/`
- oref 锚点:`../03_出图记录/R1_锚点定妆/`
- 角色卡:`../01_角色卡/霜见_角色卡_v0.1.md`
- 金字塔:[[角色一致性金字塔]]
