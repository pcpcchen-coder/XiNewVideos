# 壓電材料與製造：性能、溫度、無鉛法規、成本驅動因子

> 一句話結論：**「主動＋被動兩用」在材料層面撞上一條無法迴避的硬牆——d 常數與 Qm 互斥、且功率密度被自發熱鎖死在 ~23–33 W/cm³ 等級**；因此真正「以前做不到」的機會不在把壓電體做成更好的儲能元件（那條路被熱與成本堵死），而在**三個磁性元件在物理上根本進不去的縫隙**：(a) 極低隔離電容（0.032 pF）的聲學隔離、(b) 單一陶瓷同時是升壓器與電漿電極（>1000 倍升壓比，<25 V 進、>10 kV 出）、(c) 電磁路徑不存在的密閉金屬腔穿壁供電。至於無鉛化，RoHS 新增的 7(c)-VI 條款把 PZT 的豁免明確寫進法規並延到 **2027-12-31**，短期不是威脅，但**它是一個有明確日期的倒數計時器**，而無鉛 KNN 在「高功率硬式共振」這一格至今沒有可用材料。

---

## 0. 研究方法與限制（誠實揭露）

- **WebFetch 在本環境被 egress policy 全面封鎖**（任何 URL 皆回 403），一手全文無法抓取。本文所有數字皆來自 WebSearch 回傳的搜尋結果摘要與其中的原文摘錄。
- **本輪僅完成 16 次 WebSearch 即遭遇 session 層級的搜尋配額上限**（系統回報 200/200 已用盡，配額由本 session 的多個平行 agent 共用）。原規劃的 25–35 次查詢**未能執行完畢**。以下主題**因此完全查無、本文不做任何數字推測**：
  - **PZT 陶瓷的實際單價（$/kg 或 $/pc）與量產規模對單價的下降曲線** — 查無，本文只給定性成本驅動因子排序，**不編造百分比拆解**。
  - **TDK CeraPlas HF 的一手 datasheet 規格**（尺寸、輸出功率、升壓比）— 本輪查無，僅能引用本專案 02 號 dossier 已記錄的存在事實。
  - **Murata / TDK 無鉛量產的具體型號與出貨量** — 查無可信一手來源。
  - **石英與 GaPO4 的 f·Q 積具體數值、PZT 熱導率具體數值（W/m·K）** — 查無具體數字，僅查到相關論文標題。
  - **封裝成本占元件總成本比例** — 查無。
  - **窄頻元件頻率篩選良率的實際百分比** — 查無（只查到「±10 ppm 對多數應用而言昂貴到不可行」這類定性敘述）。
- **來源品質分級**：本文對每一條關鍵事實標註來源編號。凡來源為**廠商行銷部落格、市場報告聚合網站、AI 生成內容農場**者，一律標註「**行銷型來源，不可作決策依據**」。凡僅見於搜尋摘要、無法交叉驗證者標註「**未驗證**」。
- 搜尋結果中出現數篇 2026 年 arXiv 編號（如 2604.13364、2606.00064、2602.16102），與當前日期（2026-07）一致，但**未經一手核對**。

---

## 1. 結論摘要

1. **「兩用元件」的材料矛盾是本質性的，不是工程可解的**：搜尋結果直接指出「d33 的提升通常伴隨 Qm 的下降，反之亦然」[3][2]。被動角色（儲能／濾波／阻尼）要高 Qm、低損耗；主動角色（致動／升壓／發射）要高 d、高 k。**沒有任何一種材料能同時最佳化這兩端**，客戶的「兩用元件」在單一材料上必然是折衷，這是規格書上第一條必須寫清楚的事。

2. **功率密度天花板由熱、不是由材料極限決定**：壓電變壓器的**理論功率密度可達 330 W/cm³，實務上被限制在約 33 W/cm³**，原因明確是「材料可通過的最大電流被發熱造成的溫升限制」[56][57]。PZT-8 的另一組獨立估算給出 **23 W/cm³**（在 400 Hz、E3max = 8 kV/cm、T3max = 7000 psi 條件下）[10]。這是一個**十倍等級的理論-實務落差**，且落差的原因是散熱，不是材料。

3. **最大振動速度是硬式 PZT 的實體上限，熱壓製程把它從 1.7 m/s 推到 2.5 m/s（+47%）**——這是 2025 年 Nature Communications 的結果[6]。另有高功率 PMS-PZT 材料的「安全振動速度」報告值為 **1100 mm/s**[7]。Qm 會隨振動速度上升而劣化，且 Qm 的下降可與試片溫升直接關聯[8]，構成**自發熱正回饋**。

4. **無鉛法規：短期不是威脅，但有明確倒數日期。** 2025-09-08 歐盟執委會正式通過三項修訂 RoHS Annex III 的授權指令，原 7(c)-I / 7(c)-II 被更新，並**新增 7(c)-V 與 7(c)-VI；7(c)-VI 明確涵蓋壓電陶瓷（PZT）與 PTC 陶瓷，豁免至 2027-12-31**；原 7(c)-I（非介電陶瓷用鉛）豁免至 2027-06-30。續期申請須於期滿前 18 個月提出（即 **2026-06-30 前**，該日期在本文撰寫時已過），成員國轉置期限亦為 2026-06-30，新規自 **2026-07-01 生效**[13][14][15][16][18]。**本輪查無「是否已有廠商提出續期申請」的證據** — 這是必須追的第一件事。

5. **無鉛 KNN 在「高功率硬式共振」這一格沒有可用材料，且失敗原因是製程物理不是配方**：KNN 因鉀高度活潑而**吸濕**，鹼金屬碳酸鹽吸水生成水合物會改變相組成，且**KNN 的 Q 值與電容量對濕度敏感**[21][22]；化學計量 KNN 的固相燒結**緻密化差、燒結溫度窗極窄**，K/Na 在高溫揮發導致緻密度與壓電響應同時劣化[23][24]。搜尋摘要中「某 KNN 變種達 d33 = 220 pC/N，與 PZT 相當」一說**來源為行銷型內容農場，不可作決策依據**[27]。

6. **薄膜路線（AlN/ScAlN）是唯一 CMOS 相容、已有產業級量產的壓電製造平台，但它有厚度地板**：AlN 沉積溫度低於 400 °C、無汙染，因此 CMOS 相容[38][37]；然而膜厚由 1000 nm 縮到 250 nm 時 XRD FWHM 惡化 10%，縮到 100 nm 時惡化超過 20%，實務上**建議不要低於 200 nm**[39]。這直接限定了薄膜路線的最高頻率與最低阻抗。

7. **ScAlN 把薄膜壓電性能拉高到接近可用**：Sc 40% 時 d33 最大 28 pC/N、−d31 最大 13 pm/V，BAW 的 k² 達 **15.5%，為純 AlN 的 2.6 倍**[36]；2025 年 Nature Communications 報告以熱退火把 d33 從 as-grown 的 12.3 pC/N 提升到 **45.5 pC/N（3.5 倍，約為商用 AlN 的 8 倍）**[35]。

8. **鈮酸鋰（LN）是目前功率共振器的性能冠軍，但被雜散模態卡住**：LN 共振器已達 **Q = 4178、kt² = 29%**，並有 **750 kHz / 100 W / 99.3% 效率**的並聯徑向模態 LN 原型紀錄[28]。但同一批研究直言：**「聲學共振器介於串聯與並聯共振之間的電感性區間本身就狹窄，又被雜散模態進一步壓縮」**，雜散模態帶來電阻性損耗區、直接劣化效率並限制電壓轉換比[28][29]。

---

## 2. 現況：技術 / 產品 / 玩家

### 2.1 塊材陶瓷（bulk ceramic）

