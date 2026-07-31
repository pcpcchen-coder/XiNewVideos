# 應用B3：超音波供電植入物——物理天花板、商業現實與台灣切入點（第三版，完整重做）

> 一句話結論：超音波供電植入是「主動/被動兩用壓電元件」目前**唯一有 FDA PMA 產品、有大藥廠 3 億美元出價、有 mm³ 級實體驗證**的應用場域；但物理天花板極硬（FDA ISPTA 720 mW/cm² ⇒ 1 mm² 接收面最多攔截 7.2 mW 聲功率，實測落在 **18.8 µW–0.66 mW**）、路徑上有骨或氣體即歸零（1 MHz 穿顱功率衰減 **24.1 dB**）、且已商業化的 EBR Systems 在 FDA 核准後 12 個月**營收僅 USD 3.98M、淨損 USD 55.28M、電池壽命僅約 4 年**（對比 Medtronic Micra 內建電池 16.7 年）。台廠的理性定位是**壓電材料／微型換能器／精密件供應鏈**，不是系統。

---

## 0. 研究方法與限制（誠實揭露）

### 0.1 本輪執行紀錄

| 項目 | 結果 |
|---|---|
| 本輪成功執行的 WebSearch 次數 | **29 次**（前兩輪皆為 0 次） |
| WebFetch / curl | **未嘗試**（任務書已明示全面 403 封鎖） |
| 本文與前兩版的關係 | **完整覆寫**。前兩版所有「轉引」內容已刪除或重新以本輪一手搜尋結果取代 |
| 事實等級 | 本文所有數字均來自本輪 WebSearch 回傳之摘要與標題。**未能開啟原始 PDF／全文**，故一律標記為「搜尋摘要級，未經全文核對」 |

### 0.2 標記規則

- **【摘要驗證】**＝本輪 WebSearch 摘要明確給出，且有對應 URL（第 7 節）。**這是本文絕大多數事實的等級——可信但未經全文複核。**
- **【自行推算】**＝我用【摘要驗證】的參數做的物理計算，推導過程全部攤在第 5 節。
- **【存疑／衝突】**＝搜尋結果彼此矛盾或明顯可疑，已標出。
- **【查無】**＝實際搜過但沒有可用結果。

### 0.3 必查但本輪仍**查無**的項目

- **EBR WiSE 系統的超音波工作頻率（MHz）與聲輸出強度數值** —— 搜尋 FDA P240028 SSED 與 IFU 皆未在摘要中給出。**這是本文最遺憾的缺口**：無法驗證 WiSE 是否在 720 mW/cm² 之內運作。
- **Iota Biosciences 裝置的實際尺寸（mm³）、功率、植入深度** —— Astellas 新聞稿與 massdevice 報導皆只寫「grain-sized（米粒大小）」，**無任何工程數字**。
- **StimDust 的 backscatter 資料率** —— 摘要僅確認「單一 bit 指示晶片狀態（刺激 on/off）」，無 bit/s 數字。（DustNet 的資料率有查到，見 3 節。）
- **EBR 市值** —— 搜尋結果自相矛盾（見 0.4）。
- **RoHS / MDR 對「主動植入式醫材」是否根本不適用 RoHS** —— 我記憶中 RoHS 2011/65/EU 排除主動植入式醫材，但**本輪未查證，故不寫入正文結論**。
- **聯合骨科（UOC）的電子醫材能力** —— 查無任何相關資料。
- **台灣本土壓電陶瓷材料廠（醫療級）** —— 中文查詢完全失敗；英文查詢只找到一家台灣換能器廠（CTDCO），且無醫療植入級佐證。

### 0.4 已知的資料衝突（讀者請注意）

**EBR Systems 市值**：一份來源稱「以 AU$0.57 收盤價計，市值 **AU$2.54bn**」，另一份稱「2026 年稍早市值約 **AUD 475 million**」。AU$0.57 × 市值 AU$2.54bn 隱含約 44.5 億股，與一家年營收 4 百萬美元、剛完成 A$150M 增資的公司不相稱。**判定：AU$2.54bn 極可能是資料錯誤，本文不採用任何單一市值數字。**【存疑／衝突】

---

## 1. 結論摘要

1. **物理天花板是法規給的，不是材料給的。** FDA Track 3 上限為 **ISPTA.3 ≤ 720 mW/cm²、MI ≤ 1.9（或 derated ISPPA ≤ 190 W/cm²）**；心臟用途更嚴：**ISPTA ≤ 430 mW/cm²**；胎兒／連續波：**94 mW/cm²**；眼科：**50 mW/cm²、MI 0.23**。【摘要驗證，來源 1】換算後 **1 mm² 接收面最多攔截 7.2 mW 聲功率**。

2. **實測功率落在 18.8 µW – 0.66 mW，比理論上限低 1–2 個數量級。** mm 級壓電接收器在接近 FDA 上限的 7.2 mW/mm² 聲源強度下實測收得 **0.66 mW**；AlN PMUT 系統實測 **18.8 µW**（功率密度 7.36 µW/mm²，充飽 100 µF 至 3.19 V）。【摘要驗證，來源 2、3】**足夠做感測＋遙測＋神經刺激，不足以做加熱、泵送、高工作週期致動。**

3. **端到端效率的公開值散布在 2%–30%。** UTET 系統在 673 kHz、40 mm 深度、70 mW 輸出時整體效率 **27%**；另有報告聲學—電轉換 **29.7%**（低輸入功率下）；低頻 PMUT 只有 **2.68%**。【摘要驗證，來源 4】**設計者不能假設 >30%。**

