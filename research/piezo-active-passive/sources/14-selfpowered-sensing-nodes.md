# 應用A5：自供電/無電池節點、結構健康監測、兩用元件的系統級效益

> **一句話結論：這個領域唯一被市場驗證的成功案例（Perpetuum，5,000+ 感測器、600+ 車輛、被 Hitachi Rail 併購）用的是「電磁式」採集器；EnOcean 二十五年來的三種採集技術（電磁、光伏、熱電）裡沒有壓電；唯一取得 FAA 認證並在 Delta 71 架 737 上服役的 SHM 技術是「氣壓式」CVM 而不是壓電導波。壓電在「採集端」已經被市場否決；它真正還沒被取代的位置是「主動端」——同一顆貼片能發射導波、能穿金屬壁送電、能在 125 °C 以上活著。因此客戶若要投入，敘事必須 100% 押在主動能力，把「自供電」降為附屬條件，而不是賣點。**

---

## 0. 研究方法與限制（誠實揭露）

1. **本輪實際執行 WebSearch：22 次呼叫，其中 20 次成功回傳結果，2 次因 session 額度（200/200）用盡而失敗。** 上一版本此檔案的成功搜尋次數為 0，本版為完整重做覆寫。
2. **WebFetch 與 curl 依環境限制全面 403，本輪未使用。** 因此所有事實來自 WebSearch 的結果摘要與標題，**未能開啟原始頁面逐字核對**。凡僅由搜尋摘要得知者，我標【V·摘要】；凡與多個獨立來源交叉一致者標【V·多源】。
3. **可信度分層標記**：
   - 【V·多源】= 本輪多個獨立來源一致，可信度高。
   - 【V·摘要】= 本輪搜尋摘要得知，單一來源，**未開啟原文驗證**。
   - 【V·轉引】= 本專案其他章節（01–21）已檢索並附 URL 的事實。
   - 【推導】= 我用公開規格自行計算，計算式寫在正文，可自行複核。**這類數字是算出來的，不是查到的。**
   - 【查無】= 本輪嘗試搜尋但未取得。
4. **本輪明確「查無」的項目（不可作為決策依據）**：
   - Acellent SMART Layer / ScanGenie 的**價格**（多次搜尋均無報價資訊）。
   - Perpetuum 感測節點的**功耗規格**、採集器**體積尺寸**、Hitachi Rail 收購**金額**。
   - Perpetuum 與 **Virgin Trains** 的合約（僅查到 Southeastern 與 Eversholt Rail）。
   - **EnOcean 的累計出貨量**（僅查到營收估值，且來自可信度低的商業資料庫）。
   - **SKF 壓電供電軸承滾動體感測**的真偽（額度用盡前未能查證，上一版已標低可信度）。
   - **Ossia / Energous** 的現況（額度用盡）。
   - **LM Wind Power / Bladena** 的商用葉片 SHM 產品（僅查到學術研究）。
   - **gPIMS 的電池壽命規格**（產品頁未揭露）。
   - **橋樑監測**的壓電商用系統（本輪未及查證）。
5. **我沒有捏造任何專利號、論文標題、公司名、產品型號或數字。** 第 7 節所有 URL 均為本輪搜尋結果實際回傳，或明確標註【轉引】自本專案其他章節。

---

## 1. 結論摘要

1. **【最重要】能量採集無線感測唯一的產業級成功案例，用的不是壓電。** Perpetuum（2004 年成立於 Southampton）明確被描述為「engineered, produced and commercialized a practical **electromagnetic** vibration harvesting micro-generator」，PMG7 微發電機在 **40–50 mg 振動下輸出約 3 mW，最高可達 5 mW**，工作在市電頻率 **50/60 Hz**【V·多源：eepower、ISA blog、Southampton REF3】。**這是對客戶最關鍵的一條反面證據。**
2. **EnOcean 二十五年的產品線裡沒有壓電。** 官方能量採集頁面列出的三種轉換器是 **electromagnetic（ECO 200 電動式）、solar（ECS 300）、thermoelectric（ECT 310）**；旗艦無線開關模組 PTM 210 / PTM 215 用的是 ECO 200 的電磁彈簧–線圈機構，不是壓電【V·多源：EnOcean 官網、PTM 200 datasheet】。**這是市場對「壓電做採集」長達二十五年的用腳投票。**
3. **能源採集這整個賽道的商業體量小到令人清醒。** EnOcean 作為此領域全球最知名的公司，成立於 2001 年，累計募資 **$45.6M**，2025 年營收估計僅 **$19.2M**；2022 年 11 月宣布的 SPAC 反向併購上市案**沒有完成**，公司至今未上市【V·摘要：Growjo / PitchBook / Memoori，商業資料庫估值，可信度中低】。
4. **航空 SHM 的第一張門票被非壓電技術拿走了。** 取得 FAA 認證並實際服役的是 Structural Monitoring Systems 的 **CVM（Comparative Vacuum Monitoring，比較式真空監測，氣壓原理）**：Delta 的 **71 架在役 737** 已裝設，737 後壓力隔框的檢查時間從 **24 小時縮短到 15 分鐘**；2016 年測試通過後 Service Bulletin **SB 737-57-1309** 被修訂，允許 CVM 作為替代檢查方法；同一技術也被提報為 KC-46A 的 CBM+ 方案【V·多源：AviationPros、marketopen、MDPI Aerospace 10(7) 587、ndt.net IWSHM 2025】。
5. **相對地，壓電導波 SHM 在航空側至今停在「可以開始取證」而非「已取證」。** Airbus 的 SHM 負責人 Clemens Bockenheimer 表示 **local SHM 已脫離 R&D、可針對特定機型進行 qualification**，但 **global SHM 的可靠度評估仍在發展中**；Airbus 用一架 A350 與 MSN001 A340（換裝 A350 XWB CFRP 蒙皮板）作飛行驗證機，Acellent 的 **SMART Layer 感測網路正在做撞擊偵測的飛行測試**——仍是測試，不是服役【V·摘要：CompositesWorld】。SAE **ARP6461**（2013 發布，**ARP6461A** 2021 年 8 月改版）只是「指引」，不是取證通過【V·多源：SAE Mobilus】。
6. **能量不是 SHM 的瓶頸——這一點必須修正上一版的判斷。** 航空 SHM 能量採集回顧論文給出：波傳播式 SHM 的功率需求是 **數 mW 到數百 mW**，**單次傳輸週期的最小能量約 10 mJ**【V·摘要：Sensors, PMC7700503】。以 CR2032 的 **≈2,430 J**【推導】計算，等於 **約 24 萬次**掃描週期。**一顆兩塊台幣的鈕扣電池就能涵蓋整個結構的服役期。** 反過來說，Perpetuum 級的 3–5 mW 採集器一天就能供應 **2.6–4.3 萬次** 10 mJ 週期【推導】——**兩邊都夠用，所以「能不能供電」根本不是決勝點，「裝得上、維護得起、認證得過」才是。**
7. **真正被驗證的「電池派工成本」數字比想像中小。** WirelessHART 的具名數字是：一組電池包約 **$150**，更換約 **1 小時人工 @ $100/hr**；部分廠商專用電池 **$250 以上**；以節點單價 $1,500 計，**全生命週期的電池更換支出約為初始投資的兩倍**；500 個儀表 → 3,000 顆電池 → **含人工約 $750,000**【V·摘要：New Equipment Digest / CPECN】。**這個數字支持「免電池有價值」，但每次僅 $250 量級，不足以支撐高單價壓電元件的溢價。**
8. **市場上真正在賣的「永久安裝主動導波監測」是壓電 + 電池，不是壓電自供電。** Guided Ultrasonics 的 **gPIMS®** 明確描述為「永久安裝在管線上的感測器 + 一台**電池供電**的自主現場控制單元」【V·摘要：guided-ultrasonics.com】。**產業已經給出答案：壓電負責主動發射，電池負責供電。這正是客戶應該接受的分工。**
9. **輪胎是壓電採集唯一還活著的大廠級口袋，但已停滯五年。** TDK 在 **CES 2021** 發表 **InWheelSense**，用 TDK 壓電陶瓷在**輪胎胎唇區（bead area，官方稱「最大發電區」）**同時做應變感測與能量採集，實現無電池的輪內遙測，並與 **Goodyear** 合作【V·多源：TDK 技術庫、EE Times、RFID Journal】。**但本輪查無任何量產車型或出貨資訊**，距發表已逾五年。

