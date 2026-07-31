# 應用B1：無磁/抗磁場環境的電源與電路——磁性元件根本不能用的場景

> 一句話結論：**這是壓電雙用元件目前最硬的「非替代性」論證**——在 CERN（3.8 T）、ITER（200 mT）、MRI（1.5–7 T）這類環境裡，磁芯物理上會飽和，工程界已經被迫退回「空心電感」這種明顯次佳解並付出體積與效率代價；在磁潔淨端（Solar Orbiter 10 pT、Europa Clipper <1 nT @ 8.5 m 伸桿、OPM-MEG 7–15 fT/√Hz），業界的解法是「把電子學搬到很遠的地方」——**這兩類痛點都不是「電感貴一點」，而是「電感不能用」**。但同樣誠實地說：本輪**查無任何一份公開量測資料證明壓電變壓器的實際剩磁與交流磁場洩漏有多低**，這是整條路線最大的未證實前提。

---

## 0. 研究方法與限制（誠實揭露）

- **WebFetch 在本環境被 egress policy 全面封鎖**，任何 URL 皆回 403，全程未使用。所有事實均來自 WebSearch 回傳的「連結清單 + 模型彙整摘要」，**未能開啟原始 PDF/論文逐字核對**。
- **本輪實際只完成 16 次 WebSearch**（原規劃 25–35 次）。原因：WebSearch 額度是**整個 session 共用**，在本子任務第 17 次查詢時回傳 `this session has used its web search budget (200 of 200 WebSearch calls)`，之後所有查詢一律被拒。**因此本文件的覆蓋度低於原定目標**，下列子題目**完全沒查到**，必須列為下一輪任務：
  - 太空 DC-DC 轉換器的**交流磁場發射規格**（AC magnetic emission，nT @ 1 m 之類的具體數字）與現行磁補償（雙繞組反向繞、扭繞線）的**量化代價**
  - **MRI 射頻線圈前端（on-coil preamp）與線圈內電子的供電方式與功率等級**
  - **OPM 感測頭本身的加熱器/雷射驅動電流所產生的磁場**具體數值（只查到「控制模組通常放在磁屏蔽外」這個定性事實）
  - **壓電變壓器/諧振器本身的剩磁與交流磁矩量測**（★ 最關鍵的缺口，見 §5.1）
  - 空心電感相對鐵氧體在 FEAST 這個具體案例的**體積倍數與效率損失數字**
  - 海軍磁隱身、SQUID、原子鐘/冷原子系統的電源磁潔淨規格
  - 壓電馬達供應商（Nanomotion、PI、Faulhaber）的 MRI 相容型號**實際 datasheet 規格與售價**
- 本文件另有少數事實來自本專案同批的姊妹檔案 `01-pt-power-conversion-sota.md`（同一 repo），已在來源表中標明其原始 URL，但**同樣未經 WebFetch 逐字核對**。
- 凡標「**未驗證**」者，代表僅由單一搜尋摘要得知、無第二來源交叉比對。凡標「**推論**」者，是我依物理常識所做的判斷，**不是查證結果**，客戶不得當作事實引用。

---

## 1. 結論摘要

1. **CERN 已經被迫接受「空心電感」這個次佳解，而且寫進了 ASIC 規格。** CERN EP-ESE 的 FEAST2 降壓轉換器 ASIC 明文為 **400–500 nH 空心電感**最佳化，實際使用的是 **h = 7 mm、D = 9 mm、約 430 nH 的環形電感，磁芯是塑膠**——原因直接寫在文件裡：**鐵氧體在 CMS 的 3.8 T 磁場中會飽和**。FEAST2 規格為可在 **>40,000 Gauss（4 T）** 下運作，開關頻率 1.5 MHz，TID 耐受 >200 Mrad(Si)。〔S1, S2, S3, S5〕
2. **這個次佳解的代價是文件化的：「體積更龐大的空心版本必須被採用」。** CMS Phase-1 像素偵測器升級文件直接說「大磁場（達 4 T）不允許使用鐵磁芯電感，必須改用其體積更龐大的空心對應版本」。整體效率估計「**>80%**」——相對商用同級 POL 轉換器的 90%+ 是明顯退步。〔S5, S6〕
3. **ITER 的磁場梯度把整棟樓的電子學都劃進了問題區。** ITER 官方說明：最靠近機器（port cell）的電子學將浸在**約 200 mT** 的磁場中；托卡馬克廠房內所有 I&C 機櫃與配電盤面對 **2.5 mT 至 20 mT**。200 mT 已足以使多數鐵氧體/鐵粉芯進入非線性區。〔S12〕
4. **太空端的規格嚴苛到「以 pT 計」。** Solar Orbiter 磁強計需量測**振幅低至 10 pT** 的動力尺度磁場擾動；一般要求為太空船 DC 場在外側感測器處 **<10 nT**，且變化量須 <0.5 nT（慢變）/<1 nT（快變）才能靠標定扣除。Cross-Scale 評估報告更給出**外側感測器 0.1 nT / 4000 s** 的要求。〔S8, S9, S11〕
5. **業界目前的解法是「加長伸桿」，而伸桿是昂貴的機構風險。** JUICE 的 MAGBOOM 為 CFRP 三段式 + 鈦合金鉸鏈，**展開後 10.6 m、收納 3.8 m**；Europa Clipper 磁強計裝在 **8.5 m 伸桿**上，實測外側 fluxgate（FG1）處 DC 磁場**滿足 <1 nT 的實作要求**。伸桿的質量、長度、部署失效風險，就是「磁性電子學無法安靜」所付出的系統級代價。〔S14, S15, S16, S17〕
6. **OPM-MEG 這個高成長市場，其控制電子學至今仍被放逐到磁屏蔽室外。** QuSpin Gen-3 感測器靈敏度 **7–10 fT/√Hz（3–100 Hz，雙軸）**、Gen-2 為 **7–15 fT/√Hz（1–100 Hz）**；三軸型雜訊底 ~15 fT/√Hz。文獻明說「**OPM 控制模組本身是潛在干擾源，過去慣例是放在磁屏蔽外以確保感測器最佳性能**」。市場面：Cerca Magnetics 2026 年募得 **£3.8M Series A（≈€4.3M，投後估值 €34.5M）**。〔S18, S19, S20, S23, S24〕
7. **MRI 這一側，已有專利明確主張「用壓電技術在強外部磁場中做 AC→隔離 DC」**（US 10096764，PCT/IB2015/050085），同族還有 US 10262788「使標準 AC/DC 電源轉接器能在高磁場中運作的方法」。專利文本直指磁性元件在強外磁場會飽和、且未固定的電源供應器會成為**飛射物（projectile）危害**。〔S25, S26〕
8. **但壓電馬達在 MRI 裡的實測經驗給了一個重要警告：問題不只是「有沒有磁芯」。** 研究指出 Nanomotion 馬達（與 PI PILine 同屬線性壓電馬達類）在成像期間運轉會造成**中度 SNR 損失**、產生 zipper 與運動偽影；更關鍵的是——**即使馬達關閉**，仍觀察到訊號空洞、堆積與幾何變形，原因是**商用馬達的高金屬含量**擾動了靜場與梯度場均勻性。「非磁芯」≠「MRI 相容」。〔S21, S22〕

