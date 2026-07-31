# 應用A3：昆蟲級機器人、微型衛星電推進、微型化平台的自帶高壓電源

> **一句話結論**：在「毫克～克級」尺度上磁性升壓方案不是比較差、而是不存在，所以壓電路線的非替代性最強；但本輪新增的證據**同時削弱了**原本最被寄望的「諧振能量回收」賣點——**雙向返馳（0↔2.5 kV，含能量回收）與「2 顆二極體＋1 顆電阻回收約一半電荷」的被動回收都已存在**，磁性/開關陣營早就在做能量回收。剩下唯一明確越線的機會仍是**「壓電體同時是高壓源＋放電電極／發射極」的功能合併**（2025 *Micromachines* LN 壓電變壓器離子放電推進器是唯一已發表實證）；微型 X 光源（實測 ~14 keV 上限）與單純的偵測器偏壓應判為物理不合格或純替代，建議剔除。

---

## 0. 研究方法與限制（誠實揭露，請先讀完再讀結論）

**本輪（第 2 次嘗試）的 WebSearch 成功次數同樣是 0 次。**

1. 任務書載明「WebSearch 額度已放寬到 3000，請大量使用 30–45 次」。**實際情況是：本 session 的 WebSearch 在 harness 層被硬性鎖在 200/200，額度放寬並未生效。** 我實際發出 3 次查詢（`RoboBee untethered flight solar cells high voltage Jafferis Nature 2019`、`RoboBee X-Wing mass milligrams solar cells series stacked voltage boost converter`、`Accion Systems TILE electrospray thruster status`），全部回傳 `this session has used its web search budget (200 of 200 WebSearch calls)`，**沒有取得任何一筆搜尋結果**。我也檢查了環境變數（`CLAUDE_CODE_MAX_WEB_SEARCHES_PER_SESSION` 未設定），無法自行提高。
2. **WebFetch 與 curl 依任務書載明全面 403，未浪費回合嘗試。**
3. **因此我改變策略**：既然無法做新的外部檢索，我改為**系統性地重新開採本 repo 內 24 份姊妹檔案**（其中 05/13/14/19/21/23/24 的寫入時間晚於本檔第 1 版，含有第 1 版未取得的資料），把其中**已附完整 URL 且與 A3 直接相關**的事實抽出來。**這一輪相對第 1 版新增了 7 項帶 URL 的實質事實，並因此推翻了第 1 版的 1 項核心判斷**（見 §5.2）。這是本輪唯一的真實增量。
4. **證據分層（全文標記，請依標記調整信心度）**：
   - **【V】已驗證**＝姊妹檔中已附完整 URL 並經該檔 agent 標為已驗證者。本檔對這些連結持**二手信心**（相信姊妹 agent 的查證），非一手驗證。
   - **【M】模型記憶・未驗證**＝來自訓練知識，本輪無任何 URL 佐證。凡屬此類我只寫有把握的定性內容與量級，**不填精確數字**。
   - **【C】自行推算**＝由【V】/【M】以物理公式推導，輸入假設會寫出供檢驗。
5. **本輪明確查無（任務書點名要查、兩輪都拿不到的）——這份清單就是下一輪的檢核表**：
   - Harvard RoboBee 的驅動電壓、機上驅動電子質量（mg）與功率（mW）、整機質量、飛行時間；RoboBee X-Wing 太陽能規格；UW RoboFly、Berkeley 微型機器人規格。**兩輪皆完全查無。**
   - 微型爬行／游動機器人與 MEMS 微機器人的電源方案。
   - Accion Systems 的現況（含是否停業）、TILE 系列規格。
   - Enpulsion IFM Nano Thruster 的電壓／功率／質量；Morpheus Space、Busek、ThrustMe 規格。
   - **所有電推進 PPU 的質量（kg）、效率、輸出電壓**；FEEP 的 5–10 kV 低電流特性的一手佐證。
   - 太空級 DC-DC 模組（VPT、Crane、TT Electronics）的質量與價格級距；太空級交流磁場發射規格。
   - Moxtek、Amptek、Newton Scientific 的微型 X 光管型號、kV、功率、尺寸與其高壓電源方案。
   - 手持式 XRF（Bruker、Olympus/Evident、Hitachi）的高壓需求與電源方案。
   - PMT／SiPM／蓋革管偏壓電源的**具體型號、體積、功耗、價格**；可攜輻射偵測儀／劑量計市場規模。
   - 908 Devices、BaySpec 的高壓需求（**但本輪由姊妹檔取得了另一組可攜質譜的 ±25 kV / <4 lb 數字，見 §2.5，這是本輪唯一有 URL 的質譜資料**）。
6. **本檔的價值定位**：在無法新檢索的前提下，重心放在**「用已驗證的物理數字做尺度分析與否決性推導」**——回答「這個尺度下什麼在物理上可能、什麼不可能」。**所有需要外部事實的部分一律標為查無，不填空、不猜數字。本文件中沒有任何一個 URL、型號、公司名、期刊卷期或數字是我自行產生的。**

---

## 1. 結論摘要

