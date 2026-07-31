# 應用A4：壓電喇叭/觸覺/微泵——「致動＋電源＋感測合一」的整合機會

> **一句話結論**：這是整份研究裡「壓電兩用元件」**離收入最近**的一塊——因為壓電體已經在裡面了，不必說服客戶換材料，只要說服他把外掛的升壓電感、外掛的力量感測器、外掛的流量/閉塞感測器吃掉；但要誠實面對兩件事：**(1) Boréas Technologies 已經把「高壓驅動＋能量回收＋按壓感測同一片壓電」商品化並打進 Synaptics 觸控板與車用 HMI，客戶進場即為追隨者；(2) 真正還空著、也真正非替代性的白空間只有兩個——「密封裝置內壓電氣泵/微泵的自感測閉環（免流量計的閉塞與劑量偵測）」與「壓電升壓段與壓電致動段做在同一顆陶瓷體內、讓高壓永遠不離開陶瓷」。**

---

## 0. 研究方法與限制（誠實揭露，請先讀完再採信任何數字）

**這一節的坦白程度直接決定本文件的可用性，請客戶務必讀完。**

1. **本輪 WebSearch 成功次數 = 0。** 任務要求 25–35 次查詢，但我發出**第 1 次**查詢時即收到系統回覆：
   `this session has used its web search budget (200 of 200 WebSearch calls)`。
   session 層級的 200 次搜尋額度由本專案所有平行 agent 共用，在我啟動前已被耗盡（同目錄的 `11-electrostatic-actuators-artificial-muscle.md` 在其第 0 節也記錄了同一件事：「第 33 次查詢起，session 層級的 WebSearch 配額（200/200，與其他平行 agent 共用）耗盡」）。我實際發出 2 次查詢、2 次皆被拒，之後未再浪費回合。
2. **WebFetch 在本環境被 egress policy 全面封鎖**（任何 URL 一律 403），任務簡報已預先告知，我未嘗試。
3. **因此本文件的性質是「二次分析」而非「一手檢索」。** 所有外部事實均**轉引自本專案同目錄已完成的 dossier**（`02-dual-use-active-passive-concept.md`、`04-reliability-standards-qual.md`、`06-patents-power-and-dualuse.md`、`07-patents-nonpower-apps.md`、`11-electrostatic-actuators-artificial-muscle.md`、`21-drive-control-ic-design.md`）。那些 dossier 本身也是**搜尋摘要**而非原文查核。**這代表本文件的證據鏈長度是「模型摘要的摘要」，可信度必須相應打折。**
4. **標記系統**：
   - **【轉引】** ＝ 引用自上述 dossier 已列出的來源 URL，URL 我未親自開啟。
   - **【領域常識・未經檢索驗證】** ＝ 工程與產業常識，**凡涉及具體數字、型號、公司名一律不使用此標記**（不確定就寫「查無」）。
   - **【查無】** ＝ 本輪完全沒有資料。
5. **零編造承諾**：本文未出現任何無法對應到第 7 節某個 URL 的專利號、型號、公司名或數字。唯一例外是第 7 節 T15（Cirrus Logic 專利），URL 依 Google Patents 命名規則構造、**未驗證可達性**，已於該處標明。

### 0.1 本輪完全沒查到的部分（佔任務指派範圍的比例很大，請務必列入下一輪）

任務指派的子題中，以下**全部標為【查無】**：

| 指派子題 | 狀態 |
|---|---|
| **xMEMS Montara / Cowell** 規格、驅動電壓 | **查無**（僅有 Cypress 與 Skyline 兩則轉引） |
| **xMEMS Sycamore / XMC-2400** 超音波固態氣泵——技術原理、風量、功耗、量產狀態 | **查無（整項未查）** |
| xMEMS 募資輪次、客戶名單、與動圈喇叭的量化比較 | **查無** |
| xMEMS Cypress **驅動電壓**（兩用元件的切入點正在這裡） | **查無** |
| **TDK PiezoListen**、Murata 壓電喇叭、display-as-speaker、骨傳導 | **查無（整項未查）** |
| **Boréas 的輸出電壓/電流、靜態功耗、封裝、單價、募資輪次、白皮書內容** | **查無**（`21` 亦明記此缺口） |
| Boréas **能量回收比例的實測值**（只有廠商宣稱的相對倍數） | **查無** |
| **Ultraleap** 空中超音波觸覺 | **查無（整項未查）** |
| **超音波摩擦調變**（ultrasonic friction modulation） | **查無**；僅轉引到 Tanvas 的**電黏附**（electroadhesion）路線，那是不同物理機制 |
| Apple Force Touch 驅動方式 | **查無**（任務簡報自述為電磁式，我未能獨立驗證，故本文不引用） |
| **TTP Ventus / Lee Ventus Disc Pump** 規格、MTBF | **查無**（`04` 明記「TTP Ventus Disc Pump 的 MTBF──查無」） |
| **Murata microblower MZB** | **查無（整項未查）** |
| 壓電微泵用於**穿戴散熱 / 藥物輸送 / NPWT / 血壓計 / 氣體取樣**的具體產品 | **查無** |
| 本領域任何**市場規模、ASP、出貨量**數字 | **查無** |

**結論：本文件應被視為「基於既有內部證據的機會結構分析 + 下一輪檢索清單」，而不是市場情報報告。** 第 6 節就是可直接執行的下一輪查詢清單。

---

## 1. 結論摘要

