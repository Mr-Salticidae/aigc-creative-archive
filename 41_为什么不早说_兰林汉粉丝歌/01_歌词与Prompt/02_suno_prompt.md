# 《为什么不早说》· Suno Prompt

> 作品序号：004
> 用途：记录本曲成品方向与可复跑参数
> 建档：2026-06-10
> 当前状态：成品 WAV 已归档

---

## Style of Music

```text
Mandarin stubborn meme-pop anthem, heavy mid-tempo pop groove, punchy drums, low bass, tense minimal synth riff, spoken-sung male vocal with defiant attitude, repetitive chant chorus, call-and-response adlibs, Verse 2 slightly faster and more defensive, sarcastic livestream catchphrases, full song structure
```

## Exclude Styles

```text
cute, cheerful, blessing song, children song, happy jingle, comedy skit, serious rap, hard trap, boombap, EDM drop, rock chorus, pop ballad, female lead vocal, long instrumental intro, autotune-heavy vocal
```

## Title

```text
为什么不早说
```

## Lyrics

见同目录 `01_lyrics.md`。

---

## Prompt 设计说明

### 方向

本曲最终不走“中文硬说唱”，也不走“轻快享福式梗歌”，而是：

```text
嘴硬宣言式流行梗歌
```

需要同时满足两个目标：

- 有流行梗歌的传播性；
- 人声态度必须硬，像顶嘴和死不认。

### 关键约束

- `stubborn meme-pop anthem`：把梗歌做成宣言，不做可爱段子。
- `heavy mid-tempo pop groove`：中速偏重，避免轻快。
- `spoken-sung male vocal with defiant attitude`：口语旋律化，但态度强硬。
- `call-and-response adlibs`：保留直播间关系。
- `Verse 2 slightly faster and more defensive`：第二段解释堆叠，制造“越说越急”的听感。

### 标签修正

Suno 更稳定识别标准英文标签，因此成品归档中采用：

```text
[Both]
```

替代原始草稿里的：

```text
[audience]
```

同时将 `speed up` 放入 Style 描述，而不是写成自定义段落标签。

