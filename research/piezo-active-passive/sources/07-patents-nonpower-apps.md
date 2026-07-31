# 專利地景二：壓電高壓產生、電漿、致動器驅動、隔離、超音波供電

> 一句話結論：在「非電感替代」的方向上，唯一已經被專利與量產型號**雙重驗證**的壓電主動/被動兩用元件是 TDK/EPCOS 的 CeraPlas（壓電變壓器＋電漿源合一，US10856399B2 等家族，產品型號 CeraPlas HF、relyon plasma piezobrush PZ3）；而潛在價值最大、專利白區也最大的，是「**聲學隔離**（穿牆／跨絕緣障壁的功率＋訊號同體傳輸）」與「**超音波遠端供電植入物**」這兩條路——前者的物理優勢（0.03 pF 等級耦合電容、金屬遮蔽下 EM 完全失效）是磁性與電容式元件在物理上做不到的，後者已有 Astellas 以約 3.04 億美元收購 Iota Biosciences 的市場訊號。

---

## 0. 研究方法與限制（誠實揭露）

- **WebFetch 在本環境被 egress policy 全面封鎖**（任何 URL 回 403），因此完全未使用，所有事實均來自 WebSearch 回傳的「連結清單＋摘要」。
- **實際只執行了 16 次 WebSearch**，遠低於原計畫的 25–35 次。原因：本 session 的 WebSearch 配額（200 次）由多個平行 agent 共用，在我的第 17 次查詢時已達上限並被系統拒絕。以下主題**未能查證，屬於本報告的已知缺口**：
  - EBR Systems WiSE-CRT（超音波供電無導線左心室起搏）的專利號與 FDA 核准狀態 —— **完全未查，勿引用**
  - Medtronic / Cochlear / Boston Scientific 的超音波供電植入物專利
  - Analog Devices / Texas Instruments / Silicon Labs 是否持有壓電（非 FBAR）隔離專利
  - Philips / Sharp / Canon 在壓電變壓器高壓電源的專利族規模
  - EP3127172B1、US10531552、US10827599、US10966309、US10772182、US20200305266、US9287080 的**權利人與法律狀態（是否仍有效）未經查證**
  - 日文／德文／中文關鍵字查詢完全未執行
  - CeraPlas 的**壽命、失效模式、單價**：查了一次，官方與媒體資料**均未揭露**，屬「查無」
- **專利號真偽說明**：本報告所列每一個專利號都出現在 WebSearch 回傳的 Google Patents / USPTO / Justia 連結標題中，**號碼本身可信**；但「權利人」「年份」欄位只有明確標註來源的才算已驗證，其餘一律標「未驗證」。**沒有任何一個專利號是我編造的。**
- 專利密度（件數）**無法量化**：本環境無法執行專利資料庫檢索式（如 Espacenet/Lens.org 的 CPC 統計），下列「密度」評估是依據搜尋結果的重複出現頻率所做的**質性判斷**，不是統計數字。

---

## 1. 結論摘要

