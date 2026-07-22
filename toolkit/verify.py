#!/usr/bin/env python3
"""Acceptance check for a finished episode (adapted from the Kimi toolkit's
final_check.py). Prints a PASS/FAIL report; exits non-zero if anything fails.

Usage: python3 toolkit/verify.py videos/<episode>/
"""
import json, re, subprocess, sys
from pathlib import Path
from PIL import Image
from fontTools.ttLib import TTFont

ROOT = Path(__file__).resolve().parent.parent
FONT = ROOT/"brand"/"fonts"/"NotoSansTC-Regular.ttf"
checks = []
def ok(cond, label, detail=""):
    checks.append((bool(cond), label, detail))

def ffdur(p):
    out = subprocess.run(["ffmpeg","-i",str(p)], capture_output=True, text=True).stderr
    m = re.search(r"Duration: (\d+):(\d+):([\d.]+)", out)
    return int(m.group(1))*3600+int(m.group(2))*60+float(m.group(3)) if m else -1

def decodes(p):
    r = subprocess.run(["ffmpeg","-v","error","-i",str(p),"-f","null","-"],
                       capture_output=True, text=True)
    return r.returncode == 0 and not r.stderr.strip()

def main(vdir):
    vdir = Path(vdir)
    narration = json.loads((vdir/"narration.json").read_text(encoding="utf-8"))
    story = json.loads((vdir/"storyboard.json").read_text(encoding="utf-8"))
    spec = json.loads((vdir/"slides_spec.json").read_text(encoding="utf-8"))["slides"]
    durations = json.loads((vdir/"slide_durations.json").read_text())
    N = len(narration)

    ok(len(story)==N and len(spec)==N and len(durations)==N,
       "計數一致 narration/storyboard/spec/durations", f"={N}")

    slides = sorted((vdir/"slides").glob("slide_*.png"))
    ok(len(slides)==N, "投影片張數 == 旁白段數", f"{len(slides)}/{N}")
    bad = [s.name for s in slides if Image.open(s).size != (1920,1080)]
    ok(not bad, "所有投影片為 1920x1080", ",".join(bad))

    # avatars referenced exist
    missing_av = []
    for sl in spec:
        key = sl.get("instructor","")
        fn = f"{key}.png" if key.startswith("pose") else None
        # expression keys resolved by render_slides; just check pose files here
        if fn and not (ROOT/"assets"/"instructor"/fn).exists(): missing_av.append(fn)
    ok(not missing_av, "講師姿勢圖存在", ",".join(missing_av))

    srt = vdir/"subtitles"/"subtitles.srt"; ass = vdir/"subtitles"/"subtitles.ass"
    ok(srt.exists() and srt.stat().st_size>0, "字幕 SRT 存在")
    ok(ass.exists() and ass.stat().st_size>0, "字幕 ASS 存在")
    cues = len(re.findall(r"-->", srt.read_text(encoding="utf-8"))) if srt.exists() else 0
    ok(cues>=N, "字幕句數合理", f"{cues} cues")

    total = sum(durations)
    for name in ["video.mp4","video_sub.mp4"]:
        p = vdir/name
        ok(p.exists(), f"{name} 存在")
        if p.exists():
            ok(decodes(p), f"{name} 解碼無錯誤（decode test）")
            d = ffdur(p)
            ok(abs(d-total)<2.0, f"{name} 片長 ≈ {total:.1f}s", f"實際 {d:.1f}s")

    th = vdir/"thumbnail.jpg"
    ok(th.exists() and Image.open(th).size==(1280,720), "封面 1280x720")

    if FONT.exists():
        cmap = set(TTFont(FONT).getBestCmap().keys())
        text = set("".join(narration)) | set(json.dumps(spec, ensure_ascii=False))
        miss = sorted(c for c in text if c.strip() and ord(c)>0x20 and ord(c) not in cmap)
        ok(not miss, "字體 100% 覆蓋旁白+投影片文字", "".join(miss))

    lens = [len(s) for s in narration]
    ok(all(40<=l<=170 for l in lens), "旁白每段 40–170 字", f"min={min(lens)} max={max(lens)}")

    npass = sum(1 for c in checks if c[0])
    print(f"\n===== 驗收 {npass}/{len(checks)} =====")
    for good, label, detail in checks:
        print(f"  {'✓ PASS' if good else '✗ FAIL'}  {label}" + (f"  [{detail}]" if detail else ""))
    print("=====================")
    sys.exit(0 if npass==len(checks) else 1)

if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv)>1 else "videos/ep01-what-is-inside-a-computer")
