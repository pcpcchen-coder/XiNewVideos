# 壓電變壓器/壓電諧振器功率轉換的技術現況與元件能力邊界

> 一句話結論：壓電元件在「小體積、低壓差比、非隔離」的窄帶條件下已能做到 99% 效率與 5.7 kW/cm³ 的諧振體功率密度，物理上確實贏過磁性元件；但它的價值不在取代電感，而在於**磁性元件在物理上做不到的場合**——強磁場環境、元件本身即為放電電極（冷電漿）、毫克級高壓源、密閉金屬穿透供電——這些才是非替代性的新能力。

---

## 0. 研究方法與限制說明（誠實揭露）

本輪研究在受限網路環境下執行：**WebFetch 工具被本 session 的 egress policy 全面封鎖（所有網域皆回 403，含 arXiv、MDPI、Nature、IEEE、Wikipedia、廠商官網），curl 亦被 CONNECT tunnel 403 阻擋**。因此本文件所有事實均來自 **27 次 WebSearch**（英/中/日文關鍵字）所回傳的搜尋摘要與標題，並逐條對應到第 7 節的 URL。凡屬「摘要語意可能失真」或「無法交叉驗證」者，均標註「未驗證」。凡查不到者標註「查無」。**未捏造任何專利號、型號、公司名或數字。**

---

## 1. 結論摘要（8 條）

1. **實驗室效率與功率密度紀錄已經很漂亮，但條件極窄。** 單埠壓電諧振器（PR）的無磁性 DC-DC 設計已達 **功率級效率 99%、PR 功率承載密度 5.7 kW/cm³**；但公開文獻同時明說這些成績「只在**非隔離、且電壓轉換比溫和（2:1）**的條件下取得，把壓電式功率轉換的適用性侷限在很窄的應用子集」。〔S13〕

2. **MIT 的代表性硬體：275→150 V、12 W，493 kHz，PR 功率承載密度 1.01 kW/cm³**（Boles, Bonavia, Lang, Perreault，IEEE TPEL，獲 2024 年 10 月 TPEL Prize Letter Award）。關鍵誠實數字：該工作點的**理論效率 98.2%，但在最高功率點實測掉到 93.3%**。〔S1, S6〕

3. **Stanford 的代表性硬體：180 V→60 V，最大 89 W，效率 97%，PR 功率密度 1340 W/cm³**（Rivas-Davila 團隊）。〔S2〕

4. **首顆 IC 化的 PR 轉換器出現在 ISSCC 2024**：UC San Diego + CEA-Leti 的 DSPPR（Dual-side Series/Parallel Piezoelectric Resonator）「20-to-2.2 V」轉換器，把所有功率開關整合到單晶片，對 VCR < 0.125 相對前人離散設計**降低損耗 310%**；諧振體為 **Ø20 mm × 200 µm 厚**；資料中心導向版本宣稱 **96.2% 峰值效率（約 10:1 降壓）**。〔S14, S15〕

5. **隔離型壓電變壓器（PT）在 2025 年才追上來**：Berkeley（Naval, Xu, Touhami, Boles，APEC 2025）以徑向模 PT 設計框架同時達成峰值效率與 ZVS，原型**功率級效率 >97% 涵蓋寬工作範圍、峰值 98.3%，相對先前「無磁性隔離型 PT DC-DC」降低損耗比約 27 倍**。〔S22〕

6. **材料端的天花板由 Q·k² 決定，而 2022–2026 的突破全在鈮酸鋰（LN）與單晶 AlN**：LN 厚度剪切模 **Q 3500 / k²t 45% @ 5.94 MHz**；LN 厚度伸張模無雜模 **Q 4000 / k²t 30%**；週期極化 LN **k² 29% / Q 3187**（宣稱功率諧振器中最佳 f·Q 積）；單晶 AlN 晶圓 TE 模 **Q 1677 / k² 6.1%**，但**熱導率比現行 PZT/LN 高出數個數量級**。〔S16, S17, S18, S19〕

7. **元件成本結構的殺手是「頻率篩選 + 極化 + 陶瓷後加工」，不是材料本身。** 製程為：粉末壓製（壓力可達 1 MN）→ 1250–1350 °C 燒結 → 鋸切/研磨/拋光/研磨定尺寸 → 網印或濺鍍電極 → 熱油浴中以數 kV/mm 極化 → 量測共振頻率並分選。文獻明指窄頻元件需要**頻率準確度優於 0.1%**，以傳統製程做會得到「非常差的良率」。〔S24〕

8. **CCFL 是唯一一次真正的大量出貨，而且它死了。** 1990s 至 2000s 初，PT 主要用於筆電 LCD 的 CCFL 背光高壓逆變器，**年銷量估計超過 2,500 萬～3,000 萬顆，主要產地在日本**；2000s 末背光由 CCFL 轉 LED，高壓 PT 銷量持續下滑，**多數領導供應商停止量產**。這是評估任何壓電功率元件商業計畫時必須內建的歷史教訓。〔S3〕

---

## 2. 現況：技術 / 產品 / 玩家

### 2.1 學術玩家地圖（2019–2026）

