# 可靠性、失效模式、標準與驗證：投入研發時的工程風險清單

> 一句話結論：壓電元件在「低場強、間歇驅動、位移導向」的用法（致動器、噴墨頭、微泵）已有 10^10～10^11 次循環的量產級可靠性證據；但客戶想要的「主動/被動兩用、持續高功率/高場強驅動」用法，落在一個**幾乎沒有現成壽命資料、也沒有現成認證路徑**的空白區──真正的攔路虎不是單一失效模式，而是「自發熱 → Qm 掉 → 損耗再升」的正回饋，加上「共振頻率會隨溫度、老化、預壓漂移」對閉迴路電路的系統級衝擊，以及 2027 年到期的 RoHS 含鉛豁免。

---

## 0. 研究方法與限制（誠實揭露）

- **WebFetch 全程未使用**：依任務說明，本環境 egress policy 全面封鎖 WebFetch，任何 URL 都會回 403。本報告 100% 依賴 WebSearch 回傳的「連結清單 + 模型彙整摘要」。
- **實際只完成 16 次 WebSearch，未達任務要求的 25–35 次**。原因：第 17 次查詢時收到系統回覆 `this session has used its web search budget (200 of 200 WebSearch calls)`──這是**整個 session（含平行運作的其他子代理）共用的全域上限**，非本代理個人耗盡。此限制在我規劃階段無法預知。**這是本報告最大的品質風險，請下游統整時把本篇的覆蓋率視為「約 50–60%」。**
- **因此明確查無 / 未查到的題目（下一輪務必補）**：
  1. 超音波焊接／清洗換能器（Langevin 堆疊）的實際失效統計、預壓螺栓鬆脫、喇叭與 booster 疲勞──**完全沒查到**，這是最接近「持續高功率」的成熟工程參考，缺口很大。
  2. Nanomotion（HR 系列）、PiezoMotor（PiezoLEGS）的官方壽命規格──**查無**，只拿到 Physik Instrumente PILine 的數字。
  3. Kyocera 噴墨頭壽命規格、TTP Ventus Disc Pump 的 MTBF──**查無**。
  4. DO-160、MIL-STD-883、ISO 13485、IEC 60601 對壓電元件的具體認證路徑──**查無**（搜尋預算已耗盡前未能發出該次查詢）。
  5. IEC 63041 系列（壓電感測器）的實際內容與涵蓋範圍──**查無**，搜尋只回傳 IEEE 176 相關結果，並明確說「did not return specific information about IEC 63041」。
  6. 黏著層潛變、焊點疲勞、預壓機構隨溫度變化的定量資料──**查無**。
  7. 壓電元件的 EMI 傳導/輻射實測資料──**查無**（只間接從 MLCC 與壓電變壓器資料推論）。
- **交叉驗證程度**：凡標示「未驗證」者，代表只從單一搜尋摘要得知，未能用第二來源比對，且無法用 WebFetch 讀原文確認。
- **本報告不含任何我編造的專利號、型號或數字。** 所有數字都可對回第 7 節的來源編號。

---

## 1. 結論摘要

1. **最致命的不是單點失效，是熱正回饋。** 壓電陶瓷在高振速下 Qm「隨振幅急遽衰減」，且在自發熱條件下量到的 Qm 明顯低於用短脈衝（burst/transient）法量到的值──也就是說**用一般阻抗分析儀量到的 Qm 會系統性高估實機表現**［S4］［S5］［S6］。損耗轉成內熱、溫升再降低 Qm，構成惡性循環，文獻直接用「prone to self-heating and thermal run-away」描述［S9］。
2. **有一條被實驗證實的硬牆：最大振速約 1 m/s。** Uchino 指出存在臨界驅動電壓與最大振速，超過後壓電體「drastically increases the heat generation and becomes a ceramic heater」；Penn State 開發的高功率材料可達 >1 m/s，功率密度約為市售 hard PZT 的 10 倍［S8］。這意味著**市售 hard PZT 的實用振速上限約 0.1 m/s 量級**，是設計功率密度時的第一道天花板。
3. **溫度對「兩用元件」的傷害是雙重的，且數字很大。** Stanford 於 APEC 2024 報告：PZT 諧振器從 25°C 升到 150°C，**k² 下降 25%、Qm 下降 80%**［S15］。k² 掉表示能量轉換能力掉、Qm 掉表示損耗暴增──這兩個正好是「主動/被動兩用」設計同時依賴的兩個參數。
4. **材料的破壞極限已有具體數字。** 同一份整理指出，測到破壞時鈮酸鋰（LiNbO₃）在 **57 dBm（約 500 W）、電流密度超過 0.58 A/mm²** 發生破壞性失效；PZT 則先出現 Qm 衰減、阻抗改變與電壓/電流波形失真［S15］。另外業界慣例是**最高操作溫度取居里溫度的一半**（PZT Tc≈320°C → 實用上限約 160°C；LN Tc≈1150°C）［S15］。
5. **多層結構的頭號失效模式是「絕緣劣化導致短路」，不是陶瓷裂開。** 其次是內電極邊緣的應力集中（未被電極覆蓋的未極化區限制變形）、銀遷移（尤其 plate-through 電極設計）、界面剝離與熱疲勞［S11］［S12］［S13］。
6. **但「低場強致動」這條路的可靠性已被證明到荒謬的程度**：PI PICMA 全陶瓷封裝多層致動器經 NASA 火星任務長期測試，**10^11（1000 億）次循環後零失效、仍保有原始位移的 96%**；工業界的常用目標是 10^10 次；相較傳統高分子塗覆多層致動器壽命提升至少 10 倍［S16］［S17］［S18］。**這是本題最有力的正面證據，但要注意它是低振速、低自發熱的工況，不能直接外推到高功率兩用元件。**
7. **頻率漂移是系統級（而非元件級）的真正難題。** 傳統壓電陶瓷諧振器即使用最好的材料與強制老化製程，穩定度仍被限制在 **0.03%/decade** 附近［S22］；且諧振頻率隨老化「持續上升」［S21］。任何靠共振點工作的兩用元件，其閉迴路控制器必須有寬捕捉範圍 + 主動追頻，這會吃掉一部分「高整合度」的效率優勢。
8. **法規時鐘正在跑：RoHS 含鉛豁免 7(c)-I 到 2027/6/30 到期**，另新增 7(c)-VI 專門涵蓋 PZT 壓電陶瓷與 PTC 陶瓷、到 **2027/12/31**；相關條文自 **2026/7/1 生效**，續期申請須在到期前 18 個月提出（亦即 2026/6/30 前）［S31］［S32］。以今日（2026/7/31）看，**本輪續期窗口已關閉**，新產品若在 2028 年後量產進歐盟，含鉛 PZT 的法規地位必須重新盡職調查。