1. **「兩用元件」在觸覺領域已經有人商品化，而且明確自稱是市場唯一。** Boréas Technologies 的 **BOS1901** 被官方描述為「市場上唯一同時觸發觸覺並感測按壓力的壓電驅動 IC」，其 **CapDrive** 架構的核心正是「**從致動器內部的負載電容回收能量並再利用，而不是放掉浪費**」。這在概念上就是客戶想做的事，只是實作在 IC 側而非陶瓷側。【轉引 T1、T2】
2. **Boréas 的宣稱數字是「電流消耗」不是「轉換效率」，不可混用。** 官方宣稱能量回收可讓壓電系統**整體電流消耗降低最多 90%**、比競品壓電驅動 IC **效率好 10×**、比 LRA 省電 **20×**。同時期學術界主動 LC 電荷回收的實測是**電路能量損耗降低 49% / 50% / 55%（@40 / 80 / 120 Hz）**；被動式（2 顆二極體＋1 顆電阻）回收的**物理上限約 50%**。**廠商的 90% 與學術的 50% 不是同一個度量，做競品比較前必須統一。**【轉引 T4、T1、T25、T26】
3. **大廠採用訊號是真的存在，不是 PoC 階段。** Synaptics 與 Boréas 合作推出高性能壓電觸控板；2020 年即有車用 HMI 採用新聞稿；TDK **PowerHap** 致動器內建感測、可偵測 **≤25 N** 壓力、激振頻段 **1 Hz–1000 Hz**，免外掛觸控感測器。**「致動＋感測合一」在觸覺領域的 TRL 是 9，不是 3。**【轉引 T6、T7、T12】
4. **台灣取樣管道已經通了，這是時程上的重大利多。** EDOM（益登科技）已代理 Boréas **BOS1901 / BOS1921** 產品線，代表在台灣取得評估板與 FAE 支援不需要跨國談判，PoC 可以壓縮數個月。**建議把「買現貨量一次、確認現貨做不到什麼」列為第一個 go/no-go 里程碑。**【轉引 T8、T9】
5. **自感測在量產端最強的證據不在觸覺，在噴墨頭。** Epson 的 **Self-Diagnosing Nozzle Health System** 讓壓電元件自己產生電壓、**在毫秒內完成自我診斷**；同一顆壓電元件**每秒射出約 50,000 次**。這是「同一片壓電同時致動與感測」唯一有超高循環數＋量產良率背書的案例，也是 Epson 得以把「印字頭與機器同壽命、不可更換」做成商業模式的支柱。**這個案例應該成為客戶對外說服力的主軸。**【轉引 T20、T21】
6. **但自感測在最嚴苛的應用中被明確否決，這是必須正視的反面證據。** 頂級奈米定位廠 Physik Instrumente 現役產品仍採**外部電容式 direct metrology**；原理性缺陷是橋式自感測電路的電容失衡——壓電體的 C₀ 隨溫度與偏壓漂移，橋一失衡就把致動訊號洩進感測路徑，造成訊號污染甚至閉迴路不穩。**這決定了自感測的可售賣精度等級：夠做「有沒有、大概多大」，不夠做「奈米級量測」。**【轉引 T22、T23】
7. **固態化的競爭不是只有壓電，而且對手不需要用鉛。** Bosch Sensortec 收購的 Arioso Systems 用 **NED（靜電式）**，宣稱**有效晶片面積 10 mm² 產生 >120 dB**；Ventiva 的離子風 **ICE** 已在筆電移除**約 25 W**、2025 年宣稱上看 **100 W**、噪音 **<15 dBA**、釋放最多 **40% 板面積**，並取得 Intel / Dell 關注。**「固態喇叭」與「無風扇散熱」這兩個 socket，壓電都不是唯一解法。**【轉引 T15、T31、T32、T33】
8. **RoHS 含鉛豁免有明確倒數計時，這是消費性應用的頭號商業風險。** 豁免 **7(c)-I 至 2027/6/30**；新設 **7(c)-VI（涵蓋 PZT/PTC 陶瓷）至 2027/12/31**，**2026/7/1 生效**；續期申請須**提前 18 個月**。喇叭、觸覺、微泵全部是消費/醫療品，全部用 PZT（含鉛）。**任何以歐盟消費市場為目標的 PZT 產品，必須把法規時程當作設計輸入，而不是合規部門的事。**【轉引 T36、T37、T38】

---

## 2. 現況：技術 / 產品 / 玩家

### 2.1 玩家地圖（僅列本輪有證據者；空白處即為缺口）

| 領域 | 玩家 / 產品 | 已驗證到的內容 | 缺口 |
|---|---|---|---|
| **觸覺驅動 IC（兩用核心）** | **Boréas Technologies**（加拿大）：BOS1901 / BOS1921 / BOS1931（CapDrive 單通道）、**BOS0614**（四通道，2022 發表，整合感測） | CapDrive「從致動器負載電容回收能量再利用」；BOS1901「同時觸發觸覺並感測按壓力」；宣稱 −90% 電流、10× vs 競品、20× vs LRA；台灣經 EDOM 代理 | **輸出電壓/電流、靜態功耗、封裝、單價、募資、專利範圍全部查無** |
| **觸覺致動器（元件端）** | **TDK PowerHap** | 內建感測、≤25 N 壓力偵測、1 Hz–1000 Hz 激振 | 型號規格、價格查無 |
| **觸覺系統整合** | **Synaptics**（與 Boréas 合作壓電觸控板）、車用 HMI（2020 新聞稿） | 大廠採用訊號成立 | **是否已有量產機種、滲透率查無** |
| **表面觸感調變** | **Tanvas**（TanvasTouch） | 技術存在 | **驅動電壓查無**；其機制為**電黏附**，非超音波摩擦調變 |
| **壓電 MEMS 喇叭** | **xMEMS Cypress** | 「全球首款用於無線耳機的全音域 MEMS 喇叭」量產就緒；低頻 SPL **>130 dB**；**sound-from-ultrasound**——同一 MEMS 同時做超音波載波的調變與解調 | **驅動電壓、功耗、單價、客戶、量產時程查無** |
| **壓電 MEMS 閥** | **xMEMS Skyline DynamicVent** | 固態 MEMS 閥；開孔等效 **1.1 mm²**（雙顆 1.3 mm²）；100 Hz 衰減 **up to 25 dB**；同一壓電結構既是聲學阻抗元件又是致動器 | 規格細節查無 |
| **壓電 MEMS 氣泵** | **xMEMS Sycamore / XMC-2400** | **本輪完全查無** | 全部 |
| **PMUT 收發共用** | **Qualcomm 3D Sonic**（24×8 PMUT，180 nm CMOS 綁定） | 同一批 PMUT 由 TX 切 RX 做 pulse-echo 成像 | — |
| **壓電微泵** | **Bartels Mikrotechnik mp6 / BP7** | 壽命 **>5,000 h**；無機械閥件、unibody；連續共振驅動 | 流量、驅動電壓、價格查無 |
| **壓電微泵（碟式）** | **TTP Ventus / Lee Ventus Disc Pump** | **查無**（`04` 明記 MTBF 查無） | 全部 |
| **靜電式微喇叭（競爭）** | **Bosch Sensortec / Arioso Systems（NED）** | 有效晶片面積 **10 mm² → >120 dB**；強調低電容省電 | **驅動電壓查無** |
| **離子風散熱（競爭）** | **Ventiva ICE / ICE9** | 筆電移除 ≈25 W、2025 宣稱上看 100 W、2027 目標 40 W TDP 機種、**<15 dBA**、釋放 **40%** 板面積、Intel/Dell 關注 | 電極電壓、電流、融資查無 |
| **自感測量產先例（跨域）** | **Epson Micro Piezo / PrecisionCore** | 壓電元件自產電壓、**毫秒內自我診斷**；每元件 **≈50,000 次/秒**；年產 >1,500 萬台、印字頭與機器同壽命 | — |

