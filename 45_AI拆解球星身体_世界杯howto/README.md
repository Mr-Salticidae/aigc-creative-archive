# 45_AI拆解球星身体_世界杯howto

小红书「世界杯聊个球 · howto拥有球星同款好状态」活动参赛项目。

- **活动周期**：2025/6.10 – 7.20
- **账号定位**：AI创作 / 科技向
- **核心目标**：涨粉
- **形式**：AI图文为主
- **栏目名**：【AI拆解球星身体】— 用AI把球星的好状态"拆开"讲，一篇=1球星+1维度+清新信息图
- **打法**：单篇试水 → 看数据(收藏率/涨粉/评论点名) → 决定是否按五周计划加码

---

## 当前进度
| 期数 | 选题 | 状态 |
|---|---|---|
| 01 | 睡眠篇（达芬奇睡眠法 vs C罗R90） | ✅ 封版，待发布 |
| 02 | 夜醒篇（睡得浅/半夜醒/睡不着 × C罗R90周期+恢复舱） | ✅ 物料齐，待发布 |
| 03 | 待定（看01/02数据 / 评论点名决定） | ⬜ |

发布物料：01期见 `00_发布物料/`；02期见 `00_发布物料/02_夜醒篇/`（含4图+文案）。
图生成脚本见 `06_脚本/`（正文图纯PIL精绘，可复用调参）。

---

## 视觉规范（保持栏目统一）
- **配色**：奶油底 `#EFEBDF` ｜ 墨青主色 `#23423F` ｜ 暖珊瑚强调 `#D8643A` ｜ 青绿 `#1D7A68` ｜ 灰青文字 `#606E6C`
- **字体**：标题 微软雅黑粗体(msyhbd) ｜ 正文 微软雅黑(msyh)
- **元素**：左上角栏目胶囊标签「AI拆解球星身体 · 01」；封面"设问→反转"双层标题；正文一页一概念、大数字居中
- **风格基底**：MJ v8.1 清新极简编辑插画风（明亮、留白、不暗调）— prompt见下

### 封面/插画 MJ prompt（清新编辑插画风 · 已验证可用）
```
clean minimal editorial illustration, side view of a football player sleeping calmly with soft rounded shapes, a smooth glowing sleep-cycle curve flowing above showing five gentle 90-minute arches, flat vector style, bright cream white fresh mint and sky-blue palette, soft even lighting, generous negative space, modern friendly health-tech aesthetic, large clean title area at top --ar 3:4 --style raw --v 8.1 --no dark background, black, navy night, neon, cyberpunk, heavy shadows, text, logo, watermark, realistic photo
```
> 信息图（对比图/数据图）不走MJ — 用脚本精确绘制，保证中文与数据准确。

### 封面底图 MJ prompt · 第02期夜醒篇（已验证可用，水彩睡眠周期款）
```
soft watercolor gouache editorial illustration, an athlete sleeping peacefully on their back with a calm serene face, head resting in the lower corner of the frame, a single luminous sleep-cycle line flowing upward and across the sky with several gentle undulating peaks and valleys like ocean swells, translucent misty flowing shapes rising softly, muted palette of warm cream ivory background sage teal soft mint and pale sky-blue with one delicate glowing coral accent on the curve, airy painterly texture, soft even daylight, very generous negative space across the entire top third for a title, modern premium friendly health aesthetic --ar 3:4 --style raw --v 8.1 --no dark background, black, navy night, neon, cyberpunk, heavy shadows, harsh contrast, text, letters, logo, watermark, realistic photo, cluttered
```
> 出图后存 `01_素材_AI原图/`，再用 `06_脚本/gen_ep02_封面_mj.py` 叠双层标题（标题落左上留白区）。后续各期可复用此底图母题。
> **构图经验**：底图人物若在某下角，标题放**对角**那一侧（如人物右下→标题左上），形成对角平衡、避免"文字+人物同侧偏沉"；镜像底图让人物**脸朝向标题**还能引导视线。第02期即采用「水平镜像+标题左上」。

---

## 选题库（四维度对应活动四张卡）
| 活动卡片 | 球星锚点 | 硬核记忆点 |
|---|---|---|
| 超强肌肉 | C罗 | 瘦弱少年→足球史标志身材；训练+饮食+恢复三角 |
| 超强代谢 | 莫德里奇 | 39岁"代谢年龄<30"；一年训练350天 |
| 超强代谢 | 梅西 | 戒披萨/汽水改三文鱼+全谷物，瘦3kg状态封神 |
| 不老引擎 | C罗/莫德里奇 | C罗"37岁23岁身体"；睡眠是头号工具 |
| 极速修复 | C罗/范迪克 | C罗自建冷冻室；范迪克桑拿+冰浴+控息 |
| 睡眠专题★ | C罗 | R90法(5×90分钟)，对照达芬奇睡眠法 ← 第01期 |

## 五周排期（备用，按数据触发）
- 第1周：睡眠法★ / 超强肌肉(C罗)
- 第2周：超强代谢(莫德里奇) / 球星同款餐(梅西)
- 第3周：极速修复 / 不老引擎
- 第4周：四维度合集 / 呼声最高维度的实操版
- 第5周：爆款返场 / 世界杯收官总结

## 合规红线
- 不医疗化（不说治疗/根治/降三高）
- 数据标注来源（教练/媒体说法，非医学结论）
- 落点放"普通人可借鉴的安全版"，不鼓动照搬极端做法
