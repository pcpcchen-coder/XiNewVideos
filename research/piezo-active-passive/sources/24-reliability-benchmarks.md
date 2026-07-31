# 高功率壓電量產案例的真實壽命數據與認證路徑：可靠性標竿補查

> 一句話結論：壓電在「高功率但**低工作週期**（超音波焊接每焊 0.2–0.4 秒）」與「低功率但**超高循環數**（噴墨 10^10–10^11 次、致動器 10^11 次）」兩端都已有量產級證據，唯獨「**高功率 × 連續運轉 × 長壽命**」這個交集——正是主動/被動兩用元件的工況——**連學界都公開承認幾乎沒有壽命文獻、廠商也不公布數據**；而且真正的量產可靠性槓桿不在陶瓷配方，在**內電極材料（Cu vs Ag/Pd，85/85 下差 100 倍循環數）**與**封裝拓撲**。

---

## 0. 研究方法與限制（誠實揭露）

- **本輪實際完成 50 次 WebSearch**（超過任務要求的 30–45 次），第 51 次收到 `this session has used its web search budget (200 of 200 WebSearch calls)`——與前輪相同，是整個 session 的全域上限，非本代理個人配額。
- **WebFetch 全程未使用**（環境 403）。所有內容 100% 來自 WebSearch 回傳的「連結清單 + 搜尋引擎摘要」，**我未能開啟任何一個 URL 核對原文**。凡標示「未驗證」者代表僅單一摘要來源。
- **本輪明確查無的項目**（下一輪或委外查證）：
  1. Branson / Emerson、Herrmann、Dukane、Telsonic、Sonics & Materials 的**原廠換能器壽命規格與保固期**——全部查無。搜尋只回傳替代品供應商（中國廠）的頁面與行銷語（Herrmann 僅稱 "extremely long service life"，無數字）。
  2. **Kyocera、Ricoh 噴墨頭的官方 billion-shot 規格**——查無。Fujifilm Samba 亦查無明確循環數，只有定性的「sputtered PZT、poled as deposited、內應力低所以壽命長」。
  3. **Nanomotion HR 系列官方 MTBF / 壽命規格**——查無（僅一件專利提到 >9,000 小時，非產品規格）。
  4. **Bosch / Denso / Continental 壓電噴油嘴的官方壽命循環數**——查無。搜尋摘要明確說「the actual numerical specifications for switching cycles or billion-cycle durability ratings are not disclosed in publicly available sources」。唯一有數字的是 **TDK 的元件級數據**（見 §3）。
  5. **DO-160、MIL-STD-883、NASA EEE-INST-002 對壓電元件的專屬條款**——查無。EEE-INST-002 的檢索結果只回傳通則（screening / qualification / derating 三段式、Level 1–3），未見 piezo 類別。DO-160 的搜尋結果反而是「壓電致動器被拿來當**產生震波的測試設備**」，不是受測件。
  6. **ATEX / IECEx 對壓電元件的能量門檻**——查無具體數值；只確認走 ISO 80079-36:2016 的 ignition hazard assessment 路徑（非電氣設備），機械能轉成點火源時須做 IHA。
  7. **AEC-Q200 認證的壓電元件廠商名單**——查無任何廠商公開宣稱「AEC-Q200 qualified 壓電致動器」。Murata CERALOCK 有「車用版本」，但差異被描述為「操作溫度範圍與環境特性」，**未見 AEC-Q200 字樣**。
  8. 超音波焊接換能器的**現場更換週期（小時 / 焊點數）**——搜尋額度在發出該查詢時耗盡。
- **一個必須先講的元研究發現（本輪最重要的誠實揭露）**：Hemsel & Bornmann 在 *Archive of Applied Mechanics*（2014）的〈Reliability analysis of ultrasonic power transducers〉開宗明義寫道：**「壓電多層致動器的可靠性已被深入研究，但超音波功率換能器的可靠性幾乎沒有文獻；製造商極少公布其元件的老化或壽命數據」**［S5］。這不是我查不到，是**這個資料本來就不存在於公開領域**。客戶必須把「沒有標竿可抄」當成本題的基本前提。

---

## 1. 結論摘要

1. **超音波焊接不是「連續高功率」的參考案例，是「高功率脈衝 + 強制冷卻」。** 實際焊接時間 **200–400 ms**，絕大多數 <1 秒；自動化產線還必須在焊後插入 cooling time 才收回焊頭，換能器與 horn 常需**空氣冷卻**，否則「陶瓷會失去壓電性」［S16］［S17］。**客戶若假設可以拿超音波焊接的成熟度背書「連續運轉」，這個類比是錯的。**
2. **但它給了一個非常有用的設計餘裕數字：換能器在 179%–244% 的量產標稱振幅才失效。** 30 kHz 焊接換能器的失效分析顯示，有限元素法預測應可承受標稱振幅的 **208%**，實測失效落在 **179%–244%**；但**實測失效模式（陶瓷內徑處電弧放電）與 FEA 預測的模式（陶瓷與導電片脫耦）不一致**，且實驗室的電負載無法代表真實焊接負載［S3］。**意涵：業界的量產設計餘裕約 2× 振幅，而且模型抓不到真實失效模式。**
3. **量產環境的頭號失效模式與實驗室不同**：實驗室全部是電弧放電；**量產現場的主導失效是「陶瓷破裂與位移（fracture and shifting of crystals）」**［S3］。加上熱去極化（超過居里點，PZT-8 約 320°C）、中心螺栓過度鎖緊造成的機械開裂、以及銀電極層/黏著層的剝離［S1］。
4. **金屬件（horn/sonotrode）的疲勞是另一條獨立的壽命曲線，而且量級明顯低於陶瓷。** 設計良好的 sonotrode 在 20 kHz 下十年壽命約對應 **10^12 次應力循環**；但實際案例中鋁合金 sonotrode 曾在 **約 5×10^9 次（幾個工作週）** 就提前破斷，且同幾何、不同批次的材料表現差異巨大［S15］。**壓電系統的壽命常常不是被陶瓷限制，是被與它共振的金屬結構限制。**
5. **內電極材料是量產可靠性最大的單一槓桿，且有硬數據。** TDK：在 **85°C / 85%RH** 下，內電極含 95% Ag 的壓電疊層**約 100 萬次循環**就失效；即使用到 25% Pd 也**約 400 萬次**失效；而**銅內電極在 1 億次循環後零失效**。另外銅電極致動器可在 **170°C 下完成 10 億次切換循環無失效**，同條件下 Ag/Pd 已有顯著失效率［S28］［S29］。這是本輪查到**最乾淨、最可直接引用的可靠性對照數據**。
6. **「壓電體同時當致動器與感測器」在兩個高價值量產領域都已落地，而且都是靠它賺錢**：(a) Epson PrecisionCore 的 Nozzle Verification Technology——壓電元件驅動噴墨後，用同一顆元件讀**墨腔內的殘留振動**，經印字頭內建 IC 轉成電訊號，**毫秒內**判定該噴嘴是否堵塞或墨水黏度上升，並自動啟動清潔或把墨路改由鄰近噴嘴補償［S20］［S21］；(b) Bosch 壓電噴油嘴的 **Needle Closing Control（NCC）**——**直接從壓電致動器上的電壓偵測針閥關閉時刻**，不需外加感測器，用來在整車壽命內維持噴油量精度［S31］［S32］。**這兩個案例是「主動/被動兩用」立論最強的商業證據。**
7. **噴墨頭是目前唯一有「超高循環數 + 明確驗收準則」的量產壓電應用**：壓電噴墨頭每通道壽命典型 **>10^10 次致動**；工業級要求最低工作壽命 3–5 年、**噴嘴壓電陶瓷疲勞壽命不低於 1,500 億次（1.5×10^11）**（另有廠商規格為 300 億次）；Seiko 印字頭保證**每噴嘴 >40 億滴**、Brother 線型頭宣稱 **1,000 億滴**；驗收準則是「**每噴出 10 億滴最多允許 1 次失效**」，部分工業應用**不允許任何失效**［S23］。**這是本題可引用的最嚴格量產品質標準。**
8. **標準地圖有一個好消息與一個壞消息。** 好消息：**IEC 63041 系列是活的**——63041-1（通則，2017/2018/2021）、63041-2（化學/生化感測器，2017）、**63041-3（物理感測器，2026 年版）**，涵蓋力、壓力、扭矩、黏度、溫度、膜厚、加速度、振動、傾角［S25］［S26］。壞消息：**IEEE 176-1987 於 2000/3/6 正式撤銷，且目前 IEEE SA 沒有任何授權中的修訂專案**，撤銷理由被記錄為「多年後沒有人願意維護這份文件」［S27］。**壓電材料常數的聖經沒有繼承者。**

