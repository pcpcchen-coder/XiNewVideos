# 市場規模、資金流向、政府計畫與新創動態

> 一句話結論：**真金白銀只流向三個地方——(1) 醫療植入／神經調控（Astellas 以約 3.04 億美元收購 Iota Biosciences，另加 5 年 1.25 億投資，是本專案迄今找到的最大單筆金額）、(2) 冷電漿（TDK 八年後把 relyon plasma 以「低至中雙位數百萬歐元」賣給 Viromed，金額之小本身就是負面訊號）、(3) 早期學研補助（ARPA-E IGNIITE 給 Jessica Boles 的 50 萬美元、DARPA AMEBA / Neural Dust）——而「壓電諧振器功率轉換」這條客戶已排除的路線，其資金訊號恰恰是三者中最弱的（單筆 50 萬美元的早期職涯獎，查無任何新創、查無任何 VC 輪次）。這與客戶的方向判斷一致。**

---

## 0. 研究方法與限制（必須先讀，本節決定你該如何折價採信本文件）

**這是本專案所有 dossier 中資料獲取條件最差的一份，請務必先讀完本節再看任何數字。**

1. **本輪我實際成功執行的 WebSearch 次數為 0（零）次。** 任務書要求 25–35 次查詢。我在發出第一組查詢時，系統即回報 `this session has used its web search budget (200 of 200 WebSearch calls)`——搜尋配額由本 session 的多個平行子代理共用，在我啟動前已被耗盡。我又試了第二次確認，回報相同。
2. **WebFetch 在本環境被 egress policy 全面封鎖**（任何 URL 回 403）。我另外測試了以 Bash `curl` 經 agent proxy 直連 marketsandmarkets.com，回報 `curl: (56) CONNECT tunnel failed, response 403`。**三條對外資料通道（WebSearch / WebFetch / curl）全部不可用。**
3. **因此本文件的性質必須被正確理解：它不是一份一手市場研究，而是一份「跨 dossier 資金訊號後設分析（meta-analysis）」。** 我把本專案 `sources/` 目錄下另外 12 份由平行代理產出的 dossier 全數讀過，把散落其中的**所有**市場規模、募資、併購、政府補助、玩家與通路訊號抽出、去重、交叉比對、並按「資金訊號強度 vs 技術成熟度」重新編排。所有 URL 均為那些 dossier 提供，**我本人未開啟驗證任何一個**。
4. **來源可信度已被兩次折損**：原 dossier 本身即註明「所有來源皆為 WebSearch 摘要層級、未取得一手全文」；我在其上再加一層轉引。**凡本文出現的數字，最高只能視為「二手轉引的搜尋摘要」，不得作為投資決策的定量依據。**
5. **以下是任務書明確要求、但本輪完全查無、且我拒絕以任何方式推測的項目（這份清單本身就是交付物的一部分）：**
   - **市調機構具名數字**：MarketsandMarkets、Yole Développement、Fortune Business Insights 的壓電元件／壓電致動器／BAW 濾波器／超音波換能器／haptics driver IC 市場報告數字——**全部查無**。（唯一出現的 Yole 文件是一份 2019 年 Qualcomm 3D Sonic 拆解樣本報告，不是市場規模報告。）
   - **上市公司壓電業務營收**：Murata、TDK/EPCOS、Kyocera、Taiyo Yuden、NGK Insulators 的壓電分部營收、出貨量、資本支出——**全部查無**。
   - **專業廠營收**：CTS/Noliac、PI Ceramic、Physik Instrumente、APC International、Piezo.com (Mide)、Meggitt/Ferroperm（現 CTS Denmark）——**全部查無營收數字**。
   - **新創募資輪次**：Boréas Technologies、xMEMS、Artimus Robotics、Ventiva、TTP Ventus / Lee Ventus、Ultraleap、Piezo Motion——**全部查無任何一輪募資金額、估值或投資人**。（唯一查到募資金額的壓電相關新創是 Cerca Magnetics，而它是 OPM 磁量測，不是壓電。）
   - **政府計畫**：Horizon Europe / EIC Pathfinder、日本 NEDO / JST、韓國、中國國家重點研發計畫、**台灣經濟部技術處／國科會／工研院的壓電相關計畫與法人能量——完全查無，一條都沒有。** 這是本文件對台灣客戶而言最嚴重的缺口。
   - **「壓電諧振器功率轉換」是否存在新創公司**：跨 13 份 dossier **查無任何一家具名公司**。詳見第 5 節。
6. **本文對每條事實標註信度**：【已交叉】= 兩份以上 dossier 獨立記載；【單一】= 僅一份 dossier 記載；【低信度市調】= 來源為二手市調聚合網站（dataintelo、verifiedmarketreports、futuremarketreport、datainsightsmarket 等），該類來源在原 dossier 中即被標為不可作決策依據。

---

## 1. 結論摘要

