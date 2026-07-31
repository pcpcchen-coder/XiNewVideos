# 應用A1：壓電高壓產生 → 冷電漿、臭氧、消毒、表面處理、離子化

> 一句話結論：壓電直接放電（PDD）是目前「非電感替代」路線上**唯一已量產、已商品化、已有 TDK 級大廠背書**的壓電主動／被動兩用元件應用——單一顆 PZT 陶瓷同時扮演機械共振器（被動儲能）、升壓變壓器（被動）與放電電極（主動），把 12–24 V 直接變成 >10 kV 的常溫電漿；但它的真實新能力集中在「手持化／可拋棄化／可嵌入化／點狀選擇性處理」，而非「更大面積更便宜」，且 2026 年 TDK 正在把 relyon plasma 賣給 Viromed Medical 這件事，是必須嚴肅看待的商業化警訊。

---

## 0. 研究方法與限制（誠實揭露）

- **WebFetch 在本環境被 egress policy 全面封鎖**（任何 URL 回 403），因此本報告 **100% 依賴 WebSearch 回傳的「連結清單 + 模型彙整摘要」**，沒有任何一段是我親自打開原文頁面讀到的。
- **原訂 25–35 次查詢的計畫被迫中止**：本 session 的 WebSearch 額度（200 次，與同批其他研究 agent 共用）在我送出第 17、18 次查詢時已耗盡，系統回傳 `this session has used its web search budget (200 of 200 WebSearch calls)`。**我實際只完成 16 次有效查詢。**
- 因此本報告的定位是：**高密度的第一輪偵察，不是完整盡職調查**。第 6 節列出的未解問題比一般報告多，是刻意的。
- **明確查無的項目（不要當成「沒有」，要當成「沒查到」）**：
  1. CeraPlas HF / CeraPlas F 的**單價**（Mouser、DigiKey 都有產品頁但搜尋摘要不含價格）。
  2. CeraPlas 的**壽命小時數 / MTBF / 陶瓷侵蝕速率**的官方或第三方定量數據。
  3. 壓電臭氧產生的 **g/kWh 能效**具體數字（只查到定義，沒查到數值）。
  4. piezobrush PZ3 的**售價**與 relyon 的**營收規模**。
  5. PZT 含鉛與 **RoHS 豁免**在壓電電漿元件上的適用狀態。
  6. 汽車座艙、食品包裝內殺菌、化生防護這三塊我**完全沒查成**（額度已用盡），本文中相關段落一律標為「推論／未驗證」。
- **標記規則**：`[未驗證]` = 僅來自搜尋摘要、無法交叉比對；`[推論]` = 我根據物理／商業常識推導，不是查到的事實；其餘為至少有兩個獨立來源摘要互相支持者。

---

## 1. 結論摘要

1. **PDD 的核心賣點就是客戶的命題本身**：Rosen 型壓電變壓器（PT）在單一片 PZT 上同時完成「機械共振儲能（被動）＋電壓轉換 >1000 倍（被動）＋直接在陶瓷表面點燃微放電（主動）」，等於免掉了傳統常壓電漿源的高壓繞線變壓器、高壓線材與高壓安規隔離。（來源 1, 2, 12）
2. **量產元件規格明確**：TDK **CeraPlas F** 尺寸 72 × 6 × 2.8 mm、約 8 g、工作頻率 50 kHz、輸入 12–24 V、輸出 <15 kV、升壓比約 1000、**最大工作功率 8.0 W**。`[未驗證：來自搜尋摘要彙整的 datasheet 數值]`（來源 5, 6, 46）
3. **封裝品 CeraPlas HF** 為 47.3 × 20 × 20 mm 塑膠外殼、可焊接引腳，設計目標為常壓常溫下游離多種氣體，**電漿溫度 < 50 °C**，可處理熱敏材料；實驗樣品料號 Z63000Z2910Z 1Z60、評估套件 1Z61。（來源 4, 7, 51）
4. **終端產品已上市多年**：relyon plasma **piezobrush PZ3** 手持機，**整機最大耗電 18 W**、電漿溫度 <50 °C、處理速率「每秒數平方公分」量級；PZ3-i（自動化版）平均處理寬度 **5–29 mm**（需壓縮乾燥空氣 CDA）。前代 PZ2 已於 **2021-11-30 停產**由 PZ3 接替。（來源 10, 11, 12, 13, 47）
5. **大面積化有硬性物理天花板**：MDPI *Plasma* 4(2):19 的多元件 PDD 研究指出，相鄰壓電電漿產生器之間因**寄生耦合**，**最小可運作間距為 4 cm**；再加上活化區必須重疊才能均勻，導致陣列的面功率密度被鎖死。以 8 W／(4×4 cm) 粗估約 **0.5 W/cm²** `[推論]`，遠低於工業電暈滾輪機的 kW 級。（來源 14, 15）
6. **醫療端的殘酷事實**：目前歐洲三款取得 CE 醫材認證的慢性傷口冷電漿裝置——PlasmaDerm VU-2010（CINOGY）、kINPen MED（INP Greifswald / neoplas，Class IIa，2013 上市）、SteriPlas（Adtec）——**沒有一款是壓電式**。壓電式在醫材法規路徑上仍是 0 分。（來源 21, 22, 23）
7. **市場數字看起來漂亮但要打折**：多家機構給 2025 年冷電漿市場 **USD 2.4–3.3 B**，2032–2035 年 **USD 5–12 B**、CAGR 14–16%，常壓段佔 **66%**。但這些數字把醫療、食品、半導體、紡織全包進去，**壓電式只佔其中極小一角** `[推論]`。（來源 30, 31, 32）
8. **最重要的反面訊號**：TDK 子公司 EPCOS 於 2018 年取得 relyon plasma **50.2%** 股權；到 **2026 年 3 月 4 日** Viromed Medical AG 簽署 LOI 要收購 relyon，**2026 年 7 月 27 日**完成盡職調查、與 TDK Electronics 達成非約束性共識，價格區間為「**低至中雙位數百萬歐元**」。八年後大廠選擇賣掉，且價格只有數千萬歐元等級——這代表 CeraPlas 沒有長成 TDK 想要的元件出貨量生意。（來源 27, 28, 29）

