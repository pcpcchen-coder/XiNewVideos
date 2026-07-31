# 工程實作面：驅動與控制電路/IC——要讓「兩用元件」真的能用，電路端得解決什麼

> 一句話結論：壓電兩用元件的真正瓶頸不在陶瓷體，而在「**高壓容性負載的無功能量往返**」與「**共振點隨溫度／負載／老化漂移**」這兩件事——前者決定你的效率天花板（被動式電荷回收物理上只能回收一半，要更高必須做主動同步開關 IC），後者決定你的系統能不能在實驗室外活下來（負載失配可讓損耗暴增 ~50%）；而現成商用驅動 IC 只覆蓋「低壓觸覺」與「超音波 pulser」兩塊，kV 級與多埠雙用完全沒有現貨，必須自己做。

---

## 0. 研究方法與限制（誠實揭露）

**必須先講清楚的重大限制，請客戶在採信任何數字前先讀完這一節：**

1. **WebFetch 在本環境被 egress policy 全面封鎖**（任何 URL 一律 403），因此本文件**沒有任何一手原文查核**，所有外部事實均來自搜尋結果摘要或本專案既有 dossier。
2. **更嚴重的限制：本 session 的 WebSearch 預算在我開始工作時已被其他並行子任務用盡（200/200）**。我實際只成功執行了 **2 次** WebSearch（規劃是 25–35 次），主題分別為「壓電致動器驅動拓樸與電荷回收效率」與「Boréas CapDrive 能量回收」。**原訂要查的 TI DRV2667/DRV8662 架構、ST/Microchip 高壓驅動 IC、Class-E 壓電變壓器驅動、PLL 頻率追蹤實作、Preisach/Prandtl-Ishlinskii 遲滯補償、儀器報價等主題，全部沒有本輪檢索支持。**
3. 為了讓這份 dossier 仍有工程價值，我採取的處置是：
   - **【已檢索】**標記＝本輪 2 次搜尋直接回傳的內容（附 URL）。
   - **【轉引】**標記＝引用自本專案同目錄的 `01-pt-power-conversion-sota.md` 與 `02-dual-use-active-passive-concept.md` 已列出的來源 URL；這些 URL 我**未親自開啟驗證**，但它們是同一專案內已經過一輪檢索的結果。
   - **【領域常識・未經本輪檢索驗證】**標記＝電路工程與壓電量測的教科書級原理與標準流程（BVD 萃取、Mason/KLM、PLL 鎖相、阻抗掃頻等）。這類內容不含具體數字宣稱時風險低；**凡涉及具體數字或型號，我一律另行標註「未驗證」**。
4. **本文件中所有儀器價格皆為量級估計，沒有任何一筆取得可驗證報價，標示為「未驗證量級」。採購前必須重新詢價。**
5. 我**沒有**捏造任何專利號、論文標題或型號。凡我不確定的規格（例如某顆 IC 的實際輸出電壓範圍），我寧可寫「查無／未驗證」也不填數字。

---

## 1. 結論摘要

1. **被動式電荷回收有一個硬性的物理上限：一半。** 用「兩顆二極體＋一顆電阻」這種最輕量的被動回收，只能回收儲存在寄生／負載電容中電荷的約 50%（需該電阻遠大於二極體順向電阻）。要突破一半，必須改用帶電感的主動同步開關（雙向 buck-boost 式）拓樸。【已檢索，來源 S1 群】
2. **主動式 LC 電荷回收的實測收益量級是「損耗降一半」，不是「效率翻倍」。** 交錯式 boost 級聯改良型半橋＋LC 網路同時驅動雙晶片 PZT 並回收電荷，相較傳統驅動法，**在 40 Hz / 80 Hz / 120 Hz 分別降低電路能量損耗 49% / 50% / 55%**；同一批文獻中一個微型撲翼案例的整體效率也只從更低值提升到 **30.0%**——注意這是「系統效率 30%」，不是 90%。【已檢索，S1】
3. **商用 IC 的最佳宣稱與學術實測有一個數量級的落差，要小心讀。** Boréas CapDrive 宣稱能量回收可使壓電系統整體電流消耗**降低最多 90%**、比競品壓電驅動 IC **效率好 10 倍**、比 LRA 省電 **20 倍**。這些是廠商宣稱值、且是「電流消耗」而非「轉換效率」，與上述學術 49–55% 損耗降低不是同一個度量。【已檢索 S2/S3；20× 為【轉引】D2-5】
4. **kV 級輸出在 IC 上做不出來，必須由壓電體自己升壓。** 這是整個「兩用元件」路線最重要的電路架構結論：TDK CeraPlas 的做法是 **12–24 Vpp 輸入 → 最高 20 kV 輸出**，升壓完全由陶瓷體完成，IC 只需處理十幾伏。這意味著你的 IC 規格書可以停在低壓 BCD，**不必碰高壓製程**——這對研發成本是決定性的好消息。【轉引 D1-S9 / D1-S25】
5. **共振點漂移是控制端的頭號敵人，且已有明確的量化警訊：PT 負載失配會讓損耗增加約 50%。**【轉引 D2-47，該來源自註「數字未一手驗證」】另外硬質 PZT 在 300 V/mm DC 偏壓下，**Qm 每 0.1 m/s 振動速度退化 17%**——代表你的等效電路參數會隨驅動振幅本身改變，這是非線性追蹤問題，不是單純的溫漂補償。【轉引 D1-S7】
6. **自感測（同一顆元件同時致動＋感測）在業界最嚴苛的應用中被明確否決。** 頂級奈米定位（Physik Instrumente）仍採用**外部電容式 direct metrology**，而非自感測；根本原因是橋式自感測電路的電容失衡——壓電體的 C0 隨溫度與偏壓漂移，橋一失衡就把致動訊號洩進感測路徑，造成訊號污染與閉迴路不穩。【轉引 D2-2、D2-3】
7. **有兩條現成的原型捷徑，會直接決定你的研發時程。** (a) 低壓／中壓、需要「驅動＋感測同體」→ 直接買 Boréas BOS1901/BOS1921/BOS1931（單通道）或 BOS0614（四通道整合感測）當評估板；BOS1901 被描述為「市場上唯一同時觸發觸覺並感測按壓力的壓電驅動 IC」。(b) 需要多通道 ±數十～百伏方波、高 slew rate → 借用醫用超音波 **pulser IC** 生態（SOI 高壓製程既有產品線）。【(a) 已檢索 S3 ＋【轉引】D2-4/D2-6；(b) 為【領域常識・未經本輪檢索驗證】】
8. **頻寬是「兩用」的結構性限制，不是調校問題。** bulk-mode 壓電變壓器因 f < 數十 MHz 且 Qm ≈ 1000，**固有頻寬僅數十 kHz**，明確不足以驅動 WBG 閘極。任何「同一顆元件同時做功率與高速訊號」的構想都必須先過這一關。【轉引 D1-S36 / D2-48】