1. **本專案迄今找到的最大單筆資金事件在醫療，不在電力電子**：Astellas 收購 Iota Biosciences，**頭期 1.275 億美元 ＋ 最高 1.765 億美元里程碑（合計約 3.04 億美元），另加 5 年 1.25 億美元投資**；技術源頭是 UC Berkeley 的超音波供電植入物（Neural Dust / StimDust，DARPA 資助），2024 年取得膀胱刺激的 FDA IDE 早期可行性試驗核准。【已交叉，07 號 dossier 標為「已驗證」】
2. **冷電漿是唯一有量產壓電兩用元件的賽道，但大廠的退出價格是強烈負面訊號**：TDK 子公司 EPCOS 於 2018 年取得 relyon plasma **50.2%** 股權；**2026-03-04 Viromed Medical AG 簽署 LOI 收購，2026-07-27 完成盡職調查並與 TDK Electronics 達成非約束性共識，價格區間為「低至中雙位數百萬歐元」。** 八年後大廠選擇賣出、且金額僅數千萬歐元等級——代表 CeraPlas 沒有長成 TDK 想要的元件出貨量生意。【已交叉，10 號 dossier】
3. **冷電漿市場報告的絕對數字漂亮但與壓電無關**：多家機構給 2025 年 **USD 2.4–3.3 B**、2032–2035 年 **USD 5–12 B**、CAGR 14–16%，常壓段佔 66%。但這些數字涵蓋醫療、食品、半導體、紡織全域，**壓電式（PDD）只佔極小一角**，且 CeraPlas 的功率窗被鎖死在**個位數瓦特（評估套件 2–7 W，手持機整機 18 W）**——這個功率天花板決定它永遠吃不到工業製程級電漿那塊大餅。【已交叉，01/07/10 號 dossier】
4. **「壓電變壓器市場」的市調數字彼此矛盾達 3 倍以上，不可用**：USD 500M(2025)→950M(2033) CAGR 8%〔Data Insights〕、USD 220.5M(2025)→465.8M(2033) CAGR 9.8%〔Future Market Report〕、USD 0.57B(2023)→1.88B(2030) CAGR 20.5%〔Verified Market Reports〕。**同一標的、同一年份、三個不相容的量級。** 但無論取哪個數字，PT 市場都只有電感市場（USD 5.1B(2022)→7.0B(2027)）的 **3–10%**——這從市場結構面再次印證客戶排除「取代電感」路線的判斷。【已交叉，01/02/16 號 dossier】
5. **公部門資金真的存在，但金額小得驚人**：本專案跨 13 份 dossier 找到的**唯一具名金額的壓電功率轉換補助**是 **ARPA-E IGNIITE 2024 給 UC Berkeley 的 Jessica Boles，$500,000**（計畫名 "High-Performance, Modular Piezoelectric Components for Miniaturized Power Conversion"）。DARPA AMEBA（機械天線）與 DARPA Neural Dust 有計畫名但**查無預算金額**。DOE 側有 SLAC/CPAD 把壓電諧振器 DC-DC 列為高能物理探測器前端候選架構，以及 PNNL/Sandia 的乾式貯存桶感測器計畫（CURIE 文件）。**沒有任何一筆達到千萬美元等級。**
6. **歐盟的錢曾經投在「製造平台」而非「應用」**：FP7 **PiezoVolume**（grant 229196）把濺鍍 PZT 薄膜做到 150 mm 與 200 mm 基板上 d33,f > 100 pm/V、|e31,f| > 14 C/m² 並達標。這代表歐盟的策略是建代工能力，不是押應用——對台灣客戶的啟示是**代工能力可外購（SINTEF 經 imec/Europractice 的 MPB 每批可取得 3–12 片 6 吋 piezoMEMS 晶圓），不必自建產線**。【單一，03 號 dossier】
7. **大廠併購確實在發生，但買的是 MEMS 聲學不是壓電功率**：**Bosch Sensortec 收購 Arioso Systems**（MEMS 微揚聲器，NED 靜電驅動原理，10 mm² 有效面積產生 >120 dB）——注意這是**靜電**不是壓電，等於是壓電 MEMS 喇叭（xMEMS）的直接競爭路線被大廠買走。**收購金額查無。**【單一，11 號 dossier】
8. **一個 15 年、跨越化工巨頭的失敗案例必須記住**：SRI 於 2003 年分拆 Artificial Muscle Inc.，2006 年得獎，2010 年被 **Bayer MaterialScience 收購**並推出 ViviTouch 觸覺產品（用於手機、遊戲控制器、平板）。**今天市場上看不到 ViviTouch。**（結局未驗證——搜尋摘要未確認是否關閉，但也未顯示任何在售產品。）【單一，11 號 dossier】

---

## 2. 現況：技術 / 產品 / 玩家

### 2.1 已量產、可買到的壓電「主動＋被動兩用」商品（真實出貨的短名單）

| 產品 | 廠商 | 兩用性質 | 通路／市場證據 |
|---|---|---|---|
| **CeraPlas HF** | TDK Electronics（前 EPCOS）＋ relyon plasma | 被動＝機械共振升壓；主動＝陶瓷表面即放電電極，直接點燃常壓冷電漿 | Mouser、key-components 有售；2018-11-13 上市；尺寸 47.3×20×20 mm |
| **piezobrush PZ2 / PZ3** | relyon plasma（TDK 子公司） | 同上，整機 | PZ2 自 2014 年起銷售**已 12 年**；PZ3 在牙科通路與 igus rbtx 機器人末端執行器目錄上架 |
| **PowerHap** | TDK | 致動器內建感測：壓力偵測 ≤25 N、激振 1 Hz–1000 Hz | TDK 正式產品頁 |
| **BOS1901 / BOS1921 / BOS1931 / BOS0614** | Boréas Technologies（加拿大） | 驅動 IC 層級的兩用：同一顆壓電片既做觸覺致動又感測按壓力；BOS1901 被描述為「市場上唯一同時觸發觸覺並感測按壓力的壓電驅動 IC」 | Mouser 有售；**台灣由 EDOM 益登科技代理**；與 Synaptics 合作壓電觸控板；2020 年車用 HMI 新聞稿 |
| **3D Sonic 指紋辨識** | Qualcomm | 24×8 PMUT 陣列（180 nm CMOS），同一組電極 TX/RX 模式切換做 pulse-echo 成像 | 已在旗艦手機量產；Yole 拆解樣本報告 |
| **Cypress / Skyline** | xMEMS | Cypress：同一 MEMS 同時做超音波載波調變與解調（sound-from-ultrasound），低頻 SPL >130 dB，2025 年宣布量產就緒。Skyline DynamicVent：同一壓電結構既是聲學阻抗元件（閥）又是致動器，開孔等效 1.1 mm²、100 Hz 衰減 up to 25 dB | 官方新聞稿＋audioXpress 報導 |
| **多層 PT（SMMTF55P4S80 等）** | STEMINC / Micromechatronics | 現貨 PT 元件 | **零售單價：單層 PT（50 kHz, 2 W 級）USD 23.76 / 2 顆 ≈ USD 11.88 / 顆**（本專案唯一取得的壓電元件實際報價） |

> **這張表是本文件最有價值的一頁**：它說明「壓電兩用元件」不是紙上概念，2026 年就有六類商品在賣。但也說明——**這些商品全部集中在「觸覺」「聲學」「電漿」三塊，沒有一個在功率轉換。**

### 2.2 玩家格局（依資金與市場地位排序）

- **絕對主導者：TDK Electronics（含 EPCOS、relyon plasma）**。同時擁有 CeraPlas（電漿）、PowerHap（觸覺）、汽車噴油系統的銅內電極多層壓電技術（已用 20 年以上）。專利族厚實：US10856399B2、US10638590B2、US11903321、US10772182、US10966309、US10531552、US10827599、WO2021122995A1、US20200305266、EP2256835A3。**但它正在賣掉 relyon（見第 5 節）。**
- **驅動 IC 唯一具名玩家：Boréas Technologies**。CapDrive 架構宣稱從致動器負載電容回收能量再利用，**電流消耗最多降 90%、比競品壓電驅動 IC 效率好 10×、比 LRA 省電 20×**（全為廠商宣稱，且度量是「電流消耗」不是「轉換效率」，不可與學術界「損耗降 49–55%」混用）。**募資輪次、估值、營收、出貨量全部查無。**
- **舊世代已退場者：Murata / Matsushita(Panasonic) / NEC**。1990s–2000s CCFL 世代 PT 專利（US6184631B1、EP1050954A4、US5969954A、US6535407）推算已到期，**2020 年後新佈局查無**。Kyocera / Taiyo Yuden 的壓電功率轉換佈局**查無**。
- **piezoMEMS 代工生態（客戶可外購的能力）**：Silex Microsystems（瑞典，PZT 與 AlN 皆有，與 ULVAC 合作，投入超過 15 年）、SINTEF（經 imec / Europractice 的 MPB，每批 3–12 片 6 吋晶圓，**對台灣團隊是成本最低的切入口**）、imec、Fraunhofer ISIT、Rogue Valley Microdevices（美國）、**I-PEX（日本，唯一明確提供無鉛薄膜代工）**、ROHM（日本）。VTT、X-FAB **查無**。
- **台灣／中國廠商：完全查無。** 本專案 13 份 dossier 沒有任何一份記載到台灣或中國的壓電元件廠、法人計畫或供應鏈訊息。**這是必須在下一輪補上的最大空白。**