1. **尺度論證成立且可量化**：壓電實務功率密度上限【V・S9】為 **33 W/cm³**（理論 330 W/cm³，受應力邊界限制）；另一組獨立來源給出**單層最佳化 40 W/cm³、疊層 >13 W/cm³ 且效率 >94%**【V・S18】。取疊層的保守值 13 W/cm³，一顆 1 mm³（PZT 密度 ~7.8 g/cm³ ⇒ **約 7.8 mg**）的壓電體可處理約 **13 mW**；取 33 W/cm³ 則約 **33 mW**。【C】這個量級**恰好覆蓋昆蟲級撲翼致動器的反應功率需求**——功率密度不是瓶頸。
2. **瓶頸不在功率，在頻率與能量回收的「已被佔領」**：以雙晶片致動器 C≈2 nF、V≈250 V、撲翼 120 Hz 推算，單顆反應功率 ½CV²·f ≈ **7.5 mW**，雙顆約 **15 mW**【C，輸入假設未驗證】。所以 8–25 mg 的壓電體在功率上夠用；真正的問題是 §5.2 與 §5.3。
3. **【本輪最重要的新發現・推翻第 1 版判斷】「諧振能量回收是壓電獨有的新能力」這個宣稱站不住**。本輪查到兩篇帶 URL 的既有工作：(a)**雙向返馳轉換器，0 V ↔ 2.5 kV 充放電並回收能量**【V・S19】；(b)**被動電荷回收驅動電路，2 顆二極體＋1 顆電阻即可回收約一半電荷**【V・S20】。磁性／開關陣營早就在做高壓容性負載的能量回收，而且 (b) 的 BOM 是 3 顆零件。**第 1 版把「能量回收」列為機會 B 唯一的真新能力層，這個判斷必須下修為「半」甚至「否」**——壓電要贏必須證明往返效率顯著高於這兩者，而該數字兩輪皆查無。
4. **「機上高壓源質量」現在有真實對照數字了**：非繫繩軟體機器人的既有機上高壓方案，**含電池約 100 g / 5 W / 0–10 kV（0–5 V 輸入）**【V・S21】；口袋型 10 通道高壓電源 **250 g、8.4×13.3×2 cm（≈223 cm³）**【V・S22】。這兩個數字定義了「非繫繩高壓」目前的實際重量級距——**都是百克級，而昆蟲級機器人的總預算是百毫克級，差 3 個數量級**。這既是壓電的機會（沒人做到 mg 級），也是警訊（沒人做到不代表做得到）。
5. **最強的反面證據仍是現貨**：XP Power / EMCO Q 系列 **5 kV @ 0.125 in³（≈2 cm³）**、10 kV @ 0.614 in³、輸出 0.5 W，Q101-5 單價 **USD 420.06**【V・S3】。壓電要贏，必須進入 **<2 cm³ 或 <100 mg** 的區間；體積預算一旦大於 2 cm³，「更小」這個賣點就不存在。
6. **頻率尺度落差是本領域最致命的物理障礙**：PT 機械共振數十～數百 kHz、Qm≈1000 導致**固有頻寬僅數十 kHz**【V・S10】；而撲翼所需機械頻率是 **100–350 Hz**（昆蟲尺度 DEA 蜻蜓機器人 317 mg、4 翼、350 Hz、升重比 1.49）【V・S2】——差 2–3 個數量級。「單一諧振腔同時做功率轉換與致動」在物理上站不住。
7. **微型 X 光源應直接剔除**：壓電加速電子產生 X 光的實測**最大軔致輻射能量僅約 14 keV**【V・S4】，遠低於手持 XRF 與工業／醫療所需的數十至數百 keV。這是加速電位的物理上限，不是工程問題。（**注意：手持 XRF 的實際 kV 需求本輪查無一手來源，此判斷的分母端仍是【M】。**）
8. **真空環境把壓電的既有弱點放大而非緩解**：「機械式儲能本質上阻止了傳統散熱——諧振體必須節點支撐才不破壞 Q，而節點支撐正是最差的熱通路」【V・S5】。太空（無對流）與昆蟲機器人（無散熱面積）都把這個矛盾推到極致；且節點支撐與發射段隨機振動的結構需求直接對立，而壓電陶瓷約 **10 MPa 即機械去極化**【V・S5】。**這是我認為本應用域最被低估的風險，且公開文獻查無任何人處理。**

---

## 2. 現況：技術 / 產品 / 玩家

### 2.1 昆蟲級機器人（可驗證程度：低）

- **唯一已驗證的整機參照點**：昆蟲尺度 DEA 蜻蜓機器人，**317 mg、4 翼、350 Hz、升重比 1.49**（MDPI *Micromachines* 13(7):1136）【V・S2】。這是介電彈性體路線，不是壓電雙晶片路線。
- **本輪新增的關鍵參照**：同一份姊妹檔引用了 arXiv 2502.06166「Portable, High-Frequency, and High-Voltage Control Circuits for Untethered Miniature Robots Driven by DEA」【V・S2】——**這是與 A3 主題最直接對口的一篇文獻（非繫繩微型機器人的可攜高頻高壓控制電路），但本輪無法開啟取得其質量／效率數字**。**列為下一輪第一優先。**
- **非繫繩高壓的實際質量級距（本輪新增）**：HASEL 工具包（*Advanced Science* 2019 / PMC6662077）**含電池電源約 100 g、5 W、0–10 kV（0–5 V 輸入）、3.7 V/500 mAh LiPo**；3×22 顆致動器在 8 kV 下對 1 kg 達 40% 應變【V・S21】。口袋型 10 通道高壓電源（*Adv. Mater. Technol.* 2022）**250 g、8.4×13.3×2 cm**【V・S22】。
- **【M・未驗證】** Harvard Microrobotics Lab（R. J. Wood 團隊）的 RoboBee 使用壓電雙晶片致動器、驅動電壓數百伏等級、本體質量數十至數百 mg、長年繫繩供電；UW（S. Fuller 團隊）RoboFly 走「雷射 + 機上光伏 + 機上升壓」。**我對「RoboBee X-Wing 以串聯堆疊太陽能電池直接產生高電壓、藉此規避機上升壓器質量」有中等強度記憶——若屬實，這是對本專案極重要的反面證據（最頂尖團隊選擇繞開升壓器而非做更好的升壓器）。兩輪皆無法查證，任何人在查證前都不應引用。**
- **既有 PT 先例**：「Piezoelectric transformer-based high conversion ratio interface for driving dielectric actuator in microrobotic applications」——**PT 24 V 輸入 → 2.5 kV 輸出**，明確定位微型機器人【V・S6】。證明「PT 驅動微型機器人致動器」不是新想法。

### 2.2 立方衛星電推進（可驗證程度：極低，兩輪皆幾乎全部查無）

- **對 Accion Systems、Enpulsion、Morpheus Space、Busek、ThrustMe 的現況、規格與 PPU 質量／效率／輸出電壓，兩輪一筆都沒能查證。任務書要求的所有具體數字本文件不提供，後續統整請勿引用任何看似具體的數字，因為我沒有。**
- **【M・定性，中等把握】** 電噴霧／膠體推進與 FEEP 的共同電氣特徵是：**高電壓（kV 級）、極低電流（µA 至次 mA）、負載近似容性並帶有隨機放電**。這個負載特性在紙面上非常適合 PT（PT 正是「高輸出阻抗、擅長高升壓比低電流」的元件）。**但這是紙面推論，沒有一手來源。**
- **唯一已發表的太空側實證**：*Micromachines* 16(3):277 (2025)「An Ion Discharge-Driven Thruster Based on a Lithium Niobate Piezoelectric Transformer」，以 LN 壓電變壓器直接作為離子放電推進器的高壓源；文中論證 LN 因「低阻尼、低彈性損、低電損與更高機電耦合」比 PZT 更適合做變壓器【V・S1】。文中提及的「飛行微型機器人推重比 5.5」歸屬語意不明，**標為未驗證**。
- **太空 EMI／磁潔淨的已驗證痛點**：*Aerospace* 12(2):97 明指太空級 DC-DC 需抑制 EMI 以免干擾磁強計等敏感儀器【V・S7】；Solar Orbiter 磁強計需量測低至 **10 pT** 的擾動，一般要求太空船 DC 場在外側感測器處 **<10 nT**，甚至需引入 **EMC quiet periods（量測時關掉設備）**；JUICE 為此做 10.6 m 三段式 CFRP 伸桿、Europa Clipper 8.5 m【V・S8】。
- **但必須誠實指出**：姊妹檔 15 已查證「**查無任何一份公開文獻報告壓電變壓器／諧振器的實測剩磁矩或交流磁場**」，且物理上壓電轉換器仍有輸入輸出走線、MOSFET、去耦電容構成的電流迴路，**「沒有磁芯」遠遠不等於「磁潔淨合格」**；磁潔淨計畫的實務經驗是「每一顆螺絲都要測」【V・S8】。