---

## 2. 查證結果 / 現況

### 2.1 超音波焊接／塑膠熔接（本輪最重要的標竿）

**功率與構造。** 20 kHz Langevin（bolt-clamped）堆疊：多片 PZT 圓環在鈦合金前後質量塊之間，以中心螺栓施加壓縮預應力，避免脆性陶瓷在振動中承受拉應力並確保各元件間的耦合［S1］。Branson CJ-20（2000 / 2000X / DCX 系列）替代品供應商標示 **~2–4 kW 輸出、電容 19–21 nF、振幅 26 µm**（**未驗證**：來自替代品供應商頁面，非 Emerson 原廠）［S2］。Herrmann 的公開技術描述為「solid piezoceramic four-disk technology」（實心四片陶瓷）［S4］。

**工作週期（最關鍵的誤解點）。** 實際焊接時間 **200–400 ms**，多數 <1 秒；自動化製程通常需要**空氣冷卻換能器與/或 horn**，且操作者要設定焊後 cooling time 才能收回 horn［S16］［S17］。也就是說，**這個「kW 級」的案例其實 duty cycle 可能只有百分之幾**。它證明的是「壓電能承受極高瞬時功率密度」，**不能證明「壓電能連續高功率運轉」**。

**失效模式（實驗室 vs 量產不一致）。** 見 §1.2/§1.3。特別注意：**FEA 預測的失效模式與實測不符**［S3］——對客戶的含義是，**這個領域的模擬信賴度不足以取代實體壽命試驗**。

**預應力這條隱藏的失效鏈。** 預應力會隨時間鬆弛（embedment relaxation、墊片潛變、彈性交互作用、振動鬆脫、應力鬆弛），且**鬆弛發生的溫度遠低於潛變**；組裝時螺栓與配合面上的刮痕是拉應力集中點，會在運轉中變成疲勞裂紋起點；業界穩定化手法是「反覆上緊/鬆開多次以拋光螺紋」以降低扭矩-預拉力係數的離散［S18］［S19］。有文獻報告預應力量測的合成精確度可達 **1.13%**［S5］。

**自診斷已被專利化。** US 12,397,318〈Ultrasonic transducer health status monitor〉：用**脈衝電訊號驅動壓電元件、取樣其訊號、比對振幅與預設界限**，判定壓電元件阻抗是否因污染等原因異常［S22］。**這是「高功率壓電元件用自身做健康監測」的第二個量產級證據（第一個是 Epson）。**

### 2.2 超音波清洗（唯一真正「連續運轉」的高功率案例）

- 維護良好的機台，換能器典型壽命 **5–10 年**［S6］。
- **最常見的早期失效是乾燒（dry running）**：空槽或水位過低時，換能器數分鐘內過熱，壓電元件開裂或與槽底完全脫膠，**不可逆且不在保固範圍**［S6］。
- 保固實務差異極大：多數 1–2 年；部分廠商採 **10-5-2**（換能器 10 年 / 產生器 5 年 / 其他 2 年）；Blue Wave 對**銀焊接合的換能器/振動膜**提供終身不失效保固［S7］［S8］。
- **對客戶的意涵**：連續運轉是可行的，但**熱耦合路徑（有沒有把熱導走的液體/散熱體）是生死線**，不是陶瓷本身的問題。這與前輪「熱失控是唯一天花板」的結論完全一致。

### 2.3 醫療：超音波手術刀與白內障乳化

- **Harmonic（Ultracision）**：刀刃縱向振動 **55 kHz**，手把約 **55.5 kHz**；聲學換能器由 **4 片壓電元件夾在兩個鋁製端鐘之間壓縮固定**［S9］［S10］。
- **法規類別**：Ultracision 手把為 **Class II**，走 510(k)；K990430 於 **1999/3/12** 取得許可［S10］。FDA 產品碼：**LFL（Ultrasonic Surgical Instrument）**、GEI；例如 Misonix neXus 超音波手術吸引系統 K221235（2022/7/28）標示 LFL / GEI / LBK，架構是「**可重複使用手把 + 單次使用拋棄式探針**」［S11］［S12］。Ethicon Total Energy System 標示 GEI / HGI / LFL［S11］。
- **Phaco（白內障超音波乳化）**：頻率 **28–45 kHz**（另一來源寫 30–50 kHz）；壓電晶體驅動中空針管做縱向振動［S13］。**滅菌是壽命殺手**：「滅菌程序在人力、時間與**手把壽命縮短**上都昂貴」；且**絕對不可用超音波清洗機清潔 phaco 手把，會損壞壓電晶體**［S13］。
- **60601 系列的空隙**：IEC 60601-2-2 是**高頻電外科（RF）**，不是超音波；IEC 60601-2-5（Ed 3.0:2009）是**超音波物理治療**設備。**沒有查到專屬於「超音波手術器械」的 60601 particular standard**——實務上這類產品走 IEC 60601-1 + 相關 collateral，並在複合能量平台上同時引用 60601-2-2［S14］［S24］。

### 2.4 噴墨頭：自感測 + 超高循環數的雙重標竿