---

## 2. 現況：技術 / 產品 / 玩家

### 2.1 驅動拓樸的四個家族（工程分類）

| 家族 | 代表電路 | 適用場景 | 主要代價 | 驗證狀態 |
|---|---|---|---|---|
| **線性放大** | 高壓 op-amp / Class-AB（實驗室高壓放大器） | 研發階段、任意波形、低噪聲量測 | 效率極低（無功能量全部變熱）；散熱與體積不可攜 | 領域常識 |
| **開關＋LC 濾波** | 半橋 / 全橋 ＋ 串聯電感，Class-D 式 | 中頻大位移致動、觸覺、閥門 | 需電感；EMI；死區時間損耗 | 已檢索（半橋驅動壓電致動器設計與控制，S1 群） |
| **主動電荷回收 / 雙向** | 交錯式 boost ＋ 改良半橋 ＋ LC 回收網路；Boréas CapDrive 屬此類 | 電池供電、佔空比低但重複率高的致動 | 控制複雜；回收路徑本身有損耗 | 已檢索（S1、S2） |
| **諧振驅動** | Class-E / Class-DE，ZVS，固定頻率 | 壓電變壓器、高頻高壓、電漿源 | 對負載與頻率極敏感；失配即崩效率 | 【轉引】D1（Stanford Rivas-Davila 用 Class-E ＋ PR，180→60 V / 89 W / 97%） |

**被動電荷回收（最低成本版本）**：只需**兩顆二極體＋一顆電阻**（電阻值需遠大於二極體順向電阻），即可回收約一半的電容儲存電荷；實測顯示**升力不受影響、功耗下降**。這是「先用最便宜的方法拿到 50%」的務實起點。【已檢索 S1 群】

### 2.2 商用 IC 玩家地圖（本輪僅驗證到 Boréas 一家）

| 玩家 | 產品 | 已驗證到的內容 | 缺口 |
|---|---|---|---|
| **Boréas Technologies**（加拿大） | BOS1901 / BOS1921 / BOS1931（CapDrive 單通道）、BOS0614（四通道整合感測） | CapDrive 架構「從致動器內部負載電容回收能量並再利用，而非放掉浪費」；宣稱電流消耗最多降 90%、較競品效率高 10×；BOS1901 同時驅動與感測按壓力 | **本輪未能取得任何一顆的實際輸出電壓、輸出電流、靜態功耗、封裝與單價** |
| **Texas Instruments** | DRV2667（客戶題目指定）、DRV8662 | **本輪查無**（搜尋預算用盡） | 架構（整合 boost + 波形記憶體 + 數位介面）為領域常識，但**電壓/效率數字一律未驗證** |
| **ST / Microchip** | 高壓驅動、超音波 pulser 產品線 | **本輪查無** | 需下一輪補查 |
| **TDK** | PowerHap 致動器（元件端，非 IC） | 致動器內建感測、≤25 N 壓力偵測、1 Hz–1000 Hz 激振 | 【轉引】D2-8 |
| **Synaptics** | 與 Boréas 合作壓電觸控板 | 大廠採用訊號 | 【轉引】D2-7 |

**台灣視角的重要觀察**：EDOM（益登科技）已在代理 Boréas BOS1901/BOS1921 產品線【已檢索，edomtech.com 產品頁】——這代表**在台灣取得評估樣品與 FAE 支援的路徑是通的**，可以把 PoC 時程壓縮數個月。