### 2.3 微型 X 光源與微型中子源

- **實證上限 ~14 keV**（PMC6073904「Ceramic Piezoelectric Transformer in Vacuum for Acceleration of Electrons and Production of X-Rays」／*Scientific Reports* 2018「Piezoelectric Accelerator」）【V・S4】。專利面有 **US 9287080「Method and system for a piezoelectric high voltage x-ray source」**（權利人未驗證）【V・S4】。
- 姊妹檔 07 已獨立判定「壓電 X 光源 —— **不建議**」，並指出「超音波穿牆與 X 光這兩條路都已有 10–20 年學術文獻但無標準商品，這種『長期活躍論文、零商品』模式通常代表存在未被論文誠實揭露的工程障礙」【V・S4】。
- **Moxtek、Amptek、Newton Scientific 的型號與規格，以及手持 XRF（Bruker / Evident / Hitachi）的高壓需求，兩輪皆查無。** 因此「14 keV vs 應用需求」的比較中，分母端仍是【M】。**但即使如此，14 keV 這個絕對值已低到足以支持剔除決定。**

### 2.4 偵測器高壓偏壓

- **【M・常識級】** 典型工作點：PMT 約 1–2 kV／數十至數百 µA；蓋革-穆勒管約 400–900 V／µA 級；SiPM 約 25–70 V 但要求 mV 級穩壓與溫度補償（增益對過電壓極度敏感）。**這些是量級性陳述，兩輪皆無一手來源，不應作為設計輸入。**
- **對照組現貨**：XP Power / EMCO Q 系列 5 kV @ 2 cm³ / 0.5 W、10 kV @ 0.614 in³，Q101-5 單價 USD 420.06；另有 XP Power《Next-Generation, Miniature High Voltage Power Modules》白皮書【V・S3】。
- **技術基礎（本輪新增，對 §4.4 至關重要）**：*Sensors & Actuators A*「Simultaneous quasi-static displacement and force self-sensing of piezoelectric actuators by detecting impedance」明確給出機制——**以阻抗／諧振頻率變化做壓電自感測；並聯電容負載使串聯與並聯諧振頻率同時下降，且在並聯諧振附近最敏感**【V・S23】。這是「偏壓源即感測器」的物理依據，也同時是「PT 諧振腔與外部容性致動器聯合設計」的理論入口。另有以運動電流做自感測閉迴路控制的工作【V・S16】。

### 2.5 微型質譜儀（本輪唯一有 URL 的新資料）

- 可攜式質譜的高壓需求已有帶 URL 的數字：*J. Am. Soc. Mass Spectrom.*「Portable, Battery Operated Capillary Electrophoresis with … Ionization Source for Mass Spectrometry」——**±25 kV 高壓電源、整系統 <4 lb（≈1.8 kg）、12 V 鋰電池運作約 10 h**；另 **Mini 12（2–10 kV）**【V・S24】。
- **判斷**：±25 kV 是 PT 難以單級達成的電壓（CeraPlas 最高 20 kV 已是量產極限）【V・S15】；而 2–10 kV 這一檔正好落在 PT 的甜蜜點。**但系統已經只有 1.8 kg，其中高壓電源只佔一小部分，把它從數十克降到數克對系統質量的邊際效益很小——這使得質譜在 A3 中應判為「更小的替代品」，而非新能力。** 姊妹檔 11 已把此項標記為「半」並建議降權，本檔同意。
- **908 Devices、BaySpec 的規格兩輪皆查無。**

---

## 3. 關鍵數字表

| 項目 | 數值 | 層 | 來源 |
|---|---|---|---|
| 壓電實務功率密度上限 | **33 W/cm³**（理論 330，受應力邊界） | V | S9 |
| 壓電功率密度（另一組獨立來源，**本輪新增**） | 單層最佳化 **40 W/cm³**；疊層 **>13 W/cm³ 且效率 >94%** | V | S18 |
| ⇒ 1 mm³（≈7.8 mg PZT）功率上限 | **13–33 mW** | C（由 S9/S18 推算） | — |
| 昆蟲尺度 DEA 蜻蜓機器人 | **317 mg**、4 翼、**350 Hz**、升重比 1.49 | V | S2 |
| 壓電雙晶片致動器反應功率（推算） | C=2 nF、V=250 V、f=120 Hz ⇒ **7.5 mW/顆**，雙顆 **15 mW** | C（輸入假設**未驗證**） | — |
| **非繫繩機器人機上高壓電源（含電池）**（**本輪新增**） | **≈100 g、5 W、0–10 kV（0–5 V 輸入）**、3.7 V/500 mAh LiPo | V | S21 |
| **口袋型 10 通道高壓電源**（**本輪新增**） | **250 g、8.4×13.3×2 cm（≈223 cm³）** | V | S22 |
| **高壓容性負載能量回收既有解 (a)**（**本輪新增・反證**） | **雙向返馳，0 V ↔ 2.5 kV 充放電＋能量回收** | V | S19 |
| **高壓容性負載能量回收既有解 (b)**（**本輪新增・反證**） | **2 顆二極體＋1 顆電阻回收約一半電荷** | V | S20 |
| PT 機械共振 vs 撲翼機械頻率 | 數十–數百 **kHz** vs 100–350 **Hz** ⇒ 差 **2–3 個數量級** | V | S5, S2 |
| PT 固有頻寬 | 僅**數十 kHz**（f<數十 MHz、Qm≈1000 所致） | V | S10 |
| 微型高壓現貨（對照組） | XP Power/EMCO Q：**5 kV @ 0.125 in³**、10 kV @ 0.614 in³、**0.5 W**；Q101-5 **USD 420.06** | V | S3 |
| PT 微型機器人先例 | **24 V → 2.5 kV**，驅動介電致動器 | V | S6 |
| PT 商用上限（CeraPlas） | 12–24 Vpp 輸入 → 最高 **20 kV**；47.3×20×20 mm；TRL 9 | V | S15 |
| PT 升壓比／效率（Nihon Ceratec）（**本輪新增**） | 升壓比 **>80**、效率 **>90%** | V | S18 |
| 可攜質譜高壓需求（**本輪新增**） | **±25 kV**、系統 **<4 lb**、12 V 電池 ~10 h；Mini 12 為 **2–10 kV** | V | S24 |
| 壓電 X 光源最大光子能量 | **~14 keV** | V（原標未驗證） | S4 |
| 壓電陶瓷機械去極化門檻 | **約 10 MPa** | V | S5 |
| 硬質 PZT 在 300 V/mm DC 偏壓下（**本輪新增**） | Qm **每 0.1 m/s 振動速度退化 17%**（軟質更嚴重） | V | S25 |
| PZT gamma 輻射劣化 | **400 kGy → 介電性能約 −25%** | V | S11 |
| 單晶 AlN 輻射耐受 | 快中子 1.85×10¹⁸、熱中子 5.8×10¹⁸ n/cm²、gamma **26.8 MGy**；但 k² 僅 **~6.1%** | V | S12 |
| 壓電陶瓷中子耐受（ITER） | **~10¹⁹ n/cm²**（E>0.1 MeV）；去極化可**遠端逆轉** | V | S13 |
| 太空磁潔淨要求 | 磁強計需測 **10 pT**；船體 DC 場 **<10 nT**；JUICE 伸桿 **10.6 m**、Europa Clipper **8.5 m**；需 EMC quiet periods | V | S8 |
| PT 在放電負載下 | 電漿一形成、負載電阻下降 ⇒ **增益崩塌** | V | S14 |
| PT 自感測機制（**本輪新增**） | 並聯電容負載使串聯與並聯諧振**同時下降**，**並聯諧振附近最敏感** | V | S23 |
| **兩輪皆查無** | RoboBee/RoboFly/Berkeley 規格、Accion 現況、Enpulsion/Morpheus/Busek/ThrustMe 規格、**所有 PPU kg 與效率**、Moxtek/Amptek/Newton 型號、手持 XRF kV、PMT/SiPM/GM 偏壓模組型號與價格、太空級 DC-DC 質量、908 Devices/BaySpec | — | 見 §6 |

