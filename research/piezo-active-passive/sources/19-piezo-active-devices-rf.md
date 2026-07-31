# 應用B5：壓電當「主動元件」——piezotronics、PET 邏輯、壓電 NEMS 開關、共振體電晶體、聲波訊號處理

> **一句話結論：「讓壓電體自己變成電晶體」這條路（piezotronics、IBM PET）已被實證為死路——IBM 自己在歐盟 PETMEM 專案中把目標從邏輯改成 RF 開關，這是官方等級的認輸；但同一棵樹上有三條在 2022–2026 年被實驗證實、且「以前真的做不到」的支線：(1) 聲電放大器（acoustoelectric amplifier）在單一壓電元件中同時做出濾波＋增益＋非互易隔離（Sandia，1 GHz 淨 RF 增益 +11.3 dB、聲學雜訊指數 2.8 dB）；(2) 鐵電 AlScN 的「週期性極化」把 BAW 濾波器推上 19 GHz（插入損耗 1.3 dB，且已在商用 XBAW 產線做出）；(3) 壓電 NEM 繼電器把機械開關的驅動電壓從 60 V（Menlo Micro 靜電式）降到 520 mV 甚至 20 mV。這三條的共同點是：壓電不是去取代電晶體，而是提供電子電路沒有的自由度——聲子與載子的動量交換、非揮發的極性、以及線性無 pull-in 的機械力。**

---

## 0. 研究方法與限制（誠實揭露）

1. **本回合實際成功執行 WebSearch 共 28 次**（前一版為 0 次，本文件已完整重寫覆蓋）。第 29、30 次查詢回傳 `this session has used its web search budget (200 of 200 WebSearch calls)`，之後即停止查詢。任務書所述「額度放寬至 3000」在本 session 未生效，實際上限仍為 200 且由本 session 多個 agent 共用。
2. **WebFetch / curl 依環境限制全面 403，本回合完全未使用。** 因此**所有事實均來自搜尋引擎回傳的摘要與標題，沒有任何一篇論文全文被實際讀取**。凡是數值型事實，我一律標註來源編號；凡摘要與摘要之間有出入者，我明確指出出入。
3. **標籤定義**：
   - **【已驗證】** — 本回合搜尋結果直接顯示該事實，且有對應 URL。
   - **【摘要級】** — 搜尋摘要陳述之，但未見原文，數值可能被摘要引擎改寫。**這是本文件絕大多數數字的等級。**
   - **【推算】** — 由公開物理公式與明示假設自行計算，讀者可複核。
   - **【查無】** — 本回合查證失敗或預算用盡，不猜。
4. **本回合預算用盡而未能查證的清單（下一輪必查）**：
   - 鐵電記憶體對照組：Ferroelectric Memory Company（FMC）融資、GlobalFoundries 22FDX FeFET 量產狀態、SK Hynix / Micron / TSMC 投入 → **全部【查無】**。
   - 負電容 FET（NC-FET）現況與爭議 → **【查無】**，本文件不對其下任何判斷。
   - Zhong Lin Wang 的引用數具體數字 → **【查無】**，本文件不引用任何引用數。
   - Intel 22FDX/22FFL 上的 ScAlN 共振器 → **搜尋執行了但無任何命中，判定為【查無】**（任務書假設可能有誤，或屬非公開）。
   - 壓電光機量子轉換器（微波↔光）、QphoX 等新創 → 本回合**未查**（預算分配給更接近商業的題目）。
   - 專利 **US12525955** → **【查無】**，見 §2.5。
5. **本文件不出現任何未經本回合查證的專利號、公司名或數字。** 前一版中所有【M-低】臆測已全數刪除或改為已驗證版本。

---

## 1. 結論摘要

1. **【已驗證】IBM 的 PET 邏輯不是「悄悄沒下文」，是有明確轉向紀錄的失敗案例。** 歐盟 H2020 專案 **PETMEM（Project ID 688282，2015–2018，IBM Zurich 參與）** 原目標是「比 CMOS 低一個數量級電壓、10 GHz、功耗降兩個數量級」的壓電傳導記憶體；但專案摘要明載：**指導委員會結論為「PETMEM 最早的採用機會將是 RF 開關應用，記憶體應用則是長期目標」**［S8］。**一個以取代 CMOS 為目標的專案，最後把最佳出路訂為 RF 開關——這就是本題最重要的一句反面證據。**

2. **【已驗證】PET 確實做出過實體元件，宣稱值與實測值的落差是教科書級案例。** IBM 宣稱 PET 可用**現行 Si 電晶體 1/50 的功耗**執行傳統邏輯［S5, S6］；材料為 **PMN-PT（弛豫型壓電體）推壓 SmSe（稀土單硫族化物，具壓力誘發的等結構連續金屬–絕緣體轉變）**［S3, S4］。2015 年兩篇論文分別是 *Nano Letters* 15(4), 2391–2395（"Pathway to the Piezoelectronic Transduction Logic Device"）與 *Nanotechnology* 26(37), 375201（"First realization of the piezoelectronic stress-based transduction device"）［S1–S5］。**但公開摘要只宣稱「顯示了 on/off 切換與循環」，我在本回合未找到任何功能性邏輯閘、環形振盪器或 fan-out 驗證的證據。多 GHz 速度全部標明為「as predicted by modeling」。**

3. **【已驗證＋推算】壓電 NEM 繼電器的驅動電壓優勢是真的，而且幅度是 100 倍。** 商業標竿 **Menlo Micro MM5130（靜電式）需要 >60 V 閘極驅動電壓（電流 <10 nA）**［S12, S13］；學術界的**壓電 NEM 繼電器使用 10 nm 超薄 c 軸配向 AlN 膜，致動電壓約 520 mV，加基板偏壓後可低至 20 mV**［S15］。**這是「以前做不到」的具體例證：靜電式因 pull-in 不穩定與 1/g² 的力學關係，無法在邏輯電壓域工作；壓電式可以。**

4. **【已驗證】但 Menlo Micro 同時證明了「價值不在致動器」。** MM5130 規格：DC–18 GHz（super-port 模式延伸至 26 GHz）SP4T、**插入損耗 0.4 dB @6 GHz、隔離 25 dB @6 GHz（super-port 45 dB）、IIP3 95 dBm、25 W CW / 150 W 脈衝、>30 億次切換循環、2.5×2.5 mm WLCSP**［S12, S13］。融資：**2016 年由 GE Ventures／Microsemi／Corning 以 1,870 萬美元分拆自 GE Global Research；C 輪 1.5 億美元由 Vertical Venture Partners 與 Tony Fadell 的 Future Shape 領投，累計募資逾 2.25 億美元**［S14］。**它用的是靜電＋專有金屬合金＋玻璃基板，不是壓電。客戶若以壓電材料為核心能力，在這條路上握有的是價值較低的一半。**

5. **【已驗證】本題最強的「真新能力」是聲電放大器（acoustoelectric amplifier）——它在單一壓電元件中同時提供濾波、增益與非互易隔離。** Sandia 國家實驗室的三層異質結構（**In₀.₅₃Ga₀.₄₇As 半導體膜 / LiNbO₃ 壓電膜 / Si 基板**）在 1 GHz 連續操作下達成 **28.0 dB 聲學增益（淨 RF 增益 4.0 dB）、聲學雜訊指數 2.8 dB、消耗 40.5 mW 直流功率**；另一組達 **37.0 dB 聲學增益（淨增益 11.3 dB）、19.6 mW**［S25］。發表於 *Nature Electronics*（2022/2023）。**這不是替代品：目前產業做法是把壓電濾波器、半導體放大器、旋磁非互易元件三顆分開共封裝，聲電放大器把三者合一。**

