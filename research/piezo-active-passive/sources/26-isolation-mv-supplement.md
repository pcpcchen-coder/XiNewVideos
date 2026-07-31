# 補查：隔離/穿壁的關鍵缺口與中壓應用的可行性邊界

> 一句話結論：**本輪 WebSearch 額度在本 agent 啟動前即已被 session 耗盡（200/200），無法執行任何新查詢**；因此本檔的價值不在新事實，而在三件事——**(1) 揪出前一輪的一個關鍵錯誤（Coilcraft「12 kV」是錯的，官方規格是 2800 Vrms / 4000 VDC，這件事已由 09 號 dossier 更正但 16 號未同步）**；**(2) 用第一原理把「聲程 vs 耐壓 vs 電容 vs 延遲 vs 功率」的標度律推導出來，得到一個對決策有殺傷力的結論：跨障壁耦合電容隨聲程只呈「對數」下降、傳播延遲卻隨聲程「線性」上升（≈256 ns/mm），而功率能力與耦合電容是「線性正比」的直接取捨**；**(3) 據此把壓電/聲學在隔離領域的真正立足窗口收斂到「≤300 mW、≥10 kV、極端 dv/dt 或極端環境（低溫/高溫/無磁）的浮動偏壓與遙測」，並判定「瓦級中壓閘驅偏壓電源」這個看似最誘人的題目其實是磁性方案的地盤。**

---

## 0. 研究方法與限制（誠實揭露）

**本輪實際執行的 WebSearch 次數：0 次（嘗試 3 次，全部被拒）。**

- 任務指示稱「WebSearch 可用且額度已放寬到 3000」，但本 agent 的第一次呼叫即回傳：
  `Web search was not performed: this session has used its web search budget (200 of 200 WebSearch calls).`
  連續三次不同 query 皆相同結果。額度為 **session 層級共用**，在本 agent 被 spawn 之前就已耗盡，本 agent 無法自行提高（`CLAUDE_CODE_MAX_WEB_SEARCHES_PER_SESSION` 於 session 啟動時決定）。
- WebFetch / curl 依指示未使用（環境已知 403）。
- **因此：任務清單中的第 1、3、4、5、6、7、8 項所要求的「新事實查證」，本輪全部無法執行。** 我不會用推測填補這些空格；下方一律標為【本輪無法查證】。
- 本檔實際做了什麼：
  1. **對既有 25 份 dossier 做全文交叉比對**（`grep` 檢索 Coilcraft / Würth / SST / MMC / 電外科 / ATEX / 乾儲罐 / SAW 隔離 / MRI 等關鍵詞），把散落各處、彼此矛盾的數字集中對帳。
  2. **第一原理推導**任務第 2 項所要求的標度律（共平面電容的保角映射解、SAW 群速度、聲學功率通量密度、位移電流），全部標示為【本文推導】並附假設。
  3. 把推導結果回頭套到中壓需求上，得出可否定/可肯定的結論。
- **本文件未出現任何我編造的專利號、論文標題、公司名、型號或實測數字。所有具名事實均轉引自本 repo 既有 dossier 並附原始 URL；所有新數字均為明確標示的推導。**
- 標註規則：`【查證】`＝原 dossier 標為已查證；`【轉引】`＝本輪未重驗，沿用既有 dossier；`【未驗證】`＝原 dossier 已標未驗證；`【本文推導】`＝我從物理/算術導出；`【本輪無法查證】`＝額度耗盡，完全沒查。

---

## 1. 結論摘要

