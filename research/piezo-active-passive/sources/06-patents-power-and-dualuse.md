# 專利地景一：壓電功率轉換與「主動/被動兩用」元件

> 一句話結論：**壓電功率轉換的「地基專利」已經在 2021–2022 年被 MIT（Perreault / Lang / Boles）用兩層 claim 圈死——一層是「PR 幾何條件 vs 電壓/功率等級」（US12126324B2），一層是「以 PR 為唯一儲能元件的多階段開關序列＋resonant soft-charging」——保護期到 2041–2042；而唯一在做量產佈局的公司是 Enphase Energy（US12268094，trajectory control）與 TDK（CeraPlas 冷電漿）。**真正的專利空白區不在「壓電做電感」（那條路正好是客戶排除的替代路線、也正好是專利最密的地方），而在「同一顆壓電體在同一系統中分時扮演功率通道＋隔離屏障＋感測器＋故障診斷器」這種**系統級複用 claim**，以及「壓電做主動電感」的反向命題（Cirrus Logic 已用 US12396367B2 佔住「用矽電路模擬電感去驅動壓電」，反方向仍空著）。

---

## 0. 研究方法與限制（誠實揭露）

- **實際執行 32 次 WebSearch**（本文件所有事實均出自這 32 次搜尋回傳的原文摘錄）。第 33–36 次查詢時本 session 的 WebSearch 額度（200 次／session，與同批其他子代理共用）用罄，被系統擋下，因此**下列題目沒查到，屬於已知缺口**（見第 6 節）。
- **WebFetch 在本環境被 egress policy 全面封鎖**（任何 URL 回 403），故**無法抓取任何一手專利全文**。這造成三個結構性限制：
  1. **無法查證任何一件專利的法律狀態**（有效／失效／年費未繳／到期）。Google Patents 的 "Status" 欄位抓不到。本文所有「到期年」都是**依據申請日／優先權日 +20 年推算**，非實查。
  2. **無法取得任何一件專利的 IPC/CPC 分類碼**。僅能確認分類體系本身存在（H02M＝AC/DC/DC-DC 轉換、H02N2/18＝壓電/電致伸縮/磁致伸縮之機械輸入電輸出電機、H10N30/30＝機械輸入電輸出之壓電/電致伸縮裝置），來源為 USPTO CPC scheme 頁面搜尋摘要。**分類熱區的統計數字查無。**
  3. **無法取得專利的 claim 全文**，故「claim 覆蓋範圍」的判斷是根據搜尋摘要中的 abstract 文字推論，屬於**推論而非結論**。
- **兩件本任務指定要查證的專利號，只取得間接佐證。** `US 12,009,746` 與 `US 12,388,364` 在多次搜尋中**都沒有回傳可點的 Google Patents / Justia 專利頁連結**；搜尋引擎確實回傳了與該號碼對應的 abstract 文字（內容為「DC-DC 轉換器，含複數開關、作為功率級儲能的壓電諧振器（PR）、以及控制開關序列的手段，開關依序列動作將能量由輸入經 PR 傳至輸出，同時提供 PR 電容的低損耗 resonant soft-charging，序列含 connected stages 與 open stages」），且該文字與 Justia 的 Jessica Boles 發明人頁面關聯出現。**結論：號碼與內容高度可能正確，但無一手連結佐證，標記為「半驗證」。**
- **明確查無**：Murata / TDK / Kyocera / Taiyo Yuden 在 2020 年以後的壓電功率轉換專利申請（只查到 Murata 2000 年的 US6184631B1 壓電逆變器）；壓電功率轉換／能量擷取領域的 NPE（專利蟑螂）訴訟紀錄；任何專利分類的申請量統計數字。

---

## 1. 結論摘要