**Epson Nozzle Verification Technology（NVT）機制細節**（本輪重點補查，已查到原理層級）：
- 壓電元件加電壓會變形（當致動器，等於每個噴嘴的微型墨泵）；**壓電元件變形時也會產生電壓**［S20］。
- NVT 把壓電致動器**同時當感測器**：偵測噴射後**墨腔內壓力變化造成的殘留振動（residual vibration）**，由**印字頭內建的 IC** 把壓力變化轉成電訊號並分析，判定噴嘴狀態（堵塞、墨水黏度上升等）［S20］［S21］。
- 反應時間：**毫秒級**，「近乎即時的自我診斷」；偵測到問題後自動啟動清潔，必要時**把該噴嘴的墨改由鄰近噴嘴補噴**［S20］［S21］。
- 商業意義：Epson **年產超過 1,500 萬台**印表機，印字頭「設計為與機器同壽命（permanent printhead）」，主打「更少維護零件、更少服務叫修」［S33］。**自感測是把「不可更換印字頭」變成可行商業模式的支柱技術。**

**壽命規格（多來源，數字有量級差異，請注意）**：
| 對象 | 數字 | 註 |
|---|---|---|
| 壓電噴墨頭一般 | 每通道 **>10^10 次致動** | 學術綜述口徑［S23］ |
| 工業噴墨要求 | 最低工作壽命 **3–5 年**；噴嘴 PZT 疲勞壽命 **≥1.5×10^11 次** | 另有廠商規格為 3×10^10［S23］ |
| Seiko 印字頭 | 保證**每噴嘴 >4×10^9 滴** | ［S23］，未驗證 |
| Brother 線型頭 | **10^11 滴** | ［S23］，未驗證 |
| 驗收準則 | 「每 10^9 滴最多 1 次失效」（紙張列印）；部分工業應用**零容忍** | ［S23］ |
| Fujifilm Samba | Si-MEMS + **濺鍍 PZT、沉積時即極化**，內應力低故壽命長 | 定性描述，無數字［S34］ |
| Kyocera / Ricoh | **查無** | 只查到「提升結構強度與剛性以增強耐久性」等定性語 |

### 2.5 壓電馬達與致動器

- **PI PICMA**：NASA/JPL 的性能與壽命測試——**10^11（1,000 億）次循環後零失效，保有原始位移的 96%**；通過後才獲准用於 Curiosity 火星車 CheMin 儀器，**16 顆 PICMA 致動器**裝在取樣處理機構的撓性機構中［S35］［S36］［S37］。
- **PI 的 MTTF 模型（本輪新查到，是唯一公開的壓電壽命外推公式）**：`MTTF = AU × AT × AF`，其中 AU 為電壓因子、AT 為溫度因子、AF 為濕度因子；範例：**75%RH（AF=14）、100 V DC（AU=75）、45°C（AT=100）→ 約 105,000 小時**［S38］［S39］。PI 明確指出：**在 DC 工作模式下，壽命主要受大氣濕度支配**［S39］。**這是一個乘法式的經驗模型，不是 Arrhenius 型的物理模型——含義是業界並沒有真正的失效物理模型，只有經驗因子。**
- **摩擦驅動型壓電馬達的壽命由磨耗決定，且不同拓撲差 2 個數量級**（Xeryon 公開比較）：**超音波型 ~2,000 km**；**stick-slip（慣性）型 10–30 km**（以其極速 3 mm/s 連續運轉僅 **1–2 個月**）；**walking（Piezo LEGS 類）50–100 km**（以 10 mm/s 連續運轉約 3–4 個月）［S40］［S41］。原因：超音波型的橢圓運動讓陶瓷尖端「回程近乎不接觸」，stick-slip 每步都在滑回時磨耗［S40］。
- **Canon USM**：Ring USM 壽命長（20 年老鏡仍如新），**Micro USM（塑膠接環鏡頭、EF 50/1.4）壽命明顯短，失效前會先發出吱吱聲**［S42］（**未驗證**，來自攝影論壇與科普整理，非 Canon 官方規格）。**這是「摩擦耦合型壓電機構會有可預警的漸進退化」的實務證據。**
- **PiezoMotor / Nanomotion 官方壽命規格：查無**。

### 2.6 壓電微泵

- **Lee Ventus（原 TTP Ventus）Disc Pump**：LT 系列耐久測試**已超過 17,000 運轉小時**（宣稱可支撐 2 年連續使用），並宣布**超過 1 兆（10^12）次循環**；規格口徑為「最嚴苛條件下 >5,000 小時連續運轉，其他應用可達 10,000 小時」；**測試條件為 40°C 環境 + 限流負載**［S43］［S44］［S45］。原理是在固定容積腔內激發**高頻聲學駐波**，再用專利超快閥整流成流量［S46］。
- **Murata microblower MZB1001T02**：20×20×1.85 mm、**24–27 kHz**、15 Vpp 下 1 L/min 與 1,900 Pa、消耗 0.18 W；資料表警告**菸霧與蚊香煙霧會影響產品壽命**（對粉塵環境敏感）［S47］。**明確的小時數壽命規格：查無**。
- **Bartels mp6 / BP7：>5,000 小時**（沿用前輪［04］的 S35/S36）。

### 2.7 汽車壓電噴油嘴

- **Bosch**：壓電 common-rail（CRI3）壓力達 **2,700 bar**，支援 Digital Rate Shaping［S31］。**Needle Closing Control（NCC）**：可整合針閥關閉感測器於 **≥2,000 bar** 系統，「顯著提升整個使用壽命期間的噴射精度」；技術上**由施加在壓電致動器上的電壓即可偵測針閥關閉時刻**，即致動器兼作感測器［S32］。Bosch 壓電噴嘴有「含 NCC」與「不含 NCC」兩種版本［S32］。
- **Continental**：2016 年公布的壓電 common-rail 達 **250 MPa 軌壓、單一工作循環最多 8 次噴射**［S30］。
- **官方壽命循環數：查無**（見 §0）。可用的最接近元件級數據是 TDK 的 §1.5。
- **失效模式的定性描述**：壓電噴嘴移動件少、摩擦與磨耗低，耐久性優於電磁閥式；但現場仍有故障碼案例（例如澳洲 Toyota 70 系列的 P1238 噴嘴故障碼）［S30］——**未驗證，來自維修業者網站，可信度低，僅供「不是零故障」的佐證**。

### 2.8 失效物理的定量資料

- **熱去極化的溫度分段（PZT-4D，hard）**：**去極化從 150°C 開始**；即使加熱到 300°C 仍保有相當程度的極化；**但機械品質因數 Qm 的不可逆劣化在低到 100°C 就發生**［S48］。**這一條極其重要：Qm 比 d33 更早、更低溫劣化——也就是說用 d33 監測壽命會嚴重低估退化。**
- 更廣義的分段：**<150°C 對壓電參數影響不顯著；150–250°C 因去極化而顯著變化；>250°C 急速劣化**［S49］。缺陷偶極穩定化的 PZT 可把去極化推遲到接近居里溫度（365°C）［S50］。
- **有沒有 Arrhenius / Coffin-Manson 類模型？** 部分有，但都是借來的：
  - 單應力加速模型（Arrhenius、反冪次、指數模型）是通用做法；**陶瓷多層元件的壽命預測慣用 Arrhenius 為基礎的 Prokopowicz–Vaskas 方程式**（同時含電壓與溫度加速項）計算活化能［S51］［S52］。**這是 MLCC 領域的模型，被借到壓電多層元件；我未查到專為壓電致動器建立且經驗證的版本。**
  - 加速壽命試驗實作範例：試片在 **2,000 Hz、0–20 V** 驅動以加速壽命試驗，並在試驗後量測**絕緣阻抗**，取最低值作為退化後的絕緣阻抗［S51］。
  - 多層壓電致動器的壽命研究結論：**裂紋在壽命早期就開始生成**，濕度會加速退化；**黏著中間層（adhesive interlayer）的選擇對性能與壽命有實質影響**［S53］。