1. **CeraPlas 是本領域唯一「專利＋量產型號」同時存在的產品化訊號。** TDK Electronics AG（前身 EPCOS AG）持有至少 6 件相關美國專利，代表件 **US10856399B2「Device for generating an atmospheric-pressure plasma」**，發明人 Pavol Kudela、Franz Rinner、Markus Puff，2020-12-01 公告（已驗證）；對應產品 **CeraPlas HF**（2018-11 上市，47.3 × 20 × 20 mm）與子公司 relyon plasma 的 **piezobrush PZ2（2014，全球第一個 CeraPlas 產品）／PZ3**。
2. **CeraPlas 的真正新能力不是「省掉電感」，而是「省掉整個高壓子系統」。** 官方資料：以 **12–24 Vpp、50 kHz** 正弦訊號驅動，即可在輸出端**直接在空氣中**點燃冷電漿，元件表面溫度 **< 50 °C**，且「無需針對高壓做特別的安全防護措施即可整合」。這是傳統「高壓變壓器＋高壓佈線＋高壓連接器＋爬電距離」架構在物理上做不到的——高壓從未離開陶瓷體。
3. **功率窗極窄**：CeraPlas HF 評估套件預設輸入功率約 **4.5 W**，軟體可選 **約 2–7 W**，單一 24 V 供電；手持機 piezobrush PZ3 整機最大消耗 **18 W**。這定義了此類元件的天花板——**個位數瓦特級**，不是製程設備級。
4. **聲學隔離已有 20 年前的專利先例但未成主流。** **US7525398「Acoustically communicating data signals across an electrical isolation barrier」**，權利人 **Avago Technologies General IP (Singapore)**，發明人 John D. Larson III 等（已驗證；同族 WO2007047701A2）。Avago（今 Broadcom）以 FBAR 做隔離障壁，20 年來未見成為主流隔離器技術——這是重要的**失敗／未起飛訊號**。
5. **物理優勢是真的，且極大。** 2026 年 Communications Engineering 論文（微波聲學隔離閘極驅動器）實測：LiNbO₃ SAW 元件在 **1.25 mm** 機械傳播距離上達成 **2.75 kV 隔離、隔離電容僅 0.032 pF**，輸出 13.4 V 開路電壓／44.4 mA 短路電流，驅動 GaN HEMT 導通時間 108.8 ns。對比業界最好的磁性方案（Würth WE-AGDT 繞組間電容**低至 7 pF**），**低了兩個數量級以上**。在 SiC 100 kV/µs 的 dv/dt 下，10 pF 會產生 1 A 位移電流——這是磁性元件的硬牆。
6. **但傳統體聲波壓電變壓器（PT）做閘極驅動在頻寬上被判死刑。** 同一篇論文明確指出：現有 PT 工作頻率在數十 MHz 以下、機械 Q 值高，導致**固有頻寬只有數十 kHz**，「不足以應付寬能隙功率元件所需的次微秒切換」。這是本領域最重要的一條反面證據——它同時解釋了為何要跳到 GHz 級 SAW/BAW。
7. **超音波供電植入物有明確的資金與法規訊號。** UC Berkeley（Maharbiz／Carmena）的 neural dust 專利族包含 **US10118054、US10300309B2、US10300310B2、US10682530B2**（已驗證為 Regents of the University of California）；衍生公司 Iota Biosciences 2017 成立，**2020-10 被 Astellas 以 1.275 億美元頭期＋最高 1.765 億美元里程碑（合計約 3.04 億美元）收購，另承諾 5 年投入 1.25 億美元**；2024 年取得 FDA IDE，進行膀胱壁刺激（underactive bladder）早期可行性試驗。
8. **穿金屬牆供電＋通訊的實測數字已相當可觀**：文獻報導可達 **15 Mbps 資料率、30 W 功率**穿越平板金屬牆；另一系統在 **6.3 cm 厚鋼塊**上同時達成 **12.4 Mbps ＋ 32.5 W AC**。理由是 Faraday 屏蔽讓所有 EM 無線供電方案在金屬障壁上直接歸零——這是純粹的 non-substitutional 場景。

---

## 2. 現況：技術 / 產品 / 玩家

### 2.1 壓電變壓器高壓產生（最老、最擁擠的分支）

- 起源：Rosen、Fish、Rothenberg 的 **US2,830,274**，1954 年申請（來源：Actuators 期刊歷史回顧，MDPI 2016, 5(2), 12）。
- 第一個大量產應用是 **CCFL 背光逆變器**。1980 年代末 NEC、Matsushita 等日商投入；**2000 年代初期，全球 25–30% 的 CCFL 背光電路採用壓電變壓器**，Toshiba、NEC、Hitachi、Panasonic、Apple 的筆電都用過（同上來源）。
- 影像設備高壓電源：**US8040018B2「Piezoelectric transformer type high-voltage power apparatus and image forming apparatus」**（帶輸出電壓偵測回授），權利人未驗證但標題明示為影印機／印表機帶電裝置用途；早期件 **US5736807**（電視偏轉裝置＋影印機帶電裝置）。
- 這個分支**專利密度極高、白區極少、且主市場已死**（CCFL → LED）。

### 2.2 電漿生成（唯一有現役量產品的分支）

- **TDK / EPCOS + relyon plasma（TDK 子公司，德國 Regensburg）** 是絕對主導者。
- 技術結構（已驗證，TDK 技術文章）：多層 **Rosen 型**壓電變壓器，**輸入側為多層結構、內電極為銅（可與硬質 PZT 共燒）**，**輸出側為單體（monolithic）結構**；於 TDK 奧地利 Deutschlandsberg 陶瓷元件能力中心開發。
- 產品線：CeraPlas HF 元件 → CeraPlas HF Evaluation Kit → CeraPlas ExploreKit（去污應用）→ piezobrush PZ2/PZ3 手持機。通路可見於 Mouser、key-components 等。
- relyon 將此放電模式命名為 **PDD®（Piezoelectric Direct Discharge）**，並發表於 Korzec 等人 *Plasma Processes and Polymers* (2020) 與 MDPI *Plasma* 4(2), 19「Multi-Device Piezoelectric Direct Discharge for Large Area Plasma Treatment」。
- 應用外溢：氣溶膠帶電（Aerosol Charging with a Piezoelectric Plasma Generator, 2021）、靜電消除、表面活化（塑膠／金屬／天然材料的接著、印刷、塗裝前處理）、醫療去污。

### 2.3 離子產生／靜電消除（利基但穩定）