| 團隊 | 主持人 | 主攻方向 | 代表成果 |
|---|---|---|---|
| MIT PER Group | D. J. Perreault, J. H. Lang | 拓樸列舉、soft-charging/ZVS 切換序列、高功率密度 PR | 275→150 V/12 W，1.01 kW/cm³；US 12009746、US 12388364 專利 |
| UC Berkeley Boles Lab | Jessica D. Boles（原 MIT） | 隔離型多埠 PT、overtone PR、piezo「主動電感」 | APEC 2025 隔離 PT 98.3%；COMPEL 2024 active inductor |
| Stanford SUPERLAB | Juan Rivas-Davila | 材料/諧振體優化（LN、AlN 單晶）、Class-E + PR | 180→60 V/89 W/97%/1340 W/cm³；LN Q 3500 k²t 45%；AlN Q 1677 |
| UC San Diego + CEA-Leti | Hanh-Phuc Le 等 | PR 轉換器 IC 化、與開關電容混成 | ISSCC 2024 DSPPR，310% 損耗降低 |
| Univ. Toulouse / LAPLACE | François Pigache, Clément Nadal | PT 建模（Hamilton 原理）、**PT 驅動電漿**、MEMS 高壓供電 | Nadal 2011 博論主題即為「專為電漿產生而設計的壓電變壓器」 |
| Penn State（材料端） | Kenji Uchino | 高功率壓電特性、損耗機制、振動速度極限 | 開發振動速度 >1 m/s 材料，功率密度為市售硬質 PZT 的 10 倍 |
| SLAC / CPAD（應用端） | Nikolica 等 | 高能物理探測器前端的新型 DC-DC | CPAD 2023 / 2025 報告：磁場與輻射環境下的無磁性轉換 |

日本方面：**未查到 2023–2026 有規模的壓電變壓器功率轉換學術群**；日文檢索主要回到工業高壓變壓器廠商（タムラ製作所、富士セラミックス、NT販売）而非新研究。中文檢索（清華、浙大）也**未找到 2024 年前後的壓電變壓器 DC-DC 專題成果**，回傳的是高頻磁性變壓器與部分功率變換器綜述（清華孫凱團隊，最高效率 98.14%、功率密度 126 W/in³，但那是磁性方案，與壓電無關）。**結論：這條技術線目前是「美國 + 法國」主導，日本已從 CCFL 時代的製造中心退場，中國大陸尚未見顯著投入。**〔S20, S21〕

### 2.2 真正在賣的商品（不是論文）

- **TDK / EPCOS CeraPlas™ 系列**（F series，型號 Z63000Z2910Z…1Z68）：PZT 基冷電漿產生元件，塑膠封裝，**47.3 × 20 × 20 mm，工作頻率 52 kHz，典型功率 8 W，輸入 12 Vpp，輸出最高 20 kV（負載相依），電漿氣體溫度 <50 °C**。〔S25〕
- **relyon plasma（TDK 集團）PiezoBrush PZ3**：手持式常壓冷電漿裝置，**最大耗電 18 W**，核心即 CeraPlas。〔S9〕
- **STEMINC**：單層 PT（如 SMSTF50P2S6，50 kHz，2 W 級）、多層 PT（SMMTF55P4S80，55 kHz，4 W；SMMTF55P6S50，55 kHz，6 W）。**零售價 SMSTF50P2S6 為 2 顆 USD 23.76，即約 USD 11.88/顆**（小量零售價，非量產價）。〔S10, S11〕
- **歷史商品**：CCFL 背光逆變器模組。文獻明說「壓電變壓器主要商品化在 LCD 背光逆變器模組」，且「目前商用高壓 PT 皆為非隔離型」。〔S26〕

### 2.3 專利地景（已驗證的具體專利號）

| 專利號 | 標題 | 受讓人 / 說明 |
|---|---|---|
| US 12009746 | DC-DC converter based on piezoelectric resonator | MIT；2020-06-12 申請，2024-06-11 核准；發明人 Perreault, Boles, Piel；主張以 PR 作為功率級唯一儲能元件並定義 connected/open 切換序列以達成低損耗 soft-charging〔S23〕 |
| US 12388364 | DC-DC converter based on piezoelectric resonator | MIT；2024-05-01 申請，2025-08-12 核准；同族延續〔S23〕 |
| US 11716023 | Closed loop control for piezoelectric-based power converters | 受讓人**未驗證**（搜尋結果未能確認；相關 MIT 論文 dspace.mit.edu/handle/1721.1/143258 主題一致）〔S12〕 |
| US 10096764 | Application of piezo technology to convert AC line power to isolated DC power in high external magnetic fields | 受讓人**查無**；主張以壓電技術在強外部磁場中做 AC→隔離 DC〔S8〕 |
| US 5969954 | AC/DC converter with a piezoelectric transformer | 歷史專利，證明 AC-DC PT 路線 1990s 就有人走〔S26〕 |

UC Berkeley 技轉平台上目前掛牌可授權的三項壓電功率技術：**Piezoelectric Transformers For Power Conversion（NCD 33842）、Active Inductor Based On A Piezoelectric Resonator（NCD 33585）、Overtone Piezoelectric Resonator For Power Conversion（NCD 33625）**。〔S13, S27〕

---

## 3. 關鍵數字表

### 3.1 轉換器性能紀錄

| 團隊/來源 | 電壓 | 功率 | 頻率 | 效率 | 功率密度 | 備註 |
|---|---|---|---|---|---|---|
| MIT (Boles et al., TPEL) | 275→150 V | 12 W | 493 kHz | 理論 98.2%，最高功率點實測 **93.3%** | **1.01 kW/cm³**（諧振體） | 徑向模 PZT；2024/10 TPEL Prize Letter Award |
| Stanford (Rivas-Davila) | 180→60 V | 89 W | 查無 | 97% | **1340 W/cm³**（諧振體） | 目前查到功率最高的 PR 原型之一 |
| 領域 SOTA（單埠 PR） | 2:1 VCR | 查無 | 查無 | **99%**（功率級） | **5.7 kW/cm³** | 明示僅限非隔離、溫和 VCR |
| UCSD + CEA-Leti (ISSCC 2024) | 20→2.2 V | 查無 | 查無 | **96.2%**（約 10:1） | 諧振體 Ø20 mm × 200 µm | 首顆 PR 轉換 IC；VCR<0.125 損耗降 310% |
| Berkeley 隔離 PT (APEC 2025) | 查無 | 查無 | 查無 | **>97% 寬範圍，峰值 98.3%** | 查無 | 相對前人隔離 PT 方案損耗比降約 27× |
| PT 一般設計（引用值） | 查無 | 查無 | 查無 | 97.5% 峰值；>98% | **>40 W/cm³** | 〔S26〕 |