### 2.2 這個領域為什麼是「兩用元件」的天然入口

三個結構性理由，依重要性排序：

**(a) 壓電體已經在 BOM 裡了，成本論證的起跑點完全不同。** 客戶排除「壓電取代電感做 DC-DC」的理由是「壓電單價高、打不過磁性元件」。但在壓電喇叭 / 觸覺 / 微泵裡，**壓電陶瓷的成本已經被產品定義吃掉了**——它是這個產品之所以存在的原因。此時「多用一個功能」的邊際成本接近零（多一組電極、多一段陶瓷、多一個 IC 模式），而**省下來的是外掛元件的整顆 BOM**。這是本專案裡唯一一個「成本算式從一開始就對客戶有利」的應用域。

**(b) 這些應用的驅動電壓天然需要升壓，升壓路徑本身就是兩用元件的插入點。** 壓電致動要幾十到上百伏，電池只有 3.7 V。目前的解法是「電感式 boost → 高壓軌 → H-bridge → 壓電片」。**兩用元件的野心是把 boost 也交給陶瓷。** 這條路已有明確的量產先例證明可行：TDK **CeraPlas** 用 **12–24 Vpp、50 kHz** 輸入，在輸出端**直接點燃冷電漿**，元件表面溫度 **<50 °C**，且官方明述「無需針對高壓做特別的安全防護措施即可整合」——**因為高壓從未離開陶瓷體**。【轉引 T43】把同樣的邏輯搬到 MEMS 喇叭或微泵：**如果升壓段與致動段是同一顆陶瓷，那條高壓軌就不存在，爬電距離、高壓佈線、高壓連接器、IEC 62368-1 的 DTI ≥ 0.4 mm 全部消失。**【轉引 T44】

**(c) 這些應用大多在「拉不出線」或「放不下感測器」的地方。** 密封耳機、IP68 手機、貼片式輸液泵、體內導管——**外掛一顆流量計或壓力感測器不是貴，是物理上放不進去**。自感測在這裡不是「省一顆料」，是「有沒有這個功能」的差別。這是本領域最可能長出真新能力的地方，也是第 4 節的重點。

---

## 3. 關鍵數字表

**所有數字皆為【轉引】，未經一手驗證。「宣稱」欄標示廠商宣稱 vs 量測值。**

| 項目 | 數字 | 性質 | 來源 |
|---|---|---|---|
| Boréas CapDrive vs LRA | 省電 **20×** | 廠商宣稱 | T1 |
| Boréas CapDrive vs 競品壓電 IC | 效率好 **10×** | 廠商宣稱 | T1、T4 |
| Boréas 能量回收效益 | 整體**電流消耗**最多降 **90%** | 廠商宣稱；**非轉換效率** | T4 |
| 被動電荷回收物理上限 | **約 50%**（2 二極體＋1 電阻，電阻需 >> 二極體順向電阻） | 學術；量測 | T25、T26 |
| 主動 LC 電荷回收實測 | **電路能量損耗** −49% / −50% / −55% @ 40 / 80 / 120 Hz | 學術；量測。**注意是損耗降低不是效率** | T25 |
| TDK PowerHap 壓力偵測 | **≤25 N**；激振 **1 Hz–1000 Hz** | 規格 | T12 |
| xMEMS Cypress 低頻 SPL | **>130 dB** | 廠商宣稱 | T13 |
| xMEMS Skyline 開孔/衰減 | 等效開孔 **1.1 mm²**（雙顆 1.3 mm²）；100 Hz 衰減 **up to 25 dB** | 廠商宣稱 | T14 |
| Bosch/Arioso NED 微喇叭（競爭） | 有效晶片面積 **10 mm² → >120 dB** | 廠商宣稱 | T15 |
| Qualcomm 3D Sonic PMUT | **24 × 8** 陣列；180 nm CMOS | 拆解報告 | T16 |
| Bartels mp6 / BP7 壽命 | **>5,000 h** | 規格 | T18、T19 |
| Epson 壓電元件射出率 | **≈50,000 次/秒/元件** | 官方 | T20 |
| Epson 自診斷反應時間 | **毫秒級** | 官方 | T21 |
| PI PICMA 多層致動器壽命 | **10¹¹ 次循環零失效，保有 96% 原始位移**（NASA 火星任務測試） | 量測 | T40、T41 |
| 陶瓷諧振器頻率老化極限 | **0.03 %/decade**（即使最佳材料＋強制老化） | 量測 | T42 |
| Ventiva ICE 散熱（競爭） | 筆電 **≈25 W**；2025 宣稱上看 **100 W**；**<15 dBA**；釋放 **40%** 板面積 | 廠商宣稱 | T31、T32、T33 |
| TDK CeraPlas 升壓 | **12–24 Vpp / 50 kHz 輸入 → 直接點燃冷電漿**，表面 **<50 °C** | 官方 | T43 |
| IEC 62368-1 加強絕緣 DTI | **≥ 0.4 mm**（峰值工作電壓 >71 V） | 標準 | T44 |
| RoHS 含鉛豁免期限 | 7(c)-I 至 **2027/6/30**；7(c)-VI（PZT/PTC）至 **2027/12/31**；**2026/7/1 生效**；續期須提前 **18 個月** | 法規 | T36、T37、T38 |
| MLCC 可聽噪音頻段（寄生風險） | **20 Hz–20 kHz**，陶瓷振動經焊點傳至 PCB，PCB 當振膜 | 綜述 | T39 |
| HEAD i.S18 網球拍（失敗案例） | 振動衰減 **50%** vs 一般球拍 **20%**；**已停產** | 廠商宣稱＋停產紀錄 | T27、T28、T29 |

**度量陷阱（請客戶特別注意）**：表中第 1–5 列最容易被混用。「損耗降低 50%」在原本效率 90% 的系統代表升到 95%；在原本效率 20% 的系統代表升到 33%。**Boréas 的「電流消耗降 90%」是系統層級平均電流（受工作週期與波形強烈影響），不能當轉換效率報給客戶或投資人。**

---

## 4. 「新能力型」應用機會

依「非替代性強度 × 商業可及性」排序。**每個機會都誠實標註是新能力還是更小/更薄/更便宜的替代品。**