### 2.3 高壓製程的選擇（【領域常識・未經本輪檢索驗證】）

- **BCD（Bipolar-CMOS-DMOS）**：觸覺／中壓驅動 IC 的主流；整合類比、數位、功率於單晶片，適合把 boost、H-bridge、感測前端與 I²C 全塞進一顆。研發成本最低、IP 生態最完整。
- **SOI 高壓製程**：介電隔離、latch-up 免疫、通道間隔離好，是**多通道高壓 pulser**（醫用超音波）的標準選擇。若「兩用元件」需要陣列化（每個元件獨立收發），SOI 是預設答案。
- **GaN**：低 Qoss、可做 MHz 級軟開關，理論上最適合驅動高頻壓電諧振體；但缺乏整合類比／感測，只能當分立功率級，且高溫可靠度與雙向應用仍在演進。
- **kV 級**：**單晶片做不到，也不該做**。正確架構是讓壓電體自己升壓（Rosen 型），IC 只驅動低壓側——這正是 CeraPlas 12–24 Vpp → 20 kV 的做法【轉引 D1-S9】。這條結論應該直接寫進客戶的架構規格。

---

## 3. 關鍵數字表

| 項目 | 數字 | 度量定義（很重要） | 來源 | 可信度 |
|---|---|---|---|---|
| 被動電荷回收上限 | **約 50%** | 儲存於負載/寄生電容之電荷的可回收比例（2 二極體 + 1 電阻） | S1 群 | 已檢索（摘要） |
| 主動 LC 電荷回收收益 | **-49% / -50% / -55%** @ 40 / 80 / 120 Hz | **電路能量損耗**降低比例（非效率） | S1（Energies 13(11) 2866 及同批） | 已檢索（摘要） |
| 帶電荷回收的撲翼系統效率 | **30.0%** | 系統整體效率；升力不受影響 | S1 群 | 已檢索（摘要） |
| Boréas CapDrive | **最多 -90% 電流消耗**、**10×** 優於競品壓電 IC | 廠商宣稱，**應用相依** | S2、S3 | 已檢索（廠商宣稱） |
| Boréas vs LRA | **20×** 省電 | 廠商宣稱 | D2-5 | 轉引 |
| kV 級升壓 | **12–24 Vpp → 最高 20 kV** | 由陶瓷體完成，IC 側僅低壓 | D1-S9 / D1-S25 | 轉引 |
| PT 負載失配代價 | **損耗 +50%** | 失配 vs 匹配 | D2-47 | 轉引（該來源自註未一手驗證） |
| 驅動振幅對等效參數的影響 | 硬質 PZT @300 V/mm DC 偏壓：**Qm 每 0.1 m/s 振動速度退化 17%** | 非線性；軟質 PZT 更嚴重 | D1-S7 | 轉引 |
| 高功率點效率崩塌 | 理論 98.2% → 最高功率點實測 **93.3%** | MIT PR DC-DC，275→150 V / 12 W / 493 kHz | D1-S1 | 轉引 |
| 頻寬天花板 | Qm≈1000、f<數十 MHz ⇒ **頻寬僅數十 kHz** | 明示不足以驅動 WBG 閘極 | D1-S36 / D2-48 | 轉引 |
| 切換式電荷操作實測天花板 | SSHC **80% 翻轉效率**、9.7× 提升、8 顆切換電容、0.35 µm CMOS | 能量採集介面電路（無電感） | D2-37 | 轉引 |
| 功率＋資料同軸（穿金屬壁） | **17.37 Mbps ＋ 50 W**（63.5 mm 鋼）；早期 12.4 Mbps ＋ 32.5 W | 同一換能器同時傳功率與資料 | D2-16 | 轉引 |

**度量陷阱警告**：上表第 2、4 列常被混為一談。「損耗降低 50%」在一個原本效率 90% 的系統代表效率升到 95%；在一個原本效率 20% 的系統代表效率升到 33%。**Boréas 的「電流消耗降 90%」是系統層級的平均電流，不能拿來當轉換效率報給客戶。** 做競品比較時務必先統一度量。

---

## 4. 研發任務拆解（可直接轉成 WBS 與採購清單）

### 4.1 Phase 0：不寫一行 RTL 就能做的事（0–3 個月，成本最低，篩選價值最高）

**T0-1 等效電路萃取流水線（最優先）**
- 用阻抗分析儀掃頻，取 |Z|、∠Z 全頻譜，找出串聯共振 fs（阻抗極小）與並聯共振 fp（阻抗極大）。
- 萃取 **Butterworth-Van Dyke（BVD）**：C0（並聯靜態電容，低頻段量測）、L1/C1/R1（運動支路）。標準關係：Qm = fs/(f₂−f₁)（−3 dB 或 45° 相位點）、k² ≈ 1 − (fs/fp)²。多模態時，每一個模態掛一支獨立的 R-L-C 串聯支路，全部並聯到同一個 C0 上。【領域常識】
- 進一步做 **Mason / KLM** 三端口模型（1 電端口 + 2 聲端口），這是把「機械側負載」也算進來的必要工具——「兩用元件」的定義就是機械側要接東西。【轉引 D2-35、D2-36】
- **交付物**：一個能吃阻抗分析儀 .csv、吐出 SPICE subckt 的腳本；以及對同一批陶瓷體在 −40 / 25 / 85 / 125 °C 下的 BVD 參數表。**這張表就是你所有控制演算法的規格書。**