- **US7821762B2 / US20090135538A1 / CN101442871B「Piezoelectric transformer type ionizer and neutralization method」，權利人 SMC Corporation**（來源指出 2008 年讓與 SMC；標題與號碼已驗證，讓與細節未獨立驗證）；日本同族 **JP2009129673A**。
- 市場玩家：Simco-Ion、Panasonic、KEYENCE、KASUGA DENKI、OMRON、Fraser、SMC、NRD 等。**注意：無法確認這些公司的現售型號是否真的採用壓電變壓器**，多數靜電消除器仍用傳統高壓模組。

### 2.4 隔離（專利稀疏＝白區，但也可能是「大家試過都不行」）

- 聲學隔離：Avago **US7525398 / WO2007047701A2**（FBAR 路線，2005–2009 年代）。
- 壓電隔離感測：**EP3127172B1「Galvanic isolated piezoelectric transformer based voltage sensors」**（權利人未驗證）。
- 相關但非壓電：US10715034B2「Isolated gate driver auxiliary power supply」、US12218783「Integrated circuit with galvanic isolation」（2025-02-04 核准，權利人未驗證）、US6389061B1 / US6570513B2（電容式隔離，Silicon Labs 路線的經典先前技術）。
- 學術前沿：arXiv 2511.13412 → *Communications Engineering* (2026) 微波聲學隔離閘極驅動器。

### 2.5 超音波供電（醫療內建、工業穿牆）

- 醫療：UC Berkeley 專利族（見 §1.7），Iota Biosciences → Astellas。
- 工業穿牆：**US20150049587A1「Full-duplex ultrasonic through-wall communication and power delivery system with frequency tracking」**、**US20170163354A1「System for ultrasonic communication across curved metal surfaces」**（權利人皆未驗證）。
- 學術：MDPI *Applied Sciences* 8(5), 692（穩壓 DC 輸出的穿金屬牆供電系統）；*Scientific Reports* (2022) AlN PMUT 超音波供電。

### 2.6 X 光源（TRL 最低）

- **US9287080「Method and system for a piezoelectric high voltage x-ray source」**（權利人未驗證）。
- 學術：*Scientific Reports* (2018)「Piezoelectric Accelerator」；PMC6073904「Ceramic Piezoelectric Transformer in Vacuum for Acceleration of Electrons and Production of X-Rays」；實測**最大軔致輻射能量僅約 14 keV**（電子加速至至少 14 keV）——遠低於醫療／工業 X 光所需的數十至數百 keV。

---

## 3. 關鍵數字表

| 項目 | 數值 | 來源編號 | 驗證狀態 |
|---|---|---|---|
| CeraPlas HF 尺寸 | 47.3 × 20 × 20 mm | [5][6] | 已驗證 |
| CeraPlas 驅動條件 | 12–24 Vpp @ 50 kHz 正弦 | [3][7] | 已驗證 |
| CeraPlas 評估套件輸入功率 | 預設 ~4.5 W；軟體可選 ~2–7 W；24 V 單電源 | [8] | 已驗證 |
| piezobrush PZ3 最大消耗功率 | 18 W | [9] | 已驗證 |
| 電漿／元件溫度 | < 50 °C | [3][9] | 已驗證 |
| CeraPlas HF 上市 | 2018-11-13 | [6] | 已驗證 |
| piezobrush PZ2 上市（首個 CeraPlas 產品） | 2014 | [2] | 已驗證 |
| CeraPlas 單價 / 壽命 / MTBF | **查無** | — | 查無 |
| SAW 隔離閘驅：隔離電壓 | 2.75 kV | [16] | 已驗證（單一論文） |
| SAW 隔離閘驅：隔離電容 | **0.032 pF** @ 1.25 mm | [16] | 已驗證（單一論文） |
| SAW 隔離閘驅：輸出 | 13.4 V 開路 / 44.4 mA 短路；GaN 導通 108.8 ns | [16] | 已驗證（單一論文） |
| 磁性方案最佳繞組間電容（對照組） | 低至 7 pF（Würth WE-AGDT）；建議 < 10 pF | [17] | 已驗證 |
| SiC dv/dt 造成的位移電流 | 100 kV/µs × 10 pF ≈ 1 A 峰值 | [17] | 已驗證 |
| 體聲波 PT 固有頻寬 | 僅數十 kHz（工作頻率 < 數十 MHz、高 Q） | [16] | 已驗證（負面） |
| 穿金屬牆：資料率＋功率 | 15 Mbps / 30 W（平板牆） | [13] | 未驗證（僅摘要） |
| 穿 6.3 cm 鋼塊 | 12.4 Mbps ＋ 32.5 W AC | [13] | 未驗證（僅摘要） |
| DEAP 致動器 PT 驅動範圍 | 250 V → 2.5 kV（burst mode 控制） | [11] | 未驗證（僅摘要） |
| 壓電 X 光源最大光子能量 | ~14 keV | [15] | 未驗證（僅摘要） |
| CCFL 背光逆變器 PT 市佔（2000s 初） | 25–30% | [10] | 已驗證 |
| Astellas 收購 Iota Biosciences | 1.275 億 USD 頭期 ＋ 最高 1.765 億里程碑（合計 ~3.04 億），另 5 年 1.25 億投資 | [12] | 已驗證 |
| Iota FDA IDE（膀胱刺激） | 2024 年核准早期可行性試驗 | [12] | 已驗證 |

