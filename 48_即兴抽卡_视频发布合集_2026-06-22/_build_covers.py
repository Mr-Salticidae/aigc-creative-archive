# -*- coding: utf-8 -*-
"""
即兴抽卡 · 视频发布合集 2026-06-22
建目录 + 归档原图 + 生成 3:4 / 4:3 / 16:9 三比例封面
"""
import os, shutil
from PIL import Image, ImageFilter, ImageDraw, ImageFont, ImageEnhance

DL = r"C:\Users\Administrator\Downloads"
ROOT = r"E:\AIGC工作站\48_即兴抽卡_视频发布合集_2026-06-22"

FONT_TITLE = r"C:\Windows\Fonts\msyhbd.ttc"   # 微软雅黑 Bold
FONT_SUB   = r"C:\Windows\Fonts\msyhl.ttc"    # 微软雅黑 Light
FONT_TAG   = r"C:\Windows\Fonts\msyh.ttc"

# group key -> config
GROUPS = {
    "01_青鸾_蓝发仙装": {
        "title": "青鸾",
        "sub": "QING LUAN",
        "tag": "跳蛛先生 · 即兴抽卡",
        "cover": "mr_jumping_spider_Young_woman_fair_skin_delicate_oval_face_lo_da4ba773-cdfc-49e2-a678-5ca340958c83_1.png",
        "files": [
            "mr_jumping_spider_Young_woman_fair_skin_delicate_oval_face_lo_bbfa100b-4ac4-42af-b260-93411594568b_2.png",
            "mr_jumping_spider_Young_woman_fair_skin_delicate_oval_face_lo_540ec1c1-7640-47cc-b63b-17e9170d2e9e_3.png",
            "mr_jumping_spider_Young_woman_fair_skin_delicate_oval_face_lo_6c734cef-7031-4be6-96a7-5c88e6639a92_3.png",
            "mr_jumping_spider_Young_woman_fair_skin_delicate_oval_face_lo_d9c3d499-b243-44d1-bdf6-079513f0eeae_1.png",
            "mr_jumping_spider_Young_woman_fair_skin_delicate_oval_face_lo_da4ba773-cdfc-49e2-a678-5ca340958c83_1.png",
        ],
    },
    "02_雾窗_复古旗袍": {
        "title": "雾窗",
        "sub": "AT THE FOGGY WINDOW",
        "tag": "跳蛛先生 · 即兴抽卡",
        "cover": "mr_jumping_spider_artistic_portrait_of_an_east_asian_woman_ov_db9d594e-ed2a-4155-9751-26a3eaf02718_3.png",
        "files": [
            "mr_jumping_spider_artistic_portrait_of_an_east_asian_woman_ov_d0adf42b-b0cc-4f9e-bf2a-4496b9bcde5d_0.png",
            "mr_jumping_spider_artistic_portrait_of_an_east_asian_woman_ov_e702b56e-e87a-49f8-90e4-1b17561a1f4e_1.png",
            "mr_jumping_spider_artistic_portrait_of_an_east_asian_woman_ov_9a259b1c-4f59-4167-97df-99ef838723fb_1.png",
            "mr_jumping_spider_artistic_portrait_of_an_east_asian_woman_ov_db9d594e-ed2a-4155-9751-26a3eaf02718_3.png",
        ],
    },
    "03_黑蔷薇_废墟黑裙": {
        "title": "黑蔷薇",
        "sub": "BLACK ROSE",
        "tag": "跳蛛先生 · 即兴抽卡",
        "cover": "mr_jumping_spider_Cinematic_environmental_portrait_adult_East_0e63b1fd-ef49-41dd-a547-290042414d55_0.png",
        "files": [
            "mr_jumping_spider_Cinematic_environmental_portrait_adult_East_7b64c8c2-ae8f-483d-a2b4-d2a1c668d2a7_0.png",
            "mr_jumping_spider_Cinematic_environmental_portrait_adult_East_eefeb065-d3c8-40c9-aa98-7a3a86c06b7b_3.png",
            "mr_jumping_spider_Cinematic_environmental_portrait_adult_East_0e63b1fd-ef49-41dd-a547-290042414d55_0.png",
        ],
    },
    "04_蓝调午后_居家自拍": {
        "title": "蓝调午后",
        "sub": "AFTERNOON BLUE",
        "tag": "跳蛛先生 · 即兴抽卡",
        "cover": "mr_jumping_spider_A_casual_mirror_selfie_of_a_young_Chinese_w_fcdafb67-6d9c-431f-ac83-614cfaba0b26_1.png",
        "files": [
            "mr_jumping_spider_A_casual_mirror_selfie_of_a_young_Chinese_w_dfaf3007-7001-44ee-bce8-4de834e27c46_2.png",
            "mr_jumping_spider_A_casual_mirror_selfie_of_a_young_Chinese_w_dfaf3007-7001-44ee-bce8-4de834e27c46_3.png",
            "mr_jumping_spider_A_casual_mirror_selfie_of_a_young_Chinese_w_0267b3df-0284-4536-874a-5b5cccd9d113_3.png",
            "mr_jumping_spider_A_casual_mirror_selfie_of_a_young_Chinese_w_61bb181b-cadf-43ed-a02f-c8be649f22ce_2.png",
            "mr_jumping_spider_A_casual_mirror_selfie_of_a_young_Chinese_w_fcdafb67-6d9c-431f-ac83-614cfaba0b26_1.png",
        ],
    },
}

