# -*- coding: utf-8 -*-
"""晴枝四图 -> Seedance 2.0 图生视频片段(无音频)
用法: 设置环境变量 ARK_API_KEY 后运行  py seedance2_i2v.py
流程: 原图压缩为JPEG -> 提交4个i2v任务 -> 轮询 -> 下载MP4(链接24h过期,立即落盘) -> 写生成记录
"""
import base64
import io
import json
import os
import sys
import time
import urllib.request
import urllib.error
from pathlib import Path

from PIL import Image

# ---------------- 配置 ----------------
API_BASE = "https://ark.cn-beijing.volces.com/api/v3/contents/generations/tasks"
MODEL = "doubao-seedance-2-0-260128"
DURATION = 5            # 秒
RESOLUTION = "1080p"
RATIO = "adaptive"      # 跟随首帧图比例(3:4竖版)
POLL_INTERVAL = 15      # 轮询间隔秒
TIMEOUT_MIN = 30        # 单任务超时分钟

PROJECT = Path(r"D:\AIGC工作站\39_晴枝_花园写真")
SRC_DIR = PROJECT / "04_精选成图" / "发布精选_晴枝四图_2K"
OUT_DIR = PROJECT / "06_视频片段"
REF_DIR = OUT_DIR / "_ref_jpg"

# 每张图的运动提示词: (源图文件名, 输出片段名, prompt)
SHOTS = [
    (
        "晴枝_发布01_亮调微笑直视.png",
        "晴枝_片段01_亮调微笑直视_5s",
        "Cinematic live-photo portrait, use the reference image as the exact first frame. "
        "A young East Asian woman among pale pink blossoms, dappled sunlight on her face. "
        "0-2s: she holds soft eye contact with the camera while a gentle breeze lifts loose strands "
        "of her dark hair, petals and leaves sway softly. "
        "2-5s: her soft smile deepens slightly, one natural blink, flower shadows drift subtly across her cheek. "
        "Camera: very slow push-in toward her eyes, shallow depth of field, foreground blossoms in creamy bokeh. "
        "Photorealistic skin texture, fine art portrait photography, soft pastel color grading. "
        "Preserve her exact facial features and identity from the reference image throughout. "
        "Single continuous shot, no cuts. No text, no subtitles, no watermark, no logo.",
    ),
    (
        "晴枝_发布02_垂眸仰光.png",
        "晴枝_片段02_垂眸仰光_5s",
        "Cinematic live-photo portrait, use the reference image as the exact first frame. "
        "A young East Asian woman resting her cheek near her hand, eyes downcast, warm sunlight "
        "filtering through maple leaves. "
        "0-2s: serene stillness, leaf shadows flicker and drift across her face as foliage sways in a light breeze. "
        "2-5s: she slowly lifts her gaze halfway then lowers it again, lashes catching the warm light, "
        "hair strands drifting gently. "
        "Camera: slow lateral drift to the right with soft parallax from foreground leaves, shallow depth of field. "
        "Photorealistic skin texture, fine art portrait photography, warm amber color grading. "
        "Preserve her exact facial features and identity from the reference image throughout. "
        "Single continuous shot, no cuts. No text, no subtitles, no watermark, no logo.",
    ),
    (
        "晴枝_发布03_花影凝视.png",
        "晴枝_片段03_花影凝视_5s",
        "Cinematic live-photo portrait, use the reference image as the exact first frame. "
        "A young East Asian woman gazing through a gap between white blossom branches, cool daylight, "
        "lace-like shadows on her skin. "
        "0-2s: steady, intense gaze straight into the camera, blossoms and twigs sway slightly around her. "
        "2-5s: a subtle head tilt, her eyes keep tracking the lens, shadow patterns slide slowly across her face. "
        "Camera: slow lateral dolly to the left with strong foreground blossom parallax, shallow depth of field. "
        "Photorealistic skin texture, fine art portrait photography, cool slightly desaturated color grading. "
        "Preserve her exact facial features and identity from the reference image throughout. "
        "Single continuous shot, no cuts. No text, no subtitles, no watermark, no logo.",
    ),
    (
        "晴枝_发布04_侧目浅笑.png",
        "晴枝_片段04_侧目浅笑_5s",
        "Cinematic live-photo portrait, use the reference image as the exact first frame. "
        "A young East Asian woman glancing sideways with a gentle smile, golden sunlight, white flowers "
        "in the foreground. "
        "0-2s: she holds the side glance, breeze lifts wisps of her dark hair, foreground flowers sway softly. "
        "2-5s: she turns her head slightly toward the camera, the smile warms and widens a touch, "
        "sunlit shadows shift on her cheek. "
        "Camera: very slow pull-back revealing more blossoms around her, shallow depth of field. "
        "Photorealistic skin texture, fine art portrait photography, golden-hour color grading. "
        "Preserve her exact facial features and identity from the reference image throughout. "
        "Single continuous shot, no cuts. No text, no subtitles, no watermark, no logo.",
    ),
]
# --------------------------------------