---

## 4. 「新能力型」應用機會

### 4.1 冷電漿源合一元件（CeraPlas 類）——**已被 TDK 佔住，但白區在「陣列化／嵌入式」**

- **新能力是什麼**：把「升壓」與「電漿放電」壓縮進同一塊陶瓷，**系統中不存在任何高壓節點**。輸入 24 V 以下、50 kHz，輸出端直接在大氣中點燃 < 50 °C 的冷電漿。
- **為什麼以前做不到**：傳統冷電漿需要 kV 級高壓電源 + 高壓線 + 高壓接頭 + 安規爬電距離 + 屏蔽，體積與安規成本使其無法進入手持、消費、車內、機械手末端。CeraPlas 讓「高壓從未離開元件」。
- **是否真非替代性**：**是（新能力）**。它不是把電漿設備做小，它是讓「電漿當成一顆表面黏著元件用」這件事第一次成立。
- **誰在做**：TDK Electronics AG（前 EPCOS AG）＋ relyon plasma。專利族：US10856399B2、US10638590B2、US11903321、US10772182、US10966309、US10531552、US10827599、WO2021122995A1、US20200305266、EP2256835A3。
- **TRL**：**9（已量產銷售）**。
- **市場訊號**：Mouser 等通路可購買；PZ2 自 2014 年起銷售 12 年。
- **技術難點／白區**：(a) 單元件僅 2–7 W，**大面積處理必須陣列化**——MDPI 的 multi-device PDD 論文顯示這仍是研究題目，多元件同步、頻率牽引、互相干擾是白區；(b) 諧振點會隨負載、溫度、老化漂移，**閉迴路頻率追蹤**是專利密集區（US11903321 的場強探針法、US10772182 的頻率控制法都在圈這塊）；(c) 壽命／PZT 去極化資料 TDK 未公開，是盡職調查的最大黑洞。

### 4.2 聲學（壓電）隔離：功率＋訊號同體跨障壁 —— **最大的物理白區**

- **新能力是什麼**：用機械波而非電磁場穿越絕緣障壁，讓隔離電容降到 **0.03 pF 級**（磁性最佳 7 pF、電容式更高）。在 SiC/GaN 的 100 kV/µs dv/dt 下，共模位移電流可降兩個數量級，**CMTI 不再是設計瓶頸**；同時 EMI 幾乎為零（沒有磁通外洩）。
- **為什麼以前做不到**：需要在同一片壓電/鐵電薄膜堆疊上同時做出 GHz 級高 Q 諧振器、足夠的能量轉換效率、以及 kV 級障壁——這是近十年薄膜壓電（AlN/ScAlN、LiNbO₃ 薄膜轉移）成熟後才具備的製程條件。
- **是否真非替代性**：**半**。單就「隔離」而言它是替代品（磁耦／電容耦已有成熟產品），但就「**在 100 kV/µs 以上 dv/dt 環境仍能同時送電＋送訊號且不需要屏蔽**」而言是新能力。應以「解鎖更高 dv/dt 的功率密度」而非「更小的隔離器」定位。
- **誰在做**：歷史上 Avago/Broadcom（US7525398, FBAR）；學界最新為 2026 *Communications Engineering* 的 LiNbO₃ SAW 隔離閘極驅動器。**未查證 ADI/TI/Silicon Labs 是否有布局——這是必須補的功課。**
- **TRL**：**3–4**（實驗室驗證，已在 buck converter 中實測驅動 GaN HEMT）。
- **市場訊號**：弱。20 年前 Avago 的專利沒有變成主流產品，這件事本身要當警訊看。
- **技術難點**：**頻寬**。體聲波 PT 的高 Q 帶來高效率卻只有數十 kHz 頻寬，無法傳次微秒邊沿；跳到 GHz SAW 可解頻寬但**功率轉換效率與可傳輸功率是否夠驅動閘極（需 mA 級持續電流）仍未證明**。另外 kV 級耐壓與 mm 級聲程之間的取捨、封裝內部爬電、以及溫度對 SAW 速度的漂移都未解。

### 4.3 穿金屬牆／密封艙壁的「功率＋資料」單一通道