### 3.2 材料能力邊界

| 材料 / 模態 | Q（機械品質因數） | k 或 k² | 頻率 | 備註 | 來源 |
|---|---|---|---|---|---|
| LN 厚度剪切模（TS） | 3500 | k²t = **45%** | 5.94 MHz | 0.37 MHz 雜模抑制區 | S16 |
| LN 厚度伸張模（TE，無雜模） | 4000 | k²t = **30%** | 查無 | 62% 分數抑制帶寬 | S17 |
| 週期極化 LN（PPLN，2025/08） | 3187 | k² = 29% | 查無 | 宣稱功率諧振器中最佳 f·Q 積 | S18 |
| 單晶 AlN 晶圓 TE 模（2026/03） | 1677 | k² = **6.1%** | 查無 | **熱導率高出數量級**；接地環抑制雜模 | S19 |
| 硬質 PZT（商用） | 「數量級高於分立電感電容」 | 查無 | 493 kHz 級 | 徑向模最常用於 PR 轉換器 | S1, S13 |
| 無鉛 BNT 系（受體摻雜） | **>800 @ 0.25 m/s 振動速度** | 查無 | 查無 | 共振頻率漂移小 | S4 |
| Uchino 高功率材料 | 查無 | 查無 | 查無 | 振動速度 **>1 m/s**，功率密度為商用硬質 PZT 的 **10 倍** | S7 |

### 3.3 損耗與退化的物理極限

| 現象 | 數字 / 機制 | 來源 |
|---|---|---|
| Qm 崩塌門檻 | 低振動位準下 Qm 幾乎不變；**超過某一振動位準 Qm 急劇退化**，同時開始觀察到溫升 | S7 |
| 硬質 PZT 在 300 V/mm DC 偏壓下 | Qm **每 0.1 m/s 振動速度退化 17%**（軟質 PZT 更嚴重） | S7 |
| 離共振發熱主因 | 介電損（P-E 遲滯） | S7 |
| 共振發熱主因 | 機械損；源自非 180° 疇壁的不可逆運動 | S7 |
| 機械去極化 | 約 **10 MPa** 應力即發生機械去極化，影響 PZT 致動器壽命 | S5 |
| 熱去極化 / 降額 | 壓電陶瓷可安全使用至**約居里溫度的一半**；鐵電材料 **>700 °C 無法使用** | S28 |
| 散熱困難 | 「機械式儲能的本質阻止了傳統的散熱方式」 | S5 |
| 雜模 | 「雜散共振模態困擾低阻抗（即高功率）諧振體設計，限制工作負載範圍並降低效率」 | S5 |

### 3.4 成本與市場

| 項目 | 數字 | 年份 | 來源 |
|---|---|---|---|
| STEMINC 單層 PT（50 kHz, 2 W 級）零售 | **USD 23.76 / 2 顆 ≈ USD 11.88 / 顆** | 現行 | S10 |
| STEMINC 多層 PT 4 W / 6 W 零售價 | **查無**（頁面價格未被檢索回傳） | — | S11 |
| 同級電感/變壓器單價 | **查無可驗證報價**（搜尋僅得「客製磁性元件價格取決於量」的定性說法與 FRED 生產者物價指數，無單顆美元報價） | — | S29 |
| 壓電陶瓷變壓器市場 | USD **500M（2025）→ 950M（2033）**，CAGR 8% | 2025 | S29 |
| 壓電變壓器市場（另一家） | USD **220.5M（2025）→ 465.8M（2033）**，CAGR 9.8% | 2025 | S30 |
| 電感市場 | USD **5.1B（2022）→ 7.0B（2027）** | 2022 | S29 |
| CCFL 時代 PT 年銷量 | **>2,500 萬～3,000 萬顆/年**，主要產地日本 | 1990s–2000s | S3 |
| 冷電漿市場 | USD **2.92B（2024）→ 3.34B（2025）→ 11.14B（2034）**，CAGR 14.35% | 2024 | S31 |

> **市場數字互相矛盾的警告**：兩家市調機構對「壓電變壓器市場」給出 220M 與 500M（甚至還有一家給 1.2B）的差距，量級不一致。這類二手市調報告不可作為投資決策依據，僅供量級參考。無論取哪個數字，**PT 市場都只有電感市場的 3–10%**。

---

## 4. 「新能力型」應用機會

> 判準：客戶明確排除「用壓電諧振器取代電感做 DC-DC」。以下每個機會都標明**是否真的非替代性**。

### 4.1 強磁場 / 零 EMI 環境下的功率轉換（★ 最強的非替代性）

