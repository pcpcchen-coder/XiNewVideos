# 專利深查與白空間驗證：「主動／被動兩用」壓電元件的可專利空間

> 一句話結論：**前輪的「兩座互不相通的島」假說在低功率／觸覺節點上被證偽**——Boréas Technologies（源自 Harvard Simon Chaput 的 `US10931199B2`）已用**量產晶片 BOS1921** 把「驅動壓電致動器（主動）＋從致動器電容回收能量（被動）＋用同一顆致動器當力感測器（感測）」三合一，橋已經建好且有專利；**但那座橋只搭在 <1 W 的容性負載驅動節點上，並未延伸到 DC-DC 功率轉換島**。功率轉換島的橋樑是 2026 年才剛出現的學術成果（`arXiv 2605.15279` 用 PR 自身的 motional current 做自感測控制），**專利尚未見到，這是目前唯一還開著、但正在快速關閉的窗口**。另外查出兩件對台灣客戶極具操作性的事實：(a)「同一壓電元件兼具致動器與感測器」的**通案概念早已因 `US5347870A`(1994)／`US4035672A`(1977)／`US7235914B2`(華盛頓州立大學, 2001 申請) 到期而進入公有領域**，後進者只會被「特定電路／拓樸」的窄 claim 擋住，不會被概念擋住；(b) 觸覺這個橋接節點**同時是 NPE 重災區**——Immersion Corporation 握有 3,500 件已核准＋在審觸覺專利，2024 年與 Meta 和解（訴訟歷時 631 天）、續約 Samsung、並與 Valve 訴訟中。

---

## 0. 研究方法與限制（誠實揭露）

- **實際執行 28 次 WebSearch**（預算 25–30 次，未超支）。本文件所有事實均出自這 28 次搜尋回傳的標題、URL 與摘要文字。
- **WebFetch 與 curl 在本環境被 egress policy 全面封鎖（403），完全未使用**。因此：
  1. **無法閱讀任何一件專利的 claim 全文**。所有「claim 大意」皆來自搜尋引擎回傳的 abstract 片段，屬**推論**。
  2. **無法查證任何一件專利的法律狀態**（有效／失效／年費）。本文所有「到期年」皆為申請日／優先權日 +20 年之**推算**。
  3. **無法執行布林式 claim 全文檢索或 CPC 交集統計**。所謂「查無」＝「以自然語言搜尋引擎、以下列措辭、28 次查詢內未出現」，**不等於不存在**。
- **本輪必查但未查到的項目（已知缺口）**：
  - **MIT `US12126324B2` / `US12009746` / `US12388364` 的同族地域（台灣／中國／日本／歐洲）完全查無。** 用兩種不同措辭（含 `WO2022235962A1`、含「EP CN China filing」）都只回到美國件本身，Google Patents 的 "Also published as" 欄位抓不到。**這是本份最想回答卻沒能回答的問題，必須委外。**
  - **Harvard `US10931199B2` 的同族地域查無**；Boréas 完整專利清單查無（Justia 的 assignee 頁未被搜尋引擎回傳可用摘要）。
  - **ADI `MAX77501` 對應的專利號查無**——只查到 datasheet 描述其能量回收機制（正半波電感電流對壓電充電、負半波經整流 MOSFET T1 反向導通把電流送回輸入電容），**無法判斷它如何迴避 Harvard 專利**。這是第三優先的核心問題，未解。
  - **INSA Lyon／CNRS（Guyomar、Richard、Lallart）名下的 SSHI/SSDI 專利查無**——只查到他們的論文。**是「他們真的只發論文不申請專利」還是「搜尋不到」，無法區分。**
  - 日文檢索（圧電トランス／圧電素子 センサ 兼用／自己センシング）**執行 1 次即失敗**，只回到 1996–2002 年的舊件（`JPH0936452A`、`JP2002016302A`）與非專利內容；**日本大廠 2020 年後的動向仍然查無**。
  - TDK CeraPlas 專利族的**地域覆蓋查無**（只確認 `US10856399B2` 本身）。
- **驗證等級標示**：本文對每個事實標註「已驗證」（搜尋結果直接給出該欄位）／「未驗證」（僅從摘要推得）／「查無」。**沒有任何一個專利號、公司名、數字是編造的。**

---

## 1. 結論摘要

