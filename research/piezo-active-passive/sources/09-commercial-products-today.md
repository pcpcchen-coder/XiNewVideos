# 現有商品化產品盤點：已經在賣的壓電「兩用/非電感」產品與價格

> 一句話結論：**「今天真的買得到」的壓電兩用元件只有三小類**——TDK CeraPlas／relyon piezobrush（冷電漿，元件即高壓源即電極）、Boréas CapDrive 觸覺驅動 IC 家族（同一片壓電同時致動＋感測）、以及 STEMINC 等零售級 Rosen 型壓電變壓器（唯一有公開價格的錨點，**USD 11.88／顆，2 W 級**）；而**整個領域的價格資料幾乎全部不透明**，這本身就是本輪盡職調查最重要的發現：在拿不到 TDK／relyon／Boréas 報價之前，「壓電太貴」與「壓電夠便宜」兩種說法都無法被證實或證偽。

---

## 0. 研究方法與限制（誠實揭露，請務必先讀）

**本輪執行完成度不足，必須明講：**

1. **本輪 WebSearch 次數 = 0（有效查詢 0 次）。** 我送出的第一組查詢（TDK CeraPlas HF `Z63000Z2910Z` 規格、relyon piezobrush PZ3 價格）即被系統回覆 `this session has used its web search budget (200 of 200 WebSearch calls)`。本 session 的 200 次搜尋額度由同批多個研究 agent 共用，在我啟動時已被用盡。**原訂 25–35 次查詢計畫完全未執行。**
2. **WebFetch 在本環境被 egress policy 全面封鎖**（任何 URL 回 403），無法用抓網頁替代搜尋。
3. **因此本文件的性質是「二次彙整（secondary synthesis）」，不是一手檢索報告。** 全部內容來自同一研究專案中其他 agent 已完成、已附 URL 的 11 份 dossier（同目錄 `01/02/03/04/06/07/10/11/15/16/21`）。**我沒有親自打開過任何一個 URL，也沒有親自執行過任何一次搜尋。**
4. **標記規則**：
   - `【轉引】` = 來自同目錄某份 dossier，該 dossier 標示為已由搜尋摘要取得，並附有原始 URL（第 7 節可追）。
   - `【未驗證】` = 原 dossier 自己就標了未驗證（僅單一搜尋摘要、無法交叉比對）。
   - `【查無】` = 已有 agent 查過但沒查到。
   - `【本輪未查】` = 本專案至今**沒有任何 agent 查過**，不可當成「不存在」。
5. **明確未涵蓋的指派項目（額度歸零導致，請下一輪優先補）**：
   - (b) 壓電式離子產生器／負離子／臭氧模組的**具體型號與價格** →【查無＋本輪未查】（只查到 SMC 的專利，沒查到在售型號）。
   - (d) 壓電馬達／致動器（PI、Nanomotion、PiezoMotor、Xeryon、TDK）的**價格級距** →【本輪未查】，一個數字都沒有。
   - (e) xMEMS **Sycamore／XMC-2400 超音波氣泵**、**TDK PiezoListen**、**Murata 壓電喇叭** →【本輪未查】；Boréas 各型號的**輸出電壓／電流／封裝／單價** →【查無】。
   - (f) 超音波無線供電**商用模組／穿金屬供電產品** →【查無】，且已有 agent 明確查過並回報「2026 年仍無任何具名商用產品或 ATEX/IECEx 認證方案」。
   - (g) Bartels mp6／TTP Ventus (Lee Ventus) Disc Pump／Murata microblower MZB 的**價格** →【本輪未查】；只有 Bartels 的壽命規格。
   - CCFL 時代的 Tamura／Sumida／Murata PT 型號與停產時點 →【本輪未查】。
   - TI／ON Semi／Microchip 是否有 PT 或壓電驅動 IC →【本輪未查】（21 號 dossier 明列此為下一輪第一優先）。
6. **本文件未捏造任何型號、專利號、公司名或數字。** 凡我沒有來源的，一律寫「查無」或「本輪未查」，不做推測性補齊。

---

## 1. 結論摘要

1. **全領域唯一一個可公開查得的壓電變壓器單價：STEMINC `SMSTF50P2S6`（單層，50 kHz，2 W 級），零售 USD 23.76／2 顆 ≈ USD 11.88／顆**（小量零售價，非量產價）。這是整份研究中唯一的硬價格錨點。【轉引 D01-S10】
2. **同一供應商的多層 PT 有型號但無價格**：`SMMTF55P4S80`（55 kHz／4 W）、`SMMTF55P6S50`（55 kHz／6 W）。頁面價格未被搜尋摘要回傳。【轉引 D01-S11、D06-56】
3. **TDK CeraPlas 是本領域唯一有大廠背書的量產元件，但單價至今零揭露。** 已有兩份 dossier 分別查過 Mouser 與 DigiKey 產品頁，**都證實可購買、都查不到價格**。【轉引 D10-7、D10-8、D07-5】
4. **CeraPlas 的電氣規格是清楚的**：CeraPlas F 尺寸 72 × 6 × 2.8 mm、約 8 g、共振約 50 kHz、輸入 12–24 V、輸出 < 15 kV、升壓比 > 1000、最大工作功率 8.0 W【未驗證】；封裝版 CeraPlas HF 為 47.3 × 20 × 20 mm 塑膠外殼、可焊接引腳、電漿溫度 < 50 °C，實驗樣品料號 **Z63000Z2910Z 1Z60**、評估套件 **1Z61**，2018-11-13 發表上市。【轉引 D10-4/5/51】
5. **評估套件的實際工作點比 datasheet 保守**：key-components 的 CeraPlas HF Evaluation Kit 描述為 **24 V 單電源、預設約 4.5 W、可選 2–7 W**——比「最大 8 W」低一截，這是做功率預算時該用的數字。【轉引 D07-8】
6. **系統級產品也已上市多年但同樣無公開價格**：relyon **piezobrush PZ3** 手持機（整機最大 18 W、電漿 < 50 °C、五種可換模組、處理速率數 cm²/s 量級）、**PZ3-i** 自動化版（平均處理寬度 5–29 mm，需壓縮乾燥空氣 CDA）。前代 **PZ2 於 2014 年為首個產品、2021-11-30 停產**。【轉引 D10-10/11/12/13、D07-2】
7. **最重要的商業訊號是負面的**：TDK 子公司 EPCOS 2018 年取得 relyon plasma 50.2% 股權；**2026-03-04 Viromed Medical AG 簽 LOI 收購，2026-07-27 完成盡職調查，價格區間為「低至中雙位數百萬歐元」**。大廠八年後選擇退場，且對價只有數千萬歐元級。【轉引 D10-27/28/29】
8. **競品價格錨點（非壓電）比壓電貴得多**：XP Power／EMCO **Q101-5**（10 kV／0.5 W 灌封高壓模組，輸入 5/12/15/24 V）在 Digi-Key 單價 **USD 420.06**。這證明「壓電單價高」的論證在**高壓源市場完全不成立**——CeraPlas 的對手是幾百美元的模組，不是幾分錢的電感。【轉引 D11-15】
9. **驅動 IC 端有現貨、台灣有代理，但規格與價格全部拿不到**：Boréas **BOS1901／BOS1921／BOS1931**（CapDrive 單通道）、**BOS0614**（四通道整合感測，2022）；Mouser 有 BOS1931 產品頁；**益登科技（EDOM）已代理 BOS1901/BOS1921**，取得評估樣品與 FAE 支援的路徑在台灣是通的。但已有 agent 明講「未能取得任何一顆的實際輸出電壓、輸出電流、靜態功耗、封裝與單價」。【轉引 D21-S3b/S3d/S3f、D02-4/6】

