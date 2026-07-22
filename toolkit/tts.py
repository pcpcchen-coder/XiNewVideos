#!/usr/bin/env python3
"""Voiceover via edge-tts (free Microsoft neural voices) — replaces the Kimi
`audio_generation` plugin / ElevenLabs.

Synthesises one MP3 per narration segment into audio/slide_NN.mp3, using the
voice/rate/pitch in config.json. After running, re-run build_subtitles.py and
assemble.py — they auto-detect the audio and switch to real-duration timing.

NOTE: In this sandbox the edge-tts backend host (speech.platform.bing.com) is
blocked by the egress policy (HTTP 403). Run this on a machine/environment where
that host is reachable (e.g. locally, or the original Kimi sandbox). The proxy CA
is appended to certifi by toolkit/setup.sh so TLS verification passes.

Usage: python3 toolkit/tts.py videos/<episode>/
"""
import asyncio, json, sys
from pathlib import Path

async def synth(text, out, voice, rate, pitch):
    import edge_tts
    c = edge_tts.Communicate(text, voice=voice, rate=rate, pitch=pitch)
    await c.save(str(out))

def main(vdir):
    vdir = Path(vdir)
    cfg = json.loads((vdir/"config.json").read_text(encoding="utf-8"))["tts"]
    narration = json.loads((vdir/"narration.json").read_text(encoding="utf-8"))
    (vdir/"audio").mkdir(exist_ok=True)
    voice = cfg.get("voice","zh-TW-YunJheNeural")
    rate  = cfg.get("rate","+0%"); pitch = cfg.get("pitch","+0Hz")
    print(f"voice={voice} rate={rate} pitch={pitch}")
    for i, seg in enumerate(narration, 1):
        out = vdir/"audio"/f"slide_{i:02d}.mp3"
        try:
            asyncio.run(synth(seg, out, voice, rate, pitch))
            print(f"  ✓ slide_{i:02d}.mp3  ({out.stat().st_size//1024} KB)")
        except Exception as e:
            print(f"  ✗ slide_{i:02d}: {type(e).__name__}: {str(e)[:120]}")
            print("    (If this is a 403, the TTS host is blocked here — run where it is reachable.)")
            sys.exit(2)
    print("Done. Next: python3 toolkit/build_subtitles.py <dir> && python3 toolkit/assemble.py <dir>")

if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv)>1 else "videos/ep01-what-is-inside-a-computer")
