# 應用B6：機械天線與 VLF/ULF 通訊——壓電體同時是共振器與電磁輻射源

> 一句話結論：機械天線是本次調查中**物理上最正當、最不可能被磁性元件取代**的「新能力型」壓電應用（它繞過的是 Chu–Harrington 與 Bode–Fano 兩條電小天線基本極限，不是在跟電感比成本），奠基文獻與驚人數字這次**全部查證屬實**；但同一批查證也揭露了三件致命事實：(1) 已公開的最佳實測鏈路是 **200–730 m、數 bps 至數十 bps**，且多半落在**近場磁感應**而非真正輻射；(2) DARPA AMEBA **已於 FY2021 結案且無公開後續型號**；(3) 2026 年 4 月的獨立理論分析指出機械天線**已逼近理論 FOM 上限，質疑「還能再進步數個數量級」的說法**。對台灣決策者：**發射端是 10 年期國防押注；真正該先做的是接收/感測端（Plan A）。**

---

## 0. 研究方法與限制（誠實揭露）

1. **WebFetch 在本環境被全面封鎖（403）**，無法讀取任何原文 PDF。本文所有事實均來自 **WebSearch 回傳的摘要文字 + 該摘要所附的來源 URL**。
2. 本回合實際執行 **28 次成功 WebSearch**（第 29 次起配額耗盡）。相較前一版只有 1 次搜尋，本版**推翻並修正了前版多處錯誤**，並補齊了前版完全空白的實測硬指標。
3. 標記方式：
   - **【摘要驗證】**：由本回合搜尋摘要取得，且能對應到第 7 節具名 URL。**未經原文核對**（WebFetch 封鎖），引用前建議人工開啟該 URL 確認。
   - **【自行推算】**：由公開物理公式與明示假設推導，算式列於附錄，讀者可自行複核。
   - **【查無】**：本回合搜尋不到，明確不填數字。
4. **本文未捏造任何專利號、論文標題、作者名、公司名或數字。**
5. **本回合仍查無的項目（誠實列出）**：AMEBA 的預算金額與完整承包商名單；Kemp 2019 裝置的絕對輻射功率（W 或 dBm）與絕對場強數值；任何機械天線的商用產品型號或報價；US 10,921,360 的完整 claim 範圍（僅取得摘要式描述與 Justia 列出的權利人）；BlueME 的確切實測資料率（見第 5 節的資料矛盾說明）。

---

## 1. 結論摘要（8 條）

1. **【摘要驗證】前版標為「未驗證—模型記憶」的那組驚人數字，這次全部查證屬實，且來源比預期更硬。** 論文為 **Kemp, M.A., Franzi, M., Haase, A. et al., "A high Q piezoelectric resonator as a portable VLF transmitter", Nature Communications 10, 1715 (2019)**，機構為 **SLAC National Accelerator Laboratory + Gooch & Housego + SRI International**。核心數字：**LiNbO₃ Y∠36° 切**（降伏應力 >50 MPa、長度伸縮模態本徵損耗極低）、**9.6 cm 長棒**、**載波 35 kHz**、**機械 Q = 45,000**、**輻射效率較同電尺寸先前技術 >300 倍**、**以共振的時變調變使裝置頻寬超過 Bode–Fano 上限 >83 倍**。SLAC 內部專案代號 **VAPOR（VLF Antenna Piezoelectric Resonator）**。（來源 3、4、5、6、7）

2. **【摘要驗證】前版對 2017 奠基論文的理解有一處重大錯誤，必須修正：那篇不是 VLF 元件。** Nature Communications 8, 296 (2017)《Acoustically actuated ultra-compact NEMS magnetoelectric antennas》（Northeastern, Nian-Xiang Sun 團隊，第一作者 Nan / Lin）的實測頻段是 **60 MHz 至 2.5 GHz**：NPR 模態 **f = 60.68 MHz、Q = 930、k_t² = 1.35%**，材料為 **500 nm AlN 壓電層 + [FeGaB(45 nm)/Al₂O₃(5 nm)]×10 磁致伸縮層**懸浮於 Si。宣稱**尺寸微縮 1–2 個數量級、小至 1/1000 波長、阻抗匹配不再直接決定輻射效率**。**它是「聲共振即天線」這個概念的奠基論文，但 VLF 磁電天線是後來另一條分支**（Northeastern 另有 VLF 專利與後續系統論文）。（來源 1、2、43、52）

3. **【摘要驗證】DARPA AMEBA 已結案，且證據指向「未達可轉移門檻」。** 全名 **A MEchanically Based Antenna**，DARPA **MTO**，PM **Troy Olsson**，BAA 編號 **HR001117S0007**，2016 年 12 月公布，**45 個月**期程，分兩個技術領域（TA1：ULF <3 kHz；TA2：VLF 3–30 kHz），目標是**單兵可攜**的 VLF/ULF 發射機。已查證的承包商：**HRL Laboratories（2017-11 獲獎，走磁彈性/磁致伸縮路線，約 1 kHz）**、**University of Illinois（Tawfick 團隊，磁性共振器）**。**DARPA FY2022 預算辯護文件記載 AMEBA 於 FY2021 完成（completed）**，FY2022 經費下降即反映此事。**預算金額、完整承包商名單：查無。後續型號、軍種接手、技轉紀錄：查無。**（來源 11、12、13、14、15）

