# 《众》首帧 MJ 提示词 v1（按 v3 六拍 · 媒介熔解阶梯）

> 工具：MidJourney（出静态首帧）→ 可灵 Kling 3.0（图生视频）
> 对应：`00_立项与待决问题/立项文档.md` v3 的 6 拍 / L0–L3 熔解阶梯
> 共用参数：`--ar 16:9 --style raw`；统一 `--no text, watermark, signature, 3d render, plastic sheen, modern logos`

## ✅ 签名已锁：纱影/织物透光（2026-06-23）
全片皮影镜签名词由「leather filigree」改为 **`gauze and woven translucent textile shadow puppet`**（经纬/网纱透光、暖白底、赭褐+琥珀单色、斗笠长袍、平面背光剪影）。
**锚 A = `成图/Frame2聚集_锚A候选01_纱影签名.png`**；后续 L0/L0′/L1 镜一律挂 `--sref <锚A图URL> --sw 80`。下方各条 prompt 的 `leather`/`filigree perforated` 字样按此替换为 `woven/gauze translucent textile`。

## 双 sref 锁法（开工前）
- **锚 A＝皮影签名**（锁 Frame 1/2/3/6）：先抽 **Frame 2「聚集」** 当 hero，复制图 URL → 其余 L0/L1 镜加 `--sref <A> --sw 80`。
- **锚 B＝近实·媒介余烬**（锁 Frame 4/5）：抽一张 Frame 4 当 hero → `--sref <B>`，并叠 `--sref <A> --sw 30` 保皮影 DNA。
- 渡变两帧（Frame 3、6）各多抽 8–12 张挑中间态。
- 全片 `--stylize 200`（渡变/命题/爆发帧抬到 220），`--chaos 6`（渡变帧 12）。

---

### Frame 1 — 第1拍 L0｜古代·平凡孤独的人
```
Chinese shadow puppet theater pi ying xi, a single ordinary plain commoner in strict flat 2D profile, not a hero, slightly lonely and unremarkable, translucent ochre-red tanned hide puppet, modest filigree perforated robe glowing faintly where lantern light passes through, articulated rod-puppet joints, standing small in a vast empty glowing warm-cream cloth screen, soft candle-flicker backlight, limited palette warm cream + amber + ochre red + subtle gold-leaf, high contrast silhouette, generous negative space, hand-crafted folk-art leather texture, museum quality --ar 16:9 --style raw --stylize 200 --chaos 6 --no text, watermark, signature, 3d render, plastic sheen, modern logos
```
🌀 可灵钩子：`articulated rod-puppet joints` + 站姿留白 → 颈肩极小幅、轻轻一动，孤独的呼吸感。

---

### Frame 2 调密版 — 第2拍 L0｜聚集（人海汇拢，挂锚A）★现在抽这张
> 首抽那张(锚A)是行进队列、当第1拍用；第2拍要的是"四面汇拢叠成一片人海"的密度。挂 `--sref <锚A图URL> --sw 80` 锁签名。
```
Chinese shadow theater, gauze and woven translucent textile shadow puppets, a huge dense crowd of ordinary plain commoners in conical hats and long robes converging from all directions and piling into one single packed mass, a living human sea filling the entire frame, overlapping translucent silhouettes layered many rows deep with no gaps, warm amber backlight glowing through a woven cloth screen, sepia and ochre monochrome, flat 2D backlit silhouettes, fine mesh net translucency showing through the bodies, articulated rod-puppet hint, atmospheric, museum quality --ar 16:9 --style raw --stylize 200 --chaos 6 --sref <锚A图URL> --sw 80 --no text, watermark, signature, 3d render, plastic sheen, modern logos
```
🌀 可灵钩子：`converging from all directions and piling into one mass` → 人从四面汇拢、叠成一片的小幅同向运动。

---

### Frame 2（原案·行进队列）— 已转用作第1拍/锚A参考
```
Chinese shadow puppet theater pi ying xi, many ordinary plain commoners as flat 2D profile puppets converging from all sides into a single dense crowd, a living mass forming, overlapping translucent amber and ochre-red dyed hide, filigree perforated robes glowing as lace, articulated rod-puppet joints gradually aligning into one direction, warm lantern backlight, glowing translucent cloth screen, limited palette warm cream + amber + ochre red + gold-leaf, high contrast silhouettes, wide shot, hand-crafted folk-art leather texture, museum quality --ar 16:9 --style raw --stylize 200 --chaos 6 --no text, watermark, signature, 3d render, plastic sheen, modern logos
```
🌀 可灵钩子：`converging from all sides into a single dense crowd` + `joints gradually aligning` → 平凡人从四面汇拢、签杆趋同的小幅同向运动。