---

## 2. 現況：技術 / 產品 / 玩家

### 2.1 (a) 壓電變壓器元件與供應鏈

**在售、有型號、可零售購買的**只有 STEMINC（Steiner & Martins，美國）一家被明確驗證：單層 `SMSTF50P2S6`（50 kHz／2 W 級）與多層 `SMMTF55P4S80`（55 kHz／4 W）、`SMMTF55P6S50`（55 kHz／6 W）。STEMINC 另宣稱其 PZT 壓電變壓器「豁免於 RoHS」——**此為供應商說法，未經法規原文查證**。【轉引 D01-S10/S11、D06-56、D06-176】

**產業結構的關鍵事實：PT 產業經歷過一次崩塌。** CCFL 背光被 LED 取代後，多數主要 PT 供應商已停止高壓 PT 的大量生產。現存被點名的供應商包括 STEMINC、**TAMURA**、**Nihon Ceratec**（宣稱升壓比 > 80、效率 > 90%）、**Face International**，以及**台灣的 ELECERAM TECHNOLOGY（多層 PT 與 CCFL 逆變器）**。【轉引 D11-18/19】

> **對台灣客戶的意義**：供應鏈薄，但**在地有玩家**（ELECERAM）。這是本盤點中對「能否在台灣取得 pilot 產能」最直接的線索。ELECERAM 目前是否仍在生產、良率與單價區間為何，**本輪查無**。

**CCFL 時代的 Tamura／Sumida／Murata 具體 PT 型號、上市與停產年份：【本輪未查】。**

**TI／ON Semi／Microchip 是否有 PT 專用或壓電驅動 IC：【本輪未查】。** 21 號 dossier 已把「TI DRV2667／DRV8662、ST、Microchip 高壓驅動 IC 的實際架構、輸出電壓/電流、效率與單價」列為下一輪第一優先，並註明「這直接決定現貨能不能用的 go/no-go」。

### 2.2 (c) 冷電漿：本領域唯一真正量產、且已有完整通路的兩用元件

這是整個「壓電主動／被動兩用」命題中 **TRL 最高（8–9）** 的一支：單一片 PZT 同時是機械共振器（被動儲能）、升壓變壓器（被動）與放電電極（主動）。

**元件層（TDK Electronics，前 EPCOS）**

| 型號 | 定位 | 已知規格 |
|---|---|---|
| CeraPlas F | 裸陶瓷元件（OEM 內建） | 72 × 6 × 2.8 mm、8 g、~50 kHz、12–24 V in、< 15 kV out、8.0 W max【未驗證】 |
| CeraPlas HF | 塑膠封裝、可焊接引腳 | 47.3 × 20 × 20 mm；電漿 < 50 °C；訂購碼 Z63000Z2910Z 1Z60 |
| CeraPlas HF Evaluation Kit | 評估套件 | 訂購碼 1Z61；24 V 單電源；預設 ~4.5 W、可選 2–7 W |
| CeraPlas ExploreKit（EK1250101 系列） | 乾式消毒開發套件 | 含過濾延伸單元＋Android App 可自訂消毒流程 |

結構已驗證：**多層 Rosen 型**，輸入側為多層結構、**內電極為銅**（可與硬質 PZT 共燒），輸出側為單體（monolithic），於 TDK 奧地利 Deutschlandsberg 陶瓷元件能力中心開發。**銅電極這點很重要**——它代表壓電元件的成本並非鎖死在貴金屬電極上，但這條 know-how 在 TDK 手上。【轉引 D07-48、D06-174】

> **一個必須釐清的規格矛盾**：不同來源分別寫「< 15 kV」與「12–24 Vpp → 最高 20 kV」。兩者不一致，**採信前務必以 TDK 原始 datasheet（`ceraplas-db.pdf`）為準**。【轉引 D10-5 vs D21-27】

**上市年份**：CeraPlas HF 於 **2018-11-13** 由 GlobeNewswire 發布上市；系統端首個產品 **piezobrush PZ2 為 2014 年**。【轉引 D07-6、D07-2】

**通路**：Mouser（EU／IN 站均有產品頁）、DigiKey 產品重點頁、Texim Europe、key-components、Sekorm（中國轉載，另列 `Z63000Z2910Z 1Z68` 為 F series packaged component）。**通路確實存在，但兩份 dossier 分頭查價都失敗——搜尋摘要不含價格。**【轉引 D10-7/8/45/46、D07-5】

**系統層（relyon plasma GmbH，Regensburg，TDK 子公司）**

- **piezobrush PZ3**：手持機，PDD® 為註冊技術名稱，核心即 CeraPlas F；整機最大 18 W、< 50 °C、五種可換模組（Standard／Nearfield／Needle／Nearfield Needle／Multigas）；處理速率數 cm²/s 量級。
- **piezobrush PZ3-i**：自動化整合版，可掛機器人手臂當末端執行器，**已上架 igus rbtx 機器人零組件平台**；平均處理寬度 5–29 mm（需 CDA）。
- **通路（已具名）**：英國 Intertronics、澳洲 Nano Vacuum、Ulbrich Group、Axend；**牙科通路 Chairside Solutions 販售 PZ3 Professional Set**；relyon 自營線上商店亦販售 Professional Set。
- **已具名客戶**：PIL Sensoren GmbH（提升黏合品質）、Kunststoff-Zentrum SKZ（把 piezobrush 納入表面前處理服務組合）。
- **售價：【查無】**——這是本輪最刺眼的缺口，因為 relyon 自己就有線上商店，理論上價格應該是公開的。