---

## 4. 「新能力型」應用機會

### 4.1 ★★★★ 機會 A：壓電體同時是高壓源與離子發射／放電電極的次公斤級推進器

- **新能力**：把「高壓產生器」與「放電／發射電極」合併成同一塊陶瓷，讓推進單元不需要外部高壓線束、高壓連接器、灌封絕緣體。這正是 TDK CeraPlas 在冷電漿領域已 TRL 9 量產的模式（12–24 Vpp 輸入直接在元件表面產生最高 20 kV 並引燃常壓電漿）【V・S15】，搬到推進場景。
- **為什麼以前做不到**：磁性高壓變壓器的輸出**必須**經導線引到獨立電極，整條高壓迴路的雜散電容、絕緣體積、連接器與真空中的多重電擊穿風險，使次公斤級的自帶 kV 電源推進模組不可行。姊妹檔 10 已驗證此論證在冷電漿領域成立【V・S15】。
- **是否真非替代**：**是（高信心）**。「元件即電極」在磁性方案中沒有對應物——這是功能合併，不是尺寸縮小。**這是本文件中唯一明確越過「更小的替代品」界線、且已有一篇 2025 年論文實證的機會。**
- **誰在做**：*Micromachines* 16(3):277 (2025) LN PT 離子放電推進器【V・S1】；模式原始出處是 IOP *PSST* 15(2):S07「Discharge plasmas generated by piezoelectric transformers」，明確論證「PT 同時作為高壓產生器與放電電極」【V・S14】；冷電漿側在位者為 TDK/EPCOS 與 relyon plasma【V・S15】。**太空推進側查無任何在位者。**
- **TRL**：**3**（單篇論文級實證，無真空／太空環境驗證）。
- **市場訊號**：**推進市場數字兩輪皆查無。** 唯一可推論的是冷電漿市場（2024 USD 2.92B → 2034 USD 11.14B，CAGR 14.35%）【V・S15】證明「PT 直接放電」這條技術路徑本身有商業體量，但那是地面應用。
- **技術難點（按嚴重度）**：
  1. **增益崩塌**——已驗證：電漿／放電一形成、負載電阻下降、PT 增益就下降【V・S14】。離子發射本質上就是把 PT 從容性負載切換成耗散負載，**頭號風險**，需主動頻率／相位追蹤。
  2. **真空散熱**——無對流，唯一路徑是節點支撐傳導，而節點支撐是最差熱通路【V・S5】。
  3. **發射段振動 vs 節點支撐**——高 Q 需低約束、結構存活需高約束，直接對立；~10 MPa 即機械去極化【V・S5】；且硬質 PZT 在 DC 偏壓下 Qm 隨振動速度快速退化（每 0.1 m/s 退化 17%）【V・S25】。**公開文獻查無任何人正面處理。**
  4. 真空除氣（outgassing）與多重電擊穿（multipaction）——**兩輪查無任何相關研究。**

### 4.2 ★★☆（第 1 版為 ★★★，本輪下調）機會 B：毫克級飛行體的機上高壓源

- **新能力**：把數百 V 高壓源做進 <100 mg 預算內，使非繫繩昆蟲級飛行成為可能。
- **為什麼以前做不到**：繞線變壓器的匝數、磁芯體積、線徑／絕緣層的不可縮放性，使高壓變壓器無法微縮到毫克級【V・S1】。功率面已由 §3 證明可行：7.8 mg 壓電體可處理 13–33 mW，而雙致動器需求約 15 mW【C】。實務對照：目前最好的非繫繩高壓電源是 **100 g（含電池）** 與 **250 g / 223 cm³** 級距【V・S21, S22】——**距離百毫克差 3 個數量級，沒有人接近過。**
- **是否真非替代**：**半，且本輪下修。** 誠實拆解：
  - 「把高壓源做到 mg 級」＝**真新能力**（磁性方案在此不存在）。
  - 「目前主流機上高壓是開關電容／電荷幫浦＋分立電感」使本項屬**部分替代**【V・S1】；電荷幫浦本來就無磁性。
  - **【本輪關鍵修正】** 第 1 版主張「只有諧振能量回收那一層才是真正的新能力」。**本輪查到這一層也被佔領了**：雙向返馳已做到 0↔2.5 kV 充放電＋能量回收【V・S19】；被動回收只要 2 顆二極體＋1 顆電阻就能回收約一半電荷【V・S20】。**所以「能量回收」不是壓電獨有；壓電要贏必須證明往返效率顯著優於這兩者，而該數字兩輪皆查無。機會 B 的新能力宣稱因此只剩「質量」單一維度。**
- **誰在做**：PT 24 V→2.5 kV 驅動介電致動器的微型機器人介面【V・S6】；arXiv 2502.06166 的非繫繩微型機器人高壓控制電路【V・S2，內容未取得】。Harvard／UW 是否使用 PT **未驗證**。
- **TRL**：單純 PT 高壓源 **3–4**；諧振回收版 **2**。
- **市場訊號**：**弱且遠。** 昆蟲尺度飛行器目前無商業市場【V・S2】。
- **技術難點**：**頻率尺度落差（kHz vs Hz）致命**——見 §5.3。

### 4.3 ★★ 機會 C：磁潔淨／低 EMI 敏感酬載旁的高壓源（與姊妹檔 15 重疊）