- **硬式 PZT**：APC 841 / 880 / 840 是業界事實標準的高功率硬式材料。APC 841 被描述為「相較其他硬式材料具相對高的 d33」，且「較高 Qm、較低機械損耗，因而工作溫度較低、運轉較經濟」；APC 880 用於「需要最高電驅動／責任週期」的場合，具高介電穩定性與高驅動下的低機械損耗[1][2][3]。
- **一個容易被忽略的製程事實**：硬式 PZT 的 **Qm 會隨極化後的時間顯著上升**（老化過程）[4]，代表**出廠測試值與現場穩態值不同**，對窄頻兩用元件的設計餘裕影響直接。另有研究以**外加 DC 偏壓**改善 PZT 的高功率特性[5]，這對「主動/被動兩用」是一個有用的操作旋鈕（偏壓可即時切換元件的損耗特性）。
- **熱壓（hot-pressing）**是把塊材推到極限的製程路線，2025 年 Nature Communications 的成果把最大振動速度從常規燒結的 1.7 m/s 推到 **2.5 m/s**[6]。

### 2.2 單晶（PMN-PT 家族）

- **PMN-PT**（菱方相、[001]c 極化）：**d33 > 2000 pC/N、k33 > 0.9**，但**矯頑場僅 Ec ≈ 2–3 kV/cm**、**菱方-四方相變溫度 Trt 僅 85–95 °C**[48][49]。
- **PIN-PMN-PT**（三元）：**k33 ≈ 0.87–0.92、d33 ≈ 1000–2200 pm/V**，**Ec 提升到 > 4.5 kV/cm、Trt > 120 °C**[48][49][50]；四方相晶體 Ec 可達 8 kV/cm（菱方相對照組 4 kV/cm）[48]。
- **對兩用元件的意義**：單晶的 d 與 k 無人能敵，但 **Ec 與 Trt 是硬牆**。要在功率場合來回驅動，2–3 kV/cm 的矯頑場等於「一激勵就去極化」。Mn 摻雜 PIN-PMN-PT 專門為高功率而生[49]，是唯一值得看的單晶分支。**單晶價格本輪查無。**

### 2.3 薄膜（AlN / ScAlN / 濺鍍 PZT）

- **AlN/ScAlN 已是 BAW/FBAR 產業級量產材料**，沉積溫度 <400 °C、CMOS 相容[37][38]。ScAlN 在 5G 寬頻 BAW 已有完整研究鏈[36]，並延伸到 mmWave（濺鍍 ScAlN + Pt 電極）[40]、K 波段週期性極化 AlScN BAW、以及 19 GHz 濾波器[36 相關族群]。
- **濺鍍 PZT 薄膜**：歐盟 FP7 **PiezoVolume** 計畫（grant 229196）的目標值 **d33,f > 100 pm/V、|e31,f| > 14 C/m²，在 150 mm 與 200 mm 基板上均達成並超越**；並開發出寬 250 mm 的矩形陰極幾何，可在溫控晶圓上做到 200 mm 均勻沉積[73]。實測值報告為 **d33,f ≈ 110 pm/V、e31,f ≈ −20 C/m²**[72][75]。
- **溶膠凝膠（sol-gel）PZT**：0.7–2.2 µm 厚膜的有效 **e31 = −12.5 ± 0.3 C/m²**[74]，明顯低於濺鍍。
- **厚度區間**：產業實績為 **200 nm – 5 µm，其中 2 µm 是成本考量下的標準值**；高速濺鍍可做到 **2–8 µm 無裂縫無孔洞**[72]。

### 2.4 高溫材料（>300 °C）

| 材料 | 關鍵數字 | 上限成因 |
|---|---|---|
| **Bi 層狀（BLSF）** | Na₀.₅Bi₃(LiMn)₀.₉Ti₄₋ₓCeₓO₁₅：**d33 = 32.0 pC/N、500 °C 時 ρ = 1.2×10⁸ Ω·cm、Tc = 648 °C**[51] | d33 太低（僅 PZT 的 ~1/10） |
| **GaPO4** | 與石英同族但**機電耦合更高、壓電靈敏度更佳**；α→β 相變低於 970 °C，但**實用上限 <700 °C**，因結構失序導致 Qm 下降[52] | Qm 隨溫度崩壞 |
| **Langasite (LGS)** | 可用至 **1000 °C**[52] | 高溫電阻率不足 |
| **YCOB (ReCa₄O(BO₃)₃)** | **800 °C 時 ρ ≈ 2×10⁸ Ω·cm（比 langasite 高兩個數量級）**；**至熔點 ~1500 °C 前無相變**[52][54] | d 常數低、單晶成長成本 |
| **LiNbO3（MEMS）** | 已有**橫向振動 LN MEMS 共振器陣列在空氣中 500 °C 運作**的紀錄[34] | 高溫下 Li 出離、還原 |

### 2.5 代工與供應鏈（piezoMEMS foundry）

| 業者 | 提供 | 備註 |
|---|---|---|
| **Silex Microsystems**（瑞典） | **PZT 與 AlN 兩者**皆有；與 **ULVAC** 密切合作開發高性能濺鍍 PZT，提供完整 PZT 製程整合 | 投入 piezoMEMS 代工「超過 15 年」[76] |
| **SINTEF（經 imec / Europractice）** | 每個 MPB（Multi-Project Batch）可取得 **3–12 片 6 吋 piezoMEMS 晶圓**，每片可放不同設計與測試結構 | 對「先驗證再投產」的台灣團隊是**成本最低的切入口**[77] |
| **imec**（比利時） | AlN 製程[61] | — |
| **Fraunhofer ISIT**（德國） | AlN 製程 | 注意：搜尋結果指向 **ISIT** 而非任務書所寫的 IPMS[61] |
| **Rogue Valley Microdevices**（美國） | wafer service 與 MEMS foundry 同線：熱氧化、LPCVD SiN、poly-Si、PECVD、PVD | 美國本土，供應鏈政治風險考量[78] |
| **I-PEX**（日本） | 壓電 MEMS 委外加工；**PZT 與無鉛材料**高性能壓電沉積服務 | 唯一明確提供**無鉛薄膜**的代工[79] |
| **ROHM**（日本） | 薄膜壓電 MEMS 代工 | [80] |

> **本輪查無**：VTT、X-FAB 的 piezoMEMS 代工服務證據（不代表不存在，是本輪配額用盡未查）。

---

## 3. 關鍵數字表