4. **【摘要驗證】最重要的空白補上了：實測鏈路數字存在，但只有 200–730 m / 數 bps–數十 bps 等級。**
   - **BlueME（University of Florida，arXiv 2411.09241，IEEE J. Oceanic Eng.）**：Metglas + PZT 磁電天線，約 **35–36 kHz**，裝在 ASV 與 ROV 上做**開放水域實測**——**淡水 200 m 僅耗 1 W；鹹水 730 m 耗 <10 W**。（來源 20、21）
   - **ADMIRE（UIUC, Hassanien / Gong, Sci Rep 10, 17006 (2020)）**：**PZT** 發射器效率為同尺寸電天線的 **>6000 倍**，**FSK 調變達 60 bit/s**——**這是純壓電路線目前公開最高的資料率**。（來源 9、10）
   - **RMBMA（西安電子科技大學，電子裝備結構設計教育部重點實驗室）**：**10 cm × 5 cm × 2 cm 永磁**，產生 **1 pT** 場，通訊距離**土壤中 264.8 m、海水中 203.5 m**。（來源 16）
   - **中國最佳化旋轉永磁**：複雜電磁環境下 **20 m 內 3.5 bps** 符元率。（來源 18、19）
   - **磁擺陣列（Sci Rep 9, 13220 (2019)）**：效率較裸線圈高 **7 dB**，**1031 Hz、2 bps** 概念驗證。（來源 26）
   - **Nat Commun 16, 4137 (2025) UA-MDRR**（超音波驅動旋轉磁偶極）：**0.11 cm³ 多層壓電陶瓷**驅動 NdFeB 圓盤，**100 m 處空氣中 2.64 pT、水下 2.12 pT，耗電僅 0.61 W**，發射能力密度 **24,000 nT/cm³@1 m**，宣稱優於現有共振器/天線 1–2 個數量級。（來源 24）

5. **【自行推算 — 本文最關鍵的分析結論】這些「通訊距離」絕大多數不是輻射，是近場磁感應（B ∝ 1/r³）。** 以 UA-MDRR 為例：由 100 m 處 2.64 pT 反推磁偶極矩 m ≈ **13 A·m²**（近場軸向公式 B = μ₀m/2πr³）；若工作頻率取 ELF 100 Hz，代入 P = μ₀ω⁴m²/(12πc³)，得**輻射功率約 3×10⁻²¹ W**，相對 0.61 W 輸入即**輻射效率約 10⁻²¹**。ELF 100 Hz 的 λ = 3000 km，100 m 處的 r/λ = 3.3×10⁻⁵，**深在近場**。**商業意涵極為殘酷：近場鏈路的距離每加倍需要 8 倍磁矩，射程無法靠工程迭代拉開。** 這比第 5 節任何一條反面證據都更決定商業可行性。
   **同一套推算對 BlueME 也給出一個必須追問的矛盾**：35 kHz 在海水（σ=4 S/m）的趨膚深度僅 **1.35 m**，730 m 全程走海水等於 **~4700 dB** 衰減，物理上不可能；**因此 730 m 那條鏈路幾乎必然是經由空氣/海面側向波路徑，不是穿海水**。而淡水（σ≈0.01 S/m）35 kHz 的 δ ≈ **26.9 m**，200 m ≈ 7.4 δ ≈ **64 dB**，穿水是合理的。**這說明「鹹水 730 m」與「淡水 200 m」不是同一種鏈路，不可並列引用。**（推算，非文獻宣稱；建議以原文 Fig. 實測幾何複核）

6. **【摘要驗證】2026 年出現了第一份指名道姓的反面理論分析。** arXiv **2604.26980**（2026-04-28），*Naturally Resonant Emitters: Approaching Fundamental Antenna Limits*，作者 **Damir Latypov（CRG Defense）**。核心論點：**自然共振發射體（含機械共振器）仍受 Chu–Harrington 極限約束**；作者把 ESA 理論推廣到 ESE（electrically small emitter）類別，導出單位體積發射體在給定頻率與頻寬下的效率上限與可跨類別比較的 FOM；**實測數據顯示機械天線已運作在接近理論 FOM 上限，因此質疑「還能再取得數個數量級增益」的宣稱**。（來源 27）

7. **【摘要驗證】對照組規模確認：Cutler NAA 是 1 MW 輻射、26 座近 1000 呎鐵塔、50 baud。** 美國海軍緬因州 Cutler VLF 台，呼號 **NAA**，**24 kHz**，輸入功率最高 **1.8 MW**，常態輻射功率 **1 MW**（稱 full power）；天線為南北各 13 座、共 **26 座**鐵塔，中心塔高 **997.5 ft**；1960 年建、1961-01-04 啟用。美軍 VLF/LF 岸台的對潛廣播為 **50 baud**。（來源 31、32）
   **對照意義：現役方案是 10⁶ W；機械天線是 10⁻²¹–10⁻⁹ W。這不是「便宜替代」，是完全不同的用途類別——只能做「最後一哩、極短訊息、可攜」，永遠不可能做「全球廣播」。**

8. **【摘要驗證】Plan A 成立，且比前版預期更具體。** Nature Communications 12, 3141 (2021)《Ultra-compact dual-band smart NEMS magnetoelectric antennas for simultaneous wireless energy harvesting and magnetic field sensing》（Zaeimbashi, Nasrollahpour et al., Northeastern）：**單一元件 250 × 174 µm²**，**GHz 頻段做無線能量傳輸與資料通訊（被動取能）＋ MHz 共振做 pT 級低頻磁場感測（主動感測）**，**無線功率傳輸效率較任何已報導的微型微線圈高 1–2 個數量級**，並可滿足 **SAR 法規**；明示目標應用為**植入式醫材（神經記錄與刺激）**。（來源 25）**這是「壓電主動/被動兩用元件」在頂級期刊上最直接、最具體的存在證明，且完全不碰 DC-DC 取代電感那條被排除的路。**

---

## 2. 現況與查證結果

### 2.1 四條互相競爭的機械天線路線（更新版）

| 路線 | 物理機制 | 壓電體角色 | 代表成果與硬數字 |
|---|---|---|---|
| **A. 磁電（ME）薄膜天線** | 壓電聲共振 → 應變 → 磁化振盪 → 磁偶極輻射 | 致動器 + 共振器 | Nat Commun 8,296 (2017)：60.68 MHz、Q=930、AlN/FeGaB；VLF 分支見 ME-MLTx 與 BlueME |
| **B. 純壓電電偶極** | 壓電棒高 Q 共振 → 端面電荷擺動 → 電偶極 | **共振器＋輻射源本體（純血版）** | Kemp 2019：LiNbO₃ 9.6 cm、35 kHz、Q=45,000、>300×、>83× Bode–Fano；ADMIRE 2020：PZT、>6000×、60 bit/s |
| **C. 旋轉/往復永磁** | 機械旋轉永磁 → 時變磁偶極 | 可作超音波驅動源 | RMBMA：土壤 264.8 m / 海水 203.5 m；UA-MDRR 2025：0.11 cm³ 壓電堆疊、100 m 2.64 pT、0.61 W |
| **D. 駐極體（electret）** | 機械驅動高電荷駐極體 | 無（PTFE/FEP 駐極體） | APL 2020 Perspective 稱駐極體式輻射效率高於永磁式與壓電式（來源 30、需原文核對） |