---

## 2. 現況：技術 / 產品 / 玩家

### 2.1 已量產、可當作「最接近的成熟工程參考」的四類

| 類別 | 代表玩家 | 工況特徵 | 對本題的參考價值 |
|---|---|---|---|
| 多層致動器 | Physik Instrumente (PICMA)、CTS、TOKIN／KEMET | 低振速、準靜態～kHz、高場強 DC 偏壓 | ★★★★★ 壽命資料最完整；但**不是**高功率共振工況 |
| 壓電噴墨頭 | Epson (PrecisionCore / Micro Piezo)、Fujifilm Dimatix (Samba) | 每個壓電元件約 **50,000 次/秒** 連續射出［S24］ | ★★★★★ 唯一有「超高循環數 + 量產良率」證據的高頻應用 |
| 超音波馬達 | Physik Instrumente (PILine) | 高振速、摩擦耦合、連續運轉 | ★★★★ 最接近高功率共振；但壽命被**摩擦磨耗**而非陶瓷本身限制 |
| 壓電微泵 | Bartels (mp6 / BP7) | 連續共振驅動、無機械閥 | ★★★ 壽命規格明確但數量級低（5,000 h） |

### 2.2 已經失敗／萎縮的參考案例：壓電變壓器

壓電變壓器（Rosen 型）曾在 CCFL 背光升壓找到殺手級應用，做出更薄更輕的背光模組；但隨 LED 背光取代 CCFL，**高壓壓電變壓器產量下滑，許多專為 CCFL 設計的驅動 IC 已停產**［S27］。技術面上，PZT-based Rosen 變壓器被指出的內在缺陷是「high dielectric loss and thermal instability under large drive conditions」，直接侵蝕效率與長期可靠性［S28］。近年學界改用鈮酸鋰重做（radial-mode LN Rosen transformer）［S28］，正是為了繞開 PZT 的高場強熱不穩定。

**這個案例對客戶的意義非常直接**：壓電變壓器不是輸給「成本」，是輸給「應用消失 + 大驅動下熱不穩定」。做兩用元件時，若你的價值主張依賴單一應用，會有同樣的系統性風險。

### 2.3 標準地圖（現況比想像中破碎）

- **IEEE 176-1987《IEEE Standard on Piezoelectricity》已被列為 Inactive-Withdrawn（已撤銷）**［S19］［S20］。這是壓電材料常數定義的聖經級文件，撤銷代表**目前沒有一份現行的、統一的壓電量測基準標準**；業界仍在引用它，但引用的是一份已無效力的文件。1990 年代曾有修訂計畫的公開紀錄［S21a］，但未見完成品。
- **IEC 60483:1976** 《Guide to dynamic measurements of piezoelectric ceramics with high electromechanical coupling》仍是 IEC 主要的動態量測指引：涵蓋簡單振動模態的導納特性與等效電路、諧振器參數與材料常數的決定方法［S22a］［S23］。**注意發行年份是 1976 年**──它處理的是小訊號線性行為，對高功率非線性幾乎沒有著墨。
- **IEC 60642** 系列：壓電陶瓷諧振器與諧振器單元（頻率控制與選擇），含 60642-2（使用指引）、60642-3（標準外形）［S23］。
- **EN 50324-1**：壓電陶瓷材料與元件的性質，Part 1 為術語與定義［S23a］。
- **IEC 63041**：任務指定要查的壓電感測器系列標準，**本輪搜尋查無實質內容**。
- **AEC-Q200 Rev E（2023/3/20）** 是被動元件的車規應力測試標準［S25］，適用範圍為被動元件（電阻、電容、電感、諧振器、繼電器等）［S26］。**搜尋未能證實 AEC-Q200 有專屬於「壓電致動器」或「主動/被動兩用元件」的元件分類**──這正是問題所在：一顆同時當致動器與被動元件的東西，在 AEC 的分類表上**沒有家**。搜尋摘要另提到車用壓電蜂鳴器的認證循環長達 **18–24 個月**［S25a，未驗證，來自市場研究網站摘要，可信度低，僅列為量級參考］。
- **隔離安規**：若走高壓/隔離路線，關鍵是 IEC 62368-1 的 **DTI（distance through insulation）≥ 0.4 mm**（峰值工作電壓 >71 V 的補強/加強絕緣），但標準允許以「熱循環 + 濕度處理 + 高壓 AC withstand」測試取代 DTI 尺寸要求［S29］［S30］；爬電距離依 Table 28，加強絕緣、污染等級 2 下約從 50 V RMS 的 0.6 mm 到 600 V RMS 的 >10 mm［S29a］。隔離元件本身另走 **UL 1577**（例：V_ISO 5.7 kV）與 **IEC 60747-17**（例：V_IORM 1767 V）［S30a］。

---

## 3. 關鍵數字表

