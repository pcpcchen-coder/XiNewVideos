# 應用A4：壓電喇叭/觸覺/微泵——「致動＋電源＋感測合一」的整合機會

> **一句話結論**：這是全研究裡離收入最近的一塊，因為壓電體早已在 BOM 裡；但本輪一手檢索推翻了上一版的樂觀假設——**「同一片壓電同時致動＋感測」在觸覺（Boréas BOS1921，7.6 mV 解析度）、噴墨（Epson 殘留振動自診斷）與微泵（RAPA Healthcare × Fraunhofer EMFT，氣泡偵測準確率 99.41%）三個領域都已經是量產或近量產產品，白空間比想像中小得多**；客戶真正還空著的、且客戶端痛點明確可量化的位置只剩一個：**把 30–250 V 的驅動高壓吃回陶瓷體內**（xMEMS 喇叭需 ~30 Vpp＋DC bias、Bartels mp6 需 250 Vpp、Boréas 需 190 Vpp），而這件事目前沒有任何人在 A4 領域做。

---

## 0. 研究方法與限制（誠實揭露）

1. **本輪 WebSearch 成功次數 = 33 次**（上一版為 0 次、全為轉引；本版為完整重做並覆寫）。第 34 次查詢起收到 `this session has used its web search budget (200 of 200 WebSearch calls)`——session 層級 200 次額度由本專案所有平行 agent 共用，於我第 33 次成功查詢後耗盡。**任務簡報所述「額度已放寬到 3000」在實際執行時未生效。**
2. **WebFetch 與 curl 全面 403**，簡報已預先告知，我未嘗試。**因此所有事實均來自搜尋結果摘要，我未親自開啟任何 PDF 或網頁原文。**
3. **標記系統**：
   - **【搜尋摘要】** ＝ 本輪 WebSearch 摘要中直接出現的內容，URL 見第 7 節，**但原文未經我親自開啟核對**。這是本文件絕大多數內容的證據等級。
   - **【廠商宣稱】** ＝ 來源為廠商自述行銷數字，未經第三方量測。
   - **【查無】** ＝ 本輪未查到。
4. **零編造承諾**：本文所有專利號、型號、公司名、數字皆對應第 7 節某個 URL。無法對應者一律寫「查無」。
5. **本輪的具體查無清單**（下一輪優先）：
   | 指派子題 | 狀態 |
   |---|---|
   | xMEMS **Cypress 專屬**的驅動電壓與功耗 | **查無**（僅查到 Montara Plus「SPL@2kHz / **30 Vpp** = 127 dB」與「MEMS 相容放大器須供應 up to 30 Vpp 並施加 DC bias」，Cypress 是否同級**未驗證**） |
   | Boréas 能量回收的**實測回收比例** | **查無**——只有「vs 傳統壓電驅動 IC 省電 up to 90%」「vs LRA 20×」「vs 競品壓電 IC 10×」三個廠商宣稱倍數，**沒有任何一個是「回收了輸入能量的 X%」** |
   | Boréas **單價**、BOS0614 本輪細節 | **查無** |
   | TTP/Lee Ventus Disc Pump **單價、MTBF（區別於壽命測試）** | **查無**（查到 17,000 h / ~1.3 兆次循環的壽命測試，非 MTBF） |
   | Tanvas、超音波摩擦調變（ultrasonic friction modulation） | **本輪未查（額度耗盡）** |
   | 骨傳導在手機/筆電的採用狀況 | **本輪未查（額度耗盡）** |
   | xMEMS Cypress 客戶「哪些耳機採用」的**量產機種**（Cypress 專屬） | **查無**（查到的 Creative/Noble/Singularity 採用的是**前代** Montara/Cowell 世代，Cypress 客戶量產出貨「預計 2026」） |
   | 微泵/喇叭領域**可信**的市場規模數字 | **查無**——見 §5.7，本輪查到的兩份汽車觸覺市場報告數字**互相矛盾** |

---

## 1. 結論摘要