6. **【已驗證】鐵電 AlScN 的「週期性極化（P3F）」已把 BAW 濾波器推進到 19 GHz，且是在商用產線做出的。** 19 GHz 週期性極化 AlScN BAW 共振器**已在商用 XBAW 製程中製作**［S22］；以其構成的單端轉平衡梯–格型濾波器實測 **最小插入損耗 1.3–1.58 dB、3 dB 分數頻寬 5.11–6.26%、帶外抑制 30–33 dB**［S21］。物理理由明確：均勻極化的壓電膜在超過約 8 GHz 後厚度太薄、效能崩壞，週期性極化多層結構讓它以泛音模態工作［S21, S23］。**這是本文件中 TRL 最高、最接近錢、且確實「以前做不到」的一項。**

7. **【已驗證】「零靜態功耗喚醒」科學上早就成立，商業上走了九年還在出樣品。** Rinaldi 團隊的**電漿子增強微機械光開關**發表於 *Nature Nanotechnology*（2017）［S27］；DARPA N-ZERO 官方新聞同年發布［S26］。衍生新創 **Zepsor Technologies（2021 年成立於 Northeastern SMART Center）累計僅募得約 120 萬美元創投資金，外加 DARPA SBIR Phase II 180 萬美元、NSF Phase I 27.5 萬美元（2024/1/15）、ARPA-E 氫洩漏偵測案（2025/4）；2025 年 CES 展出，並「計畫在未來 12 個月內出貨樣品給潛在客戶」**［S28, S29］。**九年、總資金約 3–4 百萬美元量級、尚未量產——這是對「DARPA 投錢＝好生意」的最直接反證。**

8. **【已驗證】共振體電晶體（RBT）在先進節點是真的，但 Q 值低到必須誠實面對。** Weinstein & Bhave, *Nano Letters* 10(4), 1234–1237 (2010) 提出把感測 FET 直接嵌入共振體［S16］；Bahr/Marathe/Weinstein 於 *JMEMS*（2015）以聲子晶體在 **IBM 32 nm SOI** 中做出免釋放共振器［S18］；2021 年 Anderson/He/Bahr/Weinstein 在 **14 nm FinFET** 中做出 X 波段 Fin-RBT，**最佳 Q 由 115 提升至 181、幅值由 0.8 µS 提升至 4.5 µS（靠把 Mx/Cx 金屬層納入聲波導）**［S19］。**Q≈181 相對於獨立 BAW 濾波器的 Q（數百至數千）仍差一個數量級以上——「零額外光罩」是它唯一的賣點，效能不是。**

---

## 2. 現況／查證結果

### 2.1 Piezotronics（Zhong Lin Wang）：定位是感測器，不是邏輯

- **【已驗證】原理**：壓電位（piezopotential）調變金屬–半導體蕭特基能障高度，而非通道反轉層。Wang 於 **2007 年**提出壓電電子學效應［S1］。代表作包括 *Nano Letters* "Piezoelectric-Potential-Controlled Polarity-Reversible Schottky Diodes and Switches of ZnO Wires"（DOI 10.1021/nl802497e）［S2］、*ACS Nano* "Strain-Gated Piezotronic Transistors Based on Vertical Zinc Oxide Nanowires"（DOI 10.1021/nn301277m）［S1a］。
- **【已驗證】確實做出過「邏輯」**：*ACS Nano* "GaN Nanobelt-Based Strain-Gated Piezotronic Logic Devices and Computation"（DOI 10.1021/nn4026788）［S1b］。**但這是以應變為輸入的邏輯，輸出是電流；輸入與輸出物理量不同，無法級聯（cascade），這在架構上就決定它不可能成為通用邏輯家族。**（此判斷為【推算／架構分析】，非文獻直述。）
- **【已驗證】爭議是真實存在的方法學爭議，不是網路傳言**：Alexe 等人的 *"Energy Harvesting Using Nanowires?"* 引發 Wang 團隊的正式 Correspondence 反駁，反駁論點為「Alexe 的 AFM 量測系統被巨大的系統假影主導，雜訊等於或高於奈米線的壓電訊號」；Alexe 方的核心證據則是「從 Si 奈米線（非壓電）也量到與 ZnO 相同的放電峰」［S2a］。另有 arXiv:1910.01187 *"Toward Quantitative Measurements of Piezoelectricity in III-N Semiconductors Nanowires"*，顯示到 2019 年**該領域的定量量測仍是未解問題**［S2b］。
- **商品化**：**【查無】任何在售的 piezotronic 電晶體產品。**
- **仍在發展的旁支【已驗證】**：arXiv:2203.16416 *"STeP-CiM: Strain-enabled Ternary Precision Computation-in-Memory based on Non-Volatile 2D Piezoelectric Transistors"*［S30］——把壓電應變閘控用於記憶體內運算而非通用邏輯，這是比較誠實的定位。

### 2.2 IBM PET：完整的失敗軌跡已可還原

| 年份 | 事件 | 來源 |
|---|---|---|
| 2012 | *MRS Bulletin* 提出概念：nanoactuator-based post-CMOS digital switch | ［S7］ |
| 2013 | US20130009668「4-terminal PET」專利申請公開 | ［S9］ |
| 2015 | *Nano Letters* 15(4) 2391–2395「Pathway to the PET Logic Device」（arXiv:1503.07467） | ［S3, S4］ |
| 2015 | *Nanotechnology* 26(37) 375201「First realization…」：首個單片整合 PET，宣稱 1/50 功耗 | ［S5, S6］ |
| 2015 | *Appl. Phys. Lett.* 107, 073505「…for VLSI, low voltage sensor computation, and RF applications」——**標題已出現 RF** | ［S5a］ |
| 2015–2018 | 歐盟 H2020 **PETMEM**（ID 688282），目標壓電傳導記憶體 | ［S8］ |
| （專案期間） | **指導委員會結論：最早採用機會在 RF 開關，記憶體為長期目標** | ［S8］ |
| 2019 | E-MRS 春季會議 PETMEM Workshop | ［S8a］ |
| 2019 後 | **【查無】新的 PET 邏輯論文或 IBM 官方說明** | — |

- **【已驗證】專利族**：US9425381、US9466781、US9590167（多層堆疊壓電層之低電壓電晶體與邏輯元件）、US9444029（共平面 common/gate 電極）、US9058868（壓電傳導記憶體）［S3a, S6a］。
- **【已驗證】微縮困境是公開承認的**：搜尋摘要明載關鍵挑戰為「元件必須微縮才能達到低功耗，而在小尺寸下維持材料效能是有問題的」［S6］。
- **【推算】為何微縮必然失敗**：壓電位移 = d₃₃ × V。取 PMN-PT 的高階 d₃₃ = 2,000 pm/V、操作電壓 0.1 V，位移僅 **0.2 nm**；若如宣稱降到更低電壓或用薄膜（薄膜 d₃₃ 因基板箝制通常掉到塊材的 1/3–1/10），位移進入**皮米級**。要用皮米級位移在 SmSe 中觸發 GPa 級應力，機械系統必須極度剛硬且零間隙——這在製造公差上不可行。**這條算式可獨立複核，是我判斷 PET 不可能微縮的核心依據。**

### 2.3 MEMS／NEMS 開關：靜電式贏了市場，壓電式贏了物理

