# DESIGN.md: 1-Bit Duotone Dithered Anime Aesthetic

## 1. Visual Overview
A retro 1-bit pixel art style inspired by Japanese PC-98 visual novels and early Macintosh graphics. It uses a strict two-color palette, relying entirely on ordered dithering and solid color blocking for shading and depth.

## 2. Color Palette (Strict 2-Color System)
No intermediate grays, gradients, or anti-aliasing are permitted.
* **Primary Ink (Dark):** `#050C2A` (Deep Navy / Midnight Blue) — Outlines, solid shadow blocks, clothing, dark hair, and dither dots.
* **Background / Highlight (Light):** `#E9EBFF` (Pale Periwinkle / Soft Lavender-White) — Negative space, skin tones, eye highlights, and light areas.

## 3. Core Rendering Rules
* **1-Bit Ordered Dithering:** Achieve all mid-tones (hair gradients, neck/face shadows, iris texture) using Bayer matrix / checkerboard pixel patterns (`50%`, `25%`, and `12.5%` density).
* **Crisp Pixel Grid:** Hard-edged square pixels (`image-rendering: pixelated`). Zero sub-pixel blurring or smooth vector curves.
* **High-Contrast Blocking:** Render clothing and deep shadow areas as solid `#050C2A` silhouettes to anchor the character against the solid `#E9EBFF` background.
* **Minimalist Facial Features:** Use sparse single-pixel clusters for the nose and mouth, contrasted with detailed, expressive dithered eyes.

---

## 4. AI Image Generation Prompts

### Universal Prompt (Midjourney / DALL-E 3 / Flux)
> **Prompt:** 1-bit pixel art portrait of [SUBJECT], retro Japanese PC-98 visual novel aesthetic, strict duotone color palette using only deep navy blue (#050C2A) and pale lavender-white (#E9EBFF), heavy Bayer matrix ordered dithering for hair shading and soft shadows, solid dark silhouette clothing, minimalist anime facial features with expressive dithered eyes, crisp square pixel grid, no anti-aliasing, no smooth gradients, flat light background.

### Stable Diffusion / Technical Tags
* **Positive:** `1-bit pixel art, duotone, (#050C2A and #E9EBFF), ordered dithering, Bayer matrix, crosshatch pixel shading, PC-98 style, retro anime portrait, high contrast, flat background, sharp pixel edges, no anti-aliasing`
* **Negative:** `smooth gradients, anti-aliasing, blur, 3D, photorealistic, full color, grayscale, soft shading, airbrush, vector art`

---

## 5. UI / Web Implementation Specs
To apply this style to a UI or webpage:
* **Colors:** `--bg: #E9EBFF; --fg: #050C2A;`
* **Borders:** `2px solid #050C2A` with hard offset drop shadows (`4px 4px 0px #050C2A`).
* **Textures:** Use CSS repeating radial/conic gradients or ASCII blocks (`░ ▒ ▓ █`) for dividers and backgrounds.
* **Typography:** Monospace or bitmap pixel fonts (e.g., *Press Start 2P*, *VT323*, *DotGothic16*).