- **新能力是什麼**：在 1.5–7 T 的靜磁場中就地做電壓轉換與隔離。壓電元件的能量儲存在機械慣量與順度中，不依賴磁通，**原理上對外部磁場免疫**，且無磁芯即無磁通洩漏、無 EMI 輻射。
- **為什麼以前做不到**：文獻明指鐵磁變壓器與電感在 MRI 這類強外磁場中**會被外部磁場飽和**，造成損耗、過熱甚至損壞；未固定的電源供應器還會變成飛射物危害。傳統做法只能把電源放到磁場外、拉長線纜——這等於「不能做」，不是「做得比較差」。〔S8〕
- **是否真的非替代性**：**是。** 這不是「更小的電感」，而是磁性元件在此環境根本不可用。已有專利 US 10096764 針對「強外部磁場中 AC 線電轉隔離 DC」。SLAC CPAD 也把 PR DC-DC 列為高能物理探測器前端（強磁場 + 輻射 + 極低物質量預算）的候選架構。〔S8, S21〕
- **誰在做**：SLAC/CPAD（Nikolica 等，2023 Kickoff 與 2025 年會報告）；MRI 相容致動則有 Faulhaber 等的壓電馬達生態。
- **TRL**：3–4（實驗室原型 + 應用場景論證，未見輻射/磁場下的合格驗證數據）。
- **市場訊號**：CPAD 是 DOE 高能物理探測器儀器的協調機構，屬國家級計畫牽引；MRI 相容電子屬醫材高單價市場，能吸收壓電元件的高單價。
- **技術難點**：輻射硬化（PZT 在輻射下的極化穩定性**查無**公開數據）；低溫（探測器常在 −40 °C 至液氦區間，壓電常數與 Qm 溫度相依性大）；極低物質量（X₀）預算下的封裝。

### 4.2 元件本身即為放電電極的冷電漿源（★ 已商業化的非替代性）

- **新能力是什麼**：同一顆壓電體同時是「高壓產生器」與「放電電極」。TDK CeraPlas 以 12 Vpp 輸入直接在元件表面產生 20 kV 級電位並直接引燃常壓冷電漿，氣體溫度 <50 °C。這是壓電體「主動（產生高壓）＋被動（作為電極/介電層）」二用的教科書級案例。
- **為什麼以前做不到**：磁性高壓變壓器的輸出必須經由導線引到獨立電極，整個高壓迴路的雜散電容與體積使得手持、電池供電、8–18 W 級的常壓電漿裝置不可行。文獻明說「因為 PT 的緊湊與高效，這種電漿產生方式特別緊湊、高效且便宜」，且「PT 同時作為高壓產生器與放電電極」。〔S9, S32, S33〕
- **是否真的非替代性**：**是。** 功能合併（HV 源 = 電極）在磁性方案中沒有對應物。
- **誰在做**：TDK/EPCOS（CeraPlas）、relyon plasma（PiezoBrush PZ3、PDD® 商標）、LAPLACE Toulouse（Nadal 博論即此題）、日本學界（IOP PSST 上的 PT-DBD 臭氧產生器）。
- **TRL**：**9（已量產販售）**。
- **市場訊號**：冷電漿市場 2024 年 USD 2.92B → 2034 年預估 11.14B（CAGR 14.35%）；應用含表面活化改善接著/印刷、消毒滅菌、傷口癒合、食品去污。電漿產生效率報導可達 90%。〔S31, S32〕
- **技術難點**：壽命（電極表面即為陶瓷表面，長期受離子轟擊與臭氧侵蝕）；輸出高壓隨負載劇烈變化（TDK 明列「輸出最高 20 kV，負載相依」）；已有 TDK 這個強勢在位者，後進者要有差異化（例如更高功率、無鉛材料、可陣列化）。

### 4.3 毫克～克級的高壓源：微型機器人、離子推進、介電彈性體致動器

- **新能力是什麼**：把「數百 V～數 kV 高壓源」做進毫克級飛行體。2025 年 *Micromachines* 的「An Ion Discharge-Driven Thruster Based on a Lithium Niobate Piezoelectric Transformer」以 LN PT 作為離子放電推進器的高壓源，論文中所述飛行微型機器人達到**推重比 5.5**（此數字歸屬需注意，摘要語意可能指其對照或本體，標為**未驗證**）。〔S34〕
- **為什麼以前做不到**：DEA 需要 1–10 kV、壓電致動器需數百 V，而文獻明說這些電壓對多數微型機器人「不切實際」；繞線高壓變壓器無法微縮到毫克級（繞線匝數、磁芯體積、繞線電阻都不隨尺寸友善縮放）。LN PT 因「低阻尼、低彈性損、低電損與更高機電耦合」被指為做變壓器更有潛力的材料。〔S5, S34〕
- **是否真的非替代性**：**大致是。** 在 <1 g 的質量預算下，磁性升壓方案並非「比較差」而是不存在。但要誠實標註：目前微型機器人高壓驅動主流仍是「開關電容 + 分立電感」的 boost，屬於**部分替代性**。
- **誰在做**：LAPLACE Toulouse（PT 供電 MEMS 高壓）；上述 Micromachines 2025 論文團隊；Harvard 系微機器人高壓電子（毫克級高壓功率電子的既有文獻）。
- **TRL**：3–4。
- **市場訊號**：弱。微型機器人市場尚未成形；但 DEA / 電黏附 / 觸覺回饋（HV 驅動）在消費性觸覺與軟體機器人有中期潛力。
- **技術難點**：PT 輸出阻抗高、負載為容性（DEA 與壓電致動器都是電容），需要與容性負載共設計；能量回收（致動器電容上的能量需回收才有效率）；LN 的脆性與封裝。

### 4.4 密閉金屬穿透式供電＋通訊（同一顆換能器同時是被動聲學通道與主動感測器）