- **新能力是什麼**：在**完全密封、無穿孔**的金屬壁上同時送 10 W 級功率與 Mbps 級資料。文獻報導 6.3 cm 鋼塊上 12.4 Mbps ＋ 32.5 W。
- **為什麼以前做不到**：Faraday 屏蔽讓所有 EM 無線方案在金屬上歸零；有線方案必須鑽孔，鑽孔就破壞壓力容器／防爆／真空／無菌完整性。
- **是否真非替代性**：**是**。這裡沒有替代方案，只有「鑽孔」或「不做」。
- **誰在做**：US20150049587A1、US20170163354A1（權利人未驗證）；學界 MDPI *Appl. Sci.* 8(5) 692。**台灣的機會點：半導體真空腔體、壓力容器、船舶、核設施、油氣管線的感測器供電。**
- **TRL**：**4–6**（多篇實驗室系統，未見標準商品型號）。
- **市場訊號**：弱，尚未查到量產型號。**這是白區也是紅旗——20 年沒商品化通常有原因。**
- **技術難點**：金屬壁厚度／材質一變，聲學匹配與諧振點就變，**每個安裝點都要重新調校**；壁面耦合層（couplant）長期老化；駐波與多重反射造成的頻率追蹤困難（US20150049587A1 的 frequency tracking 正是在解這個）。

### 4.4 超音波遠端供電的毫米級植入物（neural dust）

- **新能力是什麼**：mm³ 級、**完全無電池、無導線**的植入式感測／刺激節點，靠體外超音波供電並以**背向散射（backscatter）**回傳訊號——同一顆壓電體同時當能量接收器（被動）與調變器／刺激器（主動）。
- **為什麼以前做不到**：RF 在組織中衰減與 SAR 限制使 mm 級 RF 天線無法取得足夠功率；超音波在軟組織中波長短、衰減小，才允許 mm 級孔徑。
- **是否真非替代性**：**是**。這不是「更小的起搏器」，而是「可以放在神經／膀胱壁／深部器官上、以注射方式植入的節點」。
- **誰在做**：UC Berkeley（US10118054、US10300309B2、US10300310B2、US10682530B2、US20190150882A1；WO2018009905A2/A3、WO2018009910A1）→ Iota Biosciences → **Astellas（2020，約 3.04 億美元）**。
- **TRL**：**6–7**（2024 FDA IDE，人體早期可行性試驗）。
- **市場訊號**：**強**——大藥廠併購＋額外 1.25 億美元五年投資＋法規進展。
- **技術難點**：體外換能器的對位與長期追蹤；骨骼／氣體界面阻擋；能量預算（背向散射訊噪比）；生物相容封裝；**最關鍵的是這條路已被 Astellas/UC Berkeley 的專利族圈住，台灣廠商的切入點應在「壓電材料／微型換能器供應鏈」而非系統。**

### 4.5 壓電變壓器驅動介電彈性體致動器（DEA/DEAP）

- **新能力是什麼**：DEA 需要 kV 級、**容性負載**驅動；PT 的高輸出阻抗與容性輸出本來就與 DEA 天生匹配，可做出無磁性元件、輕量的軟性機器人驅動級。文獻示範 250 V → 2.5 kV、burst mode 控制。
- **是否真非替代性**：**半**。飛返式高壓電源已可做到 12 V → 7 kV，PT 主要贏在體積、重量、EMI 與無磁。對「肌肉密度」導向的軟體機器人，重量本身就是規格，所以「半」偏「是」。
- **誰在做**：學界為主（DEAP 高壓電源論文群）。相關專利 EP2452426B1 / WO2011005123A1 / US10250166「Transformer and priming circuit therefor」——但**注意：這幾件是「用介電彈性體做變壓器」，不是「用 PT 驅動 DEA」，不可混為一談**。
- **TRL**：**3–4**。
- **技術難點**：DEA 是純容性且電容隨形變改變 → PT 的諧振點被負載拉著跑，需要極強健的追蹤；能量回收（DEA 放電時的能量）幾乎沒人解。

### 4.6 壓電高壓脈衝產生器（電穿孔／醫療）

- 訊號：*Annals of Biomedical Engineering* (2023)「Piezoelectric Transformer-Based High-Voltage Pulse Generator Using Wide-Bandgap Semiconductors for Medical Electroporation Therapy」。
- **是否真非替代性**：**半／否**。電穿孔設備現有高壓脈衝源已成熟，PT 主要優勢是體積與絕緣簡化（可做手持／內視鏡端）。若定位在「內視鏡末端的原位電穿孔」則轉為「是」。
- **TRL**：3。

### 4.7 壓電 X 光源 —— **不建議**

- 最大光子能量僅 ~14 keV，遠低於實用需求；真空封裝與陶瓷放氣是根本矛盾（要在真空中加速電子，卻用會放氣的多層陶瓷）。**判定：科學好奇，非商業機會。**

---

## 5. 反面證據、失敗案例與物理上限