| 指標 | Menlo Micro MM5130（靜電式，商用）［S12,S13］ | 壓電 AlN NEM 繼電器（學術）［S15］ |
|---|---|---|
| 致動電壓 | **>60 V**（閘極驅動；電流 <10 nA） | **~520 mV**，加體偏壓可至 **20 mV** |
| 頻率 | DC–18 GHz（super-port 至 26 GHz） | 【查無】（多為 DC 邏輯繼電器研究） |
| 插入損耗 | 0.4 dB @6 GHz | 【查無】 |
| 隔離度 | 25 dB @6 GHz / 45 dB super-port | 【查無】 |
| 線性度 | IIP3 95 dBm | 【查無】 |
| 功率 | 25 W CW / 150 W 脈衝 | 【查無】 |
| 壽命 | **>3×10⁹ 次切換** | 【摘要級】<1 V 切換時可望超過 10⁹ 次；10 V 時降至 <10⁸ 次［S15a］ |
| 封裝 | 2.5×2.5 mm WLCSP | 實驗室級 |

- **【摘要級】對照基準**：一般電容式 RF MEMS 開關壽命僅 **3×10⁶–10⁷ 次**［S15a］。Menlo 的 3×10⁹ 次因此是**冶金學上的成就，不是致動器的成就**。
- **【已驗證】一個關鍵的反諷**：連 DARPA N-ZERO 的 RF 喚醒接收器用的都是**靜電式 AlN RF MEMS 開關**（"Design and Fabrication of an Electrostatic AlN RF MEMS Switch for Near-Zero Power RF Wake-Up Receivers"）［S26a］——AlN 在那裡是結構材料，不是致動材料。
- **【已驗證】壓電繼電器做邏輯的學術嘗試存在**："Body-Biased Complementary Logic Implemented Using AlN Piezoelectric MEMS Switches"［S15b］。**作者與單位本回合未驗證。**

### 2.4 共振體電晶體與免釋放共振器：CMOS 相容性最好，效能最差

- **【已驗證】** RBT 原始概念：把感測電晶體直接嵌入共振體，結合 FET 感測與內部介電傳導條形共振器的高 Q 與頻率縮放能力，目標 >10 GHz，可整合進標準 CMOS［S16, S17］。
- **【已驗證】** 聲子晶體（PnC）是關鍵：Bahr–Marathe–Weinstein 的 *JMEMS*（2015）確立「免釋放 CMOS-MEMS RBT 的聲子晶體理論與設計」，實作於 **IBM 32 nm SOI**［S18］。**任務書假設的 GlobalFoundries 22FDX 在本回合搜尋中未被證實——該搜尋明確回報「未找到 Weinstein 使用 22FDX 的免釋放共振器工作」，判定為【查無】。**
- **【已驗證】** 14 nm FinFET 上的 X 波段 Fin-RBT（arXiv:2107.00608）：16 種元件變體、30 個偏壓點；**限制因素是 BEOL 聲學侷限**；納入 Mx/Cx 金屬層的聲波導使**平均 Q 與峰值幅度提升 2.2 倍，最大 Q 由 115 → 181，最大幅值 0.8 µS → 4.5 µS**［S19］。另有「32 GHz resonant-fin transistors in 14nm FinFET technology」［S19a］。
- **【已驗證】另一條免釋放路線（與鐵電交會）**：*Microsystems & Nanoengineering*（2019）"A tunable ferroelectric based unreleased RF resonator"（arXiv:1905.05903）——**以鐵電電容（FeCAP）為傳導元件，整合於 TI 130 nm FeRAM 製程，無任何後製程或釋放步驟**［S20］。**這篇是本文件中「主動（鐵電非揮發）＋被動（RF 共振）同體」概念最直接的既有實證，且是在真實商用製程上。**

### 2.5 鐵電 AlScN：本題資訊密度最高、最接近錢的一段

**材料基本參數【已驗證】**（Fichtner et al., *J. Appl. Phys.* 125, 114103, 2019）［S23］：
- 矯頑場 **Ec = 2–5 MV/cm**，且可藉 Sc 含量與應變**調整超過 3 MV/cm**；
- 剩餘極化 **Pr = 70–110 µC/cm²**，可超過 100 µC/cm²，遲滯迴線近乎理想方形；
- 機制：Al₁₋ₓScₓN 隨 Sc 含量與拉伸應變，由纖鋅礦連續畸變趨向層狀六方結構。

**耐久性【已驗證】**（*Nature Communications*, 2025, s41467-025-68221-2）［S24］：
- **45 nm 厚 Al₀.₆₄Sc₀.₃₆N 電容**：完整極化反轉可撐 **~10⁸ 次**；**採用部分極化切換（partial switching）可延伸至 >10¹⁰ 次**，且保有可觀極化量；縮小電容直徑可提高崩潰電壓、進而提高耐久性。作者稱較先前纖鋅礦鐵電基準**提升千倍**。
- **對照**：早期研究耐久僅 **~3,700 次**，保持時間 9.5×10⁵ s［S24a］。**這是三年內三個數量級以上的進步速度，值得客戶列為觀察指標。**
- **失效機制【已驗證】**：*Nano Letters* "Role of Defects in the Breakdown Phenomenon of Al₁₋ₓScₓN: From Ferroelectric to Filamentary Resistive Switching"［S24b］——**AlScN 的崩潰會從鐵電行為退化為絲狀電阻切換，這是漏電/缺陷主導的硬上限。**
- **低電壓化【已驗證】**：arXiv:2207.01858「Ultrathin AlScN for low-voltage driven ferroelectric-based devices」；arXiv:2304.02909「In-Grain Ferroelectric Switching in Sub-5 nm Thin AlScN Films at 1 V」［S23a, S23b］。
- **Penn（Olsson / Jariwala）【已驗證】**：*APL* 128, 022903「Temperature-dependent wake-up phenomena in AlScN ferrodiode memory devices」——鐵電二極體以極化相依導通區分記憶狀態，偏壓 <10 V［S24c］；另 *APL* 123, 122901「Metal-ferroelectric AlScN-semiconductor memory devices on SiC wafers」［S24d］。

**可切換／可重構聲波元件【已驗證】**：
- *phys. status solidi RRL*（2021, 10.1002/pssr.202100034）："Ferroelectric AlScN Thin Film Bulk Acoustic Resonators with Polarization-Dependent Operating States"：**Mo/AlScN/Mo，Sc≈30%，厚度模態 3.17 GHz，Q = 572，kt²_eff = 11.4%**；極化由 N-polar 切換至 metal-polar 時 FBAR 頻率響應改變［S31］。
- IEEE（文件編號 11235225）："Reconfigurable FBAR Enabled by AlScN Ferroelectric Film Switching"：以**短梯形脈衝**達成近 100% 鐵電切換（單次脈衝週期），**共振頻率可在 5.7 GHz 與 14.2 GHz 之間重構**［S32］。
- "Intrinsically Switchable GHz Ferroelectric ScAlN SAW Resonators"［S32a］。
- **週期性極化（P3F，已達商用製程）**：*Microsystems & Nanoengineering*（2024, s41378-024-00857-4）「Periodically poled AlScN BAW resonators and filters for communications in the 6G era」［S23c］；IEEE 10632112（2024）：**19 GHz 週期性極化 AlScN BAW 共振器，於商用 XBAW 製程製作，三層極化由「兩層 as-grown ＋ 一層電性極化」組合而成**［S22］；arXiv:2606.00064：19 GHz 單端轉平衡梯–格型濾波器，**IL 1.3–1.58 dB、3 dB FBW 5.11–6.26%、帶外抑制 30–33 dB**［S21］。