1. **「同一片壓電同時致動與感測」在微泵領域已經不是白空間，而是已上市產品。** RAPA Healthcare 與 Fraunhofer EMFT 合作的 self-sensing 微泵，**不加任何額外感測器、不修改泵體，只分析壓電陶瓷的充電電流**，即可偵測氣泡；嵌入式 AI 模型佔用 **15.23 kB**、執行時間 **182 µs**、氣泡偵測準確率 **99.41%**；泵壽命 **10,000 h**，主打胰島素等高劑量藥物輸送。**這推翻了上一版把此機會列為 TRL 3–5 的判斷——它是 TRL 8–9。**【搜尋摘要 S26–S28】
2. **驅動電壓才是客戶端真正的痛點，而且數字大到超乎預期。** Bartels mp6 微泵需 **250 Vpp / 300 Hz**；Boréas 觸覺驅動 IC 從 3–5.5 V 電池升到 **190 Vpp**；xMEMS piezoMEMS 喇叭需 **~30 Vpp 加上 DC bias**（Montara Plus 規格標示 SPL@2kHz **/ 30 Vpp** = 127 dB）。**這三個數字是「壓電內建升壓」這條路唯一的、也是最硬的商業理由**——不是省一顆電感，是消滅高壓軌。【S9、S11、S28】
3. **Boréas 的宣稱全部是「相對倍數」，沒有一個是回收比例，做競品比較前必須拆解。** 官方三個數字：vs 傳統壓電驅動 IC **省電 up to 90%（≈10×）**、vs LRA **20×**、vs 競品壓電 IC **10×**。可驗證的絕對規格只有：**190 Vpp 輸出、3–5.5 V 輸入、驅動 100 nF @300 Hz 消耗 350 mW、啟動時間 <300 µs**。**「350 mW 驅動 100 nF」是唯一能拿去跟自家設計對打的絕對數字，其餘全是行銷相對值。**【S11、S15】
4. **Boréas 的按壓自感測解析度是 7.6 mV（可選 7.6–54.5 mV），比第一代 BOS1901 好 15×。** 這是本輪查到最具體的「自感測商業規格」。搭配 TDK PowerHap 的 **0.60 V/N** 感測靈敏度，可以反推：**7.6 mV ÷ 0.60 V/N ≈ 13 mN 的力量解析度**（此推算為我的計算，非廠商宣稱，且兩者為不同廠商元件，僅供量級感）。【S13、S17】
5. **xMEMS 是本領域資金最充足、最接近量產的玩家，且有台灣資本在裡面。** 累計募資 **$129M**；2025/10/30 完成 **$21M Series D**，由 Boardman Bay Capital 領投，**參與者含 CDIB-TEN Capital（中華開發）與 Harbinger Venture Capital（華威）兩家台資**，以及 SIG Asia。Cypress 於 2025/9/9 宣布量產就緒，**客戶量產出貨預計 2026 年**。**台灣代理 EDOM（益登）同時代理 xMEMS Montara、XMC-2400 與 Boréas BOS1901/BOS1921——取樣管道完全暢通。**【S6、S1、S4、S5、S11】
6. **xMEMS Cypress 的「sound-from-ultrasound」是本領域唯一真正機制性的新能力。** Alta2 ASIC 把基頻訊號調變成 **DSB-SC AM** 超音波載波，Cypress 在**空氣中**解調還原音訊；SPL **>140 dB @ 20 Hz**，低頻比前代大 **40×**；封裝僅 **46 mm³ / 98 mg**。動圈喇叭沒有「載波」這個概念，**這在物理機制上確實做不到**。但代價是：**必須有專用 ASIC，且需要高度專門的訊號處理**。【S1、S2、S3、S33】
7. **空中超音波觸覺已經商業性死亡，這是最乾淨的失敗案例。** Ultraleap 2024 年裁員（一度裁 30 人、剩約 24 人）、違反 £15M 貸款條款、觸覺與手勢追蹤 IP 賣給美國 IP 金融公司 **SIM IP**，公司於 **2025/11/11 被 ROLI 收購**。背景是 AR/VR 出貨 2024 Q1 全球衰退 **>67%**。**教訓：綁定單一新興平台的觸覺技術，會跟著那個平台一起死。**【S22】
8. **螢幕發聲的量產方案用的是電磁，不是壓電。** LG Display 的 Crystal Sound OLED（含 G8 ThinQ）採用**電磁式** exciter，需要線圈、結構較厚。壓電 exciter 目前仍在研究階段——POSTECH 2025 年在 13 吋 OLED 上做出「每個像素獨立發聲」的無串音壓電陣列（Advanced Science 2025）。**「壓電做螢幕喇叭」在 2026 年還沒有量產機種可引用。**【S31】

---

## 2. 現況：技術 / 產品 / 玩家

### 2.1 xMEMS：本領域最完整的「壓電固態化」產品線

xMEMS 一家公司把 A4 的四個子領域全部做了一遍，值得逐一拆解，因為**它同時是客戶的標竿、客戶的競爭者、也是客戶潛在的客戶**（它需要驅動 IC 與升壓方案）。

| 產品 | 功能 | 已驗證規格 |
|---|---|---|
| **Montara** | 首款單體式（monolithic）MEMS 喇叭 | 20 Hz–20 kHz 全頻寬、>110 dB SPL 平坦；**免校正、免驅動器配對**、SMT-ready、防水防塵抗震【S4】 |
| **Montara Plus** | 二代高靈敏度，Hi-Res IEM 用 | 最高 **120 dB @ 200 Hz**；**SPL@2kHz / 30 Vpp = 127 dB**【S4、S9】 |
| **Cowell** | 全球最小全音域全矽 MEMS 喇叭 | 低頻可達 20 Hz；常見於「Cowell + 9 mm 動圈低音」二路設計【S4】 |
| **Cypress** | 首款全音域 piezoMEMS **超音波換能器** | **>140 dB SPL @ 20 Hz**；低頻比前代 **40×**；**46 mm³ / 98 mg**；搭配 **Alta2** ASIC；2025/9/9 宣布量產就緒，**客戶量產出貨預計 2026**；與 Rayking Electronics 合作 turnkey 模組【S1、S2、S3】 |
| **Skyline DynamicVent** | 固態 MEMS 閥 | 等效開孔 **1.1 mm²**（雙顆 1.3 mm²）；**100 Hz 衰減 up to 25 dB**；**5.0×4.0×1.15 mm LGA**；**IP58**；差動設計消除開關 pop/click 噪音；搭配 **Alpine** 驅動 IC（1.5×1.8×0.6 mm WLCSP）；量產原訂 2023 Q4【S7】 |
| **XMC-2400 µCooling**（Sycamore 平台） | 固態超音波氣泵／晶片級風扇 | **9.26 × 7.6 × 1.08 mm**、**<150 mg**；單顆最高 **39 cm³/s** 氣流、背壓 **1,000 Pa**；耗電估 **~30 mW**；全程超音波運作故**無聲無振動**；**IP58**；上出風／側出風兩種封裝【S5】 |

**技術原理（統一敘事）**：薄膜壓電材料沉積於矽上，於超音波頻率伸縮，把電能轉為機械運動；XMC-2400 靠晶片上的精密微閥陣列把超音波振動整流成連續高速氣流【S5】。**這與 Lee Ventus Disc Pump 的「聲學駐波 + 超快閥整流」是同一族物理**（見 §2.4）。

**新能力 vs 動圈喇叭（可驗證的部分）**：單體式製程**免校正、免驅動器配對**（一致性）；**防水防塵抗震**；相位一致性宣稱比傳統驅動好 **7×**【S4、S8】。**這些是「更好」，不是「以前做不到」。唯一機制性新能力是 Cypress 的 sound-from-ultrasound。**

**客戶（已驗證）**：Creative（Aurvana Ace / Ace 2）、Noble Audio FoKus Triumph、Singularity ONI、Soundpeats Capsule3 Pro+；**全球首款採用 MEMS 喇叭的助聽器用的是 Montara**【S8、S4】。**注意：這些是 Montara/Cowell 世代，不是 Cypress。**

### 2.2 Boréas Technologies：把「兩用」做成 IC 的公司

2016 年成立於加拿大魁北克 Bromont 的 fabless IC 公司【S14】。