1. **【最重要更正】16 號 dossier 的核心對照數字是錯的。** 16 號稱磁性方案已達「<1 pF / 5 W / **12 kV 連續**」，並據此在第 5 節寫下「磁性方案已經佔住低電容高地」。但 **09 號 dossier 已查證 Coilcraft `HTX7045C` 官方規格為「繞組間電容低至 0.7 pF、隔離 2800 Vrms / 4000 VDC（1 分鐘 hipot）」，明確指出「12 kV 查無佐證，請勿再引用」**［S3, S4］。**這把壓電/聲學的處境從「毫無空間」改寫為「在 >4 kV 的電壓帶，商用磁性方案其實還沒佔住 sub-pF 高地」——這是本補查最有商業意義的一條。**
2. **但學術磁性方案確實已打到中壓 sub-2 pF：1.03 pF @ 2.5 W，用於 13.8 kV / 100 kW 三相變流器**［S8］。所以正確的對手不是 Coilcraft，是這批 CPES/學術中壓 IAPS。壓電要有立足點，必須在**同一電壓等級**下贏它，而不是拿 2.75 kV 的數字去比。
3. **【本文推導・最關鍵】跨障壁耦合電容隨聲程只呈對數下降。** 以共平面電極的保角映射解，$C' \propto 1/(\ln 2 + \tfrac{1}{2}\ln(S/W))$。把聲程從 1.25 mm 拉到 20 mm（16 倍），耦合電容只下降約 **1.7 倍**（0.032 pF → ≈0.019 pF）。**這是壞消息也是好消息：壞在「拉長聲程買不到數量級的電容下降」，好在「為了耐壓而拉長聲程，幾乎不必付出電容代價」。**
4. **【本文推導・決定性】傳播延遲隨聲程線性上升，約 256 ns/mm。** LiNbO₃ 上 SAW 群速度約 3,488–3,980 m/s（128°Y-X ≈3,980、YZ ≈3,488），取 3,900 m/s。1.25 mm → **320 ns**；10 mm → **2.6 µs**；20 mm → **5.1 µs**。而商用隔離閘驅的傳輸延遲基準是 Infineon 1ED3124 的 **≈90 ns**［S12］。**結論：任何需要 >0.4 mm 聲程的聲學障壁，物理上不可能當作 PWM 訊號路徑用。中壓（10–20 kV）所需的 mm–cm 級聲程，只能做「電源/偏壓」或「慢速遙測」，絕不能做閘極訊號通道。** 這條推論同時把 16 號 dossier 機會 4.3 的定位從「隔離閘驅」修正為「隔離偏壓電源」。
5. **【本文推導・最有殺傷力】功率能力與耦合電容是線性正比的直接取捨，聲學方案在「W/pF」這個品質因數上並沒有跨越性優勢。** SAW 的功率上限由聲學功率通量密度 × 孔徑決定，$P \propto W_a$；跨障壁雜散電容也 $\propto W_a$。故 $C_{iso} \propto P$。以 150 mW / 0.032 pF 為基準外推：**0.5 W → 0.107 pF、1 W → 0.21 pF、2.5 W → 0.53 pF、5 W → 1.07 pF**。對照：Coilcraft `HTX7045C` 0.7 pF @ 2800 Vrms（功率 5 W 為 16 號轉引、本輪未驗證）＝ 7.1 W/pF；SAW ＝ 4.7 W/pF；學術中壓 IAPS 1.03 pF @ 2.5 W ＝ 2.4 W/pF。**在同一低電壓等級，商用磁性的 W/pF 已經比 SAW 好。0.032 pF 這個標題數字是「用功率換來的」，不是物理優勢。**
6. **【本文推導】但聲學在「電壓 vs 電容」這條軸上有磁性沒有的物理優勢。** 磁性變壓器要提高耐壓必須拉大繞組間距，這同時**劇烈劣化耦合係數 k**，所以磁性的 W/pF 從 2800 V 的 7.1 掉到 13.8 kV 的 2.4（劣化 3 倍）。聲學則是導波傳輸，拉長聲程只付「α·L 的傳播衰減」與「延遲」，孔徑（＝功率）完全不受影響，而電容只對數下降。**所以：電壓越高，聲學的相對優勢越大。這正是「非替代性窗口」的物理來源——不在 1200 V，在 ≥10 kV。**
7. **【本文推導・最大未知數】整條機會的生死繫於一個沒查到的數字：LiNbO₃ 在工作頻率下的 SAW 衰減係數 α（dB/mm）。** SAW 材料衰減隨 $f^2$ 上升。若要做 20 mm 聲程，論文所用的「微波頻段」必須降到 VHF（10–100 MHz 級）才可能把 α·L 控制在數 dB 內。降頻的代價是 IDT 孔徑與指叉尺寸放大 → 電容回升，且頻寬變窄。**「α(f) 與所需聲程的交點」是投入研發前必須先做的第一個實驗。**
8. **【本文推導・對電外科最有用】把跨障壁電容從 ~10 pF 壓到 0.03 pF，在電外科頻段可把高頻漏電流從數十 mA 降到亞 mA。** 電外科生成器典型工作於 300–500 kHz、輸出可達 kV 級。以 400 kHz / 3 kV 計，$I = 2\pi f C V$：10 pF → **75 mA**；1 pF → 7.5 mA；0.032 pF → **0.24 mA**。Ethicon 專利族（US9060776 等）明述「被動洩漏電容已不足以處理感應漏電流，必須做主動漏電流抵消」［S13］。**這是本領域唯一一個「痛點有名有姓、且數量級對得上」的醫療切入點。但注意：主 RF 功率路徑是 100–400 W，聲學做不到；能替代的只是控制/輔助電源與感測路徑。**
9. **20 年與 30 年的兩個失敗訊號必須放在同一頁看。** (a) **Avago（今 Broadcom）早在 2005 年前後就以 FBAR 做「跨隔離障壁的聲學傳訊」並取得 US7525398**（發明人 John D. Larson III 等），**20 年來未成為主流隔離器技術**［S10, S11］。(b) **穿金屬壁供電源自 1997 年 Connor 專利，2011 年 RPI 已做出媒體級成果，2015 年已有完整綜述，2026 年仍查無任何具名商用產品或 ATEX/IECEx 認證方案**［S15, S17］。**兩者合起來說明：這個領域的失敗模式不是「做不出來」，是「做出來也沒人買」。**
10. **【本輪無法查證，且是最大的剩餘風險】Berkeley Boles 團隊隔離式 PT 的隔離耐壓與一次/二次耦合電容，仍然查無。** 這是第二輪連續查無。既有資訊只有效率（峰值 97.6%、250 V→117 V/50 W 時 93.8%、損耗比降低 17×）與技轉案號頁 NCD 33842［S5, S6, S7］。**在拿到這個 pF 數字之前，「隔離式 PT 是否只是無磁版的磁性方案」無法判定。**

---

## 2. 現況 / 查證結果（逐項對帳）