1. **CCFL 背光是壓電變壓器唯一一次真正的大量產成功，而它死了。** 2000 年代初 PT 佔 CCFL 背光電路的 25–30%（來源 [10]），Toshiba、NEC、Hitachi、Panasonic、Apple 都用過；LED 背光普及後這個市場歸零。**教訓：PT 的商業成功高度依附於「客戶端剛好需要 kV 級高壓」這個外生條件；一旦下游改用低壓技術，PT 沒有第二個 fallback 市場。** 這正好呼應客戶排除「取代電感」的判斷——PT 沒有通用性護城河。
2. **Avago 早在 2005–2009 年就用 FBAR 做出跨隔離障壁的聲學通訊（US7525398），20 年後隔離器市場仍由磁耦（ADI iCoupler、Infineon coreless transformer）與電容耦（Silicon Labs）主導。** 這代表「物理上更好」不等於「商業上會贏」——隔離器是高度成本敏感、認證（UL/VDE/IEC 60747-17）門檻極高的市場，新原理要重跑全部安規認證。
3. **體聲波壓電變壓器的高 Q 是雙面刃。** 2026 *Communications Engineering* 論文明言：現有 PT 工作頻率 < 數十 MHz、高機械 Q，**固有頻寬僅數十 kHz**，「不足以支援寬能隙功率電子所需的次微秒切換」。高 Q 給你效率與增益，同時剝奪你頻寬與抗擾動能力——這是壓電諧振器的**根本取捨**，不是工程可以繞過的。
4. **諧振頻率漂移是所有應用的共同罩門。** TDK 自己的專利佈局就是證據：US11903321（場強探針回授找最大場強）、US10772182（頻率控制）、WO2021122995A1（操作方法）——**如果諧振點穩定，就不需要三個專利族來追它。** 負載變動、溫升、老化、機械夾持都會拉動諧振點，且高 Q 意味著偏離幾百 Hz 輸出就崩掉。
5. **功率密度天花板。** CeraPlas HF 輸入 2–7 W，手持機整機 18 W。這個量級決定它只能做「表面處理、消毒、離子化、感測」，做不了「製程級電漿」「工業殺菌線」。想放大就得陣列化，而陣列化又撞上第 4 點的同步問題。
6. **PZT 含鉛與 RoHS 豁免風險。** CeraPlas 明確為 PZT。歐盟 RoHS 對壓電陶瓷的鉛豁免長期存在但週期性受檢討；**這是投入前必須量化的法規風險（本次未查證豁免現況，屬缺口）。**
7. **關鍵商業數字全部不透明。** CeraPlas 的單價、壽命（工作小時）、失效模式、良率，官方與媒體均未揭露（我查了一次，查無）。**在無法取得單價的情況下，任何「壓電元件太貴」的成本論證都無法被驗證或反駁**——建議客戶直接向 TDK/Mouser 詢價作為第一步盡職調查。
8. **超音波穿牆與 X 光這兩條路都已有 10–20 年學術文獻但無標準商品**，這種「長期活躍的論文、零商品」模式通常代表存在未被論文誠實揭露的工程障礙（安裝校準、壽命、認證）。

---

## 6. 未解問題（給下一輪研究）

1. **EBR Systems WiSE-CRT 完全未查。** 這可能是超音波供電植入物中**最成熟的商業案例**（超音波供電的無導線左心室起搏電極）。必須補：專利號、權利人、FDA 核准狀態、營收。**本輪未查，勿在後續文件中假設任何內容。**
2. **ADI / TI / Silicon Labs / Infineon 是否持有壓電或聲學隔離專利？** 若三大隔離器廠都沒有布局，代表白區真實存在；若有防禦性專利卻無產品，代表他們評估過並放棄——兩種結論的策略含意完全相反。
3. **CeraPlas 的單價、壽命、失效模式。** 建議直接詢價 Mouser / key-components，並索取 TDK 的 reliability report。
4. **PZT 的 RoHS 鉛豁免（Annex III / IV）現況與落日時程**，以及無鉛壓電（KNN、BNT）是否已能達到 CeraPlas 所需的硬質高 Q 特性。
5. **專利密度的量化**：需要能執行 Espacenet/Lens.org CPC 檢索的環境，統計 H02N 2/18、H01L 41/107、H05H 1/24 等分類下 TDK/EPCOS 的實際件數與各年申請曲線，才能判斷「白區」是真白還是我沒查到。
6. **未驗證權利人清單**（下輪必須逐一確認）：US10531552、US10827599、US10966309、US10772182、US20200305266、US9287080、EP3127172B1、EP2256835A3、US20150049587A1、US20170163354A1、US12218783、US8040018B2。

---

## 7. 來源清單