**T0-2 溫漂 / 老化 / 振幅相依性的實測地圖**
- 三個軸各自量：溫度（環境箱）、驅動振幅（振動速度，需 LDV）、時間（老化，log(t) 規律）。
- **特別要量**：fs 與 Qm 隨驅動振幅的變化。因為 D1-S7 已指出 Qm 隨振動速度非線性退化，這代表**你的 PLL 在大訊號下追的目標點會自己移動**——這是小訊號阻抗分析儀量不出來的。
- **交付物**：fs(T, v, t) 的三維查表 + 誤差帶。決定你要用開迴路查表補償、還是必須做閉迴路追蹤。

**T0-3 現貨 IC 打樣（時程加速器）**
- 買 Boréas BOS1901/BOS1921 評估板（台灣可經 EDOM 取得）驗證「驅動＋自感測同體」的訊號品質實際有多好，直接量串音與感測解析度。
- 若需多通道高壓方波，評估醫用超音波 pulser IC 評估板作為 ±數十伏多通道平台。
- **這一步的目的是回答一個 go/no-go 問題：現貨能做到什麼程度？只有現貨做不到的部分才值得自己做 IC。**

### 4.2 Phase 1：控制演算法（3–9 個月）

**T1-1 頻率追蹤與鎖定**
- 三種可選機制，建議並行評估：
  1. **相位鎖定（PLL）**：鎖 V 與 I 的相位差。優點成熟；缺點是 C0 造成的相位偏移會讓「相位零點」不等於「真實機械共振點」，必須先做 C0 補償（並聯負電感或數位扣除 jωC0）。
  2. **運動電流感測（motional current sensing）**：直接把 C0 的電流扣掉，剩下的就是機械支路電流，用它做回授。本專案 dossier 01 已收錄一篇專門做這件事的論文（arXiv 2605.15279，「Motional-Current-Sensing Method and Simplified Closed-Loop Control Strategy for PR-based DC-DC Converters」）【轉引 D1-S12】。**這是我認為最值得投資的路線**，因為它同時解決「頻率追蹤」與「自感測解耦」兩個問題。
  3. **擾動觀察 / MPPT 式**：對輸出功率或效率做爬坡。優點不需相位資訊；缺點慢、有穩態抖動。
- **關鍵設計決策：操作在 fs 還是 fs–fp 之間？** 功率轉換通常需要電感性阻抗以達成 ZVS，因此操作點落在 fs 與 fp 之間；純致動則常在 fs 附近取最大位移。「兩用」代表這兩個需求會打架——**這是本題最核心的架構矛盾，必須在 Phase 1 用實驗定案。**
- **失效模式必測**：負載突變（開路→短路→額定）時，追蹤環路會不會跳到雜散模態（spurious mode）上鎖住？dossier 01 已明確指出「雜散共振模態困擾低阻抗（高功率）諧振體設計」【轉引 D1-S5】。要設計模態鎖定的保護區間（frequency guard band）。

**T1-2 自感測解耦**
- **橋式電容平衡法**：把 C0 用一顆匹配電容做橋，差動輸出即為運動電荷。**已知致命弱點**：C0 隨溫度與偏壓漂移，橋一失衡就洩漏；文獻明確記載這會造成訊號污染與閉迴路不穩【轉引 D2-2】。實務上必須做**自適應橋平衡**（線上估測 C0 並調整）。
- **觀測器 / 模型基礎法**：用 BVD 模型做狀態觀測器，從驅動電壓與總電流反推機械狀態。優點是不需精密匹配元件；缺點是模型誤差直接變成估測誤差。
- **電荷放大器**：把感測輸出接電荷積分器（低偏壓電流運放 + 積分電容 + 高阻值洩放電阻）。設計要點是低頻極點（洩放電阻×積分電容）與運放偏壓電流造成的漂移。
- **遲滯與潛變補償**：Preisach 與 Prandtl-Ishlinskii 是文獻標準的遲滯反模型，**本輪未能檢索驗證任何實測補償殘差數字，不給數字**。另一條迴避路線是**電荷驅動（charge drive）取代電壓驅動**，原理上可大幅壓抑遲滯——但代價是需要高阻抗電流源與漂移抑制，**具體改善倍率未經本輪驗證，不引用**。

**T1-3 多埠 / 雙功能共存策略**
| 策略 | 做法 | 已知證據 | 風險 |
|---|---|---|---|
| **時間分割** | 同一元件輪流做致動與感測／採集 | 單片 MFC 時間多工做應變感測＋能量採集已有文獻【轉引 D2-41】 | 佔空比一分，兩邊都變弱；切換暫態需等機械暫態衰減（Q=1000 ⇒ 衰減需 ~Q 個週期，這是硬性的等待時間） |
| **頻率分割 / 模態分離** | 用不同振動模態承載不同功能（例如基頻做功率、泛音做通訊） | Berkeley 有 overtone piezoelectric resonator 技轉掛牌【轉引 D1-S38】 | 模態間有機械耦合，串音難完全消除；泛音的 k² 通常較低 |
| **功率＋資料同軸** | 同一換能器同時傳功率與資料，收端分離 | 穿金屬壁 17.37 Mbps + 50 W【轉引 D2-16】；全雙工＋頻率追蹤已有專利 US20150049587A1【轉引 D2-17】 | 功率訊號是資料的巨大干擾源；需要良好的濾波與回音消除 |

