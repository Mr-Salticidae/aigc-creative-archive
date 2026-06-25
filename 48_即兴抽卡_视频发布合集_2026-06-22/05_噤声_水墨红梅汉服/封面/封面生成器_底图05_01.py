# -*- coding: utf-8 -*-
"""噤声·水墨红梅汉服 —— 封面生成器（底图：重排后 05_01 / 原 05_03）

文字采用「深墨 + 柔光晕」处理：深墨保留水墨气质，字背的浅色光晕负责把字从
杂乱背景里托起来，解决辨识度问题（副标题尤甚）。
"""
import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "..", "原图", "05_01.png")  # 重排后 05_01 即原 05_03（封面底图）
FONT_TITLE = r"C:\Windows\Fonts\STZHONGS.TTF"   # 华文中宋（中粗宋体）
FONT_SUB   = r"C:\Windows\Fonts\STSONG.TTF"     # 华文宋体
FONT_LAT   = r"C:\Windows\Fonts\Dengl.ttf"      # 等线 Light（拉丁字母）

TITLE = "噤声"
SUB_COLS = ["别惊一", "树红梅"]       # 竖排两列，从右往左读
LATIN = "HUSH"

C_TITLE = (26, 30, 28)       # 浓墨黑
C_SUB   = (24, 28, 26)       # 浓墨黑（副标题）
C_LATIN = (224, 221, 213)    # 米白浅灰

# 光晕：(颜色, 模糊半径, 不透明度0-255)
HALO_TITLE = ((244, 240, 232), 9, 200)   # 深字配浅光晕
HALO_SUB   = ((246, 242, 234), 5, 240)   # 副标题光晕更实，托得更稳
HALO_LATIN = ((20, 24, 23), 5, 150)      # 浅字配深光晕，浅背景上也立得住

def load(): return Image.open(SRC).convert("RGB")

def cover_crop(img, ratio, fx=0.5, fy=0.40):
    W, H = img.size
    cur = W / H
    if cur > ratio:
        nw, nh = int(H * ratio), H
    else:
        nw, nh = W, int(W / ratio)
    x0 = max(0, min(W - nw, int(fx * W - nw / 2)))
    y0 = max(0, min(H - nh, int(fy * H - nh / 2)))
    return img.crop((x0, y0, x0 + nw, y0 + nh))

def grade(im, factor=0.93):
    im = ImageEnhance.Brightness(im).enhance(factor)
    im = ImageEnhance.Contrast(im).enhance(1.04)
    return im

def left_scrim(im, width_frac=0.42, strength=70):
    """左侧柔和提亮浅雾，统一文字区底色。"""
    W, H = im.size
    scrim = Image.new("L", (W, H), 0)
    d = ImageDraw.Draw(scrim)
    edge = int(W * width_frac)
    for x in range(edge):
        a = int(strength * (1 - x / edge) ** 1.3)
        d.line([(x, 0), (x, H)], fill=a)
    light = Image.new("RGB", (W, H), (214, 210, 200))
    return Image.composite(light, im, scrim)

# ---------- 带光晕的文字绘制 ----------
def _put(canvas, xy, text, font, fill, halo):
    """在 RGBA 画布上绘制一段文字，先铺光晕再压实字。"""
    layer = Image.new("RGBA", canvas.size, (0, 0, 0, 0))
    ImageDraw.Draw(layer).text(xy, text, font=font, fill=fill + (255,))
    a = layer.split()[3]
    if halo:
        hc, hr, ha = halo
        glow = Image.new("RGBA", canvas.size, hc + (0,))
        glow.putalpha(a.filter(ImageFilter.GaussianBlur(hr)).point(lambda v: int(v * ha / 255)))
        canvas.alpha_composite(glow)
    canvas.alpha_composite(layer)