4. **超音波的「不可行區」是骨與氣體，界線非常硬。** 顱骨功率衰減 **220 kHz: 5.0±2.4 dB／650 kHz: 14.9±3.2 dB／1000 kHz: 24.1±6.3 dB**（插入損耗約 −10 dB/MHz）。【摘要驗證，來源 5】1 MHz 下只剩 **0.4% 功率**穿過。皮質骨衰減 **9.94 dB/cm/MHz**、軟組織—骨界面反射率 **43%**、軟組織—空氣界面反射率 **>99.9%（自行推算）**。**⇒ 顱內、肺後方、腸氣後方，超音波不是效率差，是歸零；那是磁電（ME）的地盤。**

5. **唯一已商業化的產品證明「可以做到」也證明「賺錢很慢」。** EBR Systems **WiSE CRT** 於 **2025-04-11 取得 FDA PMA（P240028）**；SOLVE-CRT 樞紐試驗：LVESV 改善 **16.4%（p=0.003）**、無裝置／術式相關併發症比率 **80.9%（p<0.001）**、急性起搏擷取 **92%**、12 個月裝置留存 **96%**。【摘要驗證，來源 6、7】但截至 **2026-03-31 的 TTM 營收僅 USD 3.98M、淨損 USD 55.28M**，2026 年 6 月再增資 **A$150M**，CMS 最終全國給付決定要等到 **2027 年 3 月**。【摘要驗證，來源 8、9】

6. **WiSE 暴露了超音波供電最致命的工程現實：電池只有約 4 年，且需要「聲窗」。** WiSE 的體內超音波發射器必須植入肋間，且**該處肋軟骨間距至少 1 cm、寬 2.5 cm** 才有足夠聲窗；電池壽命「目前已延長到約 4 年」，且**壽命與「閾值振幅＋發射器到接收器距離」成反比**。【摘要驗證，來源 10、11】**對比 Medtronic Micra VR2 內建電池中位推估壽命 16.7 年、體積僅 0.8 cc**【摘要驗證，來源 12】——超音波供電在「省電池」這件事上目前是輸的。

7. **「同一顆壓電體兼四職」已被三代實體驗證，不是概念。** StimDust：**6.5 mm³**，單顆 **750×750×750 µm³** 壓電晶體同時做下行通訊、受電與 backscatter 讀出，峰值晶片效率 **82%**。【摘要驗證，來源 13】DustNet（2025）：同尺寸壓電＋28 nm CMOS（0.43 mm²），TDMA＋**16 階 ASK backscatter**，2 MHz 載波下最高 **200 kb/s**，單顆上行 **50 kb/s 而僅耗 7 µW**。【摘要驗證，來源 14】哥倫比亞大學（Ken Shepard 團隊）：**0.065 mm³**（sub-0.1 mm³）可注射式溫度感測 mote，**耗電 <1 nW**、解析度 **<50 mK**，已在小鼠腦與後肢**體內驗證**，用的是**市售 PZT 薄片＋CMOS**。【摘要驗證，來源 15】

8. **智財被 UC Berkeley → Iota → Astellas 圈死，且還在持續發證。** 「Implants using ultrasonic backscatter」專利族已查得 **US10300309、US10300310、US10576305、US11589748、US11786124（輻射偵測／腫瘤）、US12239408（生理感測，2025-03-04 發證）**。【摘要驗證，來源 16、17】**台廠做系統必踩；做元件與體外發射端相對乾淨。**

9. **PZT 含鉛不是「決定性障礙」，但是「決定性成本」。** 現況是：PZT **必須完全氣密隔離**於組織與體液（ISO 14708 主動植入醫材／ISO 10993 生物相容性），業界已用此法量產（哥倫比亞的 0.065 mm³ mote 就是用市售 PZT）。【摘要驗證，來源 18】EU RoHS 對「PZT 壓電陶瓷」的鉛豁免（新編號 **7(c)-VI**）**僅展延至 2027-12-31**。【摘要驗證，來源 19】**⇒ 無鉛不是准入門檻，但氣密封裝是；而 RoHS 豁免的短天期是一個真實的排程風險。** 無鉛替代（KNN、BNT-BT、BaTiO₃、PVDF）已有 2024 年 Nature Communications 級的植入驗證：**無鉛雙頻超音波植入物做無線雙相深部腦刺激**（夾層多孔 1-3 型壓電複合材）。【摘要驗證，來源 20】

10. **競爭技術中，磁電（ME）在功率密度上已明確勝過超音波。** ME 達 **3.1 mW/mm²**（≥1 cm 深度，宣稱為 mm 級植入物先前紀錄的 4 倍以上），可對 **10 mm² 與 27 mm²** 接收器分別送 **31 mW 與 56 mW**，工作頻率僅約 **250 kHz**，深度可到 **30 mm**。【摘要驗證，來源 21】**這是本文最重要的反面證據：如果客戶的假設是「超音波功率最大」，那已經不成立了。**

---

## 2. 查證結果 / 現況

### 2.1 物理與法規天花板（第一優先，全部查到）

**FDA Track 3 聲輸出上限**【摘要驗證，來源 1】
Track 3 不依應用別設限，而是要求 global maximum derated **ISPTA ≤ 720 mW/cm²**，且 **MI ≤ 1.9** 或 derated ISPPA ≤ 190 W/cm² 二擇一。應用別例外：**心臟 ISPTA ≤ 430 mW/cm²**；連續波胎兒影像等 **ISPTA ≤ 94 mW/cm²**；眼科 **ISPTA.3 = 50 mW/cm²、MI = 0.23、TI = 1.0**。

**⚠️ 適用範圍的誠實說明**：本輪一則搜尋摘要聲稱「法規對超音波無線供電與診斷影像分開設限、另有專屬上限」，但**該說法未附任何可指認的法規文件，且與其他來源不一致**。【存疑／衝突】**我的判斷是：目前公開文獻普遍把 720 mW/cm² 當作「業界自我約束的基準線」引用（多篇論文明示「below FDA safety limits」），但這不等於 FDA 已為植入供電發射器建立獨立的聲輸出上限。做產品時必須走 PMA／IDE 個案協商，不能假設有現成上限可依循。**

