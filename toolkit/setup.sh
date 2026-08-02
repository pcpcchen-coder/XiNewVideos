#!/usr/bin/env bash
# One-shot environment rebuild for the XiNewVideos pipeline.
# Installs the free/offline toolchain that replaces the Kimi plugins:
#   slides  -> Playwright/Chromium (HTML->PNG)
#   voice   -> edge-tts (neural TTS; needs a reachable backend host)
#   encode  -> imageio-ffmpeg (static ffmpeg 7.x: libx264/aac/libass)
#   font    -> Noto Sans TC (committed under brand/fonts/)
set -e
HERE="$(cd "$(dirname "$0")/.." && pwd)"
echo "== 1. Python deps =="
pip3 install --quiet edge-tts playwright imageio-ffmpeg fonttools brotli pillow

echo "== 2. ffmpeg on PATH =="
FF=$(python3 -c "import imageio_ffmpeg;print(imageio_ffmpeg.get_ffmpeg_exe())")
ln -sf "$FF" /usr/local/bin/ffmpeg 2>/dev/null || sudo ln -sf "$FF" /usr/local/bin/ffmpeg
echo "   ffmpeg -> $FF"

echo "== 3. Chromium =="
# Browsers are preinstalled in Claude Code web sandboxes at /opt/pw-browsers.
# On a fresh machine, fetch one:
python3 -c "import glob,sys; sys.exit(0 if glob.glob('/opt/pw-browsers/chromium-*/chrome-linux/chrome') else 1)" \
  && echo "   using preinstalled /opt/pw-browsers chromium" \
  || python3 -m playwright install chromium

echo "== 4. Install Noto Sans TC fonts =="
mkdir -p /usr/share/fonts/truetype/notosanstc
cp "$HERE"/brand/fonts/NotoSansTC-*.ttf /usr/share/fonts/truetype/notosanstc/ 2>/dev/null || true
fc-cache -f >/dev/null 2>&1 || true
echo "   $(fc-list | grep -c 'Noto Sans TC') Noto Sans TC faces registered"

echo "== 5. TLS: trust the agent-proxy CA for edge-tts (certifi) =="
CA=/root/.ccr/ca-bundle.crt
if [ -f "$CA" ]; then
  CERTIFI=$(python3 -c "import certifi;print(certifi.where())")
  grep -q "CCR-AGENT-PROXY-APPENDED" "$CERTIFI" 2>/dev/null || {
    printf "\n# CCR-AGENT-PROXY-APPENDED\n" >> "$CERTIFI"; cat "$CA" >> "$CERTIFI";
    echo "   appended proxy CA to $CERTIFI"; }
  export SSL_CERT_FILE="$CA" REQUESTS_CA_BUNDLE="$CA" NODE_EXTRA_CA_CERTS="$CA"
fi
echo "Done. Try: python3 toolkit/render_slides.py videos/ep01-what-is-inside-a-computer"