**競品陣營（皆非壓電）**：歐洲三款取得 CE 醫材認證的冷電漿裝置——PlasmaDerm VU-2010（CINOGY）、kINPen MED（INP Greifswald／neoplas，Class IIa，2013 上市）、SteriPlas（Adtec）——**沒有一款是壓電式**。壓電式在醫材法規路徑上仍是 0 分。**plasmatreat、terraplasma medical 的具體型號與價格：【本輪未查】。**【轉引 D10-21/22/23】

### 2.3 (e) 觸覺與 MEMS 聲學：有現貨、有大廠採用，但無價格

| 廠商 | 產品 | 已驗證規格 | 價格 |
|---|---|---|---|
| Boréas Technologies（加拿大） | BOS1901 / BOS1921 / BOS1931（CapDrive 單通道）、BOS0614（四通道，2022 發表，整合感測） | 廠商宣稱：能量回收使系統整體**電流消耗最多降 90%**、較競品壓電驅動 IC 效率好 **10×**、比 LRA 省電 **20×**；BOS1901 宣稱為「市場上唯一同時觸發觸覺並感測按壓力的壓電驅動 IC」 | 【查無】 |
| TDK | PowerHap 致動器（如 `1204H018V060`） | 壓力偵測 ≤ 25 N；激振 1 Hz–1000 Hz | 【查無】 |
| xMEMS | Cypress（全音域 MEMS 喇叭，sound-from-ultrasound，宣布量產就緒） | 低頻 SPL **> 130 dB** | 【本輪未查】 |
| xMEMS | Skyline DynamicVent（固態 MEMS 閥） | 開孔等效 **1.1 mm²**（雙顆 1.3 mm²）；100 Hz 衰減 **up to 25 dB** | 【本輪未查】 |
| xMEMS | Sycamore／XMC-2400 超音波氣泵 | 【本輪未查】 | 【本輪未查】 |
| TDK PiezoListen／Murata 壓電喇叭 | 【本輪未查】 | 【本輪未查】 | 【本輪未查】 |

**度量陷阱警告（原 dossier 明列，我照抄）**：Boréas 的「電流消耗降 90%」是**系統層級平均電流**，不是轉換效率，不能拿來當效率報給客戶；學術界同類「損耗降低 49–55%」與它不是同一個度量。【轉引 D21-26/86】

**採用訊號**：Synaptics 與 Boréas 合作壓電觸控板（大廠採用）；Boréas 有車用 HMI 專稿（2020 GlobeNewswire）。**是否已有量產機種：【查無】。**【轉引 D02-7、D21-S3g】

### 2.4 (b) 離子產生器 / (f) 超音波供電 / (g) 微泵：三塊幾乎空白

- **(b) 離子產生器**：只查到**專利**——`US7821762B2`／`US20090135538A1`／`CN101442871B`「Piezoelectric transformer type ionizer and neutralization method」，來源指出 2008 年讓與 **SMC Corporation**（號碼與標題已驗證，讓與細節未獨立驗證），日本同族 `JP2009129673A`。市場玩家列出 Simco-Ion、Panasonic、KEYENCE、KASUGA DENKI、OMRON、Fraser、SMC、NRD，**但原 dossier 明確警告：無法確認這些公司的現售型號是否真的採用壓電變壓器，多數靜電消除器仍用傳統高壓模組。** 空清機／汽車負離子模組的型號與價格：**【本輪未查】**。【轉引 D07-55/56、D06-67】
- **(f) 超音波無線供電／穿金屬供電**：**已有 agent 專門查過，結論是「2026 年仍查無任何具名商用產品或 ATEX/IECEx 認證方案」**——搜尋結果全是論文與專利。技術實測數字很漂亮（RPI Lawry：63.5 mm 實心鋼塊上同時傳 **50 W ＋ 12.4 Mb/s**；另有 1.045 MHz／11 mm 鋼壁／效率 60%；40 mm 不鏽鋼／15.7 W 穩壓 DC／整體效率 27.7%），但**沒有一個可以買**。醫療端最接近商業化的是超音波供電植入物（UC Berkeley → **Iota Biosciences → Astellas 2020 收購，頭期 1.275 億 USD ＋ 里程碑最高 1.765 億，合計約 3.04 億**；2024 年取得膀胱刺激的 FDA IDE 早期可行性試驗核准）。**EBR Systems WiSE-CRT 完全未查，不得引用。**【轉引 D16-14/26/169、D07-12/101】
- **(g) 壓電微泵**：只取得 **Bartels Mikrotechnik mp6 系列壽命 > 5,000 h**、**BP7 壽命 5,000 h**（無移動閥件、unibody 結構）。**TTP Ventus／Lee Ventus Disc Pump 的 MTBF：【查無】**；Murata microblower MZB：**【本輪未查】**；三者價格全部**【本輪未查】**。【轉引 D04-S35/S36/14】

### 2.5 (d) 壓電馬達／致動器：只有可靠度線索，沒有價格

- Nanomotion（HR 系列）、PiezoMotor（PiezoLEGS）的**官方壽命規格：【查無】**；只拿到 Physik Instrumente PILine 的數字。**價格級距完全【本輪未查】。**【轉引 D04-13】
- 已驗證的應用事實：壓電超音波馬達是 **MRI 導引介入機器人的事實標準**（相對於氣壓致動），Nanomotion／PI PILine 為代表；但 Nanomotion 運轉中會造成中度 SNR 損失、干擾 RF 場產生 zipper 偽影。【轉引 D15-S21】
- **重要反證**：Physik Instrumente 的高階奈米定位**仍採用外部電容式 direct metrology，而非自感測**。這是對「同一顆元件既致動又感測」最強的商業反證。【轉引 D21-173】

---

## 3. 關鍵數字表