def api_key() -> str:
    key = os.environ.get("ARK_API_KEY", "").strip()
    if not key:
        sys.exit("错误: 未设置环境变量 ARK_API_KEY")
    return key


def prep_ref_jpeg(src: Path) -> Path:
    """2K PNG 压成 max2048 JPEG, 控制 base64 体积"""
    REF_DIR.mkdir(parents=True, exist_ok=True)
    dst = REF_DIR / (src.stem + ".jpg")
    if dst.exists():
        return dst
    img = Image.open(src).convert("RGB")
    img.thumbnail((2048, 2048), Image.LANCZOS)
    img.save(dst, "JPEG", quality=92)
    return dst


def img_data_url(p: Path) -> str:
    b64 = base64.b64encode(p.read_bytes()).decode()
    return f"data:image/jpeg;base64,{b64}"


def http_json(url: str, payload=None, method="GET"):
    req = urllib.request.Request(
        url,
        data=json.dumps(payload).encode() if payload is not None else None,
        method=method,
        headers={
            "Authorization": f"Bearer {api_key()}",
            "Content-Type": "application/json",
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=120) as r:
            return json.loads(r.read().decode())
    except urllib.error.HTTPError as e:
        body = e.read().decode(errors="replace")
        sys.exit(f"API 错误 {e.code} @ {method} {url}\n{body}")


def submit(prompt: str, ref: Path) -> str:
    payload = {
        "model": MODEL,
        "content": [
            {"type": "text", "text": prompt},
            {
                "type": "image_url",
                "image_url": {"url": img_data_url(ref)},
                "role": "first_frame",
            },
        ],
        "ratio": RATIO,
        "resolution": RESOLUTION,
        "duration": DURATION,
        "generate_audio": False,   # 无BGM无音轨,纯画面剪辑素材
        "watermark": False,
    }
    resp = http_json(API_BASE, payload, "POST")
    task_id = resp.get("id")
    if not task_id:
        sys.exit(f"提交失败,响应: {json.dumps(resp, ensure_ascii=False)}")
    return task_id


def poll(task_id: str) -> dict:
    deadline = time.time() + TIMEOUT_MIN * 60
    while time.time() < deadline:
        resp = http_json(f"{API_BASE}/{task_id}")
        status = resp.get("status")
        if status == "succeeded":
            return resp
        if status in ("failed", "cancelled"):
            sys.exit(f"任务 {task_id} 状态 {status}: {json.dumps(resp, ensure_ascii=False)}")
        time.sleep(POLL_INTERVAL)
    sys.exit(f"任务 {task_id} 超时({TIMEOUT_MIN}min)")


def download(url: str, dst: Path):
    with urllib.request.urlopen(url, timeout=300) as r:
        dst.write_bytes(r.read())


def main():
    api_key()  # 先验证密钥存在
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    log_lines = [
        "# 晴枝 Seedance 2.0 图生视频 生成记录\n",
        f"- 模型: `{MODEL}`  分辨率: {RESOLUTION}  时长: {DURATION}s  比例: {RATIO}  音频: 关\n",
    ]

    # 1) 全部提交(并发排队,省时间)
    tasks = []
    for src_name, out_name, prompt in SHOTS:
        src = SRC_DIR / src_name
        if not src.exists():
            sys.exit(f"找不到源图: {src}")
        ref = prep_ref_jpeg(src)
        tid = submit(prompt, ref)
        print(f"[提交] {out_name} -> task {tid}")
        tasks.append((tid, out_name, src_name, prompt))

    # 2) 逐个轮询并下载
    for tid, out_name, src_name, prompt in tasks:
        resp = poll(tid)
        video_url = (resp.get("content") or {}).get("video_url")
        if not video_url:
            sys.exit(f"任务 {tid} 成功但无 video_url: {json.dumps(resp, ensure_ascii=False)}")
        dst = OUT_DIR / f"{out_name}.mp4"
        download(video_url, dst)
        mb = dst.stat().st_size / 1e6
        print(f"[完成] {dst.name}  {mb:.1f}MB")
        log_lines += [
            f"\n## {out_name}\n",
            f"- 源图: {src_name}\n- 任务ID: `{tid}`\n- 文件: `{dst.name}` ({mb:.1f}MB)\n",
            f"- Prompt:\n\n```\n{prompt}\n```\n",
        ]

    (OUT_DIR / "生成记录.md").write_text("".join(log_lines), encoding="utf-8")
    print(f"\n全部完成,输出目录: {OUT_DIR}")


if __name__ == "__main__":
    main()