---

## 2. 現況：技術 / 產品 / 玩家

### 2.1 高能物理（強磁場 + 強輻射）：CERN 是唯一有量產經驗的在位者

| 項目 | 內容 | 來源 |
|---|---|---|
| ASIC 家族 | FEAST2 / FEAST2.1 / FEASTMP（模組）；下一代 **bPOL12V**（HL-LHC 追蹤器用） | S1, S2, S4, S7 |
| 開發單位 | CERN EP-ESE Electronic Systems for Experiments | S3 |
| 電感 | 空心環形，塑膠芯，~430 nH，h 7 mm × D 9 mm；ASIC 為 400–500 nH 最佳化 | S1, S5 |
| 磁場能力 | >40 kG（4 T）；CMS 實際 3.8 T | S1, S3, S5 |
| 輻射 | TID >200 Mrad(Si)；另述可承受 2×10⁹ Gy 與 >5×10¹⁴ n/cm²(1 MeV-eq) | S1, S3 |
| 輸出 | FEASTMP：4 A 同步降壓，輸入 5–12 V | S4 |
| 已知痛點 | 空心電感體積大、磁場外洩需另加屏蔽（CERN 另有專門論文研究「屏蔽式 PCB 空心環形線圈」） | S5, S6, S10 |

**這一段是本應用的黃金證據**：CERN 不是「想省錢」，而是**沒有選擇**。他們甚至為了空心電感的**外洩磁場**再寫一篇論文做屏蔽最佳化（CDS record 1399742），代表空心電感解決了「磁芯飽和」卻製造了「磁場外洩」的新問題——這正是壓電方案理論上可以同時解掉的兩件事。〔S10〕

### 2.2 太空磁潔淨：規範嚴、解法笨重、無在位競爭者

- **量測需求**：Solar Orbiter 需要 **10 pT 級**擾動量測；一般 DC 預算 **<10 nT @ 外側感測器**；變化率預算 0.5/1 nT。〔S8, S9〕
- **標準解法**：(a) 加長伸桿（JUICE 10.6 m、Europa Clipper 8.5 m、MMS 5 m〔未驗證〕）；(b) 雙感測器梯度儀法（Solar Orbiter 內外兩顆，以梯度技術分離太空船自身訊號）；(c) 全任務級磁潔淨計畫（THEMIS、KPLO/KMAG、MMS 皆有專門文獻）；(d) **EMC quiet periods**——即在關鍵量測時段**關掉某些電子設備**，這是最赤裸的「做不到」證據。〔S8, S9, S13, S27, S28〕
- **事後補救**：近年出現以演算法扣除干擾的路線（RAMEN：Reduction Algorithm for Magnetometer Electromagnetic Noise，2025），代表硬體端仍未解決。〔S30〕
- **玩家**：伸桿由 SENER Aeroespacial（JUICE MAGBOOM）等機構供應；**未查到任何供應商在賣「磁潔淨 DC-DC 轉換器」這個品項**。

### 2.3 MRI 相容電子：有市場、有產品、但都是迴避而非解決

- **現行做法一：把電源移出磁場，只留無磁性負載。** IRadimed 等廠商提供 MRI 相容病患監護儀；專利文獻顯示典型設計採用**無磁性鋰離子電池**（>12 小時續航）或**≥1 F 超級電容**取代含鐵磁材料的電池。〔S31, S32, S33, S34〕
- **現行做法二：光隔離。** US 11796613 / US 12130345「Opto-isolator circuitry for MRI applications」——訊號可以光隔離，**但功率不行**，這正是缺口所在。〔S29〕
- **現行做法三：無磁性電池。** 市面直接有「MRI Non-Magnetic C Size Batteries」這種商品在賣（1.5T/3T 適用），證明市場願意為「無磁性」付溢價。〔S35〕
- **致動端**：壓電超音波馬達已是 MRI 導引介入機器人的事實標準（相對氣壓致動），Nanomotion / PI PILine 為代表；學界則在做**全塑膠外殼超音波馬達**以進一步降低偽影。〔S21, S22, S36, S37〕

### 2.4 壓電側的技術供給狀況（跨引自姊妹檔 01）

隔離型壓電變壓器 2025 年才追上磁性方案：UC Berkeley（Boles 實驗室，APEC 2025）徑向模隔離 PT 達 **峰值 98.3%、寬範圍 >97%**，相對前人無磁性隔離 PT 方案降低損耗比約 27×；MIT 另有 **97.5% 峰值、>40 W/cm³ @ >98%** 的報告。但同一批文獻強調：**99% / 5.7 kW/cm³ 的紀錄僅在「非隔離、2:1 溫和轉換比」下取得**。〔S38, S39, S40〕

---

## 3. 關鍵數字表