---

## 2. 現況：技術 / 產品 / 玩家

### 2.1 技術原理

PDD 使用 Rosen 型 PT：輸入段（primary）施加 12 或 24 V 交流，頻率鎖在機械共振點（數十至數百 kHz），輸出段（secondary）因壓電—彈性—壓電的能量轉換鏈產生極高電位。與電暈放電、介質阻障放電（DBD）的關鍵差異在於：**微放電直接在陶瓷表面點燃**，使其在物理與應用潛力上自成一類。可在空氣或其他氣體、寬壓力範圍（含常壓）下點燃。（來源 1, 2, 52）

實務上有兩種操作模式：
- **直接模式（direct / PDD）**：待處理物就在陶瓷輸出端附近，接受帶電粒子＋自由基共同作用；活化效果強但作用距離短。
- **間接／噴射模式（APPJ）**：吹入氣流把活性物種帶出，成為常壓電漿噴流；Korzec 2020（*Plasma Processes and Polymers*）即以 PDD 驅動 APPJ。註：**降低氣流反而提升處理效率**（來源 3, 12）——這是很重要的工程反直覺點。

### 2.2 元件層：TDK CeraPlas 家族

| 型號 | 定位 | 備註 |
|---|---|---|
| CeraPlas F | 裸陶瓷元件（OEM 內建用） | 72 × 6 × 2.8 mm，8 W `[未驗證]` |
| CeraPlas HF | 塑膠封裝、可焊接 | 47.3 × 20 × 20 mm；主打高游離率、高效臭氧產率、多氣體點燃、**無磁場** |
| CeraPlas ExploreKit（EK1250101 系列） | 乾式消毒開發套件 | 含過濾延伸單元＋Android App 可自訂消毒流程；TDK 定位為「病毒生物去污」解決方案的開發平台 |

CeraPlas 曾獲創新獎項（TDK 自述）。（來源 4, 5, 6, 38, 39, 51）

### 2.3 系統層：relyon plasma（Regensburg, DE）

- **piezobrush PZ3**：手持機，PDD® 為註冊技術名稱，核心即 CeraPlas F；五種可換模組（Standard / Nearfield / Needle / Nearfield Needle / Multigas）。（來源 10, 12）
- **piezobrush PZ3-i**：整合／自動化版本，可掛在機器人手臂當末端執行器（已上架 igus rbtx 機器人零組件平台）。（來源 11, 50）
- **通路**：英國 Intertronics、澳洲 Nano Vacuum、Ulbrich Group、Axend 等代理；牙科通路 Chairside Solutions 也有賣 PZ3 Professional Set。（來源 47, 48, 49, 57）
- **已具名客戶**：PIL Sensoren GmbH（提升黏合品質）、Kunststoff-Zentrum SKZ（塑膠研究機構，把 piezobrush 納入表面前處理服務組合）。（見來源 9、10 的 relyon 公司頁敘述）

### 2.4 學術玩家

- **Dariusz Korzec**（relyon plasma / TDK Tokyo）：PDD 領域最主要的作者，2020–2021 連發 *Plasma Processes and Polymers*、MDPI *Plasma* 綜述與多元件陣列研究。（來源 2, 3, 14）
- **INP Greifswald**：冷電漿醫學與電漿農業重鎮，kINPen 系列出身地；有 PDD 電漿活化水（PAW）相關研究。（來源 16, 21, 22）
- **法國 HAL 收錄**「Low voltage plasma jet with piezoelectric generator」：討論壓電表面火花抑制、抗侵蝕材料（單晶鋰系或硬 PZT）與介電薄膜塗層。（來源 36）
- **arXiv 2412.09761**：以冷壓電電漿打膽管癌細胞的體外效能與細胞機轉研究 `[未驗證，僅見標題與摘要片段]`。（來源 40）

---

## 3. 關鍵數字表