### 2.3 相鄰賽道的資金訊號（判斷「錢的溫度」用）

- **醫療植入／超音波供電**：Astellas × Iota（約 3.04 億美元 + 1.25 億投資）是最大單筆。另有 **EBR Systems WiSE-CRT**（超音波供電無導線左心室起搏電極）——07 號 dossier 明確標註「**完全未查，勿引用任何內容**」，這可能是超音波供電植入物**最成熟的商業案例**，是下一輪的第一優先。
- **OPM-MEG（磁量測，非壓電，但代表「無磁環境」市場的付費意願）**：Cerca Magnetics 2026 年完成 **£3.8M Series A**（Guinness Ventures 領投），**投後估值 €34.5M**；市場預估 $185M(2024)→$1.02B(2033) CAGR 21.1%（**未驗證、單一來源**，且與另一組「helium-free MEG $125.88M(2025)→$355.42M(2032)」不一致，**兩組數字請勿混用**）。
- **無風扇散熱（離子風 EHD）**：**Ventiva ICE9** 已在 CES 展示為 Lunar Lake 筆電移除約 25 W 熱，2025 年宣布上看 100 W、2027 年目標 40 W TDP 筆電設計，**噪音 <15 dBA、釋放最多 40% 板面積**，取得 Intel / Dell 關注。**這是十億美元級的散熱市場，而離子風本質上就是 kV/µA 的純電容＋電暈負載——PT 的天然匹配負載。Ventiva 的融資輪次與電極實際工作電壓查無。**
- **人工肌肉 / 電黏附（低信度市調，僅供量級參考）**：人工肌肉 USD 1.98B(2024)→3.44B(2030) CAGR 9.62%〔GlobeNewswire〕；電黏附夾具 USD 412.3M(2024)→1,344.2M(2033) CAGR 15.8%〔Dataintelo〕。**兩者皆為二手市調聚合網站，原 dossier 已標為不可作決策依據。**

---

## 3. 關鍵數字表

| 類別 | 項目 | 數字 | 信度 | 來源編號 |
|---|---|---|---|---|
| **併購** | Astellas 收購 Iota Biosciences | 頭期 **USD 127.5M** ＋ 里程碑最高 **176.5M**（合計 ~**304M**），另 5 年 **125M** 投資 | 已驗證（07 標註） | [1] |
| **併購** | TDK/EPCOS 取得 relyon plasma 股權（2018） | **50.2%** | 已交叉 | [2] |
| **併購** | Viromed Medical 收購 relyon（LOI 2026-03-04；DD 完成 2026-07-27） | **低至中雙位數百萬歐元** | 已交叉 | [3][4] |
| **併購** | Bosch Sensortec 收購 Arioso Systems | 金額**查無** | 單一 | [5] |
| **併購** | Bayer MaterialScience 收購 Artificial Muscle Inc.（2010） | 金額**查無**；結局未驗證 | 單一 | [6] |
| **募資** | Cerca Magnetics Series A（2026） | **£3.8M**（另稱 €4.3M），投後估值 **€34.5M**，Guinness Ventures 領投 | 單一（未驗證） | [7][8] |
| **募資** | Boréas / xMEMS / Artimus / Ventiva / TTP Ventus / Ultraleap / Piezo Motion | **全部查無** | — | — |
| **政府** | ARPA-E IGNIITE 2024（J. Boles, UC Berkeley） | **USD 500,000** | 已交叉 | [9][10] |
| **政府** | DARPA AMEBA（機械天線，2017 起） | 預算**查無**；**結案狀態與是否轉軍種亦查無** | 單一 | [11] |
| **政府** | DARPA Neural Dust（UC Berkeley） | 預算**查無**；原型 3×1×0.8 mm | 單一 | [12] |
| **政府** | EU FP7 PiezoVolume | grant **229196**；金額**查無** | 單一 | [13] |
| **政府** | DOE SLAC/CPAD | 把壓電諧振器 DC-DC 列為高能物理探測器前端候選；金額**查無** | 單一 | [14] |
| **政府** | 台灣（經濟部／國科會／工研院）、日本 NEDO/JST、Horizon Europe/EIC、韓國、中國重點研發 | **全部查無，一條都沒有** | — | — |
| **市場** | 壓電變壓器市場（版本 A） | USD **500M(2025) → 950M(2033)**，CAGR 8% | 低信度市調 | [15] |
| **市場** | 壓電變壓器市場（版本 B） | USD **220.5M(2025) → 465.8M(2033)**，CAGR 9.8% | 低信度市調 | [16] |
| **市場** | 壓電變壓器市場（版本 C） | USD **0.57B(2023) → 1.88B(2030)**，CAGR 20.5% | 低信度市調 | [17] |
| **市場** | 電感市場（對照組） | USD **5.1B(2022) → 7.0B(2027)** | 低信度市調 | [15] |
| **市場** | 冷電漿市場（Towards Healthcare） | USD **2.92B(2024) → 3.34B(2025) → 11.14B(2034)**，CAGR 14.35% | 低信度市調 | [18] |
| **市場** | 冷電漿市場（Precedence） | USD **3.28B(2025) → 12.19B(2035)**，CAGR 14.03%；**常壓段佔 66%** | 低信度市調 | [19] |
| **市場** | 冷電漿市場（Coherent Market Insights） | USD **4.97B by 2032** | 低信度市調 | [20] |
| **市場** | 人工肌肉市場 | USD **1.98B(2024) → 3.44B(2030)**，CAGR 9.62% | 低信度市調 | [21] |
| **市場** | 電黏附夾具市場 | USD **412.3M(2024) → 1,344.2M(2033)**，CAGR 15.8% | 低信度市調 | [22] |
| **市場** | OPM-MEG 市場 | USD **185M(2024) → 1.02B(2033)**，CAGR 21.1% | 未驗證、單一 | [8] |
| **出貨量（歷史）** | CCFL 世代壓電變壓器年銷量 | **2,500–3,000 萬顆/年**（1990s 中–2000s 初，主要產地日本），LED 取代後主要供應商停產、專用 IC 停產 | 已交叉 | [23] |
| **出貨量（現行）** | Epson 印表機（自感測印字頭） | 自稱年產 **>1,500 萬台**，印字頭設計為與機器同壽命 | 單一 | [24] |
| **單價** | STEMINC 單層 PT（50 kHz, 2 W 級）零售 | **USD 23.76 / 2 顆 ≈ USD 11.88 / 顆** | 單一 | [25] |
| **單價** | TDK CeraPlas 單價 / 壽命 / MTBF | **官方與媒體均未揭露＝查無** | — | — |
| **單價** | XP Power Q101-5（10 kV / 0.5 W 磁性 HV 模組，競品對照） | **USD 420.06**；5 kV 版體積 0.125 in³ | 單一 | [26] |
| **產品規格** | CeraPlas 功率窗 | 評估套件預設 ~**4.5 W**，可選 **2–7 W**，24 V 單電源；piezobrush PZ3 整機最大 **18 W** | 已交叉 | [27][28] |
| **產品規格** | CeraPlas 升壓 | **12–24 Vpp @ 50 kHz → 最高 20 kV**，元件表面溫度 **<50 °C**，升壓比 **>1000** | 已交叉 | [29][30] |
| **法規倒數** | RoHS Annex III 7(c)-VI（涵蓋 PZT） | 豁免至 **2027-12-31**；7(c)-I 至 2027-06-30；續期申請須於 **2026-06-30 前**提出（該日已過，**是否有人提出查無**） | 已交叉 | [31][32] |

