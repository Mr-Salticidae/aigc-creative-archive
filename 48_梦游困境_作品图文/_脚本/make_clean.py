# -*- coding: utf-8 -*-
"""牧云人 × 梦游困境云海 — 无字纯净壁纸 (多图第2张 / 下载钩子)
仅等比裁切到 3:4, 不加文字与压角。用法:py make_clean.py
"""
import os
from PIL import Image

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(BASE, "01_素材原图", "原图_梦游困境云海.png")
OUT = os.path.join(BASE, "02_成品封面", "梦游困境_无字壁纸.png")
W, H = 1080, 1440

im = Image.open(SRC).convert("RGB")
sw, sh = im.size
scale = max(W / sw, H / sh)
im = im.resize((int(sw * scale), int(sh * scale)), Image.LANCZOS)
x0 = (im.width - W) // 2
y0 = (im.height - H) // 2
im = im.crop((x0, y0, x0 + W, y0 + H))
os.makedirs(os.path.dirname(OUT), exist_ok=True)
im.save(OUT, quality=95)
print("saved", OUT, im.size)