**專利查證結果**：
- **US12476613【已驗證存在，權利人已確認】**：標題 "Filter circuitry using ferroelectric tunable acoustic resonator"，**受讓人 Qorvo US, Inc.**，發明人 **Jaroslaw Niewczas、Michael McLaughlin、Ciaran McElroy**。技術內容：串聯共振器旁並聯一補償電路，補償電路含**以鐵電材料為傳導結構的可調 BAW 共振器**；調整直流偏壓即可提供**可變的負等效電容**以部分抵銷串聯共振器的等效電容［S10, S11］。**這證明一線 RF 大廠已在鐵電可調聲波共振器上佈局。**
- **US12489420【已驗證存在】**：標題 "Tunable ferroelectric acoustic resonator structure"。**受讓人本回合未直接確認（與 US12476613 出現在同一檢索結果中，疑同族），標為部分未驗證。**
- **US12525955【查無】**：本回合以多種檢索式查詢，**無任何命中**。**不能確認該號碼存在或與壓電/鐵電相關，請勿引用。**

### 2.6 聲波非互易：三種路線的實測數字對照

| 路線 | 代表工作 | 實測數字 | 是否需外加磁場 | 備註 |
|---|---|---|---|---|
| 聲波延遲線＋開關（時空調變） | Lu/Manzaneque/Yang/Gong（Illinois），arXiv:1801.03814 | **非互易對比 21 dB**（IL 6.7 dB / 隔離 28.3 dB），FBW 8.8%，中心頻率 155 MHz，**切換頻率僅 877.22 kHz**［S24e］ | 否 | 4-port 循環器；LiNbO₃ SPUDT 延遲線＋市售開關。**注意：另一份摘要對同一工作給出 18.8 dB / IL 6.6 / 隔離 25.4 dB，兩者不一致，需讀原文釐清。** |
| 空氣聲學循環器 | Fleury/Sounas/Alù, "Sound Isolation and Giant Linear Nonreciprocity in a Compact Acoustic Circulator"［S24f］ | 【查無具體 dB】 | 否（角動量偏壓） | 空氣聲學，非晶片級 |
| 超音波時空調變（理論） | *Phys. Rev. B* 91, 174306［S24g］ | **理論**隔離 >40 dB、IL 低至 0.3 dB、尺寸 <λ/6 | 否 | **純理論值，勿與實測混用** |
| **CMOS N-path（競爭者，非聲波）** | Reiskarimian & Krishnaswamy, *Nat. Commun.* 7, 11217 (2016)；2017 年 mm-wave 循環器 IC［S26b, S26c］ | **插入損耗 <2 dB**、強非互易、可重構 | 否 | **這是聲波路線最強的對手，且已在 CMOS 上、頻率更高。** |
| **聲電放大器（帶增益的非互易）** | Sandia, *Nature Electronics*（arXiv:2203.10608）［S25］ | **聲學增益 28.0 dB → 淨 RF 增益 +4.0 dB**，聲學 NF 2.8 dB，40.5 mW；另一組 **37.0 dB / 淨 +11.3 dB，19.6 mW**，皆 @1 GHz | 否 | **唯一一個「非互易＋淨增益」的方案。這是真正無可替代的一項。** |

- **【推算】誠實對照**：Illinois 聲波方案 IL 6.7 dB vs Krishnaswamy CMOS 方案 IL <2 dB，**聲波路線在插入損耗上輸了約 5 dB**。聲波方案的優勢在於**極低的調變頻率（877 kHz vs CMOS 需 LO 等於載波頻率）→ 功耗與相位雜訊優勢**，以及**線性度**。**若客戶要走這條，必須以「低功耗、高線性、低頻段」為主張，不能以「低損耗」為主張。**

---

## 3. 關鍵數字表

| 項目 | 數值 | 等級 | 來源 |
|---|---|---|---|
| PET 宣稱功耗優勢 | 現行 Si 電晶體的 **1/50** | 已驗證（宣稱值） | ［S5, S6］ |
| PET 材料組合 | PMN-PT（壓電）＋ SmSe（壓阻／IMT） | 已驗證 | ［S3, S4］ |
| PETMEM 專案目標 | 電壓低一個數量級、10 GHz、功耗降兩個數量級 | 已驗證 | ［S8］ |
| PETMEM 實際結論 | 「最早採用機會在 **RF 開關**」 | 已驗證 | ［S8］ |
| Menlo MM5130 閘極驅動電壓 | **>60 V**（<10 nA） | 已驗證 | ［S12］ |
| Menlo MM5130 IL / 隔離 | 0.4 dB / 25 dB @6 GHz（super-port 45 dB） | 已驗證 | ［S12, S13］ |
| Menlo MM5130 壽命 | **>3×10⁹ 次** | 已驗證 | ［S13］ |
| Menlo MM5130 功率 / IIP3 | 25 W CW、150 W 脈衝 / 95 dBm | 已驗證 | ［S13］ |
| Menlo Micro 累計募資 | **>2.25 億美元**（另一來源 2.35 億） | 已驗證 | ［S14］ |
| 壓電 AlN NEM 繼電器致動電壓 | **520 mV**（體偏壓下 **20 mV**），AlN 膜厚 10 nm | 摘要級 | ［S15］ |
| 電容式 RF MEMS 開關典型壽命 | 3×10⁶–10⁷ 次 | 摘要級 | ［S15a］ |
| 14 nm Fin-RBT 最大 Q | **115 → 181**（加 BEOL 聲波導） | 已驗證 | ［S19］ |
| 14 nm Fin-RBT 最大幅值 | 0.8 µS → 4.5 µS | 已驗證 | ［S19］ |
| AlScN 矯頑場 | **2–5 MV/cm**（可調 >3 MV/cm） | 已驗證 | ［S23］ |
| AlScN 剩餘極化 | **70–110 µC/cm²** | 已驗證 | ［S23］ |
| AlScN 寫入耐久（完整反轉） | **~10⁸ 次**（45 nm, Sc 36%） | 已驗證 | ［S24］ |
| AlScN 寫入耐久（部分切換） | **>10¹⁰ 次** | 已驗證 | ［S24］ |
| AlScN 早期耐久 | ~3,700 次 | 摘要級 | ［S24a］ |
| AlScN FBAR（Sc 30%） | 3.17 GHz、Q=572、kt²_eff=11.4% | 已驗證 | ［S31］ |
| 可重構 FBAR 頻率範圍 | **5.7 ↔ 14.2 GHz** | 已驗證 | ［S32］ |
| P3F AlScN 19 GHz 濾波器 | IL **1.3–1.58 dB**、FBW 5.11–6.26%、抑制 30–33 dB | 已驗證 | ［S21］ |
| 聲電放大器（Sandia） | 聲學增益 28.0 dB / 淨 RF +4.0 dB、NF 2.8 dB、40.5 mW @1 GHz | 已驗證 | ［S25］ |
| 聲電放大器（高增益版） | 聲學增益 37.0 dB / 淨 +11.3 dB、19.6 mW | 已驗證 | ［S25］ |
| 聲波延遲線循環器 | 對比 21 dB（IL 6.7 / 隔離 28.3）、FBW 8.8% @155 MHz | 已驗證 | ［S24e］ |
| CMOS N-path 循環器 | IL **<2 dB** | 已驗證 | ［S26b］ |
| Zepsor 累計創投募資 | **約 120 萬美元** ＋ DARPA SBIR II 180 萬 ＋ NSF 27.5 萬 | 已驗證 | ［S28, S29］ |
| BAW 濾波器市場規模 | 2025 年約 **21 億美元**（另一報告：基地台 RF 濾波器中 BAW 佔 14.6 億／38.4%） | **市調公司估計，可信度低** | ［S33］ |
| **AlScN 極化切換所需電壓（1 µm 膜）** | **Ec 3 MV/cm × 1 µm = 300 V** | **推算** | 由 ［S23］ 之 Ec 推得 |
| **5.7 GHz AlScN 半波厚度** | v≈10,000 m/s → t = v/2f ≈ **0.88 µm** | **推算** | 說明上式的量級來源 |
| **PET 位移量（d₃₃=2000 pm/V、V=0.1 V）** | **0.2 nm** | **推算** | 微縮不可行的核心算式 |