### 2.1 任務第 1 項：Berkeley Boles 隔離式 PT 的耐壓與耦合電容
**【本輪無法查證】。** 既有證據（全部轉引，本輪未重驗）：
- 論文：Naval, Xu, Touhami, Boles，*High-Efficiency Isolated Piezoelectric Transformers for Magnetic-less DC-DC Power Conversion*, IEEE APEC 2025［S5］。
- 數字：250 V → 125 V、~100 W 功率級；徑向模寬範圍效率 >93%；250 V→117 V / 50 W 時 93.8%；峰值 97.6%；相較先前隔離式無磁 PT 設計損耗比降 17×［S5, S6］。15 號 dossier 另記載「峰值 98.3%、寬範圍 >97%、損耗比降低約 27×」——**與 16 號的 97.6% / 17× 不一致，本輪無法裁決哪個正確**（可能是同團隊不同版本論文）。
- UC Berkeley 技轉頁 NCD 33842 已將此列為可授權技術［S7］。
- **未取得：隔離耐壓（kV）、一次-二次耦合電容（pF）、CMTI、爬電距離、局部放電起始電壓。**
- **判讀：Boles 團隊的論文標題強調的是「效率」與「magnetic-less」，不是「低耦合電容」。若該團隊真做到 sub-pF，標題與摘要幾乎必然會寫。標題不寫，通常代表那不是賣點。這是一條弱的負面推論（【本文推導】，強度低，不可當結論）。**

### 2.2 任務第 2 項：聲程 vs 耐壓 vs 插入損失的定量標度律
**本輪核心產出，全部為【本文推導】。** 詳見第 3.2 節推導表與第 5 節的假設揭露。

### 2.3 任務第 3 項：2026 *Communications Engineering* SAW 隔離閘驅論文
**作者、機構、商業化動作【本輪無法查證】。** 既有資訊：
- 正式版 URL：`https://www.nature.com/articles/s44172-026-00681-w`；預印本 arXiv 2511.13412［S1, S2］。
- 數字（多份 dossier 一致轉引）：LiNbO₃ SAW、聲程 1.25 mm、隔離耐壓 2.75 kV、隔離電容 0.032 pF、開路 13.4 V、短路 44.4 mA、驅動 650 V/11 A GaN HEMT 導通時間 108.8 ns、工作溫度 0.5 K–544 K、已在 buck 轉換器驗證。
- **作者歸屬有內部矛盾**：16 號寫「Jin et al.」，07 號與 06 號皆未具名。**本輪無法裁決，建議下游文件在查證前不要引用作者名。**
- **是否有新創/技轉：【本輪無法查證】。**
- 該論文自陳的反面證據（多份 dossier 一致）：現有塊體 PT 工作頻率 <數十 MHz、機械 Q≈1000 ⇒ 固有頻寬僅數十 kHz，「不足以支援 WBG 功率電子」［S1, S2］。

### 2.4 任務第 4 項：中壓應用的實際規格需求
**SST / MMC 子模組 / 固態斷路器 / 800 V·1500 V 電動車與儲能的具名供應商規格：【本輪無法查證】（與 16 號同一缺口，連續兩輪未補上）。**
既有的唯一硬門檻（轉引）：**10 kV SiC MOSFET 的隔離供電需耐壓 >20 kV、輸入-輸出耦合電容 <2 pF**；已達成 1.03 pF（2.5 W）、2.34 pF、2.6 pF；PCB 無芯變壓器為 >10 kV RMS / 5.85 pF［S8, S9］。

**【本文推導】閘驅偏壓功率需求的參數式**：$P = Q_g \cdot \Delta V_{gs} \cdot f_{sw} + P_{quiescent}$。
以 $\Delta V_{gs}=25$ V（+20/−5）、$f_{sw}=10$ kHz（中壓典型）計：$Q_g=0.5\ \mu$C → 0.125 W；$Q_g=2\ \mu$C → 0.5 W；加上驅動 IC 與保護電路靜態功耗 0.2–0.5 W，**總需求落在 0.3–1 W**。
**（$Q_g$ 的實際值本輪查無，上式僅供框定量級。）**
把這個 0.3–1 W 套進第 1 節第 5 條的線性取捨：**聲學方案在此功率下的耦合電容會是 0.06–0.21 pF——仍比學術磁性最佳的 1.03 pF 好 5–17 倍。這是聲學在中壓唯一還站得住的數字，但前提是 α(f) 允許做出所需聲程（見 5.3）。**

### 2.5 任務第 5 項：磁性方案的極限
| 方案 | 繞組間/耦合電容 | 隔離耐壓 | 功率 | 來源 | 狀態 |
|---|---|---|---|---|---|
| Coilcraft `HTX7045C` | **低至 0.7 pF** | **2800 Vrms / 4000 VDC（1 min hipot）** | 5 W（轉引，未重驗） | S3, S4 | 【查證・已更正】 |
| Würth `WE-AGDT` | **低至 7 pF**，建議 <10 pF | 查無 | 查無 | S22, S23 | 【查證】 |
| 學術中壓 IAPS | **1.03 pF** | 13.8 kV / 100 kW 系統 | 2.5 W | S8 | 【轉引】 |
| 學術中壓 IAPS（其他） | 2.34 pF、2.6 pF | — | — | S8, S9 | 【轉引】 |
| PCB 無芯變壓器 | 5.85 pF | >10 kV RMS | 查無 | S8 | 【轉引】 |
| **Payton / Premo** | — | — | — | — | **【本輪無法查證】** |
| **所有上述之價格** | — | — | — | — | **【本輪無法查證】** |