---

## 2. 現況：技術 / 產品 / 玩家

### 2.1 能量採集無線節點：誰活下來、用什麼技術

| 玩家 | 採集原理 | 本輪查證到的實績 | 對「壓電」的意義 |
|---|---|---|---|
| **Perpetuum**（英，2004 成立，Southampton 系） | **電磁式**（明文）【V】 | Southeastern 合約涵蓋 **148 列** Electrostar（**618 節車廂**）；已在 **112 列** class 375 EMU 完成部署；Kent 一地每日 **180 萬**資料點；自 2013 年起 **5,000+ 感測器**、**600+ 車輛**、**4 億 service-km**；Eversholt Rail 為 Class 465 採用【V·多源】 | **最強反證**：唯一產業級成功案例不是壓電 |
| **EnOcean**（德，2001 成立，Siemens 系） | **電磁 + 光伏 + 熱電**，**無壓電**【V】 | ECO 200 / ECS 300 / ECT 310 三大轉換器；PTM 210/215 開關模組；**ECO 200 官網已標「not recommended for new designs」**【V】 | 二十五年產品線零壓電 |
| **ReVibe Energy**（瑞典） | **電磁式**（明文）【V】 | modelD 可在 **0.05 g** 起工作、頻寬 **5 Hz**；VS1 自供電振動感測器（振動篩、給料機）【V·摘要】 | 同上 |
| **8power**（英，2015 成立，Cambridge，Ashwin Seshia） | MEMS **參數共振**（宣稱較傳統高 **10 倍**功率） | Companies House 編號 **09396640**，狀態 **Active**；但公司定位已改為「rotating equipment 的遠端狀態監測 + 無線感測器 + 機器學習」——**從賣採集器轉為賣監測服務**【V·摘要】 | 參數共振路線仍存活，但商業重心已離開採集器本身 |
| **Kinergizer**（荷，Delft，2012 成立） | 動能（馬達/齒輪箱/軌道） | 輸出 **0.5–2.5 mW**；**未曾募資**；**員工 5 人**【V·摘要：Tracxn】 | 規模極小 |
| **Piezo.com（原 Mide）**（美） | **壓電**（Volture v21bl / v25w、PPA 模組） | 產品仍在 Mouser / DigiKey 通路銷售；PPA 為封裝專利製程【V·摘要】 | **少數真正在賣壓電採集器的廠商，但規模與營收在 05 章與本輪皆查無** |
| **Wiliot**（以，2017 成立） | **RF 能量採集**（非壓電、非振動） | Series B **$30M**（Amazon / Avery Dennison / Samsung）、Series C **$200M**（SoftBank）；**Walmart 目標 2026 年底追蹤 9,000 萬個棧板**【V·多源】 | **「無電池」這個市場的最大贏家是 RF，不是振動，更不是壓電** |
| **uBeam / SonicEnergy**（美） | 超音波無線送電 | 募資 **$40M+**（a16z、Founders Fund、Marissa Mayer、Mark Cuban）；2018/09 創辦人 Meredith Perry 卸任 CEO；**2024/02/05 已 defunct**【V·多源：TechCrunch、Wikipedia】 | **超音波送電的消費級路線已明確死亡** |

### 2.2 結構健康監測（SHM）

- **Acellent Technologies（Stanford Fu-Kuo Chang 系）**：**SMART Layer®** 是把分散式壓電換能器嵌在薄載膜中、含整合佈線與接頭的貼層，可永久貼附於金屬或複材結構；**ScanGenie** 硬體支援對壓電陣列的「主動」聲–超音波資料擷取，**ScanGenie V 支援最多 128 個 PZT 感測器 + 8 個數位溫度感測器**；**ScanGenie Wireless Pro** 為機上版本，內建儲存與資料分析，可自主運作。**價格查無**【V·摘要：acellent.com、DTIC ADA442244】。丸紅（Marubeni）的品牌媒體有專文報導該公司【V·摘要】。
- **Metis Design Corporation**（波士頓 205 Portland St）：SHM 硬體/感測器/演算法；與 **AFWERX / AFRL/RVK** 合作，合約號 **FA945322CA031**（太空結構 SHM）；持有壓電損傷偵測專利 **US7469595B2**【V·多源】。
- **CVM / Structural Monitoring Systems（ASX:SMN）**：**非壓電**（比較式真空監測）。第一個 FAA 認證應用為 737-800 的 Wi-Fi 天線結構；Delta **71 架** 737 在役；後壓力隔框檢查 **24 h → 15 min**；FY2025 營收 **AU$28.1M**、淨利 **AU$173k**（近乎損益兩平）【V·多源】。**注意：SMN 集團營收包含非 CVM 的航太零件業務，CVM 單獨貢獻查無。**
- **管線**：Guided Ultrasonics **gPIMS®**——永久安裝的導波感測器 + 可攜式 Wavemaker® 或**永久安裝的電池供電自主現場控制單元**，配雲端 Monitoring Studio【V·摘要】。導波超音波檢測已獲准用於天然氣管線評估【V·摘要：Eddyfi】。
- **風機葉片**：查到的全是研究（NASA KSC / Purdue / Virginia Tech 的 9 m 葉片疲勞試驗、52 m 商用葉片疲勞試驗中同時用應變計 + 聲射 + 分散式加速度計 + 主動振動監測；Sandia OSTI 報告；2025 年 Springer JNDE 綜述）。**LM Wind Power / Bladena 的商用壓電 SHM 產品：查無**【V·摘要】。

### 2.3 輪胎內感測

- **TDK InWheelSense**：CES 2021 發表，模組置於**胎唇區**（tire/wheel 界面，官方稱最大發電區），用 TDK 壓電陶瓷**同時**擷取應變資料與採集能量，實現**無電池**的輪內感測、資料收集與傳輸；整合加速度計、溫度、陀螺儀；與 **Goodyear** 合作做邊緣 AI，輸出 traction / slip angle / turn angle / tread wear 等分析【V·多源：TDK 技術庫、EE Times、RFID Journal、TDK CES 2023 新聞稿】。**量產時程：查無。**
- **Bridgestone × Continental**：**2004 年**宣布共同開發胎內表面的**無電池**模組（壓力 + 溫度 + 可讀寫 ID tag），計畫 **2007 年**量產【V·摘要：Equipment World】。**其後續與是否真的量產：查無。這是一個「宣布二十年、無下文」的警訊。**
- **Pirelli × Bosch**：合作方向是**軟體式**的胎內感測解決方案與駕駛功能，非能量採集【V·摘要：Tire Review】。
- 學術側：胎內壓電採集有系統性文獻（Heliyon 2024 的模擬與量測、Microsystem Technologies 2025 的衝擊負載採集）與專利 **US8011237B2**（TPMS 用壓電採集模組）【V·摘要】。