| 項目 | 數值 | 條件／備註 | 來源 |
|---|---|---|---|
| 壓電變壓器理論功率密度 | **330 W/cm³** | 理論值 | [56][57] |
| 壓電變壓器實務功率密度 | **≈ 33 W/cm³** | 受發熱溫升限制，**10 倍落差** | [56][57] |
| PZT-8 功率密度 | **23 W/cm³** | π_max = ω·d33·E₃max·T₃max/2；E₃max = 8 kV/cm、T₃max = 7000 psi、f = 400 Hz | [10] |
| 最大振動速度（熱壓 PZT） | **2.5 m/s** | vs 常規燒結 **1.7 m/s** | [6] |
| 安全振動速度（PMS-PZT） | **1100 mm/s** | 高功率材料 | [7] |
| LN 功率共振器 | **Q = 4178、kt² = 29%** | 塊材 LN | [28] |
| LN 功率轉換器原型 | **750 kHz / 100 W / 99.3% 效率** | 並聯徑向模態 LN | [28] |
| 薄膜 LN（mmWave） | **Qm ≤ 380、功率處理 > 20 dBm** | 50 Ω 匹配 | [32][33] |
| 薄膜 LN 極高頻 | 57 GHz：k² 7.3%、Q 56 ／ 50.74 GHz：Q 237、k² 5.1% | f·Q 積在 mmWave 崩壞 | [32][33] |
| AlN BAW Q | **Qmax = 3346 @ 1.578 GHz**；16 GHz AlN FBAR **Qmax ≈ 363** | Akhiezer damping 主導 | [39] |
| AlN 膜厚地板 | 1000→250 nm：FWHM +10%；→100 nm：> +20%；**建議 > 200 nm** | 結晶品質崩壞 | [39] |
| ScAlN（Sc 40%） | **d33 = 28 pC/N、−d31 = 13 pm/V、BAW k² = 15.5%（AlN 的 2.6×）** | 濺鍍於 Si | [36] |
| ScAlN（熱退火） | d33 **12.3 → 45.5 pC/N（3.5×，約商用 AlN 的 8×）** | 2025 Nat. Commun. | [35] |
| AlN 沉積溫度 | **< 400 °C** | CMOS 後段相容關鍵 | [37][38] |
| 濺鍍 PZT 薄膜 | **d33,f ≈ 110 pm/V、e31,f ≈ −20 C/m²**；PiezoVolume 目標 d33,f>100 pm/V、\|e31,f\|>14 C/m² 於 150/200 mm 達成 | 產業級 | [72][73] |
| Sol-gel PZT | **e31 = −12.5 ± 0.3 C/m²**，厚 0.7–2.2 µm | 明顯遜於濺鍍 | [74] |
| PMN-PT | **d33 > 2000 pC/N、k33 > 0.9、Ec 2–3 kV/cm、Trt 85–95 °C** | [001]c 菱方相 | [48] |
| PIN-PMN-PT | **k33 0.87–0.92、d33 1000–2200 pm/V、Ec > 4.5 kV/cm、Trt > 120 °C** | 四方相 Ec 可達 8 kV/cm | [48][50] |
| BLSF 高溫陶瓷 | **d33 = 32 pC/N、Tc = 648 °C、500 °C 時 ρ = 1.2×10⁸ Ω·cm** | Na₀.₅Bi₄.₅Ti₄O₁₅ 系 | [51] |
| YCOB | **800 °C 時 ρ ≈ 2×10⁸ Ω·cm**、至 ~1500 °C 熔點無相變 | 比 langasite 高兩個數量級 | [52][54] |
| GaPO4 | 實用上限 **< 700 °C**（α→β 相變 < 970 °C） | Qm 因結構失序下降 | [52] |
| Curie 溫度（PZT） | 軟式（Nb 摻雜 PZT-5A 型）**360 °C**；硬式（Fe 摻雜 PZT-4 型）**325 °C** | 實用溫度慣例約 Tc/2 | [86] |
| 老化率（共振器級） | 最佳 **0.03% / decade**；一般致動器材料 **4%/decade（NCE51/51F）、9%/decade（NCE46）** | 共振頻率隨老化**上升** | [84][85] |
| 石英頻率公差 | 常見 ±20 / ±50 / ±100 ppm；**±10 ppm @ −40~+85 °C「對絕大多數應用而言貴到不可行」** | 兩用窄頻元件的成本殺手 | [81][82] |
| 聲學隔離閘極驅動 | **隔離耐壓 2.75 kV、隔離電容 0.032 pF、導通時間 108.8 ns**（驅動 650 V / 11 A GaN HEMT），聲程 1.25 mm | 微波聲學 SAW | [60] |
| 傳統壓電變壓器頻寬 | 工作頻率 < 數十 MHz、**Qm ≈ 1000 → 固有頻寬僅數十 kHz**，不足以驅動 WBG 的 sub-µs 邊沿 | 這是 PT 做不了閘驅的直接原因 | [60] |
| 壓電直接放電（PDD） | **升壓比 > 1000；輸入 < 25 V → 輸出 > 10 kV** | 單一陶瓷即完成 | [64][66] |
| 穿金屬壁供電 | **1.045 MHz、穿 11 mm 鋼壁、效率 60%** | 已優化系統 | [61] |
| 穿金屬壁供電（高功率） | 100 W（小型簡單結構壓電裝置） | 另有「88–93%、1–3 kW」之說，**來源為摘要轉述、未驗證、存疑** | [62][63] |

---

## 4. 「新能力型」應用機會

> 篩選原則：凡是「更小／更薄／更便宜地取代既有磁性或電容元件」的，一律標為**替代型**並降權。以下依「非替代性」由強到弱排列。

### 4.1 超低隔離電容的聲學隔離閘極驅動（材料：薄膜 LN / ScAlN）

- **新能力是什麼**：把隔離電容做到 **0.032 pF**，同時維持 **2.75 kV** 隔離耐壓、**108.8 ns** 導通時間，已實測驅動 650 V / 11 A GaN HEMT[60]。
- **為什麼以前做不到**：磁耦合與電容耦合隔離器的隔離電容典型在 pF 等級，**共模瞬態（dV/dt）電流 = C_iso × dV/dt**。GaN/SiC 的 dV/dt 上看 100–200 V/ns，pF 級隔離電容直接把共模電流灌回控制側。要把 C_iso 壓到 0.03 pF 等級，電磁路徑上**沒有解**——必須把能量轉成聲子走過一段實體介質。這是「以前做不到」，不是「做得更小」。
- **為什麼傳統壓電變壓器做不到**：同一篇論文自己給出反證——傳統 PT 工作頻率低於數十 MHz、Qm ≈ 1000，**固有頻寬僅數十 kHz**，無法支撐 WBG 需要的 sub-µs 邊沿[60]。**必須跳到 GHz 級 SAW**，這正是薄膜 LN / ScAlN 材料才剛剛成熟的領域。
- **是否真非替代**：**是**（隔離電容量級是新的）。
- **TRL**：3（單一原型，arXiv 2511.13412，2025-11）。
- **市場訊號**：隔離閘驅是 Infineon、ST、Microchip 都有完整產品線的成熟市場[60 相關]，代表需求端不需要教育；但也代表在位者強大。
- **最大技術障礙**：SAW 元件的**功率處理**。薄膜 LN 在 50 Ω 匹配下功率處理 > 20 dBm（即 ~100 mW）[32]，而閘驅副邊供電典型需求在 100 mW–1 W 之間，**餘裕極小**。要提高功率就要加大面積或降頻，兩者都吃掉 0.032 pF 的優勢。

### 4.2 單一陶瓷同時是升壓器與電漿電極（壓電直接放電，PDD）

- **新能力是什麼**：**輸入 < 25 V，輸出 > 10 kV，升壓比 > 1000**，且**壓電體表面本身就是放電電極**，直接在角落或鄰近電極產生類電暈放電，生成大氣壓冷電漿[64][65][66]。
- **為什麼以前做不到**：不是「不能升壓」，磁性變壓器當然能升到 10 kV。做不到的是**「升壓器與放電電極是同一個物體」**——磁性方案必須有高壓繞線、絕緣、引線、電極，體積與絕緣設計在手持／消費級尺寸下不可行。PDD 把整條高壓路徑縮到零長度，**這是拓樸上的新能力，不是尺寸縮小**。
- **是否真非替代**：**是**。
- **TRL**：**9（已量產）** — TDK **CeraPlas HF**（與 relyon plasma 合作）已是商品，見本專案 02 號 dossier 記錄；**本輪未能重新取得 CeraPlas 一手 datasheet（配額用盡）**。
- **市場訊號**：應用已擴散到工業表面活化、醫療、消費（負離子產生器）[64][66]，並有以 PT 火花放電產生 NOx 的研究（農業固氮方向）[67]。
- **最大技術障礙**：**材料在放電環境下的壽命**。表面持續承受離子轟擊與臭氧氧化；且 PDD 的臭氧副產物需壓在 60 ppb 以下才符合室內使用規範，這是靠組態與製程參數控制的[66]——即**元件設計與化學安全綁在一起**，不是純電性問題。

### 4.3 密閉金屬腔的穿壁供電＋通訊（材料：硬式 PZT 塊材）