> **讀表警告**：本表「市場」段的七個數字全部來自二手市調聚合網站。同一標的（壓電變壓器）出現 220M / 500M / 570M 三個不相容量級，**這不是誤差，是這類報告本身沒有可信方法論的證據**。它們唯一的資訊價值是「有人願意花錢賣這個領域的報告，代表有關注度」，這是**弱訊號**，不是市場規模。

---

## 4. 「新能力型」應用機會（純以資金訊號視角評估）

> 本節不重複其他 dossier 的技術論證，只回答一個問題：**這條路上有沒有錢？誰的錢？多少？**

### 4.1 超音波供電／通訊的體內植入物（資金訊號：★★★★★，全場最強）

- **新能力是什麼**：把 mm 級無電池、無導線的刺激／感測節點放進體內深處，用超音波供電並以 backscatter 回傳訊號。壓電晶體同時是能量接收器（被動）與通訊反射調變器（主動）。
- **為什麼以前做不到**：射頻在人體組織中衰減與加熱限制嚴重，且天線尺寸與波長綁定；超音波在組織中衰減低得多，且 mm 級壓電體就能有效耦合。**這是尺寸—物理的硬約束，不是工程優化。**
- **是否真非替代**：**是。** 替代方案是「有導線的植入物」或「較大的電感耦合植入物」，兩者在解剖學上是不同的東西。
- **誰在做**：UC Berkeley（Neural Dust / StimDust，DARPA 資助；專利族 US10118054、US10300309B2、US10300310B2、US10682530B2、US20190150882A1、WO2018009905A2/A3、WO2018009910A1）→ **Iota Biosciences → Astellas（2020，約 3.04 億美元 + 5 年 1.25 億投資）**。
- **TRL**：**7**（2024 年膀胱刺激取得 FDA IDE 早期可行性試驗核准）。
- **市場訊號**：**本專案最強**——大藥廠併購 ＋ 額外五年鉅額投資 ＋ 法規進展。
- **技術難點（資金視角）**：這條路的門檻不是壓電技術，是**臨床試驗與法規**。台灣元件廠若無醫材夥伴，切入點只能是**供應鏈上游（賣壓電微換能器給植入物廠）**，而非做完整產品。
- **⚠ 未查缺口**：**EBR Systems WiSE-CRT 完全未查**（超音波供電無導線左心室起搏電極，可能是本域最成熟的商業案例）。**在補上這一項之前，不應對本機會做最終判斷。**

### 4.2 元件本身即為放電電極的冷電漿源（資金訊號：★★★，但方向正在反轉）

- **新能力是什麼**：單一陶瓷同時是升壓器與放電電極，**高壓從未離開元件本體**，因此不需高壓佈線、高壓連接器、爬電距離與屏蔽。TDK 官方稱「無需針對高壓做特別的安全防護措施即可整合」。
- **為什麼以前做不到**：不是不能升壓（磁性變壓器當然能升到 10 kV），做不到的是**「升壓器與電極是同一個物體」**的拓樸——磁性方案必須有高壓繞線、絕緣、引線與獨立電極，體積與絕緣設計在手持／消費級尺寸下不可行。
- **是否真非替代**：**是**（拓樸新能力，不是尺寸縮小）。
- **誰在做**：TDK Electronics ＋ relyon plasma（PDD® 商標）；學術端 LAPLACE Toulouse、Korzec 等人（*Plasma Processes and Polymers* 2020、MDPI *Plasma* 4(2),19）。
- **TRL**：**9（已量產 12 年）**。
- **市場訊號（矛盾）**：
  - **正向**：冷電漿市場報告數字漂亮（見第 3 節）；Viromed 收購 relyon 的明確理由是「打造整合型冷電漿技術平台」並推進法規；牙科通路已在賣 PZ3；igus rbtx 把 PZ3-i 列為機器人末端執行器。
  - **負向（更重要）**：**TDK 在持股八年後選擇賣出，且價格僅「低至中雙位數百萬歐元」。** 一家年營收百億美元級的被動元件巨頭，若 CeraPlas 真的長成了元件出貨量生意，不會用這個價格出場。
- **最大障礙（資金視角）**：**功率天花板 2–7 W / 整機 18 W**，鎖死在「表面處理、消毒、離子化」，做不了工業製程級電漿。加上 TDK 專利族厚實，後進者只能在**陣列化／嵌入式／無鉛材料**這幾個縫隙找白空間。

### 4.3 kV 級高壓源作為「使能元件」賣給無風扇散熱 / 靜電應用（資金訊號：★★★★，但屬半替代）

- **新能力是什麼**：把 kV 產生器做進 2–5 mm 厚的筆電殼內。**Ventiva ICE 已證明市場真的要這個**（<15 dBA、無移動件、釋放最多 40% 板面積、Intel / Dell 關注、2025 年宣布上看 100 W）。
- **是否真非替代**：**半。** Ventiva 的產品本身是新能力（無風扇散熱），但 PT 在其中只是「更薄的高壓源」——屬使能元件而非新能力創造者。**依客戶方向限制應標記並降權。** 但商業訊號是本清單中最貼近量產的，適合當「先賺錢的橋頭堡」。
- **對照組成本**：磁性 HV 模組 XP Power Q101-5（10 kV / 0.5 W）零售 **USD 420.06**，5 kV 版體積 0.125 in³。相對於 STEMINC PT 的 USD 11.88——**在高壓這一格，「壓電太貴」的論證不成立，反而是壓電便宜兩個數量級。這是本文件對客戶成本疑慮最直接的反駁點。**
- **TRL**：Ventiva 產品側 7–8；PT 作為其電源的整合驗證 **查無任何公開案例**。
- **最大障礙**：**Ventiva ICE 的實際電極電壓、電流與電源模組規格查無**。若工作點是 2–5 kV / 數百 µA，PT 是極佳匹配；若需 10 kV+ 或數 mA，則需重評。**這是一通電話就能問到的資訊，建議列為第一優先的商業盡職調查動作。**

