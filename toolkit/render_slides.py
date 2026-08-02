#!/usr/bin/env python3
"""Render branded slides from slides_spec.json to 1920x1080 PNGs using Chromium.

Replaces the Kimi `image_generation` plugin: instead of AI-generated images
(which risk garbled Chinese / wrong numbers), we render pixel-perfect HTML/CSS.

Usage: python3 toolkit/render_slides.py videos/<episode>/
"""
import base64, glob, json, os, sys
from pathlib import Path
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parent.parent
TEMPLATE = ROOT / "toolkit" / "template" / "slide.html"
INSTRUCTOR_DIR = ROOT / "assets" / "instructor"

# expression name -> avatar file
EXPR = {
    "calm":"expr_00_calm","smile":"expr_01_smile","laugh":"expr_02_laugh",
    "curious":"expr_03_curious","skeptical":"expr_04_skeptical","thinking":"expr_05_thinking",
    "surprised":"expr_06_surprised","embarrassed":"expr_07_embarrassed","serious":"expr_08_serious",
    "worried":"expr_09_worried","inspired":"expr_10_inspired","confident":"expr_11_confident",
}

def find_chrome():
    for p in glob.glob("/opt/pw-browsers/chromium-*/chrome-linux/chrome"):
        return p
    return None

def avatar_uri(key):
    if not key: return None
    fn = f"{key}.png" if key.startswith("pose") else f"{EXPR.get(key,'expr_01_smile')}.png"
    path = INSTRUCTOR_DIR / fn
    if not path.exists(): return None
    b64 = base64.b64encode(path.read_bytes()).decode()
    return f"data:image/png;base64,{b64}"

def main(vdir):
    vdir = Path(vdir)
    spec = json.loads((vdir / "slides_spec.json").read_text(encoding="utf-8"))
    out = vdir / "slides"; out.mkdir(exist_ok=True)
    slides = spec["slides"]
    with sync_playwright() as p:
        b = p.chromium.launch(executable_path=find_chrome(),
                              args=["--no-sandbox","--disable-dev-shm-usage","--force-color-profile=srgb"])
        pg = b.new_page(viewport={"width":1920,"height":1080}, device_scale_factor=1)
        pg.goto(TEMPLATE.as_uri())
        pg.wait_for_function("document.fonts.ready")
        for s in slides:
            av = avatar_uri(s.get("instructor"))
            pg.evaluate("([s,a]) => window.buildSlide(s,a)", [s, av])
            pg.wait_for_timeout(180)
            fn = out / f"slide_{s['n']:02d}.png"
            pg.screenshot(path=str(fn), clip={"x":0,"y":0,"width":1920,"height":1080})
            print(f"  ✓ {fn.name}  ({s['layout']})")
        b.close()
    print(f"Rendered {len(slides)} slides -> {out}")

if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv)>1 else ROOT/"videos"/"ep01-what-is-inside-a-computer")