**串音（crosstalk）預算是這一節唯一真正需要交付的數字。** 建議 Phase 1 就定義：致動訊號洩漏到感測路徑的允許量（dB），並用它反推橋平衡精度與 ADC 動態範圍需求。

### 4.3 Phase 2：IC 化（9–24 個月，只在 Phase 0/1 證明現貨不夠時才做）

- 製程選擇：預設 **BCD**（若架構遵守「kV 由陶瓷體升壓」的原則，IC 側電壓可壓在數十伏內）；陣列化才考慮 SOI。
- 必須整合的區塊：升壓級 → 雙向 H 橋（含電荷回收路徑）→ C0 補償／運動電流感測前端 → ADC → 追蹤環路（數位）→ 波形記憶體 → I²C/SPI。
- **不要低估數位部分**：頻率追蹤、自適應橋平衡、遲滯反模型三者都需要 MAC 運算，這會決定你要不要放一顆小 DSP/MCU 核。

### 4.4 人才與設備清單

**人才（缺一不可，這是本題的主要進入障礙）**

| 角色 | 為什麼非要不可 |
|---|---|
| 類比／電源 IC 設計 | 高壓開關、電荷回收路徑、低噪聲感測前端 |
| **機電耦合建模**（最稀缺） | BVD/Mason/KLM 萃取、COMSOL 壓電多物理、模態辨識。**這個角色在台灣的電源 IC 公司幾乎不存在，通常要從超音波/MEMS/機械所找。** |
| 控制／DSP | PLL、自適應濾波、觀測器、遲滯反模型 |
| 材料／陶瓷製程 | 決定 Qm、溫漂、去極化邊界；若要客製陶瓷體必備 |
| 可靠性 | 熱去極化（安全溫度約居里溫度一半）、~10 MPa 機械去極化、循環疲勞【轉引 D1-S28、D1-S5】 |
| 量測工程 | 阻抗掃頻自動化、LDV 校正、EMC |

**設備（價格皆為未驗證量級估計，採購前必須詢價）**

| 設備 | 用途 | 量級（**未驗證**） |
|---|---|---|
| 阻抗／材料分析儀（客戶題目點名 Keysight E4990A 級） | BVD 參數萃取，最核心的一台 | 中高六位數新台幣～百萬級 |
| 高壓功率放大器（寬頻、可驅動容性負載） | 開迴路激振、拓樸比較基準 | 數十萬～百萬級 |
| 雷射都卜勒測振儀 LDV（單點；掃描式更貴） | 量真實機械位移／振動速度，驗證自感測是否可信 | 掃描式可達數百萬級 |
| 高壓差動探棒 + 高頻寬示波器 + 電流探棒 | 效率量測（電壓電流相位精度直接決定效率量測誤差） | 數十萬級 |
| 熱像儀 | 找損耗熱點、驗證共振 vs 離共振發熱機制 | 十萬級 |
| 環境箱（−40～125/150 °C） | 溫漂地圖、車規降額 | 數十萬級 |
| 功率分析儀 / 高精度電表 | 系統效率的可信度來源 | 數十萬級 |
| COMSOL Multiphysics（含 MEMS/Acoustics 模組）或 ANSYS | 模態預測、雜模辨識 | 年授權數十萬級 |

**量測方法學的警告**：驅動容性負載時，電壓與電流相位差接近 90°，效率量測誤差對相位誤差**極度敏感**（cos φ 在 φ≈90° 附近斜率最大）。**探棒延遲的 de-skew 校正沒做好，效率數字可以差好幾個百分點。** 這是壓電效率報告最常見的造假來源（不論有意無意）。建議一律用「輸入 DC 功率 vs 輸出有效功」的黑盒法交叉驗證 AC 相位法。

---

## 5. 反面證據、失敗案例與物理上限