---

## 3. 關鍵數字表

| 項目 | 數字 | 條件／備註 | 出處等級 |
|---|---|---|---|
| Perpetuum PMG7 輸出 | **≈3 mW @ 40–50 mg**，最高 **5 mW** | 電磁式；工作於 50/60 Hz 市電頻率 | 【V·多源】 |
| Perpetuum 部署規模 | **5,000+ 感測器 / 600+ 車輛 / 4 億 service-km**（自 2013） | Southeastern 148 列 618 節車廂；Kent 每日 180 萬資料點 | 【V·多源】 |
| Perpetuum 併購 | Hitachi Rail **2020-08 宣布**，**2021 年完成** | 金額查無 | 【V·多源】 |
| EnOcean 採集技術 | **電磁 / 光伏 / 熱電**，**零壓電** | ECO 200 / ECS 300 / ECT 310 | 【V·多源】 |
| EnOcean 營收 / 募資 | **≈$19.2M（2025）** / 累計 **$45.6M** | 商業資料庫估值，可信度中低；SPAC 上市案未完成 | 【V·摘要】 |
| ReVibe modelD | 最低 **0.05 g** 起作用，頻寬 **5 Hz** | 電磁式 | 【V·摘要】 |
| Kinergizer 輸出 | **0.5–2.5 mW** | 5 名員工、無外部募資 | 【V·摘要】 |
| 波傳播式 SHM 功率需求 | **數 mW – 數百 mW** | 視系統複雜度 | 【V·摘要】 |
| **單次傳輸週期最小能量** | **≈10 mJ** | 航空 SHM 能量採集回顧論文 | 【V·摘要】 |
| CR2032 總能量 | **≈2,430 J** | 225 mAh × 3.0 V × 3600 | 【推導】 |
| **一顆 CR2032 可供的 10 mJ 週期數** | **≈243,000 次** | 2430 / 0.01 | 【推導】 |
| **3 mW 採集器一天可供的 10 mJ 週期數** | **≈25,900 次** | 3e-3 × 86400 / 0.01 | 【推導】 |
| **採集 vs 電池的損益平衡點** | **≈77 µW 連續輸出 ＝ 每年 1 顆 CR2032** | 2430 J ÷ 3.15e7 s | 【推導】 |
| 商用壓電採集器功率密度 | **10–100 µW/cm³**（IoT 所需為 **1–10 mW/cm³**） | 差 **1–2 個數量級** | 【V·摘要，來源為 AI 生成報告，**低可信度**】 |
| 壓電高輸出阻抗造成的效率損失 | **40–60%** | 同上來源 | 【V·摘要，低可信度】 |
| 航空氣動聲學壓電膜採集 | **2 mW AC @ Mach 0.5**，淨 DC **≈1 mW** | 含自供電 SSHI + buck-boost，實測供電無電池 datalogger | 【V·摘要】 |
| 單一壓電元件自主感測+採集介面 | **1.02 µW** | 門檻式感測，JLPEA 11(2) 27 | 【V·摘要】 |
| WirelessHART 電池成本 | 電池包 **$150** + **1 h @ $100/hr**；專用電池 **>$250** | 500 儀表 → 3,000 顆 → **≈$750k**（含人工） | 【V·摘要】 |
| 電池佔全生命週期成本 | **≈初始投資（$1,500/節點）的 2 倍** | 同上 | 【V·摘要】 |
| CVM（非壓電）航空實績 | Delta **71 架** 737；檢查 **24 h → 15 min** | 唯一取得 FAA 認證的 SHM | 【V·多源】 |
| SMN（CVM 母公司）FY2025 | 營收 **AU$28.1M**、淨利 **AU$173k** | 含非 CVM 業務；近損益兩平 | 【V·摘要】 |
| Acellent ScanGenie V 通道 | **128 個 PZT + 8 個數位溫度感測器** | 價格查無 | 【V·摘要】 |
| Li-SOCl₂ 溫度上限 | 標準圓柱型 **+85 °C**；Tadiran TLH 系列 **+125 °C** | 自放電 <1%/年（Tadiran）、競品可達 3%/年 | 【V·多源】 |
| uBeam 結局 | 募資 **$40M+**，**2024-02-05 defunct** | 超音波無線送電消費路線 | 【V·多源】 |
| Wiliot / Walmart | **9,000 萬棧板**目標（2026 年底） | **RF** 採集，非壓電 | 【V·多源】 |
| 穿壁功率＋資料（最高記錄） | **50 W + 17.37 Mbps / 63.5 mm 實心鋼** | 壓電獨有能力 | 【V·轉引 02/16】 |
| 採集功率 vs 致動需求落差 | **3 個數量級**（µW–mW vs mW–W） | 「自供電致動」不成立 | 【V·轉引 02】 |

---

## 4. 「新能力型」應用機會

> **本節總判定：6 個機會裡，2 個是乾淨的新能力、2 個是半新能力、2 個應直接砍。與上一版相比，最大的修正是：4.5「工業節點免電池化」的判定從「應降權」進一步惡化為「應砍」，因為本輪查到的具名成本（$250/次）不足以支撐壓電溢價；而 4.3「複材內埋 SHM」的判定則從「半」下修，因為 FAA 的第一張門票已經被非壓電的 CVM 拿走。**

### 4.1 【真新能力 ★★★★★】密封金屬腔／不可開孔容器的內部監測

- **新能力**：不破壞密封與結構完整性，把功率與資料送進全金屬密閉容器，腔內壓電體同時是受電端、感測器與回傳端。實測 **50 W + 17.37 Mbps 穿越 63.5 mm 實心鋼**，穩壓後 **15.7 W DC / 27.7%**（40 mm 不鏽鋼）【V·轉引 02/16】。
- **為何以前做不到**：金屬是電磁的完美屏蔽，RF 無法穿透；有線必須鑽孔，在核能圍阻體、乾儲罐、潛艇殼、壓力容器上鑽孔等於摧毀認證基礎；內置電池壽命不足且不可更換。16 章記載：**乾式貯存桶目前根本沒有任何內部直接量測手段**【V·轉引 16】。
- **是否真非替代**：**是（強）**。原本零，現在有。
- **誰在做**：RPI（Lawry/Wilt/Scarton）、Penn State、PNNL/Sandia、美國陸軍研究實驗室（W911NF2220007）、Stevens Institute【V·轉引 16】。
- **TRL**：4–6（核能側較高，商用側 0）。
- **市場訊號**：軍方與能源部持續資金、專利佈局為正；**查無任何商用產品或公司**為強負。
- **技術障礙**：耦合劑長期可靠度（乾涸、腐蝕、高溫脫氣）、對準敏感度、壁內多重反射造成的通道漂移與 ISI、**認證路徑成本可能遠高於研發成本**。
- **本輪新增的警示**：uBeam（超音波無線送電）募資 $40M+ 後於 2024 年徹底消亡【V·多源】。**雖然 uBeam 是「穿空氣」而穿壁是「穿固體」（聲阻抗匹配好得多，物理上完全不同），但投資人對「超音波送電」這個字眼的耐心已經被消耗殆盡——募資敘事上這是實質障礙。**

### 4.2 【真新能力 ★★★★☆】超過電池溫度上限的環境中的無電池監測