**⚠️ 必須更正的錯誤**：16 號 dossier 第 1 節第 9 條、2.1 節表格、第 3 節數字表、第 5 節第 4 條，四處都寫「Coilcraft <1 pF / 5 W / **12 kV** 連續」，並據此下了「壓電沒有立足點」的結論。**該 12 kV 為錯誤資訊**［S3］。正確理解應為：**商用磁性在 ~3–4 kV 這個檔次做到 0.7 pF；一旦要上到 10 kV 以上，就只剩學術原型且電容退回 1 pF 級。** 這個修正把 16 號的悲觀結論放寬了一格。

### 2.6 任務第 6 項：穿金屬壁為何 30 年未商品化
**具體商業化嘗試與失敗個案、新創募資後倒閉的名單、ATEX/IECEx 認證難點的具體條文、EPRI/DOE/PNNL/Sandia 計畫的預算數字：全部【本輪無法查證】（連續兩輪未補上）。**
既有的間接證據：
- **仍有活躍的政府資金**：arXiv 2607.13797 由 **美國陸軍研究實驗室合作協議 W911NF2220007** 資助［S18］；PNNL 在全尺寸乏燃料罐 mock-up 做非侵入式超音波感測［S19］；Sandia/DOE CURIE 有乾儲罐液態水偵測感測器開發文件［S20］。
- **需求端論證仍成立**：乾式貯存桶「目前沒有任何內部感測系統」［S15］。
- **ATEX/IECEx**：24 號 dossier 查證結果為「**ATEX/IECEx 對壓電元件的能量門檻查無具體數值**，只確認走 ISO 80079-36:2016 的 ignition hazard assessment 路徑（非電氣設備），機械能轉成點火源時須做 IHA」［S24］。**這本身就是一個門檻訊號：沒有現成的判定基準，等於認證要從零談起。**
- **耦合劑可靠度**（轉引 16 號）：凝膠耦合劑乾涸、需反覆塗抹、殘留腐蝕；高溫下熱脫氣、先漂移後失效；Stevens Institute 2024 年的乾耦合可拆式發射端是最新對策［S21］。**實測壽命數據仍查無。**
- **對準容差**：文獻明言「中等程度的角度或橫向偏移即顯著劣化聲學耦合與效率」（轉引 16 號）。
- **穿壁數字內部矛盾（本輪發現）**：16 號寫「63.5 mm 鋼、50 W + 12.4 Mb/s」；07 號寫「6.3 cm 鋼、12.4 Mbps + **32.5 W AC**」，並另記「15 Mbps / 30 W」。**50 W 與 32.5 W 不一致，建議下游採保守的 32.5 W AC，並註明未收斂。**

### 2.7 任務第 7 項：電外科漏電流
**Ethicon/Medtronic 主動漏電流抵消的專利與其原因【轉引，本輪未重驗】**：US9060776 及同族（US11090104、RE47996、US9050093）明述隔離變壓器雜散電容把一次側電位耦合到二次側造成病人漏電流，被動洩漏電容不足以處理感應漏電流，故需主動抵消［S13］。IEC 60601-2-2（高頻電外科）本身為既有標準［S25］。
**壓電/聲學能否真正解決：見第 1 節第 8 條的推導。答案是「能解決控制/輔助路徑，不能解決主功率路徑」。**

### 2.8 任務第 8 項：井下與密封馬達（無穿線致動器）
**【本輪無法查證】——與 16 號同樣，連續兩輪完全未查。** 唯一相鄰資訊：18 號 dossier 的井下溫度分級（建造/測試 175 °C、DOE 系統合格 195 °C、Sandia dewarless 資料記錄器 300 °C、Thermochem 商用工具 400 °C）與 14 號的「Li-SOCl₂ 高溫特化型上限 +125 °C」［S26, S27, S28］。**這些界定了「電池活不下來」的溫度門檻（>125 °C），但沒有觸及「無穿線密封致動器」這個題目本身。**

---

## 3. 關鍵數字表

### 3.1 對帳表（含更正）
| 項目 | 數字 | 狀態 | 來源 |
|---|---|---|---|
| Coilcraft `HTX7045C` | 0.7 pF；**2800 Vrms / 4000 VDC**（**非 12 kV**） | 【查證・更正 16 號】 | S3, S4 |
| Würth `WE-AGDT` | 繞組間電容低至 7 pF，建議 <10 pF | 【查證】 | S22, S23 |
| 學術中壓 IAPS 最佳 | 1.03 pF @ 2.5 W，13.8 kV/100 kW | 【轉引】 | S8 |
| 10 kV SiC 閘驅電源門檻 | 耐壓 >20 kV、耦合電容 <2 pF | 【轉引】 | S8, S9 |
| PCB 無芯變壓器 | 5.85 pF @ >10 kV RMS | 【轉引】 | S8 |
| SAW 隔離閘驅 | 0.032 pF / 2.75 kV / 1.25 mm / 13.4 V / 44.4 mA / 0.5–544 K | 【轉引】 | S1, S2 |
| SAW 驅 GaN 導通 | 108.8 ns（650 V / 11 A GaN HEMT） | 【轉引】 | S1, S2 |
| 商用閘驅傳輸延遲基準 | Infineon 1ED3124 ≈90 ns，CMTI >200 kV/µs | 【轉引】 | S12 |
| 塊體 PT 頻寬上限 | Q≈1000、f<數十 MHz ⇒ 數十 kHz | 【轉引】 | S1, S2 |
| 穿壁最佳實測 | 6.3 cm 鋼：12.4 Mb/s ＋ **32.5 W AC**（另一版寫 50 W，**未收斂**） | 【轉引・矛盾】 | S15, S16, S17 |
| ATEX/IECEx 壓電能量門檻 | **查無具體數值**；走 ISO 80079-36:2016 IHA | 【查證・查無】 | S24 |
| Avago FBAR 聲學隔離專利 | US7525398（Avago Technologies General IP (Singapore)，John D. Larson III 等） | 【查證】 | S10, S11 |