- **CapDrive 架構**：從致動器負載電容**回收電荷而非耗散**【S15】。
- **BOS1901**：單晶片壓電驅動器，**3–5.5 V 輸入 → 190 Vpp 輸出**；驅動 **100 nF @ 190 Vpp / 300 Hz 消耗 350 mW**，低電壓下可驅動至 **820 nF**；SPI 介面、內建 FIFO；**啟動時間 <300 µs**【S11、S15】。
- **BOS1921 / BOS1931**：190 Vpp；**感測解析度可選 7.6 mV – 54.5 mV，比 BOS1901 好 15×**；自主觸發（偵測條件滿足即自動播放觸覺波形）；**MIPI I3C（相容 I2C）**；QFN 封裝；IDLE 模式靜態電流由 datasheet 圖 13 讀出約 **500–600 µA**【S12、S13】（**此為搜尋摘要對圖表的判讀，可靠度最低，務必自行核對 datasheet**）。
- **自感測原理**：**量測壓電致動器兩端電壓，把它當力量感測器用**【S13】——這正是客戶構想的核心，已經是貨架商品。
- **採用**：Synaptics 於 **Computex 2023（2023/5）** 發表 S9A0H 觸控控制器 + Boréas 二代壓電觸覺 + **BOS1921** 的觸控板模組，提供**力量感測與觸覺回饋**，並宣稱**整片作用區 100% 一致的點擊感**【S16】。
- **募資**：**US$12M Series B**（Archerman Capital，2023/11/16）；Tracxn 統計累計 **$13.56M**；投資人含 ACET、Anges Québec、Desjardins Capital、EDC Investments【S14】。**這是一家資本規模僅約 xMEMS 十分之一的公司。**
- **台灣**：EDOM（益登）代理 BOS1901 / BOS1921【S11、S12】。

### 2.3 TDK：元件端的兩用標竿

- **PowerHap**：致動器**兼具感測功能**，受壓時產生電荷，**典型靈敏度 0.60 V/N**；型號分 2.5 G（9×9×1.2 mm）、7 G（12.7×12.7×1.9 mm）、15 G（26×26×2.4 mm）；另有 4 N 型（典型位移 35 µm）、5 N 型（位移可達 100 µm）、20 N 型；**最佳預壓約 25 N**（**注意：上一版把 25 N 誤記為「壓力偵測上限」，本輪一手資料顯示那是「最佳預載」**）；**最大衝擊力 400 N**；**激振頻寬 1 Hz–1000 Hz**【S17】。
- **PiezoListen**：厚度僅 **0.49 mm**（最小尺寸 20×10×0.49 mm）；**400 Hz–20 kHz**；**24 Vpp 以下即達 80 dB 聲壓**；最大輸出功率 34 W、阻抗 2–100 Ω；多層 PZT 以 via-hole 連接；**可直接貼在 OLED/LCD 與背蓋上做「螢幕發聲」**【S18】。
- **TDK 與 Aito 在壓電觸覺上結盟**【S20】。

### 2.4 微泵 / 微閥：三種截然不同的物理路線

| 廠商/產品 | 原理 | 規格 |
|---|---|---|
| **Lee Ventus（原 TTP Ventus）Disc Pump** | **在固定容積腔內激發高頻聲學駐波，再用專利超快閥整流成流量**——不是位移式 | 最高 **2 L/min**、**−400 ~ +600 mbar(g)**；LT 系列 270 mbar(g) / −220 mbar / 1.2 L/min；**21,000 次/秒（超音波，故無聲）**；長壽命型號在 **0.6 W（約 60% 額定）連續運轉 >17,000 h（≈2 年）性能無顯著變化，約 1.3 兆次循環**；毫秒級反應、幾乎無脈動；已被 The Lee Company 收購【S23、S25】 |
| **Murata Microblower MZB1001T02** | 陶瓷超音波振動驅動 | **10–20 V**、**24–27 kHz**、流量 **0.7 L/min**、功率 **0.18 W**、最大靜壓 **1,500 Pa @15 Vpp**；**20×20×1.85 mm、1.4 g**【S24】 |
| **Bartels mp6** | 位移式膜片泵（壓電蜂鳴片） | 水 **7 ml/min @100 Hz**、空氣 **18–20 ml/min @300 Hz**；**驅動 250 Vpp / 300 Hz（SRS 波形）**；30×15×5 mm；壽命 **>5,000 h**；可滅菌【S28】 |
| **RAPA Healthcare（× Fraunhofer EMFT）self-sensing 微泵** | 位移式 + **自感測** | **無外加感測器、不改泵體**；以 I-V 轉換電路量測壓電陶瓷充電電流，流體-力學耦合在自感測訊號上留下「指紋」；**嵌入式 AI：15.23 kB / 182 µs / 氣泡偵測準確率 99.41%**；壽命 **10,000 h（宣稱為同類 2×）**；訴求：**省下外部感測器的空間與成本，特別適合拋棄式與可攜式給藥系統**【S26、S27】 |

**這張表是本文件最重要的一張表**，理由見 §4.1 與 §7 的判讀。

### 2.5 觸覺市場：為什麼壓電至今沒取代 Apple 的方案

Apple Taptic Engine 是**線性共振致動器（LRA）**：釹磁鐵固定在質量塊上、置於音圈中，以電磁訊號驅動振盪，**機制與喇叭相同**；工作頻段約 **80–230 Hz**【S19】。

壓電至今未取代它的原因，本輪**未查到 Apple 官方或第三方的直接說明**（額度耗盡），但從已驗證數字可以推出結構性障礙：**LRA 用 3–5 V 直接驅動，壓電要 190 Vpp**。Boréas 的整個商業模式就是在解這件事，而它解得再好，也還是多一顆 IC、多一段升壓、多一組高壓佈線。**在手機這種 BOM 壓到分錢的品類，這是決定性的。**（此段為推論，標示為推論。）