| 項目 | 數值 | 年份／狀態 | 可信度 | 出處 |
|---|---|---|---|---|
| **STEMINC `SMSTF50P2S6` 單層 PT（50 kHz／2 W 級）零售價** | **USD 23.76／2 顆 ≈ USD 11.88／顆** | 現行 | 中高（唯一硬價格） | D01-S10 |
| STEMINC 多層 PT `SMMTF55P4S80`（4 W）／`SMMTF55P6S50`（6 W）價格 | **查無** | — | — | D01-S11 |
| 同級電感／磁性變壓器單價（對照組） | **查無可驗證報價** | — | — | D01-S29 |
| **XP Power / EMCO `Q101-5`（10 kV／0.5 W 高壓模組）Digi-Key 單價** | **USD 420.06** | 現行 | 中高 | D11-15 |
| XP Power Q 系列體積 | 5 kV @ 0.125 in³；10 kV @ 0.614 in³；0.5 W；輸入 5/12/15/24 V | 現行 | 中 | D11-15 |
| CeraPlas F 尺寸／重量 | 72 × 6 × 2.8 mm ／ 8.0 g | 現行 | 【未驗證】 | D10-5/46 |
| CeraPlas F 最大工作功率 | 8.0 W | 現行 | 【未驗證】 | D10-5 |
| CeraPlas HF 尺寸 | 47.3 × 20 × 20 mm | 2018 上市 | 高 | D10-4/7、D07-6 |
| CeraPlas 輸入／輸出 | 12–24 V(pp) → < 15 kV（另一來源寫最高 20 kV，**矛盾**） | — | 中 | D10-5 / D21-27 |
| CeraPlas 升壓比 | > 1000 | — | 高（多來源） | D10-2/12 |
| CeraPlas HF 評估套件工作點 | 24 V 單電源、預設 ~4.5 W、可選 2–7 W | 現行 | 中 | D07-8 |
| CeraPlas 訂購碼 | HF 樣品 `Z63000Z2910Z 1Z60`；評估套件 `1Z61`；F packaged `…1Z68` | — | 中 | D10-4/46 |
| **CeraPlas 單價／壽命／MTBF／良率** | **查無（兩份 dossier 分頭查價皆失敗）** | — | — | D10-13、D07-89 |
| piezobrush PZ3 整機最大耗電 | 18 W | 現行 | 高 | D10-10/12 |
| piezobrush PZ3 電漿溫度 | < 50 °C | 現行 | 高 | D10-4/10/12 |
| piezobrush PZ3-i 平均處理寬度 | 5–29 mm（需 CDA） | 現行 | 中 | D10-11 |
| piezobrush PZ3 處理速率 | 數 cm²/s 量級 | 現行 | 中 | D10-12 |
| **piezobrush PZ3 售價** | **查無** | — | — | D10-16 |
| piezobrush PZ2 生命週期 | 2014 首個產品 → **2021-11-30 停產** | 已停產 | 高 | D07-2、D10-13 |
| PDD 陣列最小元件間距 | 4 cm（寄生耦合限制） | — | 中高 | D10-14/15 |
| TDK/EPCOS 取得 relyon 股權 | **50.2%**，2018 | 歷史 | 高 | D10-27 |
| **Viromed 收購 relyon 對價** | **低至中雙位數百萬歐元**（LOI 2026-03-04；DD 完成 2026-07-27） | 進行中 | 中 | D10-28/29 |
| TDK PowerHap 壓力偵測／激振 | ≤ 25 N ／ 1 Hz–1000 Hz | 現行 | 中 | D02-8 |
| Boréas CapDrive 宣稱 | 電流消耗最多 **−90%**；優於競品壓電 IC **10×**；優於 LRA **20×** | 廠商宣稱 | 低（未獨立驗證） | D21-S2/S3c、D02-5 |
| **Boréas 各型號輸出電壓／電流／封裝／單價** | **查無** | — | — | D21-52 |
| xMEMS Cypress 低頻 SPL | > 130 dB | 量產就緒 | 中 | D02-58 |
| xMEMS Skyline DynamicVent | 開孔等效 1.1 mm²；100 Hz 衰減 up to 25 dB | 發表 | 中 | D02-59 |
| Bartels mp6／BP7 微泵壽命 | **> 5,000 h ／ 5,000 h** | 現行 | 中高（廠商 datasheet） | D04-S35/S36 |
| 穿金屬壁供電＋通訊（實驗室） | 63.5 mm 鋼：**50 W ＋ 12.4 Mb/s**；11 mm 鋼：效率 60% | 實驗室 | 中 | D16-26、D03-72 |
| **穿金屬壁商用產品／型號／報價** | **不存在（已專門查過）** | 2026 | 高（負面結論） | D16-14/169 |
| Astellas 收購 Iota Biosciences | 頭期 **1.275 億 USD** ＋ 里程碑最高 1.765 億（合計 ~3.04 億），另 5 年 1.25 億投資 | 2020 | 高 | D07-12 |
| 壓電變壓器市場規模 | **各家互相矛盾達 3 倍**：USD 220.5M(2025)→465.8M(2033)@9.8%；~500M(2025)→950M(2033)@8%；0.57B(2023)→1.88B(2030)@20.5% | — | **低，不可作決策依據** | D02-88、D01-S29/S30 |
| 電感市場（對照） | USD 5.1B(2022) → 7.0B(2027) | — | 低 | D01-S29 |
| 冷電漿市場 | USD 2.4–3.3B(2025) → 5–12B(2032–2035)，CAGR 14–16%；常壓段佔 66% | — | 低（市調） | D10-30/31/32 |

---

## 4. 「新能力型」應用機會（從「今天已在賣什麼」倒推）

> 本節只放**由商品化現況直接推導出來**的機會；純學術機會由其他 dossier 負責。
> 非替代性判定：**是** = 以前物理上做不到；**半** = 以前能做但形態完全改變、開出新場景；**否** = 純粹更小更便宜的替代。

### 4.1 把「高壓源」從幾百美元的模組打成幾美元的陶瓷片 —— 低壓輸入高壓場產生器

- **新能力是什麼**：這是本盤點最硬的一條，而且是**由價格資料直接推導**出來的。Digi-Key 上 XP Power `Q101-5`（10 kV／0.5 W）要 **USD 420.06**；STEMINC 一顆 2 W 級 PT 零售只要 **USD 11.88**。兩者不是同一規格，但**量級差 35 倍**。這意味著在「需要 kV 級電場、但功率只有零點幾到幾瓦」的所有場合，壓電路線在成本上不是劣勢而是**壓倒性優勢**。
- **為什麼以前做不到**：傳統做法是繞線變壓器＋倍壓整流＋灌封＋安規爬電距離，體積與 BOM 都被鎖死在幾百美元、立方公分級。壓電把整個升壓段收進一片陶瓷，插拔面只剩 24 V 兩線。
- **是否真的非替代性**：**半到是**。「產生 10 kV」本身不新；但「10 kV 源便宜到可以每台設備放十顆、可以做成耗材、可以塞進消費品內部」是新的產品型態。
- **誰在做**：TDK CeraPlas（元件）；XP Power／EMCO 是被取代的對照組。
- **TRL**：**8–9**（元件已量產、Mouser／DigiKey 有貨）。
- **市場訊號**：通路完整、代理商網絡跨五國、牙科通路已在賣。
- **最大技術障礙**：**價格資料不透明**——若 CeraPlas 實際報價落在 USD 100+ 而非 USD 10 級，這整條論證會反轉。**這是本盤點對客戶最重要的一個「必須先問到答案的問題」。**