- **疲勞曲線**：可套用 **Paris 型冪次律**分析壓電陶瓷的電疲勞裂紋成長；當場強足以引發極化翻轉時，**雙極/單極電場循環最易引發嚴重裂紋成長**（實驗場強設定為矯頑場的 0.9–1.5 倍）；**裂紋成長率隨循環數下降，約 10^5 次後達到飽和**，且與鐵電應變相關［S54］［S55］［S56］。
- **濕度加速（85/85）**：見 §1.5 的 TDK 對照數據。標準做法為 THB（85°C/85%RH + 偏壓），典型 1,000 小時；**HAST（JESD22-A110）相對 85/85 有 10–100× 加速，96–264 小時即可完成**［S57］。失效機制被明確描述為**銀枝晶的電化學遷移導致局部短路或介電崩潰**；某專利記載 100% Ag 內電極的試片因銀遷移在內外電極接合處產生大負載，**導致火花與斷線**［S57］［S58］。

### 2.9 可聽噪音與機械耦合（本輪新增定量）

- **最有效的商用緩解手法是金屬端子電容，可衰減噪音 25 dB**；相較於一般型，各種特殊型電容可降低最多 **10 dB**［S59］［S60］。
- Murata 的三條產品線對應三種原理：**KRM（金屬端子把電容架高離開 PCB）／ZRA・ZRB（interposer 基板吸收振動）／GJ4（低介電常數材料衰減內層間振動）**；TDK 對應的是 CKG 系列［S60］［S61］。
- **成本是明確的阻力**：這類電容「較昂貴，因而阻礙終端設備廠商廣泛採用」［S60］。**對客戶的直接含義：若兩用元件的振動外溢必須靠金屬端子/interposer 解，等於在成本論述上先失血。**

---

## 3. 關鍵數字表

| 項目 | 數值 | 條件／備註 | 來源 |
|---|---|---|---|
| 超音波焊接實際焊接時間 | **200–400 ms**，多數 <1 s | 需空氣冷卻 + 焊後 cooling time | S16, S17 |
| 30 kHz 焊接換能器失效振幅 | 實測 **179%–244%** 標稱振幅；FEA 預測 208% | **失效模式與 FEA 預測不符** | S3 |
| 焊接換能器實驗室失效模式 | 底部陶瓷片**內徑處電弧放電**（全部） | 電負載不代表真實焊接條件 | S3 |
| 焊接換能器量產失效模式 | **陶瓷破裂與位移** | 與實驗室不同 | S3 |
| Branson CJ-20 | 20 kHz、**~2–4 kW**、19–21 nF、振幅 26 µm | **未驗證**：替代品供應商口徑 | S2 |
| Sonotrode 設計壽命 | 20 kHz 下十年約 **10^12 次應力循環** | 設計良好者 | S15 |
| 鋁合金 sonotrode 提前失效 | **~5×10^9 次**（幾個工作週） | 同幾何、不同批次差異巨大 | S15 |
| 超音波清洗換能器壽命 | **5–10 年**（維護良好） | 乾燒可在**數分鐘**內報廢 | S6 |
| 清洗機保固實務 | 1–2 年為主；亦見 **10-5-2**（換能器 10 年） | 部分廠商換能器終身保固 | S6, S7, S8 |
| Harmonic 手術刀 | **55 kHz** 刀刃 / **55.5 kHz** 手把、**4 片**壓電元件夾在兩鋁端鐘間 | FDA **Class II**，K990430（1999/3/12） | S9, S10 |
| Phaco 頻率 | **28–45 kHz**（另一來源 30–50 kHz） | 滅菌會縮短手把壽命；禁用超音波清洗 | S13 |
| 壓電噴墨頭壽命（一般） | **>10^10 次/通道** | 學術綜述 | S23 |
| 工業噴墨 PZT 疲勞壽命要求 | **≥1.5×10^11 次**（另有 3×10^10 規格） | 最低工作壽命 3–5 年 | S23 |
| 噴墨驗收準則 | **每 10^9 滴 ≤1 次失效**；部分工業零容忍 | 紙張列印口徑 | S23 |
| Seiko / Brother 印字頭 | **>4×10^9 滴/噴嘴** / **10^11 滴** | 均**未驗證** | S23 |
| Epson NVT 反應時間 | **毫秒級**自我診斷 | 印字頭內建 IC 讀殘留振動 | S20, S21 |
| Epson 產能 | 年產 **>1,500 萬台**，印字頭與機器同壽命 | 商業模式支柱 | S33 |
| PI PICMA | **10^11 次零失效、保有 96% 位移** | NASA/JPL；Curiosity CheMin 用 **16 顆** | S35, S36, S37 |
| PI 壽命模型 | `MTTF = AU × AT × AF`；75%RH(14)×100V(75)×45°C(100) → **~105,000 h** | **DC 模式下濕度主導壽命** | S38, S39 |
| **TDK 85/85 內電極對照** | 95%Ag **~10^6 次**失效；25%Pd **~4×10^6 次**失效；**Cu 10^8 次零失效** | 85°C/85%RH | S28 |
| TDK 銅電極高溫壽命 | **170°C 下 10^9 次切換循環無失效** | 同條件 Ag/Pd 有顯著失效率 | S28, S29 |
| TDK 第三代材料 | 耦合係數 **>75%** | 最小化非活性區、最大體積效率 | S29 |
| 摩擦型壓電馬達壽命 | 超音波型 **~2,000 km**；walking **50–100 km**；stick-slip **10–30 km** | stick-slip 連續 3 mm/s ≈ 1–2 個月 | S40, S41 |
| Lee Ventus Disc Pump | **>17,000 h**、**>10^12 次循環**；規格 >5,000 h（嚴苛）～10,000 h | 測試於 **40°C + 限流負載** | S43, S44, S45 |
| Murata microblower | 24–27 kHz、1 L/min @15Vpp、1,900 Pa、0.18 W | 壽命小時數**查無**；煙霧會影響壽命 | S47 |
| Bosch 壓電 CR | **2,700 bar**；NCC 感測適用 **≥2,000 bar** | **由致動器電壓偵測針閥關閉** | S31, S32 |
| Continental 壓電 CR | **250 MPa**、單循環最多 **8 次噴射**（2016） | — | S30 |
| PZT-4D 去極化門檻 | **150°C 開始去極化**；**100°C 即有不可逆 Qm 劣化** | 300°C 仍保有相當極化 | S48 |
| 壓電參數溫度分段 | <150°C 影響小；150–250°C 顯著；>250°C 急劇 | — | S49 |
| 電疲勞裂紋 | Paris 型冪次律適用；**成長率約 10^5 次後飽和** | 雙極/單極循環（0.9–1.5 Ec）最傷 | S54, S55, S56 |
| HAST vs 85/85 | 加速 **10–100×**；**96–264 h** 取代 1,000 h | JESD22-A110 | S57 |
| MLCC 噪音緩解 | **金屬端子 −25 dB**；特殊型最多 −10 dB | 成本是採用阻力 | S59, S60 |
| IEC 63041 系列 | -1 通則(2017)、-2 化學/生化(2017)、**-3 物理感測器(2026)** | 涵蓋力/壓力/扭矩/黏度/溫度/膜厚/加速度/振動/傾角 | S25, S26 |
| IEEE 176-1987 | **2000/3/6 撤銷**，**無授權中的修訂專案** | 撤銷理由：無人維護 | S27 |