### 4.4 高單價、低量、認證嚴的極端環境利基（資金訊號：★★，但商業邏輯最健康）

- **涵蓋**：穿金屬壁供電＋通訊（核電乾式貯存桶、石化壓力容器、船艦艙壁）、強磁場環境功率轉換（MRI 相容電子、高能物理探測器）、300–650 °C 高溫感測。
- **資金訊號**：DOE 系統性投入（SLAC/CPAD、PNNL/Sandia CURIE 乾儲罐感測器計畫）、Army Research Laboratory 合約 **W911NF2220007**、RPI / Penn State / Stevens Institute 的持續研究。**但全部是研究經費，查無任何一筆商業投資、查無任何一家公司。**
- **為什麼這個象限的商業邏輯健康**：**銷量小、單價高、認證嚴，正好抵消壓電單價高的缺點。** 這與客戶「壓電太貴打不過磁性元件」的顧慮直接互補——在這些市場，元件成本根本不是決策變數。
- **致命反證**：**穿金屬壁技術近 30 年未商品化。** 起源可追至 1997 年 Connor 專利，2011 年 RPI 已有 50 W / 12.4 Mb/s 的媒體級成果，2015 年已有完整綜述——但 **2026 年仍查無任何具名商用產品或 ATEX/IECEx 認證方案**。技術可行 ≠ 市場可行。

### 4.5 觸覺／聲學 MEMS（資金訊號：★★★，但已被佔位）

- **玩家已就定位**：Boréas（驅動 IC，Synaptics 合作，**台灣 EDOM 可取樣**）、TDK PowerHap（元件）、xMEMS（MEMS 喇叭與閥，2025 量產就緒）、Qualcomm（PMUT 指紋，已量產）、**Bosch Sensortec 已收購 Arioso Systems**（靜電路線的競爭者）。
- **是否真非替代**：xMEMS Cypress（同一 MEMS 做超音波調變與解調）與 Skyline（同一結構既是聲學閥又是致動器）是**真兩用**；但 haptics 這塊本質是「壓電取代 LRA / ERM」，屬**替代型，應降權**。
- **對客戶的意義**：**這是唯一「台灣供應鏈可及、可短期取樣驗證」的入口**——EDOM 代理 Boréas 意味著評估板與 FAE 支援的路徑是通的，可把 PoC 時程壓縮數個月。但作為**主戰場**，在位者太強、且多屬替代型。

---

## 5. 反面證據、失敗案例與物理上限（資金視角）

1. **「壓電諧振器功率轉換」在 2026 年沒有一家新創公司。** 這是本文件最重要的單一發現。跨 13 份 dossier、涵蓋專利、學術、市場、供應鏈的全面檢視，找到的全部是：MIT（Boles 等，US12126324，優先權日 2021-05-07，推算保護至 ~2041–2042）、UC Berkeley 技轉掛牌（NCD 33625、33842、33585）、Stanford（Rivas-Davila）、以及 **ARPA-E 的 50 萬美元早期職涯獎**。**沒有 spin-out、沒有 Series A、沒有產品、沒有報價。** 一個技術若在頂尖學校做了十年、發了一堆 IEEE TPEL、功率密度做到 1.01 kW/cm³ 甚至 5.7 kW/cm³、效率 99%，卻仍然沒有一家公司願意成立——**這本身就是市場已經投票的證據，且與客戶排除該路線的直覺一致。**
2. **TDK 賣掉 relyon plasma 是本領域最重的一記警鐘。** 2018 年買 50.2%，2026 年賣，價格「低至中雙位數百萬歐元」。**這是唯一一個「壓電主動/被動兩用元件真正量產」的案例，而它的財務結局是大廠退場。** 買方 Viromed Medical AG 是醫材公司，買的是「整合型冷電漿平台」與法規路徑——**代表價值重心從「元件」移到「應用與法規」，元件商在這條價值鏈上分不到錢。**
3. **CCFL 背光是完整的興衰週期，而且死得很快很徹底。** 2000 年代初期 25–30% 的 CCFL 背光採用壓電變壓器，年出貨 **2,500–3,000 萬顆**；LED 背光取代後，**主要供應商停止量產、連專用驅動 IC 都停產**。教訓是：**壓電元件的市場依附於一個特定的「非電磁優勢窗口」，窗口一關，整條供應鏈同時蒸發。** 投資回收期評估必須把「窗口關閉風險」明確定價。
4. **人工肌肉／電活性聚合物：15 年、一家化工巨頭、零留存產品。** SRI 2003 分拆 AMI → 2006 得獎 → 2010 Bayer MaterialScience 收購 → ViviTouch 上市（手機、遊戲控制器、平板）→ **2026 年市場上看不到**。（結局未驗證。）這條路的失敗不是因為缺錢或缺大廠背書——兩者都有過。
5. **納米定位市場明確拒絕「自感測」。** Physik Instrumente 的高階產品仍採外部電容式 direct metrology。**在精度真正要緊的地方，工程師選擇多加一顆感測器。** 若客戶的商業賣點是「省掉感測器」，這個案例必須先被回答。
6. **Avago 早在 2005–2009 年就用 FBAR 做出跨隔離障壁的聲學通訊（US7525398），20 年後隔離器市場仍由磁耦（ADI iCoupler、Infineon coreless transformer）與電容耦（Silicon Labs）主導。** 「物理上更好」不等於「商業上會贏」——隔離器是高度成本敏感、認證（UL/VDE/IEC 60747-17）門檻極高的市場，新原理要重跑全部安規認證。
7. **DARPA AMEBA 的沉默本身是證據。** 機械天線計畫若已產出可部署系統，理應有後續型號、廠商、或轉移到軍種的公開紀錄。**查無任何此類紀錄。** DARPA 專案結束後無下文，通常意味著技術指標未達可轉移門檻。20 號 dossier 對此線的判定是「**商業化零證據：無公司、無產品、無報價、無供應鏈**」。
8. **市調數字不可用，且不可用的程度超乎預期。** 同一標的「壓電變壓器市場」出現 **220.5M / 500M / 570M** 三個 2023–2025 年的不相容數字，CAGR 從 8% 到 20.5%。冷電漿市場 2032 年預估從 4.97B 到 12.19B。**這些不是誤差範圍，是不同的世界。** 任何以這些數字為基礎的財務模型都是虛構的。
9. **RoHS 有一個明確的倒數計時器。** PZT 的鉛豁免（Annex III 7(c)-VI）至 **2027-12-31**，續期申請須於 **2026-06-30 前**提出——**該日期已過，而是否有廠商提出續期申請「查無」**。若無人申請，客戶的整個 PZT 路線在歐盟市場只剩 17 個月壽命。而無鉛 KNN 在「高功率硬式共振」這一格**至今沒有可用材料**（吸濕、燒結窗窄、K/Na 揮發、電性對製程參數極度敏感）。**這是一個有日期的法規風險，不是抽象風險。**
10. **成本論證目前無法被驗證，也無法被反駁。** CeraPlas 的單價、壽命、MTBF **官方與媒體均未揭露**；PZT 陶瓷的 $/kg 或 $/pc **查無**；與磁性元件的逐項 BOM 比較 **查無**。目前唯二的實際報價是 STEMINC PT **USD 11.88/顆** 與 XP Power 10 kV 磁性模組 **USD 420.06**——**在高壓這一格，壓電便宜兩個數量級。** 客戶「壓電單價高打不過磁性元件」的前提，在低壓大電流域成立，**在 kV 級高壓域可能完全不成立。這個區分應該寫進策略文件的第一頁。**