| 場域 | 量化規格 | 現行解法 | 現行解法的代價 | 來源 |
|---|---|---|---|---|
| CMS 追蹤器（CERN） | 磁場 **3.8 T**；ASIC 標稱 **>4 T** | FEAST2 + 塑膠芯空心環形電感 430 nH | 體積「更龐大」、效率估 **>80%**、需額外磁屏蔽設計 | S1, S3, S5, S6, S10 |
| CERN 輻射環境 | TID **>200 Mrad(Si)**；>5×10¹⁴ n/cm² | 客製輻射硬化 ASIC | 商用元件全不可用，開發成本極高 | S1, S3 |
| ITER port cell | **~200 mT** | 電子學外移 / 磁屏蔽 | 纜線長度、可維護性 | S12 |
| ITER 廠房 I&C 機櫃 | **2.5–20 mT** | 一般工業設備需重新驗證 | 全廠級認證負擔 | S12 |
| Solar Orbiter MAG | 需量測 **10 pT** 級擾動；DC **<10 nT**；變化 <0.5/1 nT | 雙感測器伸桿 + 梯度儀法 + EMC quiet periods | 太空船本體尺寸限制使伸桿「相當短」，磁潔淨困難 | S8, S9 |
| Cross-Scale（評估） | 外側感測器 **0.1 nT / 4000 s** | — | 被評估為極難達成 | S11 |
| Europa Clipper ECM | 外側 fluxgate **<1 nT**（實測達標） | **8.5 m 伸桿** + 多感測器 | 伸桿質量、部署風險 | S14, S15 |
| JUICE J-MAG | 「前所未有的磁潔淨要求」 | **10.6 m 伸桿**（收納 3.8 m），CFRP + 鈦鉸鏈 | 全製程/整合/測試都受磁潔淨管制 | S16, S17 |
| OPM-MEG（QuSpin Gen-3） | **7–10 fT/√Hz** @ 3–100 Hz（雙軸） | 磁屏蔽室 + **控制模組放在屏蔽外** | 纜線束、系統體積、可穿戴性受限 | S18, S19 |
| OPM-MEG（Gen-2 / 三軸） | 7–15 fT/√Hz / ~15 fT/√Hz | 同上 + 合成梯度儀 | 三軸因分光而雜訊較高 | S18, S20 |
| MRI 主磁場 | 1.5 T / 3 T / 7 T | 電池 or 超級電容 or 移出磁場 | 續航 >12 h 上限、飛射物風險、纜線 | S25, S31, S33 |
| 壓電材料功率密度 | 理論 **330 W/cm³**（應力邊界）；**實務上限 33 W/cm³** | — | 這是壓電方案的硬天花板 | S41 |
| 壓電陶瓷輻射耐受 | ITER 測試 **~10¹⁹ n/cm² (E>0.1 MeV)**；去極化可遠端逆轉；330 °C/200 °C 多次循環存活 | 重新極化程序 | 需要額外的高壓再極化電路 | S42 |
| 單晶 AlN 輻射耐受 | 快中子 1.85×10¹⁸、熱中子 5.8×10¹⁸ n/cm²、gamma **26.8 MGy** 仍可用 | — | AlN 耦合係數低（k² ~6%） | S43 |
| PZT gamma 劣化 | 400 kGy → 介電性能約 **-25%**；1.5×10¹⁷ n/cm² 下共振頻率漂移 **<1%** | — | 中等劑量即有可觀劣化 | S44, S42 |
| 隔離型 PT SOTA | 峰值 **98.3%**、寬範圍 >97%；另 97.5% / >40 W/cm³ | — | 僅實驗室；隔離耐壓規格查無 | S38, S39 |
| OPM-MEG 市場 | $185M(2024) → $1.02B(2033)，CAGR 21.1%（**未驗證**，單一來源） | — | — | S24 |
| Cerca Magnetics | Series A **£3.8M**，投後估值 €34.5M | — | 規模仍小 | S23, S24 |

---

## 4. 「新能力型」應用機會

### 4.1 ★★★ 強磁場探測器/托卡馬克內的「無電感 POL 電源」

- **新能力是什麼**：在 3.8 T（CMS）到 200 mT（ITER port cell）的環境中，直接在負載旁做電壓轉換與隔離，且**不外洩磁場、不需要屏蔽、不需要空心電感的體積**。壓電體的能量儲存在機械慣量與彈性順度中，不依賴磁通，原理上對外部磁場免疫。
- **為什麼以前做不到**：這是**已文件化的真實痛點**，不是我推想的。CMS Phase-1 升級文件白紙黑字：「大磁場（達 4 T）不允許使用鐵磁芯電感，必須採用其體積更龐大的空心對應版本」。CERN 甚至為此開發專用 ASIC（FEAST2 系列）並額外研究空心線圈的磁場屏蔽。〔S5, S6, S10〕
- **是否真的非替代性**：**是（高信心）。** 判準很清楚——如果只是「更小的電感」，CERN 買現貨鐵氧體 POL 就好；他們做不到，所以自己做 ASIC + 塑膠芯環形線圈。壓電方案在此不是取代電感，而是取代「一個已經被迫劣化的解」。**注意這句話的雙面性：正因為 CERN 已有可用（雖差）的方案，壓電方案的價值是「改善」而非「使能」，強度略低於 §4.2 與 §4.3。**
- **誰在做**：SLAC / CPAD（Nikolica 等，2023 Kickoff 與 2025 年會）已將壓電諧振器 DC-DC 列為高能物理探測器前端候選架構——這是 DOE 高能物理儀器協調機構的層級，屬國家級計畫牽引。〔S45〕
- **TRL**：**3–4**。有應用論證與實驗室原型，**查無任何在 T 級磁場 + Mrad 級輻射下的壓電轉換器合格驗證數據**。
- **市場訊號**：HL-LHC 升級、ITER 建造期，皆為十年尺度的政府預算，能吸收高單價；但**單量小**（數萬顆等級），不是消費級生意。
- **技術難點**：(a) 輻射耐受——PZT 在 400 kGy 就有 -25% 介電劣化〔S44〕，而 CERN 要求 200 Mrad = 2 MGy，**差了 5 倍以上，PZT 很可能不合格**；ITER 測試顯示去極化可遠端逆轉，但那需要額外高壓再極化電路〔S42〕；單晶 AlN 耐 26.8 MGy 但 k² 僅 ~6%，功率密度會很差〔S43〕。(b) 探測器有極嚴格的**物質量預算（material budget）**，陶瓷密度高（PZT ~7.8 g/cm³）是負分。(c) 多層 PT 的**內電極材料**若含 Ni 即為鐵磁體（**推論，未查證**），必須改用 Ag/Pd 或 Cu。

### 4.2 ★★★★ 磁潔淨太空船：「可以放在伸桿上、甚至取消伸桿」的電源

