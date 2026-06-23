# -*- coding: utf-8 -*-
"""
即兴抽卡 · 第 07/08 组封面 (2026-06-23 抽卡) —— 主题与前六组不同, 封标各自定制
依据 KB: 04_方法论/05_prompt与工具方法/代码排版小红书封面工作流
        + 网络复盘(Vogue Didone 报头 / 暗黑戏剧海报 朱红+留白)

07 假面 (红衣戏面) —— 暗调戏剧:  宋体竖排骨白主标 + 朱红细竖线 + 朱砂印章 + 角落柔暗(护脸/护面具)
08 栖白 (白西装编辑感) —— 时尚编辑: Playfair Didone 高反差报头(顶部) + 等宽小标 + 汉仪中黑封面语
两组共用一套 cover-fit / 柔投影 / 2x 超采样 脚手架, 文本层各走各的设计。
"""
import os, glob
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter

ROOT  = r"E:\AIGC工作站\48_即兴抽卡_视频发布合集_2026-06-22"
FONTS = r"C:\Windows\Fonts"
PLAY  = os.path.join(ROOT, "_fonts", "PlayfairDisplay.ttf")

f_song = lambda s: ImageFont.truetype(os.path.join(FONTS, "simsun.ttc"), s)        # 宋体
f_hei  = lambda s: ImageFont.truetype(os.path.join(FONTS, "simhei.ttf"), s)        # 黑体
f_kai  = lambda s: ImageFont.truetype(os.path.join(FONTS, "simkai.ttf"), s)        # 楷体
f_yh   = lambda s: ImageFont.truetype(os.path.join(FONTS, "msyh.ttc"), s)          # 微软雅黑(封面语)
f_deng = lambda s: ImageFont.truetype(os.path.join(FONTS, "Dengl.ttf"), s)         # 等线细


def f_play(s, weight="Black"):
    f = ImageFont.truetype(PLAY, s)
    try:
        f.set_variation_by_name(weight)
    except Exception:
        pass
    return f


RATIOS = {"3-4": (1080, 1440), "4-3": (1440, 1080), "16-9": (1920, 1080)}
SS = 2

# ---- 07 假面 调色 ----
BONE  = (236, 230, 221)   # 骨白(主标) — 呼应裂面瓷白
BONE2 = (214, 205, 194)   # 副标暗骨白
CINNA = (171, 30, 30)     # 朱砂红(细线/印章底)
CINNA2= (120, 22, 22)     # 深朱(拉丁落款)
DARK  = (15, 10, 11)      # 角落柔暗 近黑带红

# ---- 08 栖白 调色 ----
WARMW = (246, 243, 237)   # 暖白(报头/封面语)
TERRA = (188, 99, 74)     # 暖陶土(细线/点缀) — 取自发丝暖光
INKG  = (38, 34, 33)      # 深墨(暗底小字, 备用)
SH    = (8, 9, 12)        # 文字柔投影


# ============ 通用脚手架 ============
def vtext(d, x, y0, chars, font, fill, step):
    y = y0
    for ch in chars:
        d.text((x, y), ch, font=font, fill=fill, anchor="mm")
        y += step
    return y


def htext_len(d, s, font, tr):
    return sum(d.textlength(ch, font=font) + tr for ch in s) - tr


def tracked(d, x, y, s, font, fill, tr, anchor_y="a"):
    for ch in s:
        d.text((x, y), ch, font=font, fill=fill, anchor="l" + anchor_y)
        x += d.textlength(ch, font=font) + tr


def cover_fit(src, w, h, up=0.30):
    sw, sh = src.size
    scale = max(w / sw, h / sh)
    rim = src.resize((int(sw * scale), int(sh * scale)), Image.LANCZOS)
    x0 = (rim.width - w) // 2
    y0 = int((rim.height - h) * up)
    return rim.crop((x0, y0, x0 + w, y0 + h)).convert("RGBA")