| 項目 | 數值 | 來源 | 可信度 |
|---|---|---|---|
| PT 升壓比 | > 1000 | 2, 12 | 高（多來源） |
| 輸入電壓 | 12–24 V（典型 < 25 V） | 1, 2, 5 | 高 |
| 輸出電壓 | > 10 kV；CeraPlas F < 15 kV | 1, 5 | 中（HF/F 混用需釐清） |
| 共振頻率 | 數十~數百 kHz；CeraPlas F 約 50 kHz | 1, 5 | 中 |
| CeraPlas F 尺寸 / 重量 | 72 × 6 × 2.8 mm / 8.0 g | 5, 46 | `[未驗證]` |
| CeraPlas F 最大工作功率 | 8.0 W | 5 | `[未驗證]` |
| CeraPlas HF 尺寸 | 47.3 × 20 × 20 mm | 4, 7 | 高 |
| 電漿／處理溫度 | < 50 °C | 4, 10, 12 | 高 |
| piezobrush PZ3 整機最大耗電 | 18 W | 10, 12 | 高 |
| PZ3-i 平均處理寬度 | 5–29 mm（CDA） | 11 | 中 |
| PZ3 處理速率 | 數 cm²/s 量級 | 12 | 中 |
| 陣列最小元件間距 | 4 cm（寄生耦合限制） | 14, 15 | 中高 |
| 臭氧濃度（O₂ 3 SLM） | 最高 852 ppm | 2 | `[未驗證]` |
| 臭氧濃度（N₂/O₂ 混合，純氧上限） | 485 ppm | 2 | `[未驗證]` |
| PAW 中 NO₂⁻ / H₂O₂（PDD，數分鐘） | ~100 µmol/L 量級 | 16, 17 | 中 |
| 對照：DBD PAW 最高 NO₃⁻ / NO₂⁻ | 220.1 / 5.78 mg/L | 見來源 16 檢索結果群 | `[未驗證]` |
| 未處理 PTFE 水接觸角 | 126° | 56 | 中 |
| 未處理 PP 水接觸角 → 處理後 | 82° → 60°（某專利實施例） | 56 | 低（專利數據） |
| 冷電漿市場（2025） | USD 2.4–3.3 B | 30, 31, 32 | 中（市調報告本身不確定） |
| 冷電漿市場（2032–2035） | USD 5–12 B，CAGR 14–16% | 30, 32 | 中 |
| 常壓段市佔 | 66%（2025） | 30 | 中 |
| relyon 交易價（Viromed 收購） | 低至中雙位數百萬歐元 | 28, 29 | 中 |
| UL 2998 零臭氧門檻 | < 0.005 ppm（法規值 0.050 ppm 的 1/10） | 33 | 高 |
| CDC/FEMA 測到某離子化裝置臭氧 | > 1000 ppb | 34, 35 | `[未驗證]` |

---

## 4. 「新能力型」應用機會

> 評分欄位說明：**非替代性 = 是**（以前物理上做不到）／**半**（以前能做但形態完全改變，開出新的使用場景）／**否**（純粹更小更便宜的替代）。

### 4.1 「元件即耗材」：可拋棄式無菌一次性電漿頭

- **新能力是什麼**：因為高壓不再需要外部繞線變壓器與高壓線，整個高壓段就是**一片幾克重的陶瓷**，接口只有 24 V 低壓兩線。這讓「把高壓源做成拋棄式耗材」在成本與安規上第一次變得可行——低壓端留在主機、陶瓷片隨病人／隨批次丟棄。
- **為什麼以前做不到**：傳統高壓源（繞線變壓器＋高壓電纜＋高壓連接器）本身就是最貴、最重、最需要安規認證的部分，不可能做成耗材；而且高壓連接器插拔本身就是失效與漏電風險點。PDD 把高壓「關」在單一元件內部，插拔面只有低壓。
- **非替代性**：**是**。這是拓樸改變，不是尺寸縮小。
- **誰在做**：目前查無公開的商品化案例（`查無`）。TDK ExploreKit 的「乾式消毒 + 過濾單元 + App 自訂流程」是最接近的骨架（來源 38）。
- **TRL**：3–4（概念可行、元件現貨，但無公開驗證品）。
- **市場訊號**：牙科通路已在賣 PZ3（來源 48）；牙科／傷口科正是最需要一次性頭的場域。
- **技術難點**：陶瓷表面在放電下的侵蝕與污染累積（來源 36 明言需抗侵蝕材料與介電塗層）；一次性化反而讓「壽命短」從缺點變成特性——這是最漂亮的一手，但要先量化到底能撐多久（`查無壽命數據`）。

### 4.2 機器人末端執行器上的「點狀、選擇性」表面活化

- **新能力是什麼**：把 <20 W、<50 °C、寬 5–29 mm 的電漿源直接裝在六軸手臂或 SCARA 上，**只活化要塗膠的那一條膠道**，而不是活化整片料。可跟隨 3D 曲面、可進凹槽。
- **為什麼以前做不到**：電暈處理是滾輪對電極的**大面積、平面、連續料捲**製程；火焰處理有明火與熱負荷；常壓電漿噴射（Plasmatreat 等）功率高、噴嘴重、需要外部高壓產生器與冷卻。三者都無法做到「幾瓦、幾十克、隨手臂走的一條 5 mm 線」。
- **非替代性**：**半**（電暈／火焰能做「活化」這件事，但做不到選擇性、局部、低熱、輕量、可裝機器人）。開出的新場景包括：熱敏電子組件的局部前處理、貴重／小批量件、混線生產不同料號不需換電極。
- **誰在做**：relyon piezobrush PZ3-i，已上架 igus rbtx 平台（來源 11, 50）；Intertronics 主打半自動／自動化（來源 47）。
- **TRL**：**8–9（已商品化）**。這是本領域 TRL 最高的一項。
- **市場訊號**：具名客戶 PIL Sensoren、SKZ；多國代理商網絡。
- **技術難點**：**處理速率只有數 cm²/s**，一旦客戶要的是整片，PDD 立刻輸給電暈；作用距離短（近場模組）對機器人的路徑精度要求高；CDA 供氣需求削弱「純電池化」的賣點。

### 4.3 電池供電、可攜、可進體腔的醫療／牙科電漿