---

## 4. 「新能力型」機會

### 4.1 聲電放大器：濾波＋增益＋隔離三合一 — **最強的真新能力**

- **新能力**：在單一壓電–半導體異質結構中同時實現帶通濾波、微波淨增益與非互易隔離。傳統做法必須把壓電濾波器、半導體 LNA、旋磁隔離器三顆分開共封裝［S25］。
- **為何以前做不到**：需要漂移載子速度超過聲速（v_drift > v_sound）才能產生聲電增益，這要求**半導體薄膜與壓電薄膜在數十至數百奈米距離內強耦合**——薄膜異質整合（LiNbO₃ 智慧切割 + InGaAs 磊晶轉移）成熟之前物理上做不到。
- **是否真非替代**：**真新能力**。它不是「更好的濾波器」，而是「濾波器有了增益且變成單向的」——這在被動元件的定義上是不可能的。
- **誰在做**：Sandia National Laboratories（首發，2019 年 SAW 放大器 → 2022/23 *Nature Electronics*）［S25, S25a］。**其他團隊本回合【查無】。**
- **TRL**：**3–4**（實驗室元件，連續操作、低雜訊已證，尚無產品）。
- **市場訊號**：Sandia 是國防實驗室，此路線的第一批用戶會是相列雷達與電子戰前端；**對商用手機前端，40 mW 直流功耗換 4 dB 淨增益的效率不具吸引力。**
- **技術難點**：直流功耗（40.5 mW 換 4 dB 淨增益）、InGaAs/LiNbO₃ 異質整合良率、功率處理與線性度【查無數據】、非商用製程。
- **對台灣客戶的意義**：真正的切入點是**薄膜壓電–半導體異質基板（LiNbO₃-on-Si、InGaAs 轉移）的製造**，不是元件設計。

### 4.2 鐵電 AlScN 的極化域工程 → 19 GHz 以上 BAW 濾波器 — **最接近錢的新能力**

- **新能力**：把鐵電極化當成**一次性的製程自由度**（週期性極化 P3F），讓單一膜厚支援泛音模態，突破均勻極化壓電膜在 >8 GHz 的厚度崩壞極限［S21, S22, S23c］。
- **為何以前做不到**：**【推算】** 均勻極化 BAW 的厚度 t = v/2f；19 GHz 時 t ≈ 0.27 µm，膜太薄導致電極損耗佔比暴增、Q 崩壞。P3F 用三層反向極化在同樣總厚度下工作於三次泛音，等效厚度增為 3 倍。**在 AlScN 被證實為鐵電（2019）之前，氮化物系統根本無法在成長後改變極性，所以這件事在 2019 年前物理上不存在。**
- **是否真非替代**：**真新能力**（對 >8 GHz 而言）；對 <6 GHz 而言只是替代品。
- **誰在做**：學界＋**商用 XBAW 製程**（該製程為 Akoustis 之商標名，**本回合未直接驗證論文與該公司之關係，標為未驗證**）；Qorvo 已有鐵電可調聲波共振器專利 US12476613［S10, S11］。
- **TRL**：**5–6**（已在商用產線做出共振器與濾波器並量測）。**這是本文件 TRL 最高的一項。**
- **市場訊號**：6G / FR3（7–24 GHz）與 Ku 頻段衛星通訊；BAW 市場 2025 年規模數十億美元量級［S33，市調估計］。
- **技術難點**：極化步驟的電壓（**推算 300 V/µm 級**）、極化均勻性、Sc 含量提高後的漏電與崩潰（會退化為絲狀電阻切換［S24b］）。

### 4.3 「可重構／非揮發」聲波前端 — **半新能力，且有明確物理天花板**

- **新能力**：同一顆 FBAR 靠鐵電極化狀態在 **5.7 GHz ↔ 14.2 GHz** 之間非揮發切換［S32］；或以 N-polar / metal-polar 切換改變頻率響應［S31］。這正是客戶命題「同一顆壓電體既是被動（濾波）又是主動（可寫入狀態）」的字面實現。
- **為何以前做不到**：需要一個「既是好壓電體、又是可切換鐵電體」的材料。PZT 是鐵電但不耐高頻且不相容 CMOS；AlN 相容但不可切換。**AlScN 是 2019 年才出現的交集。**
- **是否真非替代**：**半**。功能上與「多顆濾波器 + 開關」等價（現行做法），但**省去開關的插入損耗與面積**是實質改善。
- **TRL**：**3**。
- **最大技術難點（誠實）**：**【推算】切換電壓。** 5.7 GHz 的 AlScN 膜厚約 0.88 µm，Ec 取 3 MV/cm → **切換需約 260 V**。在手機前端這是不可接受的。**這解釋了為何 P3F（工廠一次性極化）已進商用產線，而場域可重構 FBAR 還停在論文——兩者材料相同、TRL 差三級，差別就在「誰來出這 260 V」。這是本文件最重要的一個工程判斷。**

### 4.4 壓電 NEM 繼電器做超低壓／零漏電開關 — **半新能力，接點是死結**

- **新能力**：**520 mV / 20 mV 致動**［S15］——這是靜電式（>60 V［S12］）與 pull-in 物理無法達到的區域，因此對「邏輯電壓域的機械繼電器」是真新能力；對 RF 開關則是替代品。
- **為何以前做不到**：靜電力 ∝ V²/g²，在邏輯電壓下產生的力太小；壓電應變與電壓線性且不依賴間隙。
- **TRL**：**2–3**。
- **死結**：接點冶金與壽命，見 §5.3。

### 4.5 免釋放 CMOS 內建共振器 — **整合度躍進，效能不足**

- **新能力**：**零額外光罩**在 14 nm FinFET 中做出 X 波段聲波共振器［S19］；或在 130 nm FeRAM 製程中以 FeCAP 做可調 RF 共振器［S20］。
- **是否真非替代**：**半**。功能（時脈、濾波）本已存在。
- **TRL**：**3–4**。
- **誠實上限**：**Q ≈ 181**［S19］。以此 Q 做濾波器不可行，做低相位雜訊時鐘也吃力。**除非 Q 提升一個數量級，否則這是學術成就而非產品路線。**

### 4.6 零靜態功耗喚醒 — **能力為真，市場未證**

- 見 §1.7 與 §5.4。**TRL 4–6（有樣品、有 CES 展示，未量產）**，但九年僅募得數百萬美元量級資金［S28, S29］。

---

## 5. 反面證據、失敗案例與物理上限

### 5.1 IBM PET：目標從「取代 CMOS」退到「RF 開關」

**這是本文件最重要的單一事實。** PETMEM 專案摘要白紙黑字寫著指導委員會認為最早採用機會在 RF 開關、記憶體是長期目標［S8］。一個以「10 GHz、功耗降兩個數量級、取代 CMOS」立項的旗艦專案，最後把出路訂在一個既有市場的替代品上。**任何「用壓電做主動邏輯元件」的提案，都應被要求先解釋自己為何不會重蹈此覆轍。**

### 5.2 Piezotronics：邏輯做過了，但無法級聯

*ACS Nano* 的 GaN 奈米帶應變閘控壓電邏輯［S1b］證明了「可以做出邏輯功能」，但**輸入是機械應變、輸出是電流**，兩者物理量不同，無法把前級輸出接到後級輸入。**這不是工程問題，是架構問題。** 加上量測方法學爭議至 2019 年仍未完全平息［S2a, S2b］，且**無任何商品**【查無】——結論：**piezotronics 是應變／觸覺感測技術，不是計算技術。**

