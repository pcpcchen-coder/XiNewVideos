# 應用B4：極端溫度——高溫（井下/渦輪/太空）與極低溫（量子運算）

> 一句話結論：**溫度是磁性元件唯一無法用工程手段繞過的物理牆（居里點在上、磁芯損耗劣化在下），而壓電體在兩端都還活著——但本輪唯一被硬證據支撐的具體元件級成果只有一個：SAW 隔離閘極驅動器實測工作範圍 0.5 K – 544 K（−272.6 °C 至 +271 °C）；高溫端的材料存在但 d 常數低到只能感測不能致動，低溫端則整條路線本輪完全未能查證。**

---

## 0. 研究方法與限制（誠實揭露）

**本節必讀。本文件的證據等級顯著低於本專案其他 dossier，客戶必須知道原因。**

- **本輪我實際完成的 WebSearch 次數：0（零）次。** 原規劃 25–35 次查詢，但在發出第一批查詢時，工具即回傳 `this session has used its web search budget (200 of 200 WebSearch calls)`。WebSearch 額度是**整個 session 共用**，在本子任務啟動前就已被同批的姊妹子任務（01/02/03/04/06/07/10/11/15/16/20/21 等 dossier）耗盡。我沒有任何辦法取得新的一手資訊。
- **WebFetch 在本環境被 egress policy 全面封鎖**（任何 URL 皆回 403），依任務書指示全程未使用。
- **因此本文件的事實來源只有兩類，我在全文中以標記嚴格區分：**
  - **【已查證】** — 事實與 URL 均**轉引自本專案同 repo 的姊妹 dossier**（`03-materials-manufacturing.md`、`04-reliability-standards-qual.md`、`15-magnetic-immune-clean.md`、`16-isolation-gatedrive-throughwall.md`）。這些事實是前面幾個子任務用真實 WebSearch 取得的，URL 完整可點，但**我本輪未再獨立核對**。
  - **【未查證假設】** — 出自我（模型）的內部知識，**本輪完全沒有任何搜尋或來源支撐**。這些**不附 URL，因為附上就是編造**。客戶**不得**引用任何一條標記為【未查證假設】的內容，它們的唯一用途是**當作下一輪研究的查證清單**（見 §6）。
- **本任務書明列、但本輪完全沒查到（列為下一輪必查）：**
  - 井下電子的實際溫度分級與失效統計（Schlumberger / Halliburton / Baker Hughes 的產品規格）
  - 地熱井（>300 °C）電子現況、NASA HOTTech 計畫的具體內容與經費
  - Vorago / X-REL / Cissoid 的產品溫度規格
  - 高溫壓電感測器供應商（Fuji Ceramics、Piezocryst、Kistler）的型號與規格
  - **cryo-CMOS 的功率預算數字（Google / Intel / IMEC / Delft）——這是低溫端最關鍵的缺口**
  - **稀釋冰箱各溫區冷卻功率（4 K 的 W 級、100 mK 的 µW 級）的實際數字**
  - **低溫壓電致動器商用規格（attocube、npoint、JPE）**
  - **PZT 在 4 K 的壓電係數相對室溫的下降百分比、以及 Qm 上升幅度——這是判斷低溫機會成立與否的單一最關鍵數字**
  - 石英 / LiNbO₃ / 藍寶石在低溫的 Q 值、量子聲學（Cleland / Schoelkopf 團隊）的耦合強度
- 本文件因此**在資訊密度上以「把已知的物理邏輯與已驗證的材料數字串起來」為主**，而不是提供新的市場情報。**請把它當作「下一輪研究的作戰地圖」，而不是「盡職調查結論」。**

---

## 1. 結論摘要

> 只有第 1–5 條有硬證據。第 6–8 條是本輪推論，已標明。