**組織聲學參數**【摘要驗證，來源 5、22】

| 介質 | 衰減係數 (dB/cm/MHz) |
|---|---|
| 脂肪 | 0.6 |
| 肝 | 0.5 – 0.94 |
| 腎 | 1.0 |
| 肌肉 | 1.3 – 3.3 |
| 骨（皮質） | 9.94（另一來源稱「約 20，幾乎不透波」） |
| 骨（小樑） | 6.9 |
| 空氣 | 12 |

顱骨功率衰減：**220 kHz → 5.0±2.4 dB；650 kHz → 14.9±3.2 dB；1000 kHz → 24.1±6.3 dB**；插入損耗隨頻率約 **−10 dB/MHz**，「經額骨量測在 **2 MHz 以下**才可能可行」。顱骨厚度變化 **0.1 mm** 即造成顱內峰值壓力誤差 **>2.6%**；換能器與顱骨間距造成的波疊加可帶來 **30–40%** 的顱內峰壓不確定度。【摘要驗證，來源 5、23】

### 2.2 商業現實：EBR Systems WiSE CRT（第二優先）

**法規與臨床**【摘要驗證，來源 6、7、24】
- FDA **PMA 核准函 2025-04-11**，PMA 編號 **P240028**。核准前製造廠查核（2025 年 1 月）**無 483 觀察項**。
- 適應症：**≥22 歲**、有 CRT 適應症、已有或符合右心室起搏系統資格，且屬 (a) 先前冠狀竇導線植入失敗／已關閉（"previously untreatable"），或 (b) 已植入 PM/ICD 者。**——這是明確的「救援療法（rescue therapy）」定位，不是一線 CRT。**
- SOLVE-CRT：**LVESV 改善 16.4%（p=0.003）**、**免於 Type I 併發症 80.9%（p<0.001）**、**急性起搏擷取 92%**、**12 個月裝置留存 96%**。試驗因期中分析達標而提前中止。

**系統構型（本專案最該學的部分）**【摘要驗證，來源 10、25】
三件式：(i) 植入**肋間**、皮下的超音波發射器／脈衝產生器；(ii) 植入**左腋下**的獨立電池模組；(iii) 植入**左心室內膜**的超音波感應接收電極（電極本體 **9.1 mm**，媒體形容「米粒大小」），以 **12F 輸送鞘**送入左心室。運作方式：共植入裝置起搏右心室後，發射器以極短延遲（**3–10 ms**）送出預設超音波脈衝，電極把聲能轉成電能起搏左心室，達成雙心室起搏。

**⇒ 這裡有一個對本專案極重要的觀察：EBR 的發射器不是「體外貼片」，而是「第二顆植入物」。** 前兩版 dossier 推測「病人要每天戴體外背心」是**錯誤的**——真實產品選擇了**把發射端也植入**，代價是需要一個第二切口、一顆會沒電的電池，以及一個解剖學上的「聲窗」條件。

**限制條件**【摘要驗證，來源 10、11】
- 發射器必須落在足夠聲窗：**肋軟骨間距 ≥1 cm、寬 ≥2.5 cm**。
- 電池壽命：**目前約 4 年**；壽命與**起搏閾值振幅＋發射器至接收器距離之和成反比**——即「病人胖一點、電極遠一點，電池就更短命」。

**財務**【摘要驗證，來源 8、9、26；另 FY2025 數字取自本 repo `05-market-funding-startups.md` 已驗證條目】

| 期間 | 營收 | 淨損 |
|---|---|---|
| FY2025（PMA 核准當年） | USD **1.6M** | USD **48.8M** |
| TTM 至 2026-03-31 | USD **≈3.98M** | USD **≈55.28M** |
| 2026 全年市場預估 | USD **16.2M**（預估，非實績） | — |

其他：**2026 Q1 商業植入 41 例**，案量較 2025 Q4 「增加逾一倍」；**2026 年 6 月啟動約 A$150M 增資**（股價下挫）；因具 Breakthrough Device Designation，預期取得 **NTAP（住院）＋ TPT（門診）** 給付；CMS **提案決定約 2026 年 12 月、最終 NCD 約 2027 年 3 月**。

**⇒ 誠實解讀：從 FDA 核准（2025-04）到 Medicare 全國給付定案（2027-03）之間有近兩年、累計逾一億美元淨損的空窗。這是「醫材植入」這條路的真實資金曲線。**

### 2.3 Iota Biosciences / Astellas（第二優先，部分查到）

【摘要驗證，來源 27、28】
- **2024-10-10** FDA 核准 IDE，進行首次人體早期可行性研究（EFS）。
- 適應症：**低活動性膀胱（underactive bladder, UAB）**，裝置直接刺激**膀胱壁**誘發收縮以協助排空。
- 分期核准：**第一階段 3 名受試者（至少各一男一女）**，安全性達標後擴至**總共 10 名**。
- 技術定位：源自 UC Berkeley 的「neural dust」，**超音波供電、無電池**，因此「可用侵入性較低的方式植入到現有產品到不了的部位」。
- **裝置尺寸／功率／深度：查無任何工程數字**，官方僅稱「grain-sized」。
- 併購金額（USD 約 3.04 億：頭期 1.275 億＋里程碑最高 1.765 億）為本 repo 其他文件既有的已驗證條目，本輪未重複查證。
- **2025–2026 進度：查無**。最新公開資訊仍停在 2024-10。**這本身就是訊號：18 個月無公開進展。**

### 2.4 Motif Neurotech（磁電，競爭技術）