### 4.1 機會 A：密封裝置內壓電氣泵/微泵的「自感測閉環」——免流量計的閉塞、氣泡與劑量偵測

- **新能力是什麼**：壓電膜片在泵水/泵氣的**同一個衝程內**，用自身的阻抗/電流波形反推腔內背壓與實際排量。於是可得到三個過去要外掛感測器才有的功能：**(i) 閉塞偵測**（管路堵了，背壓上升 → 諧振點與阻尼改變）；**(ii) 氣泡/空槽偵測**（工作流體從液體變氣體，負載質量驟降）；**(iii) 逐衝程劑量驗證**（每一下到底打出去多少）。
- **為什麼以前做不到**：在貼片式輸液泵、密封耳機、IP68 手機這類場景，**外掛壓力感測器或流量計不是成本問題，是物理上放不進去、也拉不出線**。而下游式壓力感測器在微升級流量下反應遲鈍。**只有致動器本身能在毫秒內知道自己推的是什麼。**
- **是否真的非替代性**：**是。** 這不是把外掛感測器做得更小，而是在「本來就不可能放感測器」的體積內取得資訊。判準很清楚：把外掛方案的體積縮到零也做不到逐衝程劑量驗證，因為外掛方案量的是下游穩態、不是這一下的功。
- **誰在做**：**跨域的量產先例極強但不在微泵**——Epson 噴墨頭的自診斷噴嘴健康系統就是這件事的完全體（壓電自產電壓、毫秒內診斷、支撐「印字頭與機器同壽命」的商業模式）【T20、T21】。**微泵領域本身：查無任何廠商主張此功能。** Bartels mp6/BP7 只查到壽命 >5,000 h 與 unibody 無閥設計【T18、T19】；TTP Ventus / Murata microblower **完全查無**。學術面有直接可用的方法論：以阻抗/諧振頻率變化做壓電自感測，論文明確指出**並聯電容負載會使串聯與並聯諧振頻率同時下降，且在並聯諧振附近最敏感**【T24】——這正好是「腔內負載變化→頻率漂移」的量測配方。
- **TRL**：**3–5**（原理與量測方法清楚、跨域量產先例存在、但本應用查無實作）。
- **市場訊號**：**間接但強。** 藥物輸送的閉塞警報是法規要求的安全功能【領域常識・未經檢索驗證；本輪查無 FDA 具體條文】，代表這個功能有人必須買、且願意為可靠度付錢。
- **技術難點**：(i) 高壓驅動與 mV 級感測訊號共用同一對電極的隔離與時序切換；(ii) 感測基準會隨老化漂移——陶瓷諧振器頻率老化極限 **0.03%/decade** 且諧振頻率**持續上升**【T42】，因此必須設計自校正基準（例如每次上電做一次已知空載掃頻）；(iii) 流體負載的映射高度非線性，且黏度隨溫度變化；(iv) 醫材路徑的驗證成本遠高於消費品。

### 4.2 機會 B：全螢幕/全表面的「定位式」觸覺——一片面板上多點獨立觸感

- **新能力是什麼**：面板上佈多顆壓電致動器，每顆同時是**致動器＋按壓力感測器**，於是可以做到「**你按哪裡、哪裡震**」，而不是整台裝置一起嗡。同時因為感測與致動同體，系統知道**你按了多重**，可以做力度相依的觸感曲線。
- **為什麼以前做不到**：ERM / LRA 是**整機共振體**，物理上無法定位——它們震的是整個機殼。要定位就得放很多顆 LRA，而 LRA 有線圈與磁鐵，體積與厚度無法在面板下陣列化。**壓電片可以做到零點幾毫米厚並貼滿整片。**
- **是否真的非替代性**：**是（就「定位」這一項而言）。** 「更省電的震動」是替代品（見 4.4，應降權），但「多點獨立定位觸感」是 LRA 架構做不到的能力。判準：把 LRA 做到無限小無限便宜，仍然做不到，因為它的振動會傳遍機殼。
- **誰在做**：**已經有人在賣，客戶會是追隨者。** Boréas BOS0614 是**四通道整合感測**驅動 IC（2022 發表）【T5】，四通道正是為了陣列化；Synaptics 與 Boréas 合作壓電觸控板【T6】；車用 HMI 2020 年即有採用新聞稿【T7】；TDK PowerHap 元件端內建 ≤25 N 感測【T12】。**Cirrus Logic 也已進場**：專利 **US12396367B2**「用矽主動電感驅動壓電換能器（觸覺）」【T45，URL 未驗證】——一家音訊 IC 大廠佈局壓電觸覺驅動，是市場即將擁擠的訊號。
- **TRL**：**8–9**（有商品、有大廠合作）。
- **市場訊號**：**最強**，但也代表**價格戰最近**。
- **技術難點**：(i) 陣列化後的**跨通道機械串音**——鄰近致動器的振動會被彼此感測到，會污染力量讀值；(ii) 面板的機械阻抗隨貼合、溫度、使用者握持方式改變，感測基準漂移；(iii) 這是 IC 與系統整合的競爭，不是陶瓷的競爭——**客戶若強項在陶瓷，這條路的價值捕獲點不在他手上**。

### 4.3 機會 C：升壓段與致動段做在同一顆陶瓷體內——讓高壓永遠不離開陶瓷