1. **【已查證】溫度是「主動/被動兩用」概念最直接的敵人，而且數字很難看。** Stanford 於 APEC 2024 報告：PZT 諧振器從 25 °C 升到 150 °C，**k² 下降 25%、Qm 下降 80%**［S15］。k² 掉代表電—機轉換能力掉、Qm 掉代表損耗暴增——這正好是「兩用元件」同時依賴的兩個參數。**光是 150 °C 就已經把 PZT 打殘，井下 200 °C 以上根本不用談 PZT。**
2. **【已查證】業界慣例是「最高操作溫度取居里溫度的一半」，這條慣例直接把 PZT 判出局。** PZT Tc ≈ 320–360 °C（軟式 Nb 摻雜 PZT-5A 型 360 °C、硬式 Fe 摻雜 PZT-4 型 325 °C），實用上限約 160 °C；LiNbO₃ Tc ≈ 1150 °C［S15］［03-68］。
3. **【已查證】本輪唯一橫跨兩端的硬證據：SAW 隔離閘極驅動器實測 0.5 K – 544 K。** Jin et al.（*Communications Engineering*, 2026 / arXiv 2511.13412）的微波聲學隔離閘驅，除了 0.032 pF 隔離電容、2.75 kV 耐壓、驅動 650 V/11 A GaN HEMT 導通時間 108.8 ns 之外，**明列工作溫度範圍 0.5 K – 544 K**［16-3, 16-4］。**這是「同一顆元件在液氦溫區與 271 °C 都能工作」的實測，是本 dossier 最有價值的單一事實。**
4. **【已查證】高溫壓電材料確實存在，而且卡點是「電阻率」不是「壓電性」。** Na₀.₅Bi₃(LiMn)₀.₉Ti₄₋ₓCeₓO₁₅ 系鉍層狀（BLSF）陶瓷：**d33 = 32.0 pC/N、Tc = 648 °C、500 °C 時 ρ = 1.2×10⁸ Ω·cm**［03-51］；YCOB（ReCa₄O(BO₃)₃）：**800 °C 時 ρ ≈ 2×10⁸ Ω·cm，比 langasite 高兩個數量級，且至熔點 ~1500 °C 前無相變**［03-52, 03-54］；GaPO₄ 實用上限 **<700 °C**（α→β 相變 <970 °C，Qm 因結構失序而崩壞）；langasite（LGS）可用至 **1000 °C** 但高溫電阻率不足［03-52］。
5. **【已查證】高溫端有一個元件級的實測里程碑：LiNbO₃ MEMS 共振器陣列已在空氣中 500 °C 運作。**［03-34］這證明高溫的不只是「材料樣品」，而是「有電極、有共振、可量測」的元件。
6. **【已查證，但是壞消息】高溫材料的 d 常數低到只能感測、不能致動。** BLSF 的 d33 = 32 pC/N 只有硬式 PZT 的約十分之一，YCOB 更低［03-51, 03-52］。**這代表在 >300 °C 區間，「主動/被動兩用」實際上退化成「被動共振 + 感測」，主動端（致動、升壓、產生高壓）幾乎不可用。姊妹檔 03 號 dossier 已對同一機會（其 §4.5）做出相同判斷並主動降權，本文件確認之。**
7. **【推論，非查證結果】低溫端的價值主張與高溫端在物理上是相反的：低溫下 Qm 上升（機械損耗機制凍結）而 d 常數下降。** 這意味著低溫壓電元件**天生偏向「被動」（高 Q 儲能、濾波、極穩定頻率參考）而不是「主動」（大位移致動）**——與高溫端「只能感測」的結論方向不同但同樣是單邊的。**這個推論的關鍵數字（4 K 的 d33 剩多少 %、Qm 漲多少倍）本輪完全沒查到，見 §6。**
8. **【推論】把 §1.3 的 0.5 K – 544 K 與 §1.4 的材料清單放在一起看，本領域最誠實的定位是：「不是做高溫電源轉換，而是做極端溫度下的『訊號/能量穿越隔離障壁』與『就地感測』」。** 前者（隔離供電、閘驅）已有 TRL 3–4 的實測原型；後者（高溫感測）材料已備但元件級證據薄弱。**至於「高溫致動」與「低溫功率轉換」，本輪找不到任何支撐證據。**

---

## 2. 現況：技術 / 產品 / 玩家

### 2.1 高溫端：磁性元件為什麼會死，以及死在哪一段

- **【推論／物理常識，非查證】磁性元件的高溫失效是三段式的**：(a) 磁芯損耗（core loss）隨溫度先降後升，多數鐵氧體有一個損耗最低點，超過之後損耗上升；(b) 接近居里溫度時飽和磁通密度 Bsat 快速塌陷，同一顆電感的儲能能力隨溫度縮水，必須用「冷態設計、熱態降額」的方式硬吃體積代價；(c) 過居里點則磁性完全消失，元件不再是電感。
- **【未查證假設，下一輪必查】** 我的內部印象是常見 MnZn 功率鐵氧體的居里溫度落在 200–250 °C 區間、NiZn 較高，粉末鐵芯與奈米晶帶材可再高一些。**這組數字本輪毫無來源支撐，客戶不可引用，但它決定了「磁性元件在 200 °C 以上是否真的出局」這個論述的成敗，是下一輪第一優先。**
- **【已查證】相對地，壓電側在高溫的「非磁性優勢」在核融合場合已有實測背書**：ITER 的壓電馬達輻射耐受測試顯示元件可承受 **~10¹⁹ n/cm² (E>0.1 MeV)**，並在 **330 °C / 200 °C 多次熱循環下存活**，去極化甚至可以遠端逆轉（重新極化）［15-S42］。**注意這是「存活」不是「維持性能」——需要額外的高壓再極化電路，這是系統成本。**
- **【已查證】單晶 AlN 是輻射+高溫雙抗的候選**：耐快中子 1.85×10¹⁸、熱中子 5.8×10¹⁸ n/cm²、gamma **26.8 MGy**［15-S43］。但 **k² 僅約 6%**，功率密度會大幅遜於 PZT［15-S43］。
- **【已查證】PZT 的輻射耐受則是負面的**：400 kGy（0.4 MGy）即出現約 **−25% 介電性能劣化**［15-S44］。**對「反應爐內」這個子場景，PZT 基本不合格。**

