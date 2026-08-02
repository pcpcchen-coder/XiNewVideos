# 工具鏈替代與踩坑排解 TOOLCHAIN

> 對應使用者需求 #2：「執行上有缺的工具，請你自行探索可替代的。」
> 這份文件記錄本環境**缺了什麼、怎麼補、踩了哪些坑**，讓任何人都能重現這條產線。

## 為什麼要換工具

原 [video-production-skill-kimi](https://github.com/pcpcchen-coder/video-production-skill-kimi)
產線是為 **Kimi 沙盒**寫的，依賴：Kimi `image_generation`／`audio_generation` 插件、ElevenLabs、
OpenAI/faster-whisper、系統 ffmpeg、系統 Noto CJK 字型。這些在本 Claude Code 環境**全部不存在**，
且網路 egress 政策**只放行套件註冊表**（npm / PyPI / crates…），封鎖 apt、github、jsDelivr、
以及所有雲端 TTS 主機。以下是逐項替代。

## 替代對照

| 能力 | 原本（缺） | 替代方案 | 取得方式 |
|---|---|---|---|
| 投影片生成 | Kimi `image_generation` | HTML/CSS + **Playwright/Chromium** 截圖 | `pip install playwright`；Chromium 已預裝於 `/opt/pw-browsers` |
| 配音 TTS | Kimi `audio_generation` / ElevenLabs | **edge-tts**（`zh-TW-YunJheNeural`） | `pip install edge-tts`（**主機被本沙盒封鎖，需在可連線環境跑**） |
| ASR 對齊 | OpenAI / faster-whisper | 依字數/語音長度**推算** | 內建，不需模型 |
| 影像處理 | 系統 `ffmpeg` / `ffprobe` | **imageio-ffmpeg** 靜態 ffmpeg 7.0.2 | `pip install imageio-ffmpeg` |
| 中文字型 | 系統 Noto Sans CJK | **Noto Sans TC**（由 npm 合併重建） | 見下方「字型」 |

## 踩坑與解法（重點）

### 1. apt 被 proxy 擋（405 / 403）
`apt-get` 走純 HTTP、且 `archive.ubuntu.com` 不在放行清單 → `405 Method Not Allowed`。
**解**：不要用 apt。所有工具改從 **PyPI / npm** 取得（proxy 放行 `pypi.org`、`files.pythonhosted.org`、`registry.npmjs.org`）。

### 2. ffmpeg
`static-ffmpeg` 會去 github 下載 → `403`（github 被擋）。
**解**：改用 **`imageio-ffmpeg`**，它的 wheel 內含 johnvansickle 靜態 ffmpeg（libx264/aac/libass 齊全）。
```bash
FF=$(python3 -c "import imageio_ffmpeg;print(imageio_ffmpeg.get_ffmpeg_exe())")
ln -sf "$FF" /usr/local/bin/ffmpeg
```
沒有 `ffprobe`：改用 `ffmpeg -i` 解析 Duration，時間軸則直接由投影片時長決定，不需 ffprobe。

### 3. 中文字型（關鍵）
環境內 0 個 CJK 字型；apt/github/jsDelivr 皆擋。
**解**：從 **npm `@fontsource/noto-sans-tc`** 取字（`npm pack` 走 `registry.npmjs.org`，放行）。
fontsource 把 CJK 切成很多 woff2 子集，且 `chinese-traditional` 子集**不含全形標點**（漏 `，` 等）。
於是用 `fonttools` 把「漢字 + 拉丁 + 標點/箭頭子集」**合併**成完整字型，並修正 name table 為
`Noto Sans TC`（四字重 Regular/Medium/Bold/Black）。成品已收錄於 [`../brand/fonts/`](../brand/fonts/)，
`toolkit/setup.sh` 會安裝到系統字型 + `fc-cache`。Chromium（投影片）與 libass（燒字幕）共用同一套。

### 4. edge-tts 憑證與主機封鎖
- **TLS**：edge-tts 用自帶的 `certifi`，不吃 `SSL_CERT_FILE` → 憑證驗證失敗。
  **解**：把 agent-proxy CA 附加進 certifi 的 `cacert.pem`（`setup.sh` 自動處理）。
- **主機**：TLS 過了之後，`wss://speech.platform.bing.com` 回 **403（egress 政策封鎖）**。
  這是硬封鎖，不可繞過。**解**：`toolkit/tts.py` 已寫好，請在**能連到該主機的環境**執行；
  本沙盒則產出「無語音 + 燒入字幕」的完整剪輯。Google / HuggingFace 主機同樣被擋，已一併排除。

### 5. Playwright
`pip install playwright` 後不需 `playwright install`（瀏覽器已預裝）。
以 `executable_path=/opt/pw-browsers/chromium-*/chrome-linux/chrome` 啟動，加 `--no-sandbox`。

## 一鍵重建
```bash
bash toolkit/setup.sh
```