- **新能力是什麼**：24 V 以下輸入、無外部高壓、無磁場、<50 °C，理論上可做成筆型甚至內視鏡通道尺寸（CeraPlas F 截面僅 6 × 2.8 mm）的**院外／床邊／野戰**電漿裝置。牙周袋、根管、口腔黏膜這種「窄、深、濕、熱敏」的部位，是傳統氬氣噴流機（需氣瓶、需推車）進不去的。
- **為什麼以前做不到**：三款 CE 認證裝置全部需要外部電源櫃或氣體供應（kINPen 用氬氣、SteriPlas 為微波電漿）。體積與氣體依賴決定了它們只能在診間使用。
- **非替代性**：**半到是**。「治療慢性傷口」不是新能力（kINPen 2013 就在做），但「電池供電、無氣瓶、可拋棄頭、可帶回家／帶到床邊／帶進災區」是新能力。
- **誰在做**：學術端有壓電 CAP 對牙周／植體周病原菌與生物膜的體外研究（來源 25, 26, 58）、對膽管癌細胞的體外研究（來源 40）；產品端 relyon 有牙科應用頁與牙科通路（來源 26, 48）。**但沒有任何壓電式取得醫材認證。**
- **TRL**：4–5（體外實證多，臨床與法規為 0）。
- **市場訊號**：**Viromed Medical AG 2026 年收購 relyon 的明確理由就是「打造整合型冷電漿技術平台」並推進法規（regulatory push）**（來源 28, 29）——這是本報告中最強的市場訊號，也是最值得追蹤的單一事件。
- **技術難點**：醫材認證（Class IIa 起跳、MDR 下臨床證據門檻已大幅提高）；劑量學（dosimetry）標準化——冷電漿醫學至今沒有公認的「劑量」定義；PZT **含鉛**用於人體接觸裝置的生物相容性與法規爭議 `[推論，未查證]`。

### 4.4 密閉小腔體內的「原位乾式去污」（無耗材、無濕氣、無殘留）

- **新能力是什麼**：把幾克重的元件直接**放進**要消毒的腔體內（器械盒、儲物箱、鞋櫃、冰箱抽屜、口罩／濾材匣、無人機運送箱），24 V 一開就地產生 RONS 與臭氧，關掉後臭氧自行分解，**不需要藥劑、不需要補充耗材、不需要濕氣、不需要把物件送去中央滅菌**。
- **為什麼以前做不到**：等效方案是 UV-C（有陰影死角、對高分子材料劣化、對人眼皮膚有害）、過氧化氫霧化（需藥劑、需通風排空、有殘留）、次氯酸（濕、腐蝕）。要把「高壓放電源」塞進一個小盒子裡，以前意味著要塞一顆高壓變壓器與其安規距離。
- **非替代性**：**半**。消毒本身不新，但「消毒源縮到可內建於任意消費品內部」是新的產品型態。
- **誰在做**：TDK CeraPlas ExploreKit 明確以「病毒生物去污／乾式消毒流程」為訴求（來源 38）；relyon 有 PDD 對微生物作用的技術頁（來源 53）。arXiv 2109.03054 有 CAP 消毒 FFP3 口罩與長期材料影響的研究 `[未驗證，未讀原文]`（來源 41）。
- **TRL**：5–6（有開發套件、有 COVID 期間的應用推力，但沒看到量產終端品）。
- **市場訊號**：冷電漿市場常壓段 66% 市佔（來源 30）；但這塊最擁擠。
- **技術難點**：**臭氧副產物**。密閉腔體正是臭氧最容易累積的地方，而 UL 2998 的零臭氧門檻是 0.005 ppm——PDD 的賣點之一恰恰是「高效臭氧產率」（來源 4），兩者直接衝突。要嘛做成「開門前必須降解完畢」的時序控制，要嘛加觸媒分解層。這是產品定義層級的難題，不是調參數能解的。

### 4.5 分散式微型 RONS／電漿活化水（PAW）源

- **新能力是什麼**：以 8 W 級元件在**使用點**現場產生電漿活化水（含 NO₂⁻、NO₃⁻、H₂O₂），取代「工廠生產化學品 → 運輸 → 儲存 → 稀釋」的整條供應鏈。適用於精緻農業（灌溉水就地活化）、採後保鮮、小型食品加工、船上／野外淨水。
- **為什麼以前做不到**：PAW 的活性物種**壽命有限**，本質上不能運輸——所以必須就地產生；而就地產生以前需要一整台 DBD 電源櫃。把產生器縮到一片陶瓷，才讓「每一條灌溉支管配一顆」這種分散式拓樸成立。
- **非替代性**：**是**（分散式拓樸是新的），但**效能上目前輸給 DBD**：PDD 的 NO₂⁻/H₂O₂ 落在 ~100 µmol/L 量級（來源 16, 17），而 DBD 系統報導可達 NO₃⁻ 220 mg/L 級 `[未驗證]`。
- **誰在做**：Frontiers in Physics 2020「Properties and Use of Water Activated by Plasma of Piezoelectric Direct Discharge」（來源 16）、IOP EES 390:012039（來源 17）；INP Greifswald 電漿農業（來源 21 群）。
- **TRL**：3–4。
- **市場訊號**：弱。學術熱、商業冷。
- **技術難點**：功率密度不足（見 4.7 的物理天花板）；陶瓷長期接觸液體／高濕的可靠度完全未知（`查無`）；農業客戶對單價極度敏感，而壓電元件貴——這正是客戶排除「取代電感」路線的同一個成本邏輯，在這裡同樣成立，要小心。