| 項目 | 數值 | 條件／備註 | 來源 |
|---|---|---|---|
| 最大振速（實用高功率材料） | **> 1 m/s** | Penn State 開發材料；功率密度約市售 hard PZT 的 10× | S8 |
| 超過臨界振速的後果 | 發熱急遽上升，元件「變成陶瓷加熱器」 | 存在臨界驅動電壓 | S8 |
| Qm 對振幅的敏感度 | 隨振幅**急遽衰減**，先快降後穩定於某一位準 | 自發熱條件下量值明顯低於 burst 法 | S4, S5, S6 |
| 溫度 25→150°C 對 PZT 諧振器 | **k² −25%、Qm −80%** | Stanford, APEC 2024 | S15 |
| LiNbO₃ 破壞極限 | **57 dBm、電流密度 > 0.58 A/mm²** | 測到失效 | S15 |
| 居里溫度 | PZT ≈ **320°C**；LiNbO₃ ≈ **1150°C** | 業界實用上限慣取 Tc 的一半 | S15 |
| Hard PZT 矯頑場 | **> 15 kV/cm** | Soft PZT 為 2.5–15 kV/cm | S14 |
| Soft PZT 非線性起始 | 約 **0.2 kV/cm** 開始非線性；約 **1.5 kV/cm** 前仍近線性 | 遠低於矯頑場──非線性比去極化早很多發生 | S14 |
| 陶瓷局部放電起始場強 | BaTiO₃ MLCC（1 mm 厚）**< 1.5 kV/mm** | 壓電陶瓷的 PD 起始場強**遠低於環氧樹脂** | S14a |
| 多孔 PZT 崩潰 | 無法施加超過 **16–24 kV/cm** | 多孔結構（能量擷取用）特例 | S14 |
| PI PICMA 壽命 | **10^11 次循環零失效，保有 96% 原始位移**（NASA 火星任務測試） | 工業常用目標 10^10 次；較高分子塗覆型壽命 ≥10× | S16, S17, S18 |
| PZT 薄膜疲勞 | 壓電性質穩定至 **10^10 次**；**<001> 取向幾乎無極化疲勞**，**<111> 快速疲勞** | 電極材料影響大：RuO₂ 電極的 TDDB 與疲勞表現較佳 | S33 |
| Epson 噴墨壓電元件 | 每顆每秒射出約 **50,000 次** | 噴嘴約 20 μm 直徑，墨點約 40 μm | S24 |
| PI PILine 超音波馬達 | 行程 **> 2,000 km** 或 **MTBF 20,000 h** | 依操作模式；壽命由摩擦耦合件決定 | S34 |
| Bartels mp6 / BP7 微泵 | **> 5,000 h** | 無移動閥件、unibody | S35, S36 |
| 噴墨頭現場壽命期望 | **3–4 年**（產業訪談口徑，**未驗證**） | 非原廠規格 | S26a |
| 陶瓷諧振器頻率老化極限 | **0.03 %/decade** | 即使用高穩定材料 + 強制老化製程仍受限 | S22 |
| MLCC 可聽噪音頻段 | **20 Hz–20 kHz** | 陶瓷振動經焊點傳到 PCB，PCB 當振膜 | S37 |
| IEC 62368-1 DTI | 加強/補強絕緣 **≥ 0.4 mm**（峰值工作電壓 >71 V） | 可用熱循環+濕度+AC withstand 測試豁免尺寸 | S29, S30 |
| RoHS 含鉛豁免 | 7(c)-I 至 **2027/6/30**；新設 7(c)-VI（PZT/PTC 陶瓷）至 **2027/12/31**；2026/7/1 生效 | 續期申請須提前 18 個月 | S31, S32 |
| 車規壓電蜂鳴器認證週期 | **18–24 個月**（**未驗證**，來自市場研究摘要） | 僅作量級參考 | S25a |

---

## 4. 「新能力型」應用機會

本節從我負責的「可靠性/標準」視角出發，只列出**因為壓電體同時是致動器與感測器、且陶瓷本體同時是機械共振器與電氣絕緣體**，才成立的能力。每一項都誠實標註是否為非替代性。

### 4.1 元件自體健康監測（Self-Sensing / 元件即自身的 PHM 感測器）

- **新能力是什麼**：同一顆壓電體在致動的空檔（或同一波形的特定相位）反過來當感測器，讀出自己的機械狀態，即時判定「這一發有沒有正常動作」。這在系統上等於**每一顆功率元件都自帶 100% 覆蓋率的 built-in self-test，且不需要額外感測器、不需要額外接點**。
- **為什麼以前做不到**：電感、電容、磁性變壓器沒有可讀取的機械自由度；要做健康監測必須外掛電流/溫度感測器，成本與接點數都上升，且只能量電氣量，量不到機械退化。
- **是否真的非替代性**：**是（真新能力）**。這不是把某個元件做小做便宜，是系統中原本不存在的一條資訊通道。
- **誰在做**：**Epson 已經量產化**──PrecisionCore 的自我診斷噴嘴健康系統明確描述為「利用壓電晶體本身的力量提升可靠度……壓電元件能產生電壓，在毫秒內偵測自己是否正常射出，具備近乎即時的自我診斷能力」［S24a］。
- **TRL**：噴墨領域 **TRL 9**（已量產）；移植到功率/被動元件領域約 **TRL 3–4**（未見公開實作）。
- **市場訊號**：Epson 自稱每年生產超過 1,500 萬台印表機、印字頭設計為與機器同壽命［S24］──這代表自感測是他們用來把「不可更換印字頭」做成商業模式的支柱技術，商業價值已被驗證。
- **技術難點**：(a) 高壓驅動與 mV 級感測訊號共用同一對電極的隔離與時序切換；(b) 感測靈敏度會隨老化/溫度漂移，需要自校正基準；(c) 電荷放大器的共模承受能力。

### 4.2 陶瓷本體同時作為「機械共振器 + 加強絕緣屏障」的功率+訊號隔離