### 3.2 標度律推導表（全部【本文推導】）

**(a) 耦合電容 vs 聲程 S**（共平面電極，保角映射；設電極特徵寬度 W = 0.1 mm）
$C' = \varepsilon_0\varepsilon_{eff}\,K(k')/K(k)$，$k=S/(S+2W)$；$S\gg W$ 時 $k'\approx2\sqrt{W/S}$、$K(k)\approx\ln 2+\tfrac12\ln(S/W)$、$K(k')\to\pi/2$。

| 聲程 S | 相對電容 | 由 0.032 pF 外推 |
|---|---|---|
| 1.25 mm（實測基準） | 1.00 | 0.032 pF |
| 5 mm | 0.74 | 0.024 pF |
| 10 mm | 0.65 | 0.021 pF |
| 20 mm | 0.585 | 0.019 pF |
| 40 mm | 0.53 | 0.017 pF |

→ **32 倍聲程只換到 1.9 倍電容下降。電容對聲程幾乎不敏感。**

**(b) 耐壓 vs 聲程**
實測點：2.75 kV / 1.25 mm ＝ **2.2 kV/mm**。
- 線性外推（樂觀，需完整封裝）：10 kV → **4.5 mm**；20 kV → **9.1 mm**。
- 依 IEC 60664 級爬電設計慣例（悲觀，約 2–2.5 mm/kV，空氣、污染度 2）：10 kV → **20–25 mm**；20 kV → **40–50 mm**。
- **警語：2.2 kV/mm 比一般爬電規範激進約 4–5 倍，強烈暗示該 2.75 kV 是實驗室短時 hipot，不是可通過安規認證的爬電距離。實際設計聲程應以悲觀值為準。**

**(c) 傳播延遲 vs 聲程**（$v_{SAW}$ ≈ 3,900 m/s，LiNbO₃）

| 聲程 | 單向延遲 |
|---|---|
| 0.4 mm | ≈100 ns（＝商用閘驅延遲預算上限） |
| 1.25 mm | 320 ns |
| 4.5 mm | 1.15 µs |
| 10 mm | 2.6 µs |
| 20 mm | 5.1 µs |
| 50 mm | 12.8 µs |

→ **≈256 ns/mm。中壓所需聲程 ⇒ µs 級延遲 ⇒ 只能做電源，不能做訊號。**

**(d) 功率 vs 電容（線性取捨）**：$P\propto W_a$，$C_{iso}\propto W_a$ ⇒ $C_{iso}\propto P$（同頻率、同聲程）

| 目標功率 | 外推耦合電容 | 對照 |
|---|---|---|
| 0.15 W（實測基準） | 0.032 pF | — |
| 0.5 W | 0.107 pF | |
| 1 W | 0.21 pF | vs 學術磁性 1.03 pF @ 2.5 W |
| 2.5 W | 0.53 pF | **仍優於 1.03 pF，但只剩 2 倍** |
| 5 W | 1.07 pF | **與磁性打平，優勢消失** |

**W/pF 品質因數對照**：SAW **4.7**（@2.75 kV）；Coilcraft **7.1**（@2800 Vrms，功率為轉引未驗證）；學術中壓磁性 **2.4**（@13.8 kV）。
→ **同電壓等級下聲學不佔便宜；優勢只在高電壓等級出現，因為磁性的 W/pF 隨耐壓劣化，聲學的不會。**

**(e) 位移電流**（$I = C\,dv/dt$，@100 kV/µs）：10 pF → 1 A；1 pF → 100 mA；0.21 pF → **21 mA**；0.032 pF → 3.2 mA。
**(f) 電外科漏電流**（$I=2\pi fCV$，@400 kHz / 3 kV）：10 pF → 75 mA；1 pF → 7.5 mA；0.032 pF → **0.24 mA**。

---

## 4. 「新能力型」機會（本輪修正版）

### 4.1 ★★★★☆ ≥10 kV 中壓開關的「超低耦合電容浮動偏壓電源」（**非閘極訊號路徑**）
- **新能力**：在 ≥10 kV 隔離耐壓下，同時提供 **0.3–1 W** 與 **<0.25 pF** 耦合電容。目前最佳磁性方案在該電壓帶是 1.03 pF @ 2.5 W。
- **為何以前做不到**：磁性變壓器提高耐壓必須拉大繞組間距，直接劣化耦合係數，功率與耐壓是硬衝突；聲學導波的孔徑（功率）與聲程（耐壓）在物理上解耦【本文推導】。
- **是否真非替代**：**半新能力**。功能上仍是「隔離電源」（磁性也能做），但把 pF 壓低一個數量級後，才可能把串聯堆疊層數與 dv/dt 上限推開——**在單顆 1200 V 開關上完全沒價值，在 SST/MMC 串聯堆疊上才有**。
- **重大修正**：16 號把此機會寫成「隔離閘驅」。依 3.2(c)，**µs 級延遲使其不可能承載閘極訊號**。正確定位是「偏壓電源 ＋ 慢速狀態遙測」，訊號路徑仍需另用光耦或電容耦。
- **誰在做**：**查無任何人在做「≥10 kV 的聲學隔離電源」。** SAW 論文停在 2.75 kV；Boles 團隊的 pF 數字未知。
- **TRL**：2–3（原理清楚、無任何中壓原型）。
- **技術難點**：α(f) vs 聲程的交點（見 5.3）；20 kV 級的局部放電與封裝；聲程 10–50 mm 的機械封裝與熱應力。