- **新能力**：讓推進器 PPU 或偵測器偏壓源可放在磁強計／敏感儀器附近，不需伸桿或 EMC quiet periods。系統級意義是**移除一整根 8.5–10.6 m 的可展開機構**【V・S8】——那是質量、成本與單點失效風險的大宗。
- **是否真非替代**：**未定，且前提未驗證。** 姊妹檔 15 明確指出**查無任何一份公開文獻報告壓電轉換器的實測剩磁矩或交流磁場**，且電流迴路仍在【V・S8】。**在拿到實測磁簽章之前，這個機會的價值是零，不是低。**
- **TRL**：2–4（姊妹檔判定 2）。
- **市場訊號**：帶磁強計的科學任務每年全球僅個位數，**單量極小**、單價可極高；真正的商業意義可能是技術背書＋政府 R&D 資金而非營收【V・S8】。
- **建議**：**先花兩週做磁簽章量測——這個實驗便宜、快速，可單獨否決或確立整條路線。**

### 4.4 ★★ 機會 D：「偏壓源即感測器」的偵測器高壓級

- **新能力**：一顆 PT 一邊輸出 PMT／GM 所需高壓偏壓，一邊由**輸入側**的諧振頻率／導納偏移反推負載電流與負載電容，等於免費得到偏壓電流監測與偵測器自診斷，**而且量測電路在低壓側，不需要浮在 1–2 kV 上的隔離放大器**。
- **物理依據（本輪新增，強化此項）**：*Sensors & Actuators A* 已給出可用機制——並聯電容負載使串聯與並聯諧振頻率同時下降，**並聯諧振附近靈敏度最高**【V・S23】；另有運動電流自感測閉迴路控制的技術基礎【V・S16】。**這使機會 D 從「概念」升級為「有明確量測物理量的概念」。**
- **是否真非替代**：**半。** 高壓偏壓本身是純替代（見 §5.1），**但「同一顆元件同時是偏壓源與電流感測器」沒有磁性對應物**（變壓器沒有可讀取的機械共振）。價值全部集中在感測那一層。
- **誰在做**：**查無任何人把 PT 自感測用於偵測器偏壓。** 這是空白（也可能代表沒人需要）。
- **TRL**：**2**。
- **市場訊號**：**可攜輻射偵測儀／劑量計市場數字與玩家清單兩輪皆查無。**
- **技術難點**：溫度漂移與陶瓷老化同樣會移動諧振點，必須把「負載變化」與「元件漂移」兩個訊號源分離【V・S2】；SiPM 需 mV 級穩壓，而 PT 的負載調節能力是已驗證的弱項【V・S5】。

### 4.5 明確剔除

- **微型 X 光源／微型中子源**：實測 ~14 keV 上限【V・S4】與應用所需的數十–數百 keV 差一個數量級以上；姊妹檔 07 已判「不建議」。**剔除。**
- **PMT／SiPM／GM 單純偏壓（不含感測）**：純替代，對照組已極小且**本來就無磁性**（Cockcroft-Walton／電荷幫浦）。**剔除，僅保留 §4.4 的感測版本。**
- **微型質譜儀高壓源**：見 §2.5——系統已只有 1.8 kg，高壓源減重的邊際效益小；且 ±25 kV 超出 PT 商用上限（CeraPlas 20 kV）【V・S15, S24】。**判為替代品，降權。**
- **「用 PT 取代電推進 PPU 裡的升壓變壓器」**：客戶排除的直接替代路線在太空的變體。**列出僅供辨識，不投入。**

---

## 5. 反面證據、失敗案例與物理上限

### 5.1 對照組已經很小，而且沒有磁性可以消除

XP Power / EMCO Q 系列：5 kV / 2 cm³ / 0.5 W，10 kV / 0.614 in³【V・S3】。PT 想在「微型高壓源」這個賣點上贏，必須進入 **<2 cm³ 或 <100 mg**；一旦應用的體積預算大於 2 cm³，賣點消失。更糟的是這類模組內部是「返馳＋Cockcroft-Walton 倍壓」，**倍壓級本來就不含磁性元件**——在 µA 級偵測器偏壓上，壓電連「消除磁芯」這個差異化都拿不出來。**這是對「偵測器偏壓」子題最具否決力的單一事實。**

### 5.2 【本輪新增，最重要的反證】能量回收不是壓電的專利

第 1 版把「讓致動器電容成為 PT 諧振腔的一部分、使 ½CV² 在機械共振與電場間來回震盪而非被開關丟棄」列為機會 B 唯一的真新能力。**本輪查到兩篇既有工作直接侵蝕這個宣稱**：

- **雙向返馳轉換器，多組串聯輸出，0 V ↔ 2.5 kV 高壓容性充放電與能量回收**【V・S19】。
- **被動電荷回收驅動電路：2 顆二極體＋1 顆電阻可回收約一半電荷**【V・S20】。

第二篇尤其致命——**3 顆分立零件、幾乎零成本、幾乎零質量**，就拿走了 50% 的回收效益。壓電諧振回收要成立，必須證明往返效率顯著高於 50%＋顯著低於這 3 顆零件的質量，而**兩輪皆查無任何 PT 往返效率數字**。**在拿到這個數字前，機會 B 的核心宣稱不成立。**

### 5.3 頻率尺度落差：撲翼機器人的物理牆

PT 機械共振在數十～數百 kHz、Qm≈1000 導致固有頻寬僅數十 kHz【V・S10】；撲翼所需機械頻率是 100–350 Hz【V・S2】。「一顆諧振體同時做功率轉換與致動」在物理上站不住，必須是「PT 高頻諧振腔＋低頻包絡調變＋雙向能流」，而該架構的實際往返效率**查無數據**【V・S2】。

### 5.4 節點支撐 vs 發射段振動：一個尚未被文獻處理的結構矛盾

已驗證的架構矛盾：諧振體必須節點支撐才不破壞 Q，而節點支撐正是最差熱通路【V・S5】。**本檔補充的推論**：節點支撐（低約束、近乎自由邊界）同時也是**抗發射段隨機振動與衝擊最差的安裝方式**，而壓電陶瓷約 10 MPa 即機械去極化【V・S5】，且硬質 PZT 在 300 V/mm DC 偏壓下 Qm 每 0.1 m/s 振動速度退化 17%【V・S25】。**「高 Q ⟂ 結構強固 ⟂ 散熱」是三方對立，在所有已驗證來源中找不到任何人正面處理。這是我對整個太空應用最大的技術疑慮。**【C】

### 5.5 放電負載會讓 PT 增益崩塌——而推進器的本質就是放電負載

已驗證：電漿一形成、負載電阻下降、增益就下降；設計準則要求「PT 不應對負載呈陡峭依賴」，但這正是最難達成的【V・S14】。**機會 A 的物理前提（元件即電極）與這個弱點是同一枚硬幣的兩面。**

### 5.6 輻射：LEO 沒問題，深太空與高能物理有問題

