# -*- coding: utf-8 -*-
"""第02期 趣味底图 —「睡眠周期之旅」纯PIL精绘(2x超采样)。栏目同款清新编辑插画风。
可作封面底图复用:上部留白给标题,下部场景。"""
import math
from PIL import Image, ImageDraw, ImageFont

S = 2                      # 超采样倍数
W, H = 1080*S, 1440*S
CREAM = (239, 235, 223)
INK   = (35, 66, 63)
CORAL = (216, 100, 58)
TEAL  = (29, 122, 104)
GREY  = (96, 110, 108)
MINT  = (222, 235, 228)
MINT2 = (205, 224, 214)
CLOUD = (246, 242, 233)
FACE  = (242, 230, 206)
WHITE = (255, 255, 255)

def fb(s): return ImageFont.truetype("C:/Windows/Fonts/msyhbd.ttc", s)

img = Image.new("RGB", (W, H), CREAM)
d = ImageDraw.Draw(img)

# ---------- 月亮(珊瑚弯月,右上) ----------
def crescent(cx, cy, r, color, bg):
    d.ellipse([cx-r, cy-r, cx+r, cy+r], fill=color)
    off = int(r*0.55)
    d.ellipse([cx-r+off, cy-r-off*0.25, cx+r+off, cy+r-off*0.25], fill=bg)
crescent(1850, 320, 135, CORAL, CREAM)

# ---------- 星星/亮点(4角star + 圆点) ----------
def sparkle(cx, cy, s, color):
    k = 0.34
    pts = [(cx, cy-s), (cx+s*k, cy-s*k), (cx+s, cy), (cx+s*k, cy+s*k),
           (cx, cy+s), (cx-s*k, cy+s*k), (cx-s, cy), (cx-s*k, cy-s*k)]
    d.polygon(pts, fill=color)
for (x, y, s, c) in [(1560, 250, 34, TEAL), (2010, 560, 26, CORAL),
                     (1690, 640, 20, TEAL), (1380, 470, 22, CORAL),
                     (1930, 180, 18, TEAL)]:
    sparkle(x, y, s, c)
for (x, y, r, c) in [(1640, 380, 9, CORAL), (1490, 660, 8, TEAL),
                     (1960, 700, 9, TEAL), (1780, 540, 7, CORAL)]:
    d.ellipse([x-r, y-r, x+r, y+r], fill=c)

# ---------- 睡眠周期波浪 + 珊瑚醒点 ----------
x0, x1 = 180, 1980
cy, amp, n = 1480, 150, 4.5
pts, steps = [], 600
for i in range(steps+1):
    t = i/steps
    pts.append((x0 + t*(x1-x0), cy - amp*math.cos(2*math.pi*n*t)))
d.line(pts, fill=TEAL, width=18, joint="curve")
for k in range(5):
    t = k/n
    px, py = x0 + t*(x1-x0), cy - amp
    d.ellipse([px-26, py-26, px+26, py+26], fill=CORAL)
    d.ellipse([px-11, py-11, px+11, py+11], fill=CREAM)

# ---------- 云/枕(柔软底座) ----------
cl_cx, cl_top = 1080, 2470
d.rounded_rectangle([540, cl_top, 1640, cl_top+220], radius=110, fill=CLOUD)
for (bx, by, br) in [(660, cl_top-30, 130), (860, cl_top-70, 160),
                     (1100, cl_top-85, 180), (1340, cl_top-55, 150),
                     (1520, cl_top-15, 120)]:
    d.ellipse([bx-br, by-br, bx+br, by+br], fill=CLOUD)

# ---------- 睡着的小人 ----------
# 毯子(青绿,带膝盖凸起)
d.rounded_rectangle([840, 2340, 1560, 2540], radius=90, fill=TEAL)
d.ellipse([1330, 2250, 1560, 2470], fill=TEAL)            # 膝盖鼓包
d.rounded_rectangle([840, 2332, 1500, 2398], radius=33, fill=MINT)  # 翻折床单
# 枕头
d.rounded_rectangle([520, 2380, 820, 2520], radius=60, fill=WHITE)
d.rounded_rectangle([520, 2380, 820, 2520], radius=60, outline=MINT2, width=6)
# 头(整圆头发 + 偏移脸 => 干净发际线)
hx, hy, hr = 700, 2360, 150
d.ellipse([hx-hr, hy-hr, hx+hr, hy+hr], fill=INK)          # 头发底
fx, fy, fr = hx+34, hy+22, hr-10                           # 脸偏右下
d.ellipse([fx-fr, fy-fr, fx+fr, fy+fr], fill=FACE)
# 闭眼(安睡弧) + 微笑 + 腮红 + 鼻尖(相对脸心)
d.arc([fx-12, fy-44, fx+56, fy+12], start=200, end=340, fill=INK, width=8)
d.arc([fx+0, fy+34, fx+54, fy+74], start=20, end=160, fill=INK, width=7)
d.ellipse([fx+60, fy+8, fx+90, fy+34], fill=(228, 168, 140))
d.ellipse([fx+84, fy-24, fx+106, fy-2], fill=(232, 214, 186))

# ---------- Zzz(从头顶升起) ----------
for (zx, zy, zs, c) in [(880, 2150, 60, TEAL), (980, 2010, 90, CORAL), (1100, 1820, 130, TEAL)]:
    d.text((zx, zy), "Z", font=fb(zs), fill=c)

# ---------- 输出(降采样) ----------
out = img.resize((1080, 1440), Image.LANCZOS)
p = "E:/AIGC工作站/45_AI拆解球星身体_世界杯howto/00_发布物料/02_夜醒篇/0_底图_睡眠周期之旅.png"
out.save(p)
print("saved", p)
