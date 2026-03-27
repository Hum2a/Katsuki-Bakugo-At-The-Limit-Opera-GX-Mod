# Katsuki Bakugo - At The Limit — Opera GX mod

**My Hero Academia**–style mod for Opera GX themed around **Katsuki Bakugo**: animated wallpaper, background music, sounds, **red-orange on black** (redder than *Rising*), shaders, and **bucket web modding** (same structure as *Rising*: `bakugo-limit.css` + sites + Opera + GX).

## Structure

```
Katsuki Bakugo - At The Limit/
├── manifest.json
├── Bakugo_AtLimit_Icon.png  # 512×512 mod icon (`manifest.json` → `icons.512`)
├── license.txt
├── wallpaper/
├── music/
├── sound/
├── keyboard/
├── shader/                  # Explosion Glow, Howitzer Impact
├── webmodding/
├── MOD_BROWSER.md
└── scripts/
```

## Web modding (bucket layout)

- **`bakugo-limit.css`** — Global layer (redder burst / smoke mist) + legacy `--bakugo-*` tokens.
- **`sites-01` … `sites-06`** — Same host buckets as *Rising*, tuned to red-orange accents.
- **`bakugo-opera.css`** / **`bakugo-gx-surfaces.css`** — Opera.com and GX web surfaces.
- **Wallpaper labels** — `manifest.json` → `text_color` / `text_shadow`: dark mode uses **red-orange** titles; light mode uses **near-black** text with a **soft red-orange** shadow.

## Assets

- **Icon**: `Bakugo_AtLimit_Icon.png` (starts as a copy of the Rising icon; replace with art that matches *At The Limit* if you like).
- **Wallpaper**: `wallpaper/Bakugo_At_The_Limit.mp4` and `wallpaper/Bakugo_At_The_Limit.first_frame.png` — replace the MP4 when you change the clip; re-run `python scripts/extract_first_frame.py` (or `ffmpeg`) to refresh the first frame.
- **Background music**: `music/At_The_Limit.mp3` — **replace** with your chosen track; update `manifest.json` → `background_music` if the filename changes.

## Theme

- **Look**: red-orange accents (`#E63E18`, hover `#FF7845`) on **true black** (`#000000`) and charcoal (`#121212`).
- **GX UI**: `gx_accent` / `gx_secondary_base` HSL in `manifest.json` drives native chrome (hue ~15° for red-orange). See [MOD_BROWSER.md](MOD_BROWSER.md) for limits.
- **Shaders**: **Explosion Glow** (redder warm tint), **Howitzer Impact** (animated wave).

## Load & test

1. `opera:extensions` → Developer mode → **Load unpacked** → this folder  
2. `opera:mods` → enable the mod  

## Publish

See [PUBLISHING.md](PUBLISHING.md) and [GX.create](https://create.gx.games/mods).
