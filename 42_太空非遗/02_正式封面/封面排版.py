# -*- coding: utf-8 -*-
# 《太空非遗》六联图集封面排版 — 底图: 06_皮影_太阳幕布.png
from PIL import Image, ImageDraw, ImageFont, ImageFilter

BASE = r"D:\AIGC工作站\42_太空非遗"
FONTS = r"D:\AIGC工作站\字体"

im = Image.open(rf"{BASE}\06_皮影_太阳幕布.png").convert("RGBA")
W, H = im.size

# ---- 轻渐变压暗底部文字区(skill 规则:没有留白就用暗部+轻渐变) ----
grad = Image.new("L", (1, H), 0)
for y in range(H):
    t = (y / H - 0.72) / 0.28          # 0.72H 开始渐入
    a = max(0.0, min(1.0, t)) ** 1.5 * 150
    grad.putpixel((0, y), int(a))
shade = Image.new("RGBA", (W, H), (8, 22, 26, 255))
shade.putalpha(grad.resize((W, H)))
im = Image.alpha_composite(im, shade)

# ---- 字体 ----
f_hook  = ImageFont.truetype(rf"{FONTS}\SourceHanSerifSC-Medium.otf", 58)
f_title = ImageFont.truetype(rf"{FONTS}\SourceHanSerifSC-Heavy.otf", 212)
f_sub   = ImageFont.truetype(rf"{FONTS}\SourceHanSerifSC-Regular.otf", 34)

CREAM = (244, 231, 187)   # 暖金米白,取自太阳幕布
WHITE = (235, 230, 215)
SAGE  = (196, 205, 188)

def spaced_width(draw, text, font, spacing):
    w = 0
    for ch in text:
        bb = draw.textbbox((0, 0), ch, font=font)
        w += (bb[2] - bb[0]) + spacing
    return w - spacing if text else 0

def draw_spaced(layer, center_x, top_y, text, font, spacing, fill, glow=None):
    d = ImageDraw.Draw(layer)
    total = spaced_width(d, text, font, spacing)
    x = center_x - total / 2
    if glow:
        gl = Image.new("RGBA", layer.size, (0, 0, 0, 0))
        gd = ImageDraw.Draw(gl)
        gx = x
        for ch in text:
            bb = gd.textbbox((0, 0), ch, font=font)
            gd.text((gx - bb[0], top_y), ch, font=font, fill=glow)
            gx += (bb[2] - bb[0]) + spacing
        gl = gl.filter(ImageFilter.GaussianBlur(18))
        layer.alpha_composite(gl)
        layer.alpha_composite(gl)  # 叠两次加强光晕
    for ch in text:
        bb = d.textbbox((0, 0), ch, font=font)
        d.text((x - bb[0] + 4, top_y + 4), ch, font=font, fill=(8, 22, 26, 160))  # 投影
        d.text((x - bb[0], top_y), ch, font=font, fill=fill + (255,))
        x += (bb[2] - bb[0]) + spacing

txt = Image.new("RGBA", (W, H), (0, 0, 0, 0))

# 第二层:情绪钩子
draw_spaced(txt, W / 2, int(H * 0.795), "千年手艺 · 离地四百公里", f_hook, 14, WHITE)

# 第一层:主标题(带暖光晕,像被太阳幕布照亮)
draw_spaced(txt, W / 2, int(H * 0.832), "太空非遗", f_title, 52, CREAM,
            glow=(242, 200, 120, 110))

# 第三层:系列信息
draw_spaced(txt, W / 2, int(H * 0.942), "复古科幻图集 · 六联", f_sub, 10, SAGE)
d = ImageDraw.Draw(txt)
en = "I N T A N G I B L E   H E R I T A G E   I N   S P A C E"
bb = d.textbbox((0, 0), en, font=f_sub)
d.text(((W - (bb[2] - bb[0])) / 2, int(H * 0.962)), en, font=f_sub,
       fill=SAGE + (190,))

out = Image.alpha_composite(im, txt).convert("RGB")
out.save(rf"{BASE}\封面_太空非遗_FINAL.png", quality=95)
print("done", out.size)