---

## 6. 未解問題（給下一輪研究，按優先序）

1. **【最高優先，台灣落地必需】台灣的法人能量與計畫資源完全空白。** 必須查：工研院（電光所／材化所）是否有壓電材料或 piezoMEMS 產線與試量產能力？國科會／經濟部技術處近五年有無壓電相關主題計畫？中科院在 VLF／水下通訊有無需求端入口？國內有無壓電陶瓷粉體或多層共燒（LTCC/MLCC）產能可轉用？**沒有這一節，任何投入建議都不可執行。**
2. **【最高優先，商業盡職調查】直接詢價與接觸，不要再靠搜尋。** (a) 向 Mouser / key-components / TDK 詢 CeraPlas HF 的 1 / 100 / 1k / 10k pcs 階梯價與 reliability report；(b) 向 EDOM 益登索取 Boréas BOS1901 / BOS0614 評估板與規格書；(c) **聯繫 Ventiva 詢問 ICE 電源模組的電壓／電流工作點**（判斷 PT 是否為可行供應方案）。**這三通電話能取得的資訊，超過本輪任何搜尋。**
3. **【重大缺口】EBR Systems WiSE-CRT 完全未查。** 超音波供電無導線左心室起搏電極，可能是超音波供電植入物最成熟的商業案例。需補：專利號、權利人、FDA 核准狀態、營收、上市地（疑為 ASX 掛牌，**未驗證，勿假設**）。
4. **【資金訊號補完】新創募資輪次全部空白。** Boréas Technologies、xMEMS、Artimus Robotics、Ventiva、TTP Ventus / Lee Ventus、Ultraleap、Piezo Motion 的募資金額、投資人、估值、客戶名單——一條都沒查到。建議下一輪用 Crunchbase / PitchBook 式查詢語法（"<公司> Series B funding round led by"）逐一補。
5. **【法規倒數】RoHS Annex III 7(c)-VI 的續期申請是否已在 2026-06-30 前提出？由誰提出？** 必須查 EU Commission / Oeko-Institut 的 exemption evaluation 公開文件。這決定 PZT 在歐盟是 2027-12-31 硬截止還是可再展延。
6. **【市場數字的可信替代】放棄市調報告，改用可驗證的代理指標。** 建議下一輪不要再找市場規模報告（已證明彼此矛盾 3 倍），改查：Digi-Key / Mouser 上 TDK PowerHap、CeraPlas、Murata 陶瓷共振器的階梯價與庫存量（庫存量是出貨量的可觀察代理）、以及上市公司財報中的壓電分部揭露。
7. **【反面證據補完】穿金屬壁近 30 年未商品化的真正原因是什麼？** 是認證成本、耦合劑可靠度、單位成本、還是缺乏 killer app？**必須找到具體的失敗案例或已放棄的商業化嘗試**（例如是否有新創募資後倒閉）。這條線的商業邏輯看起來最健康，卻 30 年無人成功，反差本身需要解釋。

---

## 7. 來源清單

> **全體警告**：以下所有 URL 均轉引自本專案 `research/piezo-active-passive/sources/` 目錄下其他 dossier，**我本人在本輪未開啟或驗證任何一個**（WebSearch 配額耗盡、WebFetch 與 curl 均被 egress policy 封鎖）。原 dossier 亦註明其內容僅為 WebSearch 摘要層級。**採信前務必自行開啟核對。**

### 併購與資金事件

1. Astellas / Iota Biosciences 收購案 — 轉引自 `07-patents-nonpower-apps.md` 來源 [12]（該 dossier 標註「已驗證」，但**未提供可點擊 URL**，需下一輪補齊一手新聞稿連結）— 頭期 1.275 億 USD ＋ 最高 1.765 億里程碑 ＋ 5 年 1.25 億投資；2024 年膀胱刺激 FDA IDE。
2. TDK Electronics 新聞稿 — EPCOS acquires majority stake in relyon plasma（50.2%，2018）— https://www.tdk-electronics.tdk.com/en/373388/company/press-center/press-releases/press-releases/tdk-subsidiary-epcos-acquires-majority-stake-in-relyon-plasma/2240584
3. EQS / TradingView — Viromed Medical AG signs LOI to acquire relyon plasma GmbH（2026-03-04）— https://www.tradingview.com/news/eqs:f46067e6f094b:0-viromed-medical-ag-signs-letter-of-intent-to-acquire-relyon-plasma-gmbh-strategic-step-toward-integrated-platform-for-cold-plasma-technology/ — 「整合型冷電漿技術平台」策略。
4. Viromed 盡職調查完成與價格區間（2026-07-27，「低至中雙位數百萬歐元」）— 轉引自 `10-hv-plasma-ozone-sterilization.md` 來源 [29]，**該 dossier 未列出獨立 URL，需補**。
5. audioXpress — Bosch Sensortec Acquires MEMS Microspeaker Innovator Arioso Systems — https://audioxpress.com/news/bosch-sensortec-acquires-mems-microspeaker-innovator-arioso-systems — NED 靜電驅動原理，10 mm² 產生 >120 dB；**收購金額未揭露**。
6. SRI International — 75 Years of Innovation: Artificial Muscle — https://www.sri.com/75-years-of-innovation/75-years-of-innovation-artificial-muscle/ ；chemeurope — Bayer MaterialScience acquires Artificial Muscle, Inc. — https://www.chemeurope.com/en/news/114742/bayer-materialscience-acquires-artificial-muscle-inc.html — 2003 分拆、2010 收購、ViviTouch；**結局未驗證**。
7. Pulse 2.0 — Cerca Magnetics: £3.8 Million Series A — https://pulse2.com/cerca-magnetics-3-8-million-series-a-raised-to-advance-opm-meg-brain-imaging-technology-toward-clinical-deployment/ — Guinness Ventures 領投。
8. Sci-Tech Today — Cerca Magnetics Secures €4.3M for Wearable Brain Imaging — https://www.sci-tech-today.com/news/cerca-magnetics-secures-4-3m/ — 投後估值 €34.5M；OPM-MEG 市場 $185M(2024)→$1.02B(2033) CAGR 21.1%（**未驗證**）。