PZT 在 400 kGy 就有約 −25% 介電劣化【V・S11】；壓電陶瓷在 ITER 中子測試中可耐 ~10¹⁹ n/cm² 且去極化可遠端逆轉（但需額外高壓再極化電路）【V・S13】；單晶 AlN 耐 26.8 MGy gamma 但 k² 僅 6.1%【V・S12】。**分層判斷**：LEO 立方衛星年 TID 遠低於 400 kGy 量級【M】，**輻射不是 LEO 的否決因素**；深太空（木星系）與高能物理（CERN 要求 200 Mrad = 2 MGy，差 5 倍以上）則 PZT 很可能不合格，且存在**「耐輻射 ↔ 高耦合係數」的材料層級直接衝突**【V・S12】。另外 PZT 密度 ~7.8 g/cm³ 在物質量預算敏感的場合是負分【V・S8】。

### 5.7 產業歷史：這個元件族已經崩塌過一次

PT 唯一一次真正量產是 CCFL 背光逆變器（年銷 2,500–3,000 萬顆），LED 取代後**多數領導供應商停止高壓 PT 量產**，後續嘗試未再造就等量級出貨【V・S17】。對 A3 的意涵：昆蟲機器人與立方衛星推進都是**單量極小**的市場（帶磁強計的科學任務每年全球僅個位數）【V・S8】，**不可能單獨支撐一條陶瓷產線的固定成本**。

### 5.8 領域本身的失敗紀錄

- 昆蟲級撲翼機器人自 2000 年代中期投入至今**沒有商業產品**【M・定性，高把握】；姊妹檔 11 直接判定「昆蟲尺度飛行器目前無商業市場」【V・S2】。
- 「長期活躍論文、零商品」模式（超音波穿牆、壓電 X 光）通常代表存在未被論文誠實揭露的工程障礙【V・S4】。
- **【M・未驗證，兩輪皆無法查證】** 我對「Accion Systems 在 2024 年停止營運」有模糊記憶。**若屬實，這對立方衛星電推進市場的整體健康度是重大負面訊號；若不實，本條應整條刪除。在查證前任何人都不應引用本條。**

### 5.9 物理上限清單（A3 專用）

| 上限 | 內容 | 層 |
|---|---|---|
| 功率密度 | 實務 33 W/cm³（單層最佳 40，疊層 >13 @>94%）⇒ mg 級元件只能處理 mW 級功率 | V |
| 幾何最小尺寸 | 共振頻率由聲波長決定；要更小必須更高頻，而體積隨 f⁻³ 下降 ⇒ **功率處理隨頻率立方衰減** | C |
| 頻寬 | Qm≈1000、f<數十 MHz ⇒ 固有頻寬僅數十 kHz | V |
| 電壓 | 商用 PT 單體上限約 20 kV（CeraPlas）⇒ ±25 kV 級應用（可攜質譜）不合格 | V |
| 機械 | ~10 MPa 即去極化；Qm 隨振動速度退化（300 V/mm 下每 0.1 m/s −17%）；節點支撐與抗振對立 | V + C |
| 熱 | 節點支撐＝最差熱通路；真空無對流；安全溫度約居里溫度一半 | V |
| 負載 | 對電阻性／放電負載增益崩塌；負載調節能力弱 | V |
| 輻射 | PZT 400 kGy → −25%；耐輻射與高 k² 直接衝突 | V |
| 加速電位 | 壓電加速電子的實測軔致輻射上限 ~14 keV | V |

---

## 6. 未解問題（下一輪的檢索清單）

**因為兩輪皆 0 次搜尋，這份清單特別長且特別重要。以下每一條都附可直接貼上的檢索式。**

1. **RoboBee 的機上高壓解法到底是什麼？**（最高優先）`RoboBee X-Wing untethered solar cells series stacked high voltage avoid boost converter`；`Jafferis Nature 2019 untethered flapping wing microscale aerial vehicle mass`；`RoboFly laser powered boost converter mass Fuller UW`。**決策意義**：若最強團隊的解法是「用串聯光伏繞開升壓器」，機會 B 的市場拉力需重估。
2. **arXiv 2502.06166 的內容**（本輪新發現、與 A3 最對口的一篇）：`Portable High-Frequency High-Voltage Control Circuits Untethered Miniature Robots Dielectric Elastomer mass efficiency`。
3. **昆蟲級壓電致動器的真實電氣參數**（§3 的 15 mW 推算完全建立在假設值上）：`piezoelectric bimorph actuator microrobot capacitance nF drive voltage 200 V power consumption mW`。
4. **PT 諧振能量回收的往返效率**（§5.2 指出這是機會 B 的存亡數字）：`piezoelectric transformer capacitive load energy recovery round-trip efficiency`；並與 S19（雙向返馳）、S20（被動電荷回收）直接比較。
5. **Accion Systems 現況**（決定電噴霧推進子題是否還存在）：`Accion Systems shut down 2024`；`Accion Systems TILE thruster status`；`electrospray propulsion startup ceased operations`。
6. **FEEP／電噴霧的實際電壓與 PPU 質量預算**（沒有這些數字，機會 A 的重量優勢無法量化，也就無法賣）：`Enpulsion IFM Nano thruster PPU mass kg efficiency`；`FEEP emitter voltage 5 kV 10 kV power processing unit CubeSat`；`Busek BIT-3 PPU mass`；`Morpheus Space FEEP specifications`；`ThrustMe NPT30 specifications`。
7. **高 Q 壓電諧振體如何通過太空發射環境驗證？**（§5.4，我認為的最大技術疑慮）：`piezoelectric resonator random vibration qualification launch nodal mounting`；`piezoelectric transformer shock vibration space qualification`。**若查無，就必須自己做，應列為 gate 1。**
8. **壓電轉換器的實測磁簽章**（剩磁矩 A·m² / 交流磁場 nT@距離）——姊妹檔 15 已標查無並建議兩週實驗，本檔完全同意。
9. **PT 在真空中的除氣、multipaction 與 Paschen 行為**：`piezoelectric transformer vacuum outgassing multipaction high voltage space`。
10. **「PT 諧振腔＋外部容性致動器聯合諧振設計」是否有人做過？**（姊妹檔 11 標為查無並列為最有價值的 IP 機會，本輪找到 S23 的理論入口）：`piezoelectric transformer resonant tank load capacitance co-design`；專利檢索 `"piezoelectric transformer" AND "microrobot"`。
11. **微型 X 光源與手持 XRF 的實際商用規格**（確認 §4.5 剔除決定）：`Amptek Mini-X2 specifications kV µA`；`Moxtek miniature x-ray source specifications`；`Newton Scientific miniature x-ray tube`；`handheld XRF x-ray tube voltage Bruker Evident Hitachi`。
12. **PT 在 µA 級負載下的效率**（偵測器偏壓與 FEEP 的共同工作點；所有已發表 PT 效率數字都在數 W 至數十 W）：`piezoelectric transformer light load efficiency microampere output`。
13. **太空級 DC-DC 模組的質量與價格**：`VPT DC-DC converter space mass grams price`；`Crane Aerospace radiation hardened DC-DC mass`；`TT Electronics space DC-DC converter`。
14. **偵測器偏壓模組的具體規格**：`PMT high voltage bias module miniature 2 kV power consumption price`；`SiPM bias supply module Cockcroft-Walton size`；`Geiger tube 500 V bias converter portable dosimeter`。
15. **日文檢索補充**（兩輪皆完全未做）：`圧電トランス 高電圧 マイクロロボット`；`圧電トランス 宇宙 電気推進`；`圧電 X線源`。