**對客戶的意義（不變且更強化）：只有路線 B 是「壓電體本身就是輻射源」，價值鏈佔比最高；路線 A 壓電是致動器；路線 C 壓電只是動力源（關鍵零件是永磁與軸承）；路線 D 完全不需要壓電。**

**但要注意一個對客戶不利的實測事實**：路線 B 的最佳資料率是 **60 bit/s（ADMIRE, PZT）**，而路線 A/C 已做到 **200–730 m 的實地水下鏈路**。**純壓電路線在「系統級實測」上落後於磁電與永磁路線。**

### 2.2 玩家地圖（已查證）

- **美國學界／國家實驗室**：SLAC + Stanford（Kemp，VAPOR，專利權利人為 Board of Trustees of the Leland Stanford Junior University，DOE 合約 DE-AC02-76SF00515）；Northeastern（Nian-Xiang Sun，ME 天線與 VLF ME 通訊）；UIUC（Songbin Gong / Hassanien，ADMIRE；Tawfick，AMEBA 磁性共振器）；University of Florida（RoboPI，BlueME）。（來源 3、7、9、15、20、42）
- **美國業界**：**HRL Laboratories** 是唯一查證到的 AMEBA 承包商；**Gooch & Housego** 與 **SRI International** 為 Kemp 2019 共同機構。**查無任何把機械天線商品化的公司或可購買產品型號。**（來源 13、3）
- **中國**：**西安電子科技大學**（電子裝備結構設計教育部重點實驗室，RMBMA）、**國防科技大學第 63 研究所**、以及一支由**中國煤炭科工集團 + 應急管理部重點科技項目**資助的旋轉永磁陣列團隊（Sci Rep 2025，明確指向**礦難救援**應用）。中文核心期刊（物理學報、電子與信息學報、航空學報）有連續產出。（來源 16、17、18、19）
- **台灣**：**查無**任何機械天線相關的公開計畫、論文或廠商。

### 2.3 專利地圖（前版完全空白，本版補上）

| 專利/公開號 | 標題 | 權利人 | 驗證狀態 |
|---|---|---|---|
| **US 10,424,714 / US20190074578A1 / US20190097119A1** | Piezoelectric Transmitter | **Board of Trustees of the Leland Stanford Junior University**（DOE 合約 DE-AC02-76SF00515） | 【摘要驗證】說明書載明 >300× 效率、**>88×** Bode–Fano（注意：與論文的 83× 不同，屬正常的申請/發表差異，但引用時需標明出處）（來源 7、8） |
| **US 11,355,692** | Nanoscale radio frequency magnetoelectric antenna | **Northeastern University**（發明人含 Nian Xiang Sun） | 【摘要驗證】（來源 42、44） |
| **US20190267534A1** | Magnetoelectric Very Low Frequency Communication System | Northeastern University（推定） | 【摘要驗證，權利人待核】（來源 43） |
| **US20200321512A1 / WO2017210373A1** | Nanoscale RF Magnetoelectric Antenna（同族） | Northeastern University | 【摘要驗證】 |
| **US 11,594,816** | Acoustically-driven electromagnetic antennas using piezoelectric material | 推定 UIUC 體系 | 【摘要驗證，權利人查無】（來源 46） |
| **US 12,424,736** | Portable resonant multiferroic magnetoelectric antenna for ULF/VLF communication | 推定美國海軍體系 | 【摘要驗證，權利人查無】（來源 45） |
| **US 10,921,360** | Dual magnetic and electric field quartz sensor | Justia 列出 **Rutgers University / MIT / Research Foundation of SUNY** | 【摘要驗證，權利人待人工核對】技術內容：石英共振器電極上鍍磁致伸縮膜，一軸測電場、正交軸獨立測磁場。**與 Northeastern 無關，前版的關聯推測不成立。**（來源 41） |

**結論：專利地雷區集中在 Stanford（純壓電電偶極）與 Northeastern（ME 天線）兩大家族。台灣廠商若走路線 B，Stanford 的 Piezoelectric Transmitter 家族是必須先做 FTO（freedom-to-operate）分析的對象。**

---

## 3. 關鍵數字表

