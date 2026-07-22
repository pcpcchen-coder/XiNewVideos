# 本機補語音 Local Voiceover

配音用的 **edge-tts** 需要連到微軟的語音主機。**Claude Code 網頁版（雲端沙盒）** 的 egress 政策把該主機
403 擋掉了，所以雲端這邊產出的是「無語音」版。**只要在你自己的電腦上跑，就連得到、能正常出聲。**

> 重點不是「用哪個編輯器」，而是「程式在**你的機器**還是**雲端沙盒**執行」。

## 哪些方式可以（在本機執行）

| 執行環境 | 能跑 TTS？ |
|---|---|
| Claude Code 網頁版（claude.ai/code） | ❌ 雲端沙盒擋 |
| VS Code / JetBrains 外掛 | ✅ 在你本機執行 |
| 終端機 CLI（`claude`） | ✅ 在你本機執行 |
| Claude Desktop（Mac/Windows） | ✅ 只要該 session 在本機執行 |
| **直接用 Python（不需 Claude）** | ✅ 最簡單 |

## 最簡單：三行指令（不需要 Claude）

在你自己電腦的終端機：

```bash
git clone https://github.com/pcpcchen-coder/XiNewVideos
cd XiNewVideos
pip install edge-tts imageio-ffmpeg fonttools pillow   # 另需 ffmpeg 在 PATH（Mac: brew install ffmpeg）

V=videos/ep01-what-is-inside-a-computer
python3 toolkit/tts.py             $V   # ① 產生陳犀牛語音 audio/slide_NN.mp3
python3 toolkit/build_subtitles.py $V   # ② 自動改用真實語音長度，重算 SRT
python3 toolkit/assemble.py        $V   # ③ video.mp4 帶語音重出（乾淨、無燒字幕）
```

完成後：
- **`video.mp4`** = 帶語音的乾淨影片 → 上傳 YouTube。
- **`subtitles/subtitles.srt`** = 字幕 → 在 YouTube「字幕 → 上傳檔案」載入。

## 小提醒
- **不必重跑投影片**（`slides/` 已在 repo 裡），所以本機**不用裝 Playwright/Chromium**。
- **字幕字型**已放在 `brand/fonts/`，本機不必另裝（僅選用 `--burn` 硬燒時才會用到）。
- 想換聲線／語速：改 `videos/<ep>/config.json` 的 `tts.voice`／`rate`／`pitch`
  （預設台灣男聲 `zh-TW-YunJheNeural`；女聲可用 `zh-TW-HsiaoChenNeural`）。
- 若 edge-tts 出現憑證錯誤（一般本機不會），把公司/代理 CA 併進 certifi，或見 `toolkit/setup.sh` §5。