### 5.3 MEMS 開關的價值分配對客戶不利

Menlo Micro 用 2.25 億美元證明的是：**這個市場的護城河在接點冶金與封裝，不在致動器**［S13, S14］。壓電式能把驅動電壓從 60 V 降到 0.5 V［S12, S15］，這在**邏輯繼電器**上是決定性的，但在 **RF 開關**上客戶並不在乎（60 V 電荷幫浦只是一顆便宜的 IC，功耗 <10 nA）。**若客戶的核心資產是壓電薄膜，進入 MEMS 開關市場時握有的是價值較低的那一半。**

### 5.4 零功耗喚醒：九年，數百萬美元，仍在出樣品

2017 *Nature Nanotechnology*［S27］→ 2021 成立 Zepsor → 2025 CES 展示 → 「計畫未來 12 個月出貨樣品」［S28, S29］。累計創投資金約 120 萬美元，其餘靠 DARPA/NSF/ARPA-E 補助［S28］。**這是「科學成立但市場拉力弱」的典型形態：CMOS 喚醒接收器的靜態功耗已進入 nW 區間，「nW 對 0」對多數應用不值得換一顆可靠性未知的 MEMS。** 另注意：連 N-ZERO 的 RF 喚醒開關都用**靜電式** AlN［S26a］。

### 5.5 聲波非互易輸給 CMOS 的插入損耗

Illinois 聲波循環器 IL 6.7 dB［S24e］vs Krishnaswamy CMOS N-path IL <2 dB［S26b］，且後者已推進到毫米波［S26c］。**聲波路線唯一守得住的論點是「調變頻率 877 kHz vs LO 頻率等於載波」帶來的功耗與相位雜訊優勢，以及線性度。** *Phys. Rev. B* 那個 >40 dB 隔離 / 0.3 dB IL 是**純理論值**［S24g］，**不得與實測混用**——這是本領域最常見的引用陷阱。

### 5.6 AlScN 的三個硬物理上限

1. **切換電壓 = Ec × 厚度**。Ec = 2–5 MV/cm［S23］是材料常數（比 HfO₂ 高一個數量級以上）。**任何需要在使用中切換 GHz 級厚度膜的方案，都要面對 100–300 V。【推算】**
2. **耐久性 vs 極化量的取捨**。完整反轉 ~10⁸ 次，部分切換才 >10¹⁰ 次［S24］——**部分切換意味著只用到一部分極化量，代價是訊號差異變小。**
3. **崩潰會把鐵電變成電阻式開關**［S24b］。Sc 含量提高可增強壓電性與降低 Ec，但同時增加缺陷與漏電。**「高 Sc + 高耐久 + 低漏電」三者互斥，這是客戶必須自行做的材料權衡。**

### 5.7 免釋放共振器的 Q 值天花板

Q = 181 @X 波段［S19］。**論文自己指出限制因素是 BEOL 聲學侷限**——也就是說瓶頸來自代工廠既定的金屬/介電疊構，**設計者無權改變**。這意味著改善空間受限於代工廠是否願意為此改製程，**這是商業障礙偽裝成技術障礙**。

### 5.8 通則：機械域沒有增益

**【推算／物理論證】** 壓電效應是線性可逆的能量轉換，本身不提供功率增益。因此所有「壓電主動元件」在架構上都是「壓電致動器 + 一個真正提供增益或非線性的東西」：piezotronics 靠蕭特基接面、PET 靠 SmSe 的 Mott 轉變、NEM 繼電器靠金屬接點通斷、RBT 靠 FET 通道。**唯一的例外是聲電放大器——它的增益來自漂移載子對聲波的能量注入（超音速漂移），這是真正在壓電–半導體耦合中產生的增益。這也正是為什麼 §4.1 是本文件中唯一的「真新能力」等級判定。**

---

## 6. 未解問題

1. **US12525955 是否存在？** 本回合【查無】。若客戶手上有此號碼的來源，請回頭確認是否為誤植（例如應為 **US12489420** 或其他 Qorvo 同族專利）。
2. **鐵電記憶體對照組完全未查。** FMC、GlobalFoundries 22FDX FeFET、SK Hynix、Micron、TSMC 的投入與量產狀態，以及 NC-FET 爭議現況——**這兩題是判斷「客戶的 AlScN 薄膜能力是否該轉向記憶體」的關鍵，本輪未做，必須補。**
3. **P3F AlScN 的商用歸屬未釐清。** 「commercial XBAW process」是誰的產線？該論文與 Akoustis 的關係為何？**這決定客戶是「可以合作」還是「已經被卡位」。**
4. **聲電放大器的功率處理、線性度（IIP3）與封裝熱設計無任何數據。** 沒有這三個數字，無法判斷它能否進入雷達/EW 前端。
5. **壓電 NEM 繼電器的 520 mV / 20 mV 論文之作者、單位與實測壽命曲線未驗證。** 該數字是本文件「壓電對靜電」論證的支柱，必須讀原文確認是熱切換還是冷切換條件。
6. **Illinois 聲波循環器的兩組不一致數字**（21 dB/6.7 dB/28.3 dB vs 18.8 dB/6.6 dB/25.4 dB）需以原文釐清。
7. **量子聲學／微波–光轉換路線本輪完全未查**，前一版的相關內容因無法驗證已全數刪除。

---

## 7. 來源清單

> 以下 URL 均為本回合 WebSearch 回傳之結果連結。**因 WebFetch 全面 403，沒有任何一篇被實際開啟閱讀**，內容來自搜尋摘要。