- **新能力是什麼**：讓功率轉換器可以裝在**磁強計附近**——放在伸桿中段、放在感測器電子盒內、甚至讓伸桿變短或取消。這改變的是**太空船構型**，不是元件 BOM。
- **為什麼以前做不到**：伸桿存在的唯一理由就是「太空船本體（含電源）太吵」。JUICE 為此做了 10.6 m 三段式 CFRP 伸桿、Europa Clipper 8.5 m、Solar Orbiter 因本體尺寸限制伸桿「相當短」而磁潔淨特別困難，甚至要引入 **EMC quiet periods（量測時關設備）**。〔S8, S16, S14〕
- **是否真的非替代性**：**是（高信心）。** 這不是「更小的 DC-DC」，而是**移除一整根 10 m 級的可展開機構**——那是質量、成本、單點失效風險的大宗。任何能把電源磁噪降到 pT 級的元件，改變的是系統架構。
- **誰在做**：**查無**。本輪未找到任何機構在開發「壓電式磁潔淨太空電源」。這是空白（機會，也是警訊：可能有我沒查到的物理障礙）。
- **TRL**：**2**（概念，無已知原型）。
- **市場訊號**：每年全球帶磁強計的科學任務約個位數；**單量極小**，但單價可以極高（太空級元件）。真正的商業意義可能是**技術背書 + 政府 R&D 資金**，而非營收。
- **技術難點**：(a) **必須先量到壓電轉換器自身的剩磁與交流磁矩**——這是整條路的先決條件，本輪查無任何數據（見 §5.1）。(b) 太空級可靠度：壓電陶瓷的熱去極化與時效漂移在 10 年任務中的行為未知。(c) 真空中無對流散熱，而 PT 的效率對溫度敏感〔S41〕。(d) 電極、封裝、焊料的殘磁往往比「核心元件」更難處理——磁潔淨計畫的實務經驗就是**每一顆螺絲都要測**〔S13, S28〕。

### 4.3 ★★★★ OPM-MEG / 量子感測：把控制電子學搬進磁屏蔽室內、搬上感測頭

- **新能力是什麼**：讓 OPM 的雷射驅動、加熱器、場補償線圈驅動、以及感測頭本地電源，能夠**與感測器共處**而不污染 fT 級量測。終局是「全整合可穿戴 OPM 頭盔」——不再有一大束往屏蔽室外拉的纜線。
- **為什麼以前做不到**：文獻明說「**OPM 控制模組是潛在干擾源，慣例上放在磁屏蔽外以確保感測器最佳性能**」〔S19〕。感測器雜訊底只有 **7–15 fT/√Hz**〔S18, S20〕——任何含磁芯的開關電源在數十公分外都足以蓋掉訊號。低頻（<4 Hz）雜訊尤其嚴重且各感測器不一〔S19〕。
- **是否真的非替代性**：**半。** 誠實評估：現行方案（電子學外移 + 長纜線）**能用**，只是笨重且限制可穿戴性；所以嚴格說這是「解除一個構型限制」而非「從無到有」。但它解除的限制正好是這個產品類別的核心賣點（可穿戴、可移動、兒童可用），所以商業權重仍高。
- **誰在做**：**查無**壓電方案；OPM 廠商為 QuSpin、FieldLine Medical、Cerca Magnetics、Kernel。〔S18, S23, S24〕
- **TRL**：**2–3**。
- **市場訊號**：Cerca 2026 年 **£3.8M Series A**（Guinness Ventures 領投），投後估值 €34.5M；FieldLine 與 Cerca 均在 2024–2025 完成癲癇與帕金森的 phase-2 臨床試驗。市場預估 $185M(2024)→$1.02B(2033) CAGR 21.1%（**未驗證，單一來源，且與其他報告的「helium-free MEG $125.88M(2025)→$355.42M(2032)」不一致，兩組數字請勿混用**）。〔S23, S24〕
- **技術難點**：(a) 需求功率其實**很小**（雷射二極體 + 加熱器，推估數百 mW 至數 W 級，**未查證**），這個功率帶壓電方案的效率優勢不明顯，成本劣勢卻放大。(b) 目標不是 pT 而是 **fT**，比太空任務再嚴 3 個數量級。(c) 壓電體在共振時會**機械振動**，而振動 + 環境殘磁 = 調變磁訊號，對梯度儀是致命的（**推論，未查證，但這是我認為最可能致命的物理障礙，見 §5.2**）。

### 4.4 ★★★ MRI 孔內電子的隔離供電（含介入機器人）

- **新能力是什麼**：在 1.5–7 T 孔內就地產生隔離的直流電，取代「電池 + 定期更換」或「長纜線拉出磁場外」。應用包括病患監護、介入機器人的驅動級、線圈前端電子。
- **為什麼以前做不到**：磁性變壓器與電感在強外磁場中飽和；未固定的電源供應器本身是**飛射物危害**。〔S25〕現行商品只能靠**無磁性電池（>12 h）**或 **≥1 F 超級電容**撐過掃描時段。〔S32, S33, S34, S35〕
- **是否真的非替代性**：**是**（就「在孔內做電壓轉換」這件事而言）。但要注意：**對很多應用而言「電池 + 光纖訊號」已經夠好**，所以真正的痛點集中在「需要持續較大功率」的場合——介入機器人的致動、加熱、高壓源。
- **誰在做**：已有專利族 **US 10096764**（PCT/IB2015/050085，明確主張以壓電技術在強外磁場做 AC→隔離 DC）與 **US 10262788**（使標準 AC/DC 轉接器能在高磁場運作）。**受讓人本輪查無**（搜尋摘要未揭露；專利文本提到應用於醫療裝置的 AC/DC 轉接器）。〔S25, S26〕
- **TRL**：**3–4**（有專利、有電穿孔治療用 PT 高壓脈衝產生器的學術原型，後者明言目標是「無磁性方案，適用於需在外部磁場下運作的高壓脈衝產生器，如即時 MREIT」）。〔S46〕
- **市場訊號**：MRI 相容醫材是高單價市場（能吸收壓電元件成本）；市面已有「MRI 專用無磁性電池」這類溢價商品，證明付費意願存在。〔S35〕
- **技術難點**：(a) ★ **金屬含量比磁芯更關鍵**：實測顯示壓電馬達**即使不通電**仍造成訊號空洞、堆積與幾何變形，因為商用馬達金屬含量高擾動了 B0 均勻性〔S21, S22〕。壓電陶瓷含鉛與重金屬、電極含銀，其**磁化率失配**是否會造成 B0 擾動，本輪**查無量測**。(b) **RF 干擾**：PT 工作在數十 kHz 至數 MHz，其諧波若落在 Larmor 頻率（1.5T ≈ 64 MHz、3T ≈ 128 MHz）附近會產生 zipper 偽影——實測已證明運轉中的壓電馬達會干擾 RF 場〔S21〕。這代表**壓電方案並非自動 MRI 相容，必須做頻譜工程**。(c) 梯度場 dB/dt 在導體中感應渦流——本輪**未查到具體 dB/dt 規格數字**。