---

## 4. 對決策的意涵

1. **不要用超音波焊接替「連續高功率」背書。** 它是 200–400 ms 脈衝 + 強制空冷。要證明兩用元件能連續運轉，正確的類比對象是**超音波清洗**（連續、但有液體帶走熱），而清洗機的頭號死因正是**失去熱耦合路徑（乾燒）**。→ **研發計畫的第一份規格書就要把「熱移除路徑」寫成一級需求，而不是散熱設計。**
2. **內電極先決定，再談陶瓷配方。** TDK 的 85/85 對照（Ag 10^6 / AgPd 4×10^6 / Cu 10^8）是本輪投資報酬最高的一條情報：**同樣的陶瓷，換電極材料可以買到 100 倍的濕度壽命**。若客戶要做多層結構且面對車規或戶外環境，**銅內電極（或全陶瓷包覆）是入場券，不是加分項**。同時要注意 Cu 內電極需還原氣氛共燒，會反過來限制可用的 PZT 配方——這是製程與材料的耦合決策，要在專案第一天就定。
3. **把「自感測」當作主打，而不是附加價值——因為市場已經幫你驗證過兩次。** Epson NVT（毫秒級噴嘴自診斷 + 自動補償）與 Bosch NCC（由致動器電壓讀針閥關閉、維持整車壽命精度）都不是實驗室成果，是**用來支撐商業模式與法規宣稱的量產功能**。客戶的兩用元件若能提供「每一顆功率元件自帶 BIST」，這條敘事有現成的產業先例可引。→ 建議把 §2.4/§2.7 的兩個案例直接寫進商業計畫書的「技術可行性」章節。
4. **驗收準則要向噴墨頭看齊，不要向致動器看齊。** 「每 10^9 次動作最多 1 次失效」是可引用的量化品質目標，比「10^11 次零失效」這種單顆展示數字更有工程意義（後者是 sample size = 少數幾顆的展示測試）。→ **試驗計畫要規劃足夠樣本數與 Weibull 分析，不是做一顆跑很久。**
5. **壽命模型只能用經驗乘法模型起步。** PI 公開的 `MTTF = AU×AT×AF` 說明業界並沒有壓電專屬的物理型加速模型；MLCC 的 Prokopowicz–Vaskas（Arrhenius + 電壓冪次）是目前最可借用的框架。→ **客戶必須自建加速模型，而且要用「Qm 而非 d33」當退化指標**（因為 Qm 在 100°C 就開始不可逆劣化，d33 到 150°C 才動）。這一條會直接影響量測設備採購。
6. **認證路徑要「借殼」而非「開新路」。** 沒有 AEC-Q200 的壓電致動器分類、沒有 60601 的超音波手術 particular standard、沒有 DO-160/EEE-INST-002 的壓電條款。可行策略是：(a) 車用先以**被動元件（諧振器/電容）身分**過 AEC-Q200 的機械與環境項目，另用客製 plan 補主動項；(b) 醫療走 **60601-1 + 產品碼 LFL/GEI 的 510(k) 前案**，把「可重複使用主機 + 拋棄式接觸件」當成預設架構（Misonix/Ethicon 都是這個架構）；(c) 感測宣稱可掛 **IEC 63041-3:2026**。
7. **金屬結構的疲勞可能比陶瓷先死。** 鋁合金 sonotrode 在 5×10^9 次就提前破斷、且批次間差異巨大——若兩用元件有金屬端子、金屬外殼、預壓件或焊點參與共振，**這些零件要獨立做 S-N 與批次管制**，不能只驗陶瓷。

---

## 5. 反面證據與上限

1. **「超音波功率換能器的可靠性幾乎沒有公開文獻，廠商也極少公布老化或壽命數據」——這是同行評審期刊的原話**［S5］。客戶不能期待買到或抄到標竿數據；**這筆試驗費用是無法迴避的沉沒成本。**
2. **模擬工具在這個領域信賴度不足。** 30 kHz 換能器的 FEA 預測了「陶瓷/導電片脫耦」，實際失效卻全是「陶瓷內徑電弧放電」；作者同時承認實驗室電負載無法代表真實焊接條件［S3］。→ **不要用 FEA 壽命預測取代實體試驗，也不要用簡化電負載做壽命試驗。**
3. **Qm 的不可逆劣化門檻低到 100°C**［S48］——遠低於一般人以「居里溫度一半（~160°C）」為上限的直覺。對高功率兩用元件（效率完全由 Qm 決定），**實用熱上限可能要壓到 100°C 以下**，這會大幅壓縮功率密度的設計空間。
4. **可聽噪音的解法都要花錢。** 金屬端子只能買到 −25 dB，而且成本高到「阻礙終端廠商廣泛採用」［S59］［S60］。壓電兩用元件的振動位準遠高於 MLCC，**−25 dB 很可能不夠**，而客戶的整個立論建立在「單價高但整合度高」——噪音緩解會直接吃掉這個利差。
5. **摩擦/接觸型的壽命天花板很硬。** 最好的超音波馬達也只有 ~2,000 km，stick-slip 只有 10–30 km［S40］。任何依賴接觸傳遞機械能的兩用元件拓撲，壽命都會被磨耗而非陶瓷決定。
6. **醫療端的「重複滅菌」是獨立的壽命殺手**，且已被明確記錄為縮短手把壽命的成本項［S13］。若目標市場含醫療，**拋棄式/可重複使用的切分點必須在架構階段就決定**，事後改不了。
7. **法規面沒有為「主動/被動兩用」預留位置**：IEEE 176 撤銷 26 年無人接手、AEC-Q200 無此分類、60601 無超音波手術專章。**這代表每一個客戶的品保部門都會問「你依哪份標準？」而客戶沒有標準答案可給。**

---

## 6. 未解問題

1. **超音波焊接換能器的現場更換週期究竟是多少小時／多少焊點？** 這是判斷「高瞬時功率密度是否真的可持續」的唯一實證。本輪搜尋額度在發出該查詢時耗盡。建議直接向 Emerson/Branson、Herrmann、Dukane 的台灣代理索取保養手冊與備品週轉率（**這比再查一輪網路有效**）。
2. **連續共振驅動下的去極化/Qm 退化時間常數**（前輪已列為第一優先，本輪仍未解）。已知的只有「100°C 有不可逆 Qm 劣化、150°C 開始去極化」的**靜態加熱**數據，**沒有任何「在自發熱 + 高場強 + 連續振動下，Qm 隨時間如何衰減」的曲線**。這仍是必須自己做的第一個實驗。
3. **Cu 內電極能否與客戶想用的陶瓷配方共燒？** TDK 是「唯一使用銅內電極」的廠商［S29］，這暗示製程門檻極高（還原氣氛共燒 + 材料再設計）。**客戶若無法取得 Cu 內電極製程，85/85 壽命就退回 10^6 次量級——這可能直接否決車規與戶外應用。**
4. **兩用元件的「感測通道」在高壓驅動下的實際訊噪比與隔離設計**：Epson 是低壓（噴墨）、Bosch 是高壓但脈衝式。**沒有任何公開案例是在「持續高場強」下做自感測**。這是客戶技術差異化的核心，也是最大的未知。

