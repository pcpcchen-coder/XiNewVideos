#!/usr/bin/env python3
"""Assemble slides (+ optional audio) into the final video, then burn subtitles.

Replaces the Kimi/ffmpeg sandbox scripts. Uses the static ffmpeg from
imageio-ffmpeg (johnvansickle build) — full libx264 / aac / libass.

Outputs:
  video.mp4       slides with crossfades (+ audio if present, else silent track)
  video_sub.mp4   ^ with burned-in Traditional-Chinese subtitles (main deliverable)
  thumbnail.jpg   1280x720 cover

Usage: python3 toolkit/assemble.py videos/<episode>/
"""
import json, os, subprocess, sys, glob
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FONTS = ROOT/"brand"/"fonts"

def ff(*a):
    cmd = ["ffmpeg","-y","-hide_banner","-loglevel","error",*a]
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        print("FFMPEG ERROR:\n"," ".join(cmd),"\n",r.stderr[-1500:]); sys.exit(1)

def have_audio(vdir, n):
    return all((vdir/"audio"/f"slide_{i+1:02d}.mp3").exists() for i in range(n))

def main(vdir):
    vdir = Path(vdir)
    durations = json.loads((vdir/"slide_durations.json").read_text())
    slides = sorted(glob.glob(str(vdir/"slides"/"slide_*.png")))
    n = len(slides)
    assert n == len(durations), f"slides({n}) != durations({len(durations)})"
    audio = have_audio(vdir, n)
    total = sum(durations)

    # ---------- build video with exact hard cuts (concat demuxer) ----------
    # Hard cuts keep the timeline exact so subtitles (and per-segment audio) stay
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
        # concat the per-slide mp3s into one track
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

    # ---------- burn subtitles ----------
    ass = vdir/"subtitles"/"subtitles.ass"
    video_sub = vdir/"video_sub.mp4"
    vf = f"subtitles={ass.as_posix()}:fontsdir={FONTS.as_posix()}"
    ff("-i",str(video),"-vf",vf,"-c:v","libx264","-preset","medium","-crf","20",
       "-c:a","copy","-pix_fmt","yuv420p","-movflags","+faststart", str(video_sub))

    # ---------- thumbnail ----------
    ff("-i",slides[0],"-vf","scale=1280:720","-frames:v","1","-q:v","3",
       str(vdir/"thumbnail.jpg"))

    print(f"audio={'yes' if audio else 'SILENT (TTS host blocked in sandbox)'}  total={total:.1f}s")
    for f in ["video.mp4","video_sub.mp4","thumbnail.jpg"]:
        p = vdir/f; print(f"  ✓ {f}  ({p.stat().st_size//1024} KB)")

if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv)>1 else "videos/ep01-what-is-inside-a-computer")
