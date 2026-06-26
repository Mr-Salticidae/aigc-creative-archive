# -*- coding: utf-8 -*-
"""蒙眼剪辑 · 装配执行（build）
读取 config.SHOTS -> 统一规格 -> 拼接 -> 生成 ASS(字幕+人物卡) -> 烧录+混音 -> 成片。

逻辑在这里，参数在 config。改卡点/字幕不要动本文件。
用法：python build.py            # 全流程
      python build.py --probe    # 只打印时间轴，不渲染
"""
import os, sys, json, subprocess, shutil, tempfile
try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass
import config as C

HERE = os.path.dirname(os.path.abspath(__file__))
os.chdir(HERE)
WORK = os.path.join(HERE, "_work")
os.makedirs(WORK, exist_ok=True)

def run(cmd, **kw):
    r = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace", **kw)
    if r.returncode != 0:
        sys.stderr.write("CMD FAILED: " + " ".join(str(c) for c in cmd[:6]) + " ...\n")
        sys.stderr.write((r.stderr or "")[-1500:] + "\n")
        raise SystemExit(1)
    return r

def probe_dur(path):
    r = run(["ffprobe", "-v", "error", "-show_entries", "format=duration",
             "-of", "default=nk=1:nw=1", path])
    return float(r.stdout.strip())

# ---------- 1. 计算时间轴 ----------
timeline = []
t = 0.0
for s in C.SHOTS:
    f = os.path.normpath(os.path.join(HERE, s["file"]))
    if not os.path.exists(f):
        raise SystemExit(f"缺素材: {f}")
    d = probe_dur(f)
    timeline.append({**s, "abs": f, "start": t, "dur": d})
    t += d
TOTAL = t

def fmt(x):
    return f"{int(x//60):02d}:{x%60:06.3f}"

print(f"\n=== 时间轴（共 {len(timeline)} 镜头, 总时长 {fmt(TOTAL)}）===")
for i, s in enumerate(timeline):
    print(f"  {i+1:02d}. {s['id']:<9} {s['start']:6.2f}s +{s['dur']:5.2f}s  subs={len(s['subs'])}")
if "--probe" in sys.argv:
    raise SystemExit(0)

# ---------- 2. 统一规格 + 拼接 ----------
# --final-only：复用已有 base.mp4，只重做字幕/混音（迭代字幕、人物卡时秒级出片）
W, Hh = C.RESOLUTION
base = os.path.join(WORK, "base.mp4")
if "--final-only" in sys.argv and os.path.exists(base):
    print("\n=== 复用 base.mp4（--final-only，跳过重编码）===")
else:
    seg_paths = []
    print("\n=== 统一规格（缩放/帧率/编码）===")
    for i, s in enumerate(timeline):
        seg = os.path.join(WORK, f"seg_{i:02d}.mp4")
        run(["ffmpeg", "-y", "-v", "error", "-i", s["abs"],
             "-vf", f"scale={W}:{Hh}:flags=lanczos,fps={C.FPS},format=yuv420p",
             "-c:v", "libx264", "-preset", "medium", "-crf", "18",
             "-c:a", "aac", "-ar", "44100", "-ac", "2", seg])
        seg_paths.append(seg)
        print(f"  ✓ {s['id']}")

    listfile = os.path.join(WORK, "concat.txt")
    with open(listfile, "w", encoding="utf-8") as fp:
        for p in seg_paths:
            fp.write("file '" + p.replace("\\", "/") + "'\n")
    run(["ffmpeg", "-y", "-v", "error", "-f", "concat", "-safe", "0", "-i", listfile,
         "-c", "copy", base])
    print(f"  ✓ 拼接 -> base.mp4  ({fmt(probe_dur(base))})")

# ---------- 3. 生成 ASS（字幕 + 人物登场卡）----------
def ass_t(x):
    cs = int(round(x * 100)); h = cs // 360000; cs %= 360000
    m = cs // 6000; cs %= 6000; s = cs // 100; cs %= 100
    return f"{h:d}:{m:02d}:{s:02d}.{cs:02d}"

