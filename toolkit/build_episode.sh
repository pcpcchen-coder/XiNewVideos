#!/usr/bin/env bash
# Build one episode end-to-end.  Usage: bash toolkit/build_episode.sh videos/<episode>/
set -e
V="${1:-videos/ep01-what-is-inside-a-computer}"
HERE="$(cd "$(dirname "$0")/.." && pwd)"; cd "$HERE"
export SSL_CERT_FILE=/root/.ccr/ca-bundle.crt 2>/dev/null || true

echo "### 1/5 lint narration";      python3 toolkit/lint_narration.py "$V" || true
echo "### 2/5 voiceover (edge-tts)"; python3 toolkit/tts.py "$V" || echo "   [skip] TTS host unavailable — building silent+subtitles cut"
echo "### 3/5 render slides";        python3 toolkit/render_slides.py "$V"
echo "### 4/5 subtitles + timing";   python3 toolkit/build_subtitles.py "$V"
echo "### 5/5 assemble + burn + thumbnail"; python3 toolkit/assemble.py "$V"
echo "### verify"; python3 toolkit/verify.py "$V"