### 4.6 電池供電的氣膠帶電源（可攜式粒狀物感測／集塵）

- **新能力是什麼**：用壓電電漿產生器對氣膠**充電**，作為可攜式／穿戴式微粒感測器（電量法 PM 感測）或微型靜電集塵器的離子源。查到的具名研究：「Aerosol Charging with a Piezoelectric Plasma Generator」（來源 20）。
- **為什麼以前做不到**：氣膠帶電傳統上用電暈針，需 kV 級外部高壓電源；在手機、穿戴式、無人機這類 3.7 V 電池裝置上不可能。PDD 讓 kV 級離子源第一次能被電池驅動並塞進消費品。
- **非替代性**：**是**（真的是新的功率／體積級距開出的新品類）。
- **TRL**：2–3。
- **市場訊號**：查無商品。僅一篇研究。
- **技術難點**：臭氧與 NOx 副產物在「貼身裝置」上是致命傷；元件單價 vs. 消費電子 BOM。

### 4.7 明確標示為「替代品」、應降低權重的方向（誠實揭露）

以下方向雖然 PDD 做得到，但**本質是更小／更薄／更便宜的替代**，不符合客戶要的 new capability，應降權：

- **取代電暈滾輪機做料捲表面處理**：處理速率 cm²/s vs. 電暈的 100+ m²/hr，**規模差 3–4 個數量級**，且陣列最小間距 4 cm 鎖死面功率密度。**不要碰。**
- **取代 UV-C 燈做空間消毒**：UV-C 燈非常便宜且成熟，PDD 在成本上打不過。
- **取代針尖式雙極離子產生器（NBPI）做空調除味**：NBPI 模組成本極低、已大規模安裝，且該市場正因臭氧與功效爭議而信譽受損（來源 34, 35）——**進入這個市場等於繼承別人的信譽問題**。
- **取代小型臭氧機**：市售臭氧機用電暈管，成本極低。

---

## 5. 反面證據、失敗案例與物理上限

### 5.1 最強的反面訊號：TDK 的八年與退場

2018 年 EPCOS（TDK）取得 relyon 50.2% 股權，全力推 CeraPlas（來源 27, 51）；2018–2021 密集出白皮書、產品、ExploreKit、拿創新獎（來源 38, 39）。**結果到 2026 年，TDK 選擇把 relyon 賣給一家德國小型上市醫材公司 Viromed Medical AG，價格是低至中雙位數百萬歐元**（來源 28, 29）。對照 TDK 的規模，這個數字幾乎等於「這條線沒做起來」。合理解讀：**CeraPlas 沒有找到任何一個能吃掉百萬顆／年的應用**，而元件廠的商業模式需要那個量。這一點必須放在客戶決策的最前面。

### 5.2 物理上限

1. **功率上限**：單顆 CeraPlas F 最大 8 W `[未驗證]`；PZ3 整機 18 W。Rosen 型 PT 的功率密度受**機械應力極限**與**自發熱／機械品質因數下降**雙重限制，且共振式元件的自發熱會讓共振頻率漂移，形成正回饋失控風險。想靠單顆放大功率在物理上就是死路。
2. **陣列化上限**：4 cm 最小間距（寄生耦合）＋活化區必須重疊以求均勻（來源 14, 15）。8 W / 16 cm² ≈ **0.5 W/cm²** `[推論]`。這是 PDD 大面積路線的天花板。
3. **PZT 材料退化**：長期電場作用下鈣鈦礦壓電陶瓷會發生**化學降解**——電致去氧化（electrically-induced deoxidation）使陶瓷轉為類金屬態、電阻改變（來源 37）。疊加放電本身對陶瓷表面的侵蝕（來源 36 提到需用抗侵蝕材料或介電塗層，而**塗層又必須承受基材的機械振動**——這是一個內在矛盾的需求）。**沒有任何公開的壽命數字**，這是最大的未知。
4. **含鉛**：PZT 是 Pb(Zr,Ti)O₃。醫療接觸、食品接觸、消費電子 RoHS 三個場域都會踩到 `[推論，未查證豁免狀態]`。
5. **作用距離極短**：直接放電模式下活性物種在常壓空氣中壽命以毫秒計，有效作用距離數 mm。這決定了它永遠是「近接／點狀」工具。

### 5.3 商業與法規上限

- **醫材**：三款 CE 認證冷電漿裝置無一為壓電式（來源 21, 22）。MDR 之下 Class IIa 的臨床證據要求已大幅提高；且 *Scientific Reports* 2022 的多中心隨機試驗把冷電漿與最佳實務敷料做的是**非劣性（non-inferiority）**比較（來源 24）——「不比敷料差」不是能撐起高價醫材的臨床論述。
- **臭氧**：UL 2998 要求 < 0.005 ppm，而 CeraPlas 的行銷賣點之一就是「高效臭氧產率」（來源 4）。這兩件事只能二選一。CDC/FEMA 曾測到某通過 UL 867 的離子化裝置臭氧升到 >1000 ppb（來源 34, 35），顯示監管與輿論對「放電式空氣處理」極不友善。
- **前代產品停產**：piezobrush PZ2 於 2021-11-30 停產（來源 13）。屬正常世代交替，但也顯示這條產品線的量體不大。
- **價格**：`查無` CeraPlas 與 PZ3 的實際價格。但客戶排除「取代電感」的理由（壓電元件單價高）在這裡**部分被抵銷**——因為 PDD 的競爭對手不是幾毛錢的電感，而是幾十到幾百美元的高壓變壓器＋高壓電源＋安規隔離。**這正是 A1 之所以是「非電感替代路線中最成熟方向」的根本原因，也應該是客戶投入與否的核心判準。**