- **新能力是什麼**：**1.045 MHz 載波、穿 11 mm 鋼壁、能量傳輸效率 60%**[61]；穿壁同時傳功率與資料，讓密閉腔內可放**完全無電池、無穿孔**的監測節點[63]。
- **為什麼以前做不到**：**電磁波穿不過連續金屬**（法拉第屏蔽）。這不是效率問題，是路徑不存在。且超音波換能器的聲阻抗與金屬匹配遠優於與空氣匹配，**這是為什麼穿金屬比穿空氣效率更高**——一個反直覺但物理上正確的優勢[63]。
- **是否真非替代**：**是**（替代方案是「在壓力容器上鑽孔做氣密穿線」，那不是同一件事）。
- **TRL**：5–6（多個獨立實驗系統，含穩壓 DC 輸出[62]）。
- **市場訊號**：核能、石化壓力容器、真空腔、船舶艙壁的狀態監測。**本輪查無專門商業化公司**。
- **最大技術障礙**：**耦合面的可重複性**。系統由 IPZT／耦合層／金屬壁／OPZT／阻抗匹配網路組成[61]，效率對耦合層厚度與貼合壓力極度敏感；現場安裝（而非實驗室）的效率離散度是關鍵未知數。另，搜尋摘要中「88–93% 效率、1–3 kW」的說法**未驗證且與同批文獻的 60%、100 W 量級不一致，本文不採信**。

### 4.4 非揮發可重構聲學元件（材料：鐵電 AlScN / BaTiO₃ 薄膜）

- **新能力是什麼**：利用 AlScN 的**鐵電極化可切換**特性，讓同一顆 FBAR 的串聯共振頻率被單極性電壓**開／關**；且極化一旦設定，**移除 DC 偏壓後仍保持**（非揮發），元件本身內建記憶功能[43][44][45][46]。
- **為什麼以前做不到**：AlN 傳統上被當作「不可切換的壓電體」使用；**鐵電 AlScN 是近年才被發現**。在此之前，可重構濾波器必須靠開關 + 多組固定濾波器（面積 × N）或靠變容二極體調諧（線性度差、Q 低）。「同一顆聲學共振器兼具濾波器與非揮發記憶／開關」在材料上**過去不存在**。
- **是否真非替代**：**半**。它取代的是「開關陣列 + N 顆濾波器」，功能等價但面積與 Q 值改善是量級級的；同時它多出了**非揮發狀態保持**這個真正的新性質。
- **TRL**：3–4（多篇實驗論文 + 已有美國專利 US12476613「Filter circuitry using ferroelectric tunable acoustic resonator」、US12525955「Tunable ferroelectric acoustic resonator structure」）。
- **市場訊號**：**專利已核准是最強訊號**——代表有企業在圈地。另有單晶薄膜 BaTiO₃ 的可調鐵電聲學共振器（arXiv 2602.16102）[47]，代表這條路線不只一種材料在跑。
- **最大技術障礙**：**極化翻轉的疲勞與矯頑場**。鐵電 AlScN 的矯頑場極高（數 MV/cm 等級），翻轉電壓與 CMOS 電壓不相容、且反覆翻轉的疲勞壽命是公開的未知數。**本輪查無疲勞循環次數的具體數字。**

### 4.5 300–650 °C 環境內的「就地」主被動兩用元件（材料：BLSF / YCOB / LN-MEMS）

- **新能力是什麼**：在磁性元件（Curie 點）、電解電容、與矽半導體都已出局的溫度區間，讓同一顆元件同時做共振儲能、致動與感測。可用材料確實存在：BLSF **Tc = 648 °C 且 500 °C 時 ρ = 1.2×10⁸ Ω·cm**[51]、YCOB **800 °C 時 ρ ≈ 2×10⁸ Ω·cm 且至熔點無相變**[52][54]、以及**已實測在空氣中 500 °C 運作的 LN MEMS 共振器陣列**[34]。
- **為什麼以前做不到**：不是沒人想做，是**電阻率**。高溫下壓電體漏電，訊號被漏電流淹沒；YCOB 相對 langasite 高兩個數量級的電阻率，是這幾年才把門檻推開的關鍵。
- **是否真非替代**：**是**（在該溫區沒有可替代的被動元件可言）。
- **TRL**：2–3（材料 TRL 較高，元件層級極低）。
- **市場訊號**：航太引擎健康監測、地熱／油氣井下、SiC 功率模組內部感測。**本輪查無商業產品**。
- **最大技術障礙**：**d 常數太低**。BLSF 的 d33 = 32 pC/N 僅為硬式 PZT 的約十分之一，主動端（致動／升壓）幾乎不可用；YCOB 更低。**這個機會現實上只能做「高溫感測＋共振」，做不了「高溫致動」**——必須誠實降權。

### 4.6 CMOS 後段單晶片整合的兩用元件（材料：AlN / ScAlN）

- **新能力是什麼**：AlN 沉積溫度 < 400 °C 且無汙染[37][38]，可直接長在完成的 CMOS 上，讓共振器與其驅動／感測電路做在同一顆晶片。
- **是否真非替代**：**否／半** — 這是**整合度提升**，本質上是「更小、更便宜」。**依客戶方向限制，本項應明確降權**，只當作 4.1 與 4.4 的製造載體，不當作獨立機會。
- **TRL**：8–9（BAW/FBAR 已產業級量產），但兩用元件用法為 3–4。

---

## 5. 反面證據、失敗案例與物理上限

1. **d33 與 Qm 互斥是「兩用元件」的第一因原理級障礙。** 搜尋結果直接陳述：「d33 的提升通常伴隨 Qm 的下降，反之亦然，凸顯壓電材料設計中的根本取捨」[3]。被動角色要 Qm > 1000（硬式），主動角色要 d33 > 400 pC/N（軟式）。**沒有材料同時滿足**。任何「兩用元件」的商業提案若沒有回答「你選硬式還是軟式、犧牲哪一邊」，就是還沒開始。可用的緩解手段只有兩個：外加 DC 偏壓調變損耗特性[5]、或用高 k 的單晶硬摻雜（Mn:PIN-PMN-PT）[49]。

2. **理論功率密度與實務功率密度差 10 倍，且差距來自散熱不是材料。** 330 W/cm³ vs 33 W/cm³[56][57]。而「加裝接觸式導熱結構」被證明能提升 PT 功率密度[57]——**這反過來說明壓電元件的價值鏈重心在熱管理與封裝，不在陶瓷本身**。若客戶的競爭優勢建立在材料配方上，這是一個危險訊號。

3. **自發熱是正回饋，不是線性劣化。** 低振速時損耗由機械損耗主導（Qm 高）；振速上升後**介電損耗接手並使 Qm 劣化**，Qm 的變化可與試片溫升直接關聯[8]。溫升 → Qm 降 → 損耗增 → 溫升，這個迴路是壓電高功率應用二十年的核心難題。

4. **雜散模態直接吃掉功率轉換所依賴的電感性區間。** Stanford 團隊的原話是：聲學共振器介於串聯與並聯共振之間的電感性區間**本身就受限，又被雜散模態進一步縮小**，雜散模態引入電阻性損耗區，**劣化效率並限制電壓轉換比**[28][29]。他們的解法是加厚「主動環」抑制雜散模態[28]、以及週期性極化 LN[29]——**都是製造複雜度的增加**，不是免費午餐。這也解釋了為何 99.3% 那個亮眼數字是「並聯多顆」而非單顆。

5. **無鉛化在高功率共振領域是實質失敗，不是「還沒到」。** KNN 的問題是製程物理層級的：吸濕改變相組成[22]、Q 值與電容量對濕度敏感[21]、緻密化差、燒結溫度窗極窄、K/Na 揮發[23][24]、且電性對煅燒／燒結／極化參數「極度敏感」[23]。搜尋結果的原話是：「KNN 存在燒結相關的諸多問題，因此 PZT 化合物被偏好，因為它們用傳統陶瓷製程更容易製作」[23]。**對窄頻兩用元件（需要 <0.1% 頻率準確度）而言，「電性對製程參數極度敏感」等同於「良率不可控」**。