### 2.2 高溫端：材料供給狀況（本輪唯一查證充分的部分）

見 §3 表格。要點：**BLSF / YCOB / langasite / GaPO₄ / LiNbO₃ / AlN 這條「非 PZT 高溫材料鏈」是真實存在且有學術實績的**，但：

- **【已查證】它與傳統 PZT 陶瓷產線沒有共通性。** 姊妹檔 16 號 dossier 明確指出：要離開低頻 bulk-mode PT、走 MHz–GHz 的 SAW/BAW，「那是完全不同的材料與晶圓製程（LiNbO₃、AlN），**與傳統 PZT 陶瓷產線無共通性**」［16-§5.1］。**這對台灣團隊是關鍵的產能／資本判斷點：高溫路線等於做半導體級晶圓製程，不是做陶瓷燒結。**
- **【已查證】AlN/ScAlN 的優勢是沉積溫度 <400 °C、CMOS 相容**［03-37］，但這是「製造相容性」不是「工作溫度」，兩者不可混淆。
- **【未查證假設】** 高溫壓電感測器的商業供應商，我的內部印象包括 Kistler（引擎缸壓感測、自有 PiezoStar 晶體）、Piezocryst（奧地利 Graz，引擎指示感測器）、Fuji Ceramics（日本，高溫加速規）。**本輪完全未查證任何型號、溫度規格或價格，客戶不可引用。**

### 2.3 低溫端：本輪幾乎空白

- **【已查證】唯一的硬證據仍是 §1.3 的 SAW 閘驅 0.5 K 下限**［16-3, 16-4］。姊妹檔 16 號 dossier 已把「量子計算低溫控制電子」列為該機會的市場訊號之一，並指出這類市場「皆為高單價、低量、對元件成本不敏感的市場，正好避開客戶最擔心的『壓電單價貴』問題」［16-§4.2］。**這是與客戶方向限制最契合的一段既有論述。**
- **【已查證，線索級】本專案 03 號 dossier 的來源清單中有兩篇低溫聲學論文，本輪未展開，但 URL 可用**：
  - arXiv 2407.17693 — *Low Temperature Properties of Low-Loss Macroscopic Lithium Niobate Bulk Acoustic Wave Resonators*：**少量重離子雜質限制 LN BAW 性能**［03-31］。這是「低溫高 Q 不是免費的、有材料純度天花板」的直接反面證據線索。
  - arXiv 2604.13364 — *Cryogenic Loss Limits in Microwave Epitaxial AlN Acoustic Resonators*：AlN 的本質損耗極限［03-41，原檔已標【未驗證】］。
  - **這兩篇是下一輪低溫端的起點文獻。**
- **【已查證】姊妹檔 04 號 dossier 已把「低溫下壓電係數大幅下降」列為未解問題並標為未驗證**［04-§4.5 技術難點 (b)］。**本輪未能推進這一點，缺口原封不動。**
- **【未查證假設，全部不可引用】** 我的內部印象：4 K 級 cryo-CMOS 控制晶片的供電是量子運算真實的擴展瓶頸（同軸線熱負載 + 4 K 冷卻功率有限）；稀釋冰箱 4 K 級冷卻功率在瓦級、100 mK 級在數百 µW 級、20 mK 級在數十 µW 級；低溫壓電位移台（attocube、JPE、npoint、PI）已商品化且規格書會標註低溫下行程縮減；石英與藍寶石 BAW 在低溫可達極高 Q；超導量子聲學（SAW/BAW 與 qubit 耦合，Cleland 團隊、Schoelkopf 團隊的 HBAR）是活躍的研究領域。**以上每一條都沒有來源，全部列入 §6。**

---

## 3. 關鍵數字表

**表中每一列都標了證據等級。「已查證」列的來源編號對應 §7；「假設」列沒有來源，因為它們沒有來源。**