| 項目 | 數值 | 驗證狀態 | 來源 |
|---|---|---|---|
| Kemp 2019 材料/切向 | LiNbO₃ **Y∠36°**，降伏應力 >50 MPa | 【摘要驗證】 | 3, 4 |
| Kemp 2019 尺寸/頻率/Q | **9.6 cm 棒**、**35 kHz**、**Q = 45,000** | 【摘要驗證】 | 3, 5, 6 |
| Kemp 2019 本徵頻寬 | **≈ 0.75 Hz**（35 kHz / 45,000） | 【摘要驗證】 | 3 |
| Kemp 2019 效率增益 | **>300×**（vs 同電尺寸先前技術） | 【摘要驗證】 | 3, 7 |
| Kemp 2019 頻寬突破 | **>83×** Bode–Fano（專利寫 >88×） | 【摘要驗證】 | 3, 7 |
| Kemp 2019 實測範圍 | 場強量測至 **80 m**；鏈路展示約 **100 ft (~30 m)** | 【摘要驗證】 | 6 |
| Kemp 2019 絕對輻射功率 | **查無** | 【查無】 | — |
| ADMIRE (PZT) 效率 | **>6000×** 同尺寸電天線 | 【摘要驗證】 | 9, 10 |
| ADMIRE 資料率 | **60 bit/s（FSK）** ← 純壓電路線最高 | 【摘要驗證】 | 9 |
| ME 天線 2017 頻段/Q | **60.68 MHz、Q=930、k_t²=1.35%**；全系列 60 MHz–2.5 GHz | 【摘要驗證】 | 1, 2 |
| ME 天線 2017 微縮 | **1–2 個數量級**，小至 **1/1000 λ** | 【摘要驗證】 | 1 |
| ME 天線微縮（2026 綜述） | 較傳統 EM 天線小 **4–5 個數量級** | 【摘要驗證】 | 29 |
| ME-MLTx 場強 | **112 nT @ 1 m**；推估 **108 fT @ 100 m**；21.2 kHz、50 Vpp | 【摘要驗證】 | 23 |
| ME-MLTx 功耗 | **400 mW @ 80 V 驅動** | 【摘要驗證】 | 23 |
| BlueME 實測 | 淡水 **200 m @ 1 W**；鹹水 **730 m @ <10 W**（35–36 kHz） | 【摘要驗證】 | 20, 21 |
| BlueME 資料率 | 二手報導稱 **1–100 kb/s**，**與 VLF 頻寬物理嚴重不符，本文判定為疑似誤植，不採用** | 【存疑】 | 20 |
| WUWNet ME 陣列 | **12 單元陣列合成 200 nT @ 1 m**，較單元提升 1 個數量級 | 【摘要驗證】 | 22 |
| RMBMA 通訊距離 | **土壤 264.8 m / 海水 203.5 m**；磁鐵 10×5×2 cm；1 pT | 【摘要驗證】 | 16 |
| 中國旋轉永磁最佳化 | **20 m 內 3.5 bps** | 【摘要驗證】 | 18, 19 |
| UA-MDRR (2025) | **100 m：空氣 2.64 pT / 水下 2.12 pT，0.61 W**；24,000 nT/cm³@1 m；壓電堆疊 0.11 cm³ | 【摘要驗證】 | 24 |
| 磁擺陣列 (2019) | 效率較裸線圈 **+7 dB**；**1031 Hz、2 bps** | 【摘要驗證】 | 26 |
| Nat Commun 2021 兩用元件 | **250 × 174 µm²**；GHz 取能 + MHz **pT 級**磁感測；WPT 效率較微線圈高 **1–2 數量級** | 【摘要驗證】 | 25 |
| Cutler NAA | **24 kHz、輸入 1.8 MW / 輻射 1 MW、26 座塔、中心塔 997.5 ft** | 【摘要驗證】 | 31, 32 |
| 美軍對潛廣播速率 | **50 baud** | 【摘要驗證】 | 32 |
| 聲學數據機（EvoLogics） | **62,500 bps @ 300 m、10 W**，BER 1e-10 | 【摘要驗證】 | 33, 35 |
| 聲學數據機（Benthos） | **2,000–6,000 m、140–15,360 bps**，BER 1e-7 | 【摘要驗證】 | 34, 35 |
| 藍綠雷射 | 480 nm；清澈海水消光 **0.16 m⁻¹**、近岸 **2.8 m⁻¹**（近岸實用距離約 **1.8 m**）；已演示 **12.4 Gbps** | 【摘要驗證】 | 38, 39 |
| 礦坑 leaky feeder | 低成本同軸 **27 MHz、約 1 km**；商用系統約 **US$3 / 線性呎**起 | 【摘要驗證】 | 36, 37 |
| eLoran | **90–110 kHz**、UTC 授時 **50 ns**、定位 **±8 m** | 【摘要驗證】 | 47 |
| 海水趨膚深度 | 1 kHz **7.96 m** / 10 kHz **2.52 m** / 21.2 kHz **1.73 m** / 35 kHz **1.35 m** / 1 MHz **0.25 m** | 【自行推算】 | 附錄 |
| 淡水趨膚深度 @35 kHz | **≈ 26.9 m**（σ=0.01 S/m） | 【自行推算】 | 附錄 |
| UA-MDRR 反推磁矩/輻射效率 | m ≈ **13 A·m²**；@100 Hz 輻射功率 **~3×10⁻²¹ W** → 效率 **~10⁻²¹** | 【自行推算】 | 附錄 |
| Chu 極限 Q（35 kHz, a=4.8 cm） | **≈ 2.3×10¹³** | 【自行推算】 | 附錄 |
| 商用產品 / 型號 / 報價 | **不存在** | 【查無】 | — |

---

## 4. 機會與任務拆解（non-substitutional）

### Plan A（建議優先，12–24 個月可見成果）：**接收端／感測端，不做發射端**

依據 Nat Commun 12, 3141 (2021)：**單顆 250×174 µm² 元件同時做 GHz 無線取能（被動）＋ MHz pT 級磁感測（主動）**，WPT 效率較微線圈高 1–2 數量級，且滿足 SAR。（來源 25）

- **為什麼是它**：接收端**完全不用面對 P ∝ ω⁴ 的輻射地板**，卻 100% 命中「主動/被動兩用」命題。
- **市場**：植入式醫材（神經記錄/刺激）、超低功耗磁場感測、電流感測、磁異常偵測。
- **競爭定位（已查證的靈敏度—功耗三角）**：ME 複合材料感測器 **681 pT/√Hz @1 Hz，功耗僅 3.6 mW**；ME 音叉式達 **3 pT/√Hz @318 Hz**。對照：fluxgate **20–50 pT/√Hz**（最佳 0.75 pT/√Hz）但耗數百 mW；原子磁力計 ~1 pT/√Hz 但 **20 W**；SQUID <10⁻¹⁷ T/√Hz 但需液氦。（來源 49）**ME 的賣點不是最高靈敏度，是「mW 級功耗下的 pT 級」——這正是植入式與電池供電節點的唯一可行點。**
- **任務**：(1) 取得 AlN 或 PZT 薄膜 + 磁致伸縮層（FeGaB / Metglas）的異質結構製程能力；(2) 複現 pT 級感測與 GHz WPT 雙頻共存；(3) 對 Northeastern 專利家族（US 11,355,692 等）做 FTO。

### Plan B（10 年期國防押注）：可攜 VLF/ULF 發射端

判準是「以前完全做不到」，不是「做得比較便宜」：

