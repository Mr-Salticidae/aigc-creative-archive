# EP01 SCARLATTA · prompt 复现 + 合成说明

> 留档目的：下次出同角色不同光、或六角色统一风时可直接复用。
> 成品：`成品/01_SCARLATTA_封面海报.png`（GPT Image 2 合成）。

---

## 一、写实本体 prompt（MJ，反推自原图）

原图特征（`原图/01_SCARLATTA_写实原图.png`，9:16 无字）：深红丝绒头巾斗篷裹头，黑长发，一只手抬在头巾边，另一只手的红尖甲指尖捏着一张**开裂做旧的银白色整脸面具，举在下巴/脖颈侧边**（不遮脸，与脸并置对照），**两只灰眸都露出**直视镜头，眉间一抹红痕，雾蒙蒙的前景虚化，背景是斑驳浅色墙。

> 注意：**海报**（成品）是在此原图基础上裁切重构成"面具上移、遮住下半脸、只露一只眼"的更强构图。原图与海报构图不同，复现时按目标选 prompt。

```
cinematic portrait photography, photorealistic, shot on 85mm, shallow depth of field,
low-key chiaroscuro lighting, desaturated muted film tones, fine film grain, real skin texture,
a young east-asian woman wrapped in a deep crimson velvet hood, one hand raised at the hood's edge,
long straight black hair falling past her shoulders, both pale grey eyes gazing straight at the viewer,
a small red brushstroke mark on her brow, her other hand with sharp red painted nails
holding a cracked weathered silver-white full-face mask beside her chin, the mask juxtaposed against her face,
ritualistic judgmental mood, soft misty foreground blur, mottled pale wall background, vertical portrait
--ar 9:16 --style raw --stylize 150 --no illustration,anime,cartoon,3d render,cgi,plastic skin,smooth airbrushed skin,oversaturated,deformed hands,extra fingers,watermark
```

> **海报构图变体**（面具上移遮下半脸、只露一只眼）：把上面两句换成 `holding a cracked silver mask to the lower half of her face, only one pale grey eye revealed`，并改 `--ar 3:4`。

### Layer 拆解（便于改期/换光）
- **Layer 1 身份锁（别动）**：crimson velvet hood / black long hair / cracked silver-white mask held in hand / grey eyes / red nails / red brow mark
- **Layer 2 写实色调（锁色）**：low-key chiaroscuro / desaturated film tones / crimson + cold silver / film grain
- **Layer 3 构图变量（可换）**：景别、举面具的角度、看向镜头 or 看向画外、前景雾的浓淡

---

## 二、封面海报合成（GPT Image 2）

在写实本体上叠加文字与装饰层，合成 3:4 竖版海报：

**版式元素（对照成品）：**
- 左上角：IP 之眼 logo + `01 · THE GAZE`
- 右侧竖排：`THE GAZE`（英文竖排描边）
- 主标题：`SCARLATTA` 银色衬线大字 + `斯卡拉塔`
- 称号：`他者`（大字）
- 副标：`JUDGMENTAL GAZE · 看穿伪装`
- 底部独白：`我用这副面具，看清了所有摘下面具的人。` / 斜体英文 `Behind this mask, I see yours fall.`
- 边框：暗色描边 + 四角星点/藤蔓裂纹装饰（系列统一视觉语言）

**合成 prompt 要点（GPT Image 2）：**
```
将这张写实人像合成为暗黑唯美电影海报，3:4 竖版。
保留人物不变。叠加：左上角小标"01 · THE GAZE"+眼睛logo；
主标题银色衬线大字"SCARLATTA"下方"斯卡拉塔"；称号"他者"；
副标"JUDGMENTAL GAZE · 看穿伪装"；底部两行独白
"我用这副面具，看清了所有摘下面具的人。"与斜体英文"Behind this mask, I see yours fall."；
暗色边框+四角星点与裂纹藤蔓装饰；银红配色，做旧颗粒。
```
> 中文字形由 GPT Image 2 保证。若个别字崩，重抽或局部重绘。

---

## 三、复现注意
- 红痕、红甲、银裂面具是 SCARLATTA 的"指纹"，三者缺一就不是她。
- 面具必须**她自己手持**（主动凝视的隐喻），不能挂脸上或别人递。
- 出系列统一风时：固定一个暗调 `--sref`，SCARLATTA 用其专属基准脸 `--cref`。