- **新能力**：在鋰電池物理上活不下來的環境（渦輪熱段、核島、井下 >200 °C、高離心力旋轉件）做長期監測，壓電體同時採集局部機械能與充當超音波/導波換能器。
- **為何以前做不到（本輪取得具名門檻）**：Li-SOCl₂ 標準圓柱型電池上限 **+85 °C**，高溫特化型（Tadiran TLH）到 **+125 °C**【V·多源：Tadiran】。**因此本機會的溫度門檻可以被精確定義為「>125 °C」——這比上一版的模糊估計（125–150 °C）更硬。** 高溫壓電材料（LiNbO₃、AlN、鑭鎵矽酸鹽）在 16 章脈絡下已驗證可跨越 **0.5 K – 544 K（≈271 °C）**【V·轉引 16】。
- **是否真非替代**：**是（強）**，但限縮條件嚴格：**只有 >125 °C 才成立**，低於此門檻立刻退化為 4.5 的替代賽局。
- **誰在做**：**查無具名公司**（SKF 的軸承滾動體壓電供電感測本輪未能查證，上一版已標為低可信度來源）。
- **TRL**：3–4（材料側有實證，系統側查無）。
- **市場訊號**：**弱**。**注意：高溫下先死的通常不是壓電體，而是電子元件——SiC/SOI 電子在 >200 °C 的成本與供應鏈是本機會的真正瓶頸，不是壓電材料。**
- **技術障礙**：高溫壓電材料的 d 係數遠低於 PZT（採能量掉一個數量級以上）；封裝與引線熱循環疲勞；高溫電子元件。

### 4.3 【半新能力 ★★★☆☆】複材內埋、製造後永不可及的長壽命結構感測層

- **新能力**：壓電陣列在複材鋪層階段埋入層間，出廠後無法接線也無法換電池，卻要在 25–30 年服役期內既發射導波（主動）又接收（被動）。
- **為何以前做不到**：外部感測器物理上放不進層間；有線接頭在複材內是應力集中源與進水路徑。
- **是否真非替代**：**半**。感測功能本身是替代（取代激振器＋加速度計），是「可及性」約束把它推向新能力。
- **誰在做**：Acellent（SMART Layer + ScanGenie，**128 通道 + 8 溫度感測器**）、Metis Design（AFWERX 合約 FA945322CA031）、Airbus（A350 + MSN001 A340 飛行驗證機，SMART Layer 撞擊偵測飛測中）【V·多源】。
- **TRL**：**5–6**（航空側仍在飛測與 qualification 前期；Bockenheimer 明確說 local SHM「ready for qualification」而非 certified）【V·摘要】。
- **市場訊號（本輪最重要的修正）**：**負面。第一張 FAA 門票被非壓電的 CVM 拿走了**——Delta 71 架 737 在役、SB 737-57-1309 已修訂允許 CVM 作替代檢查、KC-46A 也採用【V·多源】。**這證明「認證機關願意接受 SHM 抵換人工檢查」（好消息，市場存在），但也證明「認證機關偏好機理簡單、失效模式明確的技術」（壞消息，壓電導波的訊號詮釋複雜度正是它的劣勢）。**
- **技術障礙**：溫度補償（已有研究指出溫度對阻抗簽章的影響足以掩蓋損傷訊號【V·轉引 02】）；黏著/內埋界面老化；**以及最致命的：導波法要證明「訊號變化 = 損傷」而非「膠層老化/溫度漂移」，這個舉證責任正是 CVM 用一個簡單的氣壓洩漏機制繞過去的。**

### 4.4 【半新能力 ★★★☆☆】旋轉件與密封件上的「阻尼＋感測＋採集」三用結構貼片

- **新能力**：同一片壓電貼在葉片、旋翼、泵浦或軸承座上，平時以 shunt 電路做被動/半主動阻尼（SSD 家族），同時把振動能量收進儲能，累積夠了就發射一次導波掃描並回傳。**阻尼與採集不是互斥而是同一物理過程的兩個出口——這是壓電獨有的。**
- **為何以前做不到**：傳統上阻尼器、加速度計、能量源是三個零件三套線路；旋轉件上布線需滑環或無線送電。
- **是否真非替代**：**半（偏替代）**。02 章對「時間多工兩用」的判定是「否／偏替代（低—中）」，除非場景限定在布線不可能的旋轉件、密封件、拋棄式標籤【V·轉引 02】。
- **本輪新增的正面證據**：航空氣動聲學壓電膜採集器已做到 **2 mW AC / 1 mW 淨 DC @ Mach 0.5**，並在代表真實飛行的條件下實測供電一個無電池 wireless datalogger【V·摘要】。這是「壓電採集 + 自供電 SSHI + 實際供電負載」的完整閉環實證。**但注意它採的是氣動噪聲而不是結構振動。**
- **誰在做**：SSD/SSHI 學界；產業側最接近的是 **8power**（參數共振 + 旋轉設備狀態監測），但該公司已把重心從賣採集器移到賣監測服務【V·摘要】。
- **TRL**：3–5。
- **技術障礙**：**佔空比互斥**——21 章：「佔空比一分，兩邊都變弱；切換暫態需等機械暫態衰減（Q=1000 ⇒ 需 ~Q 個週期）」【V·轉引 21】。**高 Q 是儲能與阻尼想要的，卻是模式切換的敵人。客戶必須正面回答這個矛盾。**

### 4.5 【應砍 ★☆☆☆☆】一般工業無線感測節點（WirelessHART/ISA100/LPWAN）的免電池化

- **判定：否，純替代，且本輪查到的具名數字證明它打不過。**
- 具名成本：電池包 **$150** + **1 小時人工 @$100/hr** ≈ **$250/次**；即使是「電池全生命週期成本 = 初始投資 2 倍」的說法，基礎也是 $1,500 的節點單價【V·摘要】。**一個壓電採集模組要在 $250/次、且更換週期以年計的預算裡取勝，幾乎不可能。**
- 更致命的是**採集端的技術選擇已定**：Perpetuum（電磁）、EnOcean（電磁/光伏/熱電）、ReVibe（電磁）都不是壓電；商用壓電採集器功率密度 **10–100 µW/cm³** 距離 IoT 所需的 **1–10 mW/cm³** 差 1–2 個數量級【V·摘要，低可信度來源，但方向與其他證據一致】。
- **唯一可能翻身的條件**：位置屬於「進去一次要停機/動火/進侷限空間」的高派工成本點，且壽命需求 >15 年。**這是很小的子集合，且該子集合裡電磁式採集器同樣適用。**
- **建議：不要以此為主打敘事。**

### 4.6 【應砍 ★☆☆☆☆】智慧鞋／穿戴／人體動能

- **判定：否，純替代且已有商業失敗紀錄。** P-SSHI 鞋墊採集 **3.6 mW @ 1 Hz、83.02% 效率**【V·轉引 02】已是該領域相當好的成績，仍遠低於任何有意義的穿戴需求。**HEAD Intelligence 網球拍**（自供電壓電阻尼，專利 US6974397B2，宣稱衰減 50% vs 一般 20%）**已停產**【V·轉引 02/08/09】。
- **建議：直接排除。**

### 4.7 【觀察名單 ★★★☆☆】輪胎胎唇區的壓電採集 + 感測

- **新能力**：胎內是「離心力 + 溫度 + 不可換電池 + 需終身監測」的四重約束，且 TPMS 已是法規強制項目。TDK 用**同一片壓電陶瓷**同時做應變感測與能量採集，位置選在胎唇區（發電量最大處）【V·多源】。
- **是否真非替代**：**半到是**。現行 TPMS 用電池，所以功能是替代；但**輪胎壽命內電池不可更換**、且要做到 tread wear / slip angle 這類需要高頻連續量測的新功能時，電池預算會先崩潰——這一段是新能力。
- **為什麼放觀察名單而不是主推**：TDK 於 2021 年發表，**至今查無量產車型**；Bridgestone × Continental 早在 2004 年就宣布過無電池胎內模組並預告 2007 量產，**同樣查無下文**【V·摘要】。**這個口袋已經被喊了二十年。**
- **對客戶的意義**：如果要做，**應該是去當 TDK 或輪胎廠的材料/元件供應商，而不是自己做系統**。