### 4.2 機器人末端執行器上的點狀、選擇性表面活化（唯一 TRL 9 的既有生意）

- **新能力是什麼**：< 20 W、< 50 °C、寬 5–29 mm 的電漿源直接裝在機械手臂上，只活化要塗膠的那一條膠道，可跟隨 3D 曲面、可進凹槽。
- **為什麼以前做不到**：電暈是大面積平面連續料捲製程；火焰有明火與熱負荷；常壓電漿噴射功率高、噴嘴重、需外部高壓產生器與冷卻。三者都做不到「幾瓦、幾十克、隨手臂走的一條 5 mm 線」。
- **是否真的非替代性**：**半**。活化本身不新，但選擇性／局部／低熱／輕量／可裝機器人是新的。
- **誰在做**：relyon piezobrush PZ3-i（已上架 igus rbtx）、Intertronics 主打自動化整合。
- **TRL**：**9（已商品化銷售中）**。
- **市場訊號**：具名客戶 PIL Sensoren、SKZ；多國代理商。
- **最大技術障礙**：處理速率只有數 cm²/s，客戶一要整片就輸給電暈；CDA 供氣需求削弱「純電池化」賣點。

### 4.3 「驅動即感測」的觸覺 IC：已被 Boréas 佔位，切入點在別的地方

- **新能力是什麼**：同一片壓電，主動端做觸覺致動、被動端做按壓力偵測，省掉外掛觸控感測器；CapDrive 再把致動器負載電容裡的能量回收再利用。
- **是否真的非替代性**：**否到半**。這本質是「省一顆感測器 + 省電」的替代型改良——**依客戶的方向限制，權重應調低**。
- **誰在做**：Boréas（BOS1901/1921/1931/0614）；TDK PowerHap 在元件端做同一件事；Synaptics 已合作。**台灣有 EDOM 代理，取樣路徑通。**
- **TRL**：**9**。
- **最大技術障礙**：(1) **CapDrive 的專利範圍未知**——若「從致動器負載電容回收能量」已被圈住，自研 IC 會直接撞牆（D21 已將此列為未解問題）；(2) 自感測的橋式電容失衡問題在最嚴苛應用被否決（PI 仍用外部電容式量測）。

### 4.4 「元件即耗材」：可拋棄式無菌一次性電漿頭

- **新能力是什麼**：高壓段就是一片幾克重的陶瓷，主機端只剩 24 V。第一次讓「把高壓源做成拋棄式耗材」在成本與安規上可行。
- **為什麼以前做不到**：傳統高壓源本身就是最貴、最重、最需安規認證的部分，不可能拋棄；高壓連接器插拔本身即失效與漏電風險點。
- **是否真的非替代性**：**是**（拓樸改變，不是尺寸縮小）。
- **誰在做**：**查無公開商品化案例**。TDK ExploreKit 是最接近的骨架；牙科通路已在賣 PZ3。
- **TRL**：3–4。
- **最大技術障礙**：**壽命數字完全查無**——一次性化反而讓「壽命短」從缺點變成特性，但必須先量化能撐多久才能定價。

### 4.5 明確標為「替代品」、應降權的方向（誠實揭露）

- **用 PT 做隔離閘極驅動**：對手是 ADI iCoupler（> 150 kV/µs）、Infineon 1ED3124（> 200 kV/µs）、Coilcraft HTX7045C（繞組間電容 0.75 pF、12 kV、5 W）——皆為成熟量產件。壓電既無性能跨越，單價又更高，且 PT 的數十 kHz 頻寬先天不足以支援 WBG 閘驅。**建議明確排除，理由與客戶排除「取代電感」完全同構。**【轉引 D16-158】
- **取代電暈滾輪機做料捲表面處理**：cm²/s vs 100+ m²/hr，**規模差 3–4 個數量級**。不要碰。
- **取代針尖式雙極離子產生器做空調除味**：模組成本極低、已大規模安裝，且該市場正因臭氧與功效爭議而信譽受損。

---

## 5. 反面證據、失敗案例與物理上限

1. **最強反面訊號：TDK 的八年與退場。** 2018 年 EPCOS 取得 relyon 50.2% 股權、密集出白皮書與產品；**2026 年 TDK 選擇把 relyon 賣給德國小型上市醫材公司 Viromed，對價僅「低至中雙位數百萬歐元」**。合理解讀：**CeraPlas 沒有找到任何一個能吃掉百萬顆／年的應用**，而元件廠的商業模式需要那個量。這必須放在客戶決策的最前面。【轉引 D10-27/28/29】
2. **PT 產業已經崩塌過一次。** CCFL → LED 之後多數領先供應商停止高壓 PT 大量生產：供應鏈薄、產能與良率經驗流失、單價高企。**這是「壓電太貴」論證的真實歷史根源**，不是臆測。【轉引 D11-18】
3. **穿金屬壁供電近 30 年零商品化。** 起源可追至 1997 年 Connor 專利，2011 年已有 50 W／12.4 Mb/s 的媒體級成果，2015 年已有完整綜述——**2026 年仍查無任何具名商用產品或 ATEX/IECEx 認證方案**。技術可行 ≠ 市場可行。【轉引 D16-169】
4. **消費品上的壓電兩用有明確失敗紀錄。** HEAD Intelligence 網球拍（self-powered piezoelectric damping）有專利、有 50% vs 20% 衰減宣稱，**結果停產，推測因成本**。另 SRI → Artificial Muscle Inc. → Bayer MaterialScience → ViviTouch 觸覺產品，跨越 15 年與一家化工巨頭，**今天市場上看不到**（結局未驗證，但也未顯示任何在售產品）。【轉引 D02-167、D11-167】
5. **業界最嚴苛應用否決自感測。** Physik Instrumente 的高階奈米定位仍用**外部電容式 direct metrology**；根本原因是橋式自感測的電容失衡（C₀ 隨溫度與偏壓漂移），一失衡就把致動訊號洩進感測路徑。**若客戶賣點是「省掉感測器」，這個案例必須先被回答。**【轉引 D21-173】
6. **物理上限（元件層）**：單顆 CeraPlas F 最大 8 W【未驗證】、PZ3 整機 18 W；Rosen 型 PT 受機械應力極限與自發熱／Q 值下降雙重限制，且自發熱會拉動共振點形成正回饋失控風險。陣列化又被 4 cm 最小間距（寄生耦合）鎖死，面功率密度約 0.5 W/cm² 量級【推論】。**靠單顆或陣列放大功率在物理上是死路。**【轉引 D10-185/186】
7. **共振頻率漂移是全領域共同罩門，而且有專利證據。** TDK 自己佈了 `US11903321`（場強探針回授找最大場強）、`US10772182`（頻率控制法）、`WO2021122995A1`（操作方法）——**如果諧振點穩定，就不需要三個專利族來追它。**【轉引 D07-173】
8. **含鉛與 RoHS 豁免。** STEMINC 宣稱 PZT PT「豁免於 RoHS」，但**豁免是有審查期限的政策，不是永久權利**。把長週期產品（車用、工業、醫療接觸）押在 PZT 上有法規風險。【轉引 D06-176】
9. **市場規模數字不可用。** 壓電變壓器市場的三份報告彼此相差達 3 倍（220.5M / 500M / 570M），年份與 CAGR 都不一致。**不應作為投資依據**，只能當「有人在賣這個題目的報告」的弱訊號。【轉引 D02-177】