- **新能力是什麼**：一顆陶瓷體，一段做 Rosen 型升壓諧振器、一段做喇叭/泵/觸覺致動器，兩段機械耦合。**外部只有低壓（十幾伏）進出，系統裡不存在高壓軌。**
- **為什麼以前做不到**：傳統架構必須有「電感式 boost → 高壓軌 → H-bridge → 壓電片」。高壓軌一旦存在，就要付出爬電距離、高壓佈線、高壓連接器、以及 **IEC 62368-1 加強絕緣 DTI ≥ 0.4 mm** 的代價【T44】。在 1 mm 厚的耳機或貼片泵裡，這些代價可能直接否決產品。
- **是否真的非替代性**：**半到是，取決於怎麼定義。** 若只看「產生高壓」，這是更薄的替代品（應降權）。但若看「**在一個沒有高壓軌的系統裡取得高壓致動**」，這是架構層級的新能力——**因為它消滅的不是一顆電感，是整個高壓子系統與其安規負擔**。同目錄 `07` 對 CeraPlas 的判讀完全一致：「CeraPlas 的真正新能力不是『省掉電感』，而是**省掉整個高壓子系統**」【轉引自 `07`，依據 T43】。
- **誰在做**：**在 A4 領域查無任何人。** 唯一的物理可行性證據是 TDK CeraPlas——12–24 Vpp 輸入直接在輸出端點燃冷電漿、表面 <50 °C、官方明述無需特殊高壓防護即可整合【T43】。**CeraPlas 證明了「高壓不離開陶瓷」這件事可以量產**，但它的負載是電漿不是致動器。**「PT 諧振腔 ＋ 致動負載的聯合諧振共設計」本輪查無任何文獻或專利**（同目錄 `11` 也把這列為最有價值的待查 IP 白空間）。
- **TRL**：**2–3**（概念清楚、鄰域有量產先例、本身無公開實作）。
- **市場訊號**：**目前為零**（沒有人在賣，也沒有人在說要買）。這是純技術推動型機會，風險最高、IP 空間也最大。
- **技術難點（這幾條可能致命，必須先驗）**：
  1. **頻率尺度落差**。PT 機械諧振在數十至數百 kHz，而喇叭要 20 Hz–20 kHz、微泵要數十 Hz—數 kHz、觸覺要 1 Hz–1000 Hz【T12】。**單一諧振腔的敘事在物理上站不住**，必須是「高頻諧振腔 ＋ 低頻包絡調變」，而這個架構的往返效率**查無任何數字**。
  2. **頻寬天花板已被明確判死**。體聲波 PT 因 f < 數十 MHz 且 Qm 高，**固有頻寬僅數十 kHz**，該文獻是在論證「不足以驅動 WBG 閘極」時提出的【T48】。對音訊而言數十 kHz 剛好夠，對高保真而言相位響應是否可用**查無**。
  3. **負載變動 → 增益崩塌**。PT 輸出阻抗高，增益隨負載變化劇烈；而致動器負載會隨溫度、貼合、使用者手指按壓而變。**必須有主動頻率/相位追蹤，這會吃掉一部分「高整合度」的效率與成本優勢。**
  4. **寄生發聲**。PT 本身會機械共振發聲；陶瓷振動可經焊點傳至 PCB、PCB 當振膜，可聽頻段 **20 Hz–20 kHz**【T39】。**把這種元件放進喇叭或「靜音」產品裡是諷刺性風險**，必須確認基頻在超音波且無可聞次諧波。

### 4.4 機會 D（明確降權）：更省電的觸覺 / 更薄的喇叭

- **新能力是什麼**：沒有。這是**更小/更薄/更省電的替代品**，依任務規則必須標明並降低權重。
- 具體而言：CapDrive 宣稱比 LRA 省電 20×【T1】——這是替代既有 LRA socket；xMEMS Cypress 的「全音域 MEMS 喇叭」【T13】對耳機而言是替代動圈單體。**這些是好生意，但不是客戶要的東西。**
- **唯一值得保留的例外**：xMEMS Cypress 的 **sound-from-ultrasound**——「同一 MEMS 同時做超音波載波的調變與解調」【T13】，這在機制上確實是動圈喇叭做不到的（動圈沒有超音波載波這回事）。**但本輪查無其驅動電壓、效率、失真與功耗**，無法判斷這是真新能力還是行銷敘事。**列為下一輪第一優先查證項。**
- **降權後的建議**：這條路**只能當現金流，不能當立項理由**。

### 4.5 機會 E（低優先，但成本論證最好）：氣泵/散熱的固態化

- **新能力**：無移動件、無軸承磨耗、任意姿態可運作、可做在密封殼內。
- **是否非替代性**：**半。** 「無風扇散熱」本身是新能力，但**壓電不是唯一解法，甚至可能不是贏家**。Ventiva 的離子風 ICE 已經在同一個 socket 裡跑得更前面：筆電移除 ≈25 W、2025 宣稱上看 100 W、**<15 dBA**、釋放 **40%** 板面積、Intel/Dell 關注【T31、T32、T33】。
- **誰在做**：xMEMS Sycamore / XMC-2400 **本輪完全查無**——這是本文件最大的單一缺口，因為它正是任務指派的核心標的之一。
- **建議**：**在補齊 xMEMS Sycamore 的實際規格前，不要對這條路下任何判斷。** 但先記住一件事：這個 socket 已經有一個資金充足、已展示產品、已有 Intel/Dell 關注的非壓電對手。

---

## 5. 反面證據、失敗案例與物理上限

**這一節請客戶逐條讀，它們構成立項的否決清單。**

1. **自感測被最嚴苛的市場明確拒絕。** Physik Instrumente 的頂級奈米定位產品仍使用**外部電容式 direct metrology**，而非自感測【T23】。原理性缺陷已被綜述論文明確描述：橋式自感測的電容失衡——壓電體 C₀ 隨溫度與偏壓漂移，橋一失衡就把致動訊號洩進感測路徑，造成訊號污染與閉迴路不穩【T22】。**這不是工程細節，是原理缺陷。** 對客戶的意涵：**自感測可以賣「有/無、大概多大、有沒有異常」，不能賣「精密量測」。** 4.1 的閉塞偵測落在可賣的那一邊，這是它值得做的原因；4.2 的「按壓力精確讀值」落在灰色地帶。

2. **消費性壓電兩用元件已經失敗過一次，而且死因正是客戶最擔心的成本。** HEAD Intelligence 網球拍是「self-powered piezoelectric damping」少數真正大量上市的消費品——有專利（US6974397B2）、有臨床研究、有 **50% vs 一般球拍 20%** 的衰減宣稱，**結果停產**【T27、T28、T29】。這直接命中「壓電元件單價高，在消費品上打不過純機械/黏彈性方案」的疑慮。

3. **壓電元件的商業命運會被單一應用綁死。** CCFL 背光時代，壓電變壓器一度佔 **25–30%** 的 CCFL 背光電路，客戶含 Toshiba/NEC/Hitachi/Panasonic/Apple；LED 取代 CCFL 後，**整條供應鏈（含專用 IC）停產**【T30】。教訓：**若客戶的兩用元件只服務單一 socket，那個 socket 的技術世代交替就是它的死期。** 這是「一定要有橫向遷移能力」的實證理由。

4. **能量回收有硬性物理上限，且商業宣稱與學術實測差一個數量級的度量。** 被動回收（2 二極體＋1 電阻）上限**約 50%**【T25、T26】；主動 LC 回收的實測是**損耗降 49–55%**【T25】。Boréas 的 **−90% 電流消耗**是系統平均電流、應用相依的廠商宣稱【T4】。**如果客戶的立項簡報寫「能量回收可提升效率 90%」，那是錯的，會在盡職調查中被抓出來。**