6. **老化率是窄頻元件的隱形殺手。** 最佳共振器級材料也只到 **0.03%/decade**（= 300 ppm/decade）[84]，而一般致動器級材料達 **4–9%/decade**[85]。共振頻率**隨老化上升**[87]。若元件的被動功能依賴精確共振（濾波、儲能匹配），300 ppm/decade 已經吃掉大部分設計餘裕；4%/decade 則完全不可用。**這也是為什麼「兩用」很難：致動用的材料等級撐不起共振用的穩定度要求。**

7. **頻率精度的成本曲線是斷崖式的。** 石英業界常規公差為 ±20 / ±50 / ±100 ppm；**±10 ppm @ −40~+85 °C 被業界描述為「除最嚴苛應用外都貴到不可行」**[82]。壓電陶瓷共振器的頻率離散度遠大於石英。因應手段是**多階段頻率修整（雷射修整）**與**在晶圓階段就標記／移除不良共振器以提早止損**[83]——換言之，**良率靠「早期剔除」而非「製程收斂」，這是成本結構上的壞消息**。

8. **封裝必須提供自由振動空間，這與低成本封裝直接衝突。** 已知的工程事實：支撐必須落在節點（nodal point），否則阻尼大增[89][90]；共振元件通常需**真空腔體**以避免外力與大氣影響[90]；氣密的**金屬鍵合封裝成本高、製程複雜**，改用便宜的絕緣膠封則會讓水氣進入、在振子表面結露[90]。**「便宜、氣密、自由振動」三者只能選兩個。本輪查無封裝占總成本的比例數字。**

9. **前例警訊：CCFL 背光用壓電變壓器的市場崩塌。** 見本專案 02 號 dossier 記錄（MDPI Actuators 5(2), 12）：2000 年代初期 25–30% 的 CCFL 背光採用壓電變壓器，LCD 背光轉 LED 後出貨崩跌、多數主要供應商停產、連專用 IC 都停產。**教訓是：壓電元件的市場依附於一個特定的「非電磁優勢窗口」，窗口一關，整條供應鏈同時消失。** 本輪的搜尋摘要也重述了這段歷史，並補上材料層面的原因：PZT Rosen 型變壓器受制於**高介電損耗與大驅動下的熱不穩定**[32]。

10. **多層元件的成本由電極主導，且與層數同步上升。** 明確陳述：「隨著致動器堆疊層數增加，電極成本主導元件總成本」[68]。高於 1200 °C 燒結通常需要**昂貴的鉑**作為內電極[70]；改用賤金屬（Ag、Cu、Ni）是主要降本手段——TDK 的**銅內電極**技術已在汽車噴油系統用了 20 年以上，且對濕氣的耐受性與壽命優於傳統 Ag/Pd[69]；Ni 內電極則具高抗電遷移、與陶瓷高界面強度、成本優於 Ag/Pd[20]。**但賤金屬電極必須在低氧分壓下燒結**，這正是 Murata 開發無鉛多層壓電致動器時發現「KNN 系可在低氧分壓下緻密燒結」的價值所在[26，行銷型來源，未驗證]。

11. **薄膜路線的頻率上限是物理性的。** AlN BAW 在 1.578 GHz 有 Qmax = 3346，到 16 GHz 只剩 ≈ 363[39]；劣化來自**四個獨立機制同時惡化**：泛音模態的機電耦合下降、Akhiezer damping 隨頻率上升、膜變薄導致結晶性下降、以及壓電層與電極層變薄導致聲學與電性損耗增加[39]。薄膜 LN 在 50.74 GHz 的 Q 僅 237、57 GHz 僅 56[32][33]。**「更高頻 → 更小 → 更好」在聲學元件上不成立**，這與半導體的直覺相反。

---

## 6. 未解問題（給下一輪研究）

1. **RoHS 7(c)-VI 的續期申請是否已在 2026-06-30 前提出？由誰提出？** 這決定 PZT 在歐盟市場是 2027-12-31 硬截止還是可再展延。**必須查 EU Commission / Oeko-Institut 的 exemption evaluation 公開文件**。若無人申請續期，客戶的整個 PZT 路線在歐盟有 17 個月的壽命。
2. **PZT 元件的實際成本拆解（材料／燒結／後加工／極化／測試分選／封裝）與量產曲線。** 本輪完全查無。建議下一輪直接查具體型號的分銷商階梯價（如 Digi-Key 上 TDK PowerHap、CeraPlas、Murata 陶瓷共振器的 1/100/1000/10000 pcs 價格），**用價格階梯反推固定成本占比**，這比找不到的成本報告更可靠。
3. **窄頻壓電陶瓷元件（非石英）的實際頻率分佈標準差與分選良率。** 這是「兩用元件」商業模式成立與否的單一最關鍵數字。建議查 Murata 陶瓷共振器（CSTCE 系列）的 initial tolerance 規格（業界公開值約 ±0.07%~±0.5%，**本輪未驗證**）並與應用需求對照。
4. **鐵電 AlScN 的極化翻轉疲勞壽命（循環次數）與翻轉電壓。** 4.4 節機會的成敗完全繫於此，本輪查無。
5. **薄膜 LN / ScAlN SAW 元件的實際連續功率處理上限（W 而非 dBm）與熱失效模式。** 4.1 節機會的成敗繫於此。
6. **VTT、X-FAB 是否提供 piezoMEMS 代工**（本輪配額用盡未查），以及各家代工的 NRE 與最小批量報價。

---

## 7. 來源清單

> 標註說明：【行銷】= 廠商行銷或內容農場來源，不可作決策依據；【未驗證】= 僅見於搜尋摘要、未經一手核對。**本文所有來源均因 WebFetch 遭封鎖而未取得一手全文，皆屬「搜尋摘要層級」證據。**

### 硬式 PZT 與高功率特性
1. APC International — Piezo Materials For High Power Applications — https://www.americanpiezo.com/apc-materials/apc-materials-for-high-power-applications/ — APC 841/880 高功率材料定位與特性描述。
2. APC International — Physical & Piezoelectric Properties of Products — https://www.americanpiezo.com/apc-materials/physical-piezoelectric-properties/ — APC 全系列材料參數表入口。
3. PZT Electronic Ceramic Co. — Physical and Piezoelectric Properties of APC Materials — https://www.piezoelements.com/info/physical-and-piezoelectric-properties-of-apc-m-34218509.html — 記載 APC840/841/880 量測值，並直述「d33 上升伴隨 Qm 下降」的取捨。
4. Penn State — Time dependence of the mechanical quality factor in hard lead zirconate titanate — https://pure.psu.edu/en/publications/time-dependence-of-the-mechanical-quality-factor-in-hard-lead-zir/ — 硬式 PZT 極化後 Qm 隨時間顯著上升。
5. Penn State — Improving high-power properties of PZT ceramics by external DC bias field — https://pure.psu.edu/en/publications/improving-high-power-properties-of-pzt-ceramics-by-external-dc-bi/ — DC 偏壓可作為調變高功率特性的操作旋鈕。
6. Nature Communications (2025) — High-power performance enhancement in PZT-based piezoceramics via hot-pressing — https://www.nature.com/articles/s41467-025-64752-w （另 PMC 版 https://pmc.ncbi.nlm.nih.gov/articles/PMC12589483/）— 熱壓 PZT 最大振動速度 2.5 m/s vs 常規燒結 1.7 m/s。
7. J. Alloys Compd. — A high-power piezoelectric ceramic with great electrical properties and temperature stability — https://www.sciencedirect.com/science/article/abs/pii/S0925838824029499 — PMS-PZT 安全振動速度 1100 mm/s。
8. J. Mater. Res. Technol. — Characterization of high-power mechanical quality factor of piezoelectric ceramic discs under self-heating condition — https://www.sciencedirect.com/science/article/pii/S2238785423003836 — 振速上升後介電損耗接手、Qm 劣化與溫升直接關聯。
9. ResearchGate — Thermal Conductivities of PZT Piezoelectric Ceramics under Different Electrical Boundary Conditions — https://www.researchgate.net/publication/342631237_Thermal_Conductivities_of_PZT_Piezoelectric_Ceramics_under_Different_Electrical_Boundary_Conditions — 熱導率隨電性邊界條件變化（**具體數值本輪查無**）。
10. US Patent 7,772,746 — Thermoacoustic piezoelectric generator — https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/7772746 — PZT-8 功率密度公式與 23 W/cm³ 估算、E₃max 8 kV/cm、T₃max 7000 psi。
11. ResearchGate — Measurement and Modelling of Self-Heating in Piezoelectric Materials and Devices — https://www.researchgate.net/publication/236019015_Measurement_and_Modelling_of_Self-Heating_in_Piezoelectric_Materials_and_Devices — 自發熱建模。
12. ScienceDirect — Co-sintered PZT ceramics for the piezoelectric transformers — https://www.sciencedirect.com/science/article/abs/pii/S0272884215006902 — 壓電變壓器用共燒 PZT。