header = f"""[Script Info]
ScriptType: v4.00+
PlayResX: {W}
PlayResY: {Hh}
WrapStyle: 2
ScaledBorderAndShadow: yes

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Sub,{C.SUB_FONT},{C.SUB_FONTSIZE},&H00FFFFFF,&H00FFFFFF,&H00101010,&H7F000000,-1,0,0,0,100,100,0,0,1,{C.SUB_OUTLINE},2,2,90,90,{C.SUB_MARGIN_V},1
Style: Intro,{C.SUB_FONT},34,&H00FFFFFF,&H00FFFFFF,&H00101010,&H64000000,0,0,0,0,100,100,0,0,1,3,1,7,70,70,70,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""

events = []
# 字幕：每镜头内均匀铺开
for s in timeline:
    n = len(s["subs"])
    if not n:
        continue
    slot = s["dur"] / n
    for i, (_who, txt) in enumerate(s["subs"]):
        st = s["start"] + i * slot + C.SUB_PAD
        en = s["start"] + (i + 1) * slot - C.SUB_PAD
        if en - st < 0.5:
            en = st + max(0.5, slot * 0.8)
        events.append((0, st, en, "Sub", txt.replace("\n", "\\N")))

# 人物登场卡：name(大,金色) \N desc(小,白)
idx = {s["id"]: s for s in timeline}
GOLD = "{\\c&H00D7FF&}"   # 金色 (BGR)
for c in C.INTRO_CARDS:
    if c["at"] not in idx:
        continue
    st = idx[c["at"]]["start"] + c["t"]
    en = st + c["dur"]
    name = c["name"]
    txt = (f"{{\\fs54\\b1}}{GOLD}{name}{{\\r\\fs34}}\\N{c['desc']}")
    events.append((0, st, en, "Intro", txt))

events.sort(key=lambda e: e[1])
lines = [header]
for layer, st, en, style, txt in events:
    lines.append(f"Dialogue: {layer},{ass_t(st)},{ass_t(en)},{style},,0,0,0,,{txt}")
ass_path = os.path.join(WORK, "subs.ass")
with open(ass_path, "w", encoding="utf-8") as fp:
    fp.write("\n".join(lines))
print(f"  ✓ 字幕事件 {len([e for e in events if e[3]=='Sub'])} 条 + 人物卡 {len(C.INTRO_CARDS)} 张 -> subs.ass")

# ---------- 4. 烧录字幕 + 混音 -> 成片 ----------
out = os.path.normpath(os.path.join(HERE, C.OUTPUT))
os.makedirs(os.path.dirname(out), exist_ok=True)

# subtitles 烧录写进 filter_complex（-vf 与 -filter_complex 不能并用）；
# cwd=_work 下用相对名，规避 Windows 盘符冒号转义问题
vfilter = "[0:v]subtitles=subs.ass[vout]"
# 音频链：原生音频 dynaudnorm 统一响度；如配置 BGM 则混音
if C.BGM_FILE and os.path.exists(os.path.join(HERE, C.BGM_FILE)):
    bgm = os.path.normpath(os.path.join(HERE, C.BGM_FILE))
    inputs = ["-i", base, "-stream_loop", "-1", "-i", bgm]
    afilter = (f"[0:a]dynaudnorm=f=200:g=12,volume={C.NATIVE_AUDIO_GAIN_DB}dB[a0];"
               f"[1:a]volume={C.BGM_GAIN_DB}dB[a1];"
               f"[a0][a1]amix=inputs=2:duration=first:dropout_transition=0[aout]")
    print("  · 含 BGM 混音")
else:
    inputs = ["-i", base]
    afilter = f"[0:a]dynaudnorm=f=200:g=12,volume={C.NATIVE_AUDIO_GAIN_DB}dB[aout]"
    print("  · 仅原生音频（无 BGM）")

cmd = ["ffmpeg", "-y", "-v", "error", *inputs,
       "-filter_complex", vfilter + ";" + afilter,
       "-map", "[vout]", "-map", "[aout]",
       "-c:v", "libx264", "-preset", "medium", "-crf", "18", "-pix_fmt", "yuv420p",
       "-c:a", "aac", "-b:a", "192k", "-shortest", out]
print("\n=== 烧录字幕 + 输出成片 ===")
run(cmd, cwd=WORK)
print(f"\n✅ 成片输出: {out}\n   时长 {fmt(probe_dur(out))}  规格 {W}x{Hh}@{C.FPS}")