---

## 5. 反面證據、失敗案例與物理上限

### 5.1 【最強反證】三個成功案例，零個用壓電

這是本輪最重要的發現，因為它是**經驗證據**而非物理推論：

| 成功案例 | 領域 | 採集技術 | 壓電？ |
|---|---|---|---|
| Perpetuum（600+ 車輛、5,000+ 感測器） | 鐵路狀態監測 | **電磁式** | 否 |
| EnOcean（樓宇自動化，25 年） | 無線開關/感測 | **電磁 + 光伏 + 熱電** | 否 |
| Wiliot（Walmart 9,000 萬棧板） | 供應鏈標籤 | **RF 採集** | 否 |
| CVM / SMN（Delta 71 架 737，唯一 FAA 認證 SHM） | 航空結構檢測 | **氣壓（真空）** | 否 |

**四個賽道，四個贏家，沒有一個是壓電。** 這不是巧合：
- 在**巨觀體積、低頻（1–200 Hz）**，電磁式輸出功率 ∝ (B·A·dz/dt)²/R，磁通變化率可以做得很大；壓電式每週期可轉換能量受材料常數與降伏應力封頂，低頻共振又需大質量長懸臂，**體積效率不如電磁**。
- 在 **MEMS 尺度與 kHz 以上**，線圈與磁鐵微縮極差（B·A 隨 L² 掉），壓電才佔優——**但工業振動不在 kHz。**
- 在**沒有機械振動**的場景（棧板、開關面板），RF 與光伏直接勝出。

**對客戶的直接意涵：如果目標是「從機械振動採電」，壓電本身就是錯的技術選擇。壓電的優勢從來不是採集效率，而是「同一顆元件還能反過來當致動器與超音波發射器」。客戶的兩用命題若要成立，價值必須 100% 押在主動端，採集端只能當附加價值。**

### 5.2 能量從來不是瓶頸——這是最反直覺、也最該修正的一條

用本輪查到的具名數字重算：
- 單次 SHM 傳輸週期 **≈10 mJ**【V·摘要】。
- CR2032 **≈2,430 J** ⇒ **≈243,000 次**【推導】。以每日一掃計 = **665 年**；即使乘上 10 倍的系統開銷仍有 66 年。
- Perpetuum 級 3 mW 採集器 ⇒ **每天 ≈25,900 次**【推導】。

**兩邊都遠遠夠用。** 所以「自供電 SHM」的賣點**不能是「能量夠不夠」**，只能是「不用進去換電池」。而「進去換電池」的具名成本是 **$250/次**【V·摘要】。**這就是這個領域二十年叫好不叫座的完整解釋：問題從來不是能量學，是採購經濟學。**

損益平衡點的乾淨算法：**採集器連續輸出 77 µW ＝ 每年省一顆 CR2032**【推導：2430 J ÷ 3.15e7 s】。要省下 $250/次 的派工，必須讓更換間隔短到每年一次以上，或讓進場成本遠高於 $250。**大多數工業節點兩者都不成立。**

### 5.3 認證機關偏好「機理簡單」而非「資訊豐富」

CVM 的原理是：在裂紋可能發生的路徑上鋪一組交錯的真空與大氣通道，裂紋一旦穿過就造成漏氣，量到壓差就是有裂紋。**二值、機理透明、無需 baseline、無需溫度補償。** 它拿到了 FAA 認證，並讓 Delta 的 737 後壓力隔框檢查從 **24 小時降到 15 分鐘**【V·多源】。

壓電導波法能提供的資訊多得多（位置、大小、類型），但代價是**必須靠 baseline 比對與統計判別**，而 baseline 會被溫度、膠層老化、負載狀態污染。**認證的舉證責任落在「證明誤報率」上，而不是「證明資訊量」上——這正是壓電導波 SHM 二十年沒能上機的核心原因，本輪的 CVM 證據把這個推論從假設升級為事實。**

### 5.4 佔空比互斥與高 Q 的自我矛盾

「同一顆元件時間分割兩用」的硬性代價：佔空比一分為二，兩邊都變弱；切換時必須等機械暫態衰減，**Q = 1000 意味著需等約 1000 個週期**【V·轉引 21】。高 Q 是儲能與阻尼效能想要的，卻直接惡化模式切換反應時間。**這是共振器的本質，電路繞不過去。**

### 5.5 自供電致動的數量級幻覺

採集 µW–mW vs 致動 mW–W，差 **3 個數量級**【V·轉引 02】。self-powered SSDI 成立僅因為它驅動一顆開關、不注入能量。**任何宣稱「採集來的能量可以驅動致動」的提案都應被要求出示功率預算表。**

### 5.6 「宣布二十年、無下文」的模式

- **Bridgestone × Continental 無電池胎內模組**：2004 年宣布，預告 2007 量產【V·摘要】，其後查無。
- **TDK InWheelSense**：2021 年 CES 發表，2026 年查無量產。
- **穿金屬壁功率傳輸**：技術存在近 30 年，**搜尋結果 100% 是論文與專利，查無任何商用產品或公司**【V·轉引 16】。
- **EnOcean ECO 200**：官網已標「not recommended for new designs」【V】——連該領域最成熟的機械採集模組都在退場。

### 5.7 這個賽道的資本市場紀錄很難看

- **uBeam**：募資 **$40M+**（a16z、Founders Fund 等頂級機構），2018 年創辦人卸任，改名 SonicEnergy，**2024-02-05 defunct**【V·多源】。
- **EnOcean**：25 年、$45.6M 募資，2025 年營收僅 **$19.2M**，SPAC 上市案未完成【V·摘要，商業資料庫，可信度中低】。
- **Kinergizer**：14 年、**零募資、5 名員工**【V·摘要】。
- **8power**：Cambridge 頂尖團隊、參數共振有 Nature Scientific Reports 論文背書，**但已把重心從採集器轉為監測服務**【V·摘要】。
- **SMN（CVM）**：FY2025 淨利 **AU$173k**——即使是唯一拿到 FAA 認證的贏家，也只是勉強損益兩平【V·摘要】。

**唯一的乾淨退出是 Perpetuum 被 Hitachi Rail 併購（2020 宣布 / 2021 完成，金額查無）——而它用的是電磁式。**

### 5.8 為什麼 Perpetuum 成功而別人失敗（本輪的結構性歸納）

從查到的事實可以歸納出四個共同條件，這是本章對客戶最有操作價值的部分：

1. **振動源是穩定、可預測、幾乎永不停止的**——列車轉向架在營運中持續振動；相對地工業泵浦會停機、橋樑振動間歇、人體步行低頻隨機。
2. **布線在物理上不可能**——轉向架是簧下、旋轉、暴露於道碴衝擊的部位，拉線到車體幾乎不可行；這使「免佈線」而不是「免電池」成為真正的價值。
3. **賣的是資料與維修決策，不是元件**——Perpetuum 的營收模型是「感測器 + 雲端演算法 + 遠端網頁存取」，Southeastern 買的是預測性維護結果【V·摘要：IRJ、perpetuum.com】。**這與客戶「賣壓電元件」的模式截然不同。**
4. **有一個明確、昂貴、可量化的失效模式**（軸承與輪面磨損 → 臨時限速、脫軌風險），使 ROI 可以被算出來。