def fit_landscape(src, w, h, scrim_rgb, blur=30, blend=0.42, fgh_frac=0.96):
    sw, sh = src.size
    sc = max(w / sw, h / sh)
    bg = src.resize((int(sw * sc), int(sh * sc)), Image.LANCZOS)
    bx = (bg.width - w) // 2; by = (bg.height - h) // 2
    bg = bg.crop((bx, by, bx + w, by + h)).filter(ImageFilter.GaussianBlur(blur * SS))
    bg = Image.blend(bg, Image.new("RGB", (w, h), scrim_rgb), blend)
    fgh = int(h * fgh_frac); fgw = int(fgh * sw / sh)
    fg = src.resize((fgw, fgh), Image.LANCZOS)
    fx = (w - fgw) // 2; fy = (h - fgh) // 2
    base = bg.convert("RGBA")
    shdw = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    shdw.alpha_composite(Image.new("RGBA", (fgw + 44 * SS, fgh + 44 * SS), (0, 0, 0, 120)),
                         (fx - 22 * SS, fy - 14 * SS))
    base = Image.alpha_composite(base, shdw.filter(ImageFilter.GaussianBlur(20 * SS)))
    base.paste(fg, (fx, fy))
    return base, fx, fx + fgw


def soft_shadow(txt, w, h, rgb=SH, k=0.62, blur=4, dy=3):
    alpha = txt.split()[3]
    shadow = Image.new("RGBA", (w, h), rgb + (0,))
    shadow.putalpha(alpha.point(lambda v: int(v * k)))
    return shadow.filter(ImageFilter.GaussianBlur(blur * SS)), dy


def scrim_layer(w, h, alpha_arr, rgb):
    L = Image.fromarray(alpha_arr.astype("uint8"), "L")
    lay = Image.new("RGBA", (w, h), rgb + (0,))
    lay.putalpha(L)
    return lay