### 4.5 ★★ 「元件即感測器」：轉換器同時回報磁環境/機械狀態（雙用特性的直接體現）

- **新能力是什麼**：利用壓電體的機電雙向性，讓同一顆功率元件的運動電流（motional current）同時作為**狀態感測輸出**——已有以運動電流做自感測閉迴路控制的方法論文。〔S47〕在無磁環境中，這意味著**不需要額外的電流感測器（通常含磁芯）**。
- **為什麼以前做不到**：傳統電流感測靠電流互感器或霍爾元件，**兩者都是磁性/磁場感測元件**，在強磁場中飽和、在磁潔淨環境中是污染源。分流電阻雖無磁但損失隔離。
- **是否真的非替代性**：**半。** 分流電阻 + 光隔離已可達成類似功能，所以這是「整合度提升」而非全新能力。但在磁潔淨場景中，**「連電流感測都不能有磁芯」這個約束是真的**，權重可上調。
- **TRL**：**2–3**。
- **技術難點**：運動電流訊號與功率訊號同源，分離需要額外電路；精度與線性度未知。

### 4.6 ★ 海軍磁隱身平台的艦上電源（權重最低，證據最薄）

- 掃雷艦/獵雷艦（排水量 800–1000 噸級）「所有機械、輔機與設備均以非磁性材料製造」，使用**低磁性電動馬達**，不可避免的鐵磁部位則以消磁線圈補償。文獻並直言「**所有低磁性材料都極為昂貴**」——這正好說明此領域對「無磁」有高付費意願。〔S48, S49〕
- **但**：本輪**查無**任何艦上電源轉換器的磁簽章規格數字，也查無市場規模。此機會目前**只是方向，不是證據**，不建議作為投入決策的依據。

---

## 5. 反面證據、失敗案例與物理上限

### 5.1 ★ 最致命的缺口：沒有人量過壓電變壓器的磁場洩漏

整條 B1 路線建立在「壓電元件不輻射磁場」這個前提上。但本輪**查無任何一份公開文獻報告壓電變壓器/諧振器的實測剩磁矩（A·m²）或交流磁場（nT @ 距離）**。而物理上它**絕不是零**：

- 壓電轉換器仍有**電流迴路**（輸入輸出走線、驅動級 MOSFET、去耦電容），任何電流迴路都輻射磁場。壓電體只消除了「電感磁芯」這一項。（**推論**）
- 多層 PT 的**內電極**與焊料、端子鍍層若含 Ni，即為鐵磁材料。（**推論，未查證，但這是磁潔淨計畫實務上最常見的污染源類型**）
- 太空磁潔淨的門檻是 **0.1–1 nT**、OPM 是 **fT**——這個等級下，「沒有磁芯」遠遠不等於「合格」。THEMIS、KPLO、MMS 的磁潔淨計畫都是**逐件量測每個零件**的工程，不是靠元件型錄。〔S13, S27, S28〕

**行動建議：這是任何投入決策前必須先做的第一個實驗**——買一顆現成 PT（例如 CeraPlas 或 STEMINC 的 Rosen 型），在磁屏蔽筒裡用 fluxgate/OPM 量它的 DC 剩磁與工作時的 AC 磁場譜。**如果這個數字不比同等級磁性方案好兩個數量級以上，B1 整條路線就不成立。**

### 5.2 壓電體會機械振動，而振動在磁環境中會產生調變訊號

壓電轉換器的工作原理就是讓陶瓷以數十 kHz–數 MHz 共振。在 OPM/磁強計旁：任何殘餘磁矩隨機械位移移動 = 產生交變磁場；同時機械振動會耦合進感測器結構造成微音效應（microphonics）。這是磁性方案沒有的**新型污染機制**。（**推論，未查證** — 但這是我判斷 §4.3 最可能致命的障礙。）

### 5.3 輻射耐受可能不足以支撐 §4.1

- CERN 要求 **TID >200 Mrad(Si) = 2 MGy**〔S1〕。
- PZT 薄膜在 **400 kGy（0.4 MGy）** 即出現約 **-25% 介電性能劣化**〔S44〕——**比要求低 5 倍就已明顯劣化**。
- ITER 的壓電馬達測試顯示可承受 ~10¹⁹ n/cm²，但**依賴「遠端重新極化」這個運維動作**〔S42〕，對埋在探測器裡十年不能碰的元件不適用。
- 單晶 AlN 可耐 **26.8 MGy**〔S43〕，但 k² 僅約 6%，功率密度與效率會大幅劣於 PZT。
- **結論：材料選擇上存在「耐輻射 ↔ 高耦合係數」的直接衝突**，這是物理層級的取捨，不是工程優化可以繞過的。

### 5.4 壓電變壓器有過真正的商業成功，然後死了——而死因與技術無關

PT 曾大量商品化於 CCFL 背光逆變器（Toshiba、NEC、Hitachi、Panasonic 都採用；Apple MacBook Pro 15"/17" 螢幕內即有壓電逆變器）。2000 年代末至 2010 年代初 **LED 背光取代 CCFL，整個下游需求蒸發，高壓 PT 生產隨之停止**。〔S50〕
**這對客戶的意義**：(a) 壓電變壓器的量產可製造性**已被證明過**，不是紙上技術；(b) 但它的商業存亡取決於**單一下游應用的存續**——若把賭注押在一個窄應用上，同樣的事會再發生一次；(c) 供應鏈已萎縮，重建量產可能比想像貴。

### 5.5 功率密度有硬上限