| 項目 | 數字 | 證據等級 | 來源 |
|---|---|---|---|
| **SAW 隔離閘驅工作溫度範圍** | **0.5 K – 544 K（−272.6 °C ~ +271 °C）** | 已查證 | 1, 2 |
| SAW 隔離閘驅其餘規格 | 隔離電容 **0.032 pF**、耐壓 **2.75 kV**、開路 13.4 V / 短路 44.4 mA（≈150 mW）、聲程 1.25 mm（LiNbO₃）、驅動 650 V/11 A GaN HEMT 導通 108.8 ns | 已查證 | 1, 2 |
| PZT 諧振器 25→150 °C 劣化 | **k² −25%、Qm −80%** | 已查證 | 3 |
| 居里溫度 | PZT ≈ **320 °C**（另一來源：軟式 360 °C / 硬式 325 °C）；LiNbO₃ ≈ **1150 °C** | 已查證 | 3, 4 |
| 實用溫度上限慣例 | **取 Tc 的一半**（PZT → 約 160 °C） | 已查證 | 3 |
| BLSF 高溫陶瓷 | **d33 = 32.0 pC/N、Tc = 648 °C、500 °C 時 ρ = 1.2×10⁸ Ω·cm** | 已查證 | 5 |
| YCOB | **800 °C 時 ρ ≈ 2×10⁸ Ω·cm**（比 langasite 高兩個數量級）；至熔點 **~1500 °C** 無相變 | 已查證 | 6, 7 |
| GaPO₄ | 實用上限 **<700 °C**（α→β 相變 <970 °C）；Qm 因結構失序下降 | 已查證 | 6 |
| Langasite (LGS) | 可用至 **1000 °C**，但高溫電阻率不足 | 已查證 | 6 |
| LiNbO₃ MEMS 共振器 | **空氣中 500 °C 運作**（橫向振動陣列） | 已查證 | 8 |
| 壓電陶瓷（ITER 馬達）耐輻射+熱循環 | **~10¹⁹ n/cm² (E>0.1 MeV)**；**330 °C / 200 °C 多次循環存活**；去極化可遠端逆轉 | 已查證 | 9 |
| 單晶 AlN 耐輻射 | 快中子 1.85×10¹⁸、熱中子 5.8×10¹⁸ n/cm²、gamma **26.8 MGy**；但 k² 僅 ~6% | 已查證 | 10 |
| PZT gamma 劣化 | **400 kGy → 介電性能約 −25%** | 已查證 | 11 |
| 壓電功率密度天花板 | 理論 **330 W/cm³**（應力邊界）；**實務上限 33 W/cm³**（受散熱限制） | 已查證 | 12 |
| 高振速硬牆 | 最大振速約 **1 m/s**（Penn State 高功率材料），市售 hard PZT 實用上限約 **0.1 m/s** 量級 | 已查證 | 13 |
| **以下全部為【未查證假設】，不可引用** | | | |
| MnZn 功率鐵氧體居里溫度 | 印象值 200–250 °C 區間 | **假設** | 無 |
| 井下 HPHT 溫度分級 | 印象值：標準 150 °C / HT 175 °C / ultra-HT 200 °C+ | **假設** | 無 |
| 金星表面溫度 | 印象值 ~460 °C、~92 bar | **假設** | 無 |
| 稀釋冰箱冷卻功率 | 印象值：4 K 級瓦級、100 mK 級數百 µW、20 mK 級數十 µW | **假設** | 無 |
| PZT 在 4 K 的 d33 | 印象是顯著下降（約室溫的 1/5 – 1/3 量級），Qm 顯著上升 | **假設** | 無 |

---

## 4. 「新能力型」應用機會

> 篩選原則沿用本專案共同標準：凡「更小/更薄/更便宜地取代磁性元件」一律標為**替代型**並降權。以下四項依「非替代性強度」排序，**每一項的證據等級都在標題後標明**。

### 4.1 ★★★★☆ 極端溫度下的隔離供電與閘極驅動（證據等級：已查證，TRL 3–4）

- **新能力是什麼**：在 **0.5 K 到 544 K** 的整個溫域內，用同一種物理機制提供**電氣隔離的功率與訊號傳遞**。SAW 元件已實測涵蓋此溫域［1, 2］。
- **為什麼以前做不到**：這是三個獨立的物理障礙同時存在——(a) 磁芯有居里溫度，高溫端直接失去磁性；(b) 光耦的 LED 在高溫與輻射下快速老化、在深冷下效率崩潰；(c) 電解電容與多數矽半導體在液氦溫區不工作。**沒有任何單一既有元件族群能橫跨這個溫域，這不是「做得更好」而是「原本沒有」。**
- **是否真非替代**：**是**（在溫度極端點）；但**必須誠實補一句**——在常溫常規場景，它就只是一個比較貴的隔離器，**沒有任何價值**。這個機會的全部價值都綁在「客戶的應用真的在極端溫度」這個前提上。
- **誰在做**：Jin et al.（*Communications Engineering*，2026）［1, 2］。**聲學/壓電在此領域基本無人佔位**（姊妹檔 16 號 dossier 的判斷）。
- **TRL**：**3–4**（已在 buck 轉換器中驗證，但功率僅 ~150 mW 級）。
- **市場訊號**：量子計算低溫控制電子、井下（>200 °C）、航太、核能——**皆為高單價、低量、對元件單價不敏感的市場**，正面命中客戶「不要做成本競賽」的方向限制。
- **最大技術障礙**：**功率必須從 ~150 mW 拉到 0.5–2 W** 才能驅動實用 SiC/GaN 模組；且 **PZT 的居里點根本撐不到 544 K**，必須走 LiNbO₃/AlN/langasite，**這改變整條材料與製程供應鏈**（見 §2.2）。

