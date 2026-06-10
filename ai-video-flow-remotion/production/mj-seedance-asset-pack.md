# AI视频创作流程 - MJ / Seedance 素材生产包

> Project: `ai-video-flow-remotion`
> Format: Bilibili horizontal 16:9
> Target use: Replace or enrich the current programmatic Remotion scenes with generated key visuals and short motion inserts.

## Global Rules

- Generate one Midjourney key image per scene first.
- Use each selected MJ image as `@Image1` in Seedance.
- Keep all visuals text-free. Remotion owns subtitles and on-screen text.
- Leave the bottom 18% of the frame clean for Remotion captions.
- Do not upload realistic human faces to Seedance. Use symbolic, flat-vector, non-realistic figures only.
- Recommended Midjourney suffix: `--ar 16:9 --v 8.1 --style raw --no text logo watermark brand signature subtitles caption realistic human face photorealism anime 3d render`
- Recommended Seedance setting: 16:9, 720p or highest available, 8s for short scenes, 10s for complex scenes.

## File Naming

```text
production/
  assets/
    scene_01_hook_key.png
    scene_01_hook_motion.mp4
    scene_02_core_shift_key.png
    scene_02_core_shift_motion.mp4
    ...
```

## Scene 01 - Hook

Purpose: Show that generating isolated shots does not equal making a coherent film.

Midjourney prompt:

```text
flat vector educational explainer frame, dark clean editorial background, scattered AI prompt cards and a small model node feeding into a single bright film shot card, the shot card fails to connect to a broken editing timeline on the right, visual metaphor for "many shots but no film", crisp geometric shapes, warm paper-white cards, cyan and orange accents, subtle grain, restrained in-a-nutshell style, clear bottom caption-safe empty area, no readable text --ar 16:9 --v 8.1 --style raw --no text logo watermark brand signature subtitles caption realistic human face photorealism anime 3d render
```

Seedance prompt:

```text
@Image1 as the first frame and visual style reference. Create an 8-second flat-vector educational explainer animation. Keep the same dark editorial background, geometric cards, cyan and orange accents, and clean bottom caption-safe area. 0-2s: the prompt cards on the left gently slide toward the model node. 2-4s: the model node emits a bright pulse into the single film shot card. 4-6s: the shot card tries to connect to the editing timeline, but the connection line flickers and breaks. 6-8s: the broken timeline shakes subtly, then settles. Camera mostly locked with a very slow push-in. Sound design: soft digital clicks and one muted glitch at the break. No readable text, no logo, no watermark.
```

## Scene 02 - Core Shift

Purpose: Move the viewer from tool obsession to theme, viewpoint, and script.

Midjourney prompt:

```text
flat vector explainer illustration, two loose AI tool cards on the left labeled only by abstract icons, flowing through a funnel into a large central glowing theme compass, then connecting to a clean script document on the right, metaphor for moving from prompts and models to theme and screenplay, dark modern background, paper-white panels, cyan blue and warm yellow accents, editorial education style, strong hierarchy, clean bottom caption-safe empty area, no readable text --ar 16:9 --v 8.1 --style raw --no text logo watermark brand signature subtitles caption realistic human face photorealism anime 3d render
```

Seedance prompt:

```text
@Image1 as the first frame and visual style reference. Create a 9-second flat-vector explainer animation. 0-2s: the two tool cards drift loosely on the left. 2-5s: the cards compress through the funnel and transform into a glowing theme compass in the center. 5-7s: a thin line grows from the compass to the script document on the right. 7-9s: the script document opens slightly and emits a calm warm glow. Camera: slow push-in, no cuts. Sound: soft paper movement, gentle compression whoosh. Keep the bottom area clean for captions. No readable text, no logo, no watermark.
```

## Scene 03 - Structure

Purpose: Explain scene, beat, and shot as the video equivalent of paragraph, sentence, and word.

Midjourney prompt:

```text
flat vector educational diagram, a large paragraph block morphing into a film production hierarchy, three nested visual layers: wide scene block, middle beat group block, small shot cards, clean geometric composition, dark background, paper-white diagram panels, blue orange cyan accents, subtle arrows and modular layout, readable through icons only, bottom caption-safe empty area, no text --ar 16:9 --v 8.1 --style raw --no text logo watermark brand signature subtitles caption realistic human face photorealism anime 3d render
```

Seedance prompt:

```text
@Image1 as the first frame and visual style reference. Create a 10-second educational explainer animation. 0-3s: the paragraph-like block on the left separates into three horizontal layers. 3-6s: the layers reorganize into a film structure diagram: one large scene container, several beat groups, and multiple shot cards. 6-10s: the camera slowly pushes toward the smallest shot cards while connection lines light up in sequence. Keep all elements abstract and text-free. Sound: light modular clicks, calm educational tone. Keep bottom caption area clean.
```

## Scene 04 - Emotion To Visual

Purpose: Translate "despair" into camera, lighting, and color decisions.

Midjourney prompt:

```text
symbolic flat-vector cinematic explainer frame, abstract non-realistic human silhouette on the left, surrounded by visual language control panels: shaky camera icon, dolly zoom lens icon, cold blue color grade panel, dark low-key lighting panel, mood changes shown through light and composition not facial realism, dark restrained background, cool blue and muted red contrast, editorial film education style, bottom caption-safe empty area, no readable text --ar 16:9 --v 8.1 --style raw --no text logo watermark brand signature subtitles caption realistic human face photorealism anime 3d render
```

Seedance prompt:

```text
@Image1 as the first frame and visual style reference. Create a 10-second symbolic flat-vector film-language explainer animation. 0-2s: the abstract human silhouette appears in neutral light. 2-4s: the camera-control panel vibrates gently to show handheld shake. 4-6s: a lens icon performs a subtle Hitchcock zoom effect while the background compresses inward. 6-8s: a cold blue color wash slides across the frame. 8-10s: low-key dark lighting closes around the silhouette, then settles into a clear final composition. No realistic face, no text, no logo. Keep bottom caption area clean. Sound: low soft pulse, small camera mechanism clicks.
```

## Scene 05 - Director Skills

Purpose: Define the AI director's three abilities: writing logic, audiovisual language, editing thinking.

Midjourney prompt:

```text
flat vector explainer frame, central symbolic AI director figure without realistic face, surrounded by a balanced triangle of three visual modules: script logic represented by a screenplay stack, audiovisual language represented by camera lens and sound wave, editing thinking represented by timeline strips and cut marks, dark editorial background, warm yellow cyan orange palette, confident educational composition, clean lower caption-safe zone, no readable text --ar 16:9 --v 8.1 --style raw --no text logo watermark brand signature subtitles caption realistic human face photorealism anime 3d render
```

Seedance prompt:

```text
@Image1 as the first frame and visual style reference. Create a 9-second flat-vector educational animation. 0-2s: the central symbolic AI director figure appears with a soft pulse. 2-4s: the screenplay stack module lights up. 4-6s: the camera lens and sound wave module lights up. 6-8s: the editing timeline module lights up. 8-9s: all three modules connect into a stable triangle around the director. Camera locked with slight breathing push-in. No readable text, no realistic face, no logo. Keep bottom caption area clean.
```

## Scene 06 - Editing Logic

Purpose: Show editing as information processing, combination, and creation, not flashy technique.

Midjourney prompt:

```text
flat vector editorial explainer illustration, three information cards flow into a horizontal editing timeline, cards transform into ordered film strips, subtle cut marks and rhythm nodes, a restrained warning icon for "not showing off", dark clean background, paper-white timeline, cyan yellow green cards, orange accent, clear educational hierarchy, bottom caption-safe empty area, no readable text --ar 16:9 --v 8.1 --style raw --no text logo watermark brand signature subtitles caption realistic human face photorealism anime 3d render
```

Seedance prompt:

```text
@Image1 as the first frame and visual style reference. Create a 10-second flat-vector editing logic animation. 0-3s: three information cards enter from different directions. 3-6s: the cards snap into the horizontal timeline as ordered film strips. 6-8s: cut marks and rhythm nodes light up one by one, showing controlled editing. 8-10s: the flashy warning icon dims while the timeline becomes stable and readable. Camera: slow lateral track along the timeline. Sound: soft click cuts, no dramatic whoosh. No text, no logo, no watermark. Keep bottom caption area clean.
```

## Scene 07 - Takeaway

Purpose: Close with the core principle: clarify expression first, then let AI shoot.

Midjourney prompt:

```text
flat vector closing frame, a clear theme compass on the left connects to a calm AI shooting module in the center, then to a complete film timeline on the right, visual metaphor for "clarify expression first, then let AI shoot", dark refined educational background, warm paper-white panels, yellow cyan green accents, clean confident final composition, subtle spotlight, bottom caption-safe empty area, no readable text --ar 16:9 --v 8.1 --style raw --no text logo watermark brand signature subtitles caption realistic human face photorealism anime 3d render
```

Seedance prompt:

```text
@Image1 as the first frame and visual style reference. Create an 8-second flat-vector closing animation. 0-2s: the theme compass glows on the left. 2-4s: a connection line grows toward the AI shooting module in the center. 4-6s: the line continues into the final film timeline on the right. 6-8s: all three modules hold steady, with a gentle final glow and no extra movement. Camera: very slow pull back to reveal the whole workflow. Sound: calm resolution tone, soft final click. No readable text, no logo, no watermark. Keep bottom caption area clean.
```

## Remotion Integration Plan After Assets Return

1. Put selected MJ images and Seedance videos in `production/assets/`.
2. Copy final videos into `public/video/ai_video_flow/`.
3. Add a `sceneAssets.ts` file with one `video-insert` binding per scene.
4. Update `SceneRenderer` so generated video inserts sit behind Remotion subtitles and above the procedural fallback.
5. Re-render `out/ai-video-flow.mp4` and compare against the current programmatic version.

## Quality Checklist

- MJ output is text-free and has a clean lower caption area.
- Seedance output keeps the same flat-vector style and does not invent readable labels.
- Each Seedance clip is visually calm enough for subtitles and TTS.
- No generated asset contains realistic human faces.
- Motion shows the concept clearly without replacing Remotion captions.
