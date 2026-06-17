---
tags: [类型/prompt]
---
# 霜见 · sref 风格锚点 prompt v0.1

> 用途:抽一张**形态中性、无人物**的图,提取古典武侠写实风格签名,作为整个项目的**唯一 sref**
> 工具:Midjourney v8.1
> 铁律:见 [[sref纯净性原则]]——sref 锚点必须是**纯 prompt 抽卡产物**,**绝不能用霜见的人物图**(脸/姿态会污染整组风格)

---

## 为什么不能用 R1 锚点图当 sref

R1 是"风格 + 霜见这个具体主体"的混合产物。拿它当 sref,她的脸、侧身姿态、冷艳情绪会作为视觉指纹注入每一张图 → 主体污染。**锁脸是 oref 的活,锁风格是 sref 的活,分开。**

---

## 候选 A · 静物(推荐 — 配色还原最准)

```
Museum level still life fine art photography, a woven bamboo douli hat and a sheathed sword resting on a weathered dark wood table, a coil of crimson silk cord and a pale jade pendant beside them, a folded moon-white silk cloth, a misty bamboo grove softly blurred behind, large negative space, clean minimal composition, soft directional light, 35mm film, deep shadow gradient, cool moon white and deep ink black tones with one crimson accent, Vogue China editorial style, cinematic still, fine art photography --no text, watermark, logo, blurry, people --ar 1:1 --raw --hd
```

物件(斗笠/剑/玉佩/月白绸)是器物类,形态中性,同时把**月白+墨黑+朱砂红**配色和胶片质感编进风格指纹。`--no people` 防止 MJ 自作主张加人。

## 候选 B · 空镜(最中性,配色略弱)

```
Museum level fine art landscape photography, a misty bamboo grove at dawn, tall green grey bamboo stalks, shafts of soft cool light through fog, a few fallen leaves on stone, large negative space, clean minimal composition, no people, 35mm film, deep shadow gradient, cool moon white and ink blue green tones, Vogue China editorial style, cinematic still, fine art photography --no text, watermark, logo, blurry, people --ar 3:4 --raw --hd
```

最干净的风格指纹,但少了月白/朱砂红的服装配色。

---

## 工作流

1. **两条都抽 4-8 张**,纯 prompt,**不加任何 --sref / --oref**。
2. **选锚点**:挑调色/胶片质感最像 R1、且构图最干净中性的那张。优先候选 A(配色全)。
3. 选中图存入 `03_出图记录/R2_sref锚点/`,**标注"专用于提 sref,不作他用"**。
4. **挂 sref**:在编辑器**点击该图**设为 style reference,UI 调权重(不写 `--sref url`,见 [[oref与sref的工具版本与挂载方式]])。
5. 之后**每一张霜见**= `风格关键词 + 描述词锁定(斗笠+月白+墨黑+红绳玉佩) + 场景`,在 UI 挂 sref(锁脸时再挂 oref,切 v7)。

## 关联

- 铁律:[[sref纯净性原则]] · [[sref编号独立律]]
- 金字塔:[[角色一致性金字塔]]
- 角色卡:`../01_角色卡/霜见_角色卡_v0.1.md`
