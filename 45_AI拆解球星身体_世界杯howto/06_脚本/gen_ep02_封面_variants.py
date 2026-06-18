# -*- coding: utf-8 -*-
"""第02期封面构图对比:解决"文字+角色都在左侧"的偏沉问题。"""
from PIL import Image, ImageDraw, ImageFont

W,H=1080,1440
CREAM=(239,235,223); INK=(35,66,63); CORAL=(216,100,58); GREY=(96,110,108); WHITE=(255,255,255)
def fb(s): return ImageFont.truetype("C:/Windows/Fonts/msyhbd.ttc",s)
def fr(s): return ImageFont.truetype("C:/Windows/Fonts/msyh.ttc",s)
M=90
SRC="E:/AIGC工作站/45_AI拆解球星身体_世界杯howto/01_素材_AI原图/MJ原图_夜醒篇_睡眠周期.png"
OUTD="E:/AIGC工作站/45_AI拆解球星身体_世界杯howto/00_发布物料/02_夜醒篇/_构图对比/"
import os; os.makedirs(OUTD, exist_ok=True)

def load_bg(mirror=False):
    im=Image.open(SRC).convert("RGB")
    if mirror: im=im.transpose(Image.FLIP_LEFT_RIGHT)
    r=max(W/im.width,H/im.height)
    im=im.resize((int(im.width*r),int(im.height*r)),Image.LANCZOS)
    ox=(im.width-W)//2; oy=(im.height-H)//2
    return im.crop((ox,oy,ox+W,oy+H))

def wash(img, side):
    """side: 'left'/'top'/'right' 轻奶油护字层"""
    m=Image.new("L",(W,H),0); pd=ImageDraw.Draw(m)
    if side in ("left","right"):
        for y in range(H):
            s=max(0.0,1-y/660)
            if s<=0: continue
            a=int(150*s)
            if side=="left": pd.line([(0,y),(int(W*0.60),y)],fill=a)
            else:            pd.line([(int(W*0.40),y),(W,y)],fill=a)
    else:  # top 全宽
        for y in range(H):
            a=int(140*max(0.0,1-y/560)); pd.line([(0,y),(W,y)],fill=a)
    ov=Image.new("RGB",(W,H),CREAM)
    return Image.composite(ov,img,m)

def pill(d, x):
    lab="AI拆解球星身体 · 02"; f=fb(30); px,py=26,14
    w=d.textlength(lab,font=f)
    if x=="center": x0=(W-(w+px*2))/2
    elif x=="right": x0=W-M-(w+px*2)
    else: x0=M
    d.rounded_rectangle([x0,70,x0+w+px*2,70+44+py],radius=28,fill=INK)
    d.text((x0+px,70+py-2),lab,font=f,fill=WHITE)
    return x0

def title(d, align):
    f=fb(112); fq=fr(40); fs=fr(44)
    lines=[[("C罗 ",INK),("从不怕",CORAL)],[("半夜醒来",INK)]]
    q="半夜总醒、睡得浅,以为是失眠?"; sub="醒在睡眠周期交界,是身体的设计"
    def width(line): return sum(d.textlength(t,font=f) for t,_ in line)
    if align=="center":
        # 设问居中(带点)
        qw=d.textlength(q,font=fq); dot=18; gap=16
        x0=(W-(qw+dot+gap))/2; cyq=168+22
        d.ellipse([x0,cyq-9,x0+18,cyq+9],fill=CORAL)
        d.text((x0+dot+gap,168),q,font=fq,fill=GREY)
        y=250
        for line in lines:
            lw=width(line); cx=(W-lw)/2
            for t,c in line: d.text((cx,y),t,font=f,fill=c); cx+=d.textlength(t,font=f)
            y+=128
        sw=d.textlength(sub,font=fs); d.text(((W-sw)/2,y+10),sub,font=fs,fill=GREY)
    else:
        ax = M if align=="left" else None
        # right对齐:整体右贴边
        cyq=168+22
        if align=="left":
            d.ellipse([M,cyq-9,M+18,cyq+9],fill=CORAL); d.text((M+34,168),q,font=fq,fill=GREY)
            y=250
            for line in lines:
                cx=M
                for t,c in line: d.text((cx,y),t,font=f,fill=c); cx+=d.textlength(t,font=f)
                y+=128
            d.text((M,y+10),sub,font=fs,fill=GREY)
        else:  # right
            qw=d.textlength(q,font=fq)
            d.text((W-M-qw,168),q,font=fq,fill=GREY)
            d.ellipse([W-M-qw-34,cyq-9,W-M-qw-16,cyq+9],fill=CORAL)
            y=250
            for line in lines:
                lw=width(line); cx=W-M-lw
                for t,c in line: d.text((cx,y),t,font=f,fill=c); cx+=d.textlength(t,font=f)
                y+=128
            sw=d.textlength(sub,font=fs); d.text((W-M-sw,y+10),sub,font=fs,fill=GREY)

def make(name, mirror, align, washside):
    img=load_bg(mirror); img=wash(img,washside)
    d=ImageDraw.Draw(img); pill(d, "center" if align=="center" else ("right" if align=="right" else "left"))
    title(d, align)
    img.save(OUTD+name); print("saved",name)

# A 原图 + 标题居中(打散左侧重量)
make("A_原图_标题居中.png", False, "center", "top")
# B 镜像(角色→右下) + 标题左上(对角平衡)
make("B_镜像_标题左上.png", True, "left", "left")
# C 镜像(角色→右下) + 标题居中
make("C_镜像_标题居中.png", True, "center", "top")
print("DONE")