- **新能力是什麼**：不打孔即可對密閉金屬艙體內部供電與通訊。文獻數字：1.045 MHz 載波下能量傳輸效率 **60%**；用高阻抗超音波耦合膠可達 **34%**；實驗室通道可達 **>70% 效率並傳送 >100 W**；亦有「透過薄金屬壁傳遞 >1 kW」的實驗室展示。〔S35〕
- **為什麼以前做不到**：金屬壁是電磁屏蔽，感應式無線供電穿不過去；打孔則破壞氣密/耐壓/結構完整性。
- **是否真的非替代性**：**是（相對電磁 WPT）。** 但要誠實：這是超音波換能器的既有領域，與「壓電做主被動兩用元件」的重疊點在於「同一顆換能器同時承擔功率傳輸（被動通道）與資料/感測（主動）」，這部分才是新意。
- **誰在做**：多個學術團隊（MDPI Micromachines/Applied Sciences/Sensors 上的密閉金屬艙監測系統論文）；US 9503201「Acoustic-electric channel construction and operation using adaptive transducer arrays」顯示已有專利佈局。
- **TRL**：4–6（潛艇/壓力容器/核設施監測有實作案例）。
- **市場訊號**：中。石化壓力容器、核廢儲存、潛航器、密閉電池包監測。
- **技術難點**：耦合層（乾耦合 vs 膠）長期可靠度；自發熱（文獻明指 UPT 的介電與機械損造成自發熱顯著影響效率）；金屬壁厚度/溫度變化造成的聲學阻抗匹配漂移。

### 4.5 隔離型 PT 作為「電源＋隔離」二合一（部分替代性，權重調降）

- **新能力**：把隔離變壓器與功率級儲能合併成同一顆陶瓷，取得無磁性的隔離電源。Berkeley 2025 已做到 **峰值 98.3%、寬範圍 >97%**。〔S22〕
- **是否非替代性**：**否，主要是替代性。** 這是「更小/更薄的隔離變壓器」。
- **重要反證**：對 WBG 閘極驅動這個最誘人的目標，PT **物理上不合格**——文獻明指現行 PT「工作頻率低於數十 MHz、機械 Q 約 1000，導致固有頻寬只有數十 kHz，不足以支援 WBG 功率電子所需的次微秒級轉態」。因此 PT 只能做**隔離偏壓電源**，不能做隔離訊號通道。〔S36〕
- **另一反證**：現行商用高壓 PT **全部是非隔離型**。〔S26〕
- **TRL**：4（學術原型）。

### 4.6 壓電「主動電感」（明確為替代性，最低權重）

Berkeley（T. J. Skinner, M. Touhami, J. D. Boles，COMPEL 2024，"A Piezoelectric-Resonator-Based 'Active Inductor'"）提出用壓電體直接模擬磁性元件動態，作為 buck 轉換器中電感的 drag-and-drop 替代。〔S27〕
**是否非替代性：明確否。** 這條路的自我定位就是「取代電感」，正是客戶排除的路線。列出僅為完整性與競爭情報。

### 4.7 自感測 / 運動電流感測：同一顆 PR 同時是功率通道與狀態感測器（概念級）

已有工作提出以**運動電流（motional current）感測**做 PR-based DC-DC 的簡化閉迴路控制（arXiv 2605.15279），本質上是把諧振體當成自己的感測器。〔S12〕更廣義的「自感測致動器（self-sensing actuator）」文獻指出這能「以更低成本、更簡單構型做出緊湊裝置」。〔S37〕
**是否非替代性**：**中性。** 若能讓一顆 PR 同時輸出功率、回報溫度/應力/負載狀態（不需額外感測器與隔離），對高可靠度系統（航太、醫材）是有價值的整合能力；但目前僅是控制手段，尚無「感測輸出即產品規格」的案例。**TRL 2–3。**

---

## 5. 反面證據、失敗案例與物理上限

### 5.1 已經失敗過一次：CCFL

PT 唯一一次真正的量產是 CCFL 背光逆變器，年銷 2,500–3,000 萬顆；2000s 末 LED 背光取代 CCFL，PT 銷量持續下滑，**多數領導供應商停止高壓 PT 量產**。後續嘗試轉向螢光燈鎮流器、AC-DC 電池轉接器、LED 驅動器，但**未再造就等量級的出貨**。這證明 PT 的商業成功高度依賴單一 killer app，且該 app 可能整個消失。〔S3〕

### 5.2 「99% / 5.7 kW/cm³」的小字條款

同一段文獻在報導這個紀錄的同一句話裡就說：**「然而這些性能只在非隔離、且電壓轉換比溫和（2:1）的 DC-DC 轉換器中達成，把壓電式功率轉換的效用侷限在很窄的應用子集」**。任何以此數字做商業推演的計畫都必須先問：我的 VCR 是多少？要不要隔離？〔S13〕

### 5.3 諧振體功率密度 ≠ 轉換器功率密度

MIT 的 1.01 kW/cm³ 與 Stanford 的 1340 W/cm³ 都明確標為 **PR power handling density / resonator power density**，即**只算陶瓷體積**。開關、驅動 IC、飛輪電容、控制與散熱都不在分母內。用它跟「整機功率密度」比是不誠實的。〔S1, S2, S6〕

### 5.4 效率在高功率點崩塌

MIT 12 W 原型：理論 98.2%，**最高功率點 93.3%**。這 4.9 個百分點的落差正是非線性損耗、自發熱與雜模的實體代價。〔S1〕

### 5.5 物理上限清單