### 4.2 ★★★★☆ 電外科/高頻醫療生成器的「fF 級障壁」控制與感測路徑
- **新能力**：把控制側與病人側之間的高頻漏電流從 mA 級降到亞 mA 級，可能省掉整套主動漏電流抵消電路［S13 ＋ 3.2(f) 推導］。
- **是否真非替代**：**半新能力**。廠商目前已用主動抵消「解決」了，所以不是「以前做不到」，是「以前要用一整塊類比電路才做得到」。屬於 BOM/複雜度替代，但痛點具名、數量級對得上。
- **限制**：主 RF 功率（100–400 W）聲學做不到，只能處理輔助路徑。

### 4.3 ★★★★★ 穿實心金屬壁的功率＋資料（維持 16 號評級，但加上警語）
- 需求端論證仍是教科書級（法拉第籠、乾儲罐無任何內部感測）［S15］，軍方資金仍在（W911NF2220007）［S18］。
- **但 30 年零商品化是硬事實，且本輪仍未找到任何具體失敗個案或已倒閉的新創。「找不到失敗案例」不等於「沒有失敗」，更可能是「從沒有人認真嘗試商業化」——後者對投入決策反而是更差的訊號（代表市場方沒有付費意願）。**

### 4.4 ★★★☆☆ 極端環境（0.5 K / 271 °C / 強磁場）的隔離供電
- 維持 16 號評級。SAW 實測 0.5 K–544 K［S1, S2］；MRI 側已有無芯變壓器專利佈局（US11777487 / US12206394）與光隔離只能傳訊號不能傳功率的專利佐證（US11796613）［S14］。
- **限制**：PZT 居里點撐不到 544 K，必須走 LiNbO₃/AlN/鑭鎵矽酸鹽——與台灣既有 PZT 產線無共通性（轉引 18 號：LiNbO₃ 在 400 °C 只有 10 天壽命）。

### 4.5 ✗ 已排除：1200 V 級 SiC/GaN 的隔離閘驅
- 維持 16 號結論並補強：現在有了 3.2(c) 的延遲推導與 3.2(d) 的 W/pF 對照，**兩者都獨立指向「打不過」**。理由與客戶排除「取代電感」同構。

---

## 5. 反面證據、失敗案例與物理上限

1. **【本輪最強反面證據】W/pF 品質因數顯示 0.032 pF 是「用功率換來的」。** 在 ~3 kV 檔次，商用磁性的 7.1 W/pF 已優於 SAW 的 4.7 W/pF。若客戶被 0.032 pF 這個標題數字吸引而忽略功率只有 150 mW，會做出錯誤判斷。【本文推導】
2. **【本輪第二強】µs 級傳播延遲把「聲學隔離閘驅」這個名字本身否定掉。** 中壓所需的 mm–cm 聲程對應 1–13 µs 延遲，比商用閘驅的 90 ns 慢 1–2 個數量級。【本文推導】
3. **α(f) 是尚未量化的物理天花板。** SAW 材料衰減 $\propto f^2$。論文走微波頻段是因為聲程只有 1.25 mm；要做 10–50 mm 就必須大幅降頻，而降頻放大 IDT 尺寸 → 電容回升、頻寬變窄。**「低電容、高耐壓、大功率、寬頻寬」四者中至少有兩者互斥，這不是工程問題。**【本文推導】
4. **Avago/Broadcom 用 FBAR 做聲學隔離已有 20 年（US7525398），從未成為主流。** 一家有 FBAR 世界級量產能力、且本身就在賣隔離器的公司都沒把它做起來——這比任何學術數字都更有說服力。［S10, S11］
5. **穿金屬壁 30 年零商品化，且本輪仍找不到任何具體的商業化嘗試紀錄。** ［S15, S17］
6. **ATEX/IECEx 對壓電元件沒有現成的能量判定門檻**，必須走 ISO 80079-36 的個案式點火危害評估——認證路徑不確定性極高，時程與成本都無法事前估算。［S24］
7. **耦合劑仍是穿壁部署的第一號殺手**（乾涸、需重塗、殘留腐蝕、高溫脫氣導致先漂移後失效），且對準容差敏感（中等偏移即顯著劣化）。實測壽命數據**至今查無**。［S21］
8. **塊體 PT 的頻寬（數十 kHz）由推進聲學路線的那篇論文自己判死刑**，且 PT 的電容性負載反而讓驅動電路需要更大的電感——**這直接削弱「壓電可以消滅電感」的核心賣點**。［S1, S2］
9. **PT 產業曾經完整崩潰一次**（CCFL 背光 → LED 轉換後主要供應商停止高量生產），供應鏈與量產經驗已流失，重建成本必須計入。（轉引 16 號）
10. **本 dossier 自身的最大缺陷**：0 次新查詢。上述所有具名事實都是二手轉引，**若前輪 dossier 有錯（本輪已抓到至少一個：Coilcraft 12 kV），本輪會繼承**。所有推導的輸入參數（1.25 mm、0.032 pF、150 mW）若有誤，結論全數失效。