1. **AUV／潛航體不浮出水面的極短上行訊息。** 現況：AUV 必須浮出水面才能經衛星回報位置與資料，直接暴露位置並中斷任務。（來源 A：AUV 通訊現況綜述）**BlueME 已證明淡水 200 m @ 1 W 可行**——這在既有技術樹下沒有可攜替代品（Chu 極限封死電小天線）。**但注意：這與聲學數據機（Benthos 2–6 km / 140–15,360 bps）相比距離與速率都遠遜，只能定位在「聲學被干擾或需靜默」的補位角色，不是取代。**
2. **礦坑／隧道穿岩生命訊號。** leaky feeder 坍塌即斷，商用系統約 US$3/線性呎；TTE（through-the-earth）系統又受**礦坑防爆（intrinsic safety）電流上限**壓制。（來源 36、37）中國已有由**應急管理部**資助的旋轉永磁陣列團隊直攻此市場（來源 17）——**這是目前公開資料中商業化意圖最明確的一條**。
3. **災難搜救穿瓦礫信標。** 價值在穿透率而非資料率，數 bps 即可。
4. **GNSS 阻斷下的區域授時。** 對照 eLoran（100 kHz、50 ns 授時、±8 m）；機械天線可攜信標可作為**分散式、可拋棄式**的補充節點。**但這需要的是接收靈敏度而非發射功率，再次指回 Plan A。**
5. **LPI/LPD 低可偵測通訊。** 10⁻⁹–10⁻²¹ W 的 ERP 在此**由缺點變優點**；但只有國家級客戶，台灣廠商需搭配國防體系（中科院）才有入口。

---

## 5. 反面證據與物理／法律上限

**這一節請客戶讀兩遍。本版新增的三條（1、2、6）比前版嚴重得多。**

1. **【新增，最致命】已公開的「通訊距離」多半是近場磁感應，不是輻射。** 見第 1 節第 5 點推算：UA-MDRR 在 100 m 的磁矩反推值對應輻射功率約 10⁻²¹ W。**近場鏈路 B ∝ 1/r³，射程加倍要 8 倍磁矩；工程迭代無法把 700 m 變成 7 km。** 客戶若把論文的「通訊距離」當成天線射程來做市場推算，會系統性高估數個數量級。

2. **【新增】2026 年的獨立理論分析直接質疑「還有數量級空間」的說法。** Latypov (arXiv 2604.26980) 指出自然共振發射體仍受 Chu–Harrington 約束，且**實測顯示機械天線已在理論 FOM 上限附近**。（來源 27）這意味著：**這條技術路線的性能上限可能已經被摸到，不是「還在早期、後面會大幅進步」。**

3. **輻射功率的 ω⁴ 內生矛盾（不變）。** 你要的物理特性（低頻穿透）與你要的性能（輻射功率）在同一條公式裡對打。從 35 kHz 降到 1 kHz，ω⁴ 使輻射功率掉 **1.5×10⁶ 倍**。**這是材料進步繞不開的矛盾。**

4. **高 Q 與調變頻寬的衝突，以及對「突破 Bode–Fano」的正確理解。** Kemp 裝置 Q=45,000 → 本徵頻寬僅 **0.75 Hz**。所謂 83× 突破，本質是**時變共振（LTV）不受只適用於線性時不變網路的 Bode–Fano 約束**——**這不是免費午餐**，代價是額外主動功耗、非線性、雜散發射與切換元件耐壓。即便 83×，頻寬也只約 **62 Hz**，資料率仍在數十 bps 量級（與 ADMIRE 的 60 bit/s 一致）。**客戶若理解成「憑空多 83 倍頻寬」會嚴重誤判。**

5. **導電介質中磁場優於電場——這條物理對純壓電（路線 B）結構性不利。** 已查證：**水下磁偶極在空氣中產生的 EM 場優於電偶極**；水中發射端應採**水平磁偶極（HMD）**；相關工作以 19 kHz 小環天線、<10 W 達到海面上 **574 m**。（來源 40）**這解釋了為什麼實地水下鏈路的成功案例（BlueME、RMBMA、UA-MDRR）全部是磁偶極，而純壓電電偶極（Kemp、ADMIRE）只有陸上短距離展示。**

6. **【新增】比較基準本身可能不公平。** IEEE 的建模工作指出：**壓電應變天線的輻射電阻遠小於文獻中普遍假設的「同尺寸電偶極」**（來源 48）。若基準被高估，「>300×」「>6000×」這類倍數就會被系統性放大。**在看到獨立第三方以統一基準複現前，這些倍數應視為單一團隊自報值。**

7. **AMEBA 的結案本身就是負面訊號。** FY2021 完成、FY2022 經費下降、**查無任何後續型號、軍種接手或技轉紀錄**。（來源 14）DARPA 專案結束後無下文，通常意味著未達可轉移門檻。

8. **獨立第三方複現：仍然查無。** 本回合大量搜尋後，**未找到任何獨立團隊以相同方法複現 >300× 或 83×**。Kemp 本人也承認場強量測極易受干擾（「任何 RF 干擾或周邊材料都會顯著改變量測，很多實驗必須跑到遠離電線與建築的野地」）。（來源 6）電小天線效率量測歷史上不乏被推翻的「超越極限」宣稱。

9. **機械疲勞與壽命：公開文獻仍查無任何一筆連續運轉壽命數據。** 已知 LiNbO₃ Y∠36° 降伏應力 >50 MPa、本徵損耗低（來源 3），但**「單次量測不斷裂」與「連續發射 10,000 小時」是兩回事**。這對產品化是重大資訊缺口。

10. **商業化零證據（不變）。** 查無任何公司、產品型號、報價或供應鏈。**與客戶排除的「壓電取代電感」路線相比，那條路至少有真實產品在市場上；這條路連一個可買的東西都沒有。**

11. **法律／出口管制風險。** VLF 對潛通訊高度敏感；美方由 ITAR（USML）與 EAR（CCL，內含 Wassenaar 清單）雙軌管制，Wassenaar 近年並新增潛艦推進等技術管制。（來源 A：Wassenaar/ITAR 概述）**本回合查無 VLF 發射機的具體管制條目編號**——台灣廠商若要與美方單位合作，必須先做具體條目確認，不可假設可自由技轉。

---

## 6. 未解問題（下一輪必查，按優先序）

