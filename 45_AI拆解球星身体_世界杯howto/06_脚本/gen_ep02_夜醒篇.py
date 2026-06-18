# -*- coding: utf-8 -*-
"""第02期 夜醒篇 — 4图生成（栏目视觉规范统一）。正文图纯PIL精绘，封面复用睡眠插画。"""
import math
from PIL import Image, ImageDraw, ImageFont, ImageFilter

# ---------- 规范 ----------
W, H = 1080, 1440
CREAM   = (239, 235, 223)   # 奶油底 #EFEBDF
INK     = (35, 66, 63)      # 墨青主色 #23423F
CORAL   = (216, 100, 58)    # 暖珊瑚强调 #D8643A
TEAL    = (29, 122, 104)    # 青绿 #1D7A68
GREY    = (96, 110, 108)    # 灰青文字 #606E6C
MINT    = (222, 235, 228)   # 浅薄荷框
MINT2   = (208, 226, 218)
WHITE   = (255, 255, 255)

FB = "C:/Windows/Fonts/msyhbd.ttc"   # 微软雅黑粗体
FR = "C:/Windows/Fonts/msyh.ttc"     # 微软雅黑
def fb(s): return ImageFont.truetype(FB, s)
def fr(s): return ImageFont.truetype(FR, s)

OUT = "E:/AIGC工作站/45_AI拆解球星身体_世界杯howto/00_发布物料/02_夜醒篇/"
MJ  = "E:/AIGC工作站/45_AI拆解球星身体_世界杯howto/01_素材_AI原图/MJ原图_睡眠人物_变体2.png"

M = 90  # 左右页边距

# ---------- helpers ----------
def tw(d, t, f): return d.textlength(t, font=f)

def text(d, xy, t, f, fill, anchor=None):
    d.text(xy, t, font=f, fill=fill, anchor=anchor)

def center(d, y, t, f, fill):
    d.text((W/2, y), t, font=f, fill=fill, anchor="ma")

def segs_center(d, y, segments, f):
    total = sum(tw(d, t, f) for t, _ in segments)
    x = (W - total) / 2
    for t, c in segments:
        d.text((x, y), t, font=f, fill=c)
        x += tw(d, t, f)

def pill(d, label="AI拆解球星身体 · 02"):
    f = fb(30)
    pad_x, pad_y = 26, 14
    tw_ = tw(d, label, f)
    x0, y0 = M, 70
    d.rounded_rectangle([x0, y0, x0+tw_+pad_x*2, y0+44+pad_y], radius=28, fill=INK)
    d.text((x0+pad_x, y0+pad_y-2), label, font=f, fill=WHITE)

def coral_dot_label(d, y, t, dotx=M):
    r = 9
    cy = y + 22
    d.ellipse([dotx, cy-r, dotx+2*r, cy+r], fill=CORAL)
    f = fr(40)
    d.text((dotx+2*r+16, y), t, font=f, fill=GREY)

def base(cream=True):
    img = Image.new("RGB", (W, H), CREAM)
    return img

def save(img, name):
    img.save(OUT+name)
    print("saved", name)

