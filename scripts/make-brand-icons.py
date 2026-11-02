#!/usr/bin/env python3
"""Generate the three minimalist VOD brand icons.

Flat solid-color rounded square, bold white letters centered, nothing else.
- clean (vod.n2f.top): green  #16A34A  "VOD"
- full (video.n2f.top): blue #2563EB  "VIDEO"
- dirty (avod.n2f.top): red  #DC2626  "AVOD"

Font auto-fits each text to ~78% of the canvas width so all three look
consistent despite different letter counts. Output 1024x1024 PNG.
"""
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent.parent
FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
SIZE = 1024
RADIUS = 230
TARGET_W = 800

SPECS = [
    ("clean", "#16A34A", "VOD"),
    ("full", "#2563EB", "VIDEO"),
    ("dirty", "#DC2626", "AVOD"),
]


def fit_font(text: str) -> ImageFont.FreeTypeFont:
    lo, hi = 10, 900
    while lo < hi:
        mid = (lo + hi + 1) // 2
        f = ImageFont.truetype(FONT, mid)
        bbox = ImageDraw.Draw(Image.new("RGB", (10, 10))).textbbox((0, 0), text, font=f)
        if bbox[2] - bbox[0] <= TARGET_W:
            lo = mid
        else:
            hi = mid - 1
    return ImageFont.truetype(FONT, lo)


for name, color, text in SPECS:
    img = Image.new("RGBA", (SIZE, SIZE), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    d.rounded_rectangle([0, 0, SIZE - 1, SIZE - 1], radius=RADIUS, fill=color)
    font = fit_font(text)
    bbox = d.textbbox((0, 0), text, font=font)
    w, h = bbox[2] - bbox[0], bbox[3] - bbox[1]
    d.text(((SIZE - w) / 2 - bbox[0], (SIZE - h) / 2 - bbox[1]),
           text, font=font, fill="white")
    out = f"str(__import__("pathlib").Path(__file__).resolve().parent.parent / "public")/icon-{name}.png"
    img.save(out)
    print(out, "->", text, color, "font size", font.size)