**反過來說，客戶若複製這個模式，需要的是「找到一個具備上述四條件、且電磁式做不到而壓電做得到」的場景。本輪查到的唯一符合者是：>125 °C 的環境，以及金屬密閉腔。**

---

## 6. 未解問題

1. **Acellent SMART Layer / ScanGenie 的實際售價與部署架次是多少？** 本輪多次搜尋均無報價。若一套 128 通道系統的價格是六位數美金，則整個「內埋 SHM」機會的市場規模需要重估。
2. **Airbus 的 local SHM 何時真正取得 qualification？有沒有任何壓電導波系統已經拿到 FAA/EASA 的維修計畫抵換 credit？** 本輪只查到「ready for qualification」與飛行測試，沒有查到任何已認證的壓電導波系統。**這是 §4.3 成敗的唯一決定因素。**
3. **TDK InWheelSense 為什麼發表五年沒有量產？** 是壓電輸出不足、是胎唇區的可靠度問題、還是輪胎廠不願承擔額外 BOM？答案直接決定 §4.7 是否值得投入。
4. **SKF 的「壓電供電之軸承滾動體感測」是否真實存在？** 本輪額度用盡前未能查證（上一版來源被標為 AI 生成、低可信度）。若為真，這是本領域最強的產業訊號，因為滾動體內部是絕對不可布線、不可換電池的位置。
5. **gPIMS 的電池壽命與換電週期？** 這是「產業已經接受壓電 + 電池分工」這條論點的關鍵量化錨點。
6. **>125 °C 的環境裡，先死的是電池還是電子元件？** 若 SiC/SOI 電子的成本讓整個節點無法商業化，§4.2 的「新能力」就只是紙上的。

---

## 7. 來源清單

> 1–43 為本輪 WebSearch 實際回傳的結果；44–49 標【轉引】者逐字取自本專案其他章節。

### 7.1 能量採集玩家

1. **Hitachi Rail acquires Perpetuum** — https://www.bindt.org/News/June-2021/hitachi-rail-acquires-perpetuum/ — 收購於 2021 年完成的確認。
2. **Hitachi Rail boosts maintenance offer as it completes acquisition of Perpetuum** — https://www.mynewsdesk.com/uk/hitachi-rail-global/pressreleases/hitachi-rail-boosts-maintenance-offer-as-it-completes-acquisition-of-digital-tech-firm-perpetuum-3086892 — Hitachi Rail 官方完成收購新聞稿。
3. **Hitachi Rail to acquire Perpetuum（Hitachi Global，2020-08-11）** — https://www.hitachi.com/en/press/articles/2020/08/0811/ — 收購宣布時點。
4. **University of Southampton REF3 Impact Case Study** — https://results2021.ref.ac.uk/impact/541faf1b-8612-4135-bb91-a53e66b5ea5f/pdf — Perpetuum 2004 年成立、**electromagnetic** 微發電機、部署規模的學術影響力報告。
5. **Perpetuum Releases Vibration Energy Harvesting Microgenerator（eepower）** — https://eepower.com/new-industry-products/perpetuum-releases-vibration-energy-harvesting-microgenerator/ — PMG7 規格。
6. **Energy Harvesting: Practical Reality for Wireless Sensing（ISA blog）** — https://blog.isa.org/energy-harvesting-practical-reality-wireless-sensing — **3 mW @ 40–50 mg**、50/60 Hz 的數字來源。
7. **Perpetuum wins contract to supply Southeastern Railways ... 148 trains（Global Railway Review）** — https://www.globalrailwayreview.com/news/18356/perpetuum-wins-contract-to-supply-southeastern-railways-with-energy-harvester-powered-wireless-sensor-systems-for-148-trains/ — 148 列 / 618 節車廂。
8. **Harvesting vibrations benefits maintenance（International Railway Journal）** — https://www.railjournal.com/in_depth/harvesting-vibrations-benefits-maintenance/ — 112 列 class 375 部署、Kent 每日 180 萬資料點、商業模式描述。
9. **Perpetuum Rail Applications** — https://perpetuum.com/rail-applications/ — 5,000+ 感測器 / 600+ 車輛 / 4 億 service-km。
10. **Eversholt Rail Adopts Perpetuum's Self-Powered Rail Condition Monitoring for the Networker Class 465（Mass Transit）** — https://www.masstransitmag.com/rail/press-release/12219979/perpetuum-eversholt-rail-adopts-perpetuums-self-powered-rail-condition-monitoring-for-the-networker-class-465 — 第二個具名客戶。
11. **Train Wheel Bearing Monitoring from Perpetuum（Fierce Electronics）** — https://www.fierceelectronics.com/components/train-wheel-bearing-monitoring-from-perpetuum — 產品定位。
12. **EnOcean — Energy Harvesting** — https://www.enocean.com/en/technology/energy-harvesting/ — **官方列出電磁/光伏/熱電三種，無壓電**。本章 §1.2 的核心依據。
13. **EnOcean ECO 200 產品頁（標註 Not recommended for new designs）** — https://www.enocean.com/en/product/eco-200/ — 電動式（非壓電）採集器且已進入退場。
14. **ECO 200 Data Sheet（2021-06）** — https://www.enocean.com/wp-content/uploads/downloads-produkte/en/products/enocean_modules_928mhz/eco-200/data-sheet-pdf/ECO_200_Data_Sheet_June2021_02.pdf — 規格書。
15. **PTM 200 Data Sheet（DigiKey 鏡像）** — https://media.digikey.com/PDF/Data%20Sheets/Enocean%20PDFs/PTM200.pdf — 開關模組採用 electro-dynamic 發電機。
16. **EnOcean（Wikipedia）** — https://en.wikipedia.org/wiki/EnOcean — 公司沿革。
17. **EnOcean Financials（Memoori）** — https://memoori.com/enocean-financials-energy-harvesting-2025-outlook/ — 財務討論。
18. **EnOcean（PitchBook）** — https://pitchbook.com/profiles/company/12874-42 — 募資與 SPAC 案。
19. **EnOcean（Growjo）** — https://growjo.com/company/EnOcean — $19.2M 營收估值（**商業資料庫估算，可信度中低**）。
20. **ReVibe VS1 – Energy-Harvesting Vibration Sensor** — https://revibeenergy.com/products/vs1-vibration-sensor/ — 專利電磁式發電機。
21. **ReVibe modelD Evaluation Kit（DigiKey）** — https://www.digikey.com/en/product-highlight/r/revibe-energy/modeld-evaluation-kit — 0.05 g、5 Hz 頻寬。
22. **8power — Remote Condition Monitoring for Rotating Equipment** — https://8power.com/ — 從採集器轉向監測服務的定位改變。
23. **8POWER LIMITED（Companies House 09396640）** — https://find-and-update.company-information.service.gov.uk/company/09396640 — 公司狀態 Active。
24. **Forget batteries, Cambridge start-up 8Power is harvesting energy from vibrations（Cambridge Independent）** — https://www.cambridgeindependent.co.uk/business/forget-batteries-cambridge-start-up-8power-is-harvesting-energy-from-vibrations-9051233/ — 2015 年成立、Ashwin Seshia、參數共振 10x 宣稱。
25. **Twenty-Eight Orders of Parametric Resonance ... （Nature Scientific Reports 6:30167）** — https://www.nature.com/articles/srep30167 — 參數共振採集的學術基礎。
26. **Kinergizer** — https://kinergizer.com/ — 動能採集產品。
27. **Kinergizer（Tracxn）** — https://tracxn.com/d/companies/kinergizer/__teOr3XmZnX4PzGXeG-iLtoBp0-k3CI690wAaFf9tEXQ — 5 名員工、未募資、0.5–2.5 mW。
28. **Piezoelectric Energy Harvesters（PIEZO.COM）** — https://piezo.com/collections/piezoelectric-energy-harvesters — 仍在販售的壓電採集器。
29. **Mide PPA Piezoelectric Energy Harvesting Modules（Mouser）** — https://www.mouser.com/en/new/mide-technology/mide-ppa-piezoelectric-products — PPA 封裝製程。