### 4.2 ★★★☆☆ 300–650 °C 就地感測 + 共振（證據等級：材料已查證、元件級極弱，TRL 2–3）

- **新能力是什麼**：在磁性元件（居里點）、電解電容、與矽半導體**都已出局**的溫度區間，讓同一顆元件同時做共振（頻率參考／濾波／儲能）與感測。
- **為什麼以前做不到**：**不是沒人想做，是電阻率。** 高溫下壓電體漏電，訊號被漏電流淹沒。YCOB 相對 langasite 高**兩個數量級**的電阻率（800 °C 時 2×10⁸ Ω·cm）是近年才把門檻推開的關鍵［6, 7］。
- **是否真非替代**：**是**——在該溫區沒有可替代的被動元件可言。
- **誰在做**：學界（BLSF 缺陷工程［14］、YCOB 高溫振動感測器［7］、LN MEMS 500 °C 陣列［8］）。**本輪查無商業產品。**
- **TRL**：**2–3**（材料 TRL 較高，元件級極低）。
- **最大技術障礙（致命）**：**d 常數太低。** BLSF 的 d33 = 32 pC/N 僅為硬式 PZT 的約十分之一，YCOB 更低［5, 6］。**這個機會現實上只能做「高溫感測＋共振」，做不了「高溫致動」或「高溫升壓」——也就是說，「主動/被動兩用」的主動端在這裡是不成立的。必須誠實降權。**（本判斷與姊妹檔 03 號 dossier §4.5 一致。）

### 4.3 ★★★☆☆ 低溫（4 K 及以下）的高 Q 被動元件（證據等級：**推論為主，本輪最弱**，TRL 未知）

- **新能力是什麼**：利用低溫下機械損耗機制凍結、Qm 大幅上升的特性，做出室溫不可能達到的**超高 Q 被動共振器**，同時避開磁性元件在低溫的問題。
- **為什麼以前做不到**：**這正是本輪最需要查證卻完全沒查到的部分。** 我能誠實說的只有：低溫下磁性材料的損耗行為與室溫不同、超導繞線需要額外的低溫工程、而壓電體的機械 Q 在低溫上升是聲子物理的一般性結果。**「上升多少」「相對磁性方案好多少」本輪零證據。**
- **是否真非替代**：**無法判斷。** 若它只是「在 4 K 做一顆比較好的濾波器」，那是替代型；若它能做到「室溫任何技術都達不到的 Q 值，因而解鎖新的量子/計量應用」，那才是新能力。**這個分岔的答案完全取決於下一輪要查的數字。**
- **反面線索（已查證）**：arXiv 2407.17693 指出 **少量重離子雜質即限制 LiNbO₃ BAW 在低溫的性能**［03-31］——**低溫高 Q 有材料純度天花板，不是免費的。**
- **TRL**：**無法判斷**。
- **最大技術障礙**：低溫下 d 常數下降（幅度未知），意味著要達到同樣的電—機轉換必須加大驅動電壓或元件尺寸，而低溫端**每一瓦耗散都要付出巨大的冷卻代價**——這兩者直接衝突。

### 4.4 ★★☆☆☆ 高溫致動（閥門／引擎／渦輪）（證據等級：**已被證據否定**，不建議投入）

- **新能力會是什麼**：在 300 °C 以上做直接致動（燃油噴射閥、渦輪可變幾何、高溫製程閥）。
- **為什麼列出來卻降到兩星**：**因為 §4.2 的證據直接否定它。** 高溫材料的 d33 只有 PZT 的十分之一等級，而致動應用需要的是大 d 常數；同時姊妹檔 04 號 dossier 指出壓電體在高振速下有 **~1 m/s 的硬牆**、且自發熱會構成熱正回饋（Qm 下降→更熱→Qm 更低），文獻直接用「prone to self-heating and thermal run-away」描述［13, 15］。**在已經 300 °C 的環境裡做高功率致動，等於在熱失控的起跑點上開跑。**
- **是否真非替代**：概念上是（沒有其他致動技術能在該溫度做微米級精密致動），**但材料不支持，所以現階段是空頭支票**。
- **誠實評註**：**我把它列出來只是為了明確地叫客戶不要做。** 若下一輪查證發現有 d33 > 200 pC/N 且 Tc > 600 °C 的材料存在，本項才需重新評估。

---

## 5. 反面證據、失敗案例與物理上限