---

## 6. 未解問題（給下一輪研究）

1. **壽命與可靠度（最高優先）**：CeraPlas 在連續放電下的 MTBF、陶瓷表面侵蝕速率、輸出電壓衰退曲線、共振頻率漂移。**沒有這個數字，4.1（可拋棄頭）與 4.4（內建消毒）都無法定價。** 查法：TDK datasheet 原文（`ceraplas-db.pdf`）、Korzec 的 MDPI 綜述全文、relyon 白皮書 Part II/III。
2. **實際單價**：CeraPlas F / HF 的 1k、10k、100k 數量級報價；piezobrush PZ3 售價。決定所有商業模型。
3. **臭氧／NOx 的定量產率與可控性**：g/kWh 能效、是否能透過氣體組成與功率調變把臭氧壓到 UL 2998 門檻以下、觸媒分解層的可行性。
4. **Viromed × relyon 交易的後續**：交割是否完成、Viromed 打算把 PDD 推進哪一條醫材適應症、是否會取得 CE Class IIa。這是未來 12 個月內最能證實或證偽本領域的單一事件。
5. **未查成的三個應用**（本輪額度用盡）：食品包裝內殺菌（in-package plasma）、汽車座艙、化生防護消毒。
6. **專利地景**：本輪只在搜尋結果中掃到 US10904995（Plasma generator）、US11141251 / US11786348 / US12409018（Apparatus for dental treatment，疑為同族）、US10242856 / US10395911 / US10580634（Systems and methods for relay ionization）等，**均未讀內文、未確認申請人**，需要一輪專門的專利檢索釐清 TDK / relyon 的圍牆有多厚、台灣廠商的自由實施空間（FTO）在哪。
7. **無鉛壓電材料（KNN、BNT）能否做 PDD**：若能，5.2 第 4 點的含鉛障礙可解，且是差異化切入點。本輪完全未查。

---

## 7. 來源清單