1. **業界最頂級的應用不用自感測。** Physik Instrumente 的高階奈米定位仍採用外部電容式 direct metrology【轉引 D2-3】。這是對「同一顆元件既致動又感測」最強的商業反證：在精度真的要緊的地方，工程師選擇多加一顆感測器。**若客戶的賣點是「省掉感測器」，這個案例必須先被回答。**
2. **電荷回收的一半是物理牆，不是工程懈怠。** 被動 RC/二極體法只能回收約 50%【已檢索 S1】；要更高必須加電感做主動同步開關，而電感正是客戶想避開的磁性元件——**「用壓電省掉電感」的敘事在驅動端會自我矛盾**：高效率電荷回收本身就需要電感。這一點必須誠實面對。
3. **實測效率總是低於理論，而且是在你最需要的工作點崩塌。** MIT 的 PR DC-DC 理論 98.2%，但**最高功率點實測只有 93.3%**【轉引 D1-S1】。趨勢是一致的：功率越大，效率越差。
4. **負載失配代價巨大。** PT 在失配下損耗 +50%【轉引 D2-47】。而「兩用元件」的定義就是負載會在兩種用途間切換——**負載變動是本架構的常態而非例外**，這使得失配問題從「邊角案例」升級為「主線問題」。
5. **切換式電荷操作的實測天花板約 80%。** 無電感 SSHC 的電壓翻轉效率實測 80%【轉引 D2-37】，這給了「純開關電容式電荷處理」一個現實的效率上限參考。
6. **頻寬與 Q 的根本取捨。** 高 Q 給你低損耗與高功率密度，但同時把頻寬鎖死在數十 kHz【轉引 D1-S36】。**你不能同時要高效率儲能與寬頻訊號處理**——這是 Q 的定義決定的，沒有電路技巧可以繞過。任何「同一顆元件既做電源又做寬頻通訊」的提案在這裡就該被砍掉。
7. **散熱與支撐的架構矛盾。** 諧振體必須在振動節點支撐才不破壞 Q，而節點支撐正是最差的熱通路【轉引 D1-S5】。這代表**驅動電路能推多少功率進去，實際上是被機械封裝而不是被半導體決定的**。做 IC 前先做熱模型。
8. **產業已經失敗過一次。** CCFL 時代壓電變壓器年銷 2,500–3,000 萬顆，LED 取代後供應商成建制退場【轉引 D1-S3】。教訓是：壓電方案的生存依賴於「沒有磁性替代品」的利基，一旦替代路徑出現，量會瞬間蒸發。這對驅動 IC 的投資回收期評估是關鍵風險。
9. **本輪檢索的最大空白本身就是一條反面證據候選**：我**沒能**在本輪找到任何「專為壓電主動/被動兩用元件設計」的商用驅動 IC 或參考設計。現有商用 IC 全部落在「觸覺致動」與「超音波收發」兩個既有市場。**這既可能代表機會（沒人做），也可能代表已被評估過而不划算（有人做過但沒成）——本輪無法區分，必須在下一輪補查。**

---

## 6. 未解問題

1. **TI DRV2667 / DRV8662、ST、Microchip 高壓驅動 IC 的實際架構、輸出電壓/電流、效率與單價全部未查。** 這直接決定「現貨能不能用」的 go/no-go，是下一輪的第一優先。
2. **Boréas CapDrive 的專利範圍是什麼？** 若「從致動器負載電容回收能量」的核心手法已被專利覆蓋，客戶自研 IC 會直接撞牆。本輪完全未查專利。建議下一輪以 Boréas Technologies 為受讓人做專利檢索。
3. **共振點 vs 反共振點的操作選擇，在「兩用」情境下有沒有已發表的統一解？** 功率轉換要電感性區間、致動要 fs 附近，這個矛盾是否有人提出過雙操作點切換架構？本輪查無。
4. **遲滯補償（Preisach / Prandtl-Ishlinskii）在含電荷回收的開關式驅動下還成不成立？** 這些模型多半在線性放大器驅動下建立；開關式驅動的高 dv/dt 與電荷回收路徑會改變電荷歷程，補償模型可能失效。本輪查無任何討論。
5. **儀器實際報價全部未取得。** 上表所有金額為量級估計，不可用於預算編列。

---

## 7. 來源清單

**注意**：S1–S3 為本輪 WebSearch 直接回傳（僅摘要，未開啟原文）；D1-xx / D2-xx 為轉引自本專案同目錄 dossier，URL 由該 dossier 提供，我**未親自驗證**。

### 本輪已檢索（S 系列）