def draw_title(canvas, x, y_top, fs, line_gap_frac=0.06):
    f = ImageFont.truetype(FONT_TITLE, fs)
    gap = int(fs * line_gap_frac)
    d = ImageDraw.Draw(canvas)
    y = y_top
    for ch in TITLE:
        _put(canvas, (x, y), ch, f, C_TITLE, HALO_TITLE)
        y = d.textbbox((x, y), ch, font=f)[3] + gap
    return y

def draw_subtitle(canvas, x_right, y_top, fs):
    f = ImageFont.truetype(FONT_SUB, fs)
    line_h = int(fs * 1.15)
    col_w = int(fs * 1.28)
    x = x_right
    for col in SUB_COLS:
        y = y_top
        for ch in col:
            _put(canvas, (x, y), ch, f, C_SUB, HALO_SUB)
            y += line_h
        x -= col_w

def draw_latin(canvas, x, y, fs, tracking=0.42):
    f = ImageFont.truetype(FONT_LAT, fs)
    d = ImageDraw.Draw(canvas)
    cx = x
    for ch in LATIN:
        _put(canvas, (cx, y), ch, f, C_LATIN, HALO_LATIN)
        cx += d.textlength(ch, font=f) + fs * tracking

def blur_bg(img, ratio, size):
    bg = cover_crop(img, ratio, 0.5, 0.40).resize(size).filter(ImageFilter.GaussianBlur(46))
    return ImageEnhance.Brightness(bg).enhance(0.82)

def finish(canvas, path):
    canvas.convert("RGB").save(path)

# ---------------- 3:4 (1080x1440) 满版 ----------------
def make_34():
    W, H = 1080, 1440
    src = load()
    box = (0, 166, 1240, 166 + 1653)   # 收紧并把人物推向右侧，左侧让出文字栏
    im = src.crop(box).resize((W, H))
    im = grade(im)
    im = left_scrim(im, width_frac=0.44, strength=84)
    canvas = im.convert("RGBA")
    fs = 196
    draw_title(canvas, x=58, y_top=470, fs=fs)
    draw_subtitle(canvas, x_right=322, y_top=488, fs=46)
    draw_latin(canvas, x=60, y=H - 70, fs=30)
    finish(canvas, os.path.join(HERE, "噤声_封面_3-4.png"))

# ---------------- 16:9 (1920x1080) 模糊填充 ----------------
def make_169():
    W, H = 1920, 1080
    base = load()
    canvas = blur_bg(base, W / H, (W, H))
    strip_ratio = 0.62
    sw = int(H * strip_ratio)
    canvas.paste(cover_crop(base, strip_ratio, fx=0.52, fy=0.30).resize((sw, H)), (int(W * 0.50), 0))
    canvas = grade(canvas, 0.97).convert("RGBA")
    fs = 168
    draw_title(canvas, x=150, y_top=300, fs=fs)
    draw_subtitle(canvas, x_right=410, y_top=314, fs=42)
    draw_latin(canvas, x=152, y=H - 96, fs=30)
    finish(canvas, os.path.join(HERE, "噤声_封面_16-9.png"))

# ---------------- 4:3 (1440x1080) 模糊填充 ----------------
def make_43():
    W, H = 1440, 1080
    base = load()
    canvas = blur_bg(base, W / H, (W, H))
    strip_ratio = 0.66
    sw = int(H * strip_ratio)
    canvas.paste(cover_crop(base, strip_ratio, fx=0.52, fy=0.30).resize((sw, H)), (W - sw - 96, 0))
    canvas = grade(canvas, 0.97).convert("RGBA")
    fs = 176
    draw_title(canvas, x=92, y_top=300, fs=fs)
    draw_subtitle(canvas, x_right=352, y_top=314, fs=42)
    draw_latin(canvas, x=94, y=H - 92, fs=30)
    finish(canvas, os.path.join(HERE, "噤声_封面_4-3.png"))

if __name__ == "__main__":
    make_34(); make_169(); make_43()
    print("covers regenerated (deep ink + halo)")
