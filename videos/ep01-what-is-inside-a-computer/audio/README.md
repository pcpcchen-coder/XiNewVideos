# audio/

配音檔（`slide_01.mp3` … `slide_10.mp3`）會放在這裡。

本沙盒的 egress 政策封鎖了 edge-tts 的後端主機（`speech.platform.bing.com` → 403），
所以這個資料夾目前是空的、`video.mp4` 暫時無語音（旁白由 `subtitles/subtitles.srt` 呈現）。

要補上語音，在**你自己的電腦**（能連到該主機）執行 —— 完整說明見 [`../../../docs/LOCAL-VOICEOVER.md`](../../../docs/LOCAL-VOICEOVER.md)：

```bash
python3 toolkit/tts.py videos/ep01-what-is-inside-a-computer
python3 toolkit/build_subtitles.py videos/ep01-what-is-inside-a-computer   # 自動改用真實語音長度
python3 toolkit/assemble.py videos/ep01-what-is-inside-a-computer          # video.mp4 帶語音重出
```