5. **對手不需要壓電，也不需要含鉛。** Bosch/Arioso 的 NED 靜電式微喇叭宣稱 **10 mm² → >120 dB**【T15】；Ventiva 的離子風散熱已進入 Intel/Dell 視野【T31–T33】。**在「固態喇叭」與「無風扇散熱」兩個最誘人的 socket，壓電都面對不含鉛、不需要高壓陶瓷的替代技術。**

6. **RoHS 含鉛豁免的倒數計時是消費性應用的結構性風險。** 7(c)-I 至 **2027/6/30**、新設 7(c)-VI（PZT/PTC 陶瓷）至 **2027/12/31**、**2026/7/1 生效**、續期須提前 **18 個月**【T36、T37、T38】。**今天是 2026 年 7 月**——這代表下一次續期的申請窗口就在眼前。**任何以 3–5 年產品週期規劃的 PZT 消費品，都必須把「豁免若不續期」寫進風險登錄。**

7. **微泵的壽命規格數量級偏低。** Bartels mp6/BP7 壽命 **>5,000 h**【T18、T19】——連續運轉約 7 個月。對比多層致動器在**準靜態**工況下可達 **10¹¹ 次循環零失效、保有 96% 位移**【T40、T41】，差距說明：**限制微泵壽命的不是陶瓷本身，是流體介面、膜片疲勞與封裝**。客戶若要進醫材或長生命週期產品，**壽命是要自己解決的題目，不是買陶瓷就送的**。

8. **感測基準會自己漂走。** 陶瓷諧振器頻率老化即使用最好的材料＋強制老化製程仍受限於 **0.03%/decade**，且諧振頻率隨老化**持續上升**【T42】。任何靠共振點做自感測的方案，**必須內建自校正流程，否則出廠校正的基準在幾年後就沒有意義**。

9. **市場已經有先行者，且不只一家。** Boréas 自 BOS1901 起已建立「唯一同時致動＋感測」的定位【T2】、有四通道版本【T5】、有 Synaptics 合作【T6】、有車用 HMI 採用【T7】、在台灣有代理【T8、T9】；Cirrus Logic 已有壓電觸覺驅動專利【T45，URL 未驗證】。**「兩用元件」在觸覺這個切入點上不是白空間，是已經有人插旗的地。** 客戶的差異化必須在陶瓷側（4.3）或在別人沒做的應用側（4.1），不能在 IC 側正面對打。

10. **本文件本身是一條反面證據。** 我在被指派的十幾個具體標的中，**成功查證的不到三分之一**，其中最關鍵的 xMEMS Sycamore 氣泵、TTP Ventus、Murata microblower、Boréas 實際規格與募資**全部查無**。**在這些缺口補上之前，本文件不足以支撐任何投資決策。**

---

## 6. 未解問題（給下一輪研究，已按優先序排列並附建議查詢字串）

1. **xMEMS Sycamore / XMC-2400 的實際規格是什麼？**（風量 CFM、背壓、功耗、驅動電壓、厚度、噪音 dBA、量產狀態、客戶）——這是任務指派的核心標的，本輪完全空白，且它決定 4.5 是否成立。建議查詢：`xMEMS Sycamore XMC-2400 datasheet airflow`、`xMEMS solid-state fan CFM dBA power consumption`、`xMEMS Sycamore vs Ventiva ICE comparison`。
2. **壓電 MEMS 喇叭與微泵的驅動電壓與升壓架構是什麼？**（這正是 4.3 的插入點，沒有這個數字就無法評估「陶瓷內建升壓」值不值得做）。建議查詢：`xMEMS Cypress drive voltage boost converter`、`piezoMEMS speaker bias voltage requirement`、`Murata microblower MZB drive voltage`。
3. **Boréas 的實際輸出電壓/電流、靜態功耗、單價、募資輪次，以及 CapDrive 的專利範圍。** 若「從致動器負載電容回收能量」的核心手法已被專利覆蓋，客戶自研會直接撞牆。建議以 **Boréas Technologies 為受讓人**做專利檢索，並向 **EDOM（益登）索取 BOS1901/BOS1921 評估板與報價**——這一步不需要搜尋額度，直接打電話即可，**建議立即執行**。
4. **微泵自感測（4.1）有沒有已上市產品或 FDA 先例？** 特別是輸液泵的閉塞警報是否已有以致動器自感測實現的案例。建議查詢：`piezoelectric micropump self-sensing occlusion detection`、`infusion pump occlusion alarm piezoelectric actuator sensing`、`TTP Ventus disc pump sensing feedback`。
5. **「PT 諧振腔 ＋ 致動器負載聯合諧振共設計」到底有沒有人做過？**（4.3 的存亡問題）。建議查詢：`piezoelectric transformer integrated actuator monolithic`、`Rosen type transformer driving piezoelectric actuator same ceramic`，並做專利檢索 `"piezoelectric transformer" AND ("actuator" OR "speaker" OR "pump") AND monolithic`。**若真的空白，這是本專案最有價值的 IP 機會；若有人做過且失敗，必須知道原因。**
6. **TDK PiezoListen、Murata 壓電喇叭、display-as-speaker 的規格與市場地位**（整項未查）。
7. **超音波摩擦調變 vs 電黏附**：本輪只查到 Tanvas 的電黏附路線【T34】，且已有可靠度反面證據（電黏附觸控面板的優先汙染機制研究【T35】）。超音波摩擦調變**完全未查**，需補。
8. **本領域的市場規模、ASP、出貨量全部查無。** 注意同目錄 `02` 對壓電變壓器市場報告的警告：不同機構的數字**互相矛盾達 3 倍**——因此下一輪取得的任何市調數字都應交叉比對後才引用。

---

## 7. 來源清單

**重要說明**：以下 URL **全部轉引自本專案同目錄的既有 dossier**，我本輪**未親自開啟任何一個**（WebFetch 被封鎖、WebSearch 額度耗盡）。標題與說明為轉引時的描述。