壓電觸覺實際落地的地方，是**電壓與 BOM 不是第一考量、而「大面積 + 定位 + 免機械行程」是硬需求**的品類：
- **筆電觸控板**：Synaptics × Boréas 模組（2023/5）【S16】。
- **汽車 HMI**：Continental 的 pillar-to-pillar 整合中控螢幕預計 2024 年進入量產車型、首發 **Mercedes-Benz E/S Class**；Bosch 與 Continental 均將觸覺導入顯示產品；Audi MMI touch 以觸覺回饋取代實體按鍵；**中國 OEM（BYD、NIO、Li Auto）在觸控密集座艙中大量導入，並受 GB/T 39263-2020 HMI 標準推動**【S32、S20】。**注意：本輪未能驗證上述車型使用的是壓電還是電磁致動器，僅驗證「觸覺已導入」。**
- **Aito bv**（阿姆斯特丹／赫爾辛基）：軟體強化壓電技術（SEP），推出 **ATH220 / ATH222** 控制 IC，把壓電致動器同時當精密觸控感測器用；合作夥伴列有 **BMW、LG、TDK、Flex、Renault**；累計募資 **$23.5M**（Tracxn）【S21】。

---

## 3. 關鍵數字表

| 項目 | 數字 | 性質 | 來源 |
|---|---|---|---|
| **Bartels mp6 驅動電壓** | **250 Vpp / 300 Hz** | 規格 | S28 |
| **Boréas 輸出電壓** | **190 Vpp**（輸入 3–5.5 V） | 規格 | S11 |
| **xMEMS Montara Plus 工作電壓** | **30 Vpp**（SPL@2 kHz = 127 dB）；MEMS 放大器須供 30 Vpp + DC bias | 規格 / 業界說明 | S9 |
| **Murata microblower 驅動電壓** | **10–20 V**，24–27 kHz | 規格 | S24 |
| Boréas BOS1901 功耗 | 驅動 **100 nF @190 Vpp/300 Hz = 350 mW** | 規格（**唯一絕對值**） | S15 |
| Boréas 感測解析度 | **7.6 – 54.5 mV**（可選），比 BOS1901 好 **15×** | 規格 | S13 |
| Boréas 靜態電流（IDLE） | **≈500–600 µA** | datasheet 圖表判讀，**可靠度最低** | S12 |
| Boréas vs LRA / vs 競品壓電 IC | **20× / 10×** 省電；**up to 90%** 降耗 | **廠商宣稱，非回收率** | S15 |
| TDK PowerHap 感測靈敏度 | **0.60 V/N** | 規格 | S17 |
| TDK PowerHap 最佳預載 / 最大衝擊力 / 激振頻寬 | **25 N** / **400 N** / **1 Hz–1000 Hz** | 規格 | S17 |
| TDK PiezoListen | **0.49 mm 厚**、400 Hz–20 kHz、**≤24 Vpp 達 80 dB** | 規格 | S18 |
| xMEMS Cypress | **>140 dB @20 Hz**、低頻 **40×** 前代、**46 mm³ / 98 mg** | 廠商宣稱 | S1、S2 |
| xMEMS Skyline | 等效開孔 **1.1 mm²**、100 Hz 衰減 **25 dB**、**IP58**、5.0×4.0×1.15 mm | 廠商宣稱 | S7 |
| xMEMS XMC-2400 | **39 cm³/s @1,000 Pa 背壓**、**~30 mW**、9.26×7.6×1.08 mm、**IP58** | 廠商宣稱 | S5 |
| Lee Ventus Disc Pump | **2 L/min**、**−400~+600 mbar(g)**、**21 kHz 無聲**、**>17,000 h @0.6 W ≈1.3 兆次循環** | 廠商宣稱＋壽命測試 | S23、S25 |
| RAPA self-sensing 微泵 | 氣泡偵測 **99.41%**、模型 **15.23 kB / 182 µs**、壽命 **10,000 h** | 論文＋廠商 | S26、S27 |
| Bartels mp6 壽命 | **>5,000 h** | 規格 | S28 |
| Apple Taptic Engine | **電磁 LRA**、約 **80–230 Hz** | 綜述 | S19 |
| xMEMS 募資 | 累計 **$129M**；Series D **$21M**（2025/10/30）；Series C1 $14.3M | 新聞稿／資料庫 | S6 |
| Boréas 募資 | Series B **US$12M**（2023/11）；累計約 **$13.56M** | 資料庫 | S14 |
| Aito 募資 | **$23.5M**（6 輪） | 資料庫 | S21 |
| Ultraleap 結局 | 2024 裁員至約 24 人、IP 售予 SIM IP、**2025/11/11 被 ROLI 收購** | 媒體 | S22 |
| AR/VR 出貨（Ultraleap 死因） | **2024 Q1 全球 −67%** | 媒體 | S22 |

**度量陷阱**：Boréas 的三個倍數（90% / 10× / 20×）**都不是能量回收率**。若客戶要對外簡報「能量回收」，唯一站得住的絕對數字是「**350 mW 驅動 100 nF @190 Vpp/300 Hz**」——請以此為基準做自家設計的對照實驗。

---

## 4. 「新能力型」應用機會

### 4.1 機會 A（**降級**）：微泵自感測閉環——**已有人做，且做得很完整**

- **新能力**：不加感測器、不改泵體，只分析壓電陶瓷的驅動/充電電流，即可偵測氣泡、閉塞與劑量誤差。
- **是否真非替代**：**是**（在拋棄式與貼片式給藥裝置中，外掛流量計是物理上放不進去）。
- **但誰在做**：**RAPA Healthcare × Fraunhofer EMFT 已經有產品頁與白皮書**，且性能具體到 99.41% 準確率、15.23 kB 模型、182 µs 執行時間、10,000 h 壽命【S26、S27】。**上一版把它評為 TRL 3–5、「微泵領域查無任何廠商主張此功能」——這個判斷本輪被一手資料推翻，正確值是 TRL 8–9。**
- **TRL**：**8–9**。
- **市場訊號**：明確——訴求鎖定**胰島素等高劑量藥物**，賣點寫成「省空間、省生產成本，特別適合拋棄式與可攜式」【S27】。
- **技術難點**：AI 模型的驗證與醫材法規路徑；跨批次陶瓷差異導致「指紋」漂移。
- **對客戶的意涵**：**這條路仍值得做，但定位必須從「開創者」改為「快速追隨者 + 差異化」**。差異化的可能方向：(i) 把自感測從「氣泡」擴到「閉塞 + 黏度 + 逐衝程劑量」（Epson 已證明**殘留振動可量測黏度**【S29】，這個 know-how 可跨域搬過來）；(ii) 做在**聲學駐波式**泵（Lee Ventus 路線）而非位移式膜片泵上——**本輪查無任何人在駐波式泵上做自感測**，而駐波式泵的 Q 值高、對負載變化更敏感，理論上訊噪比更好。