| # | 標題 | URL | 說明 |
|---|---|---|---|
| S1 | Zhong Lin Wang — Georgia Tech MSE | https://www.mse.gatech.edu/people/zhong-lin-wang | 確認 2007 年提出壓電電子學效應 |
| S1a | Strain-Gated Piezotronic Transistors Based on Vertical Zinc Oxide Nanowires (ACS Nano) | https://pubs.acs.org/doi/abs/10.1021/nn301277m | 垂直 ZnO 奈米線應變閘控電晶體 |
| S1b | GaN Nanobelt-Based Strain-Gated Piezotronic Logic Devices and Computation (ACS Nano) | https://pubs.acs.org/doi/abs/10.1021/nn4026788 | 壓電邏輯確實被做出過，但無法級聯 |
| S2 | Piezoelectric-Potential-Controlled Polarity-Reversible Schottky Diodes and Switches of ZnO Wires (Nano Lett.) | https://pubs.acs.org/doi/10.1021/nl802497e | 壓電位調變蕭特基能障的原始論文之一 |
| S2a | Energy Harvesting Using Piezoelectric Nanowires — Correspondence on "Energy Harvesting Using Nanowires?" by Alexe et al. | https://www.researchgate.net/publication/227988003_Energy_Harvesting_Using_Piezoelectric_Nanowires-A_Correspondence_on_Energy_Harvesting_Using_Nanowires_by_Alexe_et_al | **量測假影爭議的正面證據**：雙方互指對方為系統假影 |
| S2b | Toward Quantitative Measurements of Piezoelectricity in III-N Semiconductor Nanowires (arXiv:1910.01187) | https://arxiv.org/pdf/1910.01187 | 到 2019 年奈米線壓電的定量量測仍是開放問題 |
| S2c | Fundamentals and Applications of ZnO-Nanowire-Based Piezotronics and Piezo-Phototronics (PMC) | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9860666/ | 綜述 |
| S2d | Advances in piezotronic transistors and piezotronics (ScienceDirect) | https://www.sciencedirect.com/science/article/abs/pii/S1748013221000335 | 2021 年綜述 |
| S3 | Pathway to the PiezoElectronic Transduction Logic Device (arXiv:1503.07467) | https://arxiv.org/pdf/1503.07467 | PET 原理與 PMN-PT/SmSe 選材 |
| S4 | Pathway to the Piezoelectronic Transduction Logic Device (Nano Letters) | https://pubs.acs.org/doi/abs/10.1021/nl5046796 | Nano Lett. 15(4) 2391–2395 (2015) |
| S4a | 同上 PubMed | https://pubmed.ncbi.nlm.nih.gov/25793915/ | 書目資料 |
| S5 | First realization of the piezoelectronic stress-based transduction device (PubMed) | https://www.ncbi.nlm.nih.gov/pubmed/26302818 | Nanotechnology 26(37) 375201 (2015) |
| S5a | The piezoelectronic stress transduction switch for VLSI, low voltage sensor computation, and RF applications (APL 107, 073505) | https://pubs.aip.org/aip/apl/article-abstract/107/7/073505/30471/ | **標題已出現 RF——轉向的早期訊號** |
| S6 | IBM Research 出版頁：First realization of the piezoelectronic stress based transduction device | https://research.ibm.com/publications/first-realization-of-the-piezoelectronic-stress-based-transduction-device | IBM 官方頁面，1/50 功耗宣稱 |
| S6a | US9425381（多層堆疊壓電層低電壓電晶體與邏輯元件） | https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/9425381 | IBM PET 專利族（另有 US9466781、US9590167） |
| S7 | The piezoelectronic transistor: A nanoactuator-based post-CMOS digital switch (MRS Bulletin, 2012) | https://link.springer.com/article/10.1557/mrs.2012.267 | 概念原始提出 |
| S8 | PETMEM — Piezoelectronic Transduction Memory Device, H2020 Project 688282 (CORDIS) | https://cordis.europa.eu/project/id/688282 | **「最早採用機會在 RF 開關」的官方結論來源** |
| S8a | PETMEM Workshop 2019 (E-MRS) | https://www.european-mrs.com/meetings/2019-spring/satellite-events/petmem-workshop-2019-piezoelectronic-transduction-devices | 專案最後的公開活動 |
| S9 | 4-Terminal Piezoelectronic Transistor (PET), US20130009668 | https://patents.justia.com/patent/20130009668 | IBM PET 早期專利申請 |
| S10 | Filter circuitry using ferroelectric tunable acoustic resonator, **US12476613** | https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/12476613 | **Qorvo US, Inc.；發明人 Niewczas / McLaughlin / McElroy** |
| S11 | Tunable ferroelectric acoustic resonator structure, US12489420 | https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/12489420 | 同族疑似專利（受讓人未直接確認） |
| S12 | Menlo Micro RF 產品頁 | https://menlomicro.com/products/rf | 閘極驅動 >60 V、<10 nA；電阻式（ohmic）MEMS |
| S13 | MM5130 Datasheet（Menlo Micro） | https://menlomicro.com/images/general/MM5130_Datasheet.pdf | IL 0.4 dB、隔離 25/45 dB、IIP3 95 dBm、25 W、>3×10⁹ 次、2.5×2.5 mm |
| S14 | Menlo Micro Announces $150 Million in Series C Funding | https://menlomicro.com/newsroom/menlo-micro-announces-150-million-in-series-c-funding-as-ideal-switch-technology-accelerates-the-electrification-of-everything | 累計 >2.25 億美元；GE/Microsemi/Corning 1,870 萬創立 |
| S15 | Sub-1-volt Piezoelectric Nanoelectromechanical Relays With Millivolt Switching Capability | https://www.researchgate.net/publication/262572567_Sub-1-volt_Piezoelectric_Nanoelectromechanical_Relays_With_Millivolt_Switching_Capability | **520 mV / 20 mV 致動、10 nm AlN**（作者未驗證） |
| S15a | A review on RF MEMS switch for radio frequency applications (Microsyst. Technol.) | https://link.springer.com/article/10.1007/s00542-020-05025-y | 壽命對照：電容式 3×10⁶–10⁷ 次；<1 V 切換可望 >10⁹ 次 |
| S15b | Body-Biased Complementary Logic Implemented Using AlN Piezoelectric MEMS Switches | https://www.researchgate.net/publication/224120737_Body-Biased_Complementary_Logic_Implemented_Using_AlN_Piezoelectric_MEMS_Switches | 壓電繼電器做互補邏輯的學術嘗試 |
| S16 | The Resonant Body Transistor (Nano Letters 10(4) 1234–1237, 2010) | https://pubs.acs.org/doi/10.1021/nl9037517 | Weinstein & Bhave 原始論文 |
| S17 | RBT 論文 PDF（Purdue HybridMEMS） | https://engineering.purdue.edu/hybridmems/wp-content/uploads/website_publications/NanoLetters2010_Dana_RBT.pdf | 全文 PDF 連結（本回合未開啟） |
| S18 | Theory and Design of Phononic Crystals for Unreleased CMOS-MEMS Resonant Body Transistors (IEEE JMEMS) | https://ieeexplore.ieee.org/document/7096929/ | IBM 32 nm SOI 實作 |
| S19 | X-Band Fin Resonant Body Transistors in 14nm CMOS Technology (arXiv:2107.00608) | https://arxiv.org/abs/2107.00608 | **Q 115→181、幅值 0.8→4.5 µS；限制為 BEOL 聲學侷限** |
| S19a | 32GHz resonant-fin transistors in 14nm FinFET technology | https://www.researchgate.net/publication/323822355_32GHz_resonant-fin_transistors_in_14nm_FinFET_technology | 更高頻的後續工作 |
| S20 | A tunable ferroelectric based unreleased RF resonator (Microsystems & Nanoengineering, 2019) | https://www.nature.com/articles/s41378-019-0110-1 | **TI 130 nm FeRAM 製程、無釋放步驟；主動被動同體的既有實證** |
| S21 | 19 GHz Single-Ended-to-Balanced Modified Ladder-Lattice Filters Realized Using Periodically Polarized AlScN BAW Resonators (arXiv:2606.00064) | https://arxiv.org/abs/2606.00064 | **IL 1.3–1.58 dB、FBW 5.11–6.26%、抑制 30–33 dB** |
| S22 | A High Quality Factor, 19-GHz Periodically Poled AlScN BAW Resonator Fabricated in a Commercial XBAW Process (IEEE) | https://ieeexplore.ieee.org/document/10632112/ | **商用產線實作；兩層 as-grown ＋ 一層電性極化** |
| S23 | AlScN: A III-V semiconductor based ferroelectric (J. Appl. Phys. 125, 114103, 2019) | https://pubs.aip.org/aip/jap/article/125/11/114103/155873/ | **Ec 2–5 MV/cm、Pr 70–110 µC/cm²** |
| S23a | Ultrathin AlScN for low-voltage driven ferroelectric-based devices (arXiv:2207.01858) | https://arxiv.org/pdf/2207.01858 | 低電壓化路線 |
| S23b | In-Grain Ferroelectric Switching in Sub-5 nm Thin AlScN Films at 1 V (arXiv:2304.02909) | https://arxiv.org/pdf/2304.02909 | 5 nm 膜、1 V 切換（與 Ec 推算一致） |
| S23c | Periodically poled AlScN BAW resonators and filters for communications in the 6G era (Microsyst. Nanoeng. 2024) | https://www.nature.com/articles/s41378-024-00857-4 | P3F 的 6G 定位 |
| S24 | Write cycling endurance exceeding 10¹⁰ in sub-50 nm ferroelectric AlScN (Nature Communications, 2025) | https://www.nature.com/articles/s41467-025-68221-2 | **完整反轉 ~10⁸；部分切換 >10¹⁰；45 nm Al₀.₆₄Sc₀.₃₆N** |
| S24a | 同上 PubMed | https://pubmed.ncbi.nlm.nih.gov/41513656/ | 書目與早期 3,700 次耐久對照 |
| S24b | Role of Defects in the Breakdown Phenomenon of Al₁₋ₓScₓN: From Ferroelectric to Filamentary Resistive Switching (Nano Letters) | https://pubs.acs.org/doi/10.1021/acs.nanolett.3c02351 | **崩潰機制：鐵電退化為絲狀電阻切換** |
| S24c | Temperature-dependent wake-up phenomena in AlScN ferrodiode memory devices (APL 128, 022903) | https://pubs.aip.org/aip/apl/article/128/2/022903/3377478/ | Penn（Olsson / Jariwala）；偏壓 <10 V |
| S24d | Metal-ferroelectric AlScN-semiconductor memory devices on SiC wafers (APL 123, 122901) | https://pubs.aip.org/aip/apl/article-abstract/123/12/122901/2911584/ | AlScN 記憶體於 SiC 上 |
| S24e | A Radio Frequency Non-reciprocal Network Based on Switched Low-loss Acoustic Delay Lines (arXiv:1801.03814) | https://arxiv.org/pdf/1801.03814 | **21 dB 對比、IL 6.7 / 隔離 28.3 dB、877.22 kHz 切換**（Illinois, Gong） |
| S24f | Sound Isolation and Giant Linear Nonreciprocity in a Compact Acoustic Circulator | https://www.researchgate.net/publication/259989778_Sound_Isolation_and_Giant_Linear_Nonreciprocity_in_a_Compact_Acoustic_Circulator | Alù 團隊空氣聲學循環器 |
| S24g | Subwavelength ultrasonic circulator based on spatiotemporal modulation (Phys. Rev. B 91, 174306) | https://journals.aps.org/prb/abstract/10.1103/PhysRevB.91.174306 | **理論值 >40 dB 隔離 / 0.3 dB IL，勿與實測混用** |
| S24h | Acoustic nonreciprocity (J. Appl. Phys. 129, 210903, 2021) | https://pubs.aip.org/aip/jap/article/129/21/210903/1065022/ | 領域綜述 |
| S24i | RF Magnet-free Circulators Based on Spatiotemporal Modulation of SAW Filters (arXiv:1905.13252) | https://arxiv.org/pdf/1905.13252 | SAW 時空調變循環器 |
| S25 | Non-reciprocal acoustoelectric microwave amplifiers with net gain and low noise in continuous operation (Nature Electronics) | https://www.nature.com/articles/s41928-022-00908-6 | **28.0 dB 聲學增益 / 淨 +4.0 dB、NF 2.8 dB、40.5 mW；另 37.0 dB / +11.3 dB、19.6 mW** |
| S25a | High-gain leaky surface acoustic wave amplifier in epitaxial InGaAs on lithium niobate heterostructure (Sandia) | https://www.sandia.gov/research/publications/details/high-gain-leaky-surface-acoustic-wave-amplifier-in-epitaxial-ingaas-on-lith-2019-06-24/ | 2019 年前導工作 |
| S25b | Nonreciprocal low-noise acoustoelectric microwave amplifiers (arXiv:2203.10608) | https://arxiv.org/pdf/2203.10608 | 預印本 |
| S26 | DARPA: Dormant, Yet Always-Alert Sensor Awakes Only in the Presence of a Signal of Interest (2017) | https://www.darpa.mil/news/2017/always-alert-sensor | N-ZERO 官方新聞 |
| S26a | Design and Fabrication of an Electrostatic AlN RF MEMS Switch for Near-Zero Power RF Wake-Up Receivers | https://www.researchgate.net/publication/326659889_Design_and_Fabrication_of_an_Electrostatic_AlN_RF_MEMS_Switch_for_Near-Zero_Power_RF_Wake-Up_Receivers | **注意：致動為靜電式，AlN 為結構材料** |
| S26b | Magnetic-free non-reciprocity based on staggered commutation (Nature Communications 7, 11217) | https://www.nature.com/articles/ncomms11217 | Krishnaswamy / Reiskarimian，CMOS N-path |
| S26c | Columbia engineers invent breakthrough millimeter-wave circulator IC (2017) | https://www.technology.org/2017/10/19/columbia-engineers-invent-breakthrough-millimeter-wave-circulator-ic/ | **IL <2 dB，毫米波** |
| S27 | Zero-power infrared digitizers based on plasmonically enhanced micromechanical photoswitches (Nature Nanotechnology, 2017) | https://www.nature.com/articles/nnano.2017.147 | Rinaldi 團隊零功耗紅外數位化器 |
| S28 | Zepsor Technologies Taps Spark Fund to Scale Zero-Power Sensor Solutions (Northeastern) | https://coe.northeastern.edu/news/zepsor-technologies-taps-spark-fund-to-scale-zero-power-sensor-solutions | 融資與 ARPA-E / NSF / DARPA SBIR 補助 |
| S29 | These 'Zero Power' Sensors May Change Consumer Electronics (Northeastern News, 2025-10-06) | https://news.northeastern.edu/2025/10/06/zhenyun-qian-designs-zero-power-sensors/ | CES 2025 展示、12 個月內出樣 |
| S29a | Zepsor Technologies Joins the Silicon Catalyst Incubator | https://siliconcatalyst.com/zepsor-technologies-joins-the-silicon-catalyst-incubator | 孵化器與投資人 |
| S30 | STeP-CiM: Strain-enabled Ternary Precision Computation-in-Memory based on Non-Volatile 2D Piezoelectric Transistors (arXiv:2203.16416) | https://arxiv.org/pdf/2203.16416 | 壓電應變閘控用於記憶體內運算 |
| S31 | Ferroelectric AlScN Thin Film Bulk Acoustic Resonators with Polarization-Dependent Operating States (pss RRL, 2021) | https://onlinelibrary.wiley.com/doi/10.1002/pssr.202100034 | **3.17 GHz、Q 572、kt²_eff 11.4%；N-polar ↔ metal-polar** |
| S32 | Reconfigurable FBAR Enabled by AlScN Ferroelectric Film Switching (IEEE) | https://ieeexplore.ieee.org/document/11235225/ | **5.7 ↔ 14.2 GHz 重構；單次梯形脈衝近 100% 切換** |
| S32a | Intrinsically Switchable GHz Ferroelectric ScAlN SAW Resonators | https://www.researchgate.net/publication/363242130_Intrinsically_Switchable_GHz_Ferroelectric_ScAlN_SAW_Resonators | 可切換 SAW 共振器 |
| S33 | BAW Filter Market Analysis（多家市調） | https://www.globalgrowthinsights.com/market-reports/bulk-acoustic-wave-baw-rf-filters-market-103695 | **市調公司估計值，各家差異大（21 億 vs 178 億），可信度低，僅供量級參考** |
| S34 | Plasmonically Enhanced Flexural-Mode AlScN Nanoplate Resonator as Uncooled and Ultrafast IR Detector (arXiv:2506.21412) | https://arxiv.org/pdf/2506.21412 | AlScN 用於零功耗紅外偵測的最新工作 |

---

**最後提醒**：本文件所有數字皆來自搜尋摘要而非論文全文（WebFetch 全面封鎖）。**在寫入任何對外簡報或投資決策文件前，§3 表格中每一個數字都應由人工開啟對應 URL 複核。** 標為【查無】與【推算】者尤須注意其性質差異：前者是我不知道，後者是我用明示假設算出來的、可被推翻的估計。