| # | 標題 | URL | 一句話說明 |
|---|---|---|---|
| T1 | CapDrive™ Piezo Driver — Boréas Technologies | https://www.boreas.ca/pages/capdrive-technology | CapDrive 從致動器內部負載電容回收能量再利用；比 LRA 省電 20×、比競品壓電 IC 省電 10× 的廠商宣稱 |
| T2 | BOS1901 Piezo Haptic Driver — Boréas | https://www.boreas.ca/products/bos1901-piezo-haptic-driver | 「市場上唯一同時觸發觸覺並感測按壓力的壓電驅動 IC」 |
| T3 | CapDrive® Ultra-Low Power Piezo Driver (BOS1931) — Boréas | https://www.boreas.ca/products/capdrive%C2%AE-ultra-low-power-piezo-driver-bos1931 | BOS1931 產品頁 |
| T4 | The 6 Elements of a Quality Piezo Driver — Boréas blog | https://pages.boreas.ca/blog/piezo-haptics/6-most-important-elements-to-look-for-in-a-piezo-driver | 「能量回收可使壓電系統整體電流消耗降低最多 90%」的出處 |
| T5 | Boréas 四通道整合感測驅動 IC 新聞稿（BOS0614, 2022） | https://www.prnewswire.com/news-releases/boreas-technologies-announces-four-channel-haptic-driver-with-integrated-sensing-301563047.html | 陣列化＋整合感測的現貨選項 |
| T6 | Synaptics × Boréas 壓電觸控板合作新聞稿 | https://www.synaptics.com/company/news/synaptics-partners-boreas-technologies-deliver-high-performance-piezo-haptic-trackpads | 大廠採用訊號 |
| T7 | Boréas Piezo Driver Chip Advances Realistic Haptic Feedback in Automotive HMIs (2020) | https://www.globenewswire.com/news-release/2020/01/07/1967204/0/en/Bor%C3%A9as-Technologies-Piezo-Driver-Chip-Advances-Realistic-Haptic-Feedback-in-Automotive-HMIs.html | 車用 HMI 採用訊號 |
| T8 | BOS1921 — CapDrive® Piezo Driver（EDOM 益登，台灣代理） | https://www.edomtech.com/en/product-detail/bos1921-capdrive-piezo-driver/ | **台灣取樣管道** |
| T9 | BOS1901 — Piezo Haptic Driver（EDOM 益登） | https://www.edomtech.com/en/product-detail/bos1901-piezo-haptic-driver/ | 同上 |
| T10 | BOS1931 High-Efficiency Piezo Driver（Mouser） | https://www.mouser.com/new/boreas-technologies/boreas-bos1931-piezo-haptic-driver/ | 通路商頁，可用於詢價 |
| T11 | Boréas Technologies 官網 | https://www.boreas.ca/ | 產品線總覽 |
| T12 | TDK PowerHap Actuators | https://product.tdk.com/en/products/sw_piezo/haptic/powerhap/index.html | 致動器內建感測、≤25 N 壓力偵測、1 Hz–1000 Hz 激振 |
| T13 | xMEMS Cypress 量產就緒新聞稿 | https://xmems.com/press-release/xmems-announces-mass-production-readiness-of-cypress-the-worlds-first-full-range-mems-speaker-for-wireless-earbuds/ | sound-from-ultrasound 調變/解調同體、低頻 SPL >130 dB |
| T14 | xMEMS Skyline 固態 MEMS DynamicVent（audioXpress） | https://audioxpress.com/news/xmems-announces-world-s-first-solid-state-mems-dynamicvent-enabling-active-ambient-control-for-next-generation-tws-and-hearing-aids | 等效開孔 1.1 mm²、100 Hz 衰減 up to 25 dB |
| T15 | Bosch Sensortec Acquires MEMS Microspeaker Innovator Arioso Systems（audioXpress） | https://audioxpress.com/news/bosch-sensortec-acquires-mems-microspeaker-innovator-arioso-systems | **競爭技術**：NED 靜電式，10 mm² 有效面積 → >120 dB；驅動電壓查無 |
| T16 | Qualcomm 3D Sonic Sensor Fingerprint — Yole 樣本報告 | https://medias.yolegroup.com/uploads/2019/07/SP19465-YOLE_Qualcomm-3D-Sonic-Sensor-Fingerprint_Sample.pdf | 24×8 PMUT 陣列、180 nm CMOS、TX/RX 同電極切換 |
| T17 | Thin-film PMUTs: a review of over 40 years of research（Microsystems & Nanoengineering 2023） | https://www.nature.com/articles/s41378-023-00555-7 | PMUT 收發共用元件的技術總覽 |
| T18 | Datasheet mp6 micropumps series（Bartels Mikrotechnik） | https://bartels-mikrotechnik.de/wp-content/uploads/2025/06/Datasheet-mp6-series.pdf | mp6 壽命 >5,000 h |
| T19 | The Bartels Pump BP7（Bartels Mikrotechnik） | https://bartels-mikrotechnik.de/product/the-bartels-pump-bp7-piezo-pump/ | BP7 壽命 5,000 h、無移動閥件、unibody |
| T20 | Micro Piezo Inkjet Technology / PrecisionCore（Epson） | https://corporate.epson/en/technology/overview/printer-inkjet/micro-piezo.html | 每壓電元件每秒射出約 50,000 次；年產 >1,500 萬台、印字頭與機器同壽命 |
| T21 | Self-Diagnosing Nozzle Health System（Epson） | https://corporate.epson/en/technology/search-by-products/printer-inkjet/nozzle-self-diagnosis.html | **自感測致動器的量產實證**：壓電元件產生電壓、毫秒內自我診斷 |
| T22 | An Overview of Piezoelectric Self-Sensing Actuation for Nanopositioning Applications（IEEE 8889413） | https://ieeexplore.ieee.org/document/8889413/ | 自感測電路分類（橋式/觀測器）＋電容漂移導致訊號污染與閉迴路不穩 |
| T23 | Physik Instrumente — Capacitive Sensors | https://www.physikinstrumente.com/en/expertise/technology/sensor-technologies/capacitive-sensors | **最強反面證據**：頂級奈米定位仍用外部電容式 direct metrology |
| T24 | Simultaneous quasi-static displacement and force self-sensing of piezoelectric actuators by detecting impedance（Sensors & Actuators A） | https://www.sciencedirect.com/science/article/abs/pii/S0924424717317478 | 以阻抗/諧振頻率變化做自感測；並聯電容負載使串並聯諧振同時下降、並聯諧振附近最敏感（4.1 的量測配方） |
| T25 | Power-Efficient Driver Circuit for Piezo Electric Actuator with Passive Charge Recovery（MDPI Energies 13(11):2866） | https://doi.org/10.3390/en13112866 | 2 二極體＋1 電阻可回收約一半電荷；主動 LC 回收損耗降 49–55% |
| T26 | Charge-recovery circuit maximizes piezoelectric-actuator efficiency（EDN） | https://www.edn.com/charge-recovery-circuit-maximizes-piezoelectric-actuator-efficiency/ | 工程期刊版的電荷回收電路說明 |
| T27 | An Extended Study … Tennis Rackets with Active Damping Technology on Tennis Elbow | https://www.researchgate.net/publication/226285635_An_Extended_Study_Investigating_the_Effects_of_Tennis_Rackets_with_Active_Damping_Technology_on_the_Symptoms_of_Tennis_Elbow | HEAD i.S18/i.X16/Protector OS 型號與停產說明 |
| T28 | US6974397B2 — Racket with self-powered piezoelectric damping system | https://patents.google.com/patent/US6974397B2/en | HEAD 自供電壓電阻尼專利 |
| T29 | Piezoelectric rackets add professional oomph（EE Times） | https://www.eetimes.com/piezoelectric-rackets-add-professional-oomph/ | 振動衰減 50% vs 一般球拍 20% 的宣稱來源 |
| T30 | Piezoelectric Transformers: An Historical Review（MDPI Actuators 5(2):12） | https://www.mdpi.com/2076-0825/5/2/12 | CCFL 時代 25–30% 市佔、客戶名單、LED 取代後產業崩解 |
| T31 | Ventiva 技術頁 | https://ventiva.com/technology/ | **競爭技術**：ICE 離子風固態散熱 |
| T32 | Ventiva Unveils Intelligent Air Cooling Solution… Up To 100 Watts（BusinessWire, 2025-05-18） | https://www.businesswire.com/news/home/20250518248653/en/Ventiva-Unveils-Intelligent-Air-Cooling-Solution-for-Electronics-that-Delivers-Up-To-100-Watts | 2025 宣稱上看 100 W |
| T33 | Ventiva's fanless laptop cooler wins Intel and Dell over（PCWorld） | https://www.pcworld.com/article/2570821/ventivas-fanless-laptop-cooler-wins-intel-and-dell-over/ | 筆電移除 ≈25 W、<15 dBA、釋放 40% 板面積、Intel/Dell 關注 |
| T34 | What is TanvasTouch（Tanvas） | https://tanvas.co/blog/what-is-tanvastouch | 表面觸感調變（**電黏附**，非超音波摩擦調變）；驅動電壓查無 |
| T35 | Preferential Contamination in Electroadhesive Touchscreens（Advanced Materials Technologies 2023） | https://advanced.onlinelibrary.wiley.com/doi/full/10.1002/admt.202300213 | 電黏附界面的汙染機制——表面觸覺的可靠度反面證據 |
| T36 | EU RoHS Directive Update: Comprehensive Refinement of Lead Exemption Clauses（CIRS） | https://www.cirs-group.com/en/chemicals/eu-rohs-directive-update-comprehensive-refinement-of-lead-exemption-clauses | 7(c)-I 至 2027/6/30；新設 7(c)-VI（PZT/PTC）至 2027/12/31；2026/7/1 生效 |
| T37 | Final Delegated Directives for Key RoHS Lead Exemptions Adopted（Assent） | https://www.assent.com/blog/draft-expiry-dates-for-key-rohs-lead-exemptions-published/ | 續期須提前 18 個月申請 |
| T38 | RoHS Exemption for Lead Updates（APC International） | https://www.americanpiezo.com/blog/rohs-exemption-for-lead-update/ | 壓電廠商角度的豁免說明 |
| T39 | "Singing" Multilayer Ceramic Capacitors and Mitigation Methods—A Review（PMC） | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9147252/ | 陶瓷振動經焊點傳至 PCB、PCB 當振膜；可聽頻段 20 Hz–20 kHz（寄生發聲風險） |
| T40 | Reliability & Lifetime of Multilayer Piezo Actuators（PI 白皮書 PDF） | https://www.pi-usa.us/fileadmin/user_upload/pi_us/files/catalogs/Piezo_Actuator_Lifetime_Test_Reliability_Results.pdf | PI 官方壽命測試結果 |
| T41 | Piezo actuators: 100 billion cycles without failures or loss in performance | https://www.engineerlive.com/content/piezo-actuators-100-billion-cycles-without-failures-or-loss-performance | NASA 測試 10¹¹ 次零失效、保有 96% 位移 |
| T42 | Aging effects on resonance frequency of Pb(Ti₀.₅₂Zr₀.₄₈)O₃ piezoelectric ceramics（Springer） | https://link.springer.com/article/10.1007/s42114-021-00239-8 | 老化使諧振頻率上升；自感測基準漂移的物理依據 |
| T43 | TDK Electronics — Cold plasma from a single component（CeraPlas） | https://www.tdk-electronics.tdk.com/en/373562/tech-library/articles/applications-cases/applications-cases/cold-plasma-from-a-single-component/1109546 | 12–24 Vpp / 50 kHz 輸入直接點燃冷電漿、表面 <50 °C、無需特殊高壓防護即可整合（4.3 的可行性依據） |
| T44 | Distance Through Insulation: How Digital Isolators Meet…（TI SLLA563） | https://www.ti.com/lit/pdf/slla563 | IEC 62368-1 加強絕緣 DTI ≥ 0.4 mm |
| T45 | US12396367B2 — 用矽主動電感驅動壓電換能器（Cirrus Logic） | https://patents.google.com/patent/US12396367B2/en | **專利號轉引自本專案 `06-patents-power-and-dualuse.md`；URL 依 Google Patents 命名規則構造，本輪未驗證可達性。** 音訊 IC 大廠佈局壓電觸覺驅動的訊號 |
| T46 | CN111060232B — 壓電致動器輸出力自感知方法 | https://patents.google.com/patent/CN111060232B/en | 中國的自感測專利，力量自感知路線 |
| T47 | US10349818 — Adaptive control of a fiber scanner with piezoelectric sensing | https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/10349818 | 致動與感測同時進行；以電容橋分離驅動與位移訊號（受讓人未驗證） |
| T48 | Microwave-acoustic-based isolated gate driver for power electronics（Nature Comm. Eng.） | https://www.nature.com/articles/s44172-026-00681-w | 明確指出**體聲波壓電變壓器固有頻寬僅數十 kHz**——4.3 的頻寬天花板依據 |
| T49 | Steminc 多層壓電變壓器產品頁 | https://www.steminc.com/PZT/en/multilayer-piezo-transformer | 現貨多層 PT 供應（4.3 打樣可用） |
| T50 | Selecting nonlinear piezoelectricity for fully autonomous self-sensing SSDI（ScienceDirect） | https://www.sciencedirect.com/science/article/abs/pii/S0888327021002417 | 自感測開關阻尼的自主化——「開關時序本身即含結構資訊」的方法論 |
