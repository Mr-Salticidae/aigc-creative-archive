# -*- coding: utf-8 -*-
"""管线验证: 用无人脸的花卉裁切图跑一次 i2v, 验证参数/计费/轮询/下载全链路"""
from pathlib import Path
from PIL import Image
import seedance2_i2v as s

s.RESOLUTION = "720p"  # 验证用低档,省费用

src = s.SRC_DIR / "晴枝_发布03_花影凝视.png"
img = Image.open(src).convert("RGB")
w, h = img.size
# 左侧白花前景区域(无人脸): 左 35% 宽, 中下 60% 高
crop = img.crop((0, int(h * 0.4), int(w * 0.35), h))
s.REF_DIR.mkdir(parents=True, exist_ok=True)
ref = s.REF_DIR / "_test_blossoms.jpg"
crop.save(ref, "JPEG", quality=92)
print(f"测试裁切图: {ref} {crop.size}")

prompt = (
    "White blossoms and green leaves swaying gently in a soft breeze, "
    "cool daylight, shallow depth of field, photorealistic, single continuous shot, "
    "no text, no watermark."
)
tid = s.submit(prompt, ref)
print(f"[提交] 管线测试 -> task {tid}")
resp = s.poll(tid)
video_url = (resp.get("content") or {}).get("video_url")
dst = s.OUT_DIR / "_pipeline_test.mp4"
s.download(video_url, dst)
print(f"[完成] {dst.name}  {dst.stat().st_size/1e6:.1f}MB")