| # | 標題 | URL | 說明 |
|---|---|---|---|
| S1a | Power-Efficient Driver Circuit for Piezo Electric Actuator with Passive Charge Recovery (Energies 13(11) 2866) | https://doi.org/10.3390/en13112866 | 被動電荷回收驅動電路；「兩二極體＋一電阻可回收約一半電荷」的主要出處候選 |
| S1b | 同上（Semantic Scholar 全文 PDF） | https://pdfs.semanticscholar.org/7dd3/b9c89dcc5905a57bd2d7d7ec447461c5cf58.pdf | S1a 的可下載全文 |
| S1c | Efficient charge recovery method for driving piezoelectric actuators with quasi-square waves | https://www.researchgate.net/publication/10801734_Efficient_charge_recovery_method_for_driving_piezoelectric_actuators_with_quasi-square_waves | 準方波電荷回收法的經典來源 |
| S1d | Charge-recovery circuit maximizes piezoelectric-actuator efficiency (EDN) | https://www.edn.com/charge-recovery-circuit-maximizes-piezoelectric-actuator-efficiency/ | 工程期刊版的電荷回收電路說明 |
| S1e | Design and control of a half-bridge converter to drive piezoelectric actuators | https://www.researchgate.net/publication/224331374_Design_and_control_of_a_half-bridge_converter_to_drive_piezoelectric_actuators | 半橋驅動壓電致動器的設計與控制 |
| S1f | Energy recovery power supply for piezoelectric actuator | https://www.academia.edu/127527810/Energy_recovery_power_supply_for_piezoelectric_actuator | 能量回收電源的另一份來源 |
| S1g | Power-Efficient Driver Circuit…（ResearchGate 版） | https://www.researchgate.net/publication/341936726_Power-Efficient_Driver_Circuit_for_Piezo_Electric_Actuator_with_Passive_Charge_Recovery | 同 S1a |
| S2 | CapDrive™ Piezo Driver — Boréas Technologies | https://www.boreas.ca/pages/capdrive-technology | CapDrive 從致動器內部負載電容回收能量並再利用的官方原理說明 |
| S3a | CapDrive® Ultra-Low Power Piezo Driver (BOS1931) | https://www.boreas.ca/products/capdrive%C2%AE-ultra-low-power-piezo-driver-bos1931 | BOS1931 產品頁 |
| S3b | CapDrive® Ultra-Low Power Piezo Driver (BOS1901) | https://www.boreas.ca/products/bos1901-piezo-haptic-driver | BOS1901 產品頁 |
| S3c | The 6 Elements of a Quality Piezo Driver (Boréas blog) | https://pages.boreas.ca/blog/piezo-haptics/6-most-important-elements-to-look-for-in-a-piezo-driver | 「能量回收可使壓電系統整體電流消耗降低最多 90%」的宣稱出處 |
| S3d | BOS1931 High-Efficiency Piezo Driver (Mouser) | https://www.mouser.com/new/boreas-technologies/boreas-bos1931-piezo-haptic-driver/ | 通路商產品頁，可用於後續詢價 |
| S3e | BOS1921 — CapDrive® Piezo Driver（EDOM 益登，台灣代理） | https://www.edomtech.com/en/product-detail/bos1921-capdrive-piezo-driver/ | **台灣取樣管道** |
| S3f | BOS1901 — Piezo Haptic Driver（EDOM 益登） | https://www.edomtech.com/en/product-detail/bos1901-piezo-haptic-driver/ | 同上 |
| S3g | Boréas Technologies' Piezo Driver Chip Advances Realistic Haptic Feedback in Automotive HMIs | https://www.globenewswire.com/news-release/2020/01/07/1967204/0/en/Bor%C3%A9as-Technologies-Piezo-Driver-Chip-Advances-Realistic-Haptic-Feedback-in-Automotive-HMIs.html | 車用 HMI 採用訊號 |
| S3h | Boréas Technologies 官網 | https://www.boreas.ca/ | 產品線總覽 |

### 轉引自本專案 dossier 01（D1 系列，URL 由該檔提供，未親自驗證）

| # | 標題 | URL | 本文用途 |
|---|---|---|---|
| D1-S1 | A Piezoelectric-Resonator-Based DC–DC Converter Demonstrating 1 kW/cm³ Resonator Power Density (IEEE TPEL) | https://ieeexplore.ieee.org/document/9931991 | 理論 98.2% vs 最高功率點實測 93.3% |
| D1-S3 | Piezoelectric Transformers: An Historical Review (Actuators, MDPI) | https://www.mdpi.com/2076-0825/5/2/12 | CCFL 產業崩解的失敗案例 |
| D1-S5 | Piezoelectric resonators in DC-DC converters: current status and limits (Power Electronics News) | https://www.powerelectronicsnews.com/piezoelectric-resonators-in-dc-dc-converters-current-status-and-limits/ | 雜模困擾低阻抗設計、散熱與節點支撐的架構矛盾 |
| D1-S7 | Loss mechanisms and high power piezoelectrics (J. Mater. Sci.) | https://link.springer.com/article/10.1007/s10853-005-7201-0 | Qm 每 0.1 m/s 退化 17%；共振/離共振發熱機制 |
| D1-S9 | Cold plasma from a single component (TDK Electronics) | https://www.tdk-electronics.tdk.com/en/373562/tech-library/articles/applications-cases/applications-cases/cold-plasma-from-a-single-component/1109546 | 12–24 Vpp 輸入 → 最高 20 kV：kV 級升壓由陶瓷體完成 |
| D1-S12 | Motional-Current-Sensing Method and Simplified Closed-Loop Control Strategy for PR-based DC-DC Converters (arXiv 2605.15279) | https://arxiv.org/pdf/2605.15279 | 本文推薦的頻率追蹤＋自感測解耦主線路線 |
| D1-S25 | CeraPlas Element — Piezoelectric Based Cold Plasma Generator (TDK 產品資料) | https://www.tdk-electronics.tdk.com/download/2307712/39eb3392c71d1191b103aa31c6a0f1c5/ceraplas-db.pdf | 52 kHz、8 W、12 Vpp、最高 20 kV 的具體規格 |
| D1-S28 | Thermal Degradation and Aging of High-Temperature Piezoelectrics | https://uknowledge.uky.edu/cgi/viewcontent.cgi?article=1568&context=gradschool_theses | 安全使用溫度約居里溫度一半（可靠性降額） |
| D1-S36 | Microwave-acoustic-based isolated gate driver for power electronics (arXiv 2511.13412) | https://arxiv.org/pdf/2511.13412 | Q≈1000 ⇒ 頻寬僅數十 kHz，不足驅動 WBG |
| D1-S38 | Overtone Piezoelectric Resonator For Power Conversion (UC Berkeley 技轉 NCD 33625) | https://techtransfer.universityofcalifornia.edu/NCD/33625.html | 泛音模態分離的可授權技術 |

