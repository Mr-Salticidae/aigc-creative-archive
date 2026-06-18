# -*- coding: utf-8 -*-
"""第02期 封面(MJ底图版) — 在水彩睡眠插画上叠栏目双层标题。左上留白放标题。"""
from PIL import Image, ImageDraw, ImageFont

W, H = 1080, 1440
CREAM=(239,235,223); INK=(35,66,63); CORAL=(216,100,58); GREY=(96,110,108); WHITE=(255,255,255)
FB="C:/Windows/Fonts/msyhbd.ttc"; FR="C:/Windows/Fonts/msyh.ttc"
def fb(s): return ImageFont.truetype(FB,s)
def fr(s): return ImageFont.truetype(FR,s)
M=90
SRC="E:/AIGC工作站/45_AI拆解球星身体_世界杯howto/01_素材_AI原图/MJ原图_夜醒篇_睡眠周期.png"
OUT="E:/AIGC工作站/45_AI拆解球星身体_世界杯howto/00_发布物料/02_夜醒篇/1_封面_夜醒篇.png"

# 底图 cover-fit 到 1080x1440(水平镜像:角色→右下,与左上标题对角平衡,且人物望向标题)
im=Image.open(SRC).convert("RGB")
im=im.transpose(Image.FLIP_LEFT_RIGHT)
r=max(W/im.width, H/im.height)
im=im.resize((int(im.width*r), int(im.height*r)), Image.LANCZOS)
ox=(im.width-W)//2; oy=(im.height-H)//2
img=im.crop((ox,oy,ox+W,oy+H))

# 左上轻奶油渐变(仅护标题,不洗插画):左→右、上→下双向衰减
prot=Image.new("L",(W,H),0)
pd=ImageDraw.Draw(prot)
for y in range(H):
    for_x_strength = max(0.0, 1 - y/640)       # 仅上部
    if for_x_strength<=0: continue
    a=int(150*for_x_strength)
    pd.line([(0,y),(int(W*0.62),y)], fill=a)   # 仅左侧62%
prot=prot.resize((W,H))
overlay=Image.new("RGB",(W,H),CREAM)
img=Image.composite(overlay,img,prot)

d=ImageDraw.Draw(img)
def tw(t,f): return d.textlength(t,font=f)

# 胶囊标签
lab="AI拆解球星身体 · 02"; f=fb(30); px,py=26,14
w=tw(lab,f); d.rounded_rectangle([M,70,M+w+px*2,70+44+py],radius=28,fill=INK)
d.text((M+px,70+py-2),lab,font=f,fill=WHITE)

# 设问(珊瑚点 + 灰青小字)
yq=168; cyq=yq+22
d.ellipse([M,cyq-9,M+18,cyq+9],fill=CORAL)
d.text((M+34,yq),"半夜总醒、睡得浅,以为是失眠?",font=fr(40),fill=GREY)

# 反转大标题(珊瑚强调"从不怕")
y=250; ft=fb(112)
for line in [[("C罗 ",INK),("从不怕",CORAL)],[("半夜醒来",INK)]]:
    cx=M
    for t,c in line:
        d.text((cx,y),t,font=ft,fill=c); cx+=tw(t,ft)
    y+=128
# 副标题
d.text((M,y+10),"醒在睡眠周期交界,是身体的设计",font=fr(44),fill=GREY)

img.save(OUT); print("saved",OUT)
