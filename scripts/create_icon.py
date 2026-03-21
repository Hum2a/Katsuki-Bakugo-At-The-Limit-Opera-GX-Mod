#!/usr/bin/env python3
"""Build 512×512 Bakugo_AtLimit_Icon.png from Kachan_Icon.avif, or a solid placeholder."""

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ICON_PATH = ROOT / "Bakugo_AtLimit_Icon.png"
SOURCE_AVIF = ROOT / "Kachan_Icon.avif"


def icon_from_avif() -> bool:
    if not SOURCE_AVIF.exists():
        return False
    try:
        import pillow_avif  # noqa: F401 — registers AVIF with Pillow
        from PIL import Image
    except ImportError:
        print("For AVIF: pip install pillow pillow-avif-plugin")
        return False

    im = Image.open(SOURCE_AVIF)
    im.load()
    if im.mode not in ("RGB", "RGBA"):
        im = im.convert("RGBA" if "A" in im.getbands() else "RGB")

    w, h = im.size
    side = min(w, h)
    left = (w - side) // 2
    top = (h - side) // 2
    im_sq = im.crop((left, top, left + side, top + side))
    im_512 = im_sq.resize((512, 512), Image.Resampling.LANCZOS)
    im_512.save(ICON_PATH, "PNG", optimize=True)
    print(f"Wrote {ICON_PATH} from {SOURCE_AVIF} ({w}×{h} → 512×512)")
    return True


def main():
    if icon_from_avif():
        return
    try:
        from PIL import Image

        img = Image.new("RGB", (512, 512), color=(230, 62, 24))
        img.save(ICON_PATH)
        print(f"Created placeholder {ICON_PATH} (no {SOURCE_AVIF.name})")
    except ImportError:
        print("Install Pillow: pip install Pillow")
        print(f"Or add {SOURCE_AVIF.name} and: pip install pillow-avif-plugin")


if __name__ == "__main__":
    main()
