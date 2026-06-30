# -*- coding: utf-8 -*-
"""封面 — 在 B 水彩底图(人物躺右下、绿烟上升、珊瑚点)上叠标题。
左上留白放「设问→反转」双层标题,与右下人物对角平衡。"""
from PIL import Image, ImageDraw, ImageFont
import numpy as np

W, H = 1080, 1440
CREAM=(239,235,223); INK=(35,66,63); CORAL=(216,100,58); GREY=(96,110,108); WHITE=(255,255,255)
FB="C:/Windows/Fonts/msyhbd.ttc"; FR="C:/Windows/Fonts/msyh.ttc"
def fb(s): return ImageFont.truetype(FB,s)
def fr(s): return ImageFont.truetype(FR,s)
M=96
BASE="D:/AIGC工作站/50_滚刀_职场反内耗_唱唱反调/01_素材_AI原图/MJ原图_滚刀肉_躺云_B.png"
OUT ="D:/AIGC工作站/50_滚刀_职场反内耗_唱唱反调/00_发布物料/1_封面.png"

# 底图 cover-fit 到 1080x1440(不镜像:人物已在右下,标题放左上即对角)
im=Image.open(BASE).convert("RGB")
r=max(W/im.width, H/im.height)
im=im.resize((int(im.width*r), int(im.height*r)), Image.LANCZOS)
ox=(im.width-W)//2; oy=(im.height-H)//2
img=im.crop((ox,oy,ox+W,oy+H))

# 左上奶油护字渐变(仅护标题区,不洗插画):水平+垂直 smoothstep 双向软衰减,无硬边
def smooth(t): return t*t*(3-2*t)        # smoothstep
xs=np.arange(W); ys=np.arange(H)
x0,x1=int(W*0.40),int(W*0.84)            # 左0.40起全强度 → 右0.84平滑淡出为0
hx=1-smooth(np.clip((xs-x0)/(x1-x0),0,1))
y1=int(H*0.60)                           # 垂直方向上强下淡,到 0.60H 归零
vy=1-smooth(np.clip(ys/y1,0,1))
mask=(175*np.outer(vy,hx)).astype("uint8")
prot=Image.fromarray(mask,mode="L")
overlay=Image.new("RGB",(W,H),CREAM)
img=Image.composite(overlay,img,prot)

d=ImageDraw.Draw(img)
def tw(t,f): return d.textlength(t,font=f)

# 胶囊标签
lab="唱唱反调"; f=fb(30); px,py=26,13
w=tw(lab,f); d.rounded_rectangle([M,72,M+w+px*2,72+44+py],radius=28,fill=INK)
d.text((M+px,72+py-2),lab,font=f,fill=WHITE)

# 设问(珊瑚点 + 灰青小字)
yq=172; d.ellipse([M,yq+16,M+17,yq+33],fill=CORAL)
d.text((M+32,yq),"违心服从,内耗到怀疑人生?",font=fr(38),fill=GREY)

# 反转大标题(珊瑚强调"滚刀肉")
y=258; ft=fb(108)
for line in [[("我偏不改",INK)],[("把自己炖成",INK)],[("「滚刀肉」",CORAL)]]:
    cx=M
    for t,c in line:
        d.text((cx,y),t,font=ft,fill=c); cx+=tw(t,ft)
    y+=122
# 副标题(与标题块拉开间距,整体更透气)
d.text((M,y+50),"油盐不进,职场反而伤不到我",font=fr(42),fill=GREY)

img.save(OUT); print("saved",OUT)
