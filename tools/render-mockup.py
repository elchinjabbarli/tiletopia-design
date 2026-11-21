#!/usr/bin/env python3
"""Tiletopia design repo — mockup sheet renderer.
Renders brand mockups (icon on shelf, feature tile, wordmark lockup) from
the design-system palette. Pure Pillow; no fonts beyond bundled system.
"""
from PIL import Image, ImageDraw, ImageFilter
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "screens")

# palette from DESIGN-SYSTEM.md §2
TEAL = (46, 196, 182, 255)
TEAL_DARK = (33, 134, 122, 255)
CREAM = (255, 246, 229, 255)
SUN = (255, 210, 63, 255)
WOOD = (201, 138, 75, 255)
INK = (92, 58, 30, 255)
CORAL = (255, 95, 109, 255)

def vgrad(w, h, stops):
    img = Image.new("RGBA", (w, h))
    px = img.load()
    for y in range(h):
        t = y / max(h - 1, 1)
        # piecewise
        seg = len(stops) - 1
        i = min(int(t * seg), seg - 1)
        f = t * seg - i
        c = tuple(int(stops[i][k] + (stops[i + 1][k] - stops[i][k]) * f) for k in range(3)) + (255,)
        for x in range(w):
            px[x, y] = c
    return img

def rounded(draw, box, r, fill=None, outline=None, width=1):
    draw.rounded_rectangle(box, radius=r, fill=fill, outline=outline, width=width)

def tile(d, cx, cy, s, fruit_fill):
    """one fruit tile: wood frame + cream face + fruit blob"""
    x0, y0 = cx - s // 2, cy - s // 2
    rounded(d, (x0, y0, x0 + s, y0 + s), s // 6, fill=WOOD, outline=(169, 111, 56, 255), width=max(s // 40, 2))
    inset = s // 9
    rounded(d, (x0 + inset, y0 + inset, x0 + s - inset, y0 + s - inset), s // 8, fill=CREAM)
    # fruit: simple circle + leaf
    r = int(s * 0.28)
    d.ellipse((cx - r, cy - r, cx + r, cy + r), fill=fruit_fill, outline=(36, 24, 12, 200), width=max(s // 50, 2))
    d.arc((cx - r, cy - r - s // 8, cx + r, cy + r - s // 8), 200, 340, fill=(46, 125, 50, 255), width=max(s // 30, 3))

def sheet():
    W, H = 1560, 820
    img = vgrad(W, H, [(46, 196, 182), (127, 227, 208), (255, 233, 184)])
    d = ImageDraw.Draw(img)
    # soft sun
    sun = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    sd = ImageDraw.Draw(sun)
    sd.ellipse((W // 2 - 260, 40, W // 2 + 260, 380), fill=(255, 247, 214, 120))
    sun = sun.filter(ImageFilter.GaussianBlur(60))
    img = Image.alpha_composite(img, sun)
    d = ImageDraw.Draw(img)
    # clouds
    for (cx, cy, s) in [(220, 120, 1.0), (1200, 90, 0.8), (760, 160, 0.6)]:
        sd.ellipse((cx - 90 * s, cy - 26 * s, cx + 90 * s, cy + 26 * s), fill=(255, 255, 255, 55))
        sd.ellipse((cx - 30 * s, cy - 44 * s, cx + 60 * s, cy + 10 * s), fill=(255, 255, 255, 55))
    d = ImageDraw.Draw(img)

    # --- 1) icon on gradient shelf (left) ---
    ix, iy, isz = 120, 200, 560
    d.rounded_rectangle((ix, iy, ix + isz, iy + isz), radius=isz // 5, fill=(33, 134, 122, 255))
    # icon art: pyramid of 3 tiles on sky gradient
    sky = vgrad(isz, isz, [(46, 196, 182), (127, 227, 208), (255, 233, 184)])
    mask = Image.new("L", (isz, isz), 0)
    md = ImageDraw.Draw(mask)
    md.rounded_rectangle((0, 0, isz, isz), radius=isz // 5, fill=255)
    img.paste(sky, (ix, iy), mask)
    d = ImageDraw.Draw(img)
    tile(d, ix + isz * 0.32, iy + isz * 0.34, isz // 4, CORAL)
    tile(d, ix + isz * 0.68, iy + isz * 0.34, isz // 4, SUN)
    tile(d, ix + isz * 0.50, iy + isz * 0.62, isz // 4, TEAL)

    # --- 2) wordmark lockup (center) ---
    lx, ly = 760, 260
    d.rounded_rectangle((lx, ly, lx + 620, ly + 150), radius=60, fill=CREAM, outline=(169, 111, 56, 255), width=6)
    try:
        from PIL import ImageFont
        f = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 96)
    except Exception:
        f = None
    d.text((lx + 310, ly + 75), "Tiletopia", font=f, fill=INK, anchor="mm")
    d.text((lx + 310, ly + 185), "TROPICAL TILE TRIPLE", font=f, fill=(90, 55, 22, 255), anchor="mm", spacing=8)

    # --- 3) buttons row (bottom-left) ---
    bx, by, bw, bh = 120, 560, 300, 78
    # primary pill
    d.rounded_rectangle((bx, by, bx + bw, by + bh), radius=39, fill=(255, 180, 46, 255), outline=(245, 159, 27, 255), width=4)
    d.rounded_rectangle((bx, by + bh + 26, bx + bw, by + bh + 26 + bh), radius=39, fill=(46, 196, 182, 255), outline=(38, 168, 156, 255), width=4)
    d.rounded_rectangle((bx + 340, by, bx + 340 + bw, by + bh), radius=39, fill=(255, 143, 94, 255), outline=(242, 96, 58, 255), width=4)
    try:
        from PIL import ImageFont
        f2 = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 40)
    except Exception:
        f2 = None
    d.text((bx + bw / 2, by + bh / 2), "CONTINUE", font=f2, fill=(107, 59, 16, 255), anchor="mm")
    d.text((bx + bw / 2, by + bh * 1.5 + 26), "LEVELS", font=f2, fill=(6, 51, 46, 255), anchor="mm")
    d.text((bx + 340 + bw / 2, by + bh / 2), "+2 SLOT", font=f2, fill=(255, 255, 255, 255), anchor="mm")

    # --- 4) ad-card mock (bottom-right) ---
    ax, ay = 860, 540
    d.rounded_rectangle((ax, ay, ax + 560, ay + 220), radius=36, fill=(0, 0, 0, 90))
    d = ImageDraw.Draw(img)
    d.rounded_rectangle((ax + 24, ay + 24, ax + 536, ay + 196), radius=24, fill=CREAM)
    d.rounded_rectangle((ax + 60, ay + 120, ax + 500, ay + 180), radius=30, fill=(255, 143, 94, 255))
    d.text((ax + 280, ay + 150), "REWARDED", font=f2, fill=(255, 255, 255, 255), anchor="mm")
    d.rounded_rectangle((ax + 380, ay + 60, ax + 500, ay + 100), radius=20, fill=(0, 0, 0, 140))
    d.text((ax + 440, ay + 80), "Ad  x", font=f2, fill=(255, 255, 255, 255), anchor="mm")

    out = os.path.join(OUT, "design-mockup-sheet.png")
    img.convert("RGB").save(out, "PNG")
    print("saved", out, img.size)

sheet()