1. **MIT 是這個領域的地基專利權人，優先權日 2021-05-07，保護到 ~2041–2042。** `US12126324B2`「Piezoelectric resonators for power conversion」發明人 David J. Perreault、Jeffrey H. Lang、Jessica Boles、Joseph Bonavia，受讓人 Massachusetts Institute of Technology（讓與登記 2023-11-06），為 PCT/US2022/028043（2022-05-06 申請）之美國國家階段，主張美國臨時案 63/185,663（2021-05-07）優先權。其 claim 標的是「**PR 之幾何條件，且該條件以轉換器指定的電壓與功率等級來定義**」——這是一個非常上游的 claim，等於把「怎麼設計這顆陶瓷」圈起來。（[Google Patents US12126324](https://patents.google.com/patent/US12126324/en)）

2. **第二層是拓樸/控制層：`US12,009,746` 與 `US12,388,364`（半驗證）**，claim 標的為「以 PR 作為功率級儲能元件、含 connected/open stages 的開關序列、達成 PR 電容的 resonant soft-charging」。這一層直接對應 Boles 論文中的 six-stage / seven-stage 開關序列。**任何人做 PR-based DC-DC，繞不開這兩層。** 這是客戶排除「直接取代電感」路線之外的第二個理由：**那條路的專利地不但貴，而且已經被佔了。**

3. **唯一大規模出貨的公司玩家是 Enphase Energy。** `US12268094`「Piezoelectric power converter with trajectory control」，受讓人 Enphase Energy, Inc.，發明人 Michael J. Harrison；架構為「輸入橋 + 壓電變壓器 + 輸出橋 + trajectory controller」，控制器取樣輸入/輸出橋的電壓/電流與流經 PT 的電流來最佳化開關。Enphase 是微逆變器年出貨數百萬台的公司，**它在壓電功率轉換的控制層佈局，是這個題目最強的商業訊號之一**。（[USPTO US12268094](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/12268094)、[Justia: Patents Assigned to Enphase Energy](https://patents.justia.com/assignee/enphase-energy-inc)）同一發明脈絡的較早件為 `US9871182B2`「Frequency tracking piezoelectric transformer power converter with simultaneous two-parameter control」（2018-01-16 核准，家族含 WO2014145587A1，2014 申請）——**受讓人未驗證**。（[Google Patents US9871182B2](https://patents.google.com/patent/US9871182B2/en)）

4. **UC Berkeley（Boles Lab）是第二個佈局中心，且已經公開掛牌授權，代表有未公開的在審申請案。** UC 技轉網站上有三件明確標的：`33842 Piezoelectric Transformers For Power Conversion`（宣稱較先前隔離式無磁性 PT-based DC-DC 設計**損耗比降低 17 倍**、峰值效率 **97.5%**）、`33625 Overtone Piezoelectric Resonator For Power Conversion`（泛音模態 PR，效率與基頻相當但功率密度更高、最佳負載阻抗更低，適用 DC-DC / DC-AC / AC-DC / active inductor）、`33585 Active Inductor Based On A Piezoelectric Resonator`（明確定位為磁性電感的 **drag-and-drop replacement**）。**專利號未公開**（技轉掛牌通常對應未公開或剛公開的申請案）。（[UC 33842](https://techtransfer.universityofcalifornia.edu/NCD/33842.html)、[UC 33625](https://techtransfer.universityofcalifornia.edu/NCD/33625.html)、[UC 33585](https://techtransfer.universityofcalifornia.edu/NCD/33585.html)）

5. **1990s 的第一波專利（NEC / Matsushita / Murata / Philips）已經全部逾 20 年，技術上已進入公有領域，但那波技術的市場也一起死了。** 代表件：`US5329200`「Piezoelectric transformer converter for power use」(1994)、`US5768111A`（1998，轉換器含 PT 且開關級共振頻率與變壓器不同）、`US5969954A` AC/DC converter with a piezoelectric transformer（NEC，1998-01-15）、`US6535407` DC/DC converter having a piezoelectric transformer and rectification-smoothing circuit（NEC，發明人 Toshiyuki Zaitsu，1998-07-28 申請、2003-03-18 核准）、`EP1050954A4` Drive circuit for piezoelectric transformer（Matsushita，1999-10-19）、`JP2002064977A`（Matsushita，2000-08-21）、`US6184631B1` Piezoelectric inverter（Murata Manufacturing，2000-03-16 申請）。**推算全部已於 2018–2021 年前後到期**（未實查法律狀態）。

6. **Rosen 原始專利早已公有領域，但號碼與日期在公開資料上互相矛盾，必須小心引用。** 搜尋摘要同時給出：概念首見於 `US2,830,274`（1954 年由 Rosen、K. Fish、H. C. Rothenberg 提出申請）；`US2,975,354`「Electrical Conversion Apparatus」被描述為「1956-11-30 核准」，但同一段又說「`US2,974,296` 於 1961-03 核准、`US2,975,354` 於 1961-03 核准」。**這是明顯的內部矛盾，本文不採信任何一個確切日期，只採信「Rosen 型 PT 概念約 1954–1961 年間成案、現已完全公有領域」。**（[MDPI Actuators 5(2)12, Piezoelectric Transformers: An Historical Review](https://www.mdpi.com/2076-0825/5/2/12)）

7. **「主動/被動兩用」在專利上是**兩個互不相通的島**：功率轉換島（H02M 系）與 self-sensing 致動器島（H02N/H10N 系），中間幾乎沒有橋。** self-sensing 側查到的代表件為 `US10349818` / `US9872606`「Adaptive control of a fiber scanner with piezoelectric sensing」（明確 claim「致動與感測同時或近似同時發生，感測電路在驅動電路施加驅動訊號時量測位移訊號」，並使用**自感測電容橋**把位移訊號從驅動訊號中分離；**受讓人未驗證**）與 `CN111060232B`「壓電致動器輸出力自感知方法」。**這兩座島之間沒有共同的專利權人**——這正是白空間所在。（[USPTO US10349818](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/10349818)、[Google Patents CN111060232B](https://patents.google.com/patent/CN111060232B/en)）

8. **有一件公司專利直接踩在「壓電＋電感模擬」的邊界上，但方向是反的：Cirrus Logic `US12396367B2`「Driver circuitry comprising active inductor circuitry for piezoelectric transducers」（受讓人 Cirrus Logic International Semiconductor Ltd / Cirrus Logic Inc）——用矽的主動電感電路去驅動壓電換能器（觸覺應用）。** Berkeley 的 33585 是**用壓電做電感給矽用**，恰為反命題。這代表：(a) 大型 audio/haptics IC 廠已經在意壓電負載的電感需求；(b) 反方向（壓電當電感）尚未被公司佔位。（[Google Patents US12396367](https://patents.google.com/patent/US12396367)）

---

## 2. 現況：技術 / 產品 / 玩家

### 2.1 學研側（專利地基持有者）

| 機構 | 佈局重點 | 代表件 | 狀態 |
|---|---|---|---|
| **MIT（Perreault / Lang / Boles / Bonavia）** | ①PR 幾何設計條件（材料/形狀 vs 電壓功率等級）②開關序列＋soft-charging 拓樸 | US12126324B2；US12,009,746（半驗證）；US12,388,364（半驗證） | 優先權 2021-05-07；推算 2041–2042 到期 |
| **UC Berkeley（Boles Lab）** | ①隔離式 PT-based DC-DC ②泛音（overtone）PR ③壓電做 active inductor | UC 技轉 33842 / 33625 / 33585，**專利號未公開** | 掛牌授權中 |
| **DTU（Michael A. E. Andersen）＋ Noliac A/S ＋ Danfoss PolyPower** | 無電感（inductorless）與**雙向** PT-based 轉換器；驅動介電彈性體致動器的微型高壓電源 | 未查到專利號（僅查到 PhD 論文與 DTU Orbit 出版品） | 專利佈局**查無** |

MIT 那一支的性能基準（用來判斷「地基專利值不值錢」）：PR 功率處理密度 **1.01 kW/cm³ @ 493 kHz**；在 >9:1 電壓轉換比下效率 **96.2%**；近期單埠 PR 無磁性 DC-DC 功率級效率達 **99%**、PR 功率密度達 **5.7 kW/cm³**。（[MIT PER, TPEL 2022](https://per.mit.edu/wp-content/uploads/2023/10/jpTPEL2022Boles_HighPRDensity_FINAL.pdf)、[Nature Communications, A hybrid piezoelectric resonator-based DC-DC converter](https://www.nature.com/articles/s41467-026-70494-0)）

**資金訊號**：Jessica Boles 獲 ARPA-E IGNIITE 2024 早期職涯獎，項目「High-Performance, Modular Piezoelectric Components for Miniaturized Power Conversion」，金額 **$500,000**。（[ARPA-E 項目頁](https://arpa-e.energy.gov/programs-and-initiatives/search-all-projects/high-performance-modular-piezoelectric-components-miniaturized-power-conversion)、[Berkeley EECS](https://eecs.berkeley.edu/news/jessica-boles-wins-arpa-e-igniite-early-career-award/)）**注意：$500k 是早期職涯獎等級，不是產業化資金。**

### 2.2 公司側

| 公司 | 在壓電功率/兩用元件的位置 | 證據 |
|---|---|---|
| **Enphase Energy** | 控制層專利（trajectory control），微逆變器出貨體量 | US12268094（已核准） |
| **TDK / TDK Electronics（Deutschlandsberg, AT）＋ relyon plasma** | **CeraPlas**：多層 Rosen 型 PT，把「升壓」與「冷電漿產生」合併在單一元件；硬 PZT 與內部**銅**電極共燒；輸入側多層、輸出側單體 | TDK 官網明述 "new patented technology"，**專利號查無** |
| **Cirrus Logic** | 用矽主動電感驅動壓電換能器（觸覺） | US12396367B2 |
| **Murata / Matsushita(Panasonic) / NEC** | 1990s–2000s CCFL 世代 PT 專利，**推算已到期**；2020 年後新佈局**查無** | US6184631B1 / EP1050954A4 / US5969954A / US6535407 |
| **Kyocera / Taiyo Yuden** | 壓電功率轉換佈局**查無**（僅確認兩者為被動元件大廠） | — |
| **Steminc / STEMINC、mmech（Micromechatronics）** | 現貨 PT 元件供應（例：SMMTF55P4S80，55 kHz / 4 W 多層 PT） | [Steminc 產品頁](https://www.steminc.com/PZT/en/multilayer-piezo-transformer) |

### 2.3 週邊島嶼（與功率轉換島無共同專利權人）

- **穿金屬壁功率＋資料同傳**：`US20150049587A1`「Full-duplex ultrasonic through-wall communication and power delivery system with frequency tracking」、`US20170163354A1`「System For Ultrasonic Communication Across Curved Metal Surfaces」。已驗證性能：**12.4 Mbps 資料 + 32.5 W 功率，穿越 6.3 cm 鋼塊**；另有 15 Mbps / 30 W 平板紀錄。
- **壓電高壓/電漿/離子**：`US7821762`「Piezoelectric transformer type ionizer and neutralization method」、`US11337295`「Device and component for generating a high voltage or high field strength」（**受讓人未驗證，疑似 TDK/Epcos 系**）。日本早期件 JP 特開平10-302994（PT 驅動針電極離子產生器）。
- **隔離感測**：`EP3127172B1`「Galvanic isolated piezoelectric transformer based voltage sensors」。
- **能量擷取**：`US7649305B2` Piezoelectric energy harvester、`US6407484B1` Piezoelectric energy harvester and method、`WO2008124762A1` Energy harvesting from multiple piezoelectric sources；近期件 `US12,255,556`（2025-03-18 核准，用於自主心臟膠囊供電之彎曲剛度梯度振盪結構壓電擷取器）。
- **壓電閂鎖繼電器/開關**：`US4538087A`（AC 驅動壓電閂鎖繼電器）、`US6512322`、`US6927529`（液態金屬縱向壓電閂鎖繼電器）、`US7679186`（壓電 MEMS 開關陣列）。核心優勢是**真機械閂鎖：保持狀態不耗電，只有切換時耗電**。

---

## 3. 關鍵數字表

| 項目 | 數值 | 來源 |
|---|---|---|
| MIT 地基專利優先權日 | 2021-05-07（US 臨時案 63/185,663） | [US12126324](https://patents.google.com/patent/US12126324/en) |
| MIT 地基專利 PCT 申請日 | 2022-05-06（PCT/US2022/028043） | 同上 |
| MIT 地基專利受讓登記日 | 2023-11-06 → MIT | 同上 |
| 推算保護到期 | **~2041–2042**（申請日+20，未實查） | 推算 |
| PR 功率處理密度（MIT 2022） | 1.01 kW/cm³ @ 493 kHz | [MIT PER TPEL 2022](https://per.mit.edu/wp-content/uploads/2023/10/jpTPEL2022Boles_HighPRDensity_FINAL.pdf) |
| PR 功率密度（近期單埠無磁性） | 最高 5.7 kW/cm³，功率級效率 99% | [UC 33625](https://techtransfer.universityofcalifornia.edu/NCD/33625.html) |
| 高轉換比效率 | 96.2% @ >9:1 | [MIT PER](https://per.mit.edu/wp-content/uploads/2023/10/jpTPEL2022Boles_HighPRDensity_FINAL.pdf) |
| 隔離式 PT-based DC-DC（Berkeley） | 峰值 97.5%，損耗比較前人降 **17×** | [UC 33842](https://techtransfer.universityofcalifornia.edu/NCD/33842.html) |
| Curie 溫度 | PZT 320 °C；LiNbO₃ 1150 °C（供應商通常把上限訂在 Curie 的一半） | [Power Electronics News](https://www.powerelectronicsnews.com/piezoelectric-resonators-in-dc-dc-converters-current-status-and-limits/) |
| 25→150 °C 劣化 | PZT：k² −25%、Q_M **−80%**；LiNbO₃：k² 不變、Q_M 僅 −21%（Stanford 研究） | 同上 |
| 塊體 PT 頻寬上限 | 工作頻率 <幾十 MHz、高 Q ⇒ 頻寬僅**幾十 kHz**，**不足以驅動寬能隙功率元件閘極** | [Nature Comms Eng.](https://www.nature.com/articles/s44172-026-00681-w) |
| SAW 隔離閘驅（新路線） | LiNbO₃ SAW，隔離 **2.75 kV**、隔離電容 **0.032 pF**，驅動 650 V/11 A GaN，導通時間 108.8 ns | 同上 |
| 穿金屬壁同傳 | 12.4 Mbps + 32.5 W，穿 6.3 cm 鋼 | [MDPI Appl. Sci. 8(5)692](https://www.mdpi.com/2076-3417/8/5/692) |
| CCFL 世代 PT 出貨規模 | 1990s 中～2000s 初，年 **2500–3000 萬顆**；LED 背光取代後主要供應商**停止量產**、專用 IC **停產** | [MDPI Actuators 5(2)12](https://www.mdpi.com/2076-0825/5/2/12) |
| ARPA-E IGNIITE 2024（Boles） | $500,000 | [ARPA-E](https://arpa-e.energy.gov/programs-and-initiatives/search-all-projects/high-performance-modular-piezoelectric-components-miniaturized-power-conversion) |
| 壓電能量擷取專利申請高峰 | 2019–2024（PatSnap 分析，**AI 生成內容，可靠度低**） | [PatSnap](https://www.patsnap.com/resources/blog/articles/piezoelectric-energy-harvesting-patent-landscape-2026/) |

---

## 4. 「新能力型」應用機會（專利視角）

### 4.1 「自診斷隔離屏障」：同一顆壓電體同時是功率通道、隔離牆、與屏障完整性感測器

- **新能力是什麼**：安規隔離屏障（光耦、變壓器、電容隔離）今天是**黑盒子**——你無法在系統運行中知道它的絕緣裕度還剩多少，只能靠出廠 HiPot 與統計壽命。壓電/聲學屏障不同：**屏障本身就是共振器**，它的共振頻率、Q 值、阻抗曲線會隨陶瓷裂紋、去極化、界面剝離、溫度而連續漂移。於是「傳能量」與「量自己還好不好」用的是同一顆元件、同一組電極。
- **為什麼以前做不到**：光耦與磁性隔離的傳輸機制（光子、磁通）不攜帶屏障材料的機械狀態資訊；電容隔離的介電層一旦擊穿就是災難性的、沒有前兆訊號。壓電屏障是**機械共振體**，退化是漸進且可電性觀測的。
- **是否真非替代**：**是（新能力）**。這不是「更小的隔離器」，而是「會回報自己健康狀態的隔離器」——功能安全（ISO 26262 / IEC 61508）要求的診斷覆蓋率（DC）在現行隔離元件上很難拿到，這是規格書上打不出來的新欄位。
- **誰在做**：`EP3127172B1`「Galvanic isolated piezoelectric transformer based voltage sensors」最接近，但那是**用 PT 做隔離電壓感測**，不是**用 PT 自我診斷**。**「屏障自診斷」的 claim 查無。這是明確白空間。**
- **TRL**：概念層（TRL 2–3）。PT 隔離供電本身是 TRL 8（1990s 就有 MOSFET/IGBT 閘驅 PT 隔離論文），但自診斷閉環查無實作。
- **市場訊號**：Nature Communications Engineering 2026 的微波聲學隔離閘驅論文（2.75 kV / 0.032 pF）證明**聲學隔離重新成為熱題**，但該論文走的是 SAW 路線且明確指出塊體 PT 頻寬不足。
- **技術難點**：(a) 要在傳能的同時做阻抗譜量測，需要 in-situ 小訊號注入且不干擾功率路徑；(b) 要把「頻率漂移 X ppm ⇒ 絕緣裕度剩 Y%」這條映射建立起來，需要大量加速壽命試驗數據——**這是護城河，也是最大成本**。

### 4.2 「零待機功耗的功率路徑重組」：壓電閂鎖開關做冷備援/斷電隔離

- **新能力是什麼**：把壓電閂鎖繼電器（機械閂鎖，保持不耗電、只有切換耗電）與壓電的高壓自生能力結合——**一顆元件既能自己升壓產生驅動自己所需的高壓，又能閂鎖保持**。結果是「真正 0 μA 靜態電流的高壓固態隔離開關」。
- **為什麼以前做不到**：半導體開關（MOSFET/固態繼電器）漏電流不為零，且高壓下 off-state 漏電隨溫度指數上升；電磁繼電器保持要耗電（除非用磁閂鎖，但體積與 EMI 大）；MEMS 靜電開關需要持續施加保持電壓。壓電閂鎖 + 壓電自升壓兩者結合，才可能做到「保持零功耗 + 高隔離 + 無磁」。
- **是否真非替代**：**半**。閂鎖繼電器本身是老技術（`US4538087A` 1985 年就有 AC 驅動壓電閂鎖繼電器），所以「閂鎖」不新；新的是「同一顆壓電體自己產生驅動電壓」這層整合。要誠實承認：這比較像**更高整合度**，不是全新物理。
- **誰在做**：查到的專利都是 2000s 早期（`US6512322`、`US6927529`、`US7679186`），**推算已到期或接近到期**。近年佈局**查無**。
- **TRL**：3–4。
- **市場訊號**：弱。查無近期產品或投資。
- **技術難點**：接點可靠度（機械接點的壽命與接觸電阻）；壓電致動力量有限，難以做大電流接點。

### 4.3 「壓電做主動電感」的反向命題（Berkeley 33585 的專利空隙）

- **新能力是什麼**：Cirrus Logic 的 `US12396367B2` 是**用矽主動電感電路去驅動壓電負載**；Berkeley 33585 是**用壓電諧振器去模擬電感給一般電路用**。後者若真能做成 drag-and-drop，等於讓「電感」變成可**電性即時調變**的元件（改開關序列即改等效電感值），而磁性電感做不到——磁芯的 L 值只能靠飽和/氣隙被動變化。
- **為什麼以前做不到**：磁性電感的 L 由幾何與磁導率決定，無法在 μs 尺度電性調變；用矽主動電感（gyrator）則功率處理能力極差。壓電諧振器是**高 Q 的機械儲能體**，能量密度夠、又能靠開關序列改變等效阻抗。
- **是否真非替代**：**半到否**。UC 技轉頁自己就寫「drag-and-drop replacement for bulky magnetic inductors」——**這正是客戶排除的替代路線**。只有當你不是拿它換電感、而是拿它做「可即時調變的電感」（例如可變共振頻率的無線充電發射端、自適應 EMI 濾波器、寬範圍阻抗匹配網路）時，才升級為新能力。**建議降低權重，但保留「可調變」這條分支。**
- **誰在做**：UC Berkeley（33585，專利號未公開）；反方向由 Cirrus Logic 佔位。
- **TRL**：3（2024 COMPEL 論文層級）。
- **技術難點**：等效 L 的可調範圍受限於 PR 的機械品質因數與雜散模態；spurious mode 已有多篇 arXiv 專門處理（見 5.5）。

### 4.4 「穿越不可穿透屏障的功率＋資料同傳」（已有專利，但白空間在應用層）

- **新能力是什麼**：穿越 6.3 cm 實心鋼壁同時送 32.5 W 功率與 12.4 Mbps 資料，**不打孔、不破壞結構完整性**。這是電磁波在導體中完全做不到的（趨膚深度）。
- **為什麼以前做不到**：金屬對 EM 是完全屏蔽；唯一替代是打貫穿孔 + 密封饋通，而在壓力容器、核設施、深海耐壓艙、防爆殼體上，**打孔本身就是最大的失效源**。
- **是否真非替代**：**是（新能力）**，這是本文件中最乾淨的一條。
- **誰在做**：`US20150049587A1`（全雙工穿牆通訊與供電，含頻率追蹤）、`US20170163354A1`（曲面金屬表面超音波通訊）。**注意這兩件都是 A1 公開案，未確認是否核准。**
- **TRL**：5–6（有實測系統論文）。
- **市場訊號**：中。應用集中在核電、油氣、船艦——**銷量小、單價高、認證嚴，正好抵消壓電單價高的缺點**。這一點與客戶「壓電太貴」的顧慮直接互補。
- **技術難點**：聲學駐波與多重反射造成的通道深度衰落；耦合劑長期可靠度；曲面/焊道/塗層的失配。

### 4.5 「單顆陶瓷 = 電源 + 電漿源」（TDK CeraPlas 已量產，白空間在下游）

- **新能力是什麼**：把「升壓變壓器」與「電漿產生電極」合併成單一陶瓷體，直接由低壓 DC 產生大氣壓冷電漿。傳統作法需要高壓電源 + 高壓線 + 電極三段。
- **為什麼以前做不到**：需要 kV 級輸出但體積要小到能手持；磁性高壓變壓器 + 高壓線的體積與安全問題無解。
- **是否真非替代**：**是**（單元件整合改變了系統形態，而不只是尺寸）。
- **誰在做**：TDK Electronics（Deutschlandsberg）+ relyon plasma，**已量產**；TDK 明述為 "new patented technology"，但**專利號查無**。
- **TRL**：9（有商品）。
- **技術難點 / 進入障礙**：TDK 的護城河是**硬 PZT 與銅內電極共燒**的材料/製程 know-how，不是電路。台灣廠若要切入，難點在陶瓷共燒而非電力電子。

### 4.6 「機械阻尼 + 能量回收 + 結構健康監測」三合一介面（學術密集、專利權人分散）

- **新能力是什麼**：同一片壓電貼片在同一個開關週期內同時完成：抑振（SSDI/SSDV）、把抑下來的能量回收（SSHI/SECE/bias-flip）、並從開關時序反推結構狀態（模態頻率漂移 ⇒ 損傷）。
- **為什麼以前做不到**：SSD 家族的開關本來就必須「同步於位移極值」，因此電路**天生就知道結構的相位與振幅**——這個資訊過去被丟掉。做成三合一，等於免費得到結構健康監測。
- **是否真非替代**：**半**。抑振、回收、監測三件事分開都做得到；價值在於**省掉線束與獨立感測器**，這偏「更整合」而非「全新能力」。但在旋轉件（航空發動機葉盤）與封裝內部這種**拉不出線**的地方，會升級為真新能力。
- **誰在做**：學術上極密集（SSDS / SSDI / SSDV / SSDNC / SP-SSDI；bias-flip、SECE、MCE、MCEBF、SICE 等），量化差距明確：MCEBF 相對 SECE 提升 **57.3%**、相對 MCE 提升 **24%**。**但專利側：查無集中的專利權人、查無代表性專利號。這是本次研究最大的缺口，也可能正是白空間。**
- **TRL**：4–5（實驗室系統多，產品少）。
- **技術難點**：自供電的極值偵測電路在低激振下起不來（冷啟動）；SSD 對寬頻/多模態激振效果衰減。

---

## 5. 反面證據、失敗案例與物理上限

1. **壓電變壓器有過一次真實的商業死亡，而且死因不是技術。** CCFL 背光是 PT 唯一一次大量產應用，1990s 中期～2000s 初年出貨 **2500–3000 萬顆**；LED 背光取代 CCFL 後，**主要供應商停止高量產、對應的專用 IC 也大量停產**。教訓有二：(a) 壓電功率元件的量產經濟性**完全綁定單一殺手級應用**，應用消失供應鏈就散；(b) 今天要重啟量產，等於要重建一整條停擺 15 年的產業鏈。（[MDPI Actuators 5(2)12](https://www.mdpi.com/2076-0825/5/2/12)）

2. **塊體壓電變壓器有一個明確的物理頻寬牆，而且新論文是繞開它而不是解決它。** Nature Communications Engineering（2026）明述：塊體模態 PT 工作頻率在幾十 MHz 以下、機械 Q 高，導致**頻寬只有幾十 kHz，不足以做先進寬能隙功率元件的閘極驅動**；該論文因此改用 **SAW（微波聲學）** 路線。**這意味著「用塊體 PT 做 WBG 閘驅隔離」這條應用是被物理否決的**，別把它列進機會清單。（[Nature Comms Eng. s44172-026-00681-w](https://www.nature.com/articles/s44172-026-00681-w)）

3. **PZT 在中溫就崩。** 25 °C → 150 °C，PZT 的 k² 掉 25%、**Q_M 掉 80%**；LiNbO₃ 相對好（k² 不變、Q_M 僅掉 21%），但 LiNbO₃ 的 k² 絕對值低、單晶成本高。此外**高溫與過強電場都會造成永久去極化**，且供應商通常把使用上限訂在 Curie 溫度的一半（PZT ⇒ 約 160 °C）。**汽車引擎艙、功率模組內部這類環境對 PZT 是不友善的。**（[Power Electronics News](https://www.powerelectronicsnews.com/piezoelectric-resonators-in-dc-dc-converters-current-status-and-limits/)）

4. **高電壓轉換比下效率退化是拓樸性的，不是工藝問題。** 基準 PR-based DC-DC 在高轉換比下，效率與電流處理能力都會因**拓樸操作施加的電荷利用率限制（charge utilization limitation）**而下降。MIT 要用專門設計（96.2% @ >9:1）才壓得住。這代表**寬輸入範圍應用（例如 PV、車用 12–48 V 混合）對 PR 特別不利**。

5. **雜散模態（spurious modes）是持續未解的工程稅。** 光是為了壓制它就有一整批專門論文：`arXiv 2409.15686`（LiNbO₃ 用 active ring 抑制雜散模態）、`arXiv 2604.06426`（接地環電極的 spurious-free LiNbO₃ BAW）、`arXiv 2603.19409`（單晶 AlN 晶圓 BAW 用於壓電功率轉換）、`arXiv 2508.09407`（週期極化 LiNbO₃ 諧振器）。另有「Fixed-Frequency Control of Piezoelectric Resonator DC-DC Converters for **Spurious Mode Avoidance**」——**連控制策略都得為雜散模態讓路**。

6. **地基專利已被佔，且到期日很遠。** MIT 的 US12126324 直接 claim「PR 的幾何條件，且該條件以轉換器指定的電壓與功率等級定義」——這是一個**設計規則層級**的 claim，很難迴避；加上拓樸/控制層的 US12,009,746 / US12,388,364。優先權 2021-05-07，**推算 2041–2042 才到期**。想做 PR-based DC-DC 的公司，要嘛授權，要嘛承擔風險。**這是客戶排除「直接取代電感」路線之外的獨立第二理由。**

7. **NPE 風險：查無證據，但也不能說沒有。** 本次未查到任何壓電功率轉換或壓電能量擷取領域的 NPE/PAE 訴訟案例。一般性背景數據為「約 60% 的新專利訴訟由 NPE 提起」（通用統計，非本領域）。**本領域專利多握在大學（MIT、UC）與實體公司（Enphase、TDK、Cirrus Logic）手上，大學技轉辦公室的授權行為與 NPE 不同（通常尋求實施而非純訴訟）。目前判斷 NPE 風險低，但這是「查無」而非「證實無」。**

8. **成本論證的反面：PT 元件不是完全沒有成本路徑。** 有研究把硬 PZT 的燒結溫度壓到 **≤1000 °C**，以便使用**銅等賤金屬電極**取代貴金屬——TDK CeraPlas 正是「硬 PZT 與內部銅電極共燒」。這代表**壓電元件的成本並非鎖死在貴金屬電極上**，客戶「壓電單價高」的前提在特定製程下有鬆動空間；但這條路的 know-how 在 TDK 手上。

9. **PZT 的鉛問題目前靠 RoHS 豁免撐著。** 供應商（Steminc）宣稱 PZT 壓電變壓器「豁免於 RoHS」。**豁免是有審查期限的政策，不是永久權利**——把長週期產品（車用、工業）押在 PZT 上有法規風險。（**此為供應商說法，未經法規原文查證，標記未驗證。**）

---

## 6. 未解問題（給下一輪研究）

1. **US 12,009,746 與 US 12,388,364 必須取得一手驗證。** 需要能開 Google Patents / Justia / USPTO Patent Public Search 的環境，確認：完整標題、核准日、claim 1 全文、法律狀態、同族（EP/CN/JP 有無進入）。**特別要確認中國與台灣有無同族——若沒有，客戶在中國市場的自由實施空間可能很大。** 這是最高優先。

2. **MIT 與 UC Berkeley 的專利族完整清單與地域覆蓋。** 建議直接查 `patents.justia.com/inventor/jessica-boles`、`/inventor/david-j-perreault`、`/assignee/massachusetts-institute-of-technology` 與 UC Regents 的受讓清單。同時查 UC 技轉 33842/33625/33585 對應的 US/WO 公開號（技轉頁通常不寫，需靠發明人＋日期反查）。

3. **「主動/被動兩用」的 claim 語言到底存不存在？** 本次沒查到任何專利在 claim 中明確主張「同一壓電元件在系統中分時或同時扮演儲能被動元件與致動/感測主動元件」。需要用結構化檢索（例如 CPC = H02M3/* AND H10N30/* 交集、或 claim 全文含 "both ... passive ... and ... active"）驗證這個白空間是真的還是搜尋不到。**若為真，這是本專案最值錢的一條發現。**

4. **SSDI/SSHI/bias-flip 的專利權人到底是誰？** 學術文獻極密集（Richard、Guyomar、Lallart 等法國 INSA Lyon 一脈；Ramadass/Chandrakasan 的 bias-flip 一脈於 MIT），但本次**完全沒查到對應專利號與受讓人**。需要專門一輪：查 INSA Lyon / CNRS、MIT（Chandrakasan）、Texas Instruments、Analog Devices 在能量擷取介面電路的專利。這決定 4.6 那條機會是白空間還是雷區。

5. **TDK CeraPlas 的專利號與地域覆蓋。** TDK 明述 "patented"，但號碼查無。這決定「單顆陶瓷 = 電源 + 電漿源」這條路對台灣廠是否可行。

6. **Murata / Kyocera / Taiyo Yuden 2020 年後有沒有在壓電功率轉換動作？** 本次只查到 Murata 的 2000 年件。日本大廠若沒動作，對台灣廠是好消息（無巨頭壓境）；若有未公開的在審案，風險完全不同。建議用日文關鍵字（圧電トランス、圧電共振子、電力変換）在 J-PlatPat 方向查。

---

## 7. 來源清單

1. [Google Patents — US12126324B2, Piezoelectric resonators for power conversion](https://patents.google.com/patent/US12126324/en) — MIT 地基專利；發明人 Perreault/Lang/Boles/Bonavia，PCT/US2022/028043，優先權 63/185,663 (2021-05-07)，受讓 MIT (2023-11-06)。
2. [Justia — Jessica Boles, Inventions, Patents and Patent Applications](https://patents.justia.com/inventor/jessica-boles) — Boles 名下專利清單頁；US12,009,746 / US12,388,364 的 abstract 文字由此關聯出現（**未取得直接專利頁連結，半驗證**）。
3. [USPTO — US12268094, Piezoelectric power converter with trajectory control](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/12268094) — 受讓人 Enphase Energy，發明人 Michael J. Harrison；輸入橋+PT+輸出橋+trajectory controller。
4. [Justia — Patents Assigned to Enphase Energy, Inc.](https://patents.justia.com/assignee/enphase-energy-inc) — 用於交叉確認 Enphase 的受讓清單。
5. [Google Patents — US9871182B2, Frequency tracking piezoelectric transformer power converter with simultaneous two-parameter control](https://patents.google.com/patent/US9871182B2/en) — 2018-01-16 核准，家族 WO2014145587A1（**受讓人未驗證**）。
6. [UC Tech Transfer 33842 — Piezoelectric Transformers For Power Conversion](https://techtransfer.universityofcalifornia.edu/NCD/33842.html) — UC Berkeley 掛牌授權；隔離式無磁性 PT-based DC-DC，峰值 97.5%、損耗比降 17×。
7. [UC Tech Transfer 33625 — Overtone Piezoelectric Resonator For Power Conversion](https://techtransfer.universityofcalifornia.edu/NCD/33625.html) — 泛音模態 PR；適用 DC-DC/DC-AC/AC-DC/active inductor。
8. [UC Tech Transfer 33585 — Active Inductor Based On A Piezoelectric Resonator](https://techtransfer.universityofcalifornia.edu/NCD/33585.html) — 明述為磁性電感的 drag-and-drop replacement（**＝客戶排除的替代路線**）。
9. [Google Patents — US12396367B2, Driver circuitry comprising active inductor circuitry for piezoelectric transducers](https://patents.google.com/patent/US12396367) — 受讓人 Cirrus Logic；用矽主動電感驅動壓電換能器（反向命題）。
10. [Google Patents — US5768111A, Converter comprising a piezoelectric transformer and a switching stage of a resonant frequency different from that of the transformer](https://patents.google.com/patent/US5768111) — 1998 年第一波 PT 轉換器專利。
11. [Google Patents — US5969954A, AC/DC converter with a piezoelectric transformer](https://patents.google.com/patent/US5969954A/en) — NEC，1998-01-15。
12. [Justia — US6535407, DC/DC converter having a piezoelectric transformer and rectification-smoothing circuit](https://patents.justia.com/patent/6535407) — NEC，發明人 Toshiyuki Zaitsu，1998-07-28 申請 / 2003-03-18 核准。
13. [USPTO — US5329200, Piezoelectric transformer converter for power use](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/5329200) — 1994 年件。
14. [Google Patents — EP1050954A4, Drive circuit for piezoelectric transformer](https://patents.google.com/patent/EP1050954A4/en) — Matsushita，1999-10-19。
15. [Google Patents — JP2002064977A, 圧電トランスの駆動方法および電源装置](https://patents.google.com/patent/JP2002064977A/en) — Matsushita，2000-08-21。
16. [Google Patents — US6184631B1, Piezoelectric inverter](https://patents.google.com/patent/US6184631B1/en) — Murata Manufacturing，2000-03-16 申請（**本次查到 Murata 唯一的壓電功率件**）。
17. [Google Patents — US6586863B2, Rosen type piezoelectric transformer with multiple output electrodes](https://patents.google.com/patent/US6586863B2/en) — Rosen 型改良件。
18. [Google Patents — US7122939B2, Piezoelectric power supply](https://patents.google.com/patent/US7122939) — 壓電電源。
19. [MDPI Actuators 5(2), 12 — Piezoelectric Transformers: An Historical Review](https://www.mdpi.com/2076-0825/5/2/12) — Rosen 原始專利號（US2,830,274 / 2,974,296 / 2,975,354，**日期敘述互相矛盾**）；CCFL 世代年出貨 2500–3000 萬顆與量產終止。
20. [Google Patents — EP3127172B1, Galvanic isolated piezoelectric transformer based voltage sensors](https://patents.google.com/patent/EP3127172B1/en) — 隔離式 PT 電壓感測（最接近「自診斷隔離屏障」的既有件）。
21. [Nature Communications Engineering — Microwave-acoustic-based isolated gate driver for power electronics](https://www.nature.com/articles/s44172-026-00681-w) — SAW 隔離 2.75 kV / 0.032 pF / 650 V GaN / 108.8 ns；**明述塊體 PT 頻寬僅幾十 kHz 不足以驅動 WBG 閘極**。
22. [arXiv 2511.13412 — Microwave-acoustic-based isolated gate driver for power electronics](https://arxiv.org/pdf/2511.13412) — 同一研究的 preprint。
23. [Power Electronics News — Piezoelectric resonators in DC-DC converters: current status and limits](https://www.powerelectronicsnews.com/piezoelectric-resonators-in-dc-dc-converters-current-status-and-limits/) — Curie 溫度、25→150 °C 的 k²/Q_M 劣化、去極化、高轉換比效率退化。
24. [MIT PER — A Piezoelectric-Resonator-Based DC–DC Converter Demonstrating 1 kW/cm³ Resonator Power Density (TPEL 2022)](https://per.mit.edu/wp-content/uploads/2023/10/jpTPEL2022Boles_HighPRDensity_FINAL.pdf) — 1.01 kW/cm³ @ 493 kHz、96.2% @ >9:1。
25. [Nature Communications — A hybrid piezoelectric resonator-based DC-DC converter](https://www.nature.com/articles/s41467-026-70494-0) — 混合式 PR 轉換器最新進展。
26. [arXiv 2409.15686 — Lithium Niobate Resonators for Power Conversion: Spurious Mode Suppression Via an Active Ring](https://arxiv.org/pdf/2409.15686) — 雜散模態抑制。
27. [arXiv 2604.06426 — Spurious-Free Lithium Niobate Bulk Acoustic Wave Resonator with Grounded-Ring Electrode](https://arxiv.org/pdf/2604.06426) — 同上，接地環電極路線。
28. [arXiv 2603.19409 — Single-Crystal AlN Wafer-Based Bulk Acoustic Resonators for Piezoelectric Power Conversion](https://arxiv.org/pdf/2603.19409) — AlN 單晶 BAW 用於功率轉換（無鉛路線）。
29. [arXiv 2508.09407 — Periodically Poled Piezoelectric Lithium Niobate Resonator for Piezoelectric Power Conversion](https://arxiv.org/pdf/2508.09407) — 週期極化 LiNbO₃。
30. [ARPA-E — High-Performance, Modular Piezoelectric Components for Miniaturized Power Conversion](https://arpa-e.energy.gov/programs-and-initiatives/search-all-projects/high-performance-modular-piezoelectric-components-miniaturized-power-conversion) — Boles，IGNIITE 2024，$500,000。
31. [Berkeley EECS — Jessica Boles wins ARPA-E IGNIITE Early Career Award](https://eecs.berkeley.edu/news/jessica-boles-wins-arpa-e-igniite-early-career-award/) — 同上之新聞佐證。
32. [TDK Electronics — Cold plasma from a single component (CeraPlas)](https://www.tdk-electronics.tdk.com/en/373562/tech-library/articles/applications-cases/applications-cases/cold-plasma-from-a-single-component/1109546) — 多層 Rosen 型 PT、硬 PZT 與銅內電極共燒、"new patented technology"（**專利號查無**）。
33. [TDK Electronics 新聞稿 — Piezo transformers and plasma generators: TDK cooperates with relyon plasma](https://www.tdk-electronics.tdk.com/en/373388/company/press-center/press-releases/press-releases/piezo-transformers-and-plasma-generators-tdk-cooperates-with-relyon-plasma-to-develop-and-manufacture-cutting-edge-plasma-solutions/1416224) — 量產合作對象。
34. [USPTO — US10349818, Adaptive control of a fiber scanner with piezoelectric sensing](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/10349818) — self-sensing：致動與感測同時進行、自感測電容橋分離驅動與位移訊號（**受讓人未驗證**）。
35. [USPTO — US9872606, Adaptive control of a fiber scanner with piezoelectric sensing](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/9872606) — 同族較早件。
36. [Google Patents — CN111060232B, 壓電致動器輸出力自感知方法](https://patents.google.com/patent/CN111060232B/en) — 中國的 self-sensing 專利。
37. [Google Patents — US20150049587A1, Full-duplex ultrasonic through-wall communication and power delivery system with frequency tracking](https://patents.google.com/patent/US20150049587) — 穿金屬壁功率＋資料同傳（**A1 公開案，核准與否未驗證**）。
38. [Google Patents — US20170163354A1, System For Ultrasonic Communication Across Curved Metal Surfaces](https://patents.google.com/patent/US20170163354A1/en) — 曲面金屬超音波通訊。
39. [MDPI Applied Sciences 8(5) 692 — An Ultrasonic Through-Metal-Wall Power Transfer System with Regulated DC Output](https://www.mdpi.com/2076-3417/8/5/692) — 12.4 Mbps + 32.5 W 穿 6.3 cm 鋼；15 Mbps / 30 W 平板。
40. [USPTO — US7821762, Piezoelectric transformer type ionizer and neutralization method](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/7821762) — PT 離子產生器；提及 JP 特開平10-302994。
41. [USPTO — US11337295, Device and component for generating a high voltage or high field strength](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/11337295) — 壓電高壓/高場強產生（**受讓人未驗證**）。
42. [Google Patents — US7649305B2, Piezoelectric energy harvester](https://patents.google.com/patent/US7649305B2/en) — 能量擷取代表件。
43. [Google Patents — US6407484B1, Piezoelectric energy harvester and method](https://patents.google.com/patent/US6407484) — 早期能量擷取件。
44. [Google Patents — WO2008124762A1, Energy harvesting from multiple piezoelectric sources](https://patents.google.com/patent/WO2008124762A1/en) — 多源擷取。
45. [Justia — US12,255,556, Piezoelectric-transducer energy harvester ... for powering an autonomous cardiac capsule](https://patents.justia.com/patent/12255556) — 2025-03-18 核准，顯示能量擷取專利仍持續核准中。
46. [Google Patents — US4538087A, Alternating current driven piezoelectric latching relay and method of operation](https://patents.google.com/patent/US4538087) — 壓電閂鎖繼電器最早期件。
47. [USPTO — US6512322, Longitudinal piezoelectric latching relay](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/6512322) — 縱向壓電閂鎖繼電器。
48. [USPTO — US6927529, Solid slug longitudinal piezoelectric latching relay](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/6927529) — 液態金屬/固體滑塊閂鎖。
49. [USPTO — US7679186, Piezoelectric micro electro-mechanical system switch, array of the switches, and method of fabricating the same](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/7679186) — 壓電 MEMS 開關陣列。
50. [DTU Orbit — Inductorless bi-directional piezoelectric transformer-based converters: Design and control considerations (PhD, 2016)](https://orbit.dtu.dk/en/publications/inductorless-bi-directional-piezoelectric-transformerbased-conver) — DTU/Andersen 一脈；與 Noliac A/S、Danfoss PolyPower 合作（**專利佈局查無**）。
51. [DTU Orbit — Piezoelectric transformer based power converters: design and control (PDF)](https://backend.orbit.dtu.dk/ws/files/54305910/Piezoelectric_transformer_based_power_converters_design_and_control.pdf) — 同上之全文。
52. [USPTO CPC Scheme — H02M](https://www.uspto.gov/web/patents/classification/cpc/html/cpc-H02M.html) — AC/DC/DC-DC 轉換分類（**未取得個別專利的分類碼**）。
53. [USPTO CPC Scheme — H02N (Electric machines not otherwise provided for)](https://www.uspto.gov/web/patents/classification/cpc/html/cpc-H02N.html) — H02N2/18＝壓電/電致伸縮/磁致伸縮之機械輸入電輸出。
54. [USPTO CPC Scheme — H10N (PDF)](https://www.uspto.gov/web/patents/classification/cpc/pdf/cpc-scheme-H10N.pdf) — H10N30/30＝機械輸入電輸出之壓電/電致伸縮裝置。
55. [PatSnap — Piezoelectric energy harvesting patent landscape 2026](https://www.patsnap.com/resources/blog/articles/piezoelectric-energy-harvesting-patent-landscape-2026/) — 申請高峰 2019–2024；提及 ABB（無線振動感測器）、SKF（壓電供電之軸承滾動體感測，德國待審）、Ceracomp（2025 JP，d₃₃ 達 6000 pC/N）、Shimco、SUNY、IIT Delhi（**AI 生成的部落格內容，可靠度低，僅供方向參考**）。
56. [Steminc — Multilayer Piezo Transformer 55 kHz 4 W (SMMTF55P4S80)](https://www.steminc.com/PZT/en/multilayer-piezo-transformer) — 現貨 PT 元件；PZT PT「豁免於 RoHS」之供應商說法（**未驗證**）。
57. [TI SLYT125 — Comparing magnetic and piezoelectric transformer approaches](https://www.ti.com/lit/pdf/slyt125) — PT vs 磁性變壓器的體積/隔離/雜散磁通比較。
58. [IEEE Xplore — A Piezoelectric-Resonator-Based "Active Inductor" (COMPEL 2024)](https://ieeexplore.ieee.org/document/10614003) — UC 33585 對應的學術發表。
59. [IEEE Xplore — Overtone Piezoelectric Resonators for Power Conversion (COMPEL 2024)](https://ieeexplore.ieee.org/document/10614005) — UC 33625 對應的學術發表。
60. [ScienceDirect — Selecting nonlinear piezoelectricity for fully autonomous self-sensing synchronized switch damping on inductor technique](https://www.sciencedirect.com/science/article/abs/pii/S0888327021002417) — SSDI 自感測自主化（4.6 節依據）。
61. [IEEE Xplore — Multiple Charge Extractions with Bias-Flip Interface Circuit for Piezoelectric Energy Harvesting](https://ieeexplore.ieee.org/document/9180492/) — MCEBF 較 SECE +57.3%、較 MCE +24%。
62. [MDPI Applied Sciences 10(4) 1478 — Dual-Connected Synchronized Switch Damping for Vibration Control of Bladed Disks in Aero-Engines](https://www.mdpi.com/2076-3417/10/4/1478) — SSDI 在航空發動機葉盤的應用（4.6 節「拉不出線」情境依據）。