---

## 6. 未解問題

1. **【最高優先・連續兩輪查無】Berkeley Boles 隔離式 PT 的隔離耐壓與一次/二次耦合電容是多少 pF？** 若 ≥1 pF，該路線只是「無磁」，不是「低電容」；若 <0.1 pF，整個中壓機會的 TRL 立刻從 2–3 跳到 4。查法：IEEE Xplore 論文全文（S5 的 PDF 連結）、UC Berkeley 技轉頁 NCD 33842（S7）。**另需裁決 15 號（98.3% / 27×）與 16 號（97.6% / 17×）的效率數字矛盾。**
2. **【最高優先・可自己做實驗回答】LiNbO₃（或 AlN、鑭鎵矽酸鹽）在 10 MHz–1 GHz 的 SAW 衰減係數 α(f)（dB/mm）是多少？** 這是唯一能判定「10–50 mm 聲程是否物理可行」的參數。**建議這是投入研發前的第一個實驗，成本低、答案二元。**
3. **2.75 kV 是短時 hipot 還是可認證的持續耐壓？爬電/局放（PDIV）數據為何？** 若只是短時 hipot，3.2(b) 的悲觀外推（20 kV 需 40–50 mm）就是實際值，配合 3.2(c) 的 12.8 µs 延遲，機會 4.1 的封裝尺寸會大到失去吸引力。
4. **穿金屬壁 30 年零商品化，究竟有沒有人真的嘗試過？** 本輪與前輪都找不到失敗個案。**必須分辨「試過且失敗」與「從沒人試」——後者代表市場方零付費意願，是更致命的訊號。** 建議查向：核電廠/船級社的實際部署案例、NRC 對非侵入式感測的認證要求、是否有新創募資後倒閉。
5. **（連續兩輪完全未查）井下/密封無穿線馬達與致動器；SST/MMC 子模組輔助電源、固態斷路器、800 V/1500 V 電動車與儲能的具名隔離電源規格與供應商。**
6. **Coilcraft `HTX7045C` 的 5 W 功率規格是否屬實、實際售價多少？** 這決定 W/pF 對照表的分子，是本檔第 1 節第 5 條結論的關鍵輸入，目前仍為 16 號轉引的未驗證值。

---

## 7. 來源清單

> **本節所有 URL 均轉引自本 repo 既有 dossier（編號後標明出處檔案），本輪未重新存取任何一個。**