---

## 7. 來源清單

**重要說明**：以下所有 URL 均來自本 repo 內姊妹檔案中**已附連結並經該檔 agent 標註驗證狀態**的來源。**本 agent 兩輪皆未能自行開啟或檢索任何一個 URL**，因此對這些連結持**二手信心**。凡姊妹檔原本標「未驗證」者沿用該標記。**本清單中沒有任何一個 URL、標題、期刊卷期、公司名或數字是我自行產生的。**

| # | 標題 | URL | 一句話說明 | 狀態 |
|---|---|---|---|---|
| S1 | An Ion Discharge-Driven Thruster Based on a Lithium Niobate Piezoelectric Transformer (*Micromachines* 16(3):277, 2025) | https://doi.org/10.3390/mi16030277 | LN 壓電變壓器作為離子放電推進器高壓源；LN 低阻尼/低損/高耦合的材料論證；文中「推重比 5.5」歸屬語意不明 | 主體已驗證，5.5 未驗證 |
| S2 | 姊妹檔 `11-electrostatic-actuators-artificial-muscle.md` 及其來源 26：MDPI *Micromachines* 13(7):1136；並含 arXiv 2502.06166 | https://www.mdpi.com/2072-666X/13/7/1136 ；https://arxiv.org/pdf/2502.06166 | 昆蟲尺度 DEA 蜻蜓機器人 317 mg / 4 翼 350 Hz / 升重比 1.49；arXiv 2502.06166 為非繫繩微型機器人的可攜高頻高壓控制電路（**內容本輪未取得**） | 已驗證（該檔） |
| S3 | XP Power / EMCO Q Series 產品頁 ／ Digi-Key Q101-5 ／ XP Power《Next-Generation, Miniature High Voltage Power Modules》白皮書 | https://www.xppower.com/product/Q-Series ；https://azcus.digikey.com/en/products/detail/xp-power/Q101-5/5873625 ；https://www.xppower.com/storage/documents/technical-articles/High-Voltage_WP_Next_Gen_Modules.pdf | 5 kV @ 0.125 in³、10 kV @ 0.614 in³、0.5 W；Q101-5 單價 USD 420.06 | 已驗證 |
| S4 | Ceramic Piezoelectric Transformer in Vacuum for Acceleration of Electrons and Production of X-Rays (PMC6073904) ／ *Scientific Reports* 2018「Piezoelectric Accelerator」／ US 9287080 | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6073904/ ；https://www.nature.com/articles/s41598-018-34831-8 ；https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/9287080 | 壓電加速電子產生 X 光，實測最大軔致輻射能量 ~14 keV；專利權利人未驗證 | 姊妹檔 07 標：14 keV 僅摘要級 |
| S5 | Piezoelectric resonators in DC-DC converters: current status and limits (Power Electronics News) ／ Loss mechanisms and high power piezoelectrics (*J. Mater. Sci.*) | https://www.powerelectronicsnews.com/piezoelectric-resonators-in-dc-dc-converters-current-status-and-limits/ ；https://link.springer.com/article/10.1007/s10853-005-7201-0 | 散熱與節點支撐的架構矛盾、負載調節能力弱、~10 MPa 機械去極化、居里溫度一半降額 | 姊妹檔 01 標：取自搜尋摘要 |
| S6 | Piezoelectric transformer-based high conversion ratio interface for driving dielectric actuator in microrobotic applications | https://www.researchgate.net/publication/308944819 | PT 24 V 輸入 → 2.5 kV 輸出驅動介電致動器，明確定位微型機器人 | 已驗證（姊妹檔 11） |
| S7 | State-of-the-Art DC-DC Converters for Satellite Applications (*Aerospace* 12(2):97, MDPI) | https://www.mdpi.com/2226-4310/12/2/97 | 太空級 DC-DC 需抑制 EMI 以免干擾磁強計等敏感儀器 | 已驗證（姊妹檔 15） |
| S8 | 姊妹檔 `15-magnetic-immune-clean.md`（含 Solar Orbiter MAG 等來源） | https://link.springer.com/article/10.1007/s11214-023-00989-5 | Solar Orbiter 需測 10 pT、船體 DC <10 nT、EMC quiet periods；JUICE 10.6 m / Europa Clipper 8.5 m 伸桿；PZT 密度 7.8 g/cm³ 對物質量預算不利；**壓電轉換器實測磁簽章查無** | 已驗證（該檔） |
| S9 | Power density of piezoelectric transformers improved using a contact heat transfer structure (PubMed 22293737) | https://pubmed.ncbi.nlm.nih.gov/22293737/ | 理論功率密度 330 W/cm³，實務上限 33 W/cm³；振動速度過大則發熱開裂 | 已驗證（姊妹檔 15） |
| S10 | Microwave-acoustic-based isolated gate driver for power electronics (arXiv 2511.13412) | https://arxiv.org/pdf/2511.13412 | 明指現行 PT 因 f<數十 MHz、Q≈1000 導致固有頻寬僅數十 kHz | 已驗證 |
| S11 | Effects and mechanisms of gamma irradiation on electrical properties of PZT-S and PZT-N (*Ceramics International*) | https://www.sciencedirect.com/science/article/abs/pii/S0272884226034942 | 400 kGy → PZT 介電性能約 −25% | 已驗證（姊妹檔 15） |
| S12 | Radiation tolerance of piezoelectric bulk single-crystal aluminum nitride (PubMed 24960710) ／ Single-Crystal AlN Wafer-Based BAW for Piezoelectric Power Conversion (arXiv 2603.19409) | https://pubmed.ncbi.nlm.nih.gov/24960710/ ；https://arxiv.org/abs/2603.19409 | AlN 耐快中子 1.85×10¹⁸、熱中子 5.8×10¹⁸ n/cm²、gamma 26.8 MGy；但 k² 僅 6.1% | 已驗證（姊妹檔 15/01） |
| S13 | Radiation tolerance testing of piezoelectric motors for ITER (first results), *Fusion Eng. Des.* | https://www.sciencedirect.com/science/article/abs/pii/S0920379622000175 | ~10¹⁹ n/cm² (E>0.1 MeV)；去極化可遠端逆轉；330 °C/200 °C 多循環存活 | 已驗證（姊妹檔 15） |
| S14 | Discharge plasmas generated by piezoelectric transformers and their applications (*Plasma Sources Sci. Technol.* 15(2):S07, IOP) ／ Effects of capacitive versus resistive loading on high transformation ratio piezoelectric transformers | https://iopscience.iop.org/article/10.1088/0963-0252/15/2/S07 ；https://www.researchgate.net/publication/260742523 | 「PT 同時作為高壓產生器與放電電極」的原始論證；電漿點燃後負載電阻下降導致增益崩塌 | 已驗證（姊妹檔 01/11） |
| S15 | Cold plasma from a single component (TDK Electronics) ／ CeraPlas Element 產品資料 ／ Cold Plasma Market Sizing (Towards Healthcare) ／ Piezoelectric direct discharge plasma | https://www.tdk-electronics.tdk.com/en/373562/tech-library/articles/applications-cases/applications-cases/cold-plasma-from-a-single-component/1109546 ；https://www.tdk-electronics.tdk.com/download/2307712/39eb3392c71d1191b103aa31c6a0f1c5/ceraplas-db.pdf ；https://www.towardshealthcare.com/insights/cold-plasma-market-sizing ；https://en.wikipedia.org/wiki/Piezoelectric_direct_discharge_plasma | CeraPlas：12–24 Vpp 輸入、最高 20 kV 輸出、47.3×20×20 mm、TRL 9；冷電漿市場 2.92B(2024)→11.14B(2034) | 已驗證（姊妹檔 07/10/11） |
| S16 | Motional-Current-Sensing Method and Simplified Closed-Loop Control Strategy for PR-based DC-DC Converters (arXiv 2605.15279) | https://arxiv.org/pdf/2605.15279 | 以運動電流做自感測式閉迴路控制——「元件即感測器」的技術基礎 | 已驗證（姊妹檔 01/15） |
| S17 | Piezoelectric Transformers: An Historical Review (*Actuators* 5(2):12, MDPI) | https://www.mdpi.com/2076-0825/5/2/12 | CCFL 時代年銷 2,500–3,000 萬顆；LED 取代後多數領導供應商停止高壓 PT 量產 | 已驗證（姊妹檔 01/15） |
| **S18** | **Optimal design of piezoelectric transformer for high efficiency and high power density (*Sensors & Actuators A*) ／ 50 Years of Piezoelectric Transformers (mmech.com)** | https://www.sciencedirect.com/science/article/abs/pii/S0924424705001585 ；https://www.mmech.com/transformers ；https://www.mmech.com/images/stories/Standard_Products/Transformers/PT_Introduction/50_Years.pdf | **本輪新增**：單層最佳化 40 W/cm³；疊層 >94% 效率、>13 W/cm³；Nihon Ceratec 升壓比 >80、效率 >90% | 已驗證（姊妹檔 11） |
| **S19** | **Bidirectional Flyback Converter with Multiple Series Connected Outputs for High Voltage Capacitive Charge and Discharge Applications** | https://www.researchgate.net/publication/269398568 | **本輪新增・關鍵反證**：磁性方案已做到 0 V ↔ 2.5 kV 高壓容性充放電與能量回收 | 已驗證（姊妹檔 11） |
| **S20** | **Power-Efficient Driver Circuit for Piezo Electric Actuator with Passive Charge Recovery (*MDPI Energies* 13(11):2866)** | https://doi.org/10.3390/en13112866 | **本輪新增・關鍵反證**：2 顆二極體＋1 顆電阻可回收約一半電荷 | 已驗證（姊妹檔 11） |
| **S21** | **An Easy-to-Implement Toolkit to Create Versatile and High-Performance HASEL Actuators for Untethered Soft Robots (*Advanced Science* 2019, PMC6662077)** | https://pmc.ncbi.nlm.nih.gov/articles/PMC6662077/ | **本輪新增**：非繫繩機器人含電池電源約 100 g、5 W、0–10 kV（0–5 V 輸入）、3.7 V/500 mAh LiPo | 已驗證（姊妹檔 11） |
| **S22** | **A Pocket-Sized Ten-Channel High Voltage Power Supply for Soft Electrostatic Actuators (*Adv. Mater. Technol.* 2022)** | https://advanced.onlinelibrary.wiley.com/doi/full/10.1002/admt.202101469 | **本輪新增**：250 g、8.4×13.3×2 cm 的 10 通道 kV 電源——目前「可攜多通道高壓」的實際重量級距 | 已驗證（姊妹檔 11） |
| **S23** | **Simultaneous quasi-static displacement and force self-sensing of piezoelectric actuators by detecting impedance (*Sensors & Actuators A*)** | https://www.sciencedirect.com/science/article/abs/pii/S0924424717317478 | **本輪新增**：以阻抗/諧振頻率變化做壓電自感測；並聯電容負載使串聯與並聯諧振同時下降，並聯諧振附近最敏感——§4.4 與「PT 腔／致動器電容聯合設計」的物理入口 | 已驗證（姊妹檔 11） |
| **S24** | **Portable, Battery Operated Capillary Electrophoresis with … Ionization Source for Mass Spectrometry (*J. Am. Soc. Mass Spectrom.*) ／ Mini 12 (*Anal. Chem.*)** | https://link.springer.com/article/10.1007/s13361-015-1314-8 ；https://pubs.acs.org/doi/10.1021/ac403766c | **本輪新增**：可攜質譜 ±25 kV HVPS、系統 <4 lb、12 V 鋰電池約 10 h；Mini 12 為 2–10 kV | 已驗證（姊妹檔 11） |
| **S25** | **姊妹檔 `01-pt-power-conversion-sota.md`（硬質 PZT 振動速度退化）** | （見該檔 S7 條目） | **本輪新增**：硬質 PZT 在 300 V/mm DC 偏壓下，Qm 每 0.1 m/s 振動速度退化 17%（軟質更嚴重）——對高振幅微型化設計是硬限制 | 已驗證（該檔）；原始 URL 見該檔 |