### RoHS 無鉛法規
13. RoHS Guide — RoHS Annex 3 Lead Exemptions 2025–2027 — https://www.rohsguide.com/rohs-lead-exemptions.htm — 7(c)-I 豁免至 2027-06-30。
14. CIRS Group — EU RoHS Directive Update: Comprehensive Refinement of Lead Exemption Clauses — https://www.cirs-group.com/en/chemicals/eu-rohs-directive-update-comprehensive-refinement-of-lead-exemption-clauses — 2025-09-08 通過三項授權指令；新增 7(c)-V、7(c)-VI；7(c)-VI 涵蓋 PZT 與 PTC 陶瓷，至 2027-12-31。
15. Assent — Final Delegated Directives for Key RoHS Lead Exemptions Adopted — https://www.assent.com/blog/draft-expiry-dates-for-key-rohs-lead-exemptions-published/ — 續期申請須期滿前 18 個月提出。
16. TÜV SÜD — EU comprehensive updates to lead exemptions under RoHS directive — https://www.tuvsud.com/en/knowledge-hub/technical-updates/consumer-products-and-retail-essentials/eu-comprehensive-updates-to-lead-exemptions-under-rohs-directive — 成員國轉置期限 2026-06-30、2026-07-01 生效。
17. APC International — RoHS Exemption for Lead Updates — https://www.americanpiezo.com/blog/rohs-exemption-for-lead-update/ — 壓電廠商視角的豁免解讀。【行銷】
18. EcoComply — RoHS Exemptions 2026–2027 — https://ecocomply.ai/blog/rohs-exemptions-2026 — 期限彙整。【未驗證】

### 無鉛材料（KNN / BNT / BCTZ）
19. arXiv 2502.20250 — Environment-friendly technologies with lead-free piezoelectric materials: a review — https://arxiv.org/html/2502.20250v1 — 無鉛材料綜述；列出 TDK、Murata、PI Ceramic、Morgan 為主要產業玩家。
20. PMC5458925 — Potassium Sodium Niobate-Based Lead-Free Piezoelectric Multilayer Ceramics Co-Fired with Nickel Electrodes — https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5458925/ — Ni 內電極的抗電遷移、界面強度與成本優勢。
21. PMC8348597 — Processing Optimization and Toxicological Evaluation of "Lead-Free" Piezoceramics: A KNN-Based Case Study — https://pmc.ncbi.nlm.nih.gov/articles/PMC8348597/ — KNN 吸濕、Q 與電容量對濕度敏感。
22. CTS Denmark (前 Ferroperm) — New knowledge of humidity could unlock lead-free piezoelectric ceramics — https://www.ferropermpiezoceramics.com/articles/new-knowledge-of-humidity-could-unlock-lead-free-piezoelectric-ceramics/ — 鹼金屬碳酸鹽吸水生成水合物改變相組成。
23. J. Appl. Phys. 127, 190901 — Perovskite lead-free piezoelectric ceramics — https://pubs.aip.org/aip/jap/article/127/19/190901/153538/Perovskite-lead-free-piezoelectric-ceramics — 「KNN 燒結問題多，故偏好 PZT」；電性對製程參數極度敏感。
24. PMC5458861 — Sintering of Lead-Free Piezoelectric Sodium Potassium Niobate Ceramics — https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5458861/ — 緻密化差、燒結窗窄、K/Na 揮發。
25. ScienceDirect — Improving non-sensitivity of sintering behavior in KNN-based ceramics via Fe2O3 doping — https://www.sciencedirect.com/science/article/abs/pii/S0925838823015918 — 燒結敏感度的緩解手段。
26. Semiconductorinsight — CeramTec, Murata, and TDK Signal Shift — https://semiconductorinsight.com/blog/ceramtec-murata-and-tdk-signal-shift-large-scale-and-lead-free-piezoelectric-ceramics-on-the-rise/ — Murata 賤金屬內電極無鉛多層致動器、KNN 可在低氧分壓緻密燒結。【行銷】【未驗證】
27. PatSnap — Lead-free piezoelectric materials 2026: BaTiO₃, KNN, PVDF — https://www.patsnap.com/resources/blog/articles/lead-free-piezoelectric-materials-2026-batio%E2%82%83-knn-pvdf/ — 「KNN 變種達 d33 = 220 pC/N」「某廠 2024 擴產 40%」等說法出處。【行銷】【未驗證，不可採信】

### 鈮酸鋰（LiNbO3）
28. arXiv 2409.15686 — Lithium Niobate Resonators for Power Conversion: Spurious Mode Suppression Via an Active Ring — https://arxiv.org/pdf/2409.15686 — Q = 4178、kt² = 29%；750 kHz/100 W/99.3% 並聯徑向模態原型；電感性區間受雜散模態壓縮。
29. arXiv 2508.09407 — Periodically Poled Piezoelectric Lithium Niobate Resonator for Piezoelectric Power Conversion — https://arxiv.org/pdf/2508.09407 — 週期性極化 LN 作為抑制雜散模態的製造解法。
30. arXiv 2511.17431 — Radial Mode Lithium Niobate Rosen Transformer — https://arxiv.org/pdf/2511.17431 — LN 取代 PZT 做 Rosen 型變壓器；PZT Rosen 型受制於高介電損耗與大驅動熱不穩定。
31. arXiv 2407.17693 — Low Temperature Properties of Low-Loss Macroscopic Lithium Niobate Bulk Acoustic Wave Resonators — https://arxiv.org/html/2407.17693 — 少量重離子雜質限制 LN BAW 性能。
32. ResearchGate — 57 GHz Acoustic Resonator with k² of 7.3% and Q of 56 in Thin-Film Lithium Niobate — https://www.researchgate.net/publication/367367766_57_GHz_Acoustic_Resonator_with_k_2_of_73_and_Q_of_56_in_Thin-Film_Lithium_Niobate — mmWave 薄膜 LN 的 Q 崩壞。
33. ResearchGate — Thin-Film Lithium Niobate Acoustic Resonator with High Q of 237 and k² of 5.1% at 50.74 GHz — https://www.researchgate.net/publication/374579734_Thin-Film_Lithium_Niobate_Acoustic_Resonator_with_High_Q_of_237_and_k_2_of_51_at_5074_GHz — 同上；並記載 Qm ≤ 380、功率處理 > 20 dBm。
34. PMC7795216 — A Laterally Vibrating Lithium Niobate MEMS Resonator Array Operating at 500 °C in Air — https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7795216/ — LN MEMS 在空氣中 500 °C 運作。