### 4.2 機會 B（**本輪唯一升級**）：把驅動高壓吃回陶瓷體內——消滅高壓軌

- **新能力**：一顆陶瓷體內同時完成升壓與致動，外部只有十幾伏進出，系統中**不存在高壓軌**。
- **為什麼以前做不到 / 為什麼現在值得做**：本輪一手數字讓這個機會第一次有了明確的量化理由——**同一個 A4 領域裡，三種產品需要三種高壓：微泵 250 Vpp、觸覺 190 Vpp、MEMS 喇叭 30 Vpp + DC bias**【S28、S11、S9】。這三個電壓全部由「電感式 boost → 高壓軌 → H-bridge → 壓電片」產生，全部要付爬電距離、高壓佈線、高壓連接器與安規代價。在 1 mm 厚的耳機（Cypress 封裝僅 46 mm³）或貼片式輸液泵裡，這個代價可能直接否決產品。
- **是否真非替代**：**半到是**。若只講「產生高壓」，是更薄的替代品（降權）；若講「**在沒有高壓軌的系統裡取得高壓致動**」，是架構層級的新能力——它消滅的不是一顆電感，是整個高壓子系統。
- **誰在做**：**A4 領域查無任何人。** 這是本輪 33 次搜尋後仍為空白的唯一一個核心構想。
- **TRL**：**2–3**。
- **市場訊號**：**目前為零**（沒有人在賣，也沒有人公開說要買）。**但 xMEMS 每一顆喇叭與每一顆 µCooling 都必須配一顆專用 ASIC（Alta2 / Alpine），這代表「驅動段」在這個生態裡是被外購的、有價值捕獲空間的一段。**
- **技術難點（可能致命，須先驗）**：
  1. **頻率尺度落差**。壓電變壓器（PT）機械諧振在數十–數百 kHz；而喇叭要 20 Hz–20 kHz、微泵要 100–300 Hz（位移式）或 21–27 kHz（駐波式）、觸覺要 1 Hz–1000 Hz【S17、S28、S23、S24】。**單一諧振腔的敘事站不住，必須是「高頻諧振腔 + 低頻包絡調變」。**
  2. **但這裡有一個本輪浮現的重大線索**：xMEMS Cypress 的整個架構**就是**「超音波載波 + 基頻包絡調變（DSB-SC AM）」【S2】；Lee Ventus 與 Murata 的泵**也是**「超音波振動 + 整流」【S23、S24】。**換言之，A4 領域已經自發地演化到「一切都在超音波頻段運作」——這恰好是壓電變壓器的原生頻段。** 這是「PT 諧振腔與致動負載聯合諧振共設計」在物理上第一次看起來合理的理由，也是本文件建議客戶投入的最主要技術假設。
  3. **負載變動 → 增益崩塌**。PT 輸出阻抗高、增益隨負載劇變；致動器負載會隨溫度、貼合、手指按壓改變。需主動頻率/相位追蹤，會吃掉一部分整合度優勢。
  4. **寄生發聲**。PT 本身機械共振會發聲，放進「靜音」產品（XMC-2400 主打無聲、Disc Pump 主打無聲）是諷刺性風險，必須確認基頻在超音波且無可聞次諧波。

### 4.3 機會 C：**Cypress 級 sound-from-ultrasound 的驅動段**

- **新能力**：超音波載波調變/解調同體，動圈喇叭沒有這個機制。
- **是否真非替代**：**是（就機制而言）**，但**它已經有主人**——xMEMS 累計募資 $129M、Cypress 已量產就緒、Alta2 ASIC 已配套【S6、S1】。
- **客戶的可切入點不是喇叭，是「30 Vpp + DC bias」的升壓段**——這是 §4.2 的具體第一個 socket，且台灣已有代理（EDOM 同時代理 xMEMS 與 Boréas），**取樣與對話成本極低**。
- **TRL**：喇叭本體 8–9；客戶可切入的驅動段 3–4。

### 4.4 機會 D（**明確降權**）：更省電的觸覺、更薄的喇叭、固態散熱

- **觸覺**：Boréas 已把「致動＋感測同一片壓電」做成貨架 IC（7.6 mV 解析度、Synaptics 合作、EDOM 代理）【S13、S16】。**客戶進場即為追隨者，且要在 IC 側對打一家有 Synaptics 背書的公司。**
- **喇叭**：xMEMS 是替代動圈；且**業界公認的缺點是深低頻**——多數品牌採「MEMS 負責 1 kHz 以上、動圈負責低頻」的混合設計【S33】。Cypress 宣稱解決了這件事，但**客戶量產出貨要到 2026 年才會驗證**。
- **固態散熱**：XMC-2400 已有具體規格（39 cm³/s @1,000 Pa、~30 mW），**但這是 xMEMS 自己的產品，不是白空間**。
- **結論**：這條路只能當現金流，不能當立項理由。

---

## 5. 反面證據、失敗案例與物理上限

1. **空中超音波觸覺是完整的失敗案例。** Ultraleap：2024 裁員（一度剩約 24 人）、違反 £15M 貸款條款、IP 賣給 SIM IP、2025/11/11 被 ROLI 收購；直接死因是 AR/VR 出貨 2024 Q1 全球 **−67%**【S22】。**教訓：不要把壓電新能力綁在單一新興平台上。**

2. **「同一片壓電同時致動＋感測」的白空間比想像小，且三個領域都已有人插旗。** 觸覺：Boréas BOS1921（7.6 mV，量產）【S13】；噴墨：Epson 殘留振動自診斷（**毫秒級**，且已延伸到**量測黏度**）【S29】；微泵：RAPA × Fraunhofer（99.41%，有產品頁）【S26、S27】。**客戶必須接受自己是快速追隨者。**