【摘要驗證，來源 29、30、31、32】
- 裝置 **DOT**（Digitally programmable Over-brain Therapeutic），**寬約 1 cm**，**磁電無線供電**，硬膜外／腦表面刺激，不直接接觸皮質。
- 募資：**2024-01 A 輪 USD 18.75M**（Arboretum Ventures 領投）；自 2022 年成立累計創投募資 **>USD 30M**（Arboretum、KdT、Dolby Family Ventures），另有英國政府、DARPA、NIH 非稀釋性資金。**查無 B 輪。**
- 臨床：已取得 **FDA 核准展開首個治療型 BCI 臨床試驗**（難治型憂鬱症），合作機構包含 Baylor、MGB、Emory、University of Iowa、University of Utah Health、NYU 等。2024 年已完成人體迷你腦刺激器示範（medRxiv：Millimeter-sized battery-free epidural cortical stimulators）。2025-12 啟動病人登錄庫。

**⇒ 顱內這一塊，磁電已經領先超音波進入臨床。這與 2.1 的顱骨衰減物理完全一致，不是巧合。**

### 2.5 兩用元件的最佳體現：Berkeley / Columbia 系列（第四優先）

| 裝置 | 體積 | 壓電體 | 同時擔任的角色 | 關鍵數字 |
|---|---|---|---|---|
| **StimDust**（Berkeley, CICC 2018） | **6.5 mm³** | 單顆 750×750×750 µm³ | 受電 ＋ 下行通訊 ＋ backscatter 讀出 ＋ 刺激 | 峰值晶片效率 **82%**；backscatter 以壓電電負載調變聲反射幅度，回傳 **1 bit**（刺激 on/off） |
| **DustNet**（arXiv 2511.14986, 2025） | 壓電 0.7×0.7×0.7 mm³ ＋ 28 nm CMOS 0.43 mm² | 同上 | 受電 ＋ 多節點網路 backscatter | TDMA ＋ **16 階 ASK**；2 MHz 載波下**最高 200 kb/s**；單顆上行 **50 kb/s @ 7 µW**；CDMA 版本量到 **784 kbps** 通道總速率 |
| **Columbia sub-0.1 mm³ mote**（Science Advances 2021） | **0.065 mm³**，可注射 | 市售 PZT 薄片 ＋ CMOS | 受電 ＋ backscatter 遙測 ＋ 溫度感測 | 耗電 **<1 nW**；解析度／準確度 **<50 mK**；**小鼠腦與後肢體內驗證** |

**這三顆是「主動/被動兩用壓電元件」最乾淨的實證：同一塊壓電陶瓷是能量接收器（被動）、是通訊調變器（被動反射調變）、是刺激驅動源（主動）、是感測讀出通道。**

補充：另有「Flexible circuit-free system via passive modulated ultrasound for wireless thoracic pressure monitoring」（Science Advances），以電阻式壓力感測器直接當 backscatter 調變器，**全無電路**——這是被動兩用的極端案例。【摘要驗證，來源 33】

---

## 3. 關鍵數字表

### 3.1 競爭技術量化比較（第三優先）

| 技術 | 可達深度 | 接收器最小尺寸 | 可傳輸功率 | 效率 | 安全上限 | 致命弱點 |
|---|---|---|---|---|---|---|
| **超音波** | **>5 cm 已驗證**；SOTA 植入物多在 5–6 cm 內 | **0.065 mm³**（Columbia mote，含 CMOS） | **18.8 µW – 0.66 mW**（mm 級）；相位陣列 16 元素 @1.1 MHz、20 mm 焦點可送 **6 mW** | **2%–30%**（UTET 峰值 27% @70 mW/40 mm） | ISPTA 720 mW/cm²（心臟 430）、MI 1.9 | **骨與氣體歸零**；需聲窗；需對位 |
| **磁電（ME）** | **30 mm** 已驗證 | 10 mm²／27 mm² 級接收面 | **31 mW（10 mm²）／56 mW（27 mm²）**；功率密度 **3.1 mW/mm²** | 未查得端到端數字 | 低 SAR（~250 kHz 近場磁場） | 需外部線圈／磁場源；對位敏感度有專文處理（omnidirectional 研究） |
| **RF 中場（midfield, Poon PNAS 2014）** | **>5 cm** | mm 級 | **>200 µW**（1.6 GHz，源功率 500 mW，等同手機） | 未查得 | SAR（於 Bay Area Compliance Labs 量測） | 組織吸收；接收器 ≪ 波長時耦合效率崩潰 |
| **感應耦合（inductive）** | 淺（皮下為主） | 線圈受限於面積 | 高（近距離） | 高（近距離） | SAR / IEC 60601 | **深度差、需大線圈**；文獻共識為超音波優於感應之處 |
| **光學／NIR 光伏** | **數 mm，最多約 10 mm**（有 phantom 可到 50 mm 但僅產生電壓） | 極小 | **數十 µW** | 低 | 光熱／ANSI 光暴露 | **深度是硬傷** |
| **內建電池（Micra VR2）** | 不限（自帶） | **0.8 cc = 800 mm³** | 不受供電限制 | — | — | **體積大 100–10000 倍**；壽命 **16.7 年（VR2）／15.6 年（AV2）** 後需更換 |

> **關鍵洞察**：超音波唯一無可取代的維度是「**體積**」——0.065 mm³ vs 800 mm³ 差 **4 個數量級**。功率上超音波已被 ME 超越（3.1 mW/mm² vs ~0.66 mW/mm² 量級），深度上與 ME、midfield 相近。**如果你的應用不需要「小到可用針注射」，超音波供電沒有非贏不可的理由。**

### 3.2 功率預算天花板（自行推算，推導見第 5 節）