---

## 6. 未解問題（給下一輪研究，已按優先序排列）

1. **【最高優先】直接詢價，不要再靠搜尋。** 本輪最大結論是「價格資料不存在於公開網路」。建議直接發詢價信：
   - TDK Electronics / Mouser / DigiKey / Texim Europe / key-components：**CeraPlas F 與 HF 的 1k / 10k / 100k 階梯價**，並索取 reliability report（MTBF、連續放電時數、輸出電壓衰退曲線）。
   - relyon plasma 線上商店：**piezobrush PZ3 Professional Set 標價**（該店應有公開價格，只是搜尋摘要沒帶出來）。
   - STEMINC、TDK、富士セラミックス、CTS／Noliac、APC International：**量產級 PT 單價**。
   - **ELECERAM TECHNOLOGY（台灣）**：是否仍生產多層 PT、pilot 產能、良率與單價區間。**這是決定客戶能否在本地做 PoC 的關鍵。**
2. **本輪額度歸零而完全未查的清單（原樣照抄，供下一輪直接執行）**：(b) 壓電式離子產生器／負離子／臭氧模組的在售型號與價格；(d) PI／Nanomotion／PiezoMotor／Xeryon／TDK 壓電馬達價格級距；(e) xMEMS Sycamore／XMC-2400、TDK PiezoListen、Murata 壓電喇叭規格與價格，Boréas 各型號 datasheet 與單價；(f) 超音波供電商用模組、EBR Systems WiSE-CRT（**完全未查，勿引用**）；(g) Bartels mp6 / Lee Ventus Disc Pump / Murata MZB 價格；CCFL 時代 Tamura／Sumida／Murata PT 型號與停產年；TI DRV2667／DRV8662、ON Semi、Microchip 壓電驅動 IC 的架構、輸出規格與單價。
3. **CeraPlas 輸出電壓的規格矛盾（< 15 kV vs 最高 20 kV）必須以原始 datasheet 釐清。**
4. **Viromed × relyon 交易的後續**：交割是否完成、Viromed 要推哪一條醫材適應症、是否取得 CE Class IIa。**這是未來 12 個月內最能證實或證偽本領域的單一事件。**
5. **Boréas CapDrive 的專利範圍**：若「從致動器負載電容回收能量」已被圈死，客戶自研驅動 IC 會直接撞牆。建議以 Boréas Technologies 為受讓人做專利檢索。

---

## 7. 來源清單

> **重要說明**：以下 URL **全部由本專案其他 agent 在其 dossier 中檢索取得並附上**，本輪我沒有親自開啟或驗證任何一個（WebFetch 被封鎖、WebSearch 額度為 0）。編號後的 `[Dxx]` 標示該 URL 出自同目錄哪一份 dossier，便於追溯原始標註（含各自的「未驗證」標記）。

### 7.1 價格與型號錨點

1. STEMINC — Single Layer Piezo Electric Transformer 50 kHz (`SMSTF50P2S6`)。**零售 USD 23.76 / 2 顆 ≈ USD 11.88/顆**。 [D01] https://www.steminc.com/PZT/en/single-layer-piezo-electric-transformer-50-khz
2. STEMINC — Multilayer Piezo Transformer 55 kHz 4 W (`SMMTF55P4S80`)。多層 PT 產品線；價格未取得；PZT PT「豁免於 RoHS」之供應商說法（未驗證）。 [D01/D06] https://www.steminc.com/PZT/en/multilayer-piezo-transformer
3. XP Power Q Series 產品頁 — 5 kV @ 0.125 in³、10 kV @ 0.614 in³、0.5 W、輸入 5/12/15/24 V。 [D11] https://www.xppower.com/product/Q-Series
4. Digi-Key — XP Power `Q101-5`（10 kV / 0.5 W）**單價 USD 420.06**。非壓電高壓模組的價格對照組。 [D11] https://azcus.digikey.com/en/products/detail/xp-power/Q101-5/5873625

### 7.2 TDK CeraPlas（元件層）

5. TDK 新聞稿 — Compact CeraPlas HF element for cold plasma。HF 尺寸 47.3×20×20 mm、<50 °C、料號。 [D10] https://www.tdk-electronics.tdk.com/en/373388/company/press-center/press-releases/press-releases/plasma-generators-compact-ceraplas-hf-element-for-cold-plasma/2435688
6. TDK CeraPlas datasheet PDF（原 agent 未能開啟，僅見搜尋摘要）。CeraPlas F 尺寸、8 W、50 kHz、<15 kV。 [D10] https://www.tdk-electronics.tdk.com/download/2307712/39eb3392c71d1191b103aa31c6a0f1c5/ceraplas-db.pdf
7. TDK 技術文章 — Cold plasma from a single component。多層 Rosen 型、硬 PZT 共燒銅內電極、piezobrush PZ2（2014）為首個產品。 [D10/D07/D02] https://www.tdk-electronics.tdk.com/en/373562/tech-library/articles/applications-cases/applications-cases/cold-plasma-from-a-single-component/1109546
8. GlobeNewswire — TDK Introduces CeraPlas HF Compact Cold Plasma Generator Element（**2018-11-13 上市日期**）。 [D10/D07] https://www.globenewswire.com/news-release/2018/11/13/1650541/0/en/TDK-Introduces-CeraPlas-HF-Compact-Cold-Plasma-Generator-Element.html
9. key-components — EPCOS/TDK CeraPlas HF Evaluation Kit。**24 V 單電源、預設 ~4.5 W、可選 2–7 W**。 [D07] https://www.key-components.com/news/epcos-tdk-ceraplas-hf-evaluation-kit.html
10. TDK — CeraPlas ExploreKit for decontamination（含過濾單元、Android App）。 [D10] https://www.tdk-electronics.tdk.com/en/2910748/products/product-catalog/cold-plasma-technology/ceraplas-explorekit
11. Mouser（EU）— CeraPlas HF 產品頁。通路可得性；**搜尋摘要未見價格**。 [D10] https://eu.mouser.com/new/epcos/epcos-ceraplas-hf/
12. Mouser（IN）— CeraPlas HF Piezoelectric Plasma Generator。同上，證明實際可購買。 [D07] https://www.mouser.in/new/epcos/epcos-ceraplas-hf/
13. DigiKey — CeraPlas 產品重點頁。通路可得性；**未見價格**。 [D10] https://www.digikey.com/en/product-highlight/e/epcos/compact-ceraplas-for-cold-plasma-technology
14. Sekorm — CeraPlas Element 初步資料（`Z63000Z2910Z 1Z68`，F series packaged component）。第三方轉載規格頁。 [D10] https://en.sekorm.com/doc/2581106.html
15. Texim Europe — Cold atmospheric pressure plasma promises decisive benefits（PDF）。通路商技術文件。 [D10] https://www.texim-europe.com/getfile.ashx?id=113097
16. TDK — Cold Plasma's Potential: Revolutionizing Forefront Medical Care。12–24 Vpp / 50 kHz / <50 °C。 [D07] https://www.tdk.com/en/featured_stories/entry_041.html