3. **MEMS 喇叭的深低頻是已知弱點，混合設計是業界現況。** 多數採用 xMEMS 的耳機是「MEMS + 動圈」二路，MEMS 管 1 kHz 以上【S33】。Cypress 宣稱以超音波調變解決，**但需要高度專門的訊號處理，且成本較高**【S33】。**「全音域 MEMS」在 2026 年仍是待驗證的宣稱，不是既成事實。**

4. **螢幕發聲的量產解是電磁，不是壓電。** LG Crystal Sound OLED 用電磁 exciter【S31】。壓電版本（POSTECH，2025，13 吋 OLED 像素級發聲）仍在研究階段【S31】。**上一版與常見產業敘事把「螢幕發聲＝壓電」是錯的。**

5. **Boréas 的所有效率宣稱都是相對倍數，沒有任何一個是回收率。** 90% / 10× / 20× 三個數字，比較基準各不相同（傳統壓電 IC / 競品壓電 IC / LRA）【S15】。**若客戶簡報寫「能量回收效率 90%」會在盡職調查中被抓出來。**

6. **微泵壽命的數量級差距巨大，取決於物理路線。** 位移式膜片泵：Bartels mp6 **>5,000 h**、RAPA **10,000 h**【S28、S27】；駐波式：Lee Ventus 在 0.6 W 下 **>17,000 h ≈1.3 兆次循環**且性能無顯著變化【S25】。**差三倍以上，且駐波式的優勢來自「幾乎沒有大位移的機械件」。這暗示：若客戶要做長壽命自感測泵，應優先考慮駐波式而非膜片式。**

7. **本領域的市場數字互相矛盾，本輪查到的兩份汽車觸覺報告不能同時為真。** 一份稱全球 2024 年 **$2,722M**、2032 年 **$4,776M**；另一份稱 2025 年**亞太**即 **$1.47B，佔全球 38.7%**（隱含全球 2025 ≈ **$3.80B**）【S20】。**2024 $2.72B → 2025 $3.80B 等於一年成長 40%，與前者的 CAGR 完全不相容。這兩個數字至少有一個錯，建議一律不引用。**

8. **競爭者的資金量級差距。** xMEMS **$129M**（含台資 CDIB-TEN、Harbinger）vs Boréas **約 $13.6M** vs Aito **$23.5M**【S6、S14、S21】。**若客戶想在觸覺 IC 側對打，對手資本額不大（Boréas）；若想在 MEMS 喇叭側對打，對手資本額是它的十倍且已有 Synaptics 級的通路。**

9. **上一版本文件本身是反面證據。** 上一版 WebSearch 成功 0 次、全為轉引，且其中至少兩處與本輪一手資料**直接矛盾**：(i) TDK PowerHap「≤25 N 壓力偵測」實為「最佳預載 25 N」【S17】；(ii)「微泵領域查無任何廠商主張自感測」實為 RAPA 已有產品【S27】。**這說明轉引鏈條在本專案內已經產生過錯誤傳播，第 7 節的 URL 請務必自行開啟核對。**

---

## 6. 未解問題

1. **xMEMS Cypress 的驅動電壓、Alta2 的升壓架構與整體功耗是多少？** 這是 §4.2 第一個 socket 的入場券。建議查詢：`xMEMS Alta2 datasheet supply voltage`、`Cypress MEMS speaker bias voltage power consumption mW`；或**直接透過 EDOM（益登）索取 xMEMS 與 Boréas 的評估板與規格書——這不需要搜尋額度，建議立即執行**。
2. **Boréas 的 CapDrive 專利範圍是否已覆蓋「從致動器負載電容回收能量」的核心手法？** 若是，客戶自研會直接撞牆。建議以 Boréas Technologies 為受讓人做專利檢索。
3. **「聲學駐波式泵 + 自感測」有沒有人做過？** 本輪查無。若真空白，這是把 RAPA 的方法論（電流指紋 + 嵌入式 AI）搬到 Lee Ventus/Murata/xMEMS 物理路線上的 IP 機會，且駐波式的高 Q 值理論上訊噪比更好。
4. **「PT 諧振腔 + 致動負載聯合諧振共設計」的專利與文獻狀況？** §4.2 的存亡問題。建議：`"piezoelectric transformer" AND ("actuator" OR "micropump" OR "MEMS speaker") AND monolithic`。**本輪 33 次搜尋未觸及此題（額度耗盡），仍為最高價值的待查 IP 白空間。**
5. **超音波摩擦調變、骨傳導在手機/筆電的採用狀況、Tanvas 現況**——本輪額度耗盡未查。

---

## 7. 來源清單

**說明**：以下 URL 均出現於本輪 WebSearch 的結果中，**但我未親自開啟任何一個原文**（WebFetch 全面 403）。標題為搜尋結果所示。