| 項目 | 數值 | 備註 |
|---|---|---|
| ISPTA 上限換算 | **7.2 mW/mm²** | 720 mW/cm² |
| 1 mm² 接收面最大攔截聲功率 | **7.2 mW** | 理想聚焦、全部攔截 |
| 乘以實測效率 10–30% | **0.72 – 2.2 mW** | 理論上限 |
| 公開文獻實測 | **18.8 µW – 0.66 mW** | 與理論差 3–40 倍 |
| MI=1.9 @1 MHz 對應峰值負壓 | **1.9 MPa** | MI = p_r.3/√f |
| 該峰壓對應瞬時強度 | **≈120 W/cm²** | I = p²/(2Z)，Z=1.5 MRayl |
| 在 ISPTA 720 mW/cm² 下的最大工作週期 | **≈0.6%** | 720 mW/cm² ÷ 120 W/cm² |
| **脈衝相對連續波的瞬時功率槓桿** | **≈170×** | **這是本領域最重要的設計自由度** |

---

## 4. 對決策的意涵 / 機會清單

### 4.1 對「主動/被動兩用元件」命題的直接支持

1. **這是全專案唯一能同時指出「四職合一的實體元件」「FDA PMA 產品」「3 億美元併購」的應用場域。** 若要對客戶論證「兩用壓電元件不是概念」，本場域是最強的證據來源。
2. **「非替代性新能力」的定義在此非常乾淨**：0.065 mm³ 可注射式體內感測節點，**沒有任何電池方案做得到**（Micra 已是電池的極限，仍有 800 mm³）。這不是取代電感或電池，是開啟一個電池物理上進不去的尺寸帶。
3. **backscatter 是「被動性」創造價值的教科書案例**：不發射、不耗能、只改變自身電負載就改變聲反射係數——DustNet 因此能以 **7 µW 換 50 kb/s**。任何主動無線電都做不到這個能效。

### 4.2 台廠切入點（誠實版）

**建議：做材料與換能器供應鏈，不要做系統。** 證據如下：

- **系統路的成本結構已被 EBR 標定**：FDA PMA 核准後仍需 **年淨損 USD 50M+**、**A$150M 增資**、**等到 2027 年才有全國給付**。這不是台灣中小型醫材廠的資金曲線。
- **智財被鎖**：ultrasonic backscatter 專利族由 UC Regents 持有並持續發證至 **2025 年（US12239408）**，經 Iota 獨家授權給 Astellas。做系統＝正面衝突。
- **台灣現有能力盤點（本輪查證結果）**：
  - **鐿鈦科技（4163）**：2004 年成立、2012-11 上櫃，**醫療器材精密金屬零件專業製造商**，長年替國際級醫療大廠代工，產品含腹腔鏡器械零件、脊椎釘、骨釘骨板、牙科植體。【摘要驗證，來源 34】**——這是「精密件＋國際大廠代工關係」，可對接的是換能器外殼、氣密封裝件、輸送系統（如 12F 鞘管類）。**
  - **台微醫（TMC）**：鐿鈦轉投資，**明確策略是「不代工、只做品牌與研發」**，主打二三類高階植入醫材、脊椎微創。【摘要驗證，來源 35】**——與供應鏈定位相反，不是代工夥伴人選。**
  - **CTDCO（Ceramic Transducer Design Co., Ltd.，1990 年成立於台灣）**：壓電換能器與超音波感測器製造商，客戶列表含 Siemens、TI、Panasonic 等。【摘要驗證，來源 36】**——這是本輪唯一查到的台灣壓電換能器廠，但無醫療植入級佐證。**
  - **聯合骨科**：**查無**任何電子／主動醫材相關資料。
- **可對接的三個具體產品位置**：
  1. **µm–mm 級單晶／陶瓷壓電塊**（0.7×0.7×0.7 mm³ 等級的切割、拋光、電極化、良率）——這是純材料與加工題，台灣有機會。
  2. **氣密封裝與生物相容外殼**（PZT 必須完全隔離；ISO 14708／ISO 10993 溶出試驗）——鐿鈦類精密金屬廠的既有能力可延伸。
  3. **體外／體內發射端相位陣列模組**（16 元素、10.9×9×1.7 mm³、100 V 驅動級）——這是換能器陣列＋高壓驅動，台灣被動元件與 MEMS 供應鏈可切入，且**智財相對乾淨**。

**但必須向客戶說清楚三件事**：
- 這是**低量、高認證負擔、長導入期**的生意（EBR 2026 Q1 全球只植入 41 例），與台灣被動元件廠賴以生存的規模經濟模式**正好相反**。
- 客戶只有 Astellas/Iota、EBR、Motif 等**個位數家**，議價權在他們手上。
- 進入門檻是 **ISO 13485＋設計歷史檔案＋可追溯性**，不是技術。

### 4.3 值得追蹤的三個時間點

| 時間 | 事件 | 為何重要 |
|---|---|---|
| **2026-12** | CMS 對 WiSE CRT 的**提案給付決定** | 決定超音波供電植入的第一個真實市場規模 |
| **2027-03** | CMS **最終 NCD** | 同上 |
| **2027-12-31** | EU RoHS 對 PZT 壓電陶瓷鉛豁免 **7(c)-VI 到期** | 決定無鉛壓電是否從「加分」變成「必要」 |

---

## 5. 反面證據與物理／法律上限

### 5.1 推導攤開（自行推算）

**(a) 1 mm² 接收面的功率上限**
720 mW/cm² = 7.2 mW/mm²。1 mm² 完美攔截 ⇒ 7.2 mW 聲功率。以第 3 節查得的 2%–30% 端到端效率 ⇒ **0.14 – 2.2 mW 電功率**。與實測 18.8 µW–0.66 mW 相符（實測偏低是因為聚焦不完美、對位誤差、阻抗失配）。

**(b) 脈衝供電的槓桿**
MI = p_r.3 / √f。MI=1.9、f=1 MHz ⇒ p_r ≤ 1.9 MPa。I_peak = p²/(2Z)，Z=1.5×10⁶ Rayl ⇒ I = (1.9×10⁶)²/(3×10⁶) = 1.2×10⁶ W/m² = **120 W/cm²**。ISPTA 720 mW/cm² 是**時間平均**，因此最大工作週期 = 0.72/120 ≈ **0.6%**。**⇒ 用 0.6% 工作週期的脈衝，瞬時功率可比連續波高約 170 倍，能量先存電容再一次放掉。StimDust 用脈衝而非連續波，正是這個原因。**

