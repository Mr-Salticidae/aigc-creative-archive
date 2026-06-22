# -*- coding: utf-8 -*-
"""
即兴抽卡 · 视频发布合集 2026-06-22  —— 封面代码排版 (v2 · 艺术性字体版)
依据 KB: 04_方法论/05_prompt与工具方法/代码排版小红书封面工作流 + 46_牧云人 make_cover
手法: 宋体竖排主标 + 楷体竖排诗句 + 暖金细线 + 左侧柔光带(不全压暗) + 文字柔投影 + 2x超采样
原图归档已完成, 本脚本仅(重)生成封面。
"""
import os, glob
from PIL import Image, ImageDraw, ImageFont, ImageFilter

ROOT = r"E:\AIGC工作站\48_即兴抽卡_视频发布合集_2026-06-22"
FONTS = r"C:\Windows\Fonts"
f_song = lambda s: ImageFont.truetype(os.path.join(FONTS, "simsun.ttc"), s)   # 宋体 主标
f_kai  = lambda s: ImageFont.truetype(os.path.join(FONTS, "simkai.ttf"), s)   # 楷体 诗句/落款
f_lat  = lambda s: ImageFont.truetype(os.path.join(FONTS, "Dengl.ttf"), s)    # 等线细 拉丁

INK  = (240, 235, 224)   # 暖米白(标题) — 避免纯白刺眼
INK2 = (224, 218, 204)   # 副标
GOLD = (201, 170, 113)   # 暖金 — 细线 / 拉丁小字
SH   = (8, 11, 17)       # 文字柔投影 深蓝灰
SCRIM = (14, 19, 29)     # 左侧柔光带 / 背景压暗 深蓝灰(非纯黑)

RATIOS = {"3-4": (1080, 1440), "4-3": (1440, 1080), "16-9": (1920, 1080)}
SS = 2

GROUPS = {
    "01_青鸾_蓝发仙装":     dict(title="青鸾",     sub="人间一粒尘",     lat="QING LUAN",     tag="跳蛛先生 · 即兴抽卡"),
    "02_雾窗_复古旗袍":     dict(title="雾窗",     sub="一封无址的信",   lat="FOGGY WINDOW",  tag="跳蛛先生 · 即兴抽卡"),
    "03_黑蔷薇_废墟黑裙":   dict(title="黑蔷薇",   sub="没人敢念的诗",   lat="BLACK ROSE",    tag="跳蛛先生 · 即兴抽卡"),
    "04_蓝调午后_居家自拍": dict(title="蓝调午后", sub="今天也好好活着", lat="AFTERNOON BLUE",tag="跳蛛先生 · 即兴抽卡"),
    "05_噤声_水墨红梅汉服": dict(title="噤声",   sub="别惊一树红梅",   lat="HUSH",          tag="跳蛛先生 · 即兴抽卡"),
}


def vtext(d, x, y0, chars, font, fill, step):
    """竖排: 每字以 x 为水平中心逐字下落, 返回末端 y"""
    y = y0
    for ch in chars:
        d.text((x, y), ch, font=font, fill=fill, anchor="mm")
        y += step
    return y


def tracked(d, x, y, s, font, fill, tr):
    for ch in s:
        d.text((x, y), ch, font=font, fill=fill)
        x += d.textlength(ch, font=font) + tr


def left_scrim(w, h, fade_to):
    """左->右 线性渐隐柔光带, 到 fade_to 归零, 保留右/中主体高光"""
    grad = Image.new("L", (w, 1), 0)
    px = grad.load()
    for x in range(w):
        v = 0 if x >= fade_to else int(150 * ((1 - x / fade_to) ** 1.4))
        px[x, 0] = v
    return grad.resize((w, h))