1. **Kemp 2019 裝置的絕對輻射功率（W / dBm）與絕對場強—距離曲線。** 這是把「>300×」換算成「能不能通訊」的唯一橋樑，本回合仍查無。需取得原文 Fig. 與補充材料。
2. **BlueME 的確切資料率。** 二手報導的「1–100 kb/s」與 VLF 頻寬物理嚴重衝突，**必須以 arXiv 2411.09241 原文核對**；若真為 kb/s 級，是本領域最重要的單一數字，需理解其調變方式。
3. **BlueME「鹹水 730 m」的鏈路幾何**：是否為水中—空氣—水中的側向波路徑？（本文第 1 節第 5 點推算指出全程走海水物理上不可能。）
4. **「>300×」「>6000×」的基準定義**：相對於什麼天線？效率是輻射效率還是總效率（含匹配網路）？IEEE 建模工作對輻射電阻的質疑是否成立？
5. **AMEBA 的預算金額、完整承包商名單、結案報告、TA1/TA2 是否達標。** 建議查 USAspending.gov 與 DTIC。
6. **機械天線的連續運轉壽命／疲勞數據**（任何路線）。若確實不存在，這本身就是必須寫進商業計畫的風險揭露。
7. **US 10,921,360 的完整 claim 與真實權利人**（Justia 顯示 Rutgers/MIT/SUNY，需以 USPTO 原件核對）；Stanford Piezoelectric Transmitter 家族的 claim 範圍與 FTO 空間。
8. **Nat Commun 2021 兩用元件的完整規格**：磁感測噪聲密度（pT/√Hz）、WPT 絕對效率百分比、耗電、以及 2021 年後是否有跟進的動物實驗或臨床工作。
9. **駐極體式機械天線（路線 D）是否真的效率最高**（APL 2020 Perspective 的說法需原文核對）——若成立，對客戶是負面訊號，因為該路線不需要壓電。
10. **台灣可及性**：中科院／國研院是否有相關計畫？ITAR/EAR 具體管制條目為何？
11. **中國礦難救援旋轉永磁陣列（中國煤炭科工＋應急管理部）的實際部署狀態**——這是唯一有明確政府客戶與應用場景的團隊。

---

## 7. 來源清單