1. Piezoelectric direct discharge plasma — Wikipedia。PDD 原理、Rosen 型 PT、12/24 V 輸入、>10 kV 輸出的總覽。 https://en.wikipedia.org/wiki/Piezoelectric_direct_discharge_plasma
2. Korzec et al., "Piezoelectric Direct Discharge: Devices and Applications", *Plasma* 4(1):1, MDPI。本領域最主要的綜述，含升壓比 >1000、臭氧濃度量測。 https://www.mdpi.com/2571-6182/4/1/1
3. Korzec et al., "Atmospheric pressure plasma jet powered by piezoelectric direct discharge", *Plasma Processes and Polymers*, 2020。PDD 驅動 APPJ；氣流降低反提升效率。 https://onlinelibrary.wiley.com/doi/full/10.1002/ppap.202000053
4. TDK 新聞稿：Compact CeraPlas HF element for cold plasma。HF 尺寸 47.3×20×20 mm、<50 °C、料號。 https://www.tdk-electronics.tdk.com/en/373388/company/press-center/press-releases/press-releases/plasma-generators-compact-ceraplas-hf-element-for-cold-plasma/2435688
5. TDK CeraPlas 產品資料 PDF（未能開啟，僅見搜尋摘要）。CeraPlas F 尺寸、8 W、50 kHz、<15 kV。 https://www.tdk-electronics.tdk.com/download/2307712/39eb3392c71d1191b103aa31c6a0f1c5/ceraplas-db.pdf
6. TDK 技術文章：Cold plasma from a single component。「單一元件同時完成升壓與電漿產生」的官方論述。 https://www.tdk-electronics.tdk.com/en/373562/tech-library/articles/applications-cases/applications-cases/cold-plasma-from-a-single-component/1109546
7. Mouser（EU）CeraPlas HF 產品頁。通路可得性；未見價格。 https://eu.mouser.com/new/epcos/epcos-ceraplas-hf/
8. DigiKey CeraPlas 產品重點頁。通路可得性；未見價格。 https://www.digikey.com/en/product-highlight/e/epcos/compact-ceraplas-for-cold-plasma-technology
9. relyon plasma：CeraPlas HF 頁。系統商對元件的定位說明。 https://www.relyon-plasma.com/plasma-technology/ceraplas-en/?lang=en
10. relyon plasma：piezobrush PZ3 產品頁。18 W、<50 °C、五種模組。 https://www.relyon-plasma.com/piezobrush-pz3/?lang=en
11. relyon plasma：piezobrush PZ3-i 頁。自動化整合版、處理寬度 5–29 mm（CDA）。 https://www.relyon-plasma.com/piezobrush-pz3-i/?lang=en
12. Korzec et al., "piezobrush PZ3: Part I: Operation Principle and Characteristics"（白皮書 PDF）。處理速率數 cm²/s、低熱負荷可用於生物材料與組織。 https://www.relyon-plasma.com/wp-content/uploads/2024/02/201024_whitepaper_piezobrush_PZ3_1.pdf
13. relyon plasma：piezobrush PZ2 頁。2021-11-30 停產、由 PZ3 接替。 https://www.relyon-plasma.com/relyon-plasma-products/piezobrush-pz2/?lang=en
14. "Multi-Device Piezoelectric Direct Discharge for Large Area Plasma Treatment", *Plasma* 4(2):19, MDPI。**4 cm 最小間距**與均勻性限制。 https://www.mdpi.com/2571-6182/4/2/19
15. relyon plasma：Multi-Device PDD 白皮書頁。同上之產業版說明。 https://www.relyon-plasma.com/multi-device-piezoelectric-direct-discharge/?lang=en
16. "Properties and Use of Water Activated by Plasma of Piezoelectric Direct Discharge", *Frontiers in Physics* 8:616385, 2020。PDD 製 PAW 的物化性質與 RONS 濃度。 https://www.frontiersin.org/articles/10.3389/fphy.2020.616385/full
17. "Generation of plasma-activated water using a direct piezo-discharge: physicochemical aspects", *IOP Conf. Ser. EES* 390:012039。壓電放電製 PAW。 https://iopscience.iop.org/article/10.1088/1755-1315/390/1/012039
18. "Modelling of Inactivation Kinetics of E. coli on Radish and Hemp seeds…", *Food and Bioprocess Technology*, 2025。Piezobrush PZ3 vs DCSBD 的殺菌效果比較（PZ3 較弱）。 https://link.springer.com/article/10.1007/s11947-025-04082-3
19. "Efficacy Comparison of Three Atmospheric Pressure Plasma Sources for Soybean Seed Treatment"（ResearchGate）。含 Piezobrush PZ3 / CeraPlas F 的種子處理比較。 https://www.researchgate.net/publication/374738627_Efficacy_Comparison_of_Three_Atmospheric_Pressure_Plasma_Sources_for_Soybean_Seed_Treatment_Plasma_Characteristics_Seed_Properties_Germination
20. "Aerosol Charging with a Piezoelectric Plasma Generator"（ResearchGate）。氣膠帶電新應用。 https://www.researchgate.net/publication/353336421_Aerosol_Charging_with_a_Piezoelectric_Plasma_Generator
21. Bernhardt et al., "Plasma Medicine: Applications of Cold Atmospheric Pressure Plasma in Dermatology", PMC6745145。列出三款 CE 認證裝置。 https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6745145/
22. kINPen MED 章節（Springer）。Class IIa、2013 上市。 https://link.springer.com/content/pdf/10.1007/978-3-030-87857-3_16
23. neoplas med GmbH 產品頁。kINPen MED 商品化現況。 https://neoplas-med.eu/en/product/
24. "Chronic wounds treated with cold atmospheric plasmajet versus best practice wound dressings: a multicenter, randomized, non-inferiority trial", *Scientific Reports*, 2022。臨床證據強度的關鍵反面證據（非劣性設計）。 https://www.nature.com/articles/s41598-022-07333-x
25. "The In-Vitro Activity of a Cold Atmospheric Plasma Device Utilizing Ambient Air against Bacteria and Biofilms Associated with Periodontal or Peri-Implant Diseases", PMC9219831。空氣式 CAP 對牙周菌與生物膜。 https://pmc.ncbi.nlm.nih.gov/articles/PMC9219831/
26. relyon plasma：牙科表面處理技術頁。廠商牙科定位。 https://www.relyon-plasma.com/plasma-technology/plasma-technology-in-dentistry/?lang=en
27. TDK 新聞稿：EPCOS acquires majority stake in relyon plasma（50.2%，2018）。 https://www.tdk-electronics.tdk.com/en/373388/company/press-center/press-releases/press-releases/tdk-subsidiary-epcos-acquires-majority-stake-in-relyon-plasma/2240584
28. EQS/TradingView：Viromed Medical AG signs LOI to acquire relyon plasma GmbH（2026-03-04）。「整合型冷電漿技術平台」策略。 https://www.tradingview.com/news/eqs:f46067e6f094b:0-viromed-medical-ag-signs-letter-of-intent-to-acquire-relyon-plasma-gmbh-strategic-step-toward-integrated-platform-for-cold-plasma-technology/
29. Viromed Medical AG：Update on the planned acquisition of relyon plasma GmbH（盡職調查於 2026-07-27 完成；價格低至中雙位數百萬歐元）。 https://www.webdisclosure.com/press-release/viromed-medical-ag-etr-viromed-medical-ag-update-on-the-planned-acquisition-of-relyon-plasma-gmbh-IFaMLec9JBo
30. Precedence Research：Cold Plasma Market（2025 USD 3.28 B → 2035 USD 12.19 B，CAGR 14.03%；常壓段 66%）。 https://www.precedenceresearch.com/cold-plasma-market
31. Grand View Research：Cold Plasma Technology Market Report。第二方市場估計。 https://www.grandviewresearch.com/industry-analysis/cold-plasma-technology-market-report
32. GlobeNewswire / Coherent Market Insights：Cold Plasma Market to Hit USD 4.97 B by 2032（2025-11-11）。第三方市場估計，用以顯示估值分歧。 https://www.globenewswire.com/news-release/2025/11/11/3185580/0/en/Cold-Plasma-Market-Size-to-Hit-USD-4-97-Billion-by-2032-says-Coherent-Market-Insights.html
33. UL Solutions：Zero Ozone Emissions Validation（UL 2998，< 0.005 ppm）。臭氧法規門檻。 https://www.ul.com/services/zero-ozone-emissions-validation
34. US EPA：Can air cleaning devices that use bipolar ionization… protect me from COVID-19?。監管機關對放電式空氣處理的保留態度。 https://www.epa.gov/indoor-air-quality-iaq/can-air-cleaning-devices-use-bipolar-ionization-including-portable-air
35. Conservation Solutions Corp："A Word About Ionization Systems: DON'T DO IT"。含 CDC/FEMA 測到 >1000 ppb 臭氧的敘述（`[未驗證]`）。 https://www.conservationsolutions.com/2020/05/26/a-word-about-ionization-systems-dont-do-it/
36. "Low voltage plasma jet with piezoelectric generator"（HAL, hal-02640823v2）。抗侵蝕材料、介電塗層須耐基材振動。 https://hal.science/hal-02640823v2/document
37. "The Electrodegradation Process in PZT Ceramics under Exposure to Cosmic Environmental Conditions", PMC10180167。長期電場下 PZT 電致去氧化降解。 https://pmc.ncbi.nlm.nih.gov/articles/PMC10180167/
38. TDK：CeraPlas ExploreKit for decontamination（含過濾單元、Android App 自訂消毒流程）。 https://www.tdk-electronics.tdk.com/en/2910748/products/product-catalog/cold-plasma-technology/ceraplas-explorekit
39. TDK：Innovation prize for CeraPlas。廠商自述之外部肯定。 https://www.tdk-electronics.tdk.com/en/373618/tech-library/articles/company-trends/company-trends/innovation-prize-for-ceraplas/2611414
40. arXiv 2412.09761："Targeting Cholangiocarcinoma Cells By Cold Piezoelectric Plasmas: In Vitro Efficacy And Cellular Mechanisms"。壓電電漿抗癌體外研究（`[未驗證]`）。 https://arxiv.org/pdf/2412.09761
41. arXiv 2109.03054："Cold Atmospheric Plasma Sterilization of FFP3 Face Masks and Long-Term Material Effects"（`[未驗證]`）。 https://arxiv.org/pdf/2109.03054
42. Justia：US 10,904,995 "Plasma generator"。專利地景線索，申請人未確認。 https://patents.justia.com/patent/10904995
43. USPTO：US 11,141,251 "Apparatus for dental treatment"（同族尚有 11,786,348 / 12,409,018）。牙科電漿專利線索，申請人未確認。 https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/11141251
44. USPTO：US 10,580,634 "Systems and methods for relay ionization"（同族 10,242,856 / 10,395,911）。離子化專利線索，申請人未確認。 https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/10580634
45. Texim Europe：Cold atmospheric pressure plasma promises decisive benefits（PDF）。通路商技術文件，含 CeraPlas 應用敘述。 https://www.texim-europe.com/getfile.ashx?id=113097
46. Sekorm：CeraPlas Element 初步資料（Z63000Z2910Z 1Z68，F series packaged component）。第三方轉載之規格頁。 https://en.sekorm.com/doc/2581106.html
47. Intertronics：PiezoBrush PZ3 產品頁。英國通路與定位。 https://intertronics.co.uk/product/piezobrush-pz3-handheld-plasma-surface-treatment/
48. Chairside Solutions：relyon plasma piezobrush PZ3 Professional Set。牙科通路已在銷售的證據。 https://www.chairsidesolutions.com/shop/p/relyonplasmapiezobrush
49. relyon plasma 線上商店：piezobrush PZ3 Professional Set。 https://www.relyon-plasma.com/produkt/piezobrush-pz3-professional-set/?lang=en
50. igus rbtx：piezobrush PZ3-i 作為機器人末端執行器上架。自動化整合的市場訊號。 https://rbtx.com/en-US/components/end-effectors/cold-plasma-device-improved-adhesion-ink-glue-relyon-plasma-piezobrush-pz3-i
51. GlobeNewswire：TDK Introduces CeraPlas HF Compact Cold Plasma Generator Element（2018-11-13）。上市時間點。 https://www.globenewswire.com/news-release/2018/11/13/1650541/0/en/TDK-Introduces-CeraPlas-HF-Compact-Cold-Plasma-Generator-Element.html
52. relyon plasma：PDD 技術頁。PDD® 商標與技術定義。 https://www.relyon-plasma.com/technology/pdd/?lang=en
53. relyon plasma：Effect of piezoelectric direct discharge plasma on microorganisms。殺菌訴求的廠商依據。 https://www.relyon-plasma.com/effect-of-piezoelectric-direct-discharge-plasma-on-microorganisms/?lang=en
54. Mechanics / MMech："50 Years of Piezoelectric Transformers — Trends In The Technology"（PDF）。PT 技術史與功率密度脈絡。 https://www.mmech.com/images/stories/Standard_Products/Transformers/PT_Introduction/50_Years.pdf
55. "A compact ozone generation system using piezoelectric transformer"（ResearchGate）。壓電臭氧產生的獨立研究。 https://www.researchgate.net/publication/290078131_A_compact_ozone_generation_system_using_piezoelectric_transformer
56. relyon plasma：Surface activation of low energy surfaces with plasma。PP／矽膠／Teflon 表面能提升。 https://www.relyon-plasma.com/surface-activation-of-low-energy-surfaces/?lang=en
57. Ulbrich Group：piezobrush PZ3「世界最小電漿手持機」。通路行銷語言。 https://www.ulbrich-group.com/piezobrush-pz3-the-world-s-smallest-plasma-handheld-device
58. "Guided Plasma Application in Dentistry—An Alternative to Antibiotic Therapy", PMC11350922。牙科冷電漿的臨床論述。 https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11350922/
59. arXiv 2506.17072："A low-cost plasma source aimed for medical applications using Ar as the working gas"。競爭技術路線（低成本氬氣源）。 https://arxiv.org/pdf/2506.17072