### 7.3 relyon plasma（系統層）與通路

17. relyon plasma — piezobrush PZ3 產品頁。**18 W、<50 °C、五種模組**。 [D10] https://www.relyon-plasma.com/piezobrush-pz3/?lang=en
18. relyon plasma — piezobrush PZ3-i 頁。自動化整合版、**處理寬度 5–29 mm（CDA）**。 [D10] https://www.relyon-plasma.com/piezobrush-pz3-i/?lang=en
19. Korzec et al. — piezobrush PZ3 Part I: Operation Principle and Characteristics（白皮書 PDF）。**處理速率數 cm²/s**。 [D10] https://www.relyon-plasma.com/wp-content/uploads/2024/02/201024_whitepaper_piezobrush_PZ3_1.pdf
20. relyon plasma — piezobrush PZ2 頁。**2021-11-30 停產**，由 PZ3 接替。 [D10] https://www.relyon-plasma.com/relyon-plasma-products/piezobrush-pz2/?lang=en
21. relyon plasma 線上商店 — piezobrush PZ3 Professional Set。**下一輪應直接在此取價**。 [D10] https://www.relyon-plasma.com/produkt/piezobrush-pz3-professional-set/?lang=en
22. Intertronics（UK）— PiezoBrush PZ3 產品頁。英國通路。 [D10] https://intertronics.co.uk/product/piezobrush-pz3-handheld-plasma-surface-treatment/
23. Chairside Solutions — relyon plasma piezobrush PZ3 Professional Set。**牙科通路已在銷售的證據**。 [D10] https://www.chairsidesolutions.com/shop/p/relyonplasmapiezobrush
24. igus rbtx — piezobrush PZ3-i 作為機器人末端執行器上架。自動化整合市場訊號。 [D10] https://rbtx.com/en-US/components/end-effectors/cold-plasma-device-improved-adhesion-ink-glue-relyon-plasma-piezobrush-pz3-i
25. Ulbrich Group — piezobrush PZ3「世界最小電漿手持機」。通路行銷語言。 [D10] https://www.ulbrich-group.com/piezobrush-pz3-the-world-s-smallest-plasma-handheld-device

### 7.4 併購與商業訊號

26. TDK 新聞稿 — EPCOS acquires majority stake in relyon plasma（**50.2%，2018**）。 [D10] https://www.tdk-electronics.tdk.com/en/373388/company/press-center/press-releases/press-releases/tdk-subsidiary-epcos-acquires-majority-stake-in-relyon-plasma/2240584
27. EQS / TradingView — Viromed Medical AG signs LOI to acquire relyon plasma GmbH（**2026-03-04**）。 [D10] https://www.tradingview.com/news/eqs:f46067e6f094b:0-viromed-medical-ag-signs-letter-of-intent-to-acquire-relyon-plasma-gmbh-strategic-step-toward-integrated-platform-for-cold-plasma-technology/
28. Viromed Medical AG — Update on the planned acquisition of relyon plasma（**DD 於 2026-07-27 完成；對價低至中雙位數百萬歐元**）。 [D10] https://www.webdisclosure.com/press-release/viromed-medical-ag-etr-viromed-medical-ag-update-on-the-planned-acquisition-of-relyon-plasma-gmbh-IFaMLec9JBo
29. TDK × relyon plasma 合作新聞稿。產業化路徑與夥伴關係。 [D07] https://www.tdk-electronics.tdk.com/en/373388/company/press-center/press-releases/press-releases/piezo-transformers-and-plasma-generators-tdk-cooperates-with-relyon-plasma-to-develop-and-manufacture-cutting-edge-plasma-solutions/1416224

### 7.5 觸覺 / 驅動 IC / MEMS 聲學

