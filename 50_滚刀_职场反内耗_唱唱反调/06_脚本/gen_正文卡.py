# -*- coding: utf-8 -*-
"""正文卡 ×8 — 奶油底,墨青标题+珊瑚强调,灰青正文。一页一概念,论证式carousel。
配色/字体沿用账号栏目规范,与水彩封面统一。"""
from PIL import Image, ImageDraw, ImageFont

W, H = 1080, 1440
CREAM=(239,235,223); INK=(35,66,63); CORAL=(216,100,58); GREY=(96,110,108); WHITE=(255,255,255)
FB="C:/Windows/Fonts/msyhbd.ttc"; FR="C:/Windows/Fonts/msyh.ttc"
def fb(s): return ImageFont.truetype(FB,s)
def fr(s): return ImageFont.truetype(FR,s)
M=100
OUTDIR="D:/AIGC工作站/50_滚刀_职场反内耗_唱唱反调/00_发布物料/"

I,C,G=INK,CORAL,GREY
# 每卡: kicker, headline(行→runs), body(行→runs;None=空行)
CARDS=[
 ("共鸣",
  [[("你是不是也这样?",I)]],
  [[("不喜欢老板,也不喜欢同事,",G)],
   [("却不得不违心点头、配合。",G)],
   [('笑着说"好的,我改",',G)],
   [("回到家,整个人是空的。",G)],
   None,
   [("这不是累 —— 是",G),("「内耗」",C),("。",G)]]),
 ("主流答案",
  [[("他们说:要么改变,",I)],[("要么离开。",I)]],
  [[('可"改变自己去适应",',G)],
   [("是把对方的标准,请进自己心里;",G)],
   [('"正面硬刚或者裸辞",',G)],
   [("成本又高得吓人。",G)],
   None,
   [("两条路,其实都很累。",G)]]),
 ("我的反调",
  [[("我的第三条路:",I)],[("战术性",I),("装笨",C)],
  ],
  [[("我表演得",G),("超级努力",C),("地,",G)],
   [('接受你的每一条"好建议",',G)],
   [("像当年学数学最认真、",G)],
   [("却怎么都学不会的那个同学——",G)],
   None,
   [("一拳,打进棉花里。",G)]]),
 ("怎么操作",
  [[("好为人师的人,",I)],[("最怕",I),("「教不会」",C)]],
  [[("你越教,我越点头;",G)],
   [('越认真,越"学不会"。',G)],
   [("久了,对方觉得我",G),("朽木不可雕",C),(",",G)],
   None,
   [("自然就不来找我麻烦了。",G)]]),
 ("往深挖",
  [[("内耗的根源,",I)],[("不是被改变",I)]],
  [[("是你",G),("「当真」",C),("了。",G)],
   [("滚刀的本质,是把一段",G)],
   [("你掌控不了的关系,",G)],
   [("降格成一场你完全掌控的表演。",G)],
   None,
   [("你不是输了 —— 是",G),("退出了游戏",C),("。",G)]]),
 ("理论撑腰 ①",
  [[("这叫",I)],[("「弱者的武器」",C)]],
  [[("人类学家 James Scott 发现:",G)],
   [("真正普遍的反抗从不是起义,",G)],
   [("而是磨洋工、装糊涂、假顺从。",G)],
   None,
   [('庄子也说:那棵"没用"的树,',G)],
   [("反而活到了最后。",G)]]),
 ("理论撑腰 ②",
  [[("把别人的期待,",I)],[("还给别人",I)]],
  [[("阿德勒",G),("「课题分离」",C),(":",G)],
   [("他爱不爱教,是他的课题;",G)],
   [("你心里平不平静,是你的课题。",G)],
   None,
   [("我配合演出,",G)],
   [("但你的评价,进不来我的世界。",G)]]),
 ("边界 & 金句",
  [[("但请记住一条",I)],[("别把自己骗了",I)]],
  [[("滚刀对付的是",G),("「控制欲」",C),(",",G)],
   [("不是你真正该学的本事。",G)],
   [("对前者装笨是自保,",G)],
   [("对后者装笨,是自欺。",G)],
   None,
   [("真正的成熟,不是学会对抗,",I)],
   [("而是学会",I),("「有选择地无能」",C),("。",I)]]),
]

def draw_runs(d,x,y,runs,font):
    cx=x
    for t,c in runs:
        d.text((cx,y),t,font=font,fill=c); cx+=d.textlength(t,font=font)

for idx,(kicker,head,body) in enumerate(CARDS, start=1):
    img=Image.new("RGB",(W,H),CREAM); d=ImageDraw.Draw(img)
    # kicker: 珊瑚点 + 小标 + 页码
    ky=120; d.ellipse([M,ky+10,M+18,ky+28],fill=CORAL)
    d.text((M+34,ky),kicker,font=fb(34),fill=INK)
    pg=f"{idx:02d} / 08"; pf=fr(30); d.text((W-M-d.textlength(pg,font=pf),ky+4),pg,font=pf,fill=GREY)
    # headline
    hf=fb(78); y=232
    for line in head:
        draw_runs(d,M,y,line,hf); y+=98
    # 珊瑚短线
    ry=y+6; d.rounded_rectangle([M,ry,M+118,ry+9],radius=4,fill=CORAL)
    # body
    bf=fr(43); y=ry+62
    for line in body:
        if line is None: y+=34; continue
        draw_runs(d,M,y,line,bf); y+=70
    # footer
    ff=fr(28); foot="唱唱反调 · 不吃压力之人"
    d.text((M,H-86),foot,font=ff,fill=GREY)
    out=f"{OUTDIR}{idx+1}_正文_{kicker.replace(' ','').replace('①','1').replace('②','2')}.png"
    img.save(out); print("saved",out)
print("done 8 cards")