以應力邊界計算的理論功率密度為 **330 W/cm³**，但**實務上限是 33 W/cm³**，且從未有 PT 達到理論值。限制因素是**振動速度**——速度過大則發熱直至開裂；效率隨溫度上升而快速下降，高功率密度 PT 必須抑制發熱以避免**去極化老化**。〔S41, S51〕
**對 B1 的具體意義**：在 CERN/太空這類**無法對流散熱**（真空、密閉、輻射環境不能加風扇）的場合，這個熱限制會直接壓低可用功率等級。而 §4.1 的 FEASTMP 目標是 **4 A** 輸出——這不是小功率。

### 5.6 「非磁」不等於「MRI 相容」——已有實測反證

前述最重要：壓電馬達**在關機狀態**仍造成 MRI 訊號空洞、堆積與幾何變形，肇因於商用馬達的高金屬含量擾動靜場與梯度場均勻性〔S21, S22〕。學界的對策是把零件換成塑膠等效物〔S36, S37〕。這代表壓電陶瓷本體 + 銀電極 + 封裝的**磁化率工程**是一個獨立且未解的問題。

### 5.7 現行解法「夠用」，是最現實的商業障礙

- CERN 的空心電感方案**已經在運行**，HL-LHC 的 bPOL12V 也已「towards production readiness」〔S7〕。要說服他們換掉一個已驗證的輻射硬化方案，門檻極高。
- 太空的伸桿方案**已經達標**（Europa Clipper 實測 <1 nT）〔S15〕。
- OPM 的「控制模組外移」**已經在賣產品**。
- MRI 的電池方案**已經有商品**。
**所有這些場景都不是「完全做不到」，而是「用一個昂貴笨重的變通做到了」。** 壓電方案賣的是「移除那個變通」的價值——這是真實的，但需要具體算出變通的成本（伸桿多少 kg、多少 M€；纜線束多少成本；電池更換多少人時），才能定價。**本輪查無這些成本數字，這是下一輪最重要的商業功課。**

---

## 6. 未解問題（給下一輪研究）

1. **★ 壓電轉換器的實測磁簽章**：DC 剩磁矩（A·m²）、工作時 AC 磁場譜（nT/√Hz @ 定距）、多層 PT 內電極材料是否含 Ni。**這是 go/no-go 級的問題，且可以用實驗直接回答，不必再靠搜尋。**
2. **現行變通方案的成本量化**：JUICE / Europa Clipper 磁強計伸桿的**質量（kg）與造價**；OPM-MEG 系統中纜線束與屏蔽室的成本占比；CERN 空心電感相對鐵氧體的**體積倍數與效率損失百分點**（FEAST 案例的具體數字本輪查無）。沒有這些數字就無法定價。
3. **輻射與磁場下的壓電轉換器合格數據**：是否存在任何在 >1 T 磁場或 >1 MGy TID 下運作的壓電 DC-DC 實測報告？（本輪查無，僅有 SLAC/CPAD 的提案級文件）
4. **功率等級與場景的配對**：OPM 感測頭實際需要多少功率？MRI 介入機器人驅動級需要多少？CERN POL 是 4 A——這三者差距可能達兩個數量級，決定了材料與拓樸選擇完全不同。本輪只確認了 CERN 的 4 A。

---

## 7. 來源清單