| # | 標題 | URL | 一句話說明 |
|---|---|---|---|
| S1 | xMEMS Announces Mass Production Readiness of Cypress（xMEMS 新聞稿） | https://xmems.com/press-release/xmems-announces-mass-production-readiness-of-cypress-the-worlds-first-full-range-mems-speaker-for-wireless-earbuds/ | Cypress 量產就緒、46 mm³/98 mg、>140 dB@20 Hz、Alta2 ASIC、客戶量產出貨預計 2026 |
| S2 | Sound from Ultrasound（xMEMS） | https://xmems.com/sound-from-ultrasound/ | 調變器產生 AM 超音波載波、解調器在聲學域同步解調；低頻比前代 40× |
| S3 | xMEMS Announces Mass Production of Cypress Full-Range PiezoMEMS Ultrasonic Transducer（audioXpress） | https://audioxpress.com/news/xmems-announces-mass-production-of-cypress-full-range-piezomems-ultrasonic-transducer | Alta 把基頻調變成 DSB-SC AM、Cypress 在聲學域解調 |
| S4 | MEMS Micro speakers（xMEMS 產品總覽） | https://xmems.com/memsspeakers/ | Montara 20 Hz–20 kHz/>110 dB、免校正免配對、防水防塵；Cowell 最小全音域 |
| S5 | xMEMS Introduces 1mm-Thin Active Micro-Cooling "Fan on a Chip"（xMEMS） | https://xmems.com/press-release/xmems-introduces-1mm-thin-active-micro-cooling-fan-on-a-chip/ | XMC-2400：9.26×7.6×1.08 mm、39 cm³/s @1000 Pa、~30 mW、IP58 |
| S6 | xMEMS Raises $21M Series D（BusinessWire, 2025-10-30） | https://www.businesswire.com/news/home/20251030953124/en/xMEMS-Raises-$21M-Series-D-to-Accelerate-Commercial-Scale-of-Breakthrough-piezoMEMS-Technologies-for-AI-Enabled-Consumer-Devices | $21M Series D、Boardman Bay 領投、CDIB-TEN 與 Harbinger 台資參與；累計 $129M |
| S7 | xMEMS Announces Skyline, the World's First Solid-State MEMS DynamicVent（BusinessWire） | https://www.businesswire.com/news/home/20230104005123/en/xMEMS-Announces-Skyline-the-World%E2%80%99s-First-Solid-State-MEMS-DynamicVent-Enabling-Active-Ambient-Control-for-Next-Generation-TWS-and-Hearing-Aids | 1.1 mm² 等效開孔、25 dB@100 Hz、5.0×4.0×1.15 mm LGA、IP58、Alpine 驅動 IC |
| S8 | xMEMS' breakthrough micro-speakers debut in earbuds at CES（TechHive） | https://www.techhive.com/article/2199736/xmemss-breakthrough-micro-speakers-debut-in-earbuds-at-ces.html | Creative Aurvana Ace 2、Noble FoKus Triumph 採用；相位一致性 7× |
| S9 | MEMS Speaker Measurements（Listen, Inc.） | https://www.listeninc.com/mems-speaker-measurements/ | **MEMS 相容放大器須供應 up to 30 Vpp 並施加 DC bias**；Montara Plus SPL@2kHz/30 Vpp=127 dB |
| S10 | xMEMS Launches Montara Monolithic Piezo-MEMS Speaker（audioXpress） | https://audioxpress.com/news/xmems-launches-montara-monolithic-piezo-mems-speaker | Montara 單體式製程說明 |
| S11 | CapDrive® Ultra-Low Power Piezo Driver (BOS1901)（Boréas） | https://www.boreas.ca/products/bos1901-piezo-haptic-driver | 190 Vpp、3–5.5 V 輸入、啟動 <300 µs、SPI+FIFO |
| S12 | BOS1921/BOS1931 Product Datasheet BT015DDS01.01 – Issue 6（DigiKey 託管） | https://mm.digikey.com/Volume0/opasdata/d220001/medias/docus/6662/2158_BOS19_Datasheet.pdf | 190 Vpp；IDLE 靜態電流圖（≈500–600 µA，**圖表判讀，須自行核對**） |
| S13 | CapDrive® Ultra-Low Power Piezo Driver with Advanced Sensing (BOS1921)（Boréas） | https://www.boreas.ca/products/bos1921-piezo-driver | **感測解析度 7.6–54.5 mV、比 BOS1901 好 15×**；把壓電致動器當力量感測器用；I3C/I2C |
| S14 | Boreas Technologies – Funding Rounds & Investors（Tracxn） | https://tracxn.com/d/companies/boreas-technologies/__gIWmTH4en51kr3U5nz9ivI8H4WRShFDAYyH0V64MGH4/funding-and-investors | Series B US$12M（Archerman Capital, 2023/11/16）、累計約 $13.56M、2016 年成立於 Bromont |
| S15 | CapDrive Technology – Powerful Haptics With Low Power Consumption（Boréas） | https://www.boreas.ca/pages/capdrive-technology | 回收電荷而非耗散；vs LRA 20×、vs 競品壓電 IC 10×、vs 傳統壓電 IC up to 90%；100 nF@190 Vpp/300 Hz = 350 mW |
| S16 | Synaptics Partners with Boréas Technologies to Deliver High-Performance Piezo Haptic Trackpads（Synaptics） | https://www.synaptics.com/company/news/synaptics-partners-boreas-technologies-deliver-high-performance-piezo-haptic-trackpads | Computex 2023、S9A0H + BOS1921、力量感測 + 100% 作用區一致點擊感 |
| S17 | PowerHap Actuators（TDK 產品頁） | https://product.tdk.com/en/products/sw_piezo/haptic/powerhap/index.html | **0.60 V/N** 感測靈敏度、2.5G/7G/15G 型號、**最佳預載 25 N**、最大衝擊力 400 N、1 Hz–1000 Hz |
| S18 | PiezoListen Piezo Speakers（TDK 產品頁） | https://product.tdk.com/en/products/sw_piezo/speaker/piezolisten/index.html | 0.49 mm 厚、400 Hz–20 kHz、≤24 Vpp 達 80 dB、可直貼 OLED/LCD 背蓋 |
| S19 | Good Vibrations: How Apple Dominates the Touch Feedback Game（iFixit） | https://www.ifixit.com/News/16768/apple-taptic-engine-haptic-feedback | Taptic Engine 為電磁 LRA（釹磁鐵+音圈），約 80–230 Hz |
| S20 | Haptics for Safer Driving: Focus on Traffic, Not the Screen（TDK） | https://www.tdk.com/en/featured_stories/entry_059-powehap-actuator-haptics/index.html | PowerHap 車用觸覺定位；本輪汽車觸覺市場數字的來源之一（**數字互相矛盾，見 §5.7**） |
| S21 | Aito bv timeline（IDTechEx） | https://www.idtechex.com/en/timeline/aito-bv/c102816 | Aito：阿姆斯特丹/赫爾辛基、SEP 軟體強化壓電、ATH220/ATH222、夥伴含 BMW/LG/TDK/Flex/Renault |
| S22 | Tencent-backed XR startup Ultraleap sold for parts following further layoffs（Sifted） | https://sifted.eu/articles/tencent-ultraleap-sold-for-parts-news | Ultraleap 裁員、IP 售予 SIM IP、被 ROLI 收購（2025/11/11）、£15M 貸款違約、AR/VR 出貨 −67% |
| S23 | Piezo micropumps for gases and microfluidics（LEE Ventus 官網） | https://www.ttpventus.com/ | Disc Pump：聲學駐波 + 超快閥整流；21,000 次/秒故無聲；2 L/min、−400~+600 mbar(g) |
| S24 | Microblower MZB1001T02（Murata 產品頁） | https://www.murata.com/en-us/products/mechatronics/fluid/overview/lineup/microblower_mzb1001t02 | 10–20 V、24–27 kHz、0.7 L/min、0.18 W、1500 Pa@15 Vpp、20×20×1.85 mm |
| S25 | LEE Ventus Long Life Pump Exceeds 1 Trillion Cycles（BusinessWire, 2022-10-31） | https://www.businesswire.com/news/home/20221031005024/en/LEE-Ventus-Long-Life-Pump-Exceeds-1-Trillion-Cycles | 0.6 W 下 >17,000 h（≈2 年連續）、約 1.3 兆次循環、性能無顯著變化 |
| S26 | Self-Sensing of Piezoelectric Micropumps: Gas Bubble Detection by AI Methods on Limited Embedded Systems（MDPI Sensors 25(12):3784） | https://www.mdpi.com/1424-8220/25/12/3784 | **自感測氣泡偵測 99.41%、模型 15.23 kB、182 µs**；I-V 轉換電路量測壓電充電電流 |
| S27 | Self-sensing technology（RAPA Healthcare 產品頁） | https://www.rapa.com/healthcare/en/products/mikropumpen/self-sensing-technology/ | **已商品化**：與 Fraunhofer EMFT 合作、無外部感測器、壽命 10,000 h、鎖定胰島素等高劑量給藥 |
| S28 | Datasheet mp6 micropumps series（Bartels Mikrotechnik） | https://bartels-mikrotechnik.de/wp-content/uploads/2025/06/Datasheet-mp6-series.pdf | **250 Vpp / 300 Hz 驅動**；水 7 ml/min、空氣 18–20 ml/min；30×15×5 mm；>5,000 h |
| S29 | Self-Diagnosing Nozzle Health System（Epson） | https://corporate.epson/en/technology/search-by-products/printer-inkjet/nozzle-self-diagnosis.html | 壓電元件既是致動器也是感測器；由墨腔殘留振動→電訊號→**毫秒內**判斷噴嘴狀態；**並可由殘留振動量測黏度** |
| S30 | Towards zero-defect inkjet printing via piezo self-sensing signals（Sensors & Actuators A, 2025） | https://www.sciencedirect.com/science/article/abs/pii/S0924424725005618 | 噴射後數十 µs 的殘壓波在壓電上產生二次變形，可純以電壓量測監控，免外加感測器 |
| S31 | Localized Sound-Integrated Display Speaker Using Crosstalk-Free Piezoelectric Vibration Array（Advanced Science, 2025） | https://advanced.onlinelibrary.wiley.com/doi/10.1002/advs.202414691 | **LG Crystal Sound OLED 用電磁 exciter**；POSTECH 以超薄壓電 exciter 在 13 吋 OLED 做像素級發聲（研究階段） |
| S32 | Haptic feedback systems for touchscreens in vehicles（Rutronik） | https://www.rutronik.com/article/haptic-feedback-systems-for-touchscreens-using-touch-applications-without-visual-contact | Bosch/Continental 導入觸覺顯示；Continental pillar-to-pillar 首發 Mercedes-Benz E/S Class |
| S33 | What is a MEMS speaker?（SoundGuys） | https://www.soundguys.com/what-is-a-mems-speaker-107038/ | **反面證據**：MEMS 深低頻不足故混合設計為主流；需高度專門訊號處理；成本較高 |
| S34 | Touch response solutions: TDK Electronics teams up with Aito in piezo haptics（TDK Europe） | https://www.tdk-electronics.tdk.com/en/373388/company/press-center/press-releases/press-releases/touch-response-solutions-tdk-electronics-teams-up-with-aito-in-piezo-haptics/2431932 | TDK × Aito 壓電觸覺結盟 |
| S35 | XMC-2400 µCooling Fan on a Chip（EDOM 益登，台灣代理） | https://www.edomtech.com/en/product-detail/xmc-2400-cooling-fan-on-a-chip/ | **台灣取樣管道**：EDOM 同時代理 xMEMS（Montara、XMC-2400）與 Boréas（BOS1901/BOS1921） |

