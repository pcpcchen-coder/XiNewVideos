#!/usr/bin/env python3
"""Assemble slides (+ optional audio) into the final video.

Uses the static ffmpeg from imageio-ffmpeg (johnvansickle build) — full
libx264 / aac / libass.

Default output (YouTube-ready):
  video.mp4       clean slides (+ audio if present, else silent track) — MAIN deliverable
  thumbnail.jpg   1280x720 cover
Subtitles are delivered as a sidecar SRT (see build_subtitles.py) — upload it to
YouTube, do NOT burn it in.

Optional:
  --burn          also produce video_sub.mp4 with hard-burned subtitles
                  (styled from subtitles.srt via libass force_style)

Usage: python3 toolkit/assemble.py videos/<episode>/ [--burn]
"""
import json, subprocess, sys, glob
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FONTS = ROOT/"brand"/"fonts"

# libass style for the optional hardsub (cream text in a semi-transparent box,
# lower-third, kept clear of the bottom-right instructor avatar).
BURN_STYLE = ("Fontname=Noto Sans TC,Fontsize=52,Bold=1,PrimaryColour=&H00D7EAF2,"
              "BorderStyle=3,Outline=14,Shadow=0,BackColour=&H8C2E1D0B,"
              "Alignment=2,MarginL=110,MarginR=470,MarginV=92")

def ff(*a):
    cmd = ["ffmpeg","-y","-hide_banner","-loglevel","error",*a]
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        print("FFMPEG ERROR:\n"," ".join(cmd),"\n",r.stderr[-1500:]); sys.exit(1)

def have_audio(vdir, n):
    return all((vdir/"audio"/f"slide_{i+1:02d}.mp3").exists() for i in range(n))

def main(vdir, burn=False):
    vdir = Path(vdir)
    durations = json.loads((vdir/"slide_durations.json").read_text())
    slides = sorted(glob.glob(str(vdir/"slides"/"slide_*.png")))
    n = len(slides)
    assert n == len(durations), f"slides({n}) != durations({len(durations)})"
    audio = have_audio(vdir, n)
    total = sum(durations)

    # ---------- build video with exact hard cuts (concat demuxer) ----------
    # Hard cuts keep the timeline exact so the SRT (and per-segment audio) stay
    # perfectly aligned to each slide. A global fade in/out softens the ends.
    listf = vdir/"_concat.txt"
    lines = []
    for s, d in zip(slides, durations):
        lines.append(f"file '{Path(s).resolve()}'")
        lines.append(f"duration {d}")
    lines.append(f"file '{Path(slides[-1]).resolve()}'")  # hold final frame
    listf.write_text("\n".join(lines), encoding="utf-8")

    tmp = vdir/"_video_noaudio.mp4"
    ff("-f","concat","-safe","0","-i",str(listf),
       "-vf", f"fps=30,format=yuv420p,fade=t=in:st=0:d=0.6,fade=t=out:st={total-0.6:.3f}:d=0.6",
       "-c:v","libx264","-preset","medium","-crf","20","-pix_fmt","yuv420p",
       "-movflags","+faststart", str(tmp))
    listf.unlink(missing_ok=True)

    video = vdir/"video.mp4"
    if audio:
        concat = "|".join(str(vdir/"audio"/f"slide_{i+1:02d}.mp3") for i in range(n))
        aud = vdir/"_audio.m4a"
        ff("-i", f"concat:{concat}", "-c:a","aac","-b:a","192k", str(aud))
        ff("-i",str(tmp),"-i",str(aud),"-c:v","copy","-c:a","aac","-b:a","192k",
           "-shortest","-movflags","+faststart", str(video))
        aud.unlink(missing_ok=True)
    else:
        # silent stereo track so the mp4 plays everywhere
        ff("-i",str(tmp),"-f","lavfi","-t",f"{total:.3f}","-i",
           "anullsrc=channel_layout=stereo:sample_rate=44100",
           "-c:v","copy","-c:a","aac","-shortest","-movflags","+faststart", str(video))
    tmp.unlink(missing_ok=True)

    # ---------- thumbnail ----------
    ff("-i",slides[0],"-vf","scale=1280:720","-frames:v","1","-q:v","3",
       str(vdir/"thumbnail.jpg"))

    outputs = ["video.mp4","thumbnail.jpg"]

    # ---------- optional: hard-burned subtitle copy ----------
    if burn:
        srt = (vdir/"subtitles"/"subtitles.srt").as_posix()
        vf = f"subtitles={srt}:fontsdir={FONTS.as_posix()}:force_style={BURN_STYLE}"
        ff("-i",str(video),"-vf",vf,"-c:v","libx264","-preset","medium","-crf","20",
           "-c:a","copy","-pix_fmt","yuv420p","-movflags","+faststart", str(vdir/"video_sub.mp4"))
        outputs.append("video_sub.mp4")

    print(f"audio={'yes' if audio else 'SILENT (add voice with toolkit/tts.py in a TTS-reachable env)'}"
          f"  burn={'yes' if burn else 'no (sidecar SRT for YouTube)'}  total={total:.1f}s")
    for f in outputs:
        p = vdir/f; print(f"  ✓ {f}  ({p.stat().st_size//1024} KB)")

if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    burn = "--burn" in sys.argv
    main(args[0] if args else "videos/ep01-what-is-inside-a-computer", burn=burn)
