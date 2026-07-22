#!/usr/bin/env python3
"""Build per-slide durations + aligned subtitles (SRT + styled ASS).

Two timing modes (config.timing.mode):
  - "estimated": derive slide length from narration char count (no audio needed).
                 Used in sandboxes where the TTS host is blocked.
  - "audio":     use real per-segment MP3 durations from audio/ (populated by tts.py).

Subtitle chunks split each segment at punctuation into <= maxCharsPerLine lines and
distribute the slide's duration proportionally to chunk length.

Usage: python3 toolkit/build_subtitles.py videos/<episode>/
"""
import json, re, sys, wave, contextlib
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

def mp3_denab(path):
    return None  # duration handled by ffmpeg in audio mode elsewhere

def fmt_srt(t):
    h=int(t//3600); m=int(t%3600//60); s=int(t%60); ms=int(round((t-int(t))*1000))
    return f"{h:02d}:{m:02d}:{s:02d},{ms:03d}"
def fmt_ass(t):
    h=int(t//3600); m=int(t%3600//60); s=t%60
    return f"{h:d}:{m:02d}:{s:05.2f}"

ASS_HEAD = """[Script Info]
ScriptType: v4.00+
PlayResX: 1920
PlayResY: 1080
WrapStyle: 2
ScaledBorderAndShadow: yes

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Cap,Noto Sans TC,52,&H00D7EAF2,&H00D7EAF2,&H00281404,&H8C2E1D0B,-1,0,0,0,100,100,0,0,3,14,0,2,110,470,92,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""

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
            # ffprobe-free duration via ffmpeg
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

    # ---- subtitles ----
    srt, ass = [], [ASS_HEAD]
    idx, t0 = 1, 0.0
    for seg, dur in zip(narration, durations):
        chunks = split_chunks(seg, maxlen)
        total = sum(len(c) for c in chunks) or 1
        ct = t0
        # leave a small lead-in so first caption isn't jammed at slide cut
        span = dur
        for c in chunks:
            cd = span * (len(c)/total)
            a, b = ct, ct+cd
            srt.append(f"{idx}\n{fmt_srt(a)} --> {fmt_srt(b)}\n{c}\n")
            ass.append(f"Dialogue: 0,{fmt_ass(a)},{fmt_ass(b)},Cap,,0,0,0,,{c}")
            idx += 1; ct = b
        t0 += dur

    (vdir/"subtitles"/"subtitles.srt").write_text("\n".join(srt), encoding="utf-8")
    (vdir/"subtitles"/"subtitles.ass").write_text("\n".join(ass)+"\n", encoding="utf-8")
    print(f"mode={mode}  slides={len(durations)}  total={sum(durations):.1f}s")
    print("durations:", durations)
    print("wrote slide_durations.json, subtitles/subtitles.srt, subtitles/subtitles.ass")

if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv)>1 else "videos/ep01-what-is-inside-a-computer")