| 上限 | 內容 |
|---|---|
| 振動速度 | 超過門檻後 Qm 急劇退化並伴隨溫升；硬質 PZT 在 300 V/mm 偏壓下每 0.1 m/s 退化 17% Qm。Uchino 團隊的「>1 m/s」材料把功率密度推高 10 倍，但那是研究級材料，非市售品。 |
| 散熱 | 「機械式儲能本質上阻止了傳統的散熱方式」——諧振體必須在節點支撐才不破壞 Q，而節點支撐正是最差的熱通路。這是根本性的架構矛盾。 |
| 雜模 | 雜散共振「困擾低阻抗諧振體設計」，而低阻抗正是高功率所需 → **雜模是高功率化的直接障礙**。 |
| 溫度 | 安全使用溫度約為居里溫度的一半；鐵電材料 >700 °C 完全不可用。車規 150 °C / 工業 125 °C 的降額必須先算清楚。 |
| 機械 | 陶瓷脆性；約 10 MPa 應力即機械去極化；循環負載下裂紋成核與擴展導致疲勞失效；跌落/衝擊需靠軟性導電膠等封裝手段緩解。 |
| 電荷利用率 | 基線 PR DC-DC 的效率與電流處理能力**在高電壓轉換比時因拓樸強加的電荷利用限制而退化**——這正是 UCSD/CEA-Leti 用開關電容混成去補救的原因。 |
| 頻寬 | Q≈1000 且頻率 <數十 MHz ⇒ 固有頻寬僅數十 kHz。動態響應與 WBG 閘驅需求不相容。 |

〔以上分別對應 S5, S7, S28, S36〕

### 5.6 控制與系統層面的老問題（30 年未解）

- 驅動電路必須**追蹤共振頻率隨溫度、安裝應力、動態負載的漂移**。
- 部分無電感半橋 PT 拓樸**沒有負載調節能力**，且有 100 Hz 輸出調變。
- 負載快速變動時**有調節失穩與振盪的風險**；文獻直言「含壓電變壓器的電路不適合需要精確調節且具電氣隔離的直流電源，有輸出電壓崩潰的危險」。
〔S5〕

### 5.7 成本結構為何降不下來

粉末壓製 → 1250–1350 °C 燒結 → 機械加工（鋸/磨/拋/研）→ 電極（網印或濺鍍）→ 熱油浴數 kV/mm 極化 → **共振頻率量測分選**。窄頻元件需要 0.1% 頻率準確度，傳統製程良率「非常差」。〔S24〕
再加上：陶瓷後加工是逐片作業（非批次晶圓製程）、極化是慢製程、封裝需避開節點又要防潮防機械應力。這解釋了為什麼 STEMINC 一顆 2 W 級 PT 零售要 ~USD 11.88，而同功率的磁性元件在消費電子 BOM 裡通常是**分～角**的量級（**注意：後者本輪未取得可驗證報價，屬產業常識而非本文件已驗證事實**）。
**AlN/LN 的晶圓級製程是唯一可能改變成本曲線的方向**（可批次製造、可直接整合到矽上），但單晶 AlN 的 k² 只有 6.1%，遠低於 LN 的 30–45%，代表同樣功率需要更大面積或更高電壓。〔S13, S19〕

---

## 6. 未解問題（給下一輪研究）

1. **量產價格對比的硬數據**：1M pcs/yr 級、車規或工業規的 PT 單價 vs 同規格磁性元件單價。本輪只取得零售價 USD 11.88/顆，**這是最關鍵的缺口**。建議直接向 STEMINC、TDK、富士セラミックス、CTS、Noliac/CTS、APC International 詢價。
2. **CeraPlas 的單價與壽命規格**：TDK 型錄有電氣規格但本輪未取得單價與 MTBF/放電時數。Digi-Key 有掛牌，可直接查價。
3. **輻射與低溫下的壓電特性**：CPAD/HEP 路線的成敗完全押在這裡，本輪**查無**任何 PZT/LN 在 Mrad 級輻射或 <77 K 下的 Qm/k 數據。
4. **PT 隔離能力的實際規格**：耐壓 kV、局部放電起始電壓、爬電距離、UL/IEC 認證狀態——本輪**全部查無**。這決定 4.5 節的隔離路線是否有商業可能。
5. **1 kW/cm³ 是連續還是脈衝**？MIT 論文的熱穩態條件、環境溫度、有無散熱器，需要讀全文確認。
6. **「同一顆元件同時做兩件事」的幾何衝突**：功率轉換最佳的諧振體幾何（低阻抗、高 Q、單一乾淨模態）與致動/感測最佳幾何（大位移、寬頻）是否根本互斥？這是本專案的核心技術風險，本輪未找到直接研究。
7. **日本與中國大陸是否真的退場**：本輪日文/中文檢索均未找到 2023–2026 的壓電功率轉換研究群，但這可能是搜尋引擎覆蓋問題而非事實。建議查 電気学会（IEEJ）研究会資料、日本音響学会、中國電源學會論文集。
8. **US 11716023 與 US 10096764 的受讓人**：本輪未能確認，需查 Google Patents / Justia 原始頁面。
9. **Nature Communications 2026 的「A hybrid piezoelectric resonator-based DC-DC converter」全文**：本輪因 403 無法讀取，這是最新的一手成果，優先補讀。

---

## 7. 來源清單

