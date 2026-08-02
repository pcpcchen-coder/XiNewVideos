# 產線指引 PRODUCTION GUIDE（本環境版）

一支影片 = 重寫 3 個 JSON + 跑一條產線。以下是五步流程與指令。
（環境重建見 [`TOOLCHAIN.md`](TOOLCHAIN.md)；講師口吻見 [`IP-INSTRUCTOR.md`](IP-INSTRUCTOR.md)。）

## 每支影片要寫的 3 個檔案

放在 `videos/epNN-<英文短名>/`：

| 檔案 | 是什麼 | 重點 |
|---|---|---|
| `narration.json` | 旁白，一段對應一張投影片 | 陳犀牛口吻，每段 **40–170 字**，以句號/驚嘆/問號結尾 |
| `slides_spec.json` | 每張投影片的**結構化內容** | 指定 `layout` 版型與資料；見下方版型清單 |
| `storyboard.json` | 分鏡：版型 + 每張的講師**表情** | `instructor` 用表情鍵或 `pose_speaking` |

另有 `config.json`（片名、TTS 語音、時長參數）。

### 可用版型 layout（`slide.html` 引擎內建）
`title`（開場）、`flow`（流程）、`mapping`（比喻對應）、`spotlight`（單一焦點）、
`compare`（左右對比）、`network`（節點連線）、`trio`（三卡）、`twocol`（對照表）、`summary`（總結）。
每種版型吃的欄位可參考第一集的 [`slides_spec.json`](../videos/ep01-what-is-inside-a-computer/slides_spec.json)。

## 五步產線

```bash
V=videos/ep02-zero-and-one

# 1. Lint 旁白（配音前必過，0 ERROR）
python3 toolkit/lint_narration.py $V

# 2. 配音（edge-tts；本沙盒主機被擋會自動略過，改走無語音+字幕）
python3 toolkit/tts.py $V

# 3. 產投影片（HTML → 1920×1080 PNG）
python3 toolkit/render_slides.py $V

# 4. 字幕 + 時長（有配音就用真實長度，否則依字數推算；輸出 SRT + slide_durations.json）
python3 toolkit/build_subtitles.py $V

# 5. 組裝 + 封面（乾淨 video.mp4 + thumbnail.jpg；字幕以 SRT 側載，預設不燒）
python3 toolkit/assemble.py $V
#    需要硬燒字幕的版本再加 --burn（產出 video_sub.mp4）：
#    python3 toolkit/assemble.py $V --burn

# 驗收（全 PASS 才交付）
python3 toolkit/verify.py $V
```

> **交付物 = `video.mp4`（乾淨）＋ `subtitles/subtitles.srt`**。上 YouTube 時：影片傳 `video.mp4`，字幕在「字幕 → 上傳檔案」載入那支 SRT。字幕**不燒進畫面**。

或一鍵： `bash toolkit/build_episode.sh $V`

## 閘門 Gates
| 步驟 | 通過條件 |
|---|---|
| Lint | 0 ERROR（缺字、未結尾標點會擋） |
| 投影片 | 張數 == 旁白段數，每張 1920×1080 |
| 字幕 | 只在標點斷句、不切詞；輸出 `subtitles.srt` |
| 組裝 | `video.mp4` decode test 無錯、片長 ≈ 各段總和 |
| 驗收 | `verify.py` 全 PASS（第一集為 16/16） |

## 設計小抄
- 品牌色：深海藍 `#0B1D2E`、探索橙 `#F5A623`、奶油白 `#F2EAD7`。改色改 `brand/tokens.json` 與 `slide.html` 的 `:root`。
- 講師固定在右下角（表情隨內容切換）；開場用 `pose_speaking` 演講姿勢。
- 中文一律走 `Noto Sans TC`；圖示用內建 inline SVG（不依賴 emoji 字型，確保不變成空格）。