- **新能力是什麼**：一塊陶瓷同時提供能量傳輸路徑與安規隔離。**IEC 62368-1 要求加強絕緣的 DTI ≥ 0.4 mm**［S29］［S30］──對磁性/電容隔離而言這是必須額外堆疊的絕緣層，對壓電變壓器而言**陶瓷本體本來就是毫米級的實心介電體**，隔離距離是「免費」的副產品。同時因為傳輸機制是彈性波不是磁場，**天生低電磁輻射、對外部磁場免疫**［S30a］。
- **為什麼以前做不到**：磁性隔離元件必須在高耐壓與體積之間取捨，且會輻射也會被輻射；光耦有老化與溫度問題。壓電路線在「隔離 + 高壓增益 + 無磁 + 低 EMI」的組合上是磁性元件做不到的。
- **是否真的非替代性**：**半**。它取代的是「隔離式 DC-DC + 光耦/數位隔離器」的組合，屬於替代；但「無磁 + 高壓 + 高功率密度 + 內建自感測」的**組合**在磁性方案裡沒有對應物，這部分是新的。誠實標註：**權重降一級**。
- **誰在做**：學界持續投入──壓電變壓器做 MOSFET/IGBT 閘極驅動的絕緣是明確的研究線［S30a］；近期有 radial-mode LiNbO₃ Rosen 變壓器［S28］、以及以微波聲學為基礎的隔離閘驅動器［S30b］。**商用隔離閘極驅動器目前仍全數採用磁/電容耦合**［S30a］。
- **TRL**：**3–4**。
- **市場訊號**：弱到中等。Infineon / TI / ST 都有完整的磁/電容隔離產品線，代表市場存在但已被佔滿；壓電要進場必須靠上面那個「組合」而非單點性能。
- **技術難點**：(a) 安規認證──要拿 UL 1577 / IEC 60747-17，陶瓷在**局部放電起始場強遠低於環氧樹脂**［S14a］是硬傷，PD 測試很可能是最大關卡；(b) 大驅動下的熱不穩定（PZT 的老問題，見 5.2）；(c) 負載變動時共振點漂移導致增益不穩。

### 4.3 用「自己的共振頻率」當作免感測器的溫度／預壓／老化量測

- **新能力是什麼**：諧振頻率對溫度、預壓、去極化程度都極度敏感（正是 5.x 節的失效訊號）。把這個「缺點」反過來用：**元件在正常工作時，連續回報自己的溫度與退化程度，不用熱敏電阻、不用應變規**。閉迴路追頻器本來就必須知道 f_r，等於這個資訊是**零額外成本**取得的。
- **為什麼以前做不到**：磁性元件的電感值隨溫度變化太小、太不單調，無法反解；且沒有可用的高 Q 共振點做精密頻率讀取。
- **是否真的非替代性**：**是**。這是「因為它是共振器」才有的資訊。
- **誰在做**：**查無明確產品化案例**。既有文獻多把頻率漂移當問題處理（溫度補償型陶瓷諧振器專利、控制去極化與老化的專利均屬「消除漂移」方向）［S22］［S38］。
- **TRL**：**2–3**（概念清楚、無公開實作）。
- **市場訊號**：無直接訊號；間接訊號是既有文獻大量投入在「量測 f_r 隨溫度/老化的關係」［S21］［S15］，代表模型基礎已存在。
- **技術難點**：(a) 溫度、預壓、老化三者對 f_r 的影響**互相混疊**，單一頻率讀值無法解耦──必須多模態（例如同時追徑向與厚度模態）才有機會反解；(b) 老化是不可逆的長期漂移，會污染短期溫度讀值，需要長期基準管理。

### 4.4 高場強下的「內建過載自保護」

- **新能力是什麼**：壓電體超過臨界振速後損耗急升、Qm 崩潰［S8］，這在系統層面表現為**功率傳輸能力自動飽和**──一種天然的、不需要控制電路介入的軟性限流。
- **為什麼以前做不到**：磁飽和的行為相反（飽和後電流暴衝，是災難）。壓電的飽和方向是「安全側」。
- **是否真的非替代性**：**半**。它是既有保護電路的替代/簡化，不是新功能；但「失效模式偏安全側」對安規與功能安全（ISO 26262 / IEC 61508）論證是有實質價值的。
- **誰在做**：查無有人把它當賣點主張。
- **TRL**：**2**。
- **技術難點**：這個「保護」的代價是把能量變成熱，若熱來不及散出就直接進入熱失控［S9］──**必須先證明它是自限而不是自毀**，這是本項成立與否的關鍵實驗。
- **誠實評註**：這一項有可能根本不成立，我把它列出來是因為它是唯一能把「熱失控」這個最大缺點轉成論述優勢的角度，但目前**沒有任何證據支持**。

### 4.5 無磁環境（MRI 腔內、超導磁體旁、量子/低溫系統）的功率與訊號傳遞

- **新能力是什麼**：壓電傳輸路徑不含任何磁性材料，也不產生磁場，可以放在磁性元件根本無法工作的位置。
- **為什麼以前做不到**：任何用磁芯的變壓器/電感在強磁場中會飽和、會被吸引、會造成影像偽影。
- **是否真的非替代性**：**是**（在該環境內磁性方案不存在，談不上替代）。
- **誰在做**：超音波馬達已是無磁定位的既有解法方向［S34］［S39］，但**我未能驗證具體的 MRI 相容產品型號與規格──標註未驗證**。
- **TRL**：馬達類約 6–8（未驗證）；功率傳輸類約 2–3。
- **市場訊號**：小眾但單價容忍度極高，符合「壓電單價高」的定位。
- **技術難點**：(a) 醫療認證路徑（IEC 60601、ISO 13485）本輪**查無**；(b) 低溫下壓電係數大幅下降（未驗證，需下一輪查證）。

---

## 5. 反面證據、失敗案例與物理上限

### 5.1 熱是唯一真正的天花板，而且量測方法本身會騙人

- Qm 在**自發熱條件下量到的值系統性低於 burst/transient 法**［S4］。實務含義：**你在實驗室用阻抗分析儀量到的漂亮 Qm，在實機連續運轉下不成立**。若研發初期用小訊號 Qm 做效率模型，模型會樂觀到失去意義。
- 熱源會隨工作點切換：**off-resonance 的發熱主要來自介電損耗 tanδ'（P-E 遲滯），on-resonance 的發熱主要來自機械損耗 tanφ'**［S8］。「主動/被動兩用」元件按定義會在這兩個工作點之間切換，代表**熱模型必須是雙模式的**，不能用單一等效串聯電阻描述。
- 溫度上升 → 熱活化使缺陷偶極解耦 → 疇壁釘扎減弱 → **Qm 與內偏場同時下降 → 能量耗散增加 → 去極化加速**［S1］。這是一條被明確描述的閉合正回饋鏈，而且它的終點是永久性去極化，不是可逆的效能下降。

### 5.2 壓電變壓器已經在市場上輸過一次