1. **【已查證，最致命】150 °C 就已經把 PZT 打殘。** k² −25%、Qm −80%［3］。任何「高溫壓電」的論述若建立在 PZT 上，在 200 °C 井下環境是**根本不成立**的。整條路線被迫轉向 LiNbO₃/AlN/BLSF/YCOB，而這意味著**放棄整個成熟的 PZT 陶瓷供應鏈與成本結構**。
2. **【已查證】高溫材料的 d 常數低一個數量級，「兩用」的主動端在高溫直接消失。** BLSF d33 = 32 pC/N vs 硬式 PZT 的十倍量級［5］。**客戶要的是「主動/被動兩用」，但高溫端只給得起被動+感測。這是對本 dossier 主張最直接的反證。**
3. **【已查證】熱失控是自我強化的。** 壓電陶瓷在高振速下 Qm 隨振幅急遽衰減，損耗轉成內熱、溫升再降 Qm［15］。Uchino 指出超過臨界振速後壓電體「drastically increases the heat generation and becomes a ceramic heater」［13］。**在高溫環境中，環境溫度已經吃掉了大部分熱裕度，這個正回饋的起跑點被大幅前移。**
4. **【已查證】散熱是功率密度的真正上限，而高溫環境沒有散熱。** 壓電功率密度理論 330 W/cm³，**實務上限 33 W/cm³，且該上限由散熱結構決定**［12］。井下、渦輪內、金星表面**都沒有低溫熱沉可用**，這個 10× 的降額在極端高溫環境可能還要再降。
5. **【已查證】低溫高 Q 有材料純度天花板。** 少量重離子雜質即限制 LiNbO₃ BAW 的低溫性能［03-31］。**這代表 §4.3 的機會可能受限於晶圓級材料純度，而不是設計。**
6. **【已查證】PZT 在輻射環境不合格。** 400 kGy 即 −25% 介電劣化［11］；ITER 的壓電馬達雖能存活 ~10¹⁹ n/cm²，但**依賴「遠端重新極化」這個運維動作**［9］——對埋在井下或探測器內十年不能碰的元件不適用。
7. **【已查證，產業史級警訊】壓電變壓器產業已經崩潰過一次。** 1980 年代末日本廠商推動 PT 用於 CCFL 背光，2000 年代末 LCD 轉向 LED，高壓 PT 銷售崩跌，**多數主要供應商停止高量生產**［16］。**供應鏈與量產經驗已經流失一次，重建成本必須計入任何商業模型。**
8. **【已查證，方法學警訊】穿壁/極端環境的聲學技術近 30 年未商品化。** 姊妹檔 16 號 dossier 的結論值得原文照抄：技術可行 ≠ 市場可行。**極端溫度市場的認證期同樣極長（電網級 5–10 年、核能與船級社的合格化成本可能遠高於研發成本）。**
9. **【誠實的方法論反證】本 dossier 本身就是一個反面證據。** 我沒有找到任何一家公司在賣「高溫壓電主被動兩用元件」或「低溫壓電功率元件」。**在 §2 的所有玩家欄位裡，商業產品欄都是空的。** 一個技術若在 30 年後仍只有學術論文，預設假設應該是「有某個未被寫出來的障礙」，而不是「市場還沒發現」。

---

## 6. 未解問題（給下一輪研究）

**本輪因搜尋額度耗盡，缺口極大。以下按優先順序排列，並直接附上建議的搜尋字串。**

**P0 — 決定低溫機會生死的單一數字：**
1. **PZT / LiNbO₃ / AlN 在 4 K 的壓電係數相對室溫剩多少 %，Qm 上升幾倍？**
   建議查詢：`piezoelectric coefficient d33 temperature dependence 4K cryogenic PZT percentage` ／ `PZT actuator stroke reduction at 4 K cryogenic` ／ `mechanical quality factor Qm cryogenic temperature piezoelectric increase`
2. **cryo-CMOS 的實際功率預算是多少？4 K 冷卻功率是多少瓦？**
   建議查詢：`cryo-CMOS power budget 4K quantum computing watts` ／ `Intel Horse Ridge II power consumption cryogenic controller` ／ `dilution refrigerator cooling power 4K 100mK 20mK specifications Bluefors` ／ `coaxial cable heat load per line dilution refrigerator milliwatts`

**P1 — 決定高溫機會市場規模的數字：**
3. **井下電子的實際溫度分級、失效率統計與市場規模。**
   建議查詢：`HPHT downhole tool temperature rating 175C 200C classification` ／ `downhole electronics failure rate high temperature statistics` ／ `Halliburton Quasar ultra-high temperature LWD specification` ／ `geothermal logging tool 300C electronics`
4. **高溫電子的既有解（SiC/GaN/SOI）到底能到幾度、賣多少錢？**
   建議查詢：`Cissoid high temperature SOI 225C product` ／ `X-REL Semiconductor high temperature IC 300C` ／ `Vorago high temperature microcontroller specification` ／ `NASA Glenn SiC integrated circuit 500C hours operation`