### AlN / ScAlN 薄膜
35. Nature Communications (2025) — Unprecedented enhancement of piezoelectricity of wurtzite nitride semiconductors via thermal annealing — https://www.nature.com/articles/s41467-025-59179-2 — d33 由 12.3 提升至 45.5 pC/N（3.5×，約商用 AlN 的 8×）。
36. Microsystems & Nanoengineering — Aluminum scandium nitride thin-film bulk acoustic resonators for 5G wideband applications — https://www.nature.com/articles/s41378-022-00457-0 （PMC9705400）— Sc 40% 時 d33 = 28 pC/N、−d31 = 13 pm/V；BAW k² = 15.5%（AlN 的 2.6×）。
37. Int. Mater. Rev. / Taylor & Francis — Piezoelectric aluminum nitride thin films for CMOS compatible MEMS: Sputter deposition and doping — https://www.tandfonline.com/doi/full/10.1080/10408436.2024.2406247 — AlN 沉積 < 400 °C、CMOS 相容、環境穩定、低遲滯。
38. Microsystems & Nanoengineering (2025) — Recent progress in aluminum nitride for piezoelectric MEMS mirror applications: enhancements with scandium doping — https://www.nature.com/articles/s41378-025-01053-8 — ScAlN 於 piezoMEMS 的定位。
39. ScienceDirect — Simulation and preparation of FBARs based on AlN thin films — https://www.sciencedirect.com/science/article/abs/pii/S1369800124007820 — Qmax 3346 @1.578 GHz、16 GHz ≈ 363；膜厚 1000→250 nm FWHM +10%、→100 nm >20%；建議 >200 nm；Akhiezer damping。
40. arXiv 2311.13448 — Millimeter Wave Thin-Film Bulk Acoustic Resonator in Sputtered Scandium Aluminum Nitride Using Platinum Electrodes — https://arxiv.org/pdf/2311.13448 — ScAlN mmWave FBAR。
41. arXiv 2604.13364 — Cryogenic Loss Limits in Microwave Epitaxial AlN Acoustic Resonators — https://arxiv.org/pdf/2604.13364 — AlN 的本質損耗極限。【未驗證】
42. ResearchGate — A K-Band Bulk Acoustic Wave Resonator Using Periodically Poled Al0.72Sc0.28N — https://www.researchgate.net/publication/371229434_A_K-Band_Bulk_Acoustic_Wave_Resonator_Using_Periodically_Poled_Al_072_Sc_028_N — 週期性極化 AlScN。

### 鐵電 AlScN 可切換／可調共振器
43. Wiley phys. status solidi RRL (2021) — Ferroelectric Aluminum Scandium Nitride Thin Film Bulk Acoustic Resonators with Polarization-Dependent Operating States — https://onlinelibrary.wiley.com/doi/10.1002/pssr.202100034 — Sc≈30% AlScN FBAR 的首次頻率調諧與本質極化切換。
44. IET Electronics Letters (2025) — Switchable Bulk Acoustic Resonator Based on AlN/Al0.7Sc0.3N Films — https://ietresearch.onlinelibrary.wiley.com/doi/abs/10.1049/ell2.70241 — 雙層 AlN/AlScN 以 DC 偏壓切換頻率。
45. US Patent 12,476,613 — Filter circuitry using ferroelectric tunable acoustic resonator — https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/12476613 — 非揮發性：移除 DC 偏壓後極化保持。
46. US Patent 12,525,955 — Tunable ferroelectric acoustic resonator structure — https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/12525955 — 同族專利。
47. arXiv 2602.16102 — Tunable Ferroelectric Acoustic Resonators in Monolithic Thin-Film Barium Titanate — https://arxiv.org/pdf/2602.16102 — 另一條可調鐵電聲學路線。【未驗證】

### 單晶（PMN-PT 家族）
48. AIP J. Appl. Phys. 120, 074105 — [111]-oriented PIN-PMN-PT crystals with ultrahigh dielectric permittivity — https://pubs.aip.org/aip/jap/article/120/7/074105/167270/ — PMN-PT 與 PIN-PMN-PT 的 d33/k33/Ec/Trt 對照。
49. Penn State ETDA — Effect of Manganese Doping on PIN-PMN-PT Single Crystals for High Power Applications — https://etda.libraries.psu.edu/catalog/22485 — Mn 摻雜為高功率單晶的主要路線。
50. AIP APL Materials 13, 071106 (2025) — Optimized orientation of PIN-PMN-PT single crystal via anisotropic structural engineering — https://pubs.aip.org/aip/apm/article/13/7/071106/3351158/ — 取向工程。

### 高溫材料
51. PMC11642524 — Simultaneously Achieved High Piezoelectricity and High Resistivity in Na0.5Bi4.5Ti4O15-Based Ceramics with High Curie Temperature — https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11642524/ — d33 = 32.0 pC/N、500 °C 時 ρ = 1.2×10⁸ Ω·cm、Tc = 648 °C。
52. PMC3926551 — High-Temperature Piezoelectric Sensing — https://pmc.ncbi.nlm.nih.gov/articles/PMC3926551/ — GaPO4 <700 °C、langasite 至 1000 °C、YCOB 800 °C 時 ρ ≈ 2×10⁸ Ω·cm、至 ~1500 °C 無相變。
53. Prog. Mater. Sci. — Ultra-high temperature piezoelectric crystals: Properties, structures and applications — https://www.sciencedirect.com/science/article/abs/pii/S0079642525001343 — 超高溫壓電晶體綜述。
54. Sensors & Actuators A — Design, fabrication and characterization of high temperature piezoelectric vibration sensor using YCOB crystals — https://www.sciencedirect.com/science/article/abs/pii/S0924424712000891 — YCOB 高溫振動感測器實作。
55. Acta Materialia — Synergy ascension of piezoresponse and Curie temperature in bismuth-layered ceramics via defect engineering — https://www.sciencedirect.com/science/article/abs/pii/S1359645425003970 — BLSF 缺陷工程。

### 壓電變壓器與功率密度
56. Sensors & Actuators A — Optimal design of piezoelectric transformer for high efficiency and high power density — https://www.sciencedirect.com/science/article/abs/pii/S0924424705001585 — 理論 330 W/cm³ vs 實務 33 W/cm³。
57. ResearchGate — Power Density of Piezoelectric Transformers Improved Using a Contact Heat Transfer Structure — https://www.researchgate.net/publication/221794976_Power_Density_of_Piezoelectric_Transformers_Improved_Using_a_Contact_Heat_Transfer_Structure — 功率密度上限由散熱決定的直接證據。
58. DTIC ADA429524 — Piezoelectric Transformers for Space Applications — https://apps.dtic.mil/sti/tr/pdf/ADA429524.pdf — 軍規／太空應用評估。
59. ScienceDirect — Voltage gain characteristics of piezoelectric transformer using PbTiO3 system ceramics — https://www.sciencedirect.com/science/article/abs/pii/S0924424799000783 — 升壓比特性。

### 隔離與穿壁能量傳輸
60. arXiv 2511.13412 — Microwave-acoustic-based isolated gate driver for power electronics — https://arxiv.org/pdf/2511.13412 — 隔離 2.75 kV、隔離電容 0.032 pF、聲程 1.25 mm、驅動 650 V/11 A GaN HEMT 導通 108.8 ns；並直述傳統 PT 因 Qm≈1000、頻寬僅數十 kHz 而不適用 WBG。
61. MDPI Micromachines 15(1), 48 — Optimized Design of an Ultrasonic-Based High-Efficiency Wireless Passive Monitoring System for Sealed Metal Compartments — https://doi.org/10.3390/mi15010048 （PMC10820569）— 1.045 MHz、11 mm 鋼壁、效率 60%；系統由 IPZT/耦合器/金屬壁/OPZT/匹配網路組成。
62. MDPI Appl. Sci. 8(5), 692 — An Ultrasonic Through-Metal-Wall Power Transfer System with Regulated DC Output — https://www.mdpi.com/2076-3417/8/5/692 — 穿壁供電並穩壓輸出。
63. Ultrasonics (2021) — Ultrasonic wireless power links for battery-free condition monitoring in metallic enclosures — https://www.sciencedirect.com/science/article/abs/pii/S0041624X21000366 — 無電池腔內監測；超音波對金屬的聲阻抗匹配優於對空氣。

