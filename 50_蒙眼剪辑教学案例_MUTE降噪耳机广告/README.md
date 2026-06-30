# 50 · 蒙眼剪辑教学案例《MUTE 静默》降噪耳机广告

> 立项：2026-06-30 ｜ 类型：教学素材 / 模拟商业广告

## 这是什么

一支**模拟商业广告**，作为「**蒙眼剪辑法 × Remotion 自动剪辑**」的**教学案例**。
最终产出是**授课逐字稿**（由跳蛛先生 decode），本立项负责提供 **encode 底料**。

- **虚构标的**：MUTE 静默 · 主动降噪耳机（"把世界调成静音"）
- **规格**：竖屏 1080×1920 · 20s · 30fps · 商业广告片种
- **教学杠杆**：题材（卖安静）= 方法论命门（音频先行）。案例自我印证。

## 分工（encode / decode）

依据 [[语言的Encoder-Decoder模型]]：encode 可交 AI，decode（声音）不可外包。

| 阶段 | 内容 | 负责 | 状态 |
|---|---|---|---|
| encode 前半 | Step 1–4：图文 / 风格 / BGM / 剪辑草案 | Claude | ✅ 完成（v1） |
| 审核 | 4.3 审核清单的审美裁决 | 跳蛛先生 | ⬜ 待办 |
| decode | 把 encode 解压成授课逐字稿 | 跳蛛先生 | ⬜ 待办 |
| encode 后半（可选） | Step 5–6：Remotion 代码 / 渲染 / 迭代 | Claude 可辅助 | ⬜ 未启动 |

## 文件

- [`案例编码_encode_v1.md`](案例编码_encode_v1.md) — **主交付物**。Step 1–4 全文，每步带"教学锚点"，含第 5 节"哪一步讲什么"拆解索引、第 6 节交接边界。

## 素材台账

| 素材位 | 文件 | 状态 | 备注 |
|---|---|---|---|
| product_hero_01 | [`素材/产品图/product_hero_01_A1母本.png`](素材/产品图/product_hero_01_A1母本.png) | ✅ 锁定（2026-06-30） | **全案产品一致性锚点**。A1 极简悬浮方向，月白哑光壳+雾灰耳垫+圆形静音键 |
| product_detail B1 静音键 | [`素材/产品图/product_detail_B1_静音键微距.png`](素材/产品图/product_detail_B1_静音键微距.png) | ✅ 锁定（gpt-image-2 身份参照） | 母题物件特写 |
| product_detail B2 接缝 | [`素材/产品图/product_detail_B2_材质接缝.png`](素材/产品图/product_detail_B2_材质接缝.png) | ✅ 锁定（gpt-image-2 身份参照） | 香槟金转轴+alcantara |
| 手按静音键（A3） | [`素材/产品图/product_A3_手按静音键.png`](素材/产品图/product_A3_手按静音键.png) | ✅ 锁定（Nano 编辑式） | DROP 动作素材，守住产品本体 |
| 产品展出·分镜两帧 | 首帧=[A1母本](素材/产品图/product_hero_01_A1母本.png)；尾帧=[尾帧静音键收势](素材/产品图/product_showcase_尾帧_静音键收势.png) | ✅ 分镜锁定 | 首尾帧路线（KB 已记录）。两帧定义运镜 |
| 产品展出·Seedance 动画 | — | 🔜 待跑 | Seedance 2.0 首尾帧，5s，A1→尾帧 缓慢环绕+收推，定格静音键 |
| 噪音可视化四波（段②） | — | ⬜ 待建（我） | flat-vector，Remotion 程序化，密度贴 backbone_v3 四波能量。encode 后半 |
| 黑屏 endcard（段④） | — | ⬜ 待建（我） | Remotion 纯文字：大标题 MUTE 静默 + logo(静音键 glyph 矢量重画) + slogan |
| BGM bed1 噪音build | [`素材/音频/bed1_噪音build.wav`](素材/音频/bed1_噪音build.wav) | ✅ 抽定（Suno，159.76s 取段用） | 爬升→急停边沿在内部 7.5–9.0s |
| BGM bed2 回暖calm | [`素材/音频/bed2_回暖calm.wav`](素材/音频/bed2_回暖calm.wav) | ⊘ 弃用 | 决定让结尾自然死寂留白，不用回暖（"卖安静"不该用音乐填满静默） |
| **音频骨架 backbone** | [`素材/音频/backbone_v3.wav`](素材/音频/backbone_v3.wav) | ✅ **锁定（最终时间脊梁）** | 33.5s。bed1 完整四波爬升→~29.5s 自然塌陷成死寂(30.0s=0.0000)→3.5s 纯静默留白(黑屏+品牌文案)。无 bed2、无 beep |

## 方法论来源

- [[蒙眼剪辑法_方法论笔记]]（v4，6 步闭环）
- [[短视频批量分发方案_蒙眼剪辑法xRemotion_v1]]（Remotion 数据驱动）
- [[2026-06-26_反诈柜台短视频pilot从0到1复盘]]（唯一已跑通的成片管线）
- [[语言的Encoder-Decoder模型]]（encode/decode 分工依据）
- skill：`blind-editing-workflow` / `remotion-skill`