RATIOS = {"3-4": (1080, 1440), "4-3": (1440, 1080), "16-9": (1920, 1080)}


def make_cover(src_path, out_path, size, title, sub, tag):
    W, H = size
    src = Image.open(src_path).convert("RGB")

    # --- 背景：源图 cover 裁切铺满 + 高斯模糊 + 压暗 ---
    sw, sh = src.size
    scale = max(W / sw, H / sh)
    bg = src.resize((int(sw * scale), int(sh * scale)), Image.LANCZOS)
    bx = (bg.width - W) // 2
    by = (bg.height - H) // 2
    bg = bg.crop((bx, by, bx + W, by + H))
    bg = bg.filter(ImageFilter.GaussianBlur(28))
    bg = ImageEnhance.Brightness(bg).enhance(0.62)

    canvas = bg.copy()

    # --- 前景：源图 contain 适配居中 ---
    pad = 0.94  # 留一点呼吸边
    scale2 = min((W * pad) / sw, (H * pad) / sh)
    fw, fh = int(sw * scale2), int(sh * scale2)
    fg = src.resize((fw, fh), Image.LANCZOS)
    fx = (W - fw) // 2
    # 竖图在横画幅里略上移，给底部标题留白；竖画幅则居中略上
    fy = (H - fh) // 2
    canvas.paste(fg, (fx, fy))

    # --- 底部渐变压暗，保证标题可读 ---
    scrim = Image.new("L", (1, H), 0)
    grad_start = int(H * 0.66)
    for y in range(H):
        if y < grad_start:
            v = 0
        else:
            v = int(165 * (y - grad_start) / (H - grad_start))
        scrim.putpixel((0, y), v)
    scrim = scrim.resize((W, H))
    black = Image.new("RGB", (W, H), (8, 12, 20))
    canvas = Image.composite(black, canvas, scrim)

    draw = ImageDraw.Draw(canvas)

    # 字号随画幅
    base = min(W, H)
    ts = int(base * (0.135 if len(title) <= 2 else 0.10))
    ss = int(base * 0.030)
    gs = int(base * 0.026)
    f_title = ImageFont.truetype(FONT_TITLE, ts)
    f_sub = ImageFont.truetype(FONT_SUB, ss)
    f_tag = ImageFont.truetype(FONT_TAG, gs)

    margin = int(base * 0.06)

    # 标题（左下）
    tb = draw.textbbox((0, 0), title, font=f_title)
    th = tb[3] - tb[1]
    title_y = H - margin - th - int(base * 0.085)
    # 细竖线装饰
    line_x = margin
    draw.line([(line_x, title_y + int(ts*0.12)), (line_x, title_y + th + int(ts*0.18))],
              fill=(235, 238, 245), width=max(2, int(base*0.006)))
    tx = line_x + int(base * 0.035)
    draw.text((tx, title_y - tb[1]), title, font=f_title, fill=(245, 247, 252))

    # 英文副标题
    sub_y = title_y + th + int(base * 0.030)
    draw.text((tx, sub_y), sub, font=f_sub, fill=(200, 208, 222))

    # 角标（左上）
    draw.text((margin, margin), tag, font=f_tag, fill=(225, 230, 240))

    canvas.save(out_path, "PNG")


def main():
    os.makedirs(ROOT, exist_ok=True)
    summary = []
    for key, cfg in GROUPS.items():
        gdir = os.path.join(ROOT, key)
        raw = os.path.join(gdir, "原图")
        cov = os.path.join(gdir, "封面")
        os.makedirs(raw, exist_ok=True)
        os.makedirs(cov, exist_ok=True)

        # 归档原图
        n = 0
        for i, fn in enumerate(cfg["files"], 1):
            sp = os.path.join(DL, fn)
            if not os.path.exists(sp):
                print("  [缺失]", fn); continue
            dp = os.path.join(raw, f"{key.split('_')[0]}_{i:02d}.png")
            shutil.copy2(sp, dp)
            n += 1

        # 封面
        cover_src = os.path.join(DL, cfg["cover"])
        for rk, size in RATIOS.items():
            outp = os.path.join(cov, f"{cfg['title']}_封面_{rk}.png")
            make_cover(cover_src, outp, size, cfg["title"], cfg["sub"], cfg["tag"])

        summary.append(f"{key}: 原图{n}张, 封面3张 (cover={cfg['cover'][:50]}...)")

    print("\n".join(summary))
    print("\nDONE ->", ROOT)


if __name__ == "__main__":
    main()