### 政府與公部門計畫

9. ARPA-E — High-Performance, Modular Piezoelectric Components for Miniaturized Power Conversion — https://arpa-e.energy.gov/programs-and-initiatives/search-all-projects/high-performance-modular-piezoelectric-components-miniaturized-power-conversion — Boles，IGNIITE 2024，**$500,000**。
10. Berkeley EECS — Jessica Boles wins ARPA-E IGNIITE Early Career Award — https://eecs.berkeley.edu/news/jessica-boles-wins-arpa-e-igniite-early-career-award/ — 同上之新聞佐證。
11. DARPA — Underwater Radio, Anyone?（AMEBA 計畫）— https://www.darpa.mil/news/2016/underwater-radio — 機械天線計畫脈絡；**預算與結案狀態查無**。
12. DARPA — Implantable "Neural Dust" — https://www.darpa.mil/news/2016/implantable-neural-dust — 3×1×0.8 mm 原型與壓電晶體雙用途官方說明。
13. EU FP7 PiezoVolume（grant 229196）— 轉引自 `03-materials-manufacturing.md` 來源 [58]，該 dossier **未列獨立 URL**；成果為濺鍍 PZT 於 150/200 mm 基板達 d33,f > 100 pm/V。
14. SLAC / CPAD（DOE 高能物理探測器儀器協調機構）2023 Kickoff 與 2025 年會 — 轉引自 `15-magnetic-immune-clean.md` 來源 S45 與 `01-pt-power-conversion-sota.md` S21，**未列獨立 URL**。
15.（另見）CURIE / Sandia — Sensor Development for Liquid Water Detection in Dry Storage Casks (FY19 Status) — https://curie.pnnl.gov/sites/default/files/sandiadocs/M3SF-19PN010201034-Sensor-Development-for-Liquid-Water-Detection-in-Dry-Storage-Casks-FY19-Status.pdf — DOE 乾儲罐感測器計畫。

### 市場規模報告（全部為低信度二手市調，不可作決策依據）

16. Data Insights Market — Piezoelectric Ceramic Transformers — https://www.datainsightsmarket.com/reports/piezoelectric-ceramic-transformers-1664155 — PT 500M(2025)→950M(2033)；同段引用電感市場 5.1B(2022)→7.0B(2027)。
17. Future Market Report — Piezoelectric Transformers Market — https://www.futuremarketreport.com/industry-report/piezoelectric-transformers-market — 220.5M(2025)→465.8M(2033)，CAGR 9.8%。
18. Verified Market Reports — Piezoelectric Transformers Market — https://www.verifiedmarketreports.com/product/piezoelectric-transformers-market/ — 0.57B(2023)→1.88B(2030)，CAGR 20.5%。**與 16、17 相差達 3 倍。**
19. Towards Healthcare — Cold Plasma Market Sizing — https://www.towardshealthcare.com/insights/cold-plasma-market-sizing — 2.92B(2024)→3.34B(2025)→11.14B(2034)，CAGR 14.35%。
20. Precedence Research — Cold Plasma Market — https://www.precedenceresearch.com/cold-plasma-market — 3.28B(2025)→12.19B(2035)，CAGR 14.03%；常壓段 66%。
21. Grand View Research — Cold Plasma Technology Market Report — https://www.grandviewresearch.com/industry-analysis/cold-plasma-technology-market-report — 第三方市場估計。
22. GlobeNewswire / Coherent Market Insights — Cold Plasma Market to Hit USD 4.97 B by 2032（2025-11-11）— https://www.globenewswire.com/news-release/2025/11/11/3185580/0/en/Cold-Plasma-Market-Size-to-Hit-USD-4-97-Billion-by-2032-says-Coherent-Market-Insights.html — 用以顯示估值分歧。
23. GlobeNewswire — Artificial Muscle Research Report 2025 — https://www.globenewswire.com/news-release/2025/12/02/3198178/0/en/Artificial-Muscle-Research-Report-2025-Market-to-Reach-3-44-Billion-by-2030-Driven-by-Advanced-Prosthetics-Soft-Robotics-and-Innovations-in-Electroactive-Polymer-Materials.html — 1.98B(2024)→3.44B(2030)，CAGR 9.62%。
24. Dataintelo — Electroadhesive Gripper Market Research Report 2033 — https://dataintelo.com/report/electroadhesive-gripper-market/amp — 412.3M(2024)→1,344.2M(2033)，CAGR 15.8%；玩家含 Grabit、Festo、Schunk、OnRobot、Piab、Zimmer。
25. MDPI Actuators 5(2), 12 — Piezoelectric Transformers: An Historical Review — https://www.mdpi.com/2076-0825/5/2/12 — **CCFL 世代年銷 2,500–3,000 萬顆、LED 取代後供應商與專用 IC 全面停產**（本文件最重要的歷史失敗案例來源）。

### 產品、通路與單價（可驗證的硬訊號）

