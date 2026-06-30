# -*- coding: utf-8 -*-
"""backbone_v3：抛弃 bed2。bed1 完整四波爬升 → 自然塌陷成死寂 → 尾部留白（黑屏+品牌文案）。
   纯粹蒙眼剪辑法：结尾零生成素材，只有真静默 + 代码文字。"""
import wave, numpy as np
BASE = r"E:\AIGC工作站\50_蒙眼剪辑教学案例_MUTE降噪耳机广告\素材\音频"
BED1 = BASE + r"\bed1_噪音build.wav"
OUT  = BASE + r"\backbone_v3.wav"
SR = 48000
CFG = {
    "build_src": (0.00, 30.00),  # 完整第一乐章，含自然塌陷；切在 30.05 谷底前、新乐章(30.075)砸进来之前
    "build_fadeout_ms": 5,       # 尾部已近零，仅防爆音；保留自然停滞，不做硬切
    "tail_silence_s": 3.5,       # 黑屏 + 品牌文案浮现的留白（纯静默，无 bed2、无 beep）
}
def load_stereo(path):
    w=wave.open(path,'rb');sr=w.getframerate();ch=w.getnchannels()
    a=np.frombuffer(w.readframes(w.getnframes()),dtype=np.int16).astype(np.float32)/32768.0;w.close()
    a=a.reshape(-1,ch)[:,:2] if ch>1 else np.stack([a,a],1)
    return a,sr
bed1,sr=load_stereo(BED1); assert sr==SR
b=bed1[int(CFG["build_src"][0]*SR):int(CFG["build_src"][1]*SR)].copy()
n=int(CFG["build_fadeout_ms"]*SR/1000); b[-n:]*=np.linspace(1,0,n)[:,None]
tail=np.zeros((int(CFG["tail_silence_s"]*SR),2),np.float32)
mix=np.concatenate([b,tail],0)
pk=np.abs(mix).max();
if pk>0.99: mix*=0.99/pk
wave_out=wave.open(OUT,'wb');wave_out.setnchannels(2);wave_out.setsampwidth(2);wave_out.setframerate(SR)
wave_out.writeframes((np.clip(mix,-1,1)*32767).astype(np.int16).tobytes());wave_out.close()
tb=len(b)/SR; tot=len(mix)/SR
print("=== backbone_v3 ===")
print(f"  0.00-{tb:.2f}s  BUILD  bed1[0-30] 完整四波 -> ~29.2s 自然塌陷 -> 死寂")
print(f"  {tb:.2f}-{tot:.2f}s  TAIL   {CFG['tail_silence_s']}s 纯静默留白（黑屏+品牌文案）")
print(f"  全长 = {tot:.2f}s  | 无 bed2 / 无 beep")
print(f"  out = {OUT}")