5. **磁性元件的高溫真實上限（本輪最大的邏輯缺口）。**
   建議查詢：`MnZn ferrite Curie temperature power core loss vs temperature` ／ `high temperature inductor 250C magnetic core options` ／ `nanocrystalline core high temperature limit`

**P2 — 決定「誰已經佔位」的商業情報：**
6. **高溫壓電感測器的商業供應商與型號。**
   建議查詢：`Kistler high temperature pressure sensor engine indicating PiezoStar 350C` ／ `Piezocryst cylinder pressure sensor specification` ／ `Fuji Ceramics high temperature accelerometer 500C`
7. **低溫壓電致動器的商業規格（含低溫行程衰減的官方數字）。**
   建議查詢：`attocube ANPz cryogenic positioner specification 4K stroke` ／ `JPE cryo positioning specification 4K` ／ `npoint cryogenic piezo stage`
8. **量子聲學是否構成新能力（本輪完全未觸及）。**
   建議查詢：`Cleland phonon qubit surface acoustic wave superconducting qubit coupling` ／ `HBAR bulk acoustic wave qubit Schoelkopf Chu` ／ `quartz BAW resonator cryogenic quality factor 10^10 Tobar`

**P3 — 反面證據補強：**
9. `high temperature piezoelectric sensor limitations problems commercial failure` ／ `why high temperature piezoelectric not commercialized` ／ `cryogenic piezoelectric transformer research limitations`

---

## 7. 來源清單

**重要聲明：以下所有 URL **均轉引自本專案同 repo 的姊妹 dossier**（由前面幾個子任務用真實 WebSearch 取得），我在本輪**未再獨立開啟或核對**任何一條。本輪我自己執行的 WebSearch 次數為 0。**

