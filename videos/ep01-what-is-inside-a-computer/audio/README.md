# audio/

配音檔（`slide_01.mp3` … `slide_10.mp3`）會放在這裡。

本沙盒的 egress 政策封鎖了 edge-tts 的後端主機（`speech.platform.bing.com` → 403），
所以這個資料夾目前是空的，成品採「無語音 + 燒入字幕」。

要補上語音，在**能連到該主機的環境**執行：

```bash
python3 toolkit/tts.py videos/ep01-what-is-inside-a-computer
python3 toolkit/build_subtitles.py videos/ep01-what-is-inside-a-computer   # 自動改用真實語音長度
python3 toolkit/assemble.py videos/ep01-what-is-inside-a-computer          # video_sub.mp4 帶語音重出
```