- CCFL 背光是壓電變壓器唯一的量產級殺手應用，隨 LED 取代，**產量下滑、專用驅動 IC 停產**［S27］。
- 技術死因被明確記錄為 PZT 的「high dielectric loss and thermal instability under large drive conditions」［S28］──**正是本題「持續高場強驅動」要面對的同一件事**。
- **對客戶的直接警示**：市面上並不缺「壓電做功率變換」的技術；缺的是能在大驅動下長期穩定的材料。若研發計畫沒有材料層面的答案（換 LN、換 hard PZT 新配方、或用缺陷偶極提高去極化溫度［S2］），就是在重走一遍已經失敗的路。

### 5.3 標準體系是破的，這會直接拉長上市時間

- **IEEE 176-1987 已撤銷**［S19］［S20］：目前沒有現行、統一的壓電量測基準標準可寫進規格書。
- **IEC 60483 是 1976 年的文件**，處理的是高機電耦合陶瓷的**小訊號動態量測**［S22a］［S23］──它根本沒有描述高功率非線性行為的框架。這代表：**你要跟客戶談的關鍵規格（高功率下的 Qm、最大振速、熱阻），沒有共通的量測方法可引用**，每家會量出不同數字。
- **AEC-Q200 沒有「主動/被動兩用元件」這個分類**。搜尋未能證實壓電致動器有對應的 AEC 應力測試分類［S25］［S26］。實務後果：進車廠必須走客製化 qualification plan，時間與成本都不可預期。

### 5.4 多層結構的失效統計指向「絕緣」而不是「陶瓷」

- 多層壓電致動器的**多數失效模式是絕緣劣化造成的短路**［S11］。
- 未被電極覆蓋的區域不會極化，在通電時限制整體變形，造成**內電極邊緣應力集中**［S11］，並可能導致介電陶瓷層開裂。
- **plate-through 電極設計難以控制銀遷移**［S11］；濕度與溫度循環會加劇界面剝離、微裂與熱疲勞［S12］。
- 對照組：PI 之所以能做到 10^11 次，關鍵在於把整顆做成**全陶瓷絕緣層包覆的單體塊**，讓濕度影響「因為陶瓷自身升溫而在局部被抑制」［S17］［S18］。**這是一個重要的設計啟示：可靠性的解不在陶瓷配方，在封裝拓撲。**

### 5.5 頻率漂移吃掉系統效率

- 陶瓷諧振器穩定度極限 **0.03%/decade**［S22］，且 f_r 隨老化持續上升［S21］。
- 溫度對 f_r 的影響本身也不單調──有文獻描述隨溫度上升呈現三個不同變化趨勢的區段［S21a］。
- 系統含義：閉迴路必須持續追頻。**追頻迴路的收斂速度與捕捉範圍，會成為整個系統動態響應的瓶頸**；而且在負載暫態時，追頻與功率控制兩個迴路會互相打架。

### 5.6 機械振動與可聽噪音是外溢型風險

- MLCC 的「singing capacitor」現象是最好的前車之鑑：陶瓷本體因壓電/電致伸縮效應振動 → 經**焊點這條剛性耦合路徑**傳到 PCB → PCB 大面積當振膜 → 20 Hz–20 kHz 可聽噪音［S37］。
- **壓電兩用元件的振動位準會比 MLCC 高好幾個數量級**，而且工作頻率若落在或其次諧波落在可聽帶，問題會嚴重得多。
- 已知緩解手段（可直接借用）：金屬端子/金屬板結構、interposer 或氧化鋁基板、加厚介電層、加厚 PCB、**PCB 正反面對稱擺放讓振動互相抵消**［S37］［S37a］。但每一項都會犧牲成本或體積──而客戶的立論基礎正是「單價高但整合度高」。
- 附帶風險：機械振動同時是**焊點疲勞源**（振動的能量最終會集中在最軟的耦合處），這一點我**未查到定量資料**。

### 5.7 場強的實用上限比矯頑場低很多

- Soft PZT 約在 **0.2 kV/cm** 就開始非線性，約 **1.5 kV/cm** 內才算線性［S14］。矯頑場（soft 2.5–15 kV/cm；hard >15 kV/cm）［S14］其實是**去極化門檻，不是可用場強門檻**。
- **陶瓷的局部放電起始場強遠低於環氧樹脂**［S14a］，且 1 mm 厚 BaTiO₃ MLCC 的 PD 起始場強低於 1.5 kV/mm［S14a］。做高壓元件時，PD 會先於介電崩潰發生，而 PD 是漸進式破壞機制。

---

## 6. 未解問題（給下一輪研究）

1. **超音波焊接/清洗換能器的實際失效統計（最高優先）**：這是唯一「連續高功率共振、且已量產數十年」的參考類別，本輪完全沒查到。要查：Langevin 堆疊的預壓螺栓鬆脫率、陶瓷片破裂率、實際 duty cycle 與壽命（小時）、Branson / Herrmann / Dukane / Telsonic 的官方換能器保固期。
2. **本題最關鍵的一個實驗數字：連續共振驅動下的去極化時間常數**。所有文獻都告訴我們「溫度會加速去極化」，但**沒有任何來源給出「在 X°C、Y kV/cm、Z 小時後 d33 掉幾 %」的加速壽命曲線**。這是投入研發前必須自己做的第一個實驗，也是最該先花錢的地方。
3. **認證路徑的空白**：AEC-Q200 對「同時是主動與被動」的元件如何分類？IEC 60601 / ISO 13485 / DO-160 / MIL-STD-883 對壓電功率元件的實際案例？IEC 63041 系列涵蓋什麼？本輪全部查無。
4. **黏著層與焊點**：多層堆疊的黏著層在 100°C+、10^9 次循環下的潛變與剝離資料；SMT 焊點在元件本體持續振動下的疲勞壽命。查無任何定量來源。

---

### 附：若要投入研發，必須先解決的可靠性題目清單