# ============================================================
# 图1 封面
# ============================================================
def cover():
    img = base()
    mj = Image.open(MJ).convert("RGB")
    mj = mj.transpose(Image.FLIP_LEFT_RIGHT)              # 镜像区别01期
    # cover-fit to WxH
    r = max(W/mj.width, H/mj.height)
    mj = mj.resize((int(mj.width*r), int(mj.height*r)), Image.LANCZOS)
    ox = (mj.width - W)//2; oy = (mj.height - H)//2
    mj = mj.crop((ox, oy, ox+W, oy+H))
    img.paste(mj, (0, 0))
    # 顶部奶油渐变遮罩，保证文字可读
    grad = Image.new("L", (1, H), 0)
    for y in range(H):
        a = int(235 * max(0, 1 - y/ (H*0.6)))   # 顶部不透明→中部透明
        grad.putpixel((0, y), a)
    grad = grad.resize((W, H))
    overlay = Image.new("RGB", (W, H), CREAM)
    img = Image.composite(overlay, img, grad)
    d = ImageDraw.Draw(img)
    pill(d)
    # 设问
    coral_dot_label(d, 168, "半夜总醒、睡得浅,以为是失眠?")
    # 反转 大标题
    y = 250
    segs_center_left = [
        [("C罗 ", INK), ("从不怕", CORAL)],
        [("半夜醒来", INK)],
    ]
    f = fb(112)
    x = M
    for line in segs_center_left:
        cx = M
        for t, c in line:
            d.text((cx, y), t, font=f, fill=c)
            cx += tw(d, t, f)
        y += 128
    # 副标题
    d.text((M, y+10), "醒在睡眠周期交界,是身体的设计", font=fr(44), fill=GREY)
    save(img, "1_封面_夜醒篇.png")

# ============================================================
# 图2 立坑：半夜醒 ≠ 失眠
# ============================================================
def page2():
    img = base(); d = ImageDraw.Draw(img)
    pill(d)
    coral_dot_label(d, 168, "先破一个误解")
    d.text((M, 228), "半夜醒一下 ≠ 失眠", font=fb(74), fill=INK)
    # 大数字
    segs_center(d, 380, [("58.5", CORAL), ("%", CORAL)], fb(150))
    center(d, 558, "国人觉得自己「睡得浅」", fr(40), GREY)
    center(d, 612, "—《2022 中国国民睡眠健康白皮书》", fr(30), GREY)
    # mint box
    bx0, by0, bx1, by1 = M, 700, W-M, 1190
    d.rounded_rectangle([bx0,by0,bx1,by1], radius=34, fill=MINT)
    d.text((bx0+44, by0+40), "真正的问题,不是「醒」", font=fb(48), fill=INK)
    d.text((bx0+44, by0+108), "是醒来之后的连锁反应", font=fr(38), fill=GREY)
    chain = ["半夜睁眼 → 抓起手机看时间",
             "「怎么又醒了,几点了…」开始焦虑",
             "越想睡越清醒,交感神经被点燃",
             "结果:把一次正常转醒,熬成了真失眠"]
    yy = by0+190
    for i, c in enumerate(chain):
        cyc = yy+24
        col = CORAL if i==len(chain)-1 else TEAL
        d.ellipse([bx0+44, cyc-9, bx0+62, cyc+9], fill=col)
        d.text((bx0+82, yy), c, font=fr(38), fill=INK)
        yy += 72
    # 底部条
    d.rounded_rectangle([M,1240,W-M,1340], radius=28, fill=INK)
    segs_center(d, 1262, [("健康的觉,本来就是 ", WHITE), ("一段一段", CORAL), (" 的", WHITE)], fb(42))
    save(img, "2_正文_半夜醒不是失眠.png")

