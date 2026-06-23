# -*- coding: utf-8 -*-
"""梦游困境云海 — 作品图文封面 (题跋式排版 · 亮调版)
排版样式参考 46_牧云人 封面母版(竖排宋体主标 + 楷体题跋副标 + 拉丁落款 + 压角保高光 + 柔投影 + 2×超采样),
但品牌/标题/落款全部为本作品自有,不含"牧云人"字样。
关键适配:原图是亮粉彩(非雾山暗调),配色反转——深墨字 + 浅米光晕 + 极轻提亮压角,保住云海高光与治愈感。
文字进左上天空负空间,不压主体(人在中、楼梯在右)。
用法:py make_cover.py 依赖:pip install Pillow (numpy 可选)
"""
import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageChops

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(BASE, "01_素材原图", "原图_梦游困境云海.png")
OUT = os.path.join(BASE, "02_成品封面", "梦游困境_作品封面.png")
TRIM_BOTTOM = 0.0

# —— 本作品自有文案(非牧云人品牌)——
HERO   = "梦游"                    # 竖排主标题
SUB1   = "云上无晨昏"              # 楷体题跋·上句
SUB2   = "梦里再走一程"            # 楷体题跋·下句
SIGN_EN = "ABOVE THE CLOUDS"       # 拉丁落款
SIGN_CN = "《梦游困境》"           # 中文落款(作品题名)

W, H = 1080, 1440           # 3:4
SS = 2
w, h = W * SS, H * SS

FONTS = r"C:\Windows\Fonts"
f_song = lambda s: ImageFont.truetype(os.path.join(FONTS, "simsun.ttc"), s)
f_kai  = lambda s: ImageFont.truetype(os.path.join(FONTS, "simkai.ttf"), s)
f_lat  = lambda s: ImageFont.truetype(os.path.join(FONTS, "Dengl.ttf"), s)

INK   = (52, 56, 70)        # 深石板蓝墨
INK2  = (96, 100, 116)
HALO  = (252, 250, 246)     # 浅米光晕

im = Image.open(SRC).convert("RGB")
if TRIM_BOTTOM:
    im = im.crop((0, 0, im.width, int(im.height * (1 - TRIM_BOTTOM))))
sw, sh = im.size
scale = max(w / sw, h / sh)
im = im.resize((int(sw * scale), int(sh * scale)), Image.LANCZOS)
x0 = (im.width - w) // 2
y0 = (im.height - h) // 2
im = im.crop((x0, y0, x0 + w, y0 + h)).convert("RGBA")

def corner_bloom(cx, cy, rx, ry, amax):
    try:
        import numpy as np
        yy, xx = np.mgrid[0:h, 0:w]
        d = ((xx - cx) / rx) ** 2 + ((yy - cy) / ry) ** 2
        a = np.clip(1 - d, 0, 1) ** 1.7 * amax
        return Image.fromarray(a.astype("uint8"), "L")
    except Exception:
        layer = Image.new("L", (w, h), 0); px = layer.load()
        for yv in range(0, h, 2):
            for xv in range(0, w, 2):
                d = ((xv - cx) / rx) ** 2 + ((yv - cy) / ry) ** 2
                px[xv, yv] = int(max(0.0, 1 - d) ** 1.7 * amax)
        return layer

bloom = Image.new("RGBA", (w, h), (255, 253, 248, 0))
m  = corner_bloom(40 * SS, 60 * SS, 700 * SS, 720 * SS, 70)
m2 = corner_bloom(60 * SS, h, 620 * SS, 320 * SS, 58)
bloom.putalpha(ImageChops.lighter(m, m2))
im = Image.alpha_composite(im, bloom)

txt = Image.new("RGBA", (w, h), (0, 0, 0, 0))
d = ImageDraw.Draw(txt)
S = SS

def vtext(x, y_start, chars, font, fill, step):
    yy = y_start
    for ch in chars:
        if ch == " ":
            yy += step; continue
        d.text((x, yy), ch, font=font, fill=fill, anchor="mm")
        yy += step

# 主标题 竖排宋体 左上
vtext(150 * S, 240 * S, HERO, f_song(150 * S), INK, step=185 * S)
# 细竖分隔线(高度随题跋副标,取较高者)
d.line([(232 * S, 168 * S), (232 * S, 600 * S)], fill=INK2 + (130,), width=2 * S)
# 副标楷体竖排(落款式题跋)
vtext(286 * S, 252 * S, SUB1, f_kai(40 * S), INK2, step=52 * S)
vtext(286 * S, 252 * S + (len(SUB1) + 1) * 52 * S, SUB2, f_kai(40 * S), INK2, step=52 * S)
# 左下落款
d.line([(72 * S, 1318 * S), (150 * S, 1318 * S)], fill=INK2 + (170,), width=2 * S)
def tracked(x, y, s, font, fill, tr):
    for ch in s:
        d.text((x, y), ch, font=font, fill=fill); x += d.textlength(ch, font=font) + tr
tracked(72 * S, 1338 * S, SIGN_EN, f_lat(27 * S), INK + (220,), 7 * S)
d.text((72 * S, 1384 * S), SIGN_CN, font=f_kai(27 * S), fill=INK2 + (200,))

# 浅米光晕(替代暗投影)
alpha = txt.split()[3]
halo = Image.new("RGBA", (w, h), HALO + (0,))
halo.putalpha(alpha.point(lambda v: int(v * 0.55)))
halo = halo.filter(ImageFilter.GaussianBlur(6 * S))

base = im.copy()
base.alpha_composite(halo)
base.alpha_composite(txt)

out = base.convert("RGB").resize((W, H), Image.LANCZOS)
os.makedirs(os.path.dirname(OUT), exist_ok=True)
out.save(OUT, quality=95)
out.resize((360, 480), Image.LANCZOS).save(os.path.join(BASE, "_脚本", "preview.jpg"), quality=90)
print("saved", OUT, out.size)