1. TDK Electronics — Piezo transformers and plasma generators: TDK cooperates with relyon plasma — https://www.tdk-electronics.tdk.com/en/373388/company/press-center/press-releases/press-releases/piezo-transformers-and-plasma-generators-tdk-cooperates-with-relyon-plasma-to-develop-and-manufacture-cutting-edge-plasma-solutions/1416224 — TDK 與 relyon plasma 合作開發並製造壓電變壓器與電漿產生器的官方新聞稿。
2. TDK Electronics — Cold plasma from a single component — https://www.tdk-electronics.tdk.com/en/373562/tech-library/articles/applications-cases/applications-cases/cold-plasma-from-a-single-component/1109546 — CeraPlas 的技術原理、多層 Rosen 型結構、銅內電極、piezobrush PZ2（2014）為首個產品。
3. TDK — Cold Plasma's Potential: Revolutionizing Forefront Medical Care — https://www.tdk.com/en/featured_stories/entry_041.html — CeraPlas 醫療應用與 12–24 Vpp / 50 kHz 驅動條件、< 50 °C。
4. Google Patents — US10856399B2 Device for generating an atmospheric-pressure plasma — https://patents.google.com/patent/US10856399 — 發明人 Kudela/Rinner/Puff，權利人 TDK Electronics AG（原 EPCOS AG），2020-12-01。
5. Mouser — CeraPlas HF Piezoelectric Plasma Generator (EPCOS/TDK) — https://www.mouser.in/new/epcos/epcos-ceraplas-hf/ — 通路商品頁，證明實際可購買。
6. GlobeNewswire — TDK Introduces CeraPlas HF Compact Cold Plasma Generator Element (2018-11-13) — https://www.globenewswire.com/news-release/2018/11/13/1650541/0/en/TDK-Introduces-CeraPlas-HF-Compact-Cold-Plasma-Generator-Element.html — 上市日期與 47.3 × 20 × 20 mm 尺寸。
7. TDK Electronics — Compact CeraPlas HF element for cold plasma — https://www.tdk-electronics.tdk.com/en/374108/tech-library/articles/products-technologies/products-technologies/compact-ceraplas-hf-element-for-cold-plasma/2435692 — 元件層級技術說明。
8. key-components — EPCOS/TDK CeraPlas HF Evaluation Kit — https://www.key-components.com/news/epcos-tdk-ceraplas-hf-evaluation-kit.html — 評估套件 ~4.5 W 預設、2–7 W 可選、24 V 單電源。
9. relyon plasma — PiezoBrush PZ3 — https://www.relyon-plasma.com/piezobrush-pz3/?lang=en — 手持機最大 18 W、PDD 技術、< 50 °C；relyon 為 TDK Electronics 子公司。
10. MDPI Actuators 5(2), 12 — Piezoelectric Transformers: An Historical Review — https://www.mdpi.com/2076-0825/5/2/12 — Rosen US2,830,274（1954 申請）、CCFL 背光 25–30% 市佔、NEC/Matsushita/Toshiba/Hitachi/Panasonic/Apple 採用史。
11. ResearchGate — Integrated high voltage power supply utilizing burst mode control ... DEAP actuators — https://www.researchgate.net/publication/260230853_Integrated_high_voltage_power_supply_utilizing_burst_mode_control_and_its_performance_impact_on_dielectric_electro_active_polymer_actuators — PT 驅動 DEAP、250 V–2.5 kV。
12. Fierce Biotech — Astellas opts to acquire Iota Biosciences in $304M deal — https://www.fiercebiotech.com/medtech/after-r-d-tryout-astellas-opts-to-acquire-bioelectronics-maker-iota-biosciences-304m-deal — 收購金額結構；另見 Astellas 官方新聞 https://newsroom.astellas.com/2020-10-15-Astellas-to-Acquire-iota-Biosciences 與 Clinical Trials Arena（2024 FDA IDE 膀胱刺激）https://www.clinicaltrialsarena.com/news/astellas-iota-receives-fda-go-ahead-for-bladder-implant-trial/
13. MDPI Applied Sciences 8(5), 692 — An Ultrasonic Through-Metal-Wall Power Transfer System with Regulated DC Output — https://www.mdpi.com/2076-3417/8/5/692 — 穿金屬牆供電；15 Mbps/30 W 與 6.3 cm 鋼塊 12.4 Mbps + 32.5 W 的引述出自此文獻脈絡（未獨立驗證原始出處）。
14. Google Patents — US20150049587A1 Full-duplex ultrasonic through-wall communication and power delivery system with frequency tracking — https://patents.google.com/patent/US20150049587 — 穿牆全雙工功率＋通訊、頻率追蹤（權利人未驗證）。另見 US20170163354A1（曲面金屬）https://patents.google.com/patent/US20170163354A1/en
15. PMC — Ceramic Piezoelectric Transformer in Vacuum for Acceleration of Electrons and Production of X-Rays — https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6073904/ — 真空中壓電加速電子產生 X 光，~14 keV 上限；另見 Scientific Reports「Piezoelectric Accelerator」 https://www.nature.com/articles/s41598-018-34831-8
16. Nature Communications Engineering — Microwave-acoustic-based isolated gate driver for power electronics — https://www.nature.com/articles/s44172-026-00681-w （預印本 https://arxiv.org/pdf/2511.13412）— LiNbO₃ SAW，2.75 kV / 0.032 pF / 1.25 mm、13.4 V、44.4 mA、GaN 108.8 ns；並明確指出體聲波 PT 頻寬僅數十 kHz 之限制。
17. Würth Elektronik — WE-AGDT Auxiliary Gate Drive Transformer — https://www.we-online.com/en/components/products/WE-AGDT — 磁性方案繞組間電容低至 7 pF、建議 < 10 pF；另見應用手冊 https://www.we-online.com/files/pdf1/rd001d-v1.pdf （SiC 100 kV/µs × 10 pF ≈ 1 A）。
18. USPTO — US7525398 Acoustically communicating data signals across an electrical isolation barrier — https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/7525398 — Avago Technologies General IP (Singapore)，發明人 John D. Larson III 等；同族 WO2007047701A2 https://patents.google.com/patent/WO2007047701A2/en
19. Google Patents — EP3127172B1 Galvanic isolated piezoelectric transformer based voltage sensors — https://patents.google.com/patent/EP3127172B1/en — 壓電變壓器式隔離電壓感測（權利人未驗證）。
20. Google Patents — US7821762B2 Piezoelectric transformer type ionizer and neutralization method — https://patents.google.com/patent/US7821762B2/ — SMC Corporation 靜電消除器；同族 US20090135538A1、CN101442871B https://patents.google.com/patent/CN101442871B/en 、JP2009129673A https://patents.google.com/patent/JP2009129673A/en
21. Google Patents — WO2021122995A1 Method of operating a piezoelectric plasma generator — https://patents.google.com/patent/WO2021122995A1/en — 壓電電漿產生器操作方法（諧振追蹤相關）。
22. USPTO — US11903321 Device for producing a non-thermal atmospheric pressure plasma and method for operating a piezoelectric transformer — https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/11903321 — 以場強探針回授調整激勵頻率使場強最大化。
23. USPTO — US10772182 Device for producing a non-thermal atmospheric-pressure plasma and method for the frequency control of a piezoelectric transformer — https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/10772182 — 頻率控制方法。
24. USPTO — US10966309 Device for generating a non-thermal atmospheric pressure plasma — https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/10966309 — 同族（權利人未驗證）。
25. USPTO — US10531552 Device for generating an atmospheric-pressure plasma — https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/10531552 — 同族（權利人未驗證）。
26. USPTO — US10827599 Piezoelectric transformer — https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/10827599 — 壓電變壓器本體（權利人未驗證）。
27. Justia — US20200305266 Device and component for generating a high voltage or high field strength — https://patents.justia.com/patent/20200305266 — 介電殼體內對稱場分佈設計，2020-09-24 公開（權利人未驗證）。
28. Google Patents — EP2256835A3 High gain miniature power supply for plasma generation — https://patents.google.com/patent/EP2256835A3/en — PT 驅動非線性電漿負載的高增益脈衝電源（權利人未驗證）。
29. Google Patents — US10118054 / US10300309B2 / US10300310B2 / US10682530B2 Implants using ultrasonic backscatter — https://patents.google.com/patent/US10682530B2/en （另見 https://patents.google.com/patent/US10300310B2/en 、 https://patents.google.com/patent/WO2018009905A2/en ）— Regents of the University of California，發明人 Maharbiz & Carmena，neural dust 專利族。
30. Wiley Plasma Processes and Polymers — Korzec et al., Atmospheric pressure plasma jet powered by piezoelectric direct discharge (2020) — https://onlinelibrary.wiley.com/doi/full/10.1002/ppap.202000053 — relyon 的 PDD 技術學術描述；另見 MDPI Plasma 4(2), 19 多元件大面積 PDD https://www.mdpi.com/2571-6182/4/2/19
31. IOPscience Plasma Sources Sci. Technol. 18, 045011 — Development of dielectric barrier discharge-type ozone generator constructed with piezoelectric transformers — https://iopscience.iop.org/article/10.1088/0963-0252/18/4/045011 — 壓電變壓器 DBD 臭氧產生器，介電電極材料對臭氧產率的影響。
32. Springer Annals of Biomedical Engineering — Piezoelectric Transformer-Based High-Voltage Pulse Generator Using Wide-Bandgap Semiconductors for Medical Electroporation Therapy (2023) — https://link.springer.com/article/10.1007/s10439-023-03319-6 — PT + WBG 元件做電穿孔治療脈衝源。
33. Google Patents — US8040018B2 Piezoelectric transformer type high-voltage power apparatus and image forming apparatus — https://patents.google.com/patent/US8040018B2/en — 影像形成裝置用 PT 高壓電源含輸出電壓偵測回授（權利人未驗證）。
34. USPTO — US9287080 Method and system for a piezoelectric high voltage x-ray source — https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/9287080 — 壓電高壓 X 光源（權利人未驗證）。
35. Google Patents — EP2452426B1 / WO2011005123A1 Transformer and priming circuit therefor — https://patents.google.com/patent/EP2452426B1/en — **以介電彈性體換能器構成變壓器**（非 PT 驅動 DEA，勿混淆）；美國同族 US10250166 https://patents.justia.com/patent/10250166