**(c) 軟組織—空氣界面**
Z_soft ≈ 1.63 MRayl、Z_air ≈ 0.0004 MRayl。R = ((Z₂−Z₁)/(Z₂+Z₁))² ≈ **0.9990** ⇒ **>99.9% 反射**。肺與腸氣後方**不是效率差，是歸零**。（軟組織—骨界面的 43% 反射率為文獻值。）

**(d) 深度衰減 vs 「derated」的關係——一個常被搞錯的點**
ISPTA.3 的「.3」代表以 **0.3 dB/cm/MHz** 的均質模型 derate。這表示：法規約束的是**體內原位**強度，不是水中源強度。因此組織衰減主要吃掉的是**發射端的電池能量**，而非接收端可得功率——直到發射器本身的功率／發熱極限。**這對系統設計的意涵是：深度增加傷害的是「發射器電池壽命」，這正好解釋了 WiSE「電池壽命與發射器—接收器距離成反比」的臨床觀察。**【自行推算＋來源 11 佐證】

### 5.2 明確的反面證據

1. **磁電已在功率密度上勝出。** ME 的 3.1 mW/mm²（≥1 cm）對比超音波 mm 級接收器的 ~0.66 mW/mm² 量級——**「超音波是深部供電最強」這個假設在 2023 年之後已不成立**，超音波剩下的護城河是「最小體積」與「不需外部磁場源」。【來源 21】
2. **顱內市場對超音波實質關閉。** 1 MHz 穿顱功率衰減 24.1 dB（僅剩 0.4%），且顱骨厚度 0.1 mm 變化就造成 >2.6% 顱內壓力誤差、換能器間距造成 30–40% 不確定度——**這不是「難」，是「無法保證劑量」**。Motif 用磁電做腦刺激不是偏好，是物理選擇。【來源 5、23】
3. **超音波供電並沒有解決電池問題，只是把電池搬到別處。** WiSE 的電池仍是植入物，仍約 4 年壽命，仍需更換手術；而它取代的 Micra 內建電池有 16.7 年。**「無電池」是對「接收端」成立，對「系統」不成立。**【來源 11、12】
4. **商業速度極慢。** EBR：PMA 核准（2025-04）→ 首個完整年營收 1.6M USD → TTM 至 2026-03 為 3.98M USD、淨損 55.28M USD → 2026-06 再增資 A$150M → CMS 最終給付 2027-03。**核准到現金流之間 ≥2 年、≥1 億美元。**
5. **Iota 已 18 個月無公開進展。** 2024-10 拿到 IDE 後（分期核准，第一階段僅 3 人），至本輪查詢（2026-07）**查無任何後續**。對一個被 3 億美元收購的資產而言，這是需要警惕的沉默。
6. **適應症是「救援」不是「一線」。** WiSE 的 FDA 適應症限於 CS 導線植入失敗或已有 PM/ICD 者——**天花板由「傳統 CRT 失敗率」決定，不是由「CRT 病人總數」決定**。
7. **解剖學排除。** WiSE 要求肋軟骨間距 ≥1 cm × 2.5 cm 的聲窗——這會**篩掉一部分病人**，且無法用工程改善。
8. **PZT 的鉛不是禁令，但 RoHS 豁免只到 2027-12-31**，且無鉛替代（KNN/BNT-BT）雖已達「與軟 PZT 同級 d₃₃」的實驗室成果，仍需重新做全套 ISO 10993／長期穩定性／滅菌相容性——**材料換代的成本落在供應鏈上，也就是台廠身上**。

---

## 6. 未解問題

1. **WiSE 的實際工作頻率與聲輸出是多少？是否落在 720 mW/cm² 之內？** 若 EBR 已被 FDA 核准以**超過**診斷上限的強度運作，那將徹底改寫本文第 3.2 節的功率預算（可能放寬數倍）。**這是本文最高價值的未解問題**，需取得 P240028 SSED 全文（https://www.accessdata.fda.gov/cdrh_docs/pdf24/P240028B.pdf）。
2. **FDA 對「非診斷用途的植入供電超音波」到底適用哪條上限？** 文獻普遍引用 720 mW/cm² 作自我約束，但這是否為法規要求、或僅為慣例，本輪未能釐清（見 2.1 存疑段）。
3. **Iota 的 EFS 進度如何？裝置實際尺寸與功率？** 官方 18 個月無更新；需 ClinicalTrials.gov 檢索與 Astellas 財報／研發管線頁核對。
4. **RoHS 2011/65/EU 是否根本排除主動植入式醫材？** 若是，則 7(c)-VI 豁免到期對本應用**不構成風險**，第 4.3 節的時間點需刪除。**這是一個 15 分鐘就能查清、但會改變結論的問題。**
5. **台灣是否有醫療級（ISO 13485）壓電陶瓷／單晶材料供應能力？** 本輪中文查詢完全失敗；CTDCO 僅有工業級佐證。**若答案是「沒有」，則第 4.2 節的建議需退回到「精密封裝件與輸送系統」這一更窄的位置。**

---

## 7. 來源清單