1. **「兩島互不相通」的假說**在低功率節點**被證偽**。Boréas Technologies（加拿大 Bromont，創辦人 Simon Chaput，Harvard 博士）的 **BOS1921** 官方描述為「**第一顆能同時感測與驅動壓電致動器（最高 190 Vpp）的單晶片方案**」，且「**可把壓電致動器當力感測器用，方法是量測其端子間電壓**」，感測解析度 7.6 mV–54.5 mV，並內建**能量回收**。這就是「同一顆壓電體同時是主動元件（致動）、被動元件（能量回收儲能）、感測器」的**已量產實例**。（[Boréas BOS1921](https://www.boreas.ca/products/bos1921-piezo-driver)、[DigiKey](https://www.digikey.com/en/product-highlight/b/boreas/bos1921-piezo-driver)）**已驗證**

2. **這座橋有專利地基，而且來自 Harvard。** `US10931199B2`「Driver for a circuit with a capacitive load」——單電感、高整合、**雙向**、高壓致動器驅動器，**能把儲存在致動器上的能量回收回來**；對應學術發表為 Chaput / Brooks / Gu-Yeon Wei 的 ISSCC 論文「A 3-to-5V input 100V pp output 57.7 mW 0.42% THD+N highly integrated piezoelectric actuator driver」。同族續案 `US11374496`（同標題）。Boréas 對外宣稱「30+ 專利」（**未驗證**）。推算保護到 **~2037–2039**。（[Google Patents US10931199B2](https://patents.google.com/patent/US10931199B2/en)、[Harvard VLSIArch](https://vlsiarch.eecs.harvard.edu/publications/215-3-5v-input-100v-pp-output-577-mw-042-thd-n-highly-integrated-piezoelectric)、[USPTO US11374496](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/11374496)）

3. **但這座橋只搭在「容性負載驅動」節點，沒有延伸到功率轉換島。** CapDrive 處理的是 **<1 W、100–190 Vpp、<300 Hz** 的類比波形產生與回收，不是 bidirectional bulk power conversion。**MIT／Berkeley 的 PR-based DC-DC 島與 Boréas 島之間，本輪仍查無共同專利權人，也查無任何一件同時 claim 兩者的專利。**「兩島論」在**功率轉換 × 自感測**這個具體交叉點上**仍然成立**。

4. **功率轉換島的自感測橋樑，2026 年才剛在學術端出現，專利端還是空的。** `arXiv 2605.15279`（2026-05）「Motional-Current-Sensing Method and Simplified Closed-Loop Control Strategy for Piezoelectric-Resonator-based DC-DC Converters」明述：PR 等效電路 LC 串聯支路的 **motional current 對控制至關重要卻無法直接量測**，「偵測其零交越點或量測其振幅的困難，一直是最主要的障礙之一」；該文用 **ring-dot 型壓電變壓器**做 motional current 感測，特性為「**低延遲、低損耗、本質隔離**」，並以有限狀態機＋PI 迴路＋低速 ADC＋比較器實現事件驅動控制，達成整個開關週期內全 ZVS 且**可自啟動**。**這正是「功率元件當自己的感測器」——白空間的正中心，且窗口正在關閉（論文出現後 12–18 個月通常就會有對應專利公開）。**（[arXiv 2605.15279](https://arxiv.org/abs/2605.15279)）**已驗證（論文內容）**

5. **「一顆壓電元件既當致動器又當感測器」這個通案概念，早已進入公有領域。** 三件關鍵到期先前技術：
   - `US5347870A`「**Dual function system having a piezoelectric element**」——「一個具有壓電元件的系統以及與之搭配使用的電路，使該元件能提供**致動器與感測器的雙重功能**」，1994 年核准，**推算 2011–2014 年到期**。
   - `US4035672A`「**Acoustic transducer with a dual purpose piezoelectric element**」，1977 年，**早已到期**。
   - `US7235914B2`「Piezoelectric micro-transducers」，受讓人 **Washington State University Research Foundation**（已驗證），2001-10-25 申請、2007-06-26 核准，明述該壓電單元「**既作為壓電致動器（電能→機械功）也作為壓電發電機（機械功→電能）**」，**推算 2021 年前後到期**。
   
   **策略意涵：任何人想用「同一顆壓電元件兼具主動與被動功能」這個上位概念去圈客戶，都會被這三件打掉。客戶的自由實施空間在概念層是乾淨的；風險只在特定電路／拓樸／控制序列的窄 claim。**（[USPTO US5347870](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/5347870)、[Google Patents US4035672](https://patents.google.com/patent/US4035672)、[Google Patents US7235914](https://patents.google.com/patent/US7235914)）

6. **能量擷取＋感測的兩用 claim 也早有德國先例。** `WO2006087304A1`「Vorrichtung zur Energieversorgung」明述：該壓電模組「**不僅用於產生電壓，也作為感測器，特別是壓力感測器**」。2006 年公開，**推算已到期**。這進一步收窄了「兩用」概念可被獨占的空間。（[Google Patents WO2006087304A1](https://patents.google.com/patent/WO2006087304A1/de)）**未驗證（僅摘要）**

7. **對台灣客戶最直接的一條：SSHI 的關鍵美國專利握在國立清華大學手上。** `US9450510B2` / `US9831796`「**Energy harvesting device using SSHI techniques**」，受讓人 **National Tsing Hua University**（**未驗證——來自搜尋摘要，非一手頁面**）；另一件 `US9548680B2`「Self power SSHI circuit for piezoelectric energy harvester」受讓人 **King Saud University**（**未驗證**）。**若清大確為權利人，這是國內可談的授權標的，成本與談判難度遠低於 MIT／Harvard。這是本份最可立即行動的一條。**（[Google Patents US9450510B2](https://patents.google.com/patent/US9450510B2/en)、[Google Patents US9548680B2](https://patents.google.com/patent/US9548680B2/en)）

8. **「阻尼＋回收＋SHM 三合一」不是雷區，但也不是乾淨白區——它是「散落的地雷」。** SSHI/SSDI 的權利人**高度分散且以大學為主**（清大、King Saud），法國 INSA Lyon 一脈（Guyomar/Richard/Lallart）**只查到論文、查無專利**；另有 `EP2579440A1` / `US20140218989A1`「Rectifier circuit with AC side short-circuiting function and synchronized switch harvesting on inductor converter」（**受讓人查無**）。**沒有任何一家 IC 大廠（TI／ADI／e-peas）被查到持有 SSHI 核心專利**——e-peas AEM30330 的官方描述只提 buck-boost + MPPT，未提 SSHI。**判定：灰區偏安全，但必須逐件排除，不能假設無主。**

9. **觸覺這個「橋接節點」同時是 NPE 重災區——這是本輪最重要的風險發現。** **Immersion Corporation** 為公認的觸覺 NPE，宣稱達到 **3,500 件已核准與在審觸覺專利**；2024-02-09 與 **Meta Platforms** 簽訂專利授權與和解協議（西德州地院，涉 6 件觸覺專利、標的含 Meta Quest 2／Beat Saber／Horizon Worlds，訴訟歷時 **631 天**）；2024-05 與 **Samsung Electronics** 續約授權；與 **Valve** 的訴訟於 2024-05-14 因 **7 件 IPR** 而中止。截至 2025-01-31 現金與固定收益投資 **1.324 億美元**。**意涵：客戶若把「主動／被動兩用」的第一個落地應用選在觸覺，等於一腳踏進 Immersion 的射程。**（[PatSnap: Immersion v. Meta](https://www.patsnap.com/resources/blog/litigation/immersion-corp-v-meta-platforms-haptic-feedback-patent-litigation-patsnap/)、[PatSnap: Immersion v. Valve](https://www.patsnap.com/resources/blog/litigation/immersion-corp-v-valve-corp-haptic-feedback-patent-litigation-patsnap/)、[Immersion IR](https://ir.immersion.com/news-releases/news-release-details/immersion-reaches-3500-issued-and-pending-haptics-patents)）

10. **MIT 第二層專利的標題本輪取得一手佐證。** `US12388364` 的 USPTO 列印連結標題確認為「**DC-DC converter based on piezoelectric resonator**」（此前為半驗證）。`US12126324B2` 再次確認為 PCT/US2022/028043（2022-05-06）之美國國家階段、主張 63/185,663（2021-05-07）優先權、發明人 Boles／Perreault／Lang／Bonavia、申請人 MIT。**但同族地域仍查無。**（[USPTO US12388364](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/12388364)、[Google Patents US12126324B2](https://patents.google.com/patent/US12126324/en)）

11. **能量回收驅動器的競爭者已經出現，但身分不明。** `US12520728` / `EP4326038A1`「**Energy recovery driver for PZT actuators**」（EP 公開日 2024-02-21）——**受讓人查無**。這代表 Harvard／Boréas 之外至少還有一個玩家在同一節點佈局，客戶的迴避設計必須把它算進來。（[USPTO US12520728](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/12520728)、[EPO EP4326038A1](https://data.epo.org/gpi/EP4326038A1)）

12. **「壓電變壓器自我健康診斷」仍是真白區，但邊界比想像中近。** `US6078124`「Piezoelectric transformer driving circuit and driving method」已經 claim 了「偵測高壓輸出的持續狀態並調整驅動頻率，以避免變壓器承受過度應力」——這是**保護**，不是**診斷**。壓電元件的電機阻抗自診斷（EMI 法）在**學術上成熟**（可辨識虛焊、脫層、磨損、破裂），但**未見與功率傳輸整合的專利**。「**同一顆 PT 一邊傳能量、一邊用共振頻率漂移量化自身絕緣裕度**」的 claim **仍查無**。（[USPTO US6078124](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/6078124)、[Sci Rep s41598-021-90567-y](https://www.nature.com/articles/s41598-021-90567-y)）

---

## 2. 查證結果：白空間驗證的逐項結果

### 2.1 第一優先——七組措辭的檢索結果

| # | 檢索措辭（自然語言） | 結果 | 判定 |
|---|---|---|---|
| 1 | dual-function piezoelectric device patent（"both actuator and energy storage"） | 命中 `US5347870A`「Dual function system having a piezoelectric element」（致動器＋感測器雙功能，1994）；`US4035672A`（雙用途壓電元件聲學換能器，1977） | **假說部分證偽**：概念件存在但**已到期** |
| 2 | piezoelectric transducer simultaneous power transfer and sensing | 命中 `US20220131482A1`（穿戴裝置：三片預彎低 K 壓電元件分別作擷取器／壓力感測器／觸覺器——**但是三片，不是同一片**）；`US5703474A`（壓電發電能量傳輸最佳化） | **未命中真正的「同一元件」claim** |
| 3 | multifunctional piezoelectric transformer sensor patent | 全部落到多輸出 PT（`US7474040`）與非專利的多模態感測論文 | **查無** |
| 4 | combined piezoelectric power conversion and sensing | 命中 `WO2006087304A1`（壓電模組兼作壓力感測器，2006，德） | **弱命中，已到期** |
| 5 | piezoelectric self-sensing power converter patent | 命中 `US10931199B2`（Harvard／Boréas，驅動＋能量回收）與 Boréas BOS1921 產品（驅動＋回收＋力感測） | **強命中——假說在此節點證偽** |
| 6 | CPC H10N30 × H02M 交集 | 只回到能量擷取件（`US20160346556A1`、`US7649305B2` 等）與 CPC 定義頁；**無法執行真正的分類交集統計** | **方法失效** |
| 7 | time-multiplexed / shared piezoelectric element alternately power conversion and actuation | 命中 `US7235914B2`（WSU，致動器＋發電機同體，已到期）；文獻層面命中「dual-mode UPT 換能器以同一壓電元件同時做能量與資訊傳輸」（植入物領域） | **概念件已到期；植入物領域有活躍先前技術** |

**綜合判定**：
- **「同一壓電元件兼具主動與被動功能」的上位概念——已公有領域，不可能被任何人獨占。**
- **「驅動 ＋ 能量回收 ＋ 自感測」三合一於容性負載——已被 Harvard／Boréas 佔住（有效專利，量產產品）。**
- **「功率轉換（DC-DC）＋ 自感測」於同一 PR——以本輪檢索方法查無任何專利；學術首發於 2026-05。**
- **「功率傳輸 ＋ 屏障完整性自診斷」——查無。**
- **限制聲明：以上「查無」是在無專業資料庫、無法做布林式 claim 全文檢索、無法查 CPC 交集統計的條件下得出。信心度：中等（60–70%），不足以作為投資決策的唯一依據。**

### 2.2 第二優先——MIT／Harvard 關鍵專利

| 專利號 | 標題 | 受讓人／發明人 | 關鍵日期 | claim 大意（推論） | 同族地域 |
|---|---|---|---|---|---|
| `US12126324B2` | Piezoelectric resonators for power conversion | MIT；Boles／Perreault／Lang／Bonavia（已驗證） | 優先權 2021-05-07（US 63/185,663）；PCT/US2022/028043 於 2022-05-06 | PR **幾何條件**，且該條件**以轉換器指定的電壓與功率等級定義**——設計規則層級 claim | **查無** |
| `US12009746` | （DC-DC，PR 為功率級儲能，含 connected/open stages 開關序列＋resonant soft-charging） | Boles 等（半驗證） | 未取得 | 拓樸／控制層 | **查無** |
| `US12388364` | **DC-DC converter based on piezoelectric resonator**（本輪由 USPTO 連結標題確認） | 未驗證 | 未取得 | 同上 | **查無** |
| `US10931199B2` | Driver for a circuit with a capacitive load | Harvard 系（Chaput/Brooks/Wei）→ Boréas | 未取得核准前日期 | 單電感、雙向、高壓、**可回收致動器上儲存的能量** | **查無** |
| `US11374496` | Driver for a circuit with a capacitive load（續案） | 推定 Boréas（未驗證） | 未取得 | 產生**可變預驅動脈衝**以達成 ZVS/ZCS、降低切換損耗與波形失真 | **查無** |

> **關鍵未解**：任務指定「若 MIT 與 Harvard 的關鍵專利未進入台灣與中國，客戶的自由實施空間會大很多」——**本輪無法回答**。兩種措辭都失敗。**這一題必須用 Espacenet／Global Dossier／INPADOC 家族檢索，是委外案的第一項。**

### 2.3 第三優先——Boréas 專利組合與 ADI 迴避路徑

**Boréas Technologies（Bromont, Québec；創辦人 Simon Chaput）**

- 技術品牌：**CapDrive™**（官方稱「patented scalable piezo driver architecture」）。宣稱相對傳統驅動可**省下最多 10 倍功耗**（**未驗證**）。
- 產品線（皆為量產、通路可購）：**BOS1901**（單通道，能量回收）、**BOS1921**（＋Advanced Sensing，最高 190 Vpp，感測解析度 7.6–54.5 mV，內建數位前端，**單晶片同時感測與驅動**）、**BOS1931**（高效率）、**BOS1211**（車用 HMI）、**BOS0614**（多通道行動裝置）。
- 專利：`US10931199B2`（核心）、`US11374496`（續案）。**公司宣稱 30+ 專利（未驗證）**；完整清單查無。
- **戰略關鍵**：BOS1921 的官方賣點是「讓 PC OEM **免除其他壓電驅動器所需的專用力感測電路**」——**這正是「同一顆壓電體既是致動器也是感測器」的商業價值主張，且已被驗證為可賣錢的規格。**（[Boréas press](https://www.boreas.ca/blogs/press-center/boreas-bos1921-meets-demand-for-low-cost-high-performance-haptics-in-ultra-thin-pc-trackpads)、[BOS1921 datasheet PDF](https://5753554.fs1.hubspotusercontent-na1.net/hubfs/5753554/BOS1921/BT015BDS01.01.pdf)）

**ADI MAX77501（迴避設計問題——未解）**

- 官方描述：2.8–5.5 V 輸入，單端輸出最高 **110 Vpk-pk**，最佳化驅動 **2 µF 以下**壓電元件；**專有的能量回收機制**——正半波電感電流對壓電電容充電，負半波電流**經整流 MOSFET T1（導通時允許反向電流）送回輸入電容**，形成「除了切換損耗與 MOSFET RDS(ON) 之外幾乎無損」的能量回收方案。
- **對應專利號查無。** 因此**無法判斷 ADI 是靠「單端 vs 雙向」「單電感 vs 四開關」還是「boost 架構」來迴避 `US10931199B2`。**
- **這是客戶最該補的一課**：ADI 是全球最會做 FTO 的公司之一，它的迴避路徑就是最好的迴避設計教科書。（[ADI MAX77501](https://www.analog.com/en/products/max77501.html)、[ADI datasheet PDF](https://www.analog.com/media/en/technical-documentation/data-sheets/max77501.pdf)、[ADI 技術文章](https://www.analog.com/en/resources/technical-articles/energysaving-piezo-haptic-driver-is-the-touch-sensors-best-friend.html)）
- 另有第三方學術實作：MDPI *Actuators* 12(9) 345「A 3-to-5 V Input, 80 Vpp Output, 2.75% THD+N, 2.9 µF Load Piezoelectric Actuator Driver with **Four-Switch Buck–Boost**」——**四開關 buck-boost 是明確的另一條架構路徑**，可作為迴避設計起點。（[MDPI Actuators 12(9) 345](https://www.mdpi.com/2076-0825/12/9/345)）

### 2.4 第四優先——SSHI／SSDI／bias-flip 介面電路權利人

| 專利／申請號 | 標題 | 受讓人 | 驗證狀態 |
|---|---|---|---|
| `US9450510B2` / `US9831796` | Energy harvesting device using SSHI techniques | **National Tsing Hua University（國立清華大學）** | **未驗證（僅搜尋摘要）** |
| `US9548680B2` / `US20150311824A1` | Self power SSHI circuit for piezoelectric energy harvester | **King Saud University** | **未驗證（僅搜尋摘要）** |
| `EP2579440A1` / `US20140218989A1` | Rectifier circuit with AC side short-circuiting function and SSHI converter | **查無** | 查無 |
| `CN204271948U` | 一種自供電 P-SSHI 電路 | 查無 | 查無 |
| `US10361356` | Piezoelectric energy harvesting | 查無 | 查無 |
| INSA Lyon / CNRS（Guyomar、Richard、Lallart、Badel、Lefeuvre） | — | **查無任何專利** | 只查到論文（Badel/Guyomar/Lefeuvre/Richard, JIMSS 2005 等） |
| MIT（Ramadass、Chandrakasan，bias-flip） | — | **查無任何專利** | 只查到 2009/2010 論文與 MIT DSpace 全文 |
| TI／ADI／e-peas | — | **查無 SSHI 專利** | e-peas AEM30330 官方僅述 buck-boost + MPPT，未提 SSHI |

**判定：SSHI/SSDI 是「大學持有、分散、無產業守門人」的格局。這對客戶是好消息（可談授權、無巨頭封鎖），但「無主」的假設不安全——必須逐件排除。**

### 2.5 第五優先——順帶查到的其他發現

- **TDK CeraPlas**：`US10856399B2`「Device for generating an atmospheric-pressure plasma」，發明人 Kudela / Puff / Rinner，2020-12-01 核准，開發者為 **TDK Electronics GmbH & Co. OG**（已驗證）；材料為 PZT，**可與內部銅電極共燒**；官方定位為「**在單一元件中結合電壓轉換與電漿產生**」。**同族地域查無。**（[Google Patents US10856399](https://patents.google.com/patent/US10856399)、[TDK 技術文](https://www.tdk-electronics.tdk.com/en/373562/tech-library/articles/applications-cases/applications-cases/cold-plasma-from-a-single-component/1109546)）
- **PT 諧振腔 ＋ 外部容性致動器聯合共設計**：本輪查到的最接近件是 `US9871182`（PT 功率轉換器，在電抗網路與 **PT 輸入電容**之間形成諧振腔，電抗網路通常就是一顆與 PT 靜態電容共振的電感）與 `US5126589A`「Piezoelectric driver using resonant energy transfer」。**但「把外部致動器的負載電容當成諧振腔的一部分來共同設計」的 claim 查無。這是一個具體、狹窄、可申請的白空間。**（[Justia US9871182](https://patents.justia.com/patent/9871182)、[Google Patents US5126589A](https://patents.google.com/patent/US5126589A/en)）
- **日本大廠 2020 後動向**：**完全查無**。日文檢索只回到 `JPH0936452A`（1997，圧電トランス）、`JP2002016302A`（2002，PZT 壓電變壓器，含一次驅動部與二次發電部）、`JP2016186954A`（2016，壓電元件與壓力感測器）。**無法判斷 Murata／TDK／Kyocera 是否有 2020 後的未公開在審案。**
- **超音波穿壁／植入物領域的兩用先前技術活躍**：`arXiv 2110.12428`「A CMOS SoC for Wireless Ultrasonic Power/Data Transfer **and SHM Measurements** on Structures」——**同一超音波鏈路同時做供電、資料傳輸與結構健康監測**，這是「三合一」在**學術端已實作**的證據；另 IOPscience 2026 綜述明述「近期的雙模 UPT 換能器**以同一顆壓電元件同時做能量與資訊傳輸**，藉此縮小植入物體積並簡化封裝」。**這一區的先前技術密度比預期高，白空間比預期小。**（[arXiv 2110.12428](https://arxiv.org/pdf/2110.12428)、[IOPscience 2516-1091/ae5f8a](https://iopscience.iop.org/article/10.1088/2516-1091/ae5f8a)）

---

## 3. 關鍵數字表

| 項目 | 數值／事實 | 驗證狀態 | 來源編號 |
|---|---|---|---|
| 本輪 WebSearch 次數 | **28**（預算 25–30） | 已驗證 | — |
| BOS1921 最高驅動電壓 | **190 Vpp** | 已驗證 | [1][2] |
| BOS1921 力感測解析度 | **7.6 mV – 54.5 mV**（可選） | 已驗證 | [1] |
| BOS1921 定位 | **業界第一顆能同時感測與驅動壓電致動器的單晶片** | 已驗證（官方宣稱） | [1][3] |
| CapDrive 宣稱省電 | **最多 10×** vs 傳統驅動 | 未驗證（官方宣稱） | [4] |
| Boréas 專利數 | **30+**（已核准＋在審） | 未驗證 | [5] |
| Harvard 驅動器 ISSCC 實測 | 3–5 V 輸入 → **100 Vpp** 輸出、**57.7 mW**、THD+N **0.42%** | 已驗證 | [6] |
| MAX77501 輸出 | **110 Vpk-pk**，輸入 2.8–5.5 V，負載 ≤ **2 µF** | 已驗證 | [7][8] |
| MAX77501 專利號 | **查無** | 查無 | — |
| MIT `US12126324B2` 優先權日 | **2021-05-07**（US 63/185,663） | 已驗證 | [9] |
| MIT PCT 申請日 | **2022-05-06**（PCT/US2022/028043） | 已驗證 | [9] |
| MIT 專利推算到期 | **~2041–2042** | 推算 | — |
| MIT 家族地域（TW/CN/JP/EP） | **查無** | 查無 | — |
| `US12388364` 標題 | **DC-DC converter based on piezoelectric resonator** | 已驗證（USPTO 連結標題） | [10] |
| `US5347870A` 核准年 | **1994**（推算 2011–2014 到期） | 已驗證（標題）／推算（到期） | [11] |
| `US4035672A` 年份 | **1977**（早已到期） | 已驗證（標題） | [12] |
| `US7235914B2` 受讓人 | **Washington State University Research Foundation** | 已驗證 | [13] |
| `US7235914B2` 申請／核准 | 2001-10-25 ／ 2007-06-26（推算 ~2021 到期） | 已驗證 | [13] |
| `US9450510B2` 受讓人 | **National Tsing Hua University（台灣）** | **未驗證** | [14] |
| `US9548680B2` 受讓人 | **King Saud University** | **未驗證** | [15] |
| Immersion 專利規模 | **3,500 件**已核准＋在審觸覺專利 | 已驗證 | [16] |
| Immersion v. Meta | 2024-02-09 和解＋授權；訴訟歷時 **631 天**；涉 **6 件**專利 | 已驗證 | [17] |
| Immersion v. Valve | 2024-05-14 因 **7 件 IPR** 中止 | 已驗證 | [18] |
| Immersion 現金部位 | **1.324 億美元**（2025-01-31） | 已驗證 | [18] |
| `US10856399B2` 核准日 | **2020-12-01**（Kudela/Puff/Rinner，TDK Electronics GmbH & Co. OG） | 已驗證 | [19] |
| PR motional current 感測論文 | **2026-05**（arXiv 2605.15279）；ring-dot PT 感測，**低延遲、低損耗、本質隔離** | 已驗證（論文） | [20] |
| `EP4326038A1` 公開日 | **2024-02-21**（Energy recovery driver for PZT actuators，**受讓人查無**） | 已驗證（日期） | [21] |
| 四開關 buck-boost 壓電驅動器 | 3–5 V 輸入 → **80 Vpp**，THD+N **2.75%**，負載 **2.9 µF** | 已驗證 | [22] |

---

## 4. 對決策的意涵：三張清單

### 4.1 🟢 安全區（可自由實施，本輪未見有效專利阻擋）

| 標的 | 依據 | 附帶條件 |
|---|---|---|
| **「同一壓電元件兼具主動（致動）與被動（儲能／感測）功能」的上位概念本身** | `US5347870A`(1994)、`US4035672A`(1977)、`US7235914B2`(WSU, 2001 申請)、`WO2006087304A1`(2006) 全部推算已到期 | 概念安全，**具體電路仍須逐件排除** |
| **1990s 世代 PT 轉換器拓樸**（NEC / Matsushita / Murata） | 前輪已查證，推算 2018–2021 年全數到期 | 但這也代表**該世代技術沒有性能優勢** |
| **Rosen 型 PT 本體** | `US2,830,274` 等 1954–1961 年件 | 完全公有領域 |
| **「壓電變壓器兼作自身絕緣屏障完整性感測器」（自診斷隔離屏障）** | 本輪與前輪均**查無**任何 claim；最接近的 `US6078124` 只 claim 保護（偵測高壓持續狀態→調整頻率），`EP3127172B1` 只 claim 用 PT 量外部電壓 | **信心度中等**；建議先申請暫時案卡位 |
| **「把外部容性致動器的負載電容納入 PT 諧振腔一起共同設計」** | 查無；`US9871182` 只 claim PT **自身**輸入電容與外加電感的諧振腔 | 窄而具體，**適合作為第一件核心專利** |
| **PR 泛音／非基頻模態 × 自感測控制的組合** | UC 33625 只掛「泛音 PR 用於功率轉換」，未見與自感測組合 | 需先確認 UC 未公開申請案 |
| **多元件壓電電漿陣列的同步與互擾抑制** | TDK 自己的論文（MDPI *Plasma* 4(2)19）顯示仍是研究題目 | 但材料製程門檻在 TDK 手上 |

### 4.2 🟡 灰區（技術可用，但必須做迴避設計 / FTO 逐件清查）

| 標的 | 障礙 | 迴避方向（初步） |
|---|---|---|
| **高壓容性負載驅動 ＋ 能量回收 ＋ 自感測（<1 W 觸覺／微流體／光學）** | `US10931199B2` + `US11374496`（Harvard／Boréas，推算 2037–2039） | 參考 ADI MAX77501 的**單端 + boost + 整流 MOSFET 反向導通**路徑；或 MDPI 的**四開關 buck-boost** 路徑。**必須先查出 ADI 的專利號才能定案** |
| **SSHI / SSDI / SSDV / bias-flip 介面電路** | 清大 `US9450510B2`/`US9831796`（未驗證）、King Saud `US9548680B2`、`EP2579440A1`（無主） | 權利人分散且以大學為主 → **可談授權**。清大若確為權利人，是**國內談判的最佳起點** |
| **自感測致動器（電容橋分離驅動與位移訊號）** | `US10349818` / `US9872606`（受讓人未驗證）、`CN111060232B` | 改用**非電容橋**的分離手段（例如 motional current 觀測、注入式阻抗譜、時分多工） |
| **PR-based DC-DC 的閉環控制（motional current 相關）** | 學術首發 2026-05；**專利端查無，但極可能有在審案** | **時間壓力最大的一格**。若要做，**現在就要申請**，不要等 |
| **穿金屬壁功率＋資料同傳** | `US20150049587A1`、`US20170163354A1`（A1 公開案，**核准狀態未驗證**） | 先確認是否核准；若已放棄則轉為安全區 |
| **PT 式隔離電壓感測** | `EP3127172B1`（受讓人未驗證） | 差異化在「診斷屏障自身」而非「量測外部電壓」 |
| **超音波供電植入物 ＋ 同體資料回傳** | UC Berkeley neural dust 家族；且 IOPscience 2026 綜述顯示 dual-mode UPT 已是領域常識 | **切入點應在材料／微型換能器供應鏈，不是系統** |

### 4.3 🔴 禁區（已被圈死，不建議正面進入）

| 標的 | 圈地者 | 推算解禁年 |
|---|---|---|
| **以 PR 為唯一功率級儲能元件的 DC-DC，含 connected/open 多階段開關序列與 resonant soft-charging** | MIT（`US12009746`、`US12388364`） | **~2041–2042** |
| **以「轉換器指定電壓與功率等級」定義的 PR 幾何設計規則** | MIT（`US12126324B2`） | **~2041–2042**；**這是設計規則層 claim，極難迴避** |
| **單電感、雙向、高壓、可回收致動器儲能的整合式驅動器**（CapDrive 核心） | Harvard → Boréas（`US10931199B2`、`US11374496`，宣稱 30+ 件） | **~2037–2039** |
| **單一陶瓷體內完成升壓＋大氣壓冷電漿放電，含共振頻率追蹤** | TDK Electronics（`US10856399B2`、`US11903321`、`US10772182`、`US10966309`、`US10531552`、`US10827599`） | **~2035–2040**；且材料共燒 know-how 為額外壁壘 |
| **觸覺回饋的系統層／使用者體驗層 claim** | **Immersion Corporation（3,500 件，活躍 NPE）** | 不適用——**組合式包裹授權，只能付錢或繞開整個應用** |
| **壓電做磁性電感的 drag-and-drop 替代** | UC Berkeley 33585（專利號未公開） | 且**這正是客戶已排除的路線** |

### 4.4 建議委託專業事務所執行的具體檢索式

給事務所的委任書可直接照抄以下四組。建議使用 **Espacenet / INPADOC + Derwent Innovation + PatSnap 或 Orbit**，並要求 **claim 全文（CL=）而非全文（FT=）** 檢索。

**A. 白空間終局驗證（最高優先，決定專案是否成立）**
```
CL=( (piezoelectric OR piezo* OR "electromechanical resonator")
     AND (actuat* OR "drive signal" OR excite*)
     AND (sens* OR measur* OR detect* OR monitor*)
     AND ("energy stor*" OR "power convert*" OR "power transfer" OR "energy recovery"
          OR transform* OR damp* OR filter*) )
AND CL=( "same" OR "single" OR "common" OR "shared" OR "simultaneous*"
         OR "time-multiplex*" OR "dual function" OR "dual-mode" OR "bifunctional" )
AND PD >= 2015
```
> 要求事務所回報：命中件數、依受讓人分佈、依 CPC 分佈、以及**任一 claim 1 同時包含「被動能量處理」與「主動致動／感測」兩個功能限定詞的件**。

**B. CPC 交集熱區統計（回答「白空間是真白還是我沒查到」）**
```
CPC=(H10N30/* OR H02N2/*) AND CPC=(H02M3/* OR H02M7/* OR H02M1/*)
AND PD >= 2018
→ 出申請年曲線 + Top 20 受讓人 + Top 20 發明人
```
再單獨跑：
```
CPC=(H10N30/* OR H02N2/*) AND CPC=(G01R OR G01H OR G01M OR G01N29/*) AND PD >= 2018
→ 找「壓電功率元件 × 量測／診斷」的交集熱區
```

**C. 同族地域查核（本輪最大缺口，最可操作的結論來源）**
```
對以下每一件，出完整 INPADOC 家族清單 + 各國法律狀態 + 年費繳納紀錄：
  US12126324B2 / US12009746 / US12388364      （MIT）
  US10931199B2 / US11374496                    （Harvard → Boréas）
  US10856399B2 / US11903321 / US10772182       （TDK CeraPlas）
  US9450510B2 / US9831796 / US9548680B2        （SSHI）
特別確認：TW / CN / JP / EP / KR 是否有同族，以及是否已放棄或未進國家階段。
```
> **決策規則：若 MIT 與 Harvard 的關鍵件在 TW 與 CN 均無同族，則客戶在台灣製造、銷往中國／東南亞的路徑實質無阻，禁區可降級為灰區；美國與歐洲市場另議。**

**D. 特定人／機構的完整組合**
```
PA=("Boreas Technologies" OR "Boréas Technologies") OR IN=("Chaput, Simon")
PA=("Analog Devices" OR "Maxim Integrated") AND CL=(piezo* AND ("energy recovery" OR "charge recovery" OR "energy recycl*"))
IN=("Guyomar, Daniel" OR "Richard, Claude" OR "Lallart, Mickael" OR "Badel, Adrien" OR "Lefeuvre, Elie")
PA=("Centre National de la Recherche Scientifique" OR "INSA Lyon" OR "Institut National des Sciences Appliquees") AND CL=(piezo* AND (rectif* OR "switch*"))
PA=("National Tsing Hua University") AND CL=(piezo*)
PA=(Murata OR Kyocera OR "Taiyo Yuden" OR "TDK") AND CL=(piezo* AND ("power conversion" OR transformer OR "self-sensing" OR 兼用)) AND PD>=2020
IN=("Perreault, David") OR IN=("Boles, Jessica") OR IN=("Lang, Jeffrey")   → 含未核准之公開申請案 A1
```

---

## 5. 反面證據與物理／法律上限

1. **最重要的反面證據：白空間的核心假說在低功率端已經被商業產品證偽。** BOS1921 不是論文、不是專利申請，是**通路可買、有 datasheet、有 PC OEM 客戶**的量產晶片，做的正是「同一顆壓電體＝致動器＋能量回收元件＋力感測器」。**客戶若以為這是無人區，會嚴重誤判。正確的定位是「這個模式已被市場驗證有價值，但只在 <1 W 的容性驅動節點；價值主張成立，位置已被占據，必須換節點。」**

2. **概念層的公有領域是雙面刃。** `US5347870A`(1994)、`US4035672A`(1977)、`US7235914B2`(WSU) 讓客戶不會被概念性 claim 擋住——但**同樣代表客戶也拿不到概念性 claim**。客戶能申請到的專利，必然是**窄的、具體的、電路／拓樸／控制序列層級的**。這直接影響專利的商業價值：**窄專利防不住競爭者換架構，護城河要靠 know-how 而非專利。**

3. **白空間正在以可測量的速度關閉。** PR-based DC-DC 的 motional current 自感測，2026-05 才有第一篇公開（arXiv 2605.15279）。專利公開落後申請 18 個月——**這代表現在（2026-07）可能已經有 2024–2025 年申請、尚未公開的案子躺在 USPTO。客戶若在 2027 年才動作，很可能撞上已存在但當時看不見的申請案。**

4. **觸覺是最誘人也最危險的入口。** 它同時具備：(a) 已驗證的市場需求；(b) 已量產的兩用元件範例；(c) **一家握有 3,500 件專利、現金 1.324 億美元、剛打贏 Meta（631 天）、正在打 Valve 的 NPE**。前輪「NPE 風險低」的判斷**在觸覺這個子領域是錯的**——必須修正。

5. **前輪「兩島之間查無共同專利權人」的敘述，在方法論上不可靠。** 那是用自然語言搜尋引擎得出的結論。本輪用 7 種措辭重查，**光是換措辭就找出 4 件前輪沒有的兩用件**（US5347870、US4035672、US7235914、WO2006087304）。**這說明「查無」的信心度會隨檢索深度快速下降。任何以「這是白空間」為前提的投資決策，都必須先做專業資料庫檢索。**

6. **法律上限：設計規則層級的 claim 幾乎無法迴避。** MIT `US12126324B2` claim 的是「PR 幾何條件，且該條件以轉換器指定的電壓與功率等級定義」。這不是「一種電路」，而是「**一套設計方法**」。只要客戶的 PR 尺寸落在那個以電壓／功率為參數的幾何範圍內，就可能落入 claim——**而高效率設計必然收斂到相似的幾何**。**這是本專案在美國市場最硬的一堵牆，且要到 2041–2042 年才倒。**

7. **超音波／植入物領域的先前技術密度比前輪估計高。** IOPscience 2026 綜述明述「以同一顆壓電元件同時做能量與資訊傳輸」已是**近期換能器的常規作法**；`arXiv 2110.12428` 甚至已把「供電＋資料＋結構健康監測」做在一顆 CMOS SoC 上。**「三合一」在這個領域不是新穎點，是既有技術。**

8. **本輪的方法本身有結構性上限，必須誠實面對。** 沒有專業資料庫、無法讀 claim 全文、無法查法律狀態、無法查同族、無法做 CPC 統計。**本文件的定位應是「委外檢索的委任書與假說清單」，不是「FTO 意見書」。任何實質投資前，必須有事務所出具的 FTO / patentability opinion。**

---

## 6. 未解問題

1. **MIT（US12126324B2 / US12009746 / US12388364）與 Harvard（US10931199B2）是否進入台灣與中國？**——本輪兩次嘗試皆失敗。**這是最可操作的單一問題**：若答案是「否」，禁區立刻降級為灰區，客戶的策略從「繞開」變成「在美歐以外自由實施」。**必須用 INPADOC 家族檢索，成本極低（事務所半天工作量）。**

2. **ADI MAX77501 對應的專利號是什麼？它如何迴避 US10931199B2？**——查無。這是最好的迴避設計教材。建議路徑：查 ADI／Maxim 在 CPC H02M3/158 + H10N30 的 2019–2023 年申請案，發明人交叉比對 MAX77501 datasheet 的作者群。

3. **INSA Lyon / CNRS 到底有沒有 SSHI/SSDI 專利？**——本輪只查到論文。若真的只發論文不申請專利，SSD 家族的核心方法就在公有領域，「阻尼＋回收＋SHM 三合一」的門檻會低很多；若有專利只是搜尋不到，結論完全相反。**這一題的答案會直接翻轉 4.6 類機會的評級。**

4. **清華大學 `US9450510B2` / `US9831796` 的受讓人是否確為國立清華大學？法律狀態？有無台灣同族？**——本輪為「未驗證」。若屬實，這是**唯一一條國內可談的授權路徑**，應列為第一個要打的電話。

5. **日本大廠（Murata / Kyocera / Taiyo Yuden / TDK）2020 年後有無壓電功率轉換或兩用元件的在審案？**——日文檢索本輪失敗，仍完全查無。需用 J-PlatPat 或 Derwent 的日文 claim 檢索。

6. **`US12520728` / `EP4326038A1`「Energy recovery driver for PZT actuators」的受讓人是誰？**——查無。這是 Harvard／Boréas 之外的第三個玩家，身分決定風險等級（大廠 vs 大學 vs NPE）。

---

## 7. 來源清單

1. [Boréas Technologies — CapDrive® Ultra-Low Power Piezo Driver with Advanced Sensing (BOS1921)](https://www.boreas.ca/products/bos1921-piezo-driver) — 官方產品頁；190 Vpp、能量回收、把壓電致動器當力感測器（量測端子電壓）、感測解析度 7.6–54.5 mV。**本份最關鍵的證偽證據。**
2. [DigiKey — BOS1921 Piezo Driver](https://www.digikey.com/en/product-highlight/b/boreas/bos1921-piezo-driver) — 通路頁，佐證量產與可購買性。
3. [Boréas 新聞稿 — BOS1921 Meets Demand for Low-Cost, High-Performance Haptics in Ultra-thin PC Trackpads](https://www.boreas.ca/blogs/press-center/boreas-bos1921-meets-demand-for-low-cost-high-performance-haptics-in-ultra-thin-pc-trackpads) — 「免除其他驅動器所需的專用力感測電路」之價值主張。
4. [Boréas — CapDrive Technology](https://www.boreas.ca/pages/capdrive-technology) — CapDrive 架構說明；宣稱最多省 10× 功耗（未驗證）。
5. [Electronic Products & Technology — Boreas Technologies targets disruption of haptics sector](https://www.ept.ca/features/boreas-technologies-targets-disruption-of-haptics-sector/) — 公司背景；Chaput 於 Harvard 博士期間發明壓電驅動 IC 架構；「30+ 專利」宣稱（未驗證）。
6. [Harvard VLSIArch — 21.5 A 3-to-5V input 100Vpp output 57.7 mW 0.42% THD+N highly integrated piezoelectric actuator driver](https://vlsiarch.eecs.harvard.edu/publications/215-3-5v-input-100v-pp-output-577-mw-042-thd-n-highly-integrated-piezoelectric) — US10931199B2 的學術對應；Chaput / Brooks / Gu-Yeon Wei。
7. [Google Patents — US10931199B2, Driver for a circuit with a capacitive load](https://patents.google.com/patent/US10931199B2/en) — 單電感、雙向、高壓致動器驅動器，**可回收致動器上儲存的能量**。CapDrive 的專利地基。
8. [USPTO — US11374496, Driver for a circuit with a capacitive load](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/11374496) — 同標題續案；可變預驅動脈衝達成 ZVS/ZCS（受讓人未驗證）。
9. [Analog Devices — MAX77501 產品頁](https://www.analog.com/en/products/max77501.html) — 110 Vpk-pk、≤2 µF 壓電負載、專有能量回收機制。
10. [Analog Devices — MAX77501 Datasheet (PDF)](https://www.analog.com/media/en/technical-documentation/data-sheets/max77501.pdf) — 完整規格。
11. [Analog Devices — Energy-Saving Piezo Haptic Driver is the Touch Sensor's Best Friend](https://www.analog.com/en/resources/technical-articles/energysaving-piezo-haptic-driver-is-the-touch-sensors-best-friend.html) — 能量回收機制的電路級描述（正半波充電、負半波經 T1 反向導通回送）。**專利號查無。**
12. [MDPI Actuators 12(9) 345 — A 3-to-5 V Input, 80 Vpp Output, 2.75% THD+N, 2.9 µF Load Piezoelectric Actuator Driver with Four-Switch Buck–Boost](https://www.mdpi.com/2076-0825/12/9/345) — 第三方四開關 buck-boost 架構，**可作為迴避設計起點**。
13. [Google Patents — US12126324B2, Piezoelectric resonators for power conversion](https://patents.google.com/patent/US12126324/en) — MIT 地基專利；PCT/US2022/028043（2022-05-06），優先權 63/185,663（2021-05-07），發明人 Boles/Perreault/Lang/Bonavia。**同族地域查無。**
14. [USPTO — US12388364, DC-DC converter based on piezoelectric resonator](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/12388364) — 本輪確認標題（前輪為半驗證）。
15. [Justia — Jessica Boles, Inventions and Patent Applications](https://patents.justia.com/inventor/jessica-boles) — Boles 名下清單；US12009746 的 abstract 文字來源（PR 為功率級儲能、connected/open stages、resonant soft-charging）。
16. [arXiv 2605.15279 — Motional-Current-Sensing Method and Simplified Closed-Loop Control Strategy for Piezoelectric-Resonator-based DC-DC Converters](https://arxiv.org/abs/2605.15279) — **白空間正中心的學術首發（2026-05）**；ring-dot PT 做 motional current 感測，低延遲／低損耗／本質隔離；事件驅動控制、全 ZVS、可自啟動。
17. [USPTO — US5347870, Dual function system having a piezoelectric element](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/5347870) — **1994 年即 claim「壓電元件兼具致動器與感測器雙功能」；推算 2011–2014 到期 → 概念已公有領域。**
18. [Justia — US5347870](https://patents.justia.com/patent/5347870) — 同上之交叉確認頁。
19. [Google Patents — US4035672A, Acoustic transducer with a dual purpose piezoelectric element](https://patents.google.com/patent/US4035672) — 1977 年的雙用途壓電元件；最早期先前技術。
20. [Google Patents — US7235914B2, Piezoelectric micro-transducers, methods of use and manufacturing methods for same](https://patents.google.com/patent/US7235914) — 受讓人 **Washington State University Research Foundation**；2001-10-25 申請、2007-06-26 核准；明述同一壓電單元既作致動器亦作發電機。
21. [Justia — US7235914](https://patents.justia.com/patent/7235914) — 同上交叉確認。
22. [Google Patents — WO2006087304A1, Vorrichtung zur Energieversorgung](https://patents.google.com/patent/WO2006087304A1/de) — 壓電模組「不僅用於產生電壓，也作為感測器（特別是壓力感測器）」；2006 年，德文件。
23. [Google Patents — US9450510B2, Energy harvesting device using SSHI techniques](https://patents.google.com/patent/US9450510B2/en) — 受讓人據搜尋摘要為 **National Tsing Hua University（未驗證）**。**台灣客戶最可行的授權標的。**
24. [USPTO — US9831796, Energy harvesting device using SSHI techniques](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/9831796) — 同族。
25. [Google Patents — US9548680B2, Self power SSHI circuit for piezoelectric energy harvester](https://patents.google.com/patent/US9548680B2/en) — 受讓人據搜尋摘要為 **King Saud University（未驗證）**；同族 US20150311824A1。
26. [Google Patents — EP2579440A1, Rectifier circuit with AC side short-circuiting function and synchronized switch harvesting on inductor converter](https://patents.google.com/patent/EP2579440A1/en) — SSHI 轉換器；**受讓人查無**。美國同族 [US20140218989A1](https://patents.google.com/patent/US20140218989/ko)。
27. [Google Patents — CN204271948U, 一種自供電 P-SSHI 電路](https://www.google.com/patents/CN204271948U?cl=en) — 中國 SSHI 實用新型。
28. [USPTO — US10361356, Piezoelectric energy harvesting](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/10361356) — 能量擷取件（受讓人查無）。
29. [MIT DSpace — Ramadass & Chandrakasan, An Efficient Piezoelectric Energy Harvesting Interface Circuit Using a Bias-Flip Rectifier and Shared Inductor](https://dspace.mit.edu/bitstream/handle/1721.1/62174/Ramadass-2010-An%20Efficient%20Piezoelectric%20Energy%20Harvesting%20Interface%20Circuit%20Using%20a%20Bias-Flip%20Rectifier%20and%20Shared%20Inductor.pdf?sequence=2) — bias-flip 原始論文；較全橋整流／倍壓提升 >4×，0.35 µm CMOS。**對應專利查無。**
30. [SAGE JIMSS — Badel, Guyomar, Lefeuvre, Richard (2005), Efficiency Enhancement of a Piezoelectric Energy Harvesting Device in Pulsed Operation by Synchronous Charge Inversion](https://doi.org/10.1177/1045389x05053150) — INSA Lyon 一脈的代表論文；**該團隊專利查無**。
31. [e-peas — AEM30330](https://e-peas.com/product/aem30330/) — 官方僅述 buck-boost + MPPT，**未提 SSHI**；用於判斷 IC 廠是否持有 SSHI 專利（查無）。
32. [PatSnap — Immersion Corp. v. Meta Platforms, Haptic Feedback Patent Litigation](https://www.patsnap.com/resources/blog/litigation/immersion-corp-v-meta-platforms-haptic-feedback-patent-litigation-patsnap/) — 2024-02-09 和解＋授權；西德州；6 件專利；631 天；標的含 Quest 2 / Beat Saber / Horizon Worlds。
33. [PatSnap — Immersion Corp. v. Valve Corp.](https://www.patsnap.com/resources/blog/litigation/immersion-corp-v-valve-corp-haptic-feedback-patent-litigation-patsnap/) — 2024-05-14 因 7 件 IPR 中止；現金部位 1.324 億美元（2025-01-31）。
34. [Immersion IR — Immersion Reaches 3,500 Issued and Pending Haptics Patents](https://ir.immersion.com/news-releases/news-release-details/immersion-reaches-3500-issued-and-pending-haptics-patents) — 專利規模官方數字。
35. [Justia — Patents Assigned to Immersion Corporation](https://patents.justia.com/assignee/immersion-corporation) — 完整受讓清單入口（本輪未逐件檢視）。
36. [Lexology — After declaring itself litigation free, Immersion makes substantial cuts to its patent portfolio and puts more emphasis on technology licensing](https://www.lexology.com/library/detail.aspx?g=8df8f268-9f3c-4066-aada-151ae4c5d252) — Immersion 商業模式演變之第三方分析。
37. [Google Patents — US10856399B2, Device for generating an atmospheric-pressure plasma](https://patents.google.com/patent/US10856399) — TDK Electronics GmbH & Co. OG；Kudela / Puff / Rinner；2020-12-01 核准；PZT 與銅內電極共燒；**單一元件結合電壓轉換與電漿產生**。**同族地域查無。**
38. [TDK Electronics — Cold plasma from a single component](https://www.tdk-electronics.tdk.com/en/373562/tech-library/articles/applications-cases/applications-cases/cold-plasma-from-a-single-component/1109546) — CeraPlas 技術原理。
39. [USPTO — US6078124, Piezoelectric transformer driving circuit and driving method](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/6078124) — **既有的 PT 自我保護 claim**（偵測高壓輸出持續狀態→調整驅動頻率避免過度應力）；「自診斷隔離屏障」白空間的最近邊界。
40. [Nature Scientific Reports — Electromechanical impedance based self-diagnosis of piezoelectric smart structure using PCA and LibSVM](https://www.nature.com/articles/s41598-021-90567-y) — EMI 法可辨識虛焊、脫層、磨損、破裂；**自診斷在學術上成熟，但未與功率傳輸整合**。
41. [MDPI Electronics 13(3) 521 — Diagnostics of Piezoelectric Bending Actuators Subjected to Varying Operating Conditions](https://www.mdpi.com/2079-9292/13/3/521) — 壓電致動器退化可經阻抗／位移／電壓監測。
42. [Google Patents — EP3127172B1, Galvanic isolated piezoelectric transformer based voltage sensors](https://patents.google.com/patent/EP3127172B1/en) — 用 PT 做**外部**電壓的隔離感測（非自診斷）；灰區邊界件。
43. [Justia — US9871182, Frequency tracking piezoelectric transformer power converter with simultaneous two-parameter control](https://patents.justia.com/patent/9871182) — claim 中「電抗網路與 PT **輸入電容**構成諧振腔」；用於界定「外部致動器電容納入諧振腔」白空間的邊界。
44. [Google Patents — US5126589A, Piezoelectric driver using resonant energy transfer](https://patents.google.com/patent/US5126589A/en) — 容性負載與電感構成 L-C 諧振以達最大能量傳輸；早期先前技術。
45. [USPTO — US12520728, Energy recovery driver for PZT actuators](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/12520728) — Harvard／Boréas 之外的第三個玩家；**受讓人查無**。
46. [EPO Global Patent Index — EP4326038A1, Energy recovery driver for PZT actuators](https://data.epo.org/gpi/EP4326038A1) — 歐洲同族，2024-02-21 公開。
47. [arXiv 2110.12428 — A CMOS SoC for Wireless Ultrasonic Power/Data Transfer and SHM Measurements on Structures](https://arxiv.org/pdf/2110.12428) — **同一超音波鏈路做供電＋資料＋結構健康監測**；「三合一」在學術端已實作之證據。
48. [IOPscience Prog. Biomed. Eng. — Recent advances in transducers for through-tissue ultrasonic power transfer](https://iopscience.iop.org/article/10.1088/2516-1091/ae5f8a) — 明述「近期雙模 UPT 換能器以**同一顆壓電元件**同時做能量與資訊傳輸」；植入物領域先前技術密度高於預期。
49. [Google Patents — US20220131482A1, Piezo-Elements for Wearable Devices](https://patents.google.com/patent/US20220131482A1/en) — 三片預彎低 K 壓電元件分任擷取器／壓力感測器／觸覺器；**注意是三片而非同一片**，用於界定「同一元件」的分野。
50. [Google Patents — US6140740A, Piezoelectric transducer](https://patents.google.com/patent/US6140740A/en) — 以開關在並聯／反並聯間切換電極連接，**可控地改變壓電層的機械阻抗**；「電性可調機械阻抗」的早期先前技術。
51. [Google Patents — JPH0936452A, 圧電トランス](https://patents.google.com/patent/JPH0936452A/ja) — 1997 年日本 PT 件（日文檢索僅回到此世代）。
52. [Google Patents — JP2002016302A, 圧電トランス](https://patents.google.com/patent/JP2002016302A/ja) — 2002 年，PZT 陶瓷，含一次驅動部與二次發電部。
53. [USPTO — US7267008, Drive, transmit & receive circuit for structural health monitoring systems](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/7267008) — **單一換能器元件**＋收發切換開關（隔離驅動訊號與接收端）用於 SHM；「同一元件收發兩用」的既有件。
54. [USPTO — US12397318, Ultrasonic transducer health status monitor](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/12397318) — 以異常阻抗／污染層偵測監控超音波換能器自身健康；「元件自診斷」的近期件。
55. [Google Patents — US5703474A, Power transfer of piezoelectric generated energy](https://patents.google.com/patent/US5703474A/en) — 壓電發電能量傳輸最佳化（等待振幅到峰值再傳輸）。
56. [Google Patents — US20160346556A1, Materials, devices and systems for piezoelectric energy harvesting and storage](https://patents.google.com/patent/US20160346556) — 擷取＋儲存整合件（CPC 交集檢索的命中）。
57. [USPTO — US5691592, Actuator drive and energy recovery system](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/5691592) — 1997 年即有「單一路徑同時充電與回收能量」的致動器驅動 claim（放電閘流體＋放電電感＋回收電容）；**能量回收概念的早期先前技術，推算已到期**。
58. [USPTO CPC Definition — H02N Electric machines not otherwise provided for](https://www.uspto.gov/web/patents/classification/cpc/html/defH02N.html) — H02N 引用 H10N30/00；用於構築第 4.4 節的 CPC 檢索式。
59. [USPTO — Global Dossier Initiative](https://www.uspto.gov/patents/basics/international-protection/global-dossier-initiative) — IP5（USPTO/EPO/JPO/KIPO/CNIPA）同族查詢工具；**第 6 節第 1 題的建議執行途徑**。