| # | 標題 | URL | 說明 |
|---|---|---|---|
| S1 | A Piezoelectric-Resonator-Based DC–DC Converter Demonstrating 1 kW/cm³ Resonator Power Density (IEEE TPEL) | https://ieeexplore.ieee.org/document/9931991 | MIT 275→150 V/12 W/493 kHz/1.01 kW/cm³；理論 98.2%、實測最高功率點 93.3% |
| S2 | Juan Rivas-Davila's research works (ResearchGate 彙整頁) | https://www.researchgate.net/scientific-contributions/Juan-Rivas-Davila-2114714953 | Stanford 180→60 V/89 W/97%/1340 W/cm³ 的來源；同頁另提 3.2 kW/97.9% 之說（未驗證是否為壓電方案） |
| S3 | Piezoelectric Transformers: An Historical Review (Actuators, MDPI) | https://www.mdpi.com/2076-0825/5/2/12 | CCFL 時代年銷 2,500–3,000 萬顆、產地日本、LED 取代後供應商退場 |
| S4 | Characterization of high-power mechanical quality factor of piezoelectric ceramic discs under self-heating condition | https://www.sciencedirect.com/science/article/pii/S2238785423003836 | 自發熱下 Qm 特性；無鉛 BNT Qm>800 @0.25 m/s |
| S5 | Piezoelectric resonators in DC-DC converters: current status and limits (Power Electronics News) | https://www.powerelectronicsnews.com/piezoelectric-resonators-in-dc-dc-converters-current-status-and-limits/ | 雜模、散熱、電荷利用率、負載調節、控制穩定性等限制的集中出處（本文件未能 WebFetch，內容取自搜尋摘要） |
| S6 | jpTPEL2022Boles_HighPRDensity (MIT PER 全文 PDF) | https://per.mit.edu/wp-content/uploads/2023/10/jpTPEL2022Boles_HighPRDensity_FINAL.pdf | S1 的作者版全文 |
| S7 | Loss mechanisms and high power piezoelectrics (J. Mater. Sci.) / High Power Piezoelectric Materials (Penn State) | https://link.springer.com/article/10.1007/s10853-005-7201-0 | Uchino 的振動速度 >1 m/s、Qm 退化 17%/0.1 m/s、離共振 vs 共振發熱機制 |
| S8 | US 10096764 — Application of piezo technology to convert AC line power to isolated DC power in high external magnetic fields | https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/10096764 | 強磁場中磁性元件飽和、飛射物危害、壓電方案的專利主張 |
| S9 | Cold plasma from a single component (TDK Electronics) | https://www.tdk-electronics.tdk.com/en/373562/tech-library/articles/applications-cases/applications-cases/cold-plasma-from-a-single-component/1109546 | CeraPlas 原理：12–24 Vpp 輸入、最高 20 kV 輸出、雙區塊材料 |
| S10 | STEMINC Single Layer Piezo Electric Transformer 50 kHz (SMSTF50P2S6) | https://www.steminc.com/PZT/en/single-layer-piezo-electric-transformer-50-khz | 零售價 USD 23.76 / 2 顆 ≈ 11.88/顆 |
| S11 | STEMINC Multilayer Piezo Transformer 55 kHz 4W (SMMTF55P4S80) | https://www.steminc.com/PZT/en/multilayer-piezo-transformer | 多層 PT 產品線；價格未取得 |
| S12 | Motional-Current-Sensing Method and Simplified Closed-Loop Control Strategy for PR-based DC-DC Converters (arXiv 2605.15279) | https://arxiv.org/pdf/2605.15279 | 以運動電流做自感測式閉迴路控制 |
| S13 | Piezoelectric Transformers For Power Conversion (UC Berkeley 技轉，NCD 33842) | https://techtransfer.universityofcalifornia.edu/NCD/33842.html | 「99% 功率級效率、5.7 kW/cm³」但僅限非隔離 2:1 VCR 的關鍵限制陳述；多埠 PT 的隔離潛力 |
| S14 | ISSCC: Piezoelectric energy transfer in dc-dc converter (Electronics Weekly) | https://www.electronicsweekly.com/news/research-news/isscc-piezoelectric-energy-transfer-in-dc-dc-converter-2024-02/ | DSPPR 拓樸、Ø20 mm×200 µm 諧振體、與兩級 2:1 開關電容混成 |
| S15 | UCSD and CEA-Leti Report First IC for Piezoelectric Resonator DC-DC Conversion Achieving a 310% Loss Reduction (CEA-Leti 新聞稿) | https://www.leti-cea.com/cea-tech/leti/english/Pages/What's-On/Press%20release/ISSCC-2024-papers.aspx | ISSCC 2024 論文標題、310% 損耗降低、VCR<0.125 |
| S16 | Near-Spurious-Free Lithium Niobate Resonator for Piezoelectric Power Conversion with Q of 3500 and k²t of 45% (Stanford SUPERLAB) | https://superlab.stanford.edu/publication/2022-10-10-IUS_Nguyen/index.html | LN TS 模 Q 3500 / k²t 45% @ 5.94 MHz |
| S17 | Spurious-Free Lithium Niobate Bulk Acoustic Resonator for Piezoelectric Power Conversion (arXiv 2308.13902) | https://arxiv.org/abs/2308.13902 | LN TE 模 Q 4000 / k²t 30% / 62% 抑制帶寬 |
| S18 | Periodically Poled Piezoelectric Lithium Niobate Resonator for Piezoelectric Power Conversion (arXiv 2508.09407) | https://arxiv.org/abs/2508.09407 | PPLN k² 29% / Q 3187 / SOTA f·Q |
| S19 | Single-Crystal AlN Wafer-Based Bulk Acoustic Resonators for Piezoelectric Power Conversion (arXiv 2603.19409) | https://arxiv.org/abs/2603.19409 | AlN Q 1677 / k² 6.1%；熱導率高數量級；接地環抑制雜模 |
| S20 | 圧電トランス メーカー6社 注目ランキング (Metoree) | https://metoree.com/categories/3997/ | 日本現存 PT 相關廠商清單（タムラ製作所、NT販売、富士セラミックス） |
| S21 | DC-DC Converters Using New Materials and Architectures (CPAD, SLAC Indico) | https://indico.slac.stanford.edu/event/8288/contributions/7679/attachments/3653/9997/CPAD_DCDC_Nikolica_20231109_v1.pdf | 高能物理探測器前端的 PR DC-DC 應用論證 |
| S22 | High-Efficiency Isolated Piezoelectric Transformers for Magnetic-less DC-DC Power Conversion (IEEE APEC 2025) | https://ieeexplore.ieee.org/iel8/10977026/10977027/10977397.pdf | Berkeley 隔離 PT：>97% 寬範圍、峰值 98.3%、~27× 損耗比降低 |
| S23 | US 12009746 / US 12388364 — DC-DC converter based on piezoelectric resonator | https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/12009746 | MIT 受讓；Perreault/Boles/Piel；soft-charging 切換序列權利主張 |
| S24 | Piezoelectric Manufacturing Technology (CTS Corp) | https://www.ctscorp.com/Resources/Blog/Piezoelectric-Ceramics-Manufacturing-Technology | 壓製 1 MN、燒結 1250–1350 °C、電極、油浴數 kV/mm 極化 |
| S25 | CeraPlas Element — Piezoelectric Based Cold Plasma Generator (TDK 產品資料) | https://www.tdk-electronics.tdk.com/download/2307712/39eb3392c71d1191b103aa31c6a0f1c5/ceraplas-db.pdf | 47.3×20×20 mm、52 kHz、8 W、12 Vpp、最高 20 kV、氣溫 <50 °C |
| S26 | Design of High-Performance Piezoelectric Transformer-Based DC-DC Converters (MIT 碩論, Elaine Ng, 2022) | https://dspace.mit.edu/bitstream/handle/1721.1/147567/Ng-elaineng-meng-eecs-2022-thesis.pdf?sequence=1&isAllowed=y | PT 峰值 97.5%、>40 W/cm³ @>98%；商用 PT 僅 LCD 背光且皆非隔離 |
| S27 | A Piezoelectric-Resonator-Based "Active Inductor" (IEEE COMPEL 2024) | https://ieeexplore.ieee.org/document/10614003 | Skinner/Touhami/Boles；壓電體直接模擬電感動態（明確替代性路線） |
| S28 | Thermal Degradation and Aging of High-Temperature Piezoelectrics (Univ. of Kentucky 學位論文) | https://uknowledge.uky.edu/cgi/viewcontent.cgi?article=1568&context=gradschool_theses | 居里溫度一半的降額規則、熱去極化、>700 °C 不可用 |
| S29 | Piezoelectric Ceramic Transformers Insights: Market Size Analysis to 2033 (Data Insights) | https://www.datainsightsmarket.com/reports/piezoelectric-ceramic-transformers-1664155 | PT 陶瓷市場 500M(2025)→950M(2033)；同段引用電感市場 5.1B(2022)→7.0B(2027) |
| S30 | Piezoelectric Transformers Market: 465.80 million by 2033 (Future Market Report) | https://www.futuremarketreport.com/industry-report/piezoelectric-transformers-market | 另一組互相矛盾的市場數字：220.5M(2025)→465.8M(2033), CAGR 9.8% |
| S31 | Cold Plasma Market Sizing (Towards Healthcare) | https://www.towardshealthcare.com/insights/cold-plasma-market-sizing | 冷電漿 2.92B(2024)→3.34B(2025)→11.14B(2034), CAGR 14.35% |
| S32 | Piezoelectric direct discharge plasma (Wikipedia) | https://en.wikipedia.org/wiki/Piezoelectric_direct_discharge_plasma | PDD 定義、電漿產生效率約 90%、氣體溫度 <50 °C |
| S33 | Discharge plasmas generated by piezoelectric transformers and their applications (Plasma Sources Sci. Technol., IOP) | https://iopscience.iop.org/article/10.1088/0963-0252/15/2/S07 | PT 同時作為高壓產生器與放電電極的原始論證；PT-DBD 臭氧產生器 |
| S34 | An Ion Discharge-Driven Thruster Based on a Lithium Niobate Piezoelectric Transformer (Micromachines 16(3):277, 2025) | https://doi.org/10.3390/mi16030277 | LN PT 作為離子推進器高壓源；LN 低阻尼低損高耦合的材料論證 |
| S35 | An Ultrasonic Through-Metal-Wall Power Transfer System with Regulated DC Output (Applied Sciences, MDPI) | https://mdpi.com/2076-3417/8/5/692/htm | 穿金屬壁供電：1.045 MHz 下 60%、乾/膠耦合 34%、>70% 且 >100 W、>1 kW 實驗室展示 |
| S36 | Microwave-acoustic-based isolated gate driver for power electronics (arXiv 2511.13412) | https://arxiv.org/pdf/2511.13412 | 明確指出現行 PT 因 f<數十 MHz、Q≈1000 導致頻寬僅數十 kHz，不足以驅動 WBG |
| S37 | A Self-Sensing Piezoelectric Actuator for Collocated Control | https://www.researchgate.net/publication/258152358_A_Self-Sensing_Piezoelectric_Actuator_for_Collocated_Control | 自感測致動器：同一元件兼作感測器可降低成本與簡化構型 |
| S38 | Overtone Piezoelectric Resonator For Power Conversion (UC Berkeley 技轉, NCD 33625) / Active Inductor (NCD 33585) | https://techtransfer.universityofcalifornia.edu/NCD/33625.html | Berkeley 掛牌可授權的壓電功率技術清單 |

---

### 附註：對客戶決策的一句話建議

若目標真的是「非替代性新能力」，本領域的重心應該從「壓電體能不能替代電感」**移開**，改為問：**「有沒有一種系統，它的功率轉換元件同時必須是電極、必須是致動器、必須不含磁性材料、或必須做到毫克級？」** 第 4.1（強磁場/零 EMI）與第 4.2（元件即電極的冷電漿）是本輪查證中唯二**物理上非替代**且已有實證的方向，其中 4.2 已經 TRL 9 且有 TDK 這個在位者，4.1 則 TRL 3–4 但無明顯在位者——**這個組合值得下一輪深挖。**
