"""OCR the subtitle band frames from the reference film -> subtitle segments.

Frames were sampled at 2 fps from 成片v2 (bottom 280px band). We OCR each,
keep the longest high-confidence line (the subtitle), then merge consecutive
frames with the same text into timed segments.
"""
import os, glob, json, re, sys

FRAMES = os.path.join(os.path.dirname(__file__), "..", "02_素材", "reference", "_sub")
OUT = os.path.join(os.path.dirname(__file__), "..", "03_剪辑流程", "ref_subtitles.json")
FPS = 2.0

from paddleocr import PaddleOCR

ocr = PaddleOCR(lang="ch", use_textline_orientation=False,
                use_doc_orientation_classify=False, use_doc_unwarping=False)

def frame_time(idx):
    # frame idx (1-based) sampled at FPS -> midpoint time
    return round((idx - 0.5) / FPS, 2)

def ocr_frame(path):
    try:
        res = ocr.predict(path)
    except Exception:
        try:
            res = ocr.ocr(path)
        except Exception as e:
            print(f"    [skip] {os.path.basename(path)}: {str(e)[:50]}", flush=True)
            return ""
    texts, scores = [], []
    for page in res:
        # paddleocr 3.x: page is dict-like with rec_texts/rec_scores
        if isinstance(page, dict):
            texts += list(page.get("rec_texts", []))
            scores += list(page.get("rec_scores", []))
        else:
            for line in (page or []):
                try:
                    texts.append(line[1][0]); scores.append(line[1][1])
                except Exception:
                    pass
    # keep high-confidence, drop tiny fragments; join multi-line subtitle
    cand = [t.strip() for t, s in zip(texts, scores) if s and s > 0.6 and len(t.strip()) >= 2]
    if not cand:
        return ""
    # subtitle is usually the longest CJK line
    cand.sort(key=lambda t: -len(t))
    return cand[0]

frames = sorted(glob.glob(os.path.join(FRAMES, "f_*.jpg")))
rows = []
for i, f in enumerate(frames, 1):
    t = frame_time(i)
    txt = ocr_frame(f)
    rows.append((t, txt))
    if i % 30 == 0:
        print(f"  ...{i}/{len(frames)} t={t}s", flush=True)

def norm(s):
    return re.sub(r"[\s，。！？、,.!?]", "", s)

# merge consecutive equal(ish) texts into segments
segs = []
for t, txt in rows:
    if not txt:
        continue
    if segs and norm(segs[-1]["text"]) == norm(txt):
        segs[-1]["end"] = t
    elif segs and norm(txt) and (norm(txt) in norm(segs[-1]["text"]) or norm(segs[-1]["text"]) in norm(txt)):
        # one is substring of other (OCR jitter) -> keep longer, extend
        if len(txt) > len(segs[-1]["text"]):
            segs[-1]["text"] = txt
        segs[-1]["end"] = t
    else:
        segs.append({"start": t, "end": t, "text": txt})

# pad single-frame segments and drop ultra-short noise
clean = []
for s in segs:
    if s["end"] == s["start"]:
        s["end"] = round(s["start"] + 0.5, 2)
    if (s["end"] - s["start"]) >= 0.4 and len(norm(s["text"])) >= 2:
        clean.append(s)

with open(OUT, "w", encoding="utf-8") as fp:
    json.dump(clean, fp, ensure_ascii=False, indent=1)

print(f"\n{len(clean)} subtitle segments -> {OUT}")
for s in clean:
    print(f"  {s['start']:6.2f}-{s['end']:6.2f}  {s['text']}")