| # | 標題 | URL | 說明 | 轉引自 |
|---|---|---|---|---|
| 1 | Microwave-acoustic-based isolated gate driver for power electronics (arXiv preprint) | https://arxiv.org/pdf/2511.13412 | ★ **本 dossier 最重要來源**：SAW 隔離閘驅 0.032 pF / 2.75 kV / **0.5 K – 544 K**；聲程 1.25 mm LiNbO₃；驅動 650 V/11 A GaN HEMT 導通 108.8 ns；並直述傳統 PT 因 Qm≈1000、頻寬僅數十 kHz 而不適用 WBG | 16, 03 |
| 2 | Microwave-acoustic-based isolated gate driver for power electronics, *Communications Engineering* | https://www.nature.com/articles/s44172-026-00681-w | 同上之正式期刊版本 | 16 |
| 3 | Piezoelectric resonators in DC-DC converters: current status and limits | https://www.powerelectronicsnews.com/piezoelectric-resonators-in-dc-dc-converters-current-status-and-limits/ | ★ **關鍵溫度數字來源**：Stanford APEC 2024 的 25→150 °C 造成 k² −25% / Qm −80%；PZT Tc≈320 °C、LN Tc≈1150 °C；「實用上限取半個 Tc」的業界慣例 | 04 (S15) |
| 3a | Nonlinear Losses and Material Limits of Piezoelectric Resonators for DC-DC Converters | https://www.researchgate.net/publication/380310755_Nonlinear_Losses_and_Material_Limits_of_Piezoelectric_Resonators_for_DC-DC_Converters | 來源 3 所引用的原始研究（姊妹檔標註「未能開啟核對」） | 04 (S15a) |
| 4 | Base Metal Co-Fired Multilayer Piezoelectrics（綜述） | https://www.researchgate.net/publication/296625421_Base_Metal_Co-Fired_Multilayer_Piezoelectrics | 軟式 PZT-5A 型 Tc = 360 °C、硬式 PZT-4 型 Tc = 325 °C | 03 (68) |
| 5 | Simultaneously Achieved High Piezoelectricity and High Resistivity in Na₀.₅Bi₄.₅Ti₄O₁₅-Based Ceramics with High Curie Temperature (PMC11642524) | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11642524/ | ★ BLSF：d33 = 32.0 pC/N、Tc = 648 °C、500 °C 時 ρ = 1.2×10⁸ Ω·cm | 03 (51) |
| 6 | High-Temperature Piezoelectric Sensing (PMC3926551) | https://pmc.ncbi.nlm.nih.gov/articles/PMC3926551/ | ★ **高溫材料的主參考**：GaPO₄ <700 °C、langasite 至 1000 °C、YCOB 800 °C 時 ρ ≈ 2×10⁸ Ω·cm 且至 ~1500 °C 無相變 | 03 (52) |
| 7 | Design, fabrication and characterization of high temperature piezoelectric vibration sensor using YCOB crystals (Sensors & Actuators A) | https://www.sciencedirect.com/science/article/abs/pii/S0924424712000891 | YCOB 高溫振動感測器的實作級證據 | 03 (54) |
| 8 | A Laterally Vibrating Lithium Niobate MEMS Resonator Array Operating at 500 °C in Air (PMC7795216) | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7795216/ | ★ LN MEMS 共振器陣列在空氣中 500 °C 運作——高溫端唯一的元件級里程碑 | 03 (34) |
| 9 | Radiation tolerance testing of piezoelectric motors for ITER (first results), *Fusion Eng. Des.* | https://www.sciencedirect.com/science/article/abs/pii/S0920379622000175 | ★ ~10¹⁹ n/cm² (E>0.1 MeV)；**330 °C / 200 °C 多次熱循環存活**；去極化可遠端逆轉 | 15 (S42) |
| 10 | Radiation tolerance of piezoelectric bulk single-crystal aluminum nitride (PubMed 24960710) | https://pubmed.ncbi.nlm.nih.gov/24960710/ | 單晶 AlN 耐快中子 1.85×10¹⁸、熱中子 5.8×10¹⁸ n/cm²、gamma 26.8 MGy；k² 僅 ~6% | 15 (S43) |
| 11 | Effects and mechanisms of gamma irradiation on electrical properties of PZT-S and PZT-N (*Ceramics International*) | https://www.sciencedirect.com/science/article/abs/pii/S0272884226034942 | 400 kGy → PZT 介電性能約 −25% | 15 (S44) |
| 12 | Power density of piezoelectric transformers improved using a contact heat transfer structure (PubMed 22293737) | https://pubmed.ncbi.nlm.nih.gov/22293737/ | ★ 理論功率密度 330 W/cm³、實務上限 33 W/cm³，且上限由散熱結構決定 | 15 (S41) |
| 13 | High-Power Piezo Characterization System (HiPoCS) / Uchino 高功率壓電研究 | https://www.researchgate.net/publication/343781169_High-Power_Piezo_Characterization_System | 最大振速 ~1 m/s 硬牆；超過後「becomes a ceramic heater」；Penn State 高功率材料 | 04 (S8/S10) |
| 14 | Synergy ascension of piezoresponse and Curie temperature in bismuth-layered ceramics via defect engineering (*Acta Materialia*) | https://www.sciencedirect.com/science/article/abs/pii/S1359645425003970 | BLSF 缺陷工程——同時提升壓電響應與居里溫度的材料路線 | 03 (55) |
| 15 | Characterization of high-power mechanical quality factor of piezoelectric ceramic discs under self-heating condition | https://www.sciencedirect.com/science/article/pii/S2238785423003836 | Qm 隨振幅急遽衰減；自發熱條件下 Qm 明顯低於 burst 法量值——熱正回饋的直接證據 | 04 (S4) |
| 16 | Piezoelectric Transformers: An Historical Review (*Actuators*, MDPI 2016) | https://www.mdpi.com/2076-0825/5/2/12 | ★ CCFL→LED 轉換導致高壓 PT 產業崩潰、多數供應商停產的商業失敗史 | 16 (45), 04 (S27) |
| 17 | Low Temperature Properties of Low-Loss Macroscopic Lithium Niobate Bulk Acoustic Wave Resonators (arXiv 2407.17693) | https://arxiv.org/html/2407.17693 | ★ **低溫端唯一的實質線索**：少量重離子雜質即限制 LN BAW 的低溫性能 | 03 (31) |
| 18 | Cryogenic Loss Limits in Microwave Epitaxial AlN Acoustic Resonators (arXiv 2604.13364) | https://arxiv.org/pdf/2604.13364 | AlN 的低溫本質損耗極限（姊妹檔原已標【未驗證】，**日期看似 2026 年，需確認真實性**） | 03 (41) |
| 19 | Ultra-high temperature piezoelectric crystals: Properties, structures and applications (*Prog. Mater. Sci.*) | https://www.sciencedirect.com/science/article/abs/pii/S0079642525001343 | 超高溫壓電晶體綜述——下一輪高溫材料研究的主要入口 | 03 (53) |
| 20 | How do electronics react to magnetic fields? (ITER) | https://www.iter.org/node/20687/how-do-electronics-react-magnetic-fields | ITER port cell ~200 mT；托卡馬克廠房 I&C 機櫃 2.5–20 mT（高溫+強磁+輻射複合環境的背景） | 15 (S12) |

**沒有來源的內容一覽（誠實列出，供稽核）**：§2.1 磁性元件三段式失效機制的定性描述、§2.1 MnZn 鐵氧體居里溫度、§2.2 高溫感測器供應商（Kistler / Piezocryst / Fuji Ceramics）、§2.3 全部低溫端的假設（cryo-CMOS 功率預算、稀釋冰箱冷卻功率、低溫致動器廠商、石英/藍寶石低溫 Q、量子聲學）、§3 表格下半部所有標【假設】的列、§4.3 的低溫 Qm 上升與 d 常數下降的方向性判斷。**以上皆為模型內部知識，本輪零查證，客戶不得引用。**