1. **S1** — Microwave-acoustic-based isolated gate driver for power electronics（arXiv 預印本）— https://arxiv.org/pdf/2511.13412 — SAW 隔離閘驅 0.032 pF / 2.75 kV / 1.25 mm / 0.5–544 K，並自陳塊體 PT 頻寬僅數十 kHz。〔轉引 16、07、06、03、18〕
2. **S2** — Microwave-acoustic-based isolated gate driver for power electronics, *Communications Engineering*（2026）— https://www.nature.com/articles/s44172-026-00681-w — 同上正式期刊版。〔轉引 07、06、16〕
3. **S3** — Coilcraft `HTX7045C` 產品頁 — https://www.coilcraft.com/en-us/products/transformers/power-transformers/power-converter-transformers/htx7045c/ — **繞組間電容低至 0.7 pF、隔離 2800 Vrms / 4000 VDC（1 min hipot）；更正 16 號「12 kV」之誤。**〔轉引 09〕
4. **S4** — Coilcraft `HTX7045` 閘驅變壓器系列頁 — https://www.coilcraft.com/en-us/products/transformers/power-transformers/gate-drive/htx7045/ 〔轉引 09〕
5. **S5** — High-Efficiency Isolated Piezoelectric Transformers for Magnetic-less DC-DC Power Conversion, IEEE APEC 2025（Naval, Xu, Touhami, Boles）— https://ieeexplore.ieee.org/iel8/10977026/10977027/10977397.pdf — **本輪仍未取得 pF 與耐壓。**〔轉引 16〕
6. **S6** — 同上 ResearchGate 條目 — https://www.researchgate.net/publication/391376205_High-Efficiency_Isolated_Piezoelectric_Transformers_for_Magnetic-less_DC-DC_Power_Conversion — 97.6% 峰值、17× 損耗降低。〔轉引 16〕
7. **S7** — UC Berkeley 技轉 NCD 33842「Piezoelectric Transformers For Power Conversion」— https://techtransfer.universityofcalifornia.edu/NCD/33842.html 〔轉引 16〕
8. **S8** — CPES (Virginia Tech) — Power Supply with Low Input-Output Capacitance for Multiple Gate Driver Units of a 10 kV SiC-MOSFET Module — https://cpes.vt.edu/library/viewnugget/760 — 1.03 pF @ 2.5 W；10 pF@100 kV/µs → 1 A。〔轉引 16〕
9. **S9** — Design Considerations for High-Voltage-Insulated Gate Drive Power Supply for 10-kV SiC MOSFET — https://www.researchgate.net/publication/341909986_Design_Considerations_for_High-Voltage-Insulated_Gate_Drive_Power_Supply_for_10-kV_SiC_MOSFET_Applied_in_Medium-Voltage_Converter — >20 kV 耐壓、<2 pF 門檻。〔轉引 16〕
10. **S10** — US7525398「Acoustically communicating data signals across an electrical isolation barrier」— https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/7525398 — Avago Technologies General IP (Singapore)，John D. Larson III 等；**聲學隔離 20 年未起飛的直接證據。**〔轉引 07〕
11. **S11** — 同族 WO2007047701A2 — https://patents.google.com/patent/WO2007047701A2/en 〔轉引 07〕
12. **S12** — Infineon — Common mode transient immunity (CMTI) in gate drivers — https://community.infineon.com/t5/Knowledge-Base-Articles/Common-mode-transient-immunity-CMTI-in-gate-drivers/ta-p/1114529 — 1ED3124 傳輸延遲 ≈90 ns、CMTI >200 kV/µs；本文延遲推導的對照基準。〔轉引 16〕
13. **S13** — US9060776「Surgical generator for ultrasonic and electrosurgical devices」— https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/9060776 — 雜散電容造成病人漏電流、被動洩漏電容不足、需主動抵消（同族 US11090104、RE47996、US9050093）。〔轉引 16〕
14. **S14** — US11796613 / US12130345「Opto-isolator circuitry for MRI applications」— https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/11796613 — **訊號可光隔離、功率不行**，此即缺口所在。〔轉引 15〕
15. **S15** — Self-powered Through-wall Communication for Dry Cask Storage Monitoring, *Annals of Nuclear Energy* — https://www.sciencedirect.com/science/article/abs/pii/S0306454922003413 — 乾儲罐「目前無任何內部感測系統」。〔轉引 16、14〕
16. **S16** — Through-Metal-Wall Power Delivery and Data Transmission for Enclosed Sensors: A Review, *Sensors* 2015 — https://www.mdpi.com/1424-8220/15/12/29870 — 本領域標準綜述。〔轉引 16〕
17. **S17** — RPI News — Student Innovation Transmits Data and Power Wirelessly Through Submarine Hulls — https://news.rpi.edu/luwakkey/2836 — 穿 2.5 吋鋼；**功率數字與 07 號的 32.5 W AC 不一致，未收斂。**〔轉引 16〕
18. **S18** — Experimental Characterization and Prediction of Radial and Thickness Mode Power Transfer Capability in Through-Metal Acoustic Power Transfer（arXiv）— https://arxiv.org/html/2607.13797 — 美國陸軍研究實驗室合作協議 **W911NF2220007** 資助。〔轉引 16〕
19. **S19** — PNNL — Non-invasive ultrasonic sensing of internal conditions on a partial full-scale spent nuclear fuel canister mock-up — https://www.pnnl.gov/publications/non-invasive-ultrasonic-sensing-internal-conditions-partial-full-scale-spent-nuclear 〔轉引 16〕
20. **S20** — CURIE/Sandia — Sensor Development for Liquid Water Detection in Dry Storage Casks (FY19 Status) — https://curie.pnnl.gov/sites/default/files/sandiadocs/M3SF-19PN010201034-Sensor-Development-for-Liquid-Water-Detection-in-Dry-Storage-Casks-FY19-Status.pdf 〔轉引 16〕
21. **S21** — Portable through-metal ultrasonic power transfer using a dry-coupled detachable transmitter, *Ultrasonics* 2024（Stevens Institute）— https://www.sciencedirect.com/science/article/abs/pii/S0041624X2400101X — 針對耦合劑問題的乾耦合解法。〔轉引 16〕
22. **S22** — Würth Elektronik `WE-AGDT` Auxiliary Gate Drive Transformer — https://www.we-online.com/en/components/products/WE-AGDT — 繞組間電容低至 7 pF、建議 <10 pF。〔轉引 07〕
23. **S23** — Würth 應用手冊 — https://www.we-online.com/files/pdf1/rd001d-v1.pdf — SiC 100 kV/µs × 10 pF ≈ 1 A。〔轉引 07〕
24. **S24** — IEC 60601-2-2:2017（高頻電外科）— https://webstore.iec.ch/en/publication/28118 — 24 號 dossier 另查證 ATEX/IECEx 對壓電無具體能量門檻、走 ISO 80079-36:2016 IHA。〔轉引 24〕
25. **S25** — Advanced Energy — Safety Requirements in Medical Equipment: BF and CF — https://www.advancedenergy.com/en-us/about/news/blog/safety-requirements-in-medical-equipment-designing-for-bf-and-cf-classifications/ — CF <10 µA。〔轉引 16〕
26. **S26** — Dewarless Logging Tool – 1st Generation（Sandia, OSTI）— https://www.osti.gov/servlets/purl/763144 — 300 °C 井下資料記錄器。〔轉引 18〕
27. **S27** — Downhole Electronic Components: Achieving Performance Reliability — https://www.researchgate.net/publication/276346165_Downhole_Electronic_Components_Achieving_Performance_Reliability — 5 年 @225 °C；MTBF 250,000 h 對含動件系統不切實際。〔轉引 18〕
28. **S28** — US11415555「Ultrasonic through-wall sensors」— https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/11415555 〔轉引 16〕
29. **S29** — Piezoelectric Transformers: An Historical Review, *Actuators* 2016 — https://www.mdpi.com/2076-0825/5/2/12 — CCFL→LED 導致高壓 PT 商業崩潰史。〔轉引 16〕
30. **S30** — US11777487 / US12206394「Gate driver coreless transformers for magnetic resonance imaging power electronics」— https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/11777487 — MRI 無磁閘驅的產業需求佐證。〔轉引 16〕