# ============================================================
# 图3 给解：R90 — 醒是身体的设计（睡眠周期波形）
# ============================================================
def page3():
    img = base(); d = ImageDraw.Draw(img)
    pill(d)
    coral_dot_label(d, 168, "球星用的科学版 · R90")
    d.text((M, 228), "C罗教练:醒,是设计好的", font=fb(64), fill=INK)
    # 睡眠周期波形（hypnogram风）
    x0, x1 = M, W-M; Wc = x1-x0
    cy, amp = 470, 95
    n = 4.5
    pts = []
    steps = 400
    for i in range(steps+1):
        t = i/steps
        y = cy - amp*math.cos(2*math.pi*n*t)
        pts.append((x0 + t*Wc, y))
    # 清醒参考线
    d.line([(x0, cy-amp),(x1, cy-amp)], fill=MINT2, width=3)
    d.text((x0, cy-amp-44), "清醒", font=fr(28), fill=GREY)
    d.text((x0, cy+amp+14), "深睡", font=fr(28), fill=GREY)
    d.line(pts, fill=TEAL, width=9, joint="curve")
    # 5个自然醒峰值打珊瑚点
    for k in range(5):
        t = k/n
        px = x0 + t*Wc; py = cy-amp
        d.ellipse([px-13, py-13, px+13, py+13], fill=CORAL)
    d.text((x0, cy+amp+70), "← 一夜自然转醒 4~5 次,每次都很正常", font=fr(36), fill=CORAL)
    # mint box 三条
    bx0, by0, bx1, by1 = M, 720, W-M, 1190
    d.rounded_rectangle([bx0,by0,bx1,by1], radius=34, fill=MINT)
    d.text((bx0+44, by0+34), "醒了,到底怎么办", font=fb(48), fill=INK)
    pts3 = [("90 分钟 = 一个完整睡眠周期", "一夜要走 4~5 个,周期之间本就会短暂转醒"),
            ("醒了别开灯、别看手机、别盯钟", "顺势深呼吸,等身体滑进下一个周期"),
            ("夜里缺的周期,白天补", "20~30 分钟小睡(CRP),别赖床补整觉")]
    yy = by0+128
    for i,(a,b) in enumerate(pts3):
        cyc = yy+28
        d.ellipse([bx0+44, cyc-20, bx0+88, cyc+24], fill=TEAL)
        d.text((bx0+57, yy-2), str(i+1), font=fb(40), fill=WHITE)
        d.text((bx0+112, yy-4), a, font=fb(40), fill=INK)
        d.text((bx0+112, yy+46), b, font=fr(34), fill=GREY)
        yy += 116
    # 底部条
    d.rounded_rectangle([M,1240,W-M,1340], radius=28, fill=INK)
    segs_center(d, 1262, [("醒来 ≠ 失眠 ｜ ", WHITE), ("醒后焦虑+盯钟", CORAL), (",才变成失眠", WHITE)], fb(40))
    save(img, "3_正文_醒是身体的设计.png")

# ============================================================
# 图4 实操：普通人安全版
# ============================================================
def page4():
    img = base(); d = ImageDraw.Draw(img)
    pill(d)
    coral_dot_label(d, 168, "普通人怎么抄 · 安全版")
    d.text((M, 228), "今晚就能用的 5 条", font=fb(70), fill=INK)
    tips = [
        ("把卧室调成「恢复舱」", "偏凉 16~18℃ + 拉黑遮光——睡得浅先从环境改"),
        ("睡前 90 分钟降光、关屏", "把手机/电视关掉,灯调暗,给身体降挡信号"),
        ("固定「起床时间」", "比固定几点睡更重要,它才是生物钟的锚"),
        ("半夜醒了:不碰手机", "深呼吸,等下一个周期,别盯钟吓自己"),
        ("白天困:20~30 分钟小睡", "16 点前结束,补周期不补整觉"),
    ]
    yy = 360
    for i,(a,b) in enumerate(tips):
        bh = 168
        d.rounded_rectangle([M, yy, W-M, yy+bh-24], radius=30, fill=MINT if i%2==0 else MINT)
        cyc = yy + (bh-24)/2
        d.ellipse([M+34, cyc-34, M+102, cyc+34], fill=CORAL)
        d.text((M+52, cyc-34), str(i+1), font=fb(52), fill=WHITE)
        d.text((M+138, yy+30), a, font=fb(46), fill=INK)
        d.text((M+138, yy+92), b, font=fr(34), fill=GREY)
        yy += bh
    # 收尾金句
    d.rounded_rectangle([M, yy+6, W-M, yy+118], radius=28, fill=INK)
    segs_center(d, yy+24, [("球星的好状态,不是睡满 8 小时,", WHITE)], fb(38))
    segs_center(d, yy+70, [("是连「醒」都管理好了", CORAL)], fb(38))
    save(img, "4_正文_普通人怎么抄.png")

# 封面已改由 gen_ep02_封面_mj.py(MJ水彩底图)专管,此处不再生成,避免覆盖正式封面
page2(); page3(); page4()
print("DONE")