1. **Acoustically actuated ultra-compact NEMS magnetoelectric antennas** — Nature Communications 8, 296 (2017) — https://www.nature.com/articles/s41467-017-00343-8 — *ME 機械天線奠基論文；60 MHz–2.5 GHz，非 VLF；微縮 1–2 數量級。*
2. **同上 PMC 全文（PMC5567369）** — https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5567369/ — *開放取用入口，含 AlN/FeGaB 材料與 Q=930 等細節。*
3. **A high Q piezoelectric resonator as a portable VLF transmitter** — Nature Communications 10, 1715 (2019), Kemp M.A., Franzi M., Haase A. et al. — https://www.nature.com/articles/s41467-019-09680-2 — *本題地基；LiNbO₃ Y∠36°、9.6 cm、35 kHz、Q=45,000、>300×、>83× Bode–Fano。*
4. **同上 OSTI 條目** — https://www.osti.gov/pages/biblio/1510219 — *確認 SLAC/DOE 出處與作者機構。*
5. **SLAC develops novel compact antenna for communicating where radios fail** — https://www6.slac.stanford.edu/news/2019-04-12-slac-develops-novel-compact-antenna-communicating-where-radios-fail — *SLAC 官方新聞稿。*
6. **A strain-based antenna paves the way for portable long-range transmitters** — Physics Today — https://physicstoday.aip.org/news/a-strain-based-antenna-paves-the-way-for-portable-long-range-transmitters — *9.6 cm 棒、量測至 80 m、100 ft 鏈路展示、Kemp 對量測困難的自述。*
7. **US20190074578A1 — Piezoelectric Transmitter** — https://patents.google.com/patent/US20190074578A1/en — *權利人 Board of Trustees of the Leland Stanford Junior University；載明 VAPOR 代號與 >88× Bode–Fano。*
8. **US10424714B2 — Piezoelectric transmitter** — https://patents.google.com/patent/US10424714 — *同族已核准專利。*
9. **Acoustically Driven and Modulation Inducible Radiating Elements (ADMIRE)** — arXiv:1906.07797, Hassanien et al. — https://arxiv.org/abs/1906.07797 — *PZT >6000× 效率、60 bit/s FSK。*
10. **Acoustically driven electromagnetic radiating elements** — Scientific Reports 10, 17006 (2020) — https://www.nature.com/articles/s41598-020-73973-6 — *ADMIRE 期刊版。*
11. **Underwater Radio, Anyone?（DARPA 官方）** — https://www.darpa.mil/news/2016/underwater-radio — *AMEBA 官方說明與 Troy Olsson。*
12. **A MEchanical Based Antenna (AMEBA) — BAA HR001117S0007** — https://govtribe.com/opportunity/federal-contract-opportunity/a-mechanical-based-antenna-ameba-hr001117s0007 — *45 個月、TA1/TA2 分工。*
13. **HRL Awarded DARPA Project AMEBA** — https://www.hrl.com/news/2017/11/02/hrl-awarded-darpa-project-ameba-develop-man-portable-low-frequency-radio-antennas — *唯一查證到的承包商，磁彈性路線、約 1 kHz。*
14. **DARPA FY2022 Budget Justification（RDT&E Vol.1）** — https://comptroller.war.gov/Portals/45/Documents/defbudget/fy2022/budget_justification/pdfs/03_RDT_and_E/RDTE_Vol1_DARPA_MasterJustificationBook_PB_2022.pdf — *記載 AMEBA 於 FY2021 完成。*
15. **New DARPA AMEBA project on magnetic resonators（UIUC Tawfick）** — https://tawfick.mechse.illinois.edu/2017/09/01/new-darpa-ameba-project-on-magnetic-resonators-for-low-frequency-communication/ — *第二個查證到的 AMEBA 參與團隊。*
16. **A Rotating-Magnet Based Mechanical Antenna (RMBMA) for ELF-ULF Wireless Communication** — JPIER — https://www.jpier.org/ac_api/download.php?id=18070204 — *土壤 264.8 m、海水 203.5 m、10×5×2 cm 磁鐵、1 pT。*
17. **Planar rotating permanent magnetic mechanical antenna array for beamforming** — Scientific Reports (2025) — https://www.nature.com/articles/s41598-025-28918-2 — *中國煤炭科工集團＋應急管理部資助，礦難救援導向。*
18. **基於旋轉永磁體的超低頻機械天線電磁特性分析** — 物理學報 68, 20190339 — https://wulixb.iphy.ac.cn/article/doi/10.7498/aps.68.20190339 — *中國旋轉永磁機械天線理論分析。*
19. **基於旋轉永磁體的低頻通信技術研究** — 電子與信息學報 — https://jeit.ac.cn/cn/article/doi/10.11999/JEIT210274 — *20 m 內 3.5 bps 符元率。*
20. **BlueME: Robust Underwater Robot-to-Robot Communication Using Compact Magnetoelectric Antennas** — arXiv:2411.09241（IEEE J. Oceanic Eng.） — https://arxiv.org/abs/2411.09241 — *淡水 200 m @1 W、鹹水 730 m @<10 W、35–36 kHz、ASV+ROV 實地測試。*
21. **UF 官方新聞：A new frontier for marine robot communication** — https://news.ufl.edu/2026/05/marine-robot-communication/ — *BlueME 的機構歸屬與數字二次確認。*
22. **VLF Mechanical Antenna Arrays for Underwater Wireless Communications** — WUWNet '22 — https://dl.acm.org/doi/abs/10.1145/3567600.3568150 — *12 單元陣列合成 200 nT @1 m。*
23. **A Multilayered Magnetoelectric Transmitter with Suppressed Nonlinearity for Portable VLF Communication** — Research (2023) — https://spj.science.org/doi/10.34133/research.0208 — *112 nT@1 m、108 fT@100 m、21.2 kHz、400 mW。*
24. **A wearable, ultrasonically-actuated magnetic-dipole rotating resonator for mobile communication in cross-medium environment** — Nature Communications 16, 4137 (2025), Cheng Z. et al. — https://www.nature.com/articles/s41467-025-59539-y — *0.11 cm³ 壓電堆疊驅動 NdFeB；100 m 2.64 pT（空氣）/2.12 pT（水下）、0.61 W。*
25. **Ultra-compact dual-band smart NEMS magnetoelectric antennas for simultaneous wireless energy harvesting and magnetic field sensing** — Nature Communications 12, 3141 (2021), Zaeimbashi et al. — https://www.nature.com/articles/s41467-021-23256-z — *Plan A 的存在證明：250×174 µm²、GHz 取能＋MHz pT 感測。*
26. **Magnetic Pendulum Arrays for Efficient ULF Transmission** — Scientific Reports 9, 13220 (2019) — https://www.nature.com/articles/s41598-019-49341-4 — *較裸線圈 +7 dB；1031 Hz、2 bps。*
27. **Naturally Resonant Emitters: Approaching Fundamental Antenna Limits** — arXiv:2604.26980 (2026-04-28), Damir Latypov (CRG Defense) — https://arxiv.org/abs/2604.26980 — *本文最重要的反面證據：機械天線已接近理論 FOM 上限。*
28. **A survey of mechanical antennas applied for low-frequency transmitting** — iScience 26(1), 2022 — https://www.sciencedirect.com/science/article/pii/S2589004222021058 — *領域綜述，含各團隊性能比較表（表格內容未經原文核對）。*
29. **Magnetoelectric antennas: Fundamentals, state-of-the-art, challenges, and future perspectives** — APL Electronic Devices 2, 011502 (2026) — https://pubs.aip.org/aip/aed/article/2/1/011502/3378475/Magnetoelectric-antennas-Fundamentals-state-of-the — *最新綜述；ME 天線微縮 4–5 數量級，但輻射機制不確定、缺乏最佳化方法、頻寬窄。*
30. **Ultra-compact mechanical antennas（Perspective）** — Applied Physics Letters 117, 170501 (2020) — https://pubs.aip.org/aip/apl/article-abstract/117/17/170501/39082/ — *四條路線比較；宣稱駐極體式輻射效率高於永磁式與壓電式（需原文核對）。*
31. **VLF Transmitter Cutler — Wikipedia** — https://en.wikipedia.org/wiki/VLF_Transmitter_Cutler — *NAA、24 kHz、1.8 MW 輸入、26 座塔。*
32. **NAA Cutler Maine — Navy VLF Transmitter Site** — https://www.navy-radio.com/commsta/cutler.htm — *1 MW 輻射、997.5 ft 中心塔、50 baud 對潛廣播。*
33. **EvoLogics 聲學數據機產品頁** — https://www.evologics.com/acoustic-modems — *商用聲學數據機規格對照組。*
34. **Teledyne Marine Acoustic Communication 產品線** — https://www.teledynemarine.com/products/product-line/acoustic-communication — *Benthos 系列規格。*
35. **State-of-the-Art Underwater Acoustic Communication Modems: Classifications, Analyses and Design Challenges** — https://www.researchgate.net/publication/341253870_State-of-the-Art_Underwater_Acoustic_Communication_Modems_Classifications_Analyses_and_Design_Challenges — *EvoLogics 62.5 kbps@300 m/10 W、Benthos 2–6 km/140–15,360 bps 的來源。*
36. **Low-cost leaky feeder communication for mines rescue** — Mining Technology 129(4), 2020 — https://www.tandfonline.com/doi/abs/10.1080/25726668.2020.1838110 — *27 MHz、約 1 km；商用 leaky feeder 昂貴笨重。*
37. **Underground Communications & Tracking Systems Update（Coal Age reprint）** — https://www.rfsworld.com/userfiles/pdf/coal_age_reprint_jan08.pdf — *leaky feeder 約 US$3/線性呎起。*
38. **Blue Laser Diode Enables Underwater Communication at 12.4 Gbps** — Scientific Reports (2017) — https://www.nature.com/articles/srep40480 — *藍綠雷射速率上限對照。*
39. **Laser Transmission Characteristics of Seawater for Underwater Wireless Optical Communication** — PMC12115245 — https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12115245/ — *480 nm 消光係數 0.16 / 2.8 m⁻¹，近岸僅約 1.8 m。*
40. **Performance of both-way communications using a magnetic dipole near the sea surface** — IET MAP (2022) — https://ietresearch.onlinelibrary.wiley.com/doi/10.1049/mia2.12228 — *導電介質中磁偶極優於電偶極；19 kHz 小環 <10 W 達海面上 574 m。*
41. **US 10,921,360 — Dual magnetic and electric field quartz sensor** — https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/10921360 — *石英共振器＋磁致伸縮膜；正交軸同時測 E 與 H。權利人依 Justia 為 Rutgers/MIT/SUNY，待原件核對。*
42. **Nian Xiang Sun 專利清單（Justia）** — https://patents.justia.com/inventor/nian-xiang-sun — *Northeastern ME 天線專利家族入口。*
43. **US20190267534A1 — Magnetoelectric Very Low Frequency Communication System** — https://patents.google.com/patent/US20190267534A1/en — *Northeastern 的 VLF ME 通訊系統專利。*
44. **US 11,355,692 — Nanoscale radio frequency magnetoelectric antenna** — https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/11355692 — *Northeastern 已核准的核心專利。*
45. **US 12,424,736 — Portable resonant multiferroic magnetoelectric antenna for ULF/VLF communication** — https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/12424736 — *最新的可攜 ULF/VLF ME 天線專利（權利人待查）。*
46. **US 11,594,816 — Acoustically-driven electromagnetic antennas using piezoelectric material** — https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/11594816 — *ADMIRE 路線對應專利（權利人待查）。*
47. **eLoran – Alternative PNT for submerged and GNSS denied environments（UDT 簡報）** — https://cdn.asp.events/CLIENT_Clarion__96F66098_5056_B733_492B7F3A0E159DC7/sites/UDT-2020/media/libraries/udt-2022-distec-slides/20004---Dr-Gerard-Offermans---FINAL-SLIDES---eLoran-Presentation.pdf — *90–110 kHz、50 ns 授時、±8 m；LF 可入水數公尺。*
48. **Modeling of Piezoelectric Resonator Antennas for VLF Electromagnetic Radiation** — IEEE — https://ieeexplore.ieee.org/iel7/9372408/9372428/09372654.pdf — *指出壓電應變天線輻射電阻遠小於文獻普遍假設的同尺寸電偶極——比較基準的關鍵質疑。*
49. **Ultrasensitive Magnetic Field Sensors for Biomedical Applications** — PMC7146409 — https://pmc.ncbi.nlm.nih.gov/articles/PMC7146409/ — *fluxgate / ME / TMR / SQUID / 原子磁力計的靈敏度—功耗對照。*
50. **Piezo-Based Approach Dramatically Shrinks VLF Antennas** — Electronic Design — https://www.electronicdesign.com/technologies/analog/article/21808539/piezo-based-approach-dramatically-shrinks-vlf-antennas — *Kemp 工作的業界媒體解讀。*
51. **A Bionic Flapping Magnetic-Dipole Resonator for ELF Cross-Medium Communication** — PMC11321680 — https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11321680/ — *路線 C 的另一變體（拍翼式磁偶極），跨介質 ELF。*
52. **Developing VLF Magnetoelectric Antennas for Communication Systems（Northeastern ECE）** — https://ece.northeastern.edu/news/developing-vlf-magnetoelectric-antennas-for-communication-systems/ — *確認 Northeastern 的 VLF ME 天線分支存在。*