# ============ 设计 A: 07 假面 — 暗调戏剧 ============
def design_mask(base, w, h, W, H, cfg, portrait, zoneL, zoneR):
    yy, xx = np.mgrid[0:h, 0:w]
    # 右上角柔暗带: 右强左零(0.5w起) × 上满下taper(护住下方面具)
    x0 = 0.50 * w
    xf = np.clip((xx - x0) / (w - x0), 0, 1) ** 1.3
    y_full, y_zero = 0.58 * h, 0.74 * h
    yf = np.where(yy <= y_full, 1.0, np.clip((y_zero - yy) / (y_zero - y_full), 0, 1))
    if not portrait:                      # 横屏: 主体居中, 文字区在右, 不做下taper
        yf = np.ones_like(yf)
        xf = np.clip((xx - 0.55 * w) / (w - 0.55 * w), 0, 1) ** 1.2
    base = Image.alpha_composite(base, scrim_layer(w, h, xf * yf * 150, DARK))
    # 顶部很浅一层, 压住标题顶端
    topf = np.clip((0.16 * h - yy) / (0.16 * h), 0, 1) ** 1.4 * 70
    base = Image.alpha_composite(base, scrim_layer(w, h, topf, DARK))

    txt = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    d = ImageDraw.Draw(txt)
    title, sub = cfg["title"], cfg["sub"]

    ts = int(H * 0.150) * SS          # 主标(2字)
    ss_ = int(H * 0.038) * SS         # 楷体副标
    t_step = int(ts * 1.18)
    s_step = int(ss_ * 1.34)

    # 文本块靠右: 副标在最右, 朱红线, 主标在左
    edge = zoneR - int(W * 0.045) * SS
    sub_x = edge - ss_ // 2
    line_x = sub_x - ss_ // 2 - int(H * 0.020) * SS
    title_x = line_x - int(H * 0.022) * SS - ts // 2

    block_h = len(title) * t_step
    cy = int(h * (0.48 if portrait else 0.46))
    t_top = cy - block_h // 2 + t_step // 2
    vtext(d, title_x, t_top, title, f_song(ts), BONE, t_step)

    line_top = t_top - t_step // 2 + int(ts * 0.10)
    line_bot = t_top + block_h - t_step // 2 + int(ts * 0.10)
    d.line([(line_x, line_top), (line_x, line_bot)], fill=CINNA + (235,), width=max(2, SS + 1))

    vtext(d, sub_x, line_top + s_step // 2 + int(H * 0.012) * SS, sub, f_kai(ss_), BONE2, s_step)

    # 拉丁落款(左下, 朱) + 朱砂印章(其上)
    mg = int(w * 0.058)
    foot_y = int(h * 0.945)
    ls_ = int(H * 0.025) * SS
    d.line([(mg, foot_y), (mg + int(H * 0.072) * SS, foot_y)], fill=CINNA + (220,), width=max(2, SS))
    tracked(d, mg, foot_y + int(H * 0.010) * SS, cfg["lat"], f_deng(ls_), CINNA2 + (245,),
            int(H * 0.006) * SS)

    out = base.copy()
    shadow, dy = soft_shadow(txt, w, h)
    out.alpha_composite(shadow, (0, dy * SS))
    out.alpha_composite(txt)

    # 朱砂印章(独立层, 不投影) — 左下, 落款之上
    seal = cfg.get("seal")
    if seal:
        sz = int(H * 0.072) * SS
        sx, sy = mg, foot_y - int(H * 0.026) * SS - sz
        sl = Image.new("RGBA", (w, h), (0, 0, 0, 0))
        ds = ImageDraw.Draw(sl)
        ds.rounded_rectangle([sx, sy, sx + sz, sy + sz], radius=int(sz * 0.10),
                             fill=CINNA + (235,))
        ds.text((sx + sz // 2, sy + sz // 2 + int(sz * 0.02)), seal,
                font=f_hei(int(sz * 0.70)), fill=BONE + (255,), anchor="mm")
        out.alpha_composite(sl)
    return out


# ============ 设计 B: 08 栖白 — 时尚编辑(Vogue) ============
def design_vogue(base, w, h, W, H, cfg, portrait, fx0, fx1):
    yy, xx = np.mgrid[0:h, 0:w]
    # 顶部柔渐变(托报头) + 左下角柔渐变(托封面语)
    topf = np.clip((0.26 * h - yy) / (0.26 * h), 0, 1) ** 1.5 * 95
    cx, cy = 0.0, 1.0 * h
    rad = np.clip(1 - (((xx - cx) / (0.62 * w)) ** 2 + ((yy - cy) / (0.5 * h)) ** 2), 0, 1) ** 1.5
    botf = rad * 96
    base = Image.alpha_composite(base, scrim_layer(w, h, topf, (10, 12, 16)))
    base = Image.alpha_composite(base, scrim_layer(w, h, botf, (12, 12, 16)))

    txt = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    d = ImageDraw.Draw(txt)

    # ---- 报头 BLANC (Playfair Black, 居中, 字距展开) ----
    mh = cfg["masthead"]
    mhs = int(H * 0.150) * SS if portrait else int(H * 0.165) * SS
    tr = int(mhs * 0.06)
    fpl = f_play(mhs, "Black")
    total = htext_len(d, mh, fpl, tr)
    mx = (w - total) / 2 if portrait else int(w * 0.06)
    my = int(h * 0.052)
    tracked(d, mx, my, mh, fpl, WARMW + (255,), tr, anchor_y="a")
    # 报头下细横线 + 期号
    lyy = my + int(mhs * 1.02)
    if portrait:
        d.line([(mx + total * 0.18, lyy), (mx + total * 0.82, lyy)], fill=TERRA + (210,), width=max(2, SS))
        d.text((w / 2, lyy + int(H * 0.022) * SS), cfg["issue"], font=f_deng(int(H * 0.020) * SS),
               fill=WARMW + (235,), anchor="ma")
    else:
        d.line([(mx, lyy), (mx + total, lyy)], fill=TERRA + (210,), width=max(2, SS))
        d.text((mx, lyy + int(H * 0.020) * SS), cfg["issue"], font=f_deng(int(H * 0.020) * SS),
               fill=WARMW + (235,), anchor="la")

    # ---- 封面语(汉仪中黑, 左下堆叠) ----
    ls = int(H * 0.040) * SS
    lh = int(ls * 1.62)
    bx = int(w * 0.066)
    by = int(h * (0.74 if portrait else 0.62))
    d.line([(bx, by - int(H * 0.014) * SS), (bx + int(H * 0.052) * SS, by - int(H * 0.014) * SS)],
           fill=TERRA + (235,), width=max(3, SS + 1))
    for i, ln in enumerate(cfg["lines"]):
        d.text((bx, by + i * lh), ln, font=f_yh(ls), fill=WARMW + (250,), anchor="la")

    # ---- 中文刊名 栖白 + 署名(右下) ----
    zh = cfg["zh"]
    zs = int(H * 0.052) * SS
    zx = int(w * (0.93 if portrait else 0.95)); zy = int(h * 0.86)
    tracked(d, zx - htext_len(d, zh, f_song(zs), int(zs * 0.18)), zy, zh, f_song(zs),
            WARMW + (250,), int(zs * 0.18), anchor_y="a")
    d.text((zx, zy + int(zs * 1.18)), cfg["byline"], font=f_deng(int(H * 0.018) * SS),
           fill=WARMW + (215,), anchor="ra")

    out = base.copy()
    shadow, dy = soft_shadow(txt, w, h, k=0.55, blur=5)
    out.alpha_composite(shadow, (0, dy * SS))
    out.alpha_composite(txt)
    return out


# ============ 总装 ============
def build(src_path, out_path, size, cfg):
    W, H = size
    w, h = W * SS, H * SS
    portrait = H >= W
    src = Image.open(src_path).convert("RGB")

    if cfg["design"] == "mask":
        if portrait:
            base = cover_fit(src, w, h, up=0.26)
            zoneL, zoneR = 0, w
        else:
            base, fx0, fx1 = fit_landscape(src, w, h, DARK, blend=0.46)
            zoneL, zoneR = 0, w
        out = design_mask(base, w, h, W, H, cfg, portrait, zoneL, zoneR)
    else:  # vogue
        if portrait:
            base = cover_fit(src, w, h, up=0.16)   # 偏上, 给报头留头顶
            out = design_vogue(base, w, h, W, H, cfg, True, 0, w)
        else:
            base, fx0, fx1 = fit_landscape(src, w, h, (16, 17, 21), blend=0.40)
            out = design_vogue(base, w, h, W, H, cfg, False, fx0, fx1)

    out = out.convert("RGB").resize((W, H), Image.LANCZOS)
    out.save(out_path, "PNG")


GROUPS = {
    "07_假面_红衣戏面": dict(
        design="mask", title="假面", sub="替我哭的那张脸", lat="MASQUE", seal="戲",
        pick="07_03.png"),
    "08_栖白_白西装编辑感": dict(
        design="vogue", masthead="BLANC", zh="栖白", issue="ÉDITION  N°08",
        byline="跳蛛先生 · 即兴抽卡",
        lines=["卷发 与 白西装", "格子间里的松弛", "下班前最后一束光"],
        pick="08_01.png"),
}


def pick_cover(key, cfg):
    files = sorted(glob.glob(os.path.join(ROOT, key, "原图", "*.png")))
    for f in files:
        if os.path.basename(f) == cfg["pick"]:
            return f
    return files[-1]


def main():
    for key, cfg in GROUPS.items():
        src = pick_cover(key, cfg)
        cdir = os.path.join(ROOT, key, "封面")
        os.makedirs(cdir, exist_ok=True)
        name = cfg.get("title") or cfg.get("zh")
        for rk, size in RATIOS.items():
            build(src, os.path.join(cdir, f"{name}_封面_{rk}.png"), size, cfg)
        print("OK", key, "<-", os.path.basename(src))


if __name__ == "__main__":
    main()