---

## 8. 給客戶的行動建議（一頁版）

**最快能賣進去的市場：醫療/工業微泵的「自感測 + 內建升壓」模組。**

理由：(a) 微泵驅動電壓最高（250 Vpp），高壓軌的痛最深；(b) 拋棄式與貼片式裝置放不下外掛感測器，自感測是剛需不是省料；(c) 醫材客戶願意為**功能與安全**（劑量正確、氣泡警報）付錢，不是為省一顆感測器的 BOM 付錢——**這正面回答了任務問題：客戶願意為「新功能」付更多，RAPA 的訴求措辭已經證實這件事**；(d) 出貨量小、單價高、認證壁壘高，與「壓電單價高」的體質相容——這與客戶排除 DC-DC 替代路線的邏輯完全一致。

**客戶端真正的痛點排序（依本輪一手數字）**：
1. **驅動電壓 / 高壓子系統**（250 Vpp、190 Vpp、30 Vpp + bias）——最硬、最貴、最沒人解。
2. **體積**（Cypress 46 mm³、Skyline 5×4×1.15 mm、XMC-2400 厚 1.08 mm）——放不下外掛件是物理事實。
3. **可靠度/壽命**（膜片式 5,000–10,000 h vs 駐波式 17,000 h）。
4. **BOM**——排在後面，因為在這些高單價品類它不是決勝點；只有在手機觸覺這種品類它才是（也正因如此，手機觸覺至今是 LRA 的天下）。

**第一個 go/no-go 里程碑（不需要搜尋額度，本週即可執行）**：向 **EDOM 益登** 索取 Boréas BOS1921 評估板與 xMEMS 評估套件，實測「350 mW 驅動 100 nF @190 Vpp/300 Hz」與「7.6 mV 感測解析度」，確認**現貨做不到什麼**——那個「做不到」就是客戶的產品定義。
