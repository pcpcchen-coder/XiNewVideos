#!/usr/bin/env python3
"""Lint narration.json before synthesis (adapted from the Kimi toolkit's
lint_narration.js). Catches TTS-unfriendly segments and font-coverage gaps.

Usage: python3 toolkit/lint_narration.py videos/<episode>/
"""
import json, re, sys
from pathlib import Path
from fontTools.ttLib import TTFont

ROOT = Path(__file__).resolve().parent.parent
FONT = ROOT/"brand"/"fonts"/"NotoSansTC-Regular.ttf"

def main(vdir):
    vdir = Path(vdir)
    narration = json.loads((vdir/"narration.json").read_text(encoding="utf-8"))
    cmap = set(TTFont(FONT).getBestCmap().keys()) if FONT.exists() else None
    err = warn = 0
    for i, seg in enumerate(narration, 1):
        n = len(seg)
        if not re.search(r"[。！？]$", seg):
            print(f"  ERROR slide {i}: 未以句號/驚嘆/問號結尾"); err += 1
        if n < 40:  print(f"  WARN  slide {i}: 偏短 ({n} 字)"); warn += 1
        if n > 170: print(f"  WARN  slide {i}: 偏長 ({n} 字)，TTS 可能太趕"); warn += 1
        if re.search(r"[0-9]", seg):
            print(f"  WARN  slide {i}: 含阿拉伯數字，建議改中文數字（TTS 讀法較穩）"); warn += 1
        if cmap:
            miss = sorted({c for c in seg if c.strip() and ord(c) > 0x20 and ord(c) not in cmap})
            if miss: print(f"  ERROR slide {i}: 字體缺字 {''.join(miss)}"); err += 1
    print(f"lint: {len(narration)} segments | {err} ERROR | {warn} WARN")
    sys.exit(1 if err else 0)

if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv)>1 else "videos/ep01-what-is-inside-a-computer")