26. Mouser — CeraPlas HF Piezoelectric Plasma Generator (EPCOS/TDK) — https://www.mouser.in/new/epcos/epcos-ceraplas-hf/ — 通路商品頁，證明實際可購買。
27. key-components — EPCOS/TDK CeraPlas HF Evaluation Kit — https://www.key-components.com/news/epcos-tdk-ceraplas-hf-evaluation-kit.html — 評估套件 ~4.5 W 預設、2–7 W 可選、24 V 單電源。
28. relyon plasma — PiezoBrush PZ3 — https://www.relyon-plasma.com/piezobrush-pz3/?lang=en — 手持機最大 18 W、PDD 技術、<50 °C。
29. TDK Electronics — Cold plasma from a single component — https://www.tdk-electronics.tdk.com/en/373562/tech-library/articles/applications-cases/applications-cases/cold-plasma-from-a-single-component/1109546 — 12–24 Vpp → 最高 20 kV、<50 °C、多層 Rosen 型硬 PZT 共燒銅電極。
30. TDK — CeraPlas Element datasheet — https://www.tdk-electronics.tdk.com/download/2307712/39eb3392c71d1191b103aa31c6a0f1c5/ceraplas-db.pdf — 52 kHz、8 W、12 Vpp、最高 20 kV。
31. GlobeNewswire — TDK Introduces CeraPlas HF Compact Cold Plasma Generator Element（2018-11-13）— https://www.globenewswire.com/news-release/2018/11/13/1650541/0/en/TDK-Introduces-CeraPlas-HF-Compact-Cold-Plasma-Generator-Element.html — 上市日期與 47.3×20×20 mm 尺寸。
32. igus rbtx — piezobrush PZ3-i 作為機器人末端執行器 — https://rbtx.com/en-US/components/end-effectors/cold-plasma-device-improved-adhesion-ink-glue-relyon-plasma-piezobrush-pz3-i — 自動化整合的市場訊號。
33. STEMINC — Multilayer Piezo Transformer — https://www.steminc.com/PZT/en/multilayer-piezo-transformer — 現貨 PT（例 SMMTF55P4S80，55 kHz / 4 W）；**單層 50 kHz 2 W 級零售 USD 23.76 / 2 顆**（單價來源見 `01-pt-power-conversion-sota.md` S10）。
34. XP Power Q Series — https://www.xppower.com/product/Q-Series ；Digi-Key Q101-5 — https://azcus.digikey.com/en/products/detail/xp-power/Q101-5/5873625 — 10 kV / 0.5 W 磁性 HV 模組單價 **USD 420.06**，5 kV 版 0.125 in³（**壓電 vs 磁性在高壓域的成本對照基準**）。
35. TDK — PowerHap Actuators — https://product.tdk.com/en/products/sw_piezo/haptic/powerhap/index.html — 內建感測、≤25 N 壓力偵測、1 Hz–1000 Hz。
36. Boréas Technologies — BOS1901 Piezo Haptic Driver — https://www.boreas.ca/products/bos1901-piezo-haptic-driver — 「市場上唯一同時觸發觸覺並感測按壓力的壓電驅動 IC」。
37. Boréas — CapDrive Technology — https://www.boreas.ca/pages/capdrive-technology — 電流消耗最多降 90%、比競品壓電 IC 效率好 10×、比 LRA 省電 20×（**廠商宣稱，度量為電流消耗而非轉換效率**）。
38. PRNewswire — Boréas Technologies Announces Four-Channel Haptic Driver with Integrated Sensing（BOS0614, 2022）— https://www.prnewswire.com/news-releases/boreas-technologies-announces-four-channel-haptic-driver-with-integrated-sensing-301563047.html
39. GlobeNewswire — Boréas Technologies' Piezo Driver Chip Advances Realistic Haptic Feedback in Automotive HMIs（2020-01-07）— https://www.globenewswire.com/news-release/2020/01/07/1967204/0/en/Bor%C3%A9as-Technologies-Piezo-Driver-Chip-Advances-Realistic-Haptic-Feedback-in-Automotive-HMIs.html — 車用採用訊號。
40. Synaptics — Synaptics Partners with Boréas Technologies to Deliver High-Performance Piezo Haptic Trackpads — https://www.synaptics.com/company/news/synaptics-partners-boreas-technologies-deliver-high-performance-piezo-haptic-trackpads — 大廠採用訊號。
41. EDOM 益登科技 — BOS1921 CapDrive Piezo Driver — https://www.edomtech.com/en/product-detail/bos1921-capdrive-piezo-driver/ ；BOS1901 — https://www.edomtech.com/en/product-detail/bos1901-piezo-haptic-driver/ — **台灣取樣管道，本文件對客戶最具可執行性的單一連結**。
42. xMEMS — Cypress 量產就緒新聞稿 — https://xmems.com/press-release/xmems-announces-mass-production-readiness-of-cypress-the-worlds-first-full-range-mems-speaker-for-wireless-earbuds/ — sound-from-ultrasound 調變／解調同體、>130 dB SPL。
43. audioXpress — xMEMS Skyline 固態 MEMS DynamicVent — https://audioxpress.com/news/xmems-announces-world-s-first-solid-state-mems-dynamicvent-enabling-active-ambient-control-for-next-generation-tws-and-hearing-aids — 1.1 mm² 等效開孔、100 Hz 衰減 25 dB。
44. Yole — Qualcomm 3D Sonic Sensor Fingerprint 樣本報告 — https://medias.yolegroup.com/uploads/2019/07/SP19465-YOLE_Qualcomm-3D-Sonic-Sensor-Fingerprint_Sample.pdf — 24×8 PMUT 陣列、180 nm CMOS。**（注意：這是拆解樣本報告，不是市場規模報告。）**
45. Ventiva — 技術頁 https://ventiva.com/technology/ ；BusinessWire https://www.businesswire.com/news/home/20250518248653/en/Ventiva-Unveils-Intelligent-Air-Cooling-Solution-for-Electronics-that-Delivers-Up-To-100-Watts ；PCWorld https://www.pcworld.com/article/2570821/ventivas-fanless-laptop-cooler-wins-intel-and-dell-over.html — ICE9 固態 EHD 散熱、Lunar Lake 移除約 25 W、上看 100 W、<15 dBA、釋放最多 40% 板面積、Intel/Dell 關注。**融資輪次與電極工作電壓查無。**

### 供應鏈與代工

46. Silex Microsystems / SINTEF（經 imec / Europractice MPB）/ imec / Fraunhofer ISIT / Rogue Valley Microdevices / I-PEX / ROHM 的 piezoMEMS 代工能力 — 轉引自 `03-materials-manufacturing.md` 來源 [52]–[56]，該 dossier 對部分項目**未列獨立 URL**；SINTEF MPB 每批 3–12 片 6 吋晶圓為**對台灣團隊成本最低的驗證切入口**。

### 法規

47. CIRS Group — EU RoHS Directive Update: Comprehensive Refinement of Lead Exemption Clauses — https://www.cirs-group.com/en/chemicals/eu-rohs-directive-update-comprehensive-refinement-of-lead-exemption-clauses — 2025-09-08 通過三項授權指令；新增 7(c)-V、7(c)-VI；**7(c)-VI 涵蓋 PZT，豁免至 2027-12-31**。
48. Assent — Final Delegated Directives for Key RoHS Lead Exemptions Adopted — https://www.assent.com/blog/draft-expiry-dates-for-key-rohs-lead-exemptions-published/ — **續期申請須期滿前 18 個月提出（即 2026-06-30 前，該日已過，是否有人提出查無）**。
49. TÜV SÜD — EU comprehensive updates to lead exemptions under RoHS directive — https://www.tuvsud.com/en/knowledge-hub/technical-updates/consumer-products-and-retail-essentials/eu-comprehensive-updates-to-lead-exemptions-under-rohs-directive — 成員國轉置期限 2026-06-30、2026-07-01 生效。

---

**本文件的一句話使用說明**：把它當作「資金地圖的骨架」而不是「市場報告」。骨架是可信的（併購金額、政府補助、有無新創、產品有無在賣、單價對照），血肉（市場規模數字）是不可信的。**下一輪最有價值的動作不是再搜尋，而是打第 6 節列出的那三通電話。**
