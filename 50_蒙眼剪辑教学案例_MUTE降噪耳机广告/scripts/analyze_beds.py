# -*- coding: utf-8 -*-
import wave, numpy as np, sys

BASE = r"E:\AIGC工作站\50_蒙眼剪辑教学案例_MUTE降噪耳机广告\素材\音频"
FILES = {"bed1": BASE + r"\bed1_噪音build.wav",
         "bed2": BASE + r"\bed2_回暖calm.wav"}

def load(path):
    w = wave.open(path, 'rb')
    sr = w.getframerate(); ch = w.getnchannels(); sw = w.getsampwidth(); n = w.getnframes()
    raw = w.readframes(n); w.close()
    dt = {1: np.int8, 2: np.int16, 4: np.int32}[sw]
    a = np.frombuffer(raw, dtype=dt).astype(np.float64)
    if ch > 1: a = a.reshape(-1, ch).mean(axis=1)
    a /= (np.abs(a).max() + 1e-9)   # normalize to [-1,1]
    return a, sr, ch, n/sr

def rms_env(a, sr, win=0.10):
    w = int(sr*win);
    if w < 1: w = 1
    nb = len(a)//w
    buckets = a[:nb*w].reshape(nb, w)
    rms = np.sqrt((buckets**2).mean(axis=1))
    t = np.arange(nb)*win
    return t, rms

for name, path in FILES.items():
    a, sr, ch, dur = load(path)
    t, rms = rms_env(a, sr, 0.10)
    rmsn = rms/(rms.max()+1e-9)
    print(f"\n===== {name} =====")
    print(f"path: {path}")
    print(f"sr={sr}  ch={ch}  duration={dur:.2f}s  peakRMS@={t[int(np.argmax(rms))]:.2f}s")
    # coarse envelope every 0.5s for eyeballing shape
    print("envelope (0.5s buckets, normalized RMS, bar):")
    step = 5  # 0.5s
    for i in range(0, len(rmsn), step):
        seg = rmsn[i:i+step]
        v = seg.mean()
        bar = "#"*int(round(v*40))
        print(f"  {t[i]:5.1f}s |{bar:<40}| {v:.3f}")
    if name == "bed1":
        # locate climax + the sudden stop after climax
        pk = int(np.argmax(rms))
        thr = 0.08*rms[pk]
        stop = None
        for i in range(pk, len(rms)):
            if rms[i] < thr:
                # confirm it stays low for >=0.5s
                if np.all(rms[i:i+5] < thr*1.5):
                    stop = i; break
        print(f"  >>> climax at {t[pk]:.2f}s")
        if stop is not None:
            print(f"  >>> SUDDEN STOP (drops below 8% of peak) at {t[stop]:.2f}s")
            print(f"  >>> usable build window: ~0.0s -> {t[stop]:.2f}s, the CUT lands at the climax->stop edge")
        else:
            print("  >>> no hard stop detected by threshold; inspect envelope tail above")
    if name == "bed2":
        # find a stable calm window: longest run where rms within [0.4,1.0]*max and low variance
        print(f"  >>> overall mean normalized RMS={rmsn.mean():.3f} (calm bed should be fairly flat)")