---

## 7. 來源清單

| # | 標題 | URL | 說明 |
|---|---|---|---|
| S1 | Branson / Telsonic PZT-4 & PZT-8 Piezo Ceramic Replacement | https://www.sinosonics.com/piezo-ceramic/branson-telsonic-piezo-ceramic-replacement-pzt4-pzt8/ | Langevin 構造、預應力功能、失效模式（熱去極化/機械開裂/剝離）與陶瓷更換實務 |
| S2 | Ultrasonic Replacement Branson Converter CJ20 (26 µm) | https://www.ultrasonic-metalwelding.com/sale-11580688-ultrasonic-replacement-branson-converter-cj20-with-26um-amplitude-for-2000x-welding-series.html | CJ-20 規格（**未驗證**，替代品供應商口徑） |
| S3 | Failure analysis of a 30 kHz ultrasonic welding transducer (IDEALS) | https://www.ideals.illinois.edu/items/18745 | **本輪最重要**：179–244% 失效振幅、FEA 208%、實驗室 vs 量產失效模式差異 |
| S3a | 同上（CORE 全文 PDF） | https://files01.core.ac.uk/download/pdf/4827087.pdf | 同上，另一取得管道 |
| S4 | Ultrasonic converter for ultrasonic welding (Herrmann Ultraschall) | https://www.herrmannultraschall.com/en/products/ultrasonic-components/converters | 「solid piezoceramic four-disk technology」；**無壽命數字** |
| S5 | Reliability analysis of ultrasonic power transducers (Archive of Applied Mechanics, 2014) | https://link.springer.com/article/10.1007/s00419-014-0965-4 | **關鍵**：明說超音波功率換能器可靠性幾無文獻、廠商不公布壽命；預應力量測精度 1.13% |
| S5a | 同上（TIB 全文 PDF） | https://edocs.tib.eu/files/e01fn13/770730868.pdf | 同上 |
| S6 | Ultrasonic Transducer Maintenance Tips (LeelaSonic) | https://www.leelaelectronics.in/transducer-maintenance.html | 換能器 5–10 年；乾燒數分鐘內報廢且不保固 |
| S7 | Lifetime Warranty (Blue Wave Ultrasonics) | https://bluewaveinc.com/why-blue-wave/lifetime-warranty | 銀焊換能器/振動膜終身保固 |
| S8 | Ultrasonic Power Warranty Information | https://www.upcorp.com/warranty-information/ | 10-5-2 保固（換能器 10 年） |
| S9 | ULTRACISION HARMONIC SCALPEL Service Manual | https://documents.cdn.ifixit.com/hYFs2VHlIHOCC3MX.pdf | 55 kHz/55.5 kHz、4 片壓電元件夾於兩鋁端鐘 |
| S10 | ULTRACISION HARMONIC SCALPEL HAND PIECE (K990430) | https://fda.innolitics.com/device/K990430 | Class II、510(k) 1999/3/12 |
| S11 | Ultrasonic Surgical Instrument, FDA Product Code LFL | https://fda.report/Product-Code/LFL | LFL 產品碼與已核准裝置清單 |
| S12 | Misonix neXus Ultrasonic Surgical Aspirator 510(k) K221235 | https://www.accessdata.fda.gov/cdrh_docs/pdf22/K221235.pdf | LFL/GEI/LBK；可重複使用手把 + 單次使用探針架構 |
| S13 | US20230210692A1 Disposable phaco handpiece | https://patents.google.com/patent/US20230210692A1/en | Phaco 28–45 kHz；滅菌縮短壽命；禁用超音波清洗手把 |
| S14 | IEC 60601-2-5:2009（超音波物理治療） | https://webstore.iec.ch/en/publication/2668 | 超音波治療設備的 particular standard（Ed 3.0） |
| S15 | Failure analysis of two aluminium alloy sonotrodes for ultrasonic plastic welding | https://www.sciencedirect.com/science/article/abs/pii/S0142112313001552 | 10^12 次十年設計壽命；鋁 sonotrode 於 ~5×10^9 次提前破斷 |
| S16 | Ultrasonic Welding – overview (ScienceDirect Topics) | https://www.sciencedirect.com/topics/physics-and-astronomy/ultrasonic-welding | 焊接時間 200–400 ms、多數 <1 s |
| S17 | Understanding ultrasonic welding (The Fabricator) | https://www.thefabricator.com/thewelder/article/arcwelding/understanding-ultrasonic-welding | 需空氣冷卻；過熱會使陶瓷失去壓電性 |
| S18 | Piezoceramics prestress control (ATCP) | https://www.atcp-ndt.com/en/essentials/prestress-technology.html | 預應力定義與目的 |
| S19 | Does loss of prestress occur over time? (ATCP FAQ) | https://www.atcp-ndt.com/en/support/faq_piezoclamping/345-is-there-prestress-relaxation-loss-in-converters-over-time-how-to-improve-prestress-retention.html | 預應力鬆弛機制與反覆上緊拋光螺紋的穩定化手法 |
| S20 | Self-Diagnosing Nozzle Health System (Epson) | https://corporate.epson/en/technology/search-by-products/printer-inkjet/nozzle-self-diagnosis.html | 壓電元件變形即發電、毫秒級自診斷 |
| S21 | Epson's Nozzle Verification Technology (Indian Printer & Publisher) | https://indianprinterpublisher.com/blog/2026/03/epsons-nozzle/ | **NVT 原理細節**：讀墨腔殘留振動、印字頭內建 IC、自動清潔或改由鄰近噴嘴補噴 |
| S22 | US 12,397,318 Ultrasonic transducer health status monitor | https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/12397318 | 脈衝驅動 + 振幅比對判定壓電阻抗異常（焊接換能器自診斷專利） |
| S23 | The dynamics of the piezo inkjet printhead operation (Physics Reports) | https://www.sciencedirect.com/science/article/abs/pii/S0370157310000827 | >10^10 次/通道；「每 10^9 滴 ≤1 次失效」驗收準則 |
| S23a | A Comprehensive Guide to Industrial Inkjet Printhead (Johope) | https://johopetech.com/print-basics/a-comprehensive-guide-to-industrial-inkjet-printhead/ | 工業要求 3–5 年、PZT 疲勞壽命 ≥1.5×10^11；Seiko >4×10^9 滴/噴嘴；Brother 10^11 滴（**均未驗證**） |
| S24 | IEC 60601-2-2:2017（高頻電外科） | https://webstore.iec.ch/en/publication/28118 | 確認 60601-2-2 是 RF 電外科、非超音波；<50 W 可豁免部分要求 |
| S25 | IEC 63041-1:2017 Piezoelectric sensors – Generic specifications | https://cdn.standards.iteh.ai/samples/22983/6d42bee1318240459015e28c54b6cd1d/IEC-63041-1-2017.pdf | 63041-1 原文樣本 |
| S26 | EN IEC 63041-1:2021 / 系列說明 | https://standards.iteh.ai/catalog/standards/clc/dd224443-0a64-4b81-88a2-eaa89017fae2/en-iec-63041-1-2021 | 63041-2（化學/生化）、**63041-3:2026（物理感測器）**涵蓋範圍 |
| S27 | IEEE 176 – Inactive-Withdrawn Standard | https://standards.ieee.org/ieee/176/6315 | **2000/3/6 撤銷；無授權中的修訂專案** |
| S28 | Multilayer Piezo Actuators – COM HAS (TDK datasheet) | https://product.tdk.com/system/files/dam/doc/product/sw_piezo/sw_piezo/piezo-actuator/data_sheet/piezostacks-com_s5.pdf | **85/85 對照數據**：95%Ag ~10^6、25%Pd ~4×10^6、Cu 10^8 零失效 |
| S29 | Piezo components for automotive: New EPCOS copper piezo actuators set benchmark (TDK) | https://www.tdk-electronics.tdk.com/en/373388/company/press-center/press-releases/press-releases/piezo-components-for-automotive-new-epcos-copper-piezo-actuators-set-benchmark/1049810 | **170°C 下 10^9 次切換無失效**；耦合係數 >75%；唯一使用 Cu 內電極的廠商 |
| S30 | Study of the Influencing Factors on the Small-Quantity Fuel Injection of Piezoelectric Injector (PMC) | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9146563/ | Continental 250 MPa、單循環 8 次噴射（2016） |
| S31 | Common-rail system with piezo injectors (Bosch Mobility) | https://www.bosch-mobility.com/en/solutions/powertrain/diesel/common-rail-system-piezo/ | 2,700 bar、Digital Rate Shaping |
| S32 | WO2010091902A1 Method for determining a needle closing in a piezo injector | https://patents.google.com/patent/WO2010091902A1/en | **由壓電致動器電壓偵測針閥關閉**；NCC 提升整車壽命期噴射精度 |
| S32a | Piezo injector for common-rail systems (Bosch CRI3) | https://www.bosch-mobility.com/en/solutions/injectors/piezo-injector-cri3/ | 含/不含 NCC 感測器的版本區分 |
| S33 | PrecisionCore Advanced Printing Technology (Epson US) | https://epson.com/precisioncore-advanced-printing-technology | 年產 >1,500 萬台；印字頭與機器同壽命；減少服務叫修 |
| S34 | SAMBA G3L (Fujifilm) | https://www.fujifilm.com/us/en/business/inkjet-solutions/industrial-printheads/samba-g3l | Si-MEMS + 濺鍍 PZT、沉積時即極化、內應力低 |
| S35 | Piezo actuators: 100 billion cycles without failures or loss in performance | https://www.engineerlive.com/content/piezo-actuators-100-billion-cycles-without-failures-or-loss-performance | 10^11 次零失效、96% 位移 |
| S36 | Supporting Space Research: Piezo Actuators in the Curiosity Mars Rover (PI) | https://www.pi-usa.us/en/expertise/markets/large-scale-scientific-projects/astronomy/discovering-mars-surface-conditions | CheMin 儀器、**16 顆** PICMA、通過 10^11 次才獲准 |
| S37 | PICMA Technology (Physik Instrumente) | https://www.physikinstrumente.com/en/expertise/technology/piezo-technology/picma | 全陶瓷封裝技術說明 |
| S38 | Multilayer Piezoelectric Actuators – ceramic vs polymer coated (AZoOptics) | https://www.azooptics.com/Article.aspx?ArticleID=219 | **`MTTF = AU × AT × AF`**；75%RH/100V/45°C → ~105,000 h |
| S39 | Ambient Conditions (Physik Instrumente) | https://www.physikinstrumente.com/en/expertise/technology/piezo-technology/properties-piezo-actuators/ambient-conditions | PICMA 壽命模型考慮溫度/濕度/電壓；**DC 模式下濕度主導** |
| S40 | What is the lifetime of a piezo motor (Xeryon) | https://xeryon.com/technology/what-is-the-lifetime-of-a-piezo-motor/ | 超音波 2,000 km / walking 50–100 km / stick-slip 10–30 km |
| S41 | How Do Piezo Motors Work? Ultrasonic, Stick-Slip, Walking (Xeryon) | https://xeryon.com/technology/how-do-piezo-motors-work/ | 磨耗機制差異（回程近乎不接觸 vs 每步滑回） |
| S42 | How do lenses "wear out"? (DPReview forum) | https://www.dpreview.com/forums/thread/2810955 | Micro USM 壽命短、失效前先吱吱聲；Ring USM 長壽（**未驗證，論壇來源**） |
| S43 | Lee Ventus long life disc pump exceeds 17,000 running hours (World Pumps) | https://www.worldpumps.com/content/news/lee-ventus-long-life-disc-pump-exceeds-17-000-running-hours | >17,000 h、可支撐 2 年連續使用 |
| S44 | LEE Ventus' Long Life Pump Exceeds 1 Trillion Cycles (Business Wire) | https://www.businesswire.com/news/home/20221031005024/en/LEE-Ventus%E2%80%99-Long-Life-Pump-Exceeds-1-Trillion-Cycles | **>10^12 次循環**；測試於 40°C + 限流負載 |
| S45 | New High Performance Long-life LT Disc Pump Models (Ion Science) | https://ionscience.com/en/news/new-high-performance-long-life-lt-disc-pump-models/ | >5,000 h（嚴苛條件）～10,000 h |
| S46 | TTP Ventus Technology / The Lee Co | https://www.ttpventus.com/technology | 固定容積腔內高頻聲學駐波 + 超快閥整流 |
| S47 | Microblower MZB1001T02 Reference Data Sheet (Murata) | https://media.digikey.com/pdf/Data%20Sheets/Murata%20PDFs/MZB1001T02_DS.pdf | 24–27 kHz、1 L/min@15Vpp、1,900 Pa、0.18 W；煙霧影響壽命 |
| S48 | Degradation of PZT-4D hard piezoceramics under moderate heating | https://www.sciencedirect.com/science/article/abs/pii/S0955221900002211 | **去極化始於 150°C；Qm 在 100°C 即有不可逆劣化** |
| S49 | Effect of temperature on the main piezoelectric parameters of a soft PZT ceramic | https://www.researchgate.net/publication/235988202_Effect_of_temperature_on_the_main_piezoelectric_parameters_of_a_soft_PZT_ceramic | <150 / 150–250 / >250°C 三段行為 |
| S50 | Defect dipoles elevating depolarization temperature to Curie point in PMS-PZT | https://www.sciencedirect.com/science/article/pii/S0272884225055841 | 缺陷偶極把去極化推遲至接近 Tc（365°C） |
| S51 | Piezoelectric multilayer actuator life test (PubMed) | https://pubmed.ncbi.nlm.nih.gov/21507759/ | 2,000 Hz / 0–20 V 加速壽命試驗；試後量絕緣阻抗取最低值 |
| S52 | Thermal activation energy on electrical degradation in BaTiO₃ MLCC for lifetime reliability (PMC) | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10770127/ | **Prokopowicz–Vaskas（Arrhenius 基礎）**為陶瓷多層元件壽命預測慣用模型 |
| S53 | Lifetime of piezoceramic multilayer actuators: Interplay of material properties and actuator design (J. Electroceramics 22:163–170, 2009) | https://link.springer.com/article/10.1007/s10832-007-9411-0 | 裂紋於壽命早期即生成；濕度加速；黏著中間層選擇影響壽命 |
| S54 | Fatigue crack growth driven by electric fields in piezoelectric ceramics | https://www.sciencedirect.com/science/article/abs/pii/S0020722507001450 | Paris 型冪次律可用於電疲勞裂紋成長 |
| S55 | Cyclic fatigue due to electric loading in ferroelectric ceramics | https://www.sciencedirect.com/science/article/abs/pii/S0955221998004294 | 0.9–1.5 Ec 循環；成長率隨循環下降、~10^5 次飽和 |
| S56 | Cyclic Fatigue Crack Growth in Three-Point Bending PZT Ceramics under Electromechanical Loading (J. Am. Ceram. Soc., 2007) | https://ceramics.onlinelibrary.wiley.com/doi/10.1111/j.1551-2916.2007.01774.x | 裂紋成長率對最大能量釋放率與 DC 場敏感 |
| S57 | Temperature Humidity Bias (THB) Testing / IEC 60068-2-67 (Infinita Lab) | https://infinitalab.com/blog/temperature-humidity-bias-thb-testing/ | 85/85 + 偏壓；HAST（JESD22-A110）加速 10–100×、96–264 h |
| S58 | US 7,902,726 Multi-layer piezoelectric device | https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/7902726 | 100% Ag 內電極因銀遷移造成火花與斷線 |
| S59 | "Singing" Multilayer Ceramic Capacitors and Mitigation Methods—A Review (Sensors, MDPI) | https://www.mdpi.com/1424-8220/22/10/3869 | **金屬端子 −25 dB**；特殊型最多 −10 dB |
| S60 | MLCC solutions for suppressing acoustic noise (Murata) | https://article.murata.com/en-us/article/measures-against-mlcc-squealing-in-laptop-battery-lines | KRM（金屬端子）/ ZRA・ZRB（interposer）/ GJ4（低介電常數）三路線；成本是採用阻力 |
| S61 | How to Reduce Acoustic Noise of MLCCs in Power Applications (TI SSZTB09) | https://www.ti.com/lit/pdf/ssztb09 | TDK CKG 等對應方案 |
| S62 | ISO 80079-36:2016 Explosive atmospheres Part 36 | https://www.iso.org/standard/56550.html | 非電氣設備防爆；機械能轉點火源須做 IHA（**無壓電專屬條款**） |
| S63 | EEE-INST-002 (NASA NEPP) | https://nepp.nasa.gov/pages/EEE-INST-002.cfm | 篩選/鑑定/降額三段式、Level 1–3（**未見壓電類別**） |
| S64 | AEC-Q200 Rev E Base Document | http://www.aecouncil.com/Documents/AEC_Q200_Rev_E_Base_Document.pdf | 車規被動元件應力測試（**未見壓電致動器分類**） |
| S65 | Advantages of Murata's CERALOCK for automotive applications | https://www.murata.com/products/timingdevice/ceralock/overview/app/auto | 車用版與一般版差異在操作溫度與環境特性（**未見 AEC-Q200 宣稱**） |