30. Boréas Technologies — BOS1901 Piezo Haptic Driver 產品頁。「市場上唯一同時觸發觸覺並感測按壓力的壓電驅動 IC」。 [D02/D21] https://www.boreas.ca/products/bos1901-piezo-haptic-driver
31. Boréas — CapDrive Technology。從致動器負載電容回收能量；比 LRA 省電 20×、比競品壓電 IC 效率好 10×（廠商宣稱）。 [D02/D21] https://www.boreas.ca/pages/capdrive-technology
32. Boréas blog — The 6 Elements of a Quality Piezo Driver。「電流消耗降低最多 90%」宣稱出處。 [D21] https://pages.boreas.ca/blog/piezo-haptics/6-most-important-elements-to-look-for-in-a-piezo-driver
33. Mouser — Boréas `BOS1931` High-Efficiency Piezo Driver。**通路產品頁，可直接用於詢價**。 [D21] https://www.mouser.com/new/boreas-technologies/boreas-bos1931-piezo-haptic-driver/
34. EDOM（益登科技）— BOS1901 Piezo Haptic Driver。**台灣代理，取樣與 FAE 路徑通**。 [D21] https://www.edomtech.com/en/product-detail/bos1901-piezo-haptic-driver/
35. PRNewswire — Boréas 四通道整合感測驅動 IC（`BOS0614`, 2022）。 [D02/D21] https://www.prnewswire.com/news-releases/boreas-technologies-announces-four-channel-haptic-driver-with-integrated-sensing-301563047.html
36. Synaptics × Boréas 壓電觸控板合作新聞稿。大廠採用訊號。 [D02] https://www.synaptics.com/company/news/synaptics-partners-boreas-technologies-deliver-high-performance-piezo-haptic-trackpads
37. GlobeNewswire — Boréas Piezo Driver Chip Advances Realistic Haptic Feedback in Automotive HMIs（2020）。車用採用訊號。 [D21] https://www.globenewswire.com/news-release/2020/01/07/1967204/0/en/Bor%C3%A9as-Technologies-Piezo-Driver-Chip-Advances-Realistic-Haptic-Feedback-in-Automotive-HMIs.html
38. TDK — PowerHap Actuators 產品頁。壓力偵測 ≤25 N、激振 1 Hz–1000 Hz。 [D02] https://product.tdk.com/en/products/sw_piezo/haptic/powerhap/index.html
39. xMEMS — Cypress 量產就緒新聞稿。sound-from-ultrasound、低頻 SPL >130 dB。 [D02] https://xmems.com/press-release/xmems-announces-mass-production-readiness-of-cypress-the-worlds-first-full-range-mems-speaker-for-wireless-earbuds/
40. audioXpress — xMEMS Skyline 固態 MEMS DynamicVent。等效開孔 1.1 mm²、100 Hz 衰減 25 dB。 [D02] https://audioxpress.com/news/xmems-announces-world-s-first-solid-state-mems-dynamicvent-enabling-active-ambient-control-for-next-generation-tws-and-hearing-aids
41. Physik Instrumente — Capacitive Sensors。高階奈米定位仍用外部電容式 direct metrology（自感測的反面證據）。 [D02/D21] https://www.physikinstrumente.com/en/expertise/technology/sensor-technologies/capacitive-sensors

### 7.6 微泵 / 馬達 / 可靠度

42. Bartels Mikrotechnik — Datasheet mp6 micropumps series（PDF）。**壽命 > 5,000 h**。 [D04] https://bartels-mikrotechnik.de/wp-content/uploads/2025/06/Datasheet-mp6-series.pdf
43. Bartels Mikrotechnik — The Bartels Pump BP7。**壽命 5,000 h**。 [D04] https://bartels-mikrotechnik.de/product/the-bartels-pump-bp7-piezo-pump/
44. PMC2975551 — MRI Compatibility of Robot Actuation Techniques: A Comparative Study。Nanomotion 運轉造成中度 SNR 損失、zipper 偽影。 [D15] https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2975551/
45. CTS Corp — Typical Failures for Multilayer Actuators。多數失效為絕緣劣化短路、銀遷移、內電極邊緣應力集中。 [D04] https://www.ctscorp.com/Resources/Blog/Typical-Failures-for-Multilayer-Actuators
46. APC International — RoHS Exemption for Lead Updates。壓電廠商視角的鉛豁免解讀（行銷文件）。 [D03/D04] https://www.americanpiezo.com/blog/rohs-exemption-for-lead-update/

### 7.7 離子產生 / 超音波供電（僅專利與論文，無商品）

47. Google Patents — `US7821762B2` Piezoelectric transformer type ionizer and neutralization method。指出 2008 年讓與 SMC Corporation（讓與細節未獨立驗證）；同族 `CN101442871B`、`JP2009129673A`。 [D07/D06] https://patents.google.com/patent/US7821762B2/
48. Google Patents — `US20150049587A1` Full-duplex ultrasonic through-wall communication and power delivery system with frequency tracking。 [D07/D06/D02] https://patents.google.com/patent/US20150049587
49. MDPI Applied Sciences 8(5), 692 — An Ultrasonic Through-Metal-Wall Power Transfer System with Regulated DC Output。1.045 MHz / 60%、乾耦合 34%、>100 W 實驗室展示。 [D07/D01] https://www.mdpi.com/2076-3417/8/5/692
50. New Atlas — Ultrasonic data and power transmission through metal（RPI Lawry，63.5 mm 鋼、50 W + 12.4 Mb/s）。 [D16] https://newatlas.com/ultrasonic-data-and-power-transmission-through-metal/18097/
51. Ultrasonics (2024) — Portable through-metal ultrasonic power transfer using a dry-coupled detachable transmitter（Stevens Institute）。針對耦合劑問題的乾耦合解法。 [D16] https://www.sciencedirect.com/science/article/abs/pii/S0041624X2400101X

### 7.8 市場規模（低可信度，僅供參考，不可作決策依據）

52. Precedence Research — Cold Plasma Market（2025 USD 3.28B → 2035 USD 12.19B，CAGR 14.03%；常壓段 66%）。 [D10] https://www.precedenceresearch.com/cold-plasma-market
53. Future Market Report — Piezoelectric Transformers Market（USD 220.5M(2025) → 465.8M(2033)，CAGR 9.8%）。 [D02] https://www.futuremarketreport.com/industry-report/piezoelectric-transformers-market
54. Verified Market Reports — Piezoelectric Transformers Market。與上者相差達 3 倍的另一組估計。 [D02] https://www.verifiedmarketreports.com/product/piezoelectric-transformers-market/

### 7.9 本專案內部來源（本文件的實際資料來源）

55. `01-pt-power-conversion-sota.md` — STEMINC 價格、PT 功率轉換 SOTA、市場規模。
56. `02-dual-use-active-passive-concept.md` — 兩用概念家族、xMEMS／Boréas／PowerHap 規格、HEAD 網球拍失敗案例。
57. `03-materials-manufacturing.md` — 材料與製程成本驅動因子、穿金屬壁效率數字。
58. `04-reliability-standards-qual.md` — Bartels 壽命、多層致動器失效模式、可靠度標準。
59. `06-patents-power-and-dualuse.md` — 專利地景、STEMINC RoHS 說法、銅電極成本論證。
60. `07-patents-nonpower-apps.md` — CeraPlas 結構與專利族、SMC 離子器專利、Iota/Astellas 數字。
61. `10-hv-plasma-ozone-sterilization.md` — **本文件冷電漿段落的主要來源**：CeraPlas/piezobrush 全部規格、通路、Viromed 交易。
62. `11-electrostatic-actuators-artificial-muscle.md` — XP Power Q101-5 價格、PT 產業崩塌、ViviTouch 案例。
63. `15-magnetic-immune-clean.md` — MRI 相容壓電馬達、無磁應用。
64. `16-isolation-gatedrive-throughwall.md` — 穿金屬壁「零商品化」結論、隔離閘驅競品規格。
65. `21-drive-control-ic-design.md` — Boréas 產品線與宣稱值、度量陷阱警告、自感測反證。