| # | 題目 | 難度 | 已有解法？ | 需要什麼量測設備 |
|---|---|---|---|---|
| R1 | 連續高功率下的自發熱與熱失控邊界 | **極高** | 部分：Penn State 高功率材料達 >1 m/s［S8］；但無現成設計準則 | 高功率壓電量測系統（HiPoCS 類）［S10］、burst 與連續雙模式阻抗量測、紅外熱像、雷射測振儀（量真實振速） |
| R2 | 去極化的加速壽命模型（溫度×場強×時間×應力） | **極高** | 無公開模型；缺陷偶極提高去極化溫度是研究方向［S2］ | 高溫高場老化爐陣列、d33 meter、P-E 迴線量測（Sawyer-Tower）、原位阻抗追蹤 |
| R3 | Qm 量測方法學（小訊號值不可信） | 中 | 有：burst/transient 法已被文獻建立［S4］［S6］ | 高功率驅動源 + 短脈衝驅動能力、精密溫控腔 |
| R4 | 內電極邊緣應力集中與絕緣劣化 | 高 | 有：全陶瓷單體封裝［S17］；網狀陶瓷-金屬複合內電極［S13］ | 微焦點 X-ray CT、聲學掃描顯微鏡（SAM）、絕緣阻抗長期監測、HALT/HAST 箱 |
| R5 | 電極遷移（銀）與濕度 | 中 | 有：改 Ag/Pd 或 Cu 內電極、全陶瓷包覆、避免 plate-through［S11］［S17］ | THB/HAST（85°C/85%RH）、離子遷移測試、SEM-EDX |
| R6 | 局部放電與高壓安規 | 高 | 部分：IEC 62368-1 允許以熱循環+濕度+AC withstand 取代 DTI 尺寸［S29］［S30］ | 局部放電偵測器（IEC 60270）、耐壓測試機、爬電距離量測 |
| R7 | 共振頻率漂移（溫度+老化）對閉迴路的衝擊 | 高 | 部分：溫度補償型諧振器設計已有前例［S38］；穩定度上限 0.03%/decade［S22］ | 溫控腔 + 網路分析儀長期掃描、老化爐、閉迴路 HIL 平台 |
| R8 | 機械振動耦合到 PCB / 可聽噪音 | 中 | 有：interposer、金屬端子、對稱擺放、加厚 PCB［S37］ | 消音室 + 聲壓計、雷射掃描測振儀（LDV）、模態分析 |
| R9 | 黏著層/焊點疲勞 | 中～高 | **查無定量資料** | 熱循環箱、震動台、剪切強度測試機、切片金相 |
| R10 | 認證路徑（車規/醫療/航太） | 高（非技術） | **查無現成路徑** | 不是設備問題，是要及早找認證顧問與目標客戶的品保部門對齊 |
| R11 | RoHS 含鉛豁免到期（2027） | 中（法規） | 部分：豁免已延至 2027/6/30 與 2027/12/31［S31］［S32］ | 法規追蹤；若走無鉛壓電材料，需重跑 R1–R3 全套 |

---

## 7. 來源清單

> 說明：以下 URL 皆為 WebSearch 回傳的結果連結。**因 WebFetch 被封鎖，我未能開啟任何一個連結核對原文**；標題與內容摘要來自搜尋引擎回傳。凡標註「未驗證」者請下游務必自行核實。