---

### 附：由本輪數據直接導出的「研發階段可靠性驗證計畫」與試驗設備清單

| # | 驗證項目 | 依據（來源） | 加速條件建議 | 需要的設備 |
|---|---|---|---|---|
| V1 | **Qm 退化為主指標的熱-場加速壽命試驗** | Qm 於 100°C 即不可逆劣化［S48］ | 多組（溫度 × 場強）矩陣，連續共振驅動；以 Qm 而非 d33 判退化 | 高功率壓電量測系統、精密溫控腔陣列、原位阻抗/導納追蹤、雷射測振儀（量真實振速）、紅外熱像 |
| V2 | **85/85 THB + HAST 濕度壽命** | Ag 10^6 / AgPd 4×10^6 / Cu 10^8［S28］；HAST 加速 10–100×［S57］ | 85°C/85%RH + 額定偏壓 1,000 h；HAST 96–264 h 作快篩 | 恆溫恆濕箱（THB）、HAST 箱、絕緣阻抗長期監測、SEM-EDX（查銀枝晶） |
| V3 | **振幅過載餘裕試驗（step-stress）** | 焊接換能器失效落在 179–244% 標稱振幅［S3］ | 階梯升振幅至破壞，求失效分佈而非單點 | 可程式高功率驅動源、LDV、聲學掃描顯微鏡（SAM）、微焦點 X-ray CT |
| V4 | **電疲勞（雙極/單極場循環）** | 0.9–1.5 Ec 循環最傷；~10^5 次飽和［S55］ | 以 Ec 正規化的場強掃描；至少涵蓋 10^6 次 | 高壓函數產生器、Sawyer-Tower P-E 迴線、裂紋觀測（染色滲透/CT） |
| V5 | **金屬結構疲勞（預壓件/端子/焊點）** | 鋁 sonotrode 5×10^9 次提前破斷、批次差異大［S15］ | 獨立 S-N 曲線 + 批次管制 | 共振疲勞試驗台、應變量測、金相切片、批次材料驗收 |
| V6 | **預應力鬆弛長期監測** | 鬆弛機制與螺紋拋光穩定化［S18］［S19］ | 熱循環 + 長期運轉後回測預應力 | 超音波預應力量測、扭矩-拉力校驗機、熱循環箱 |
| V7 | **自感測通道的靈敏度漂移與隔離** | Epson NVT［S20］［S21］、Bosch NCC［S32］ | 高壓驅動下量測 mV 級感測訊號的 SNR 隨溫度/老化變化 | 電荷放大器（高共模）、高速取樣、隔離量測前端、長期基準管理平台 |
| V8 | **可聽噪音與 PCB 耦合** | 金屬端子僅 −25 dB［S59］ | 對照組：直焊 / interposer / 金屬端子 / 對稱擺放 | 消音室 + 聲壓計、掃描式 LDV、模態分析 |
| V9 | **樣本數與統計** | 噴墨業界準則「10^9 滴 ≤1 次失效」［S23］ | 規劃 Weibull 分析所需樣本量，禁止單顆展示測試 | 多通道平行老化台（同時跑數十顆）、自動資料擷取 |
| V10 | **認證前置對齊** | 無 AEC-Q200 分類、無 60601 超音波手術專章、IEEE 176 已撤銷［S27］［S64］ | 不是實驗，是專案管理 | 及早引入認證顧問；車用談 AEC-Q200 客製 plan；醫療以 LFL/GEI 前案對標；感測宣稱掛 IEC 63041-3 |