**無 URL 的內容一律屬【M】（模型記憶）或【C】（自行推算），已在正文逐處標記，並在 §6 附上下一輪的檢索式。**

---

### 附註：對客戶決策的一句話建議

A3 的正確問法**不是「壓電能不能做出更輕的高壓源」**（能，但對照組 XP Power/EMCO Q 已是 2 cm³ / USD 420，且本輪證明連「能量回收」這個第二賣點都已被 3 顆分立零件的被動回收電路佔領），**而是「有沒有一個系統，它的高壓源必須同時是放電電極或發射極」**——因為那才是磁性方案在物理上沒有對應物的地方，也是本領域唯一已有 2025 年論文實證（S1）且在鄰近領域 TRL 9（CeraPlas, S15）的模式。**建議把 A3 資源集中在 §4.1，並用三個便宜的 gate 實驗先殺掉它：(1) 高 Q 壓電體在發射段隨機振動下的存活與 Q 值劣化（§5.4，公開文獻查無，最大未知）；(2) PT 在帶放電電流負載下的增益崩塌幅度（§5.5，已知會發生，只是不知多嚴重）；(3) PT 諧振能量回收的往返效率，並與 S19/S20 直接對比（§5.2，決定機會 B 存亡）。任一失敗，對應的那條線就該收掉。**
