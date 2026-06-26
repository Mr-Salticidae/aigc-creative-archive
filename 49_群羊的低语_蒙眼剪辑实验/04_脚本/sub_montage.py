"""Build readable montage strips of the reference film's subtitle band.

Samples a frame every STEP seconds, crops the bottom subtitle band, stamps the
timestamp, and stacks PER_IMG bands into tall images for direct visual reading.
"""
import os, cv2, numpy as np

REF = os.path.join(os.path.dirname(__file__), "..", "02_素材", "reference", "成片v2.mp4")
OUTDIR = os.path.join(os.path.dirname(__file__), "..", "02_素材", "reference", "_montage")
os.makedirs(OUTDIR, exist_ok=True)

STEP = 2.5          # seconds between samples
PER_IMG = 18        # bands per montage image
BAND_TOP = 900      # crop top (of 1080)
BAND_H = 150

cap = cv2.VideoCapture(REF)
fps = cap.get(cv2.CAP_PROP_FPS)
total = cap.get(cv2.CAP_PROP_FRAME_COUNT) / fps

times = [round(t, 1) for t in np.arange(1.0, total, STEP)]
bands = []
for t in times:
    cap.set(cv2.CAP_PROP_POS_MSEC, t * 1000)
    ok, fr = cap.read()
    if not ok:
        continue
    band = fr[BAND_TOP:BAND_TOP + BAND_H, :].copy()
    # darken a label box and write the timestamp
    cv2.rectangle(band, (0, 0), (110, 34), (0, 0, 0), -1)
    cv2.putText(band, f"{t:.1f}s", (5, 25), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 255), 2)
    cv2.line(band, (0, BAND_H - 1), (band.shape[1], BAND_H - 1), (0, 200, 0), 1)
    bands.append(band)
cap.release()

for gi in range(0, len(bands), PER_IMG):
    chunk = bands[gi:gi + PER_IMG]
    img = np.vstack(chunk)
    path = os.path.join(OUTDIR, f"montage_{gi // PER_IMG:02d}.jpg")
    ok, buf = cv2.imencode(".jpg", img, [cv2.IMWRITE_JPEG_QUALITY, 88])
    with open(path, "wb") as fp:
        fp.write(buf.tobytes())
    print(os.path.basename(path), img.shape)
print(f"{len(bands)} bands over {total:.0f}s")