### 7.2 結構健康監測

30. **Acellent Technologies — Hardware（ScanGenie 系列）** — https://www.acellent.com/products/hardware — ScanGenie V 128 PZT + 8 溫度感測器、Wireless Pro 自主機上版本。
31. **Acellent — SMART Layer® Sensors** — https://www.acellent.com/products/smart-layer-sensors — 感測貼層產品說明。
32. **SMART Layer and SMART Suitcase for SHM Applications（DTIC ADA442244）** — https://apps.dtic.mil/sti/tr/pdf/ADA442244.pdf — 技術原始報告。
33. **Acellent（Marubeni Scope）** — https://www.marubeni.com/en/brand_media/scope/acellent/ — 產業側報導。
34. **Metis Design Corporation — Structural Health Monitoring** — https://www.metisdesign.com/structural-health-monitoring-company.html — 公司定位。
35. **US7469595B2 — Piezoelectric damage detection device** — https://patents.google.com/patent/US7469595B2/en — Metis Design 專利。
36. **SHM of Space Structures Using Elastic Waves and Integrated Piezoelectric Sensors（Springer）** — https://link.springer.com/chapter/10.1007/978-3-031-61421-7_51 — AFWERX/AFRL 合約 FA945322CA031。
37. **Structural health monitoring: NDT-integrated aerostructures（CompositesWorld）** — https://www.compositesworld.com/articles/structural-health-monitoring-ndt-integrated-aerostructures-enter-service — Airbus Bockenheimer 的 local vs global SHM 說法、A350/A340 飛行驗證機、SMART Layer 飛測。**§4.3 的主要依據。**
38. **SMS Completes Installation of CVM Sensor Kits on Delta Aircraft（AviationPros）** — https://www.aviationpros.com/aircraft-maintenance-technology/mros-repair-shops/inspection-testing/press-release/53057343/structural-monitoring-systems-sms-completes-installation-of-cvm-sensor-kits-on-delta-aircraft — FAA Statement of Conformity、STC 路徑。
39. **Structural Monitoring Systems (ASX:SMN) advancing CVM in aircraft maintenance（marketopen）** — https://www.marketopen.com.au/structural-monitoring-systems-asxsmn-advancing-comparative-vacuum-monitoring-in-aircraft-maintenance/ — **Delta 71 架 737、24 h → 15 min**。
40. **Testing for Certification of CVM Sensors on the 737NG Aft Pressure Bulkhead（ndt.net, IWSHM 2025）** — https://www.ndt.net/article/iwshm2025/papers/IWSHM_133.pdf — 取證測試細節。
41. **Comparative Vacuum Monitoring Solutions to Advance U.S. Air Force KC-46A CBM+（MDPI Aerospace 10(7) 587）** — https://doi.org/10.3390/aerospace10070587 — CVM 為 FAA 認證的 CBM+ 技術。
42. **Cost-Effectiveness of Structural Health Monitoring in Aviation: A Literature Review（Sensors 25(19) 6146）** — https://pmc.ncbi.nlm.nih.gov/articles/PMC12526806/ — SHM 經濟性綜述。
43. **Structural Health Sensors Come Of Age（Aviation Week）** — https://aviationweek.com/mro/emerging-technologies/structural-health-sensors-come-age — 產業側綜述。
44. **CVM™ — Airframe Crack Detection Compliance** — https://cvm.aero/ — CVM 官方。
45. **Structural Monitoring Systems (ASX:SMN)（Simply Wall St）** — https://simplywall.st/stocks/au/tech/asx-smn/structural-monitoring-systems-shares — FY2025 營收 AU$28.1M、淨利 AU$173k。
46. **SMS signs its first commercial deal with Delta Air Lines** — https://www.smsystems.com.au/structural-monitoring-systems-signs-its-first-commercial-deal-with-delta-air-lines/ — 首張商業合約。
47. **ARP6461A: Guidelines for Implementation of SHM on Fixed Wing Aircraft（SAE, 2021-08）** — https://saemobilus.sae.org/standards/arp6461a-guidelines-implementation-structural-health-monitoring-fixed-wing-aircraft — 現行版指引。
48. **ARP6461（SAE, 2013-09 原始版）** — https://saemobilus.sae.org/standards/arp6461-guidelines-implementation-structural-health-monitoring-fixed-wing-aircraft — 原始版。
49. **Energy Harvesting Technologies for SHM of Airplane Components — A Review（Sensors, PMC7700503）** — https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7700503/ — **波傳播 SHM 數 mW–數百 mW、單次傳輸週期最小能量 ≈10 mJ**。§5.2 的核心依據。
50. **Energy Harvesting for Structural Health Monitoring Sensor Networks（Park et al., UCSD）** — http://varys.ucsd.edu/media/papers/park2008energy.pdf — SHM 採集的經典回顧。
51. **Piezoelectric Transducer-Based SHM for Aircraft Applications（Sensors, PMC6387086）** — https://pmc.ncbi.nlm.nih.gov/articles/PMC6387086/ — 壓電導波 SHM 綜述。
52. **Lamb waves-based technologies for SHM of composite structures for aircraft applications（Taylor & Francis）** — https://www.tandfonline.com/doi/full/10.1080/26889277.2022.2094839 — 導波 SHM 現況。
53. **gPIMS® Monitoring System（Guided Ultrasonics Limited）** — https://www.guided-ultrasonics.com/monitoring/gpims-system/ — **永久安裝壓電導波感測器 + 電池供電自主控制單元**。§1.8 的依據。
54. **gPIMS sensor installation checklist（GUL）** — https://www.guided-ultrasonics.com/gpims/ — 安裝實務。
55. **Guided Wave Ultrasonic Testing Approved for Gas Pipeline Assessments（Eddyfi）** — https://blog.eddyfi.com/en/guided-wave-ultrasonic-testing-approved-for-gas-pipeline-assessments — 導波檢測的法規接受度。
56. **Smart SHM system for on-board localization of defects in pipes using torsional ultrasonic guided waves（arXiv 2403.11110）** — https://arxiv.org/pdf/2403.11110 — 管線導波 SHM 學術現況。
57. **A State-of-the-Art Review of SHM Techniques for Wind Turbine Blades（J. Nondestruct. Eval., 2025）** — https://link.springer.com/article/10.1007/s10921-025-01296-5 — 風機葉片 SHM 綜述。
58. **Inspection and monitoring of wind turbine blade embedded structures（Sandia / OSTI）** — https://www.osti.gov/servlets/purl/1122363 — 9 m 葉片疲勞試驗中的 AE 與壓電主動感測。

### 7.3 自供電 / 兩用實證