### 壓電直接放電（冷電漿）
64. Wikipedia — Piezoelectric direct discharge plasma — https://en.wikipedia.org/wiki/Piezoelectric_direct_discharge_plasma — PDD 定義與 PT 表面直接放電機制。【未驗證，僅作概念定位】
65. Wiley Plasma Processes and Polymers (2020), Korzec et al. — Atmospheric pressure plasma jet powered by piezoelectric direct discharge — https://onlinelibrary.wiley.com/doi/full/10.1002/ppap.202000053 — PDD 電漿噴流。
66. MDPI Plasma 4(3), 29 — Generation of Negative Air Ions by Use of Piezoelectric Cold Plasma Generator — https://www.mdpi.com/2571-6182/4/3/29 — PCPG 升壓比 >1000、輸入 <25 V、輸出 >10 kV；臭氧可壓在 60 ppb 以下。
67. AIP Physics of Plasmas 32, 063502 — Production of nitrogen oxides by spark discharges in air generated by a piezoelectric transformer — https://pubs.aip.org/aip/pop/article/32/6/063502/3348034/ — PT 火花放電產生 NOx。

### 多層製造與電極
68. ResearchGate / Actuators — Base Metal Co-Fired Multilayer Piezoelectrics（綜述） — https://www.researchgate.net/publication/296625421_Base_Metal_Co-Fired_Multilayer_Piezoelectrics — 「層數增加後電極成本主導總成本」。
69. TDK Electronics — Multilayer Piezo Actuator Stacks — https://www.tdk-electronics.tdk.com/en/542398/products/product-catalog/switching-heating-piezo-components-buzzers-microphones/multilayer-piezo-actuator-stacks — 銅內電極專利技術，汽車噴油系統使用逾 20 年，抗濕與壽命優於 Ag/Pd。
70. ScienceDirect — A low-cost multilayer piezoelectric actuator fabricated by a low-temperature co-fired ceramic process — https://www.sciencedirect.com/science/article/abs/pii/S0272884222036847 — >1200 °C 燒結需鉑內電極；LTCC 降本路線。
71. ScienceDirect — Effects of structural design on the performance of low-temperature co-fired multilayer piezoelectric ceramic actuators — https://www.sciencedirect.com/science/article/abs/pii/S0921510724006937 — LTCC 多層結構設計。

### 薄膜製程與代工
72. SINTEF (Tyholdt) — Industrial fabrication of piezoMEMS — https://www.sintef.no/globalassets/project/piezovolume/publications/industrial-fabrication-of-piezomems_tyholdt.pdf — 濺鍍 PZT d33,f ≈ 110 pm/V、e31,f ≈ −20 C/m²；厚度 200 nm–5 µm、2 µm 為成本標準；高速濺鍍 2–8 µm。
73. CORDIS — PiezoVolume (FP7, grant 229196) — https://cordis.europa.eu/project/id/229196/reporting — d33,f >100 pm/V、|e31,f| >14 C/m² 於 150/200 mm 達成；250 mm 寬矩形陰極。
74. ScienceDirect — Piezoelectric properties of PZT films prepared by the sol–gel method and their application in MEMS — https://www.sciencedirect.com/science/article/abs/pii/S0040609007011431 — sol-gel 0.7–2.2 µm，e31 = −12.5 ± 0.3 C/m²。
75. AIP J. Appl. Phys. 137, 020702 (2025) — Piezoelectric thin films and their applications in MEMS: A review — https://pubs.aip.org/aip/jap/article/137/2/020702/3330689/ — 薄膜壓電綜述。
76. Silex Microsystems — Technologies — https://www.silexmicrosystems.com/en/mems-foundry/technologies/ — PZT 與 AlN 代工逾 15 年；與 ULVAC 合作濺鍍 PZT。
77. Europractice — Europractice starts offering SINTEF's Piezoelectric MEMS fabrication services through imec — https://europractice-ic.com/sintef/ — MPB 每批 3–12 片 6 吋晶圓。
78. Rogue Valley Microdevices — MEMS Foundry — https://roguevalleymicrodevices.com/mems-foundry/ — 美國本土 MEMS 代工與 wafer service。
79. I-PEX — Piezoelectric MEMS Foundry Service — https://www.i-pex.com/ips/products/mems_foundry — PZT 與無鉛材料壓電沉積代工。
80. ROHM — Thin-Film Piezo MEMS Foundry — https://www.rohm.com/foundry-service/thin-film-piezoelectric-mems — 薄膜壓電 MEMS 代工。

### 頻率精度、老化與封裝
81. Siward — Frequency Tolerance vs Frequency Stability — https://www.siward.com/en/about/industry/Frequency_Tolerance_vs_Frequency_Stability__A_Detailed_Look_into_Quartz_Crystal — ±20/±50/±100 ppm 常規公差；消費 ±50 ppm、通訊基建 ±10 ppm。
82. All About Circuits — Characterizing Frequency Deviations of Quartz Crystals — https://www.allaboutcircuits.com/technical-articles/characterizing-frequency-deviations-of-quartz-crystals-frequency-tolerance-frequency-stability-and-aging/ — 「±10 ppm @ −40~+85 °C 除最嚴苛應用外貴到不可行」；IC 內建可調電容為業界修整手段。
83. US Patent 8,122,587 — Manufacturing method of quartz crystal unit — https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/8122587 — 晶圓階段標記/移除不良共振器以提高良率。
84. US Patent 4,384,229 — Temperature compensated piezoelectric ceramic resonator unit — https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/4384229 — 傳統壓電陶瓷共振器穩定度上限 0.03%/decade。
85. Noliac — Dictionary — http://www.noliac.com/dictionary/ — NCE51/51F 老化 4%/decade、NCE46 9%/decade。
86. ScienceDirect — Effects of temperature on aging degradation of soft and hard lead zirconate titanate ceramics — https://www.sciencedirect.com/science/article/abs/pii/S0272884217307502 — 軟式（Nb 摻雜 PZT-5A 型）Tc 360 °C、硬式（Fe 摻雜 PZT-4 型）Tc 325 °C；老化速率隨熱處理溫度上升。
87. Springer Adv. Compos. Hybrid Mater. — Aging effects on resonance frequency of Pb(Ti0.52Zr0.48)O3 piezoelectric ceramics for power ultrasonic transducers — https://link.springer.com/article/10.1007/s42114-021-00239-8 — 共振頻率隨老化上升。
88. Morgan Electro Ceramics TP-226 (Berlincourt) — Properties of Piezoelectricity Ceramics — https://www.ultrasonic-resonators.org/misc/references/articles/Berlincourt__'Properties_of_Morgan_Electro_Ceramic_Ceramics'_(Morgan_Technical_Publication_TP-226).pdf — 壓電陶瓷性質經典技術文件。
89. US Patent 6,563,400 — Piezoelectric resonator utilizing bending vibrations and ladder-type filter — https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/6563400 — 外電極置於節點可降低安裝阻尼。
90. US Patent 8,330,336 — Piezoelectric vibration component — https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/8330336 — 金屬氣密封裝成本高、製程複雜；便宜絕緣膠封會讓水氣進入並結露。
91. Ultrasonic Resonators — Piezoelectric transducer design — https://www.ultrasonic-resonators.org/design/transducers/transducer_design.html — 節點支撐的工程慣例。
