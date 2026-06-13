# A 系统层 · Remotion 工程

A 层（系统文字、方块溶解、数据可视化）的代码生成层。当前为**风格基底测试合成** `AnomalyStyleTest`，三段验证全片视觉语言。

## 三个场景

| 段 | 帧区间 | 内容 | 验证 |
|---|---|---|---|
| OpeningTitle | 0–240 | 开头字幕，散文档案体逐段浮现 | 暖黄字在黑底的"过期档案"气质 |
| SystemReadout | 240–440 | 系统状态读出，终端逐字打字 + 光标 | 机器冷感、打字节奏 |
| AnomalyDissolve | 440–640 | 方块溶解 + 一个发光红块 + 暖黄系统字 | **四色焊接**：深蓝黑/灰白/暖黄/一点红 |

## 设计要点

- Token 覆盖了卡片流 skill 的默认蓝，换成终端档案暗调（黑底 + 暖黄等宽字）。
- 刻意保留 skill 默认禁止的**扫描线 + 暗角 + 微闪烁**——这是 CRT/终端美学本身，非装饰。
- **红色配给**：`AnomalyDissolve` 里"FAILED"不标红，全帧唯一的红留给那个不肯消散的方块（异常值本体）。
- `seed()` 用 sin 哈希做确定性伪随机，保证逐帧不闪（不可用 `Math.random`）。

## 跑起来

```bash
# 首次：在本目录外建一个 Remotion 项目，把 src/ 拷进去
npx create-video@latest        # 选 Blank
cd <项目> && npm install
# 用本目录的 src/Anomaly.tsx、src/Root.tsx 覆盖项目 src/
npx remotion studio            # 预览，重点看第三段四色焊接
```

预览时可直接调的参数：CRT 扫描线 `opacity 0.5`、暗角 `0.7`、打字速度 `cps`、红块脉冲 `pulse`。

## 验证通过后

- 把这三段拆成正片各章的实际系统屏模板。
- 第四章"偏移"、第五章"不可压缩"、第六章"路径熄灭"都从 `AnomalyDissolve` 演化。