### 轉引自本專案 dossier 02（D2 系列，URL 由該檔提供，未親自驗證）

| # | 標題 | URL | 本文用途 |
|---|---|---|---|
| D2-2 | An Overview of Piezoelectric Self-Sensing Actuation for Nanopositioning Applications (IEEE 8889413) | https://ieeexplore.ieee.org/document/8889413/ | 自感測電路分類（橋式／觀測器）＋電容漂移導致訊號污染與閉迴路不穩 |
| D2-3 | Physik Instrumente — Capacitive Sensors | https://www.physikinstrumente.com/en/expertise/technology/sensor-technologies/capacitive-sensors | **最強反面證據**：頂級奈米定位仍用外部電容式 direct metrology |
| D2-4 | Boréas BOS1901 Piezo Haptic Driver | https://www.boreas.ca/products/bos1901-piezo-haptic-driver | 「市場上唯一同時觸發觸覺並感測按壓力的壓電驅動 IC」 |
| D2-5 | Boréas CapDrive Technology | https://www.boreas.ca/pages/capdrive-technology | 比 LRA 省電 20×、比競品壓電 IC 省電 10× 的廠商宣稱 |
| D2-6 | Boréas 四通道整合感測驅動 IC 新聞稿（BOS0614, 2022） | https://www.prnewswire.com/news-releases/boreas-technologies-announces-four-channel-haptic-driver-with-integrated-sensing-301563047.html | 多通道整合感測的現貨選項 |
| D2-8 | TDK PowerHap Actuators | https://product.tdk.com/en/products/sw_piezo/haptic/powerhap/index.html | 致動器內建感測、≤25 N 壓力偵測 |
| D2-16 | A high-performance ultrasonic system for simultaneous data and power through solid metal barriers (IEEE UFFC 6396499) | https://ieeexplore.ieee.org/document/6396499/ | 功率＋資料同軸：17.37 Mbps + 50 W |
| D2-17 | US20150049587A1 — Full-duplex ultrasonic through-wall communication and power delivery with frequency tracking | https://patents.google.com/patent/US20150049587 | 全雙工＋頻率追蹤的專利路徑 |
| D2-28 | Synthetic impedance for implementation of piezoelectric shunt-damping circuits (Fleming & Moheimani) | https://www.researchgate.net/publication/3382744_Synthetic_impedance_for_implementation_of_piezoelectric_shunt-damping_circuits | DSP＋VCCS 合成任意 shunt 阻抗——「用主動電路合成被動元件」的電路實作原型 |
| D2-35 | Comparison of the Mason and KLM Equivalent Circuits (JPL/NASA) | https://ndeaa.jpl.nasa.gov/ndeaa-pub/USDC/Kk_1-comparison.pdf | Mason vs KLM 三端口模型對照 |
| D2-36 | Equivalent Circuits for Resonators and Transducers (DTIC ADA231520) | https://apps.dtic.mil/sti/tr/pdf/ADA231520.pdf | BVD／Mason 等效電路完整推導 |
| D2-37 | An Inductorless Bias-Flip Rectifier for Piezoelectric Energy Harvesting | https://www.repository.cam.ac.uk/bitstream/1810/266131/1/201609_SijunDU_revised.pdf | SSHC 80% 翻轉效率——無電感電荷操作的實測天花板 |
| D2-41 | Single Piezoelectric Transducer as Strain Sensor and Energy Harvester Using Time-Multiplexing (IEEE 7938680) | https://ieeexplore.ieee.org/document/7938680/ | 時間分割多工的既有實證 |
| D2-47 | High-Efficiency Isolated Piezoelectric Transformers for Magnetic-less DC-DC Power Conversion | https://www.researchgate.net/publication/391376205_High-Efficiency_Isolated_Piezoelectric_Transformers_for_Magnetic-less_DC-DC_Power_Conversion | 負載失配 → 損耗 +50%（該來源自註未一手驗證） |
| D2-48 | Microwave-acoustic-based isolated gate driver for power electronics (arXiv 2511.13412) | https://arxiv.org/pdf/2511.13412 | 同 D1-S36 |

### 未取得來源（誠實揭露的空白）

- TI DRV2667 / DRV8662 datasheet 與架構：**本輪查無**（搜尋預算用盡）。
- ST / Microchip 高壓壓電驅動 IC 與超音波 pulser 產品線：**本輪查無**。
- Class-E 驅動壓電變壓器的效率實測：**本輪查無**（僅有 dossier 01 轉引的 Stanford 97% @ 89 W）。
- PLL 頻率追蹤在壓電驅動上的具體實作論文：**本輪查無**。
- Preisach / Prandtl-Ishlinskii 遲滯補償殘差數字：**本輪查無**。
- Keysight E4990A 等儀器報價：**本輪查無**，文中金額全為未驗證量級估計。
- 「壓電主動/被動兩用元件」專用驅動 IC 或參考設計：**本輪查無任何一件**。