def build(src_path, out_path, size, cfg):
    W, H = size
    w, h = W * SS, H * SS
    portrait = H >= W
    src = Image.open(src_path).convert("RGB")
    sw, sh = src.size

    if portrait:
        scale = max(w / sw, h / sh)
        rim = src.resize((int(sw * scale), int(sh * scale)), Image.LANCZOS)
        x0 = (rim.width - w) // 2
        y0 = int((rim.height - h) * 0.30)          # 裁切偏上, 保住头部/头冠
        base = rim.crop((x0, y0, x0 + w, y0 + h)).convert("RGBA")
        zone_right = int(w * 0.42)
    else:
        scale_b = max(w / sw, h / sh)
        bg = src.resize((int(sw * scale_b), int(sh * scale_b)), Image.LANCZOS)
        bx = (bg.width - w) // 2; by = (bg.height - h) // 2
        bg = bg.crop((bx, by, bx + w, by + h)).filter(ImageFilter.GaussianBlur(30 * SS))
        bg = Image.blend(bg, Image.new("RGB", (w, h), SCRIM), 0.42)
        fgh = int(h * 0.96); fgw = int(fgh * sw / sh)
        fg = src.resize((fgw, fgh), Image.LANCZOS)
        fx = (w - fgw) // 2; fy = (h - fgh) // 2
        base = bg.convert("RGBA")
        sh_fg = Image.new("RGBA", (w, h), (0, 0, 0, 0))
        sh_fg.alpha_composite(Image.new("RGBA", (fgw + 44 * SS, fgh + 44 * SS), (0, 0, 0, 120)),
                              (fx - 22 * SS, fy - 14 * SS))
        sh_fg = sh_fg.filter(ImageFilter.GaussianBlur(20 * SS))
        base = Image.alpha_composite(base, sh_fg)
        base.paste(fg, (fx, fy))
        zone_right = fx - int(w * 0.03)

    if portrait:
        sc = left_scrim(w, h, int(w * 0.46))
        sl = Image.new("RGBA", (w, h), SCRIM + (0,)); sl.putalpha(sc)
        base = Image.alpha_composite(base, sl)

    # ---------- 文本层 ----------
    txt = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    d = ImageDraw.Draw(txt)
    title, sub = cfg["title"], cfg["sub"]
    nt = len(title)

    base_h = H
    # 标题字号随字数收敛
    ts = int(base_h * (0.150 if nt <= 2 else 0.118 if nt == 3 else 0.092)) * SS
    ss_ = int(base_h * 0.040) * SS                       # 楷体副标
    ls_ = int(base_h * 0.026) * SS                       # 拉丁
    tg_ = int(base_h * 0.0235) * SS                      # 角标
    t_step = int(ts * 1.16)
    s_step = int(ss_ * 1.30)

    # 块右内缘对齐到 zone_right, 副标在右, 主标在左
    sub_x = zone_right - ss_ // 2 - int(base_h * 0.012) * SS
    sep_x = sub_x - ss_ // 2 - int(base_h * 0.022) * SS
    title_x = sep_x - int(base_h * 0.020) * SS - ts // 2
    if title_x < ts // 2 + int(w * 0.04):                # 防越界
        title_x = ts // 2 + int(w * 0.04)

    # 垂直: 标题块居中略偏下
    block_h = nt * t_step
    cy = int(h * 0.55)
    t_top = cy - block_h // 2 + t_step // 2
    vtext(d, title_x, t_top, title, f_song(ts), INK, t_step)

    # 暖金细竖线
    line_top = t_top - t_step // 2 + int(ts * 0.10)
    line_bot = t_top + block_h - t_step // 2 + int(ts * 0.10)
    d.line([(sep_x, line_top), (sep_x, line_bot)], fill=GOLD + (200,), width=max(2, SS))

    # 楷体诗句 竖排, 略下沉 (错落)
    vtext(d, sub_x, line_top + s_step // 2 + int(base_h * 0.01) * SS, sub, f_kai(ss_), INK2, s_step)

    # (左上角标已移除)
    mg = int(w * 0.055)

    # 拉丁落款 (左下, 字距展开) + 暖金短线
    foot_y = int(h * 0.935)
    d.line([(mg, foot_y - int(base_h*0.012)*SS), (mg + int(base_h*0.075)*SS, foot_y - int(base_h*0.012)*SS)],
           fill=GOLD + (210,), width=max(2, SS))
    tracked(d, mg, foot_y, cfg["lat"], f_lat(ls_), GOLD + (235,), int(base_h * 0.006) * SS)

    # 文字柔投影 (由文本 alpha 派生)
    alpha = txt.split()[3]
    shadow = Image.new("RGBA", (w, h), SH + (0,))
    shadow.putalpha(alpha.point(lambda v: int(v * 0.62)))
    shadow = shadow.filter(ImageFilter.GaussianBlur(4 * SS))

    out = base.copy()
    out.alpha_composite(shadow, (0, 3 * SS))
    out.alpha_composite(txt)
    out = out.convert("RGB").resize((W, H), Image.LANCZOS)
    out.save(out_path, "PNG")


def main():
    for key, cfg in GROUPS.items():
        cover_src = sorted(glob.glob(os.path.join(ROOT, key, "原图", "*.png")))
        # 用各组选定的封面主图(沿用 v1: 末位流水号为代表图)
        src = pick_cover(key, cover_src)
        cdir = os.path.join(ROOT, key, "封面")
        os.makedirs(cdir, exist_ok=True)
        for rk, size in RATIOS.items():
            build(src, os.path.join(cdir, f"{cfg['title']}_封面_{rk}.png"), size, cfg)
        print("OK", key, "<-", os.path.basename(src))


# 各组代表封面图(与 v1 一致): 序号_XX.png
COVER_PICK = {"01_青鸾_蓝发仙装": "01_05.png", "02_雾窗_复古旗袍": "02_04.png",
              "03_黑蔷薇_废墟黑裙": "03_03.png", "04_蓝调午后_居家自拍": "04_05.png",
              "05_噤声_水墨红梅汉服": "05_05.png"}


def pick_cover(key, files):
    want = COVER_PICK[key]
    for f in files:
        if os.path.basename(f) == want:
            return f
    return files[-1]


if __name__ == "__main__":
    main()