59. **Coupling Supercapacitors and Aeroacoustic Energy Harvesting for Autonomous Wireless Sensing in Aeronautics（Energy Harvesting and Systems, 2016）** — https://www.degruyterbrill.com/document/doi/10.1515/ehs-2016-0003/html — **壓電膜 2 mW AC @ Mach 0.5、淨 1 mW DC、自供電 SSHI、實測供電無電池 datalogger**。§4.4 的正面證據。
60. **A 1.02 µW Autarkic Threshold-Based Sensing and Energy Harvesting Interface Using a Single Piezoelectric Element（JLPEA 11(2) 27）** — https://doi.org/10.3390/jlpea11020027 — **單一壓電元件同時感測與採集**的低功耗介面實證。
61. **Piezoelectric Sensors as Energy Harvesters for Ultra Low-Power IoT Applications（Sensors 24(8) 2587）** — https://doi.org/10.3390/s24082587 — 感測/採集雙功能綜述。
62. **US12101041 — Self-powered sensor nodes for structural health monitoring** — https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/12101041 — 自供電 SHM 節點專利。
63. **Piezoelectric Energy Harvesting: A Systematic Review of Reviews（Actuators 10(12) 312）** — https://www.mdpi.com/2076-0825/10/12/312 — 綜述之綜述。
64. **同上，arXiv 版** — https://arxiv.org/pdf/2101.09312
65. **Electromagnetic Vibrational Energy Harvesters: A Review（PMC9331882）** — https://pmc.ncbi.nlm.nih.gov/articles/PMC9331882/ — 電磁式採集的物理與性能基準。
66. **Triboelectric Nanogenerator versus Piezoelectric Generator at Low Frequency (<4 Hz): A Quantitative Comparison（PMC7334414）** — https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7334414/ — 低頻下壓電的劣勢量化。
67. **Piezoelectricity For Energy Harvesting: Power Density, Impedance Matching And Lifetime（PatSnap Eureka）** — https://eureka.patsnap.com/report-piezoelectricity-for-energy-harvesting-power-density-impedance-matching-and-lifetime — 10–100 µW/cm³ vs 1–10 mW/cm³、40–60% 阻抗失配損失。**⚠ AI 生成內容，可信度低，僅作方向參考。**

### 7.4 輪胎 / 工業節點 / 反面案例

68. **InWheelSense™: Where the rubber meets the road（TDK 技術庫）** — https://product.tdk.com/en/techlibrary/developing/inwheelsense/index.html — 胎唇區壓電採集 + 感測的官方說明。
69. **TDK Harvests Energy from Vehicle Wheels（EE Times）** — https://www.eetimes.com/tdk-harvests-energy-from-vehicle-wheels/ — CES 2021 發表、bead area 為最大發電區。
70. **Goodyear, TDK Partnership Drives IoT Tire Intelligence（RFID Journal）** — https://www.rfidjournal.com/news/goodyear-tdk-partnership-drives-iot-tire-intelligence/202273/ — Goodyear 合作、邊緣 AI。
71. **TDK spotlights innovations at CES 2023（TDK 新聞稿）** — https://www.tdk.com/en/news_center/press/20221213_01.html — 產品線持續展出。
72. **Bridgestone, Continental to develop tire pressure monitoring systems（Equipment World）** — https://www.equipmentworld.com/workforce/safety/article/14941998/bridgestone-continental-to-develop-tire-pressure-monitoring-systems — **2004 年宣布無電池胎內模組、預告 2007 量產**。§5.6 的依據。
73. **Pirelli, Bosch partner on software-based in-tire sensor development（Tire Review）** — https://www.tirereview.com/pirelli-bosch-in-tire-sensors/ — Pirelli 路線是軟體而非採集。
74. **Simulated and measured piezoelectric energy harvesting of dynamic load in tires（Heliyon, 2024）** — https://www.sciencedirect.com/science/article/pii/S2405844024050746 — 胎內壓電採集的實測。
75. **US8011237B2 — Piezoelectric module for energy harvesting, such as in a TPMS** — https://patents.google.com/patent/US8011237B2/en — 胎內壓電採集專利。
76. **Taking Batteries out of the Cost Equation for WirelessHART Networks（New Equipment Digest）** — https://www.newequipment.com/plant-operations/article/22059763/taking-batteries-out-of-the-cost-equation-for-wirelesshart-networks — **電池包 $150 + 1 h @ $100/hr、500 儀表 3,000 顆電池 ≈ $750k**。§1.7 / §4.5 的具名依據。
77. **同上（CPECN 版）** — https://www.cpecn.com/features/taking-batteries-out-of-the-cost-equation-for-wirelesshart-networks/
78. **Why You Need Wireless in Your Plant: The $20,000 Difference（Relevant Solutions）** — https://relevantsolutions.com/relevant-blog/why-you-need-wireless-in-your-plant-the-20000-difference/ — 有線 vs 無線的安裝成本對照（廠商部落格，可信度中）。
79. **uBeam wireless power's CEO Meredith Perry steps aside amidst B2B pivot（TechCrunch, 2018-09-20）** — https://techcrunch.com/2018/09/20/ubeam/ — $40M+ 募資、技術質疑。
80. **SonicEnergy（Wikipedia）** — https://en.wikipedia.org/wiki/SonicEnergy — **2024-02-05 defunct**。
81. **Wiliot（官網）** — https://www.wiliot.com/ — RF 採集的無電池 BLE 標籤。
82. **Walmart to deploy 90 million Bluetooth passive IoT nodes（Medium / IoT EXPO）** — https://medium.com/@ioteventinchina/industry-trend-walmart-to-deploy-90-million-bluetooth-passive-iot-nodes-is-rfid-facing-a-c136fa1a3593 — 9,000 萬棧板規模（**二手媒體，可信度中**）。
83. **How battery-free Bluetooth sensors are helping to enable the demand chain（Bluetooth SIG）** — https://www.bluetooth.com/blog/how-battery-free-bluetooth-sensors-are-helping-to-enable-the-demand-chain/ — 官方組織側佐證。
84. **High Temperature — Tadiran Batteries** — https://tadiranbat.com/applications/high-temperature/ — **TLH 系列 3.6 V @ 125 °C**。§4.2 溫度門檻依據。
85. **Tadiran LTC-Batteries 技術手冊** — https://www.tme.eu/Document/66a4af5ebe2c06371f1b7b9951ee318d/TADIRAN%20LTC-Batteries.pdf — –40…+85 °C 標準規格。

### 7.5 轉引自本專案其他章節（附原 URL）

86. **Single Piezoelectric Transducer as Strain Sensor and Energy Harvester Using Time-Multiplexing** — https://ieeexplore.ieee.org/document/7938680/ — 單一壓電時間多工兼感測與採集。【轉引 02、21 章】
87. **Ultrasonic through-wall communication and power delivery（RPI / Lawry et al.）** — https://ieeexplore.ieee.org/document/6396499/ — **50 W + 17.37 Mbps / 63.5 mm 鋼**。【轉引 02、16 章】
88. **Self-powered Through-wall Communication for Dry Cask Storage Monitoring（Annals of Nuclear Energy）** — https://www.sciencedirect.com/science/article/abs/pii/S0306454922003413 — 乾式貯存桶「無任何內部感測系統」。【轉引 16 章】
89. **Ultrasonic wireless power links for battery-free condition monitoring in metallic enclosures（Ultrasonics, 2021）** — https://www.sciencedirect.com/science/article/abs/pii/S0041624X21000366 — 無電池金屬腔內監測。【轉引 03 章】
90. **溫度對阻抗式 SHM 壓電感測器的影響** — https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3926611/ — EMI-SHM 的溫度脆弱性。【轉引 02 章】
91. **US6974397B2 — Racket with self-powered piezoelectric damping system** — https://patents.google.com/patent/US6974397B2/en — HEAD 自供電壓電阻尼（產品已停產）。【轉引 02、08、09 章】
92. **Self-Powered Synchronized Switching Interface Circuit for Piezoelectric Footstep Energy Harvesting** — https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9966393/ — 3.6 mW @ 1 Hz、83.02% 效率。【轉引 02 章】