| # | 標題 | URL | 一句話說明 |
|---|---|---|---|
| S1 | FEAST2 datasheet rev1.1 (CERN Power Distribution) | https://power-distribution.web.cern.ch/assets/datasheets/FEAST2%20datasheet.pdf | 1.5 MHz、為 400–500 nH 空心電感最佳化、>40 kG 磁場、TID >200 Mrad(Si) |
| S2 | FEAST2.1 datasheet rev1.0 (CERN) | https://power-distribution.web.cern.ch/assets/datasheets/FEAST2.1%20datasheet.pdf | FEAST 後續版本規格 |
| S3 | Radiation and magnetic tolerant DC-DC converters (CERN EP-ESE) | https://ep-ese.web.cern.ch/project/radiation-and-magnetic-tolerant-dc-dc-converters | CERN 官方專案頁：LHC 實驗需要耐輻射且耐 tesla 級磁場的轉換器 |
| S4 | CMS-doc-11899: CERN FEASTMP DC-DC converters | https://cms-docdb.cern.ch/cgi-bin/PublicDocDB/ShowDocument?docid=11899&version=9 | FEASTMP 4 A 同步降壓、輸入 5–12 V |
| S5 | The CMS Phase-1 Pixel Detector Upgrade (arXiv 2012.14304) | https://arxiv.org/pdf/2012.14304 | ★ 「3.8 T 中鐵氧體會飽和，故磁芯用塑膠」；430 nH、h 7 mm × D 9 mm 環形空心電感 |
| S6 | System Integration Issues of DC to DC converters in the sLHC Trackers (CERN CDS 1234908) | https://cds.cern.ch/record/1234908/files/p276.pdf | ★ 「4 T 不允許鐵磁芯電感，必須用體積更龐大的空心版本」；buck 方案整體效率估 >80% |
| S7 | The bPOL12V DCDC converter for HL-LHC trackers: towards production readiness | https://www.researchgate.net/publication/340836784_The_bPOL12V_DCDC_converter_for_HL-LHC_trackers_towards_production_readiness | 下一代 CERN 轉換器已接近量產 |
| S8 | The Solar Orbiter magnetometer (A&A 2020) | https://www.aanda.org/articles/aa/full_html/2020/10/aa37257-19/aa37257-19.html | ★ 需量測 10 pT 級擾動；DC <10 nT；伸桿短導致磁潔淨困難；EMC quiet periods |
| S9 | Novel magnetic cleaning techniques for Solar Orbiter magnetometer (IEEE) | https://ieeexplore.ieee.org/document/9828828/ | Solar Orbiter 磁潔淨手法 |
| S10 | Optimization of Shielded PCB Air-Core Toroids for High-... (CERN CDS 1399742) | https://cds.cern.ch/record/1399742/files/05621918.pdf | ★ CERN 需額外研究空心線圈的磁場屏蔽——空心電感製造了新的外洩問題 |
| S11 | Cross-Scale: Multi-Scale Coupling in Space Plasma, Assessment Study Report (arXiv 0912.0856) | https://arxiv.org/pdf/0912.0856 | 外側感測器 0.1 nT / 4000 s 的電磁潔淨要求 |
| S12 | How do electronics react to magnetic fields? (ITER) | https://www.iter.org/node/20687/how-do-electronics-react-magnetic-fields | ★ port cell ~200 mT；托卡馬克廠房 I&C 機櫃 2.5–20 mT |
| S13 | The THEMIS magnetic cleanliness program | https://www.researchgate.net/publication/225596708_The_THEMIS_magnetic_cleanliness_program | 任務級磁潔淨計畫的實務內容 |
| S14 | The Europa Clipper Magnetometer (Space Sci. Rev. 219:48, 2023) | https://link.springer.com/article/10.1007/s11214-023-00989-5 | 8.5 m 伸桿；多感測器以扣除太空船殘場 |
| S15 | Europa Clipper Magnetometer Boom Deployment: A First Look (Space Sci. Rev. 2025) | https://link.springer.com/article/10.1007/s11214-025-01238-7 | ★ 外側 fluxgate FG1 實測 DC 場滿足 <1 nT 要求 |
| S16 | JUICE's deployable magnetometer boom (MAGBOOM) — SENER | https://www.group.sener/en/project/juices-deployable-magnetometer-boom-magboom/ | ★ 展開 10.6 m、收納 3.8 m；CFRP 三段 + 鈦鉸鏈；「前所未有的磁潔淨要求」 |
| S17 | ESA Science & Technology — JUICE's magnetometer boom | https://sci.esa.int/web/juice/-/61238-juice-magnetometer-boom | ESA 官方對 JUICE 伸桿與其上五項儀器的說明 |
| S18 | Optimising the sensitivity of OPM-MEG to gamma band activity (Imaging Neuroscience) | https://direct.mit.edu/imag/article/doi/10.1162/imag_a_00112/119823/Optimising-the-sensitivity-of-optically-pumped | QuSpin Gen-3 7–10 fT/√Hz（3–100 Hz 雙軸）、Gen-2 7–15 fT/√Hz |
| S19 | Interference suppression techniques for OPM-based MEG (PMC8803550) | https://pmc.ncbi.nlm.nih.gov/articles/PMC8803550/ | ★ 「OPM 控制模組是潛在干擾源，慣例放在磁屏蔽外」；低頻(<4 Hz)雜訊問題 |
| S20 | An integrated full-head OPM-MEG system based on 128 zero-field sensors (PMC10303922) | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10303922/ | 三軸 OPM 雜訊底約 15 fT/√Hz（分光導致較高） |
| S21 | MRI Compatibility of Robot Actuation Techniques – A Comparative Study (PMC2975551) | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2975551/ | ★ Nanomotion 運轉中造成中度 SNR 損失；與 PI PILine 同類；干擾 RF 場產生 zipper 偽影 |
| S22 | A study on observed ultrasonic motor-induced MRI artifacts (PMC6541879) | https://pmc.ncbi.nlm.nih.gov/articles/PMC6541879/ | ★ 馬達**關閉**時仍有訊號空洞/堆積/幾何變形；肇因為高金屬含量 |
| S23 | Cerca Magnetics: £3.8 Million Series A (Pulse 2.0) | https://pulse2.com/cerca-magnetics-3-8-million-series-a-raised-to-advance-opm-meg-brain-imaging-technology-toward-clinical-deployment/ | Cerca £3.8M Series A，Guinness Ventures |
| S24 | Cerca Magnetics Secures €4.3M for Wearable Brain Imaging (Sci-Tech Today) | https://www.sci-tech-today.com/news/cerca-magnetics-secures-4-3m/ | 投後估值 €34.5M；OPM-MEG 市場 $185M(2024)→$1.02B(2033) CAGR 21.1%（未驗證） |
| S25 | US 10096764 — Application of piezo technology to convert AC line power to isolated DC power in high external magnetic fields | https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/10096764 | ★ 壓電做強磁場中 AC→隔離 DC 的專利主張；PCT/IB2015/050085；受讓人查無 |
| S26 | US 10262788 — Method to enable standard AC/DC power adapters to operate in high magnetic fields | https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/10262788 | 同族專利：讓標準電源轉接器在強磁場中可用 |
| S27 | Analysis of the KPLO magnetic cleanliness for the KMAG instrument (Adv. Space Res.) | https://www.sciencedirect.com/science/article/pii/S0273117721008644 | 韓國月球軌道器的磁潔淨分析案例 |
| S28 | Prediction of DC magnetic fields for magnetic cleanliness on spacecraft | https://www.researchgate.net/publication/238524081_Prediction_of_DC_magnetic_fields_for_magnetic_cleanliness_on_spacecraft | 太空船 DC 磁場預測方法論 |
| S29 | US 11796613 / US 12130345 — Opto-isolator circuitry for MRI applications | https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/11796613 | MRI 用光隔離：訊號可光隔離，功率不行 |
| S30 | In Situ Calculation of Spaceflight Magnetometer Coupling Coefficients (RAMEN, Earth & Space Science 2025) | https://agupubs.onlinelibrary.wiley.com/doi/full/10.1029/2024EA003914 | 以演算法事後扣除磁強計電磁干擾——反證硬體端未解 |
| S31 | MRI-Compatible Patient Monitor (IRadimed) | https://www.iradimed.com/products/mri-patient-monitor | MRI 相容病患監護儀商品 |
| S32 | US 9585574 — Magnetic resonance system including an automated non-magnetic medical monitor | https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/9585574 | 以陶瓷壓電元件消除電磁敏感元件的監護儀設計 |
| S33 | US 8294588 — Battery system for MRI compatible wireless patient monitor | https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/8294588 | 無磁性鋰電池 >12 h；≥1 F 超級電容替代方案 |
| S34 | Wireless patient parameter sensors for use in MRI (US 8098149) | https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/8098149 | 無線傳輸頻率與功率須受限以免干擾 MR 訊號 |
| S35 | MRI Non-Magnetic C Size Batteries (MRI Med) | https://mrimed.com/products/mri-non-magnetic-c-size-batteries-4pk | 市售「MRI 專用無磁性電池」——證明無磁性的付費意願 |
| S36 | Demonstration and Experimental Validation of Plastic-Encased Resonant Ultrasonic Piezoelectric Actuator for MRI-Guided Surgical Robots (PMC7376759) | https://pmc.ncbi.nlm.nih.gov/articles/PMC7376759/ | 以塑膠件取代金屬件降低偽影 |
| S37 | Design and Characterization of MRI-compatible Plastic Ultrasonic Motor (arXiv 2409.04006) | https://arxiv.org/abs/2409.04006 | 全塑膠超音波馬達的 MRI 相容性研究 |
| S38 | High-Efficiency Isolated Piezoelectric Transformers for Magnetic-less DC-DC Power Conversion (APEC 2025) | https://ieeexplore.ieee.org/iel8/10977026/10977027/10977397.pdf | 隔離 PT 峰值 98.3%、寬範圍 >97%、損耗比降約 27×（經姊妹檔 01 引用） |
| S39 | Design of High-Performance Piezoelectric Transformer-Based DC-DC Converters (MIT 碩論, Ng 2022) | https://dspace.mit.edu/bitstream/handle/1721.1/147567/Ng-elaineng-meng-eecs-2022-thesis.pdf?sequence=1&isAllowed=y | PT 峰值 97.5%、>40 W/cm³ @ >98%；商用高壓 PT 皆非隔離型 |
| S40 | Piezoelectric Transformers For Power Conversion (UC Berkeley 技轉 NCD 33842) | https://techtransfer.universityofcalifornia.edu/NCD/33842.html | 99% / 5.7 kW/cm³ 僅限非隔離 2:1 VCR 的關鍵限制 |
| S41 | Power density of piezoelectric transformers improved using a contact heat transfer structure (PubMed 22293737) | https://pubmed.ncbi.nlm.nih.gov/22293737/ | ★ 理論功率密度 330 W/cm³，實務上限 33 W/cm³；振動速度過大則發熱開裂 |
| S42 | Radiation tolerance testing of piezoelectric motors for ITER (first results), Fusion Eng. Des. | https://www.sciencedirect.com/science/article/abs/pii/S0920379622000175 | ★ ~10¹⁹ n/cm² (E>0.1 MeV)；去極化可遠端逆轉；330 °C/200 °C 多循環存活 |
| S43 | Radiation tolerance of piezoelectric bulk single-crystal aluminum nitride (PubMed 24960710) | https://pubmed.ncbi.nlm.nih.gov/24960710/ | 單晶 AlN 耐快中子 1.85×10¹⁸、熱中子 5.8×10¹⁸ n/cm²、gamma 26.8 MGy |
| S44 | Effects and mechanisms of gamma irradiation on electrical properties of PZT-S and PZT-N (Ceramics International) | https://www.sciencedirect.com/science/article/abs/pii/S0272884226034942 | ★ 400 kGy → PZT 薄膜介電性能約 -25% |
| S45 | DC-DC Converters Using New Materials and Architectures (Nikolica, SLAC CPAD 2023) | https://indico.slac.stanford.edu/event/8288/contributions/7679/attachments/3653/9997/CPAD_DCDC_Nikolica_20231109_v1.pdf | 高能物理探測器前端採用壓電諧振器 DC-DC 的應用論證 |
| S46 | Piezoelectric Transformer-Based High-Voltage Pulse Generator Using WBG Semiconductors for Medical Electroporation Therapy (Ann. Biomed. Eng., PMC10761399) | https://pmc.ncbi.nlm.nih.gov/articles/PMC10761399/ | ★ 明言 PT 提供「無磁性方案」，適用於須在外部磁場下運作（如即時 MREIT）的高壓脈衝產生器 |
| S47 | Motional-Current-Sensing Method and Simplified Closed-Loop Control for PR-based DC-DC Converters (arXiv 2605.15279) | https://arxiv.org/pdf/2605.15279 | 以運動電流做自感測閉迴路控制——「元件即感測器」的技術基礎 |
| S48 | Engineering:Minehunter (HandWiki) | https://handwiki.org/wiki/Engineering:Minehunter | 800–1000 噸 MCMV 全船非磁性材料；低磁性材料極為昂貴；消磁線圈 |
| S49 | Low magnetic electric motor (Wikipedia) | https://en.wikipedia.org/wiki/Low_magnetic_electric_motor | 掃雷艦/獵雷艦/特定潛艦使用低磁性馬達 |
| S50 | Piezoelectric Transformers: An Historical Review (Actuators 5(2):12, MDPI) | https://www.mdpi.com/2076-0825/5/2/12 | ★ CCFL 背光是 PT 唯一大規模商業成功；LED 取代後生產停止；Apple MacBook Pro 15"/17" 曾採用 |
| S51 | Thermal Degradation and Aging of High-Temperature Piezoelectrics (Univ. of Kentucky 學位論文) | https://uknowledge.uky.edu/cgi/viewcontent.cgi?article=1568&context=gradschool_theses | 熱去極化與時效漂移；tetragonal vs rhombohedral/MPB 的去極化溫度差異 |
| S52 | State-of-the-Art DC-DC Converters for Satellite Applications (Aerospace 12(2):97, MDPI) | https://www.mdpi.com/2226-4310/12/2/97 | 太空級 DC-DC 需抑制 EMI 以免干擾磁強計等敏感儀器 |
| S53 | Katja Klein, The DC-DC Conversion Power System (TWEPP 2014, CERN Indico) | https://indico.cern.ch/event/299180/contributions/1659577/attachments/563061/775706/KatjaKlein_TWEPP14.pdf | CMS DC-DC 供電系統的整體設計簡報 |
| S54 | New Small Wheel Low-Voltage Power: Design Review (ATLAS) | https://air.unimi.it/retrieve/handle/2434/270406/379778/LV_power_rev1.pdf | ATLAS NSW 低壓供電對耐磁耐輻射轉換器的需求 |

---

### 附註：對客戶決策的一句話建議

B1 的價值命題應該精準表述為——**「不是更小的電感，而是讓 10.6 m 的伸桿、屏蔽室外的一整櫃電子學、以及每次掃描前更換的電池，可以消失」**。這個命題在物理上成立、在多個領域有已文件化的痛點、且**目前沒有在位競爭者**。但它有一個未經驗證的前提（壓電轉換器的實測磁簽章）和一個明確的物理衝突（耐輻射 ↔ 高耦合係數）。**建議：在投入任何研發資源前，先花兩週做 §6.1 的磁簽章量測實驗。** 這個實驗便宜、快速，而且能單獨否決或確立整條路線。
