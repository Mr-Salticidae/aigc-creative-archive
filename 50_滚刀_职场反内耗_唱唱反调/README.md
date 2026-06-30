# 50_滚刀_职场反内耗_唱唱反调

小红书「唱唱反调」活动参赛项目 · 话题赛道 **# 不吃压力之人**。

- **账号定位**:AI创作 / 科技向(视觉延续 45_AI拆解球星身体 的水彩编辑插画人设)
- **核心反调命题**:面对烂老板/同事,主流答案是「改变自己」或「对抗/离开」;我唱反调——**主动变成一块"滚刀肉"**(油盐不进的软抵抗),用战术性装笨化解控制欲,反而不内耗。
- **形式**:AI 水彩封面 + PIL 论证式正文卡,共 9 图。

---

## 成品(00_发布物料/)
| 图 | 内容 | 来源 |
|---|---|---|
| 1_封面 | 设问→反转双层标题压在 B 水彩底图上 | MJ 底图 + `gen_封面.py` |
| 2~9 正文 | 共鸣→主流答案→我的反调→怎么操作→往深挖→理论撑腰①②→边界&金句 | 纯 PIL 精绘 `gen_正文卡.py` |

文案见 `00_发布物料/发布文案.md`。

## 哲学骨架(有理有据 / 浅入深出)
1. 内耗根源是「当真」——违心服从=被迫认同→认知失调;滚刀把关系降格为可掌控的表演,撕裂感消失。
2. James C. Scott《弱者的武器》——日常反抗(磨洋工/装糊涂/假顺从)。
3. 庄子《人间世》「无用之用」——朽木不可雕是保命智慧。
4. 阿德勒「课题分离」(《被讨厌的勇气》)——把别人的期待还给别人。
5. 边界:装笨只对付"控制欲",不对付真该学的本事,否则是自欺。

---

## 视觉规范(沿用账号栏目)
- **配色**:奶油底 `#EFEBDF` ｜ 墨青主色 `#23423F` ｜ 暖珊瑚强调 `#D8643A` ｜ 灰青文字 `#606E6C`
- **字体**:标题 微软雅黑粗体(msyhbd) ｜ 正文 微软雅黑(msyh)
- **元素**:左上珊瑚点+kicker小标、右上 `0X/08` 页码、标题下珊瑚短线、底部活动 footer
- **封面**:水彩底图人物落右下 → 标题占左上对角留白 + 左上奶油护字渐变(不洗插画)
- **风格基底**:MJ v8.1 水彩水粉编辑插画(明亮留白不暗调)

### 封面底图 MJ prompt(B 版 · 已验证可用)
```
soft watercolor gouache editorial illustration, a person reclining calmly and lazily cushioned inside a soft billowing cloud in the lower corner of the frame, serene unbothered expression, a heavy force pressing down from above quietly melting and dissolving into mist before it can reach them, translucent flowing shapes rising softly, muted palette of warm cream ivory background sage teal soft mint with one delicate glowing coral accent, airy painterly texture, soft even daylight, very generous negative space across the top third for a title, modern premium friendly aesthetic --ar 3:4 --style raw --v 8.1 --no dark background, black, navy night, neon, cyberpunk, heavy shadows, harsh contrast, text, letters, logo, watermark, realistic photo, cluttered
```

---

## 出图前自检 checklist
**标点**(账号 house style:逗号/冒号/问号半角、句号/顿号全角,**全篇各类型统一不混用**)
- [x] 逗号全篇半角 `,`;句号全篇全角 `。`;顿号 `、`;冒号半角 `:`;问号半角 `?`
- [x] 无渲染豆腐块(雅黑无彩色 emoji,图内禁 emoji;emoji 只放发布文案)

**版式**
- [x] 文字不出血、不压到看不清的纹理(封面有奶油护字渐变)
- [x] 行末不孤字;封面标题与人物对角平衡
- [x] 页码 `0X/08` 正确;配色用栏目色

**平台/合规**
- [x] 发布框标题 ≤ 20 字(封面图标题不限)
- [x] 不医疗化、不教唆摆烂;明确边界(装笨≠对付本职)

## 待办 / 复盘
- ⬜ 发布后看数据(点赞率 >3% 为佳),决定是否做成「唱唱反调」系列
- ⬜ 满意封面底图记 sref,后续同系列复用统一水彩基调
