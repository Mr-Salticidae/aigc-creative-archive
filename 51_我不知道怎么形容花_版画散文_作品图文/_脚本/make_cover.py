# -*- coding: utf-8 -*-
"""亮色编辑风封面:把版画原作放进杂志式版式(代码排版,非直接上原图)。
改 ART / OUT / 三处文案即可复用。路径相对本项目根。"""
import os
from PIL import Image, ImageDraw, ImageFont

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

W, H = 1080, 1440
PAPER = (243, 237, 223)      # 亮暖纸底
INK   = (20, 36, 29)         # 近黑深绿(标题)
GREEN = (29, 74, 58)         # 版画墨绿(边框/分隔线/kicker)
MUTE  = (123, 122, 104)      # 灰调(小字)

# 选定:骷髅花器版;备选:原图_01_少女抱花束.png
ART = os.path.join(ROOT, "01_素材原图", "原图_06_骷髅花器抱蔫花.png")
OUT = os.path.join(ROOT, "02_成品封面", "封面_骷髅花器版_选定.png")

KICKER = "VINTAGE POSTER · 情绪散文当 PROMPT"
TITLE  = "我不知道该怎么形容花"
SUB    = "于是 AI 替我画了出来"

F_SONG = "C:/Windows/Fonts/simsun.ttc"   # 宋体
F_HEI  = "C:/Windows/Fonts/simhei.ttf"   # 黑体
F_KAI  = "C:/Windows/Fonts/simkai.ttf"   # 楷体

def font(p, s): return ImageFont.truetype(p, s)
def text_w(d, s, f):
    b = d.textbbox((0,0), s, font=f); return b[2]-b[0]
def draw_tracked(d, cx, y, s, f, fill, track):
    widths = [text_w(d, ch, f) for ch in s]
    total = sum(widths) + track*(len(s)-1)
    x = cx - total/2
    for ch, w in zip(s, widths):
        d.text((x, y), ch, font=f, fill=fill); x += w + track

img = Image.new("RGB", (W, H), PAPER)
d = ImageDraw.Draw(img)

m = 26
d.rectangle([m, m, W-m, H-m], outline=GREEN, width=2)
draw_tracked(d, W/2, 70, KICKER, font(F_HEI, 22), GREEN, 6)

art = Image.open(ART).convert("RGB")
ar = art.width/art.height
art_h = 980; art_w = int(art_h*ar)
art_rs = art.resize((art_w, art_h), Image.LANCZOS)
ax = (W-art_w)//2; ay = 120
mat = 14
d.rectangle([ax-mat-3, ay-mat-3, ax+art_w+mat+3, ay+art_h+mat+3], fill=(250,247,238), outline=GREEN, width=3)
img.paste(art_rs, (ax, ay))

ry = ay + art_h + mat + 40
d.line([(W/2-150, ry), (W/2+150, ry)], fill=GREEN, width=2)
draw_tracked(d, W/2, ry+34, TITLE, font(F_SONG, 58), INK, 4)
draw_tracked(d, W/2, ry+34+82, SUB, font(F_KAI, 30), MUTE, 6)

img.save(OUT, quality=95)
print("saved:", OUT, img.size)