| # | 標題 | URL | 說明 |
|---|---|---|---|
| S1 | Depoling / defect dipole 相關搜尋彙整（多篇） | https://www.tandfonline.com/doi/full/10.1080/19475411.2018.1439850 | 場強相關非線性壓電性回顧；線性區/非線性區/飽和與去極化區的三段式描述 |
| S2 | Defect dipoles elevating depolarization temperature to Curie point in PMS-PZT ceramics | https://www.sciencedirect.com/science/article/pii/S0272884225055841 | 用缺陷偶極把去極化溫度拉高到居里點，是提高熱穩定性的材料路線 |
| S3 | Properties of piezoceramic materials in high electric field actuator applications | https://arxiv.org/pdf/1804.00192 | 高電場致動器用壓電陶瓷性質 |
| S4 | Characterization of high-power mechanical quality factor of piezoelectric ceramic discs under self-heating condition | https://www.sciencedirect.com/science/article/pii/S2238785423003836 | Qm 隨振幅急遽衰減；自發熱條件下 Qm 低於 burst 法 |
| S5 | Self-heating phenomenon of piezoelectric elements excited by a tone-burst electric field | https://www.sciencedirect.com/science/article/abs/pii/S0041624X2100189X | tone-burst 驅動下的自發熱現象 |
| S6 | Studies on the High-Power Piezoelectric Property Measurement Methods and Decoupling the Power and Temperature Effects on PZT-5H | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11768652/ | 解耦功率與溫度效應；自發熱放大功率對 k31/d31/s11E 的影響 |
| S7 | Evaluation of the mechanical quality factor under high power conditions in piezoelectric ceramics from electrical power | https://www.sciencedirect.com/science/article/abs/pii/S0955221914004671 | 由電功率評估高功率 Qm |
| S8 | Uchino, Loss mechanisms and high power piezoelectrics, J. Mater. Sci. | https://link.springer.com/article/10.1007/s10853-005-7201-0 | **最重要來源**：臨界振速、>1 m/s、10× 功率密度、off-resonance 靠 tanδ' / on-resonance 靠 tanφ' |
| S9 | High Temperature, High Power Piezoelectric Composite Transducers | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4179017/ | 明確使用「prone to self-heating and thermal run-away」描述 |
| S10 | High-Power Piezo Characterization System (HiPoCS) | https://www.researchgate.net/publication/343781169_High-Power_Piezo_Characterization_System | 高功率壓電量測系統，R1/R3 所需設備的參考 |
| S11 | Typical Failures for Multilayer Actuators (CTS Corp) | https://www.ctscorp.com/Resources/Blog/Typical-Failures-for-Multilayer-Actuators | 多數失效為絕緣劣化短路；銀遷移；內電極邊緣應力集中 |
| S12 | Multilayer piezoelectric actuators – structures and reliability (Penn State) | https://pure.psu.edu/en/publications/multilayer-piezoelectric-actuators-structures-and-reliability/ | 界面剝離、微裂、熱疲勞 |
| S13 | Enhanced reliability of multilayer piezoelectric ceramic actuators with networked ceramic-metal composite internal electrodes | https://www.sciencedirect.com/science/article/abs/pii/S0921510725009250 | 網狀陶瓷-金屬複合內電極提升可靠性（R4 的已知解法） |
| S14 | Piezoceramic Materials (PI Ceramic) / Piezoelectricity Basics (CTS) | https://www.piceramic.com/en/expertise/piezo-technology/piezoelectric-materials ・ https://www.ctscorp.com/Resources/Blog/Piezo-Basics | Hard/soft PZT 矯頑場區間、非線性起始場強 |
| S14a | Investigation of partial discharge in piezoelectric ceramics | https://www.sciencedirect.com/science/article/abs/pii/S1359645415007120 | 陶瓷 PD 起始場強遠低於環氧；1 mm BaTiO₃ MLCC <1.5 kV/mm |
| S14b | NASA/CR-1998-208708 Properties of PZT-Based Piezoelectric Ceramics | https://ntrs.nasa.gov/api/citations/19980236888/downloads/19980236888.pdf | PZT 材料性質基準資料（未細讀） |
| S15 | Piezoelectric resonators in DC-DC converters: current status and limits | https://www.powerelectronicsnews.com/piezoelectric-resonators-in-dc-dc-converters-current-status-and-limits/ | **關鍵數字來源**：Stanford APEC 2024 的 k²−25%/Qm−80%；LN 在 57 dBm、>0.58 A/mm² 破壞；Tc 與「半個 Tc」慣例 |
| S15a | Nonlinear Losses and Material Limits of Piezoelectric Resonators for DC-DC Converters | https://www.researchgate.net/publication/380310755_Nonlinear_Losses_and_Material_Limits_of_Piezoelectric_Resonators_for_DC-DC_Converters | S15 所引用的原始研究（未能開啟核對） |
| S15b | Design considerations for power conversion using piezoelectric materials (Stanford thesis) | https://purl.stanford.edu/md994gh4262 | Stanford SuperLab 的系統性論文，建議下一輪重點閱讀 |
| S16 | Reliability & Lifetime of Multilayer Piezo Actuators (PI 白皮書 PDF) | https://www.pi-usa.us/fileadmin/user_upload/pi_us/files/catalogs/Piezo_Actuator_Lifetime_Test_Reliability_Results.pdf | PI 官方壽命測試結果 |
| S17 | PICMA Technology (Physik Instrumente) | https://www.physikinstrumente.com/en/expertise/technology/piezo-technology/picma | 全陶瓷單體封裝、濕度影響因自身升溫而在局部被抑制 |
| S18 | Piezo actuators: 100 billion cycles without failures or loss in performance | https://www.engineerlive.com/content/piezo-actuators-100-billion-cycles-without-failures-or-loss-performance | NASA 測試 10^11 次零失效、保有 96% 位移 |
| S18a | Multilayer Piezoelectric Actuators – ceramic vs polymer coated (AZoOptics) | https://www.azooptics.com/Article.aspx?ArticleID=219 | 陶瓷封裝 vs 高分子塗覆的壽命差異（≥10×） |
| S18b | TOKIN / KEMET Multilayer piezoelectric actuators datasheet | https://content.kemet.com/datasheets/TOK_PA101.pdf | 另一家多層致動器規格書（未細讀，供比對用） |
| S18c | Failure Analysis of High-Power Piezoelectric Transducers | https://www.researchgate.net/publication/235032480_Failure_Analysis_of_High-Power_Piezoelectric_Transducers | 高功率換能器失效分析（未能開啟，下一輪必讀） |
| S19 | IEEE 176 – Inactive-Withdrawn Standard | https://standards.ieee.org/ieee/176/6315 | **IEEE 176-1987 已撤銷** |
| S20 | IEEE 176-1987 IEEE Standard on Piezoelectricity | https://standards.ieee.org/standard/176-1987.html | 原標準頁 |
| S21 | Aging effects on resonance frequency of Pb(Ti0.52Zr0.48)O3 piezoelectric ceramics for power ultrasonic transducers | https://link.springer.com/article/10.1007/s42114-021-00239-8 | 老化使諧振頻率上升；溫度×時間交互作用 |
| S21a | Publication and Proposed Revision of ANSI/IEEE Standard 176-1987 | http://ieeexplore.ieee.org/iel1/58/11257/00535477.pdf | IEEE 176 修訂提案的歷史紀錄 |
| S22 | US4384229 Temperature compensated piezoelectric ceramic resonator unit | https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/4384229 | 背景技術述及穩定度限於 **0.03%/decade** |
| S22a | IEC 60483:1976 | https://webstore.iec.ch/en/publication/2229 | 高機電耦合壓電陶瓷動態量測指引（1976 年版） |
| S23 | Piezoelectric Standards (Electrosciences) | https://electrosciences.co.uk/piezoelectric_standards/ | 壓電相關標準總覽：IEC 60483 / 60642 系列 / 60302 |
| S23a | BS EN 50324-1 Piezoelectric properties of ceramic materials and components Part 1 | https://standards.globalspec.com/std/612191/bsi-bs-en-50324-1 | 歐洲的術語與定義標準 |
| S24 | Micro Piezo Inkjet Technology / PrecisionCore (Epson) | https://corporate.epson/en/technology/overview/printer-inkjet/micro-piezo.html | 每顆壓電元件每秒射出近 50,000 次；年產 >1500 萬台、印字頭與機器同壽命 |
| S24a | Self-Diagnosing Nozzle Health System (Epson) | https://corporate.epson/en/technology/search-by-products/printer-inkjet/nozzle-self-diagnosis.html | **自感測致動器的量產實證**：壓電元件產生電壓、毫秒內自我診斷 |
| S24b | PrecisionCore Printhead Technology Fact Sheet (Epson EMEAR) | https://epsonemear.a.bigcontent.io/v1/static/precisioncore_1121_factsheeteu | 官方規格單 |
| S25 | AEC-Q200 Rev E, March 20, 2023 (原文 PDF) | http://www.aecouncil.com/Documents/AEC_Q200_Rev_E_Base_Document.pdf | 車規被動元件應力測試標準本文 |
| S25a | Passive Buzzer Market（市場研究網站） | https://markwideresearch.com/passive-buzzer-market | 車用壓電蜂鳴器認證循環 18–24 個月；**未驗證、可信度低，僅供量級參考** |
| S26 | What Is AEC-Q200?（Panasonic Industrial） | https://industrial.panasonic.com/ww/ds/ss/technical/b17 | AEC-Q200 適用範圍說明 |
| S26a | Revisiting the Samba printhead (WhatTheyThink / InkjetInsight) | https://whattheythink.com/articles/125463-inkjetinsight-revisiting-the-samba-printhead/ | 產業訪談口徑：印字頭壽命期望 3–4 年（**未驗證**） |
| S26b | SAMBA G3L (Fujifilm) | https://www.fujifilm.com/us/en/business/inkjet-solutions/industrial-printheads/samba-g3l | 官方產品頁；墨滴 2.4–13.2 pL |
| S27 | Piezoelectric Transformers: An Historical Review (Actuators, MDPI) | https://www.mdpi.com/2076-0825/5/2/12 | CCFL 應用萎縮、專用 IC 停產 |
| S28 | Radial Mode Lithium Niobate Rosen Transformer (arXiv) | https://arxiv.org/pdf/2511.17431 | 指出 PZT Rosen 變壓器在大驅動下「high dielectric loss and thermal instability」；LN 為替代路線 |
| S29 | Demystifying Clearance and Creepage Distance for High-Voltage End Equipment (TI SLUP419) | https://www.ti.com/lit/pdf/slup419 | 爬電/電氣間隙與 IEC 62368-1 Table 28 |
| S29a | Demystifying clearance and creepage distance (TI SLUP421) | https://www.ti.com/lit/pdf/SLUP421 | 同上，另一版本 |
| S30 | Distance Through Insulation: How Digital Isolators Meet…（TI SLLA563） | https://www.ti.com/lit/pdf/slla563 | **DTI ≥ 0.4 mm** 要求與測試豁免路徑 |
| S30a | Piezoelectric transformer for integrated MOSFET and IGBT gate driver | https://www.researchgate.net/publication/3280843_Piezoelectric_transformer_for_integrated_MOSFET_and_IGBT_gate_driver | 壓電變壓器做閘極驅動隔離；商用產品仍為磁/電容耦合 |
| S30b | Microwave-acoustic-based isolated gate driver for power electronics (arXiv) | https://arxiv.org/pdf/2511.13412 | 聲學隔離閘驅動器的近期研究方向 |
| S31 | EU RoHS Directive Update: Comprehensive Refinement of Lead Exemption Clauses (CIRS) | https://www.cirs-group.com/en/chemicals/eu-rohs-directive-update-comprehensive-refinement-of-lead-exemption-clauses | 7(c)-I 至 2027/6/30；新設 7(c)-VI（PZT/PTC）至 2027/12/31；2026/7/1 生效 |
| S32 | Final Delegated Directives for Key RoHS Lead Exemptions Adopted (Assent) | https://www.assent.com/blog/draft-expiry-dates-for-key-rohs-lead-exemptions-published/ | 2025/9/8 正式通過三份 delegated directive；續期須提前 18 個月 |
| S32a | RoHS Exemption for Lead Updates (APC International) | https://www.americanpiezo.com/blog/rohs-exemption-for-lead-update/ | 壓電廠商角度的豁免說明 |
| S33 | Piezoelectric thin films and their applications in MEMS: A review (J. Appl. Phys.) | https://pubs.aip.org/aip/jap/article/137/2/020702/3330689/Piezoelectric-thin-films-and-their-applications-in | PZT 薄膜疲勞至 10^10 次；<001> 幾乎無極化疲勞、<111> 快速疲勞；RuO₂ 電極 TDDB 較佳 |
| S34 | Reliability of Ultrasonic Motors (PI USA tech blog) | https://www.pi-usa.us/en/tech-blog/reliability-of-ultrasonic-motors | PILine >2,000 km 行程或 MTBF 20,000 h；陶瓷耦合件控制磨耗 |
| S34a | Piezoelectric Motors, an Overview (PI 白皮書) | https://www.pi-usa.us/fileadmin/user_upload/pi_us/files/technotes_whitepapers/Different_Piezo_Motor_Designs_Overview.pdf | 各類壓電馬達原理比較 |
| S35 | Datasheet mp6 micropumps series (Bartels Mikrotechnik) | https://bartels-mikrotechnik.de/wp-content/uploads/2025/06/Datasheet-mp6-series.pdf | mp6 壽命 >5,000 h |
| S36 | The Bartels Pump BP7 | https://bartels-mikrotechnik.de/product/the-bartels-pump-bp7-piezo-pump/ | BP7 壽命 5,000 h |
| S37 | "Singing" Multilayer Ceramic Capacitors and Mitigation Methods—A Review (PMC) | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9147252/ | 陶瓷振動經焊點傳至 PCB；20 Hz–20 kHz；各種緩解手段 |
| S37a | Piezoelectric Noise: MLCC Ringing-Singing (NIC Components) | https://www.newark.com/wcsstore/ExtendedSitesCatalogAssetStore/cms/asset/pdf/americas/common/nic-components/MLCC-Ringing-Singing-NSPH-SMT-FilmCapacitors-May2015.pdf | 業界緩解實務 |
| S38 | US5643353 Controlling depoling and aging of piezoelectric transducers | https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/5643353 | 專利：控制換能器的去極化與老化（既有解法的線索） |
| S39 | A Comprehensive Review of Piezoelectric Ultrasonic Motors (Micromachines) | https://www.mdpi.com/2072-666X/15/9/1170 | 超音波馬達分類、特性、製造與未來挑戰 |
| S40 | Contact mechanics of piezoelectric ultrasonic motors (Smart Mater. Struct.) | https://iopscience.iop.org/article/10.1088/0964-1726/7/3/011 | 磨耗與壽命由接觸力學決定 |
| S41 | A hybrid piezoelectric resonator-based DC-DC converter (Nature Communications) | https://www.nature.com/articles/s41467-026-70494-0 | 混合式壓電諧振器 DC-DC；**日期看似 2026 年，未驗證，下一輪需確認** |
