# Browser chrome vs web modding

Opera GX mods can style **web pages** you open (via `page_styles` + CSS) and set the mod **theme** (HSL) and **wallpaper text** in `manifest.json`.

## Address bar / omnibox (limitation)

There is **no public manifest field** for “URL bar text colour” or “address bar font” in the [official mod template](https://github.com/opera-gaming/gxmods). The native toolbar, tabs, and omnibox are coloured from:

- `theme.dark` / `theme.light` → **`gx_accent`** and **`gx_secondary_base`** (HSL only)

So “orange URL text” is **not** something you can set as a separate hex. Opera derives contrast and highlights from those two colours. Tweaking them (especially **`gx_accent` lightness** and **`gx_secondary_base` lightness**) is the only lever in the mod format.

For chrome not covered by mods, use **Opera GX → Settings → Appearance** as well.

## What this mod *does* control beyond that

| Feature | Where |
|--------|--------|
| Wallpaper / speed-dial style **title text** colour & shadow | `manifest.json` → `payload.wallpaper.*.text_color` / `text_shadow` |
| Toolbar / accent **tint** (indirect) | `payload.theme` HSL |
| **Opera.com** pages in a tab | `webmodding/opera.css` |
| **GX web** (e.g. store / creator) in a tab | `webmodding/gx-surfaces.css` |
| **Selection, scrollbars, focus rings** on injected sites | `webmodding/micro-nuance.css` |

If Opera adds more theme keys in a future `schema_version`, you can extend `manifest.json` when documented.
