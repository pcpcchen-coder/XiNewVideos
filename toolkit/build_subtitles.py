#!/usr/bin/env python3
"""Build per-slide durations + a sidecar SRT subtitle file.

The SRT is the subtitle deliverable: upload it alongside video.mp4 to YouTube
(Subtitles → Upload file). Subtitles are NOT burned into the video by default —
see toolkit/assemble.py --burn if you ever want a hardsub copy.

Two timing modes (auto-detected):
  - "audio":     real per-segment MP3 durations from audio/ (populated by tts.py).
  - "estimated": derive slide length from narration char count (no audio needed).

Subtitle chunks split each segment at punctuation into <= maxCharsPerLine lines and
distribute the slide's duration proportionally to chunk length.

Usage: python3 toolkit/build_subtitles.py videos/<episode>/
"""
import json, re, sys
from pathlib import Path

PUNCT = "，。！？、；："

def split_chunks(text, maxlen):
    # break ONLY at punctuation, then greedily pack phrases up to maxlen
    phrases = [p for p in re.split(r'(?<=[，。！？、；：])', text) if p.strip()]
    lines, cur = [], ""
    for p in phrases:
        if not cur:
            cur = p
        elif len(cur) + len(p) <= maxlen:
            cur += p
        else:
            lines.append(cur); cur = p
    if cur: lines.append(cur)
    # safety: hard-wrap any single phrase longer than maxlen+4
    out = []
    for ln in lines:
        while len(ln) > maxlen + 4:
            out.append(ln[:maxlen]); ln = ln[maxlen:]
        out.append(ln)
    return out

def fmt_srt(t):
    h=int(t//3600); m=int(t%3600//60); s=int(t%60); ms=int(round((t-int(t))*1000))
    return f"{h:02d}:{m:02d}:{s:02d},{ms:03d}"

def main(vdir):
    vdir = Path(vdir)
    cfg = json.loads((vdir/"config.json").read_text(encoding="utf-8"))
    narration = json.loads((vdir/"narration.json").read_text(encoding="utf-8"))
    T = cfg["timing"]; maxlen = cfg["subtitles"]["maxCharsPerLine"]
    # auto-detect: if a full set of audio clips exists, use real durations
    audio_present = all((vdir/"audio"/f"slide_{i+1:02d}.mp3").exists() for i in range(len(narration)))
    mode = "audio" if audio_present else T.get("mode","estimated")

    # ---- per-slide durations ----
    durations = []
    if mode == "audio":
        import subprocess
        for i in range(len(narration)):
            mp3 = vdir/"audio"/f"slide_{i+1:02d}.mp3"
            out = subprocess.run(["ffmpeg","-i",str(mp3)], capture_output=True, text=True).stderr
            m = re.search(r"Duration: (\d+):(\d+):([\d.]+)", out)
            d = int(m.group(1))*3600+int(m.group(2))*60+float(m.group(3)) if m else 8.0
            durations.append(round(d + T["tailSeconds"], 2))
    else:
        cps = T["charsPerSecond"]
        for seg in narration:
            n = len([c for c in seg if c not in " "])
            durations.append(round(max(T["minSlideSeconds"], n/cps) + T["tailSeconds"], 2))

    (vdir/"slide_durations.json").write_text(json.dumps(durations, ensure_ascii=False, indent=2), encoding="utf-8")

    # ---- SRT (YouTube-ready sidecar) ----
    srt = []
    idx, t0 = 1, 0.0
    for seg, dur in zip(narration, durations):
        chunks = split_chunks(seg, maxlen)
        total = sum(len(c) for c in chunks) or 1
        ct = t0
        for c in chunks:
            cd = dur * (len(c)/total)
            srt.append(f"{idx}\n{fmt_srt(ct)} --> {fmt_srt(ct+cd)}\n{c}\n")
            idx += 1; ct += cd
        t0 += dur

    (vdir/"subtitles").mkdir(exist_ok=True)
    (vdir/"subtitles"/"subtitles.srt").write_text("\n".join(srt), encoding="utf-8")
    print(f"mode={mode}  slides={len(durations)}  total={sum(durations):.1f}s")
    print("durations:", durations)
    print("wrote slide_durations.json, subtitles/subtitles.srt  (upload the SRT to YouTube)")

if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv)>1 else "videos/ep01-what-is-inside-a-computer")