---

### Frame 3 — 第3拍 L1｜呐喊·渡变①（皮影→现代）【难·多抽】
```
Chinese shadow puppet theater pi ying xi mid-transformation into flesh, a roaring crowd caught at the exact moment the flat leather silhouettes begin growing volume, cut-leather edges softening into half-three-dimensional bodies, translucent ochre-red hide flushing with living blood-red, stadium floodlight glow bleeding through the cloth screen from behind, open shouting mouths held unchanged across the morph, front rows nearly fleshed while back rows still pure shadow puppet, articulated rod joints dissolving into real shoulders, limited palette warm cream + amber + ochre red + gold-leaf, high contrast, hand-crafted leather texture melting into skin, museum quality --ar 16:9 --style raw --stylize 220 --chaos 12 --no text, watermark, signature, 3d render, plastic sheen, modern logos
```
🌀 可灵钩子：`flat silhouettes begin growing volume` + `front rows fleshed, back rows still shadow` + `mouths held unchanged` → 喂可灵"皮影长出血肉，从前排推向后排，背光与口型不变"，一镜完成古→今。

---

### Frame 4 — 第4拍 L2｜足球现场·近实带媒介余烬（抽这张做 hero / 锚B）
```
A modern World Cup stadium at night, packed terraces of cheering fans, floodlights, giant screen, sweeping tifo, mostly realistic and alive, yet a faint translucent amber ghost-grain floats over the whole frame, every figure carries a soft backlit rim, the faint warp-and-weft texture of a cloth screen still ghosts behind everything, the medium not fully shed, warm amber and ochre-red color cast, cinematic wide shot, limited warm palette with gold-leaf glints, atmospheric haze, museum quality --ar 16:9 --style raw --stylize 220 --chaos 8 --no text, watermark, signature, 3d render, plastic sheen, modern logos
```
🌀 可灵钩子：`packed terraces of cheering fans` + `tifo sweeping` → 现代看台小幅群动 + tifo 翻涌，可灵稳。

---

### Frame 5 — 第5拍 L3｜特写·所有人都是主角·提线重现【命题镜·孔雀蓝冷点】
```
Modern realistic close-ups of ordinary football fans each as a protagonist, an old supporter, a child, a person who came alone, then a player, intercut as equals, then the camera pulls back to reveal a thin control rod has risen above every single head, the rods interconnect across the whole crowd with no single puppeteer anywhere, the hand working the player is the crowd and the hand working the crowd is the player, the shadow-puppet world quietly reclaiming them, one cold peacock-blue accent glowing among the warm tones to mark the reveal, faint amber ghost-grain and backlit rims, limited warm palette + one peacock-blue note, quiet composition, museum quality --ar 16:9 --style raw --stylize 220 --chaos 8 --no text, watermark, signature, 3d render, plastic sheen, modern logos
```
🌀 可灵钩子：`camera pulls back to reveal thin rods above every head` + `rods interconnect` → 镜头后退、签杆上浮并相连（慢速单向揭示），把"所有人都是主角／互为提线"在动态里揭出来。

---

### Frame 6 — 第6拍 L0′｜胜利呐喊·渡变②（现代→皮影蹴鞠）·首尾呼应【难·多抽】
```
Chinese shadow puppet theater pi ying xi reclaiming reality, a victorious roar at the exact moment realistic fans flatten back into backlit translucent leather silhouettes, scarves lifting off and turning into a flock of cut-leather silhouette birds sweeping across the cloth screen, the whole mass condensing into one single ancient filigree-carved leather cuju ball hanging quietly on the glowing screen, lantern backlight fading toward the opening shot, flesh dissolving back into ochre-red hide, limited palette warm cream + amber + ochre red + gold-leaf, high contrast silhouette, hand-crafted folk-art leather texture, ring composition echoing the first frame, museum quality --ar 16:9 --style raw --stylize 220 --chaos 12 --no text, watermark, signature, 3d render, plastic sheen, modern logos
```
🌀 可灵钩子：`realistic fans flatten back into leather silhouettes` + `condensing into one cuju ball` + `birds sweeping` → 喂可灵"血肉拍扁成皮影、围巾化飞鸟、最后凝成一只蹴鞠"，收回 L0、与首帧咬合。

---

## 抽帧顺序建议
1. 先 **Frame 2**（锚 A）→ 锁皮影签名。
2. **Frame 4**（锚 B，叠 A 的 sw30）→ 锁近实余烬。
3. 再出 Frame 1 / 5 / 3 / 6；**Frame 3、6 多抽挑中间态**。
4. 6 张静态占位 → 排 80s 节奏粗剪 → 可灵分段图生视频（逐级 L0→L1→L2→L3→L0′）。