> 註：第 5 節第 11 點（ITAR/Wassenaar）與第 4 節 Plan B 第 1 點（AUV 需浮出水面）所依據的搜尋結果為一般性綜述與官方說明頁，本回合未取得可單一引用的權威條目編號，故在正文標為「來源 A」而不編入上表，以免造成過度引用的假象。

---

### 附錄：本文所有【自行推算】的算式（供複核）

- **海水趨膚深度**：`δ = √(2/(ωμ₀σ)) = 251.6/√f`（σ=4 S/m, μ₀=4π×10⁻⁷）。f=1 kHz→7.96 m；10 kHz→2.52 m；21.2 kHz→1.73 m；35 kHz→1.35 m；1 MHz→0.25 m。每 δ 衰減 8.686 dB（35 kHz ≈ 6.4 dB/m）。
- **淡水趨膚深度**（σ=0.01 S/m）：f=35 kHz → `δ = √(2/(2π·35000·1.2566e-6·0.01)) ≈ 26.9 m`。→ BlueME 淡水 200 m ≈ 7.4δ ≈ 64 dB，物理上合理。
- **BlueME 鹹水 730 m 的一致性檢驗**：730/1.35 = 541 個 δ → ≈ 4,700 dB，全程走海水不可能 ⇒ 必為空氣/海面路徑。
- **近場磁偶極矩反推**：軸向 `B = μ₀m/(2πr³)` ⇒ `m = 2πr³B/μ₀`。r=100 m, B=2.64 pT ⇒ m ≈ 13.2 A·m²。
- **磁偶極輻射功率**：`P = μ₀ω⁴m²/(12πc³)`。取 f=100 Hz（ω=628）、m=13.2 ⇒ P ≈ 3.4×10⁻²¹ W。相對 0.61 W 輸入 ⇒ 輻射效率 ~10⁻²¹。**（頻率為假設值，原文未給；若實際頻率更高，效率按 ω⁴ 上升，請以原文頻率重算。）**
- **Chu 極限**：`Q_min ≈ 1/(ka)³ + 1/(ka)`。f=35 kHz → λ=8.566 km；a=0.048 m → ka=3.52×10⁻⁵ → Q ≈ 2.3×10¹³。
- **Kemp 裝置本徵頻寬**：35,000 Hz / 45,000 = 0.78 Hz（論文記為 ≈0.75 Hz）。× 83 ⇒ 約 62 Hz，對應資料率數十 bps，與 ADMIRE 實測 60 bit/s 同量級。
- **ω⁴ 頻率懲罰**：35 kHz → 1 kHz，頻率降 35 倍，輻射功率降 35⁴ ≈ 1.5×10⁶ 倍。