1. FDA Guidance for Industry and FDA Staff — Information for Manufacturers Seeking Marketing Clearance of Diagnostic Ultrasound Systems and Transducers — https://downloads.regulations.gov/FDA-2017-D-5372-0003/content.pdf — Track 3 上限 ISPTA.3 ≤ 720 mW/cm²、MI ≤ 1.9，及心臟 430／胎兒 94／眼科 50 mW/cm² 的應用別例外。
2. A Millimeter Scale Piezoelectric Receiver with Sub-Milliwatt Output for Ultrasonic Wireless Power Transfer in Water (IEEE) — https://ieeexplore.ieee.org/document/9495447/ — mm 級壓電接收器在 7.2 mW/mm² 聲源下實測收得 0.66 mW。
3. An ultrasound-induced wireless power supply based on AlN piezoelectric micromachined ultrasonic transducers (Scientific Reports) — https://www.nature.com/articles/s41598-022-19693-5 — 輸出 18.8 µW、功率密度 7.36 µW/mm²，充飽 100 µF 至 3.19 V，宣稱在 FDA 限值以下。
4. A Comprehensive Comparative Study on Inductive and Ultrasonic Wireless Power Transmission to Biomedical Implants — https://pmc.ncbi.nlm.nih.gov/articles/PMC6192045/ — 感應 vs 超音波比較；相關效率數字（UTET 27% @673 kHz/40 mm/70 mW）。
5. Mathematical Model of Ultrasound Attenuation With Skull Thickness for Transcranial-Focused Ultrasound (Frontiers in Neuroscience) — https://www.frontiersin.org/journals/neuroscience/articles/10.3389/fnins.2021.778616/full — 顱骨功率衰減 220 kHz 5.0 dB／650 kHz 14.9 dB／1000 kHz 24.1 dB；顱骨厚度敏感度。
6. FDA Approves WiSE System, World's First and Only Leadless Left Ventricular Endocardial Pacing (LVEP) Device for CRT (BioSpace) — https://www.biospace.com/press-releases/fda-approves-wise-system-worlds-first-and-only-leadless-left-ventricular-endocardial-pacing-lvep-device-for-crt — PMA 核准公告。
7. EBR Systems SEC EX-99.1（2025） — https://www.sec.gov/Archives/edgar/data/1347123/000121465925005814/ex99_1.htm — 2025-04-11 核准函、五個 PMA 模組、2025-01 廠查無 483。
8. EBR Systems (ASX:EBR) — Stock Analysis — https://stockanalysis.com/quote/asx/EBR/ — TTM 至 2026-03-31 營收約 USD 3.98M、淨損約 USD 55.28M。
9. EBR Systems (ASX:EBR) lands CMS gate with March 2027 Medicare date — https://stocksdownunder.com/ebr-systems-asxebr-cms-ncd/ — NTAP／TPT 預期、CMS 提案 2026-12、最終 NCD 2027-03。
10. WiSE Cardiac Resynchronization Therapy (CRT) System Instructions for Use（FDA） — https://www.accessdata.fda.gov/cdrh_docs/pdf24/P240028D.pdf — 三件式構型、聲窗要求（肋軟骨間距 ≥1 cm × 2.5 cm）、12F 輸送鞘。
11. LV endocardial wireless pacing for heart failure (WiSE-CRT): parameters relevant for longevity（Europace） — https://academic.oup.com/europace/article/19/suppl_3/iii19/3872429 — 電池壽命約 4 年；壽命與閾值振幅＋發射器接收器距離成反比。
12. Device longevity of a leadless pacemaker family（PMC） — https://pmc.ncbi.nlm.nih.gov/articles/PMC12330253/ — Micra 體積 0.8 cc；VR2 中位推估壽命 16.7 年、AV2 15.6 年、VR 12.3 年、AV 10.8 年。
13. StimDust: A 6.5mm³, Wireless Ultrasonic Peripheral Nerve Stimulator with 82% Peak Chip Efficiency（IEEE CICC 2018 / eScholarship） — https://escholarship.org/uc/item/8px811qc — 6.5 mm³、單顆 750 µm 立方壓電同時供電/通訊/backscatter、82% 峰值晶片效率。
14. DustNet: A Wireless Network of Ultrasonic Neural Implants（arXiv 2511.14986） — https://arxiv.org/pdf/2511.14986 — 0.7 mm 立方壓電＋28 nm CMOS 0.43 mm²；TDMA＋16 階 ASK；200 kb/s @2 MHz；50 kb/s @7 µW。
15. Application of a sub–0.1-mm³ implantable mote for in vivo real-time wireless temperature sensing（Science Advances） — https://www.science.org/doi/10.1126/sciadv.abf6312 — 0.065 mm³、<1 nW、<50 mK、小鼠腦與後肢體內驗證、市售 PZT＋CMOS。
16. US12239408 — Implants using ultrasonic backscatter for sensing physiological conditions（2025-03-04 發證） — https://patents.justia.com/patent/12239408 — UC Berkeley backscatter 感測專利族最新一件。
17. US11786124 — Implants using ultrasonic backscatter for radiation detection and oncology — https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/11786124 — 同族，延伸至放射偵測與腫瘤應用。（同族另見 US10300309、US10300310、US10576305、US11589748。）
18. Piezoelectricity For Implantables: Encapsulation, Sterilization And Long-Term Stability（PatSnap Eureka） — https://eureka.patsnap.com/report-piezoelectricity-for-implantables-encapsulation-sterilization-and-long-term-stability — PZT 須完全氣密隔離；ISO 14708／ISO 10993 為合規依據；封裝材料須證明不溶出。
19. EU Updates RoHS Directive with Revised Lead Exemption Clauses（CIRS Group） — https://www.cirs-group.com/en/chemicals/eu-updates-rohs-directive-with-revised-lead-exemption-clauses — 2025-11-21 三份 Delegated Directives；PZT 壓電陶瓷鉛豁免（新編號 7(c)-VI）至 2027-12-31。
20. Lead-free dual-frequency ultrasound implants for wireless, biphasic deep brain stimulation（Nature Communications 2024） — https://www.nature.com/articles/s41467-024-48250-z — 無鉛夾層多孔 1-3 型壓電複合材、雙頻、可程式雙相刺激脈衝、癲癇鼠模型長期生物安全性。
21. Magnetoelectrics enables large power delivery to mm-sized wireless bioelectronics（PubMed / bioRxiv） — https://pubmed.ncbi.nlm.nih.gov/37692260/ — 功率密度 3.1 mW/mm²（≥1 cm 深）、對 10 mm²／27 mm² 接收器送 31／56 mW、~250 kHz、深度 30 mm。
22. Intensive Care Ultrasound: I. Physics, Equipment, and Image Quality（PMC） — https://pmc.ncbi.nlm.nih.gov/articles/PMC5475422/ — 各組織衰減係數；軟組織—骨界面反射率 43%；軟組織—含氣肺界面全反射。
23. Effects of skull properties on long-pulsed transcranial focused ultrasound transmission（arXiv 2405.08489） — https://arxiv.org/pdf/2405.08489 — 顱骨厚度 0.1 mm 變化 → 顱內峰壓誤差 >2.6%；換能器間距造成 30–40% 不確定度。
24. World's Smallest Leadless Pacemaker Shows Clinical Benefits in Patients with Previous CRT Failure（HRS） — https://www.hrsonline.org/news/wise-crt-system-crt/ — SOLVE-CRT 結果與「先前 CRT 失敗」定位。
25. Leadless left ventricular stimulation with WiSE-CRT System — Phase I of SOLVE-CRT（Heart Rhythm） — https://www.heartrhythmjournal.com/article/S1547-5271(21)01808-7/fulltext — 系統構型、3–10 ms 延遲、電極 9.1 mm、12F 鞘。
26. EBR Systems (ASX:EBR) Launches $150m Capital Raise, Shares Stumble（Kalkine） — https://kalkine.com.au/news/general-news/ebr-systems-asxebr-launches-150m-capital-raise-shares-stumble — 2026-06 約 A$150M 增資；2026 Q1 商業植入 41 例。
27. FDA Grants iota Biosciences IDE Approval for First-In-Human Early Feasibility Study with Implantable Bladder Device（Astellas Newsroom, 2024-10-10） — https://newsroom.astellas.us/2024-10-10-FDA-Grants-iota-Biosciences-IDE-Approval-for-First-In-Human-Early-Feasibility-Study-with-Implantable-Bladder-Device — IDE 核准、UAB 適應症、分期 3→10 人。
28. Astellas subsidiary Iota wins FDA IDE nod to study implantable bladder device（MassDevice） — https://www.massdevice.com/iota-fda-ide-implantable-bladder-device/ — 「grain-sized」、超音波供電無電池、可達現有產品到不了的部位。
29. Brain-computer interface based on Rice research wins FDA approval for first clinical trial（Rice News, 2026） — https://news.rice.edu/news/2026/brain-computer-interface-based-rice-research-wins-fda-approval-first-clinical-trial — Motif DOT 首個臨床試驗核准、多中心名單。
30. Rice Biotech Launch Pad startup Motif Neurotech closes Series A financing of $18.75 million（Rice News, 2024） — https://news.rice.edu/news/2024/rice-biotech-launch-pad-startup-motif-neurotech-closes-series-financing-1875-million — A 輪 USD 18.75M、Arboretum 領投。
31. Millimeter-sized battery-free epidural cortical stimulators（medRxiv） — https://www.medrxiv.org/content/10.1101/2023.09.13.23295460v1 — Motif 前身技術的人體示範。
32. Motif Neurotech Launches Patient Registry for Future Research Opportunities（Business Wire, 2025-12-16） — https://www.businesswire.com/news/home/20251216800381/en/Motif-Neurotech-Launches-Patient-Registry-for-Future-Research-Opportunities — 病人登錄庫、累計 >USD 30M 募資與非稀釋性資金來源。
33. Flexible circuit-free system via passive modulated ultrasound for wireless thoracic pressure monitoring（Science Advances） — https://www.science.org/doi/10.1126/sciadv.ads5634 — 電阻式壓力感測器直接作為 backscatter 調變器，全無電路的被動遙測。
34. 鐿鈦科技股份有限公司（環球生技月刊） — https://news.gbimonthly.com/tw/invest/show2.php?num=87 — 2004 成立、2012-11 上櫃、醫材精密金屬零件、國際大廠代工經驗、產品線。
35. 台灣微創醫療器材—鐿鈦子公司台微醫 IPO 啟動 — https://haoge.pixnet.net/blog/post/312166305 — 台微醫堅持不代工、只做品牌與研發，主打二三類高階植入醫材。
36. Ceramic Transducer Design Co., Ltd.（CTDCO，台灣） — https://www.ctdco.com.tw/index.php?lang=en — 1990 年成立於台灣的壓電換能器與超音波感測器製造商。
37. Wireless power transfer to deep-tissue microimplants（PNAS 2014, Ada Poon 團隊） — https://www.pnas.org/doi/pdf/10.1073/pnas.1403002111 — 中場 RF 於 >5 cm 深度輸送 >200 µW；1.6 GHz；源功率 500 mW。
38. Subcutaneous power supply by NIR-II light（PMC） — https://pmc.ncbi.nlm.nih.gov/articles/PMC9633840/ — 光伏供電深度數 mm～約 10 mm、輸出數十 µW 級。
39. A Study on Ultrasonic Wireless Power Transfer with Phased Array for Biomedical Implants（PMC） — https://pmc.ncbi.nlm.nih.gov/articles/PMC10664043/ — 16 元素陣列 10.9×9×1.7 mm³、1.1 MHz、100 V 驅動、20 mm 焦點、0.8 MPa、可送 6 mW。
40. FDA P240028 Summary of Safety and Effectiveness Data（WiSE CRT） — https://www.accessdata.fda.gov/cdrh_docs/pdf24/P240028B.pdf — SOLVE-CRT 結果與適應症原始文件（**本輪未能取得全文，第 6 節列為最高優先待查**）。
