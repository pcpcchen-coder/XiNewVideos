# 應用B2：聲學隔離、隔離式閘極驅動、穿金屬壁/穿密封艙供電與通訊

> 一句話結論：本領域中「隔離式閘極驅動電源」大體上只是磁性方案的替代品（磁性方案已做到 <1 pF / 12 kV / 5 W，壓電打不過），但有三塊是真正的「新能力」——**(1) 穿實心金屬壁不開孔的功率+資料傳輸**（已實測 50 W + 12.4 Mb/s 穿透 63.5 mm 鋼板，RF 因法拉第籠物理上不可能）、**(2) 極端溫度與全無磁環境下的隔離供電**（聲學元件已驗證 0.5 K–544 K，磁芯與光耦均不可用）、**(3) 中壓串聯堆疊所需的「數量級更低耦合電容（<0.1 pF）＋數十 kV 耐壓＋瓦級功率」三者兼具**，這個組合目前**無人達成**。

---

## 0. 研究方法與限制（誠實揭露）

- **WebFetch 在本環境被 egress policy 全面封鎖**（403），依指示未嘗試。
- **WebSearch 原計畫執行 25–35 次，但本 session 的搜尋額度（200 次上限）在我跑到第 12 次查詢時即被耗盡**（回傳 `this session has used its web search budget (200 of 200 WebSearch calls)`）。額度為 session 共用，非本 agent 獨佔。因此本 dossier 的證據基礎是 **12 次成功查詢**，遠低於任務要求，**廣度不足必須列入判讀**。
- 已完成的 12 次查詢主題：壓電變壓器隔離閘驅、Boles/Berkeley APEC 2025、ADI iCoupler CMTI、SiC/GaN CMTI 需求、穿金屬壁供電通訊總覽、Penn State/乾式貯存桶、軍方/潛艇艙壁、RPI Lawry、微波聲學隔離閘驅、10 kV SiC 閘驅電源耦合電容、IEC 60601 漏電流、電外科/ECG 隔離、穿金屬壁商用/ATEX 產品、穿金屬壁技術限制、Bristol/Warwick、壓電變壓器商業失敗史。
- **明確「查無 / 未查」的項目**（不得視為不存在，只是本輪沒證據）：
  - Berkeley Boles 團隊隔離式 PT 的**隔離耐壓值與一次/二次耦合電容 pF 數字**——搜尋摘要只給效率，**查無**。
  - 具名的**商用穿金屬壁 ATEX/IECEx 產品或公司**——**查無**（搜尋結果全是論文與專利）。
  - Bristol、Warwick、Georgia Tech 的專屬研究群——**查無**（搜尋引擎未回傳）。
  - TI 電容耦合隔離器、Silicon Labs、光耦的**具體 barrier capacitance pF 數字**——**未查到**（僅取得 ADI/Infineon 的 CMTI 數字）。
  - 井下/密封無穿線馬達與致動器（子題 d）——**額度用盡，完全未查**。
  - MMC 子模組輔助電源、固態斷路器閘驅電源、800V/1500V 電動車與儲能的隔離電源規格——**額度用盡，未查**。
  - 飛機油箱、真空腔體、密封電池組的穿壁感測——**未查**。
- 標註規則：凡僅出自單一搜尋摘要、無法交叉驗證者標「**未驗證**」；凡為我自行算術推導者標「**本文推導**」。**本文件未出現任何我編造的專利號、型號、公司名或數字。**

---

## 1. 結論摘要

1. **穿金屬壁的性能上限已被實測拉得很高**：RPI 的 Tristan Lawry 在 **2.5 英吋（63.5 mm）實心鋼塊**上，**同時且連續**傳輸 **50 W 功率與 12.4 Mb/s 資料**（RPI 官方新聞稿；註：sciencedaily 版本寫「megabytes per second」，RPI 版本寫「Mbps」，**兩者不一致，以 Mb/s 為保守解讀**）［來源 12,13,14］。這是本領域最強的「新能力」證據。
2. **其他穿壁實測數字**：1.045 MHz 載波、11 mm 鋼壁、**能量效率 60%、50 kb/s**；**40 mm 不鏽鋼板、15.7 W 穩壓 DC 輸出、整體效率 27.7%**；雙層鋼壁（15.97 mm + 10.92 mm，中間 88.3 mm 水柱）**4 Mb/s 且功率效率 >30%**；50 mm 鋁板已成功傳影像［來源 9,10］。
3. **RF 在此物理上不可行**：厚金屬壁形成法拉第籠，電磁無線傳輸「不切實際且極度無效率」；乾式貯存桶內「目前沒有任何內部感測系統」，因為既無長效電源、又不能拉線、也不能用 RF［來源 11］。這是教科書等級的 non-substitutional 論證。
4. **軍方/核能的價值錨點不是元件單價，是工程成本**：美國海軍為了在艦體/潛艇殼裝感測器必須鑽孔穿線，每個孔都增加漏水與結構失效風險；在已服役艦艇上加裝需進**乾塢或圍堰，耗時數月、花費數百萬美元**［來源 12,13］。壓電元件單價在這個對照組下**完全不是問題**——這是本領域相對於「取代電感」路線最關鍵的商業差異。
5. **中壓閘驅電源的門檻已被文獻明確量化**：10 kV SiC MOSFET 的隔離供電需**耐壓 >20 kV 且輸入-輸出耦合電容 <2 pF**；已達成值包括 **1.03 pF（2.5 W，用於 13.8 kV/100 kW 三相變流器）**、2.34 pF、2.6 pF；PCB 無芯變壓器方案為 >10 kV RMS / **5.85 pF**［來源 5,6,7］。**這代表磁性方案已經打到 1 pF 級，壓電若只做到 1–2 pF 就沒有新意。**
6. **聲學路線的耦合電容確實可以低一個數量級以上**：LiNbO₃ 上的**微波頻段 SAW 隔離閘驅**做到**隔離電容 0.032 pF**、隔離耐壓 2.75 kV、聲程 1.25 mm、開路 13.4 V / 短路 44.4 mA、驅動 GaN HEMT 開通時間 108.8 ns（與商用驅動器相當）、並在 buck 轉換器中驗證；**工作溫度 0.5 K 至 544 K**［來源 3,4］。**但功率只有百毫瓦級（本文推導：13.4 V × 44.4 mA 的最大匹配功率約 150 mW），耐壓也只有 2.75 kV。**
7. **位移電流算術（本文推導）**：dv/dt = 100 kV/µs 時，10 pF → 1 A 共模位移電流（此數字亦見於 CPES 文獻［來源 5］）；1 pF → 100 mA；**0.032 pF → 3.2 mA**。串聯堆疊 N 顆開關時共模電流線性累加，這正是「更低一個數量級」在中壓串聯/SST/MMC 才有價值、在單顆 1200 V 開關上沒價值的原因。
8. **傳統壓電變壓器（PT）的物理天花板已被明確指出**：工作頻率在數十 MHz 以下、機械 Q 約 1000，導致**固有頻寬只有數十 kHz**，「不足以支援 WBG 功率電子的先進閘極驅動」；且 PT 的電容性本質使瞬時功率遠大於平均功率，傳統驅動電路（尤其電感）過於笨重［來源 3］。**這是對「用 PT 做隔離閘驅」最致命的反面證據，而且是由推進聲學隔離的那篇論文自己講的。**
9. **磁性競品已經很強**：Coilcraft 的低電容變壓器產品線可做到 **5 W 輸出、12 kV 連續工作電壓、一次-二次耦合電容 <1 pF**，HTX7045C 的繞組間電容低至 **0.75 pF**［來源 2］。**任何壓電方案若定位在「更低電容的閘驅電源」，直接對手就是這個，不是電感。**
10. **醫療端門檻（本文推導 + 標準）**：IEC 60601-1 對 CF 型（心臟直接接觸，如 ECG 電極、導管）的病人漏電流限制為 **<10 µA**（AC+DC 合計）；2×MOPP 需 4000 VAC 隔離與 ≥8 mm 爬電距離［來源 15,16,17］。以 240 V/60 Hz 反推，**跨隔離障壁的總電容須 ≲100 pF**（本文推導）——這意味「1 pF 以下」對一般醫療電源其實是**過度規格**，壓電在此**沒有壓倒性新能力**，除非疊加「無磁」或「高功率+高 CMRR」條件。

---

## 2. 現況：技術 / 產品 / 玩家

### 2.1 隔離閘驅（既有商用方案，壓電的真正對手）
| 路線 | 代表 | 已知數字 |
|---|---|---|
| 磁耦（薄膜變壓器） | ADI iCoupler / ADuM4121 | ADuM4121 CMTI >150 kV/µs；iCoupler 資料表通常保證至少 25 kV/µs；量測報告 >100 kV/µs［來源 18,19］ |
| 磁耦（分立低電容變壓器） | Coilcraft HTX 系列 | 5 W / 12 kV 連續 / <1 pF；HTX7045C 繞組間電容 0.75 pF［來源 2］ |
| 電容耦 / 整合驅動 | Infineon 1ED3124 | 14 A source/sink、傳輸延遲約 90 ns、**CMTI >200 kV/µs**［來源 20］ |
| 半導體整合（GaN-on-SOI） | NYCU 學術 | CMTI >100 V/ns，用於 1700 V SiC［來源 21］ |
| PCB 無芯變壓器 | 學術（10 kV SiC） | >10 kV RMS 絕緣、**5.85 pF**［來源 5］ |
| 中壓專用 IAPS | CPES / 學術 | 2.5 W、**1.03 pF**（13.8 kV/100 kW）；另有 2.34 pF、2.6 pF；設計目標 >20 kV 耐壓、<2 pF［來源 5,6,7］ |
| **聲學（SAW，新）** | Jin et al., *Communications Engineering*（2026） | **0.032 pF**、2.75 kV、~150 mW（本文推導）、0.5 K–544 K［來源 3,4］ |
| **壓電變壓器（PT）** | 學術（歐洲，含 PCB/晶片整合） | 串聯 PT 串列可達**隔離電壓 4 kV、效率 >95%**；早期閘驅 PT 隔離電容 **1.6 pF（4 mm 氣隙）**［來源 1,22,23］（**未驗證**，僅出自摘要） |

CMTI 的產業共識：SiC/GaN 應用建議 **CMTI ≥100 kV/µs，並預期隨頻率提高需求翻倍至 200 kV/µs**［來源 20］。

### 2.2 隔離式壓電變壓器 DC-DC（Berkeley Boles Lab）
- Naval, Xu, Touhami, Boles，**「High-Efficiency Isolated Piezoelectric Transformers for Magnetic-less DC-DC Power Conversion」，IEEE APEC 2025**（亞特蘭大）。
- 數字：輸入-輸出至 **250 V → 125 V**、功率級 100 W；徑向振動模式下**寬工作範圍效率 >93%**；**250 V→117 V、50 W 時 93.8%**；**峰值效率 97.6%**，相較先前隔離式無磁 PT DC-DC 設計**損耗比降低 17 倍**［來源 24,25,26］。
- Sourav Naval 以此獲 APEC 2025 最佳口頭報告獎；BPEC 該屆共獲四項最佳報告獎［來源 27,28］。
- UC Berkeley 已將「Piezoelectric Transformers For Power Conversion」列為可授權技術（案號頁面 NCD 33842）［來源 29］。
- **關鍵缺口：我找不到這批工作的隔離耐壓等級與一次-二次耦合電容 pF。若該數字停在 1–2 pF，它相對於既有磁性 IAPS 就沒有新能力，只是「無磁」。**
- 相鄰數據點：單埠壓電諧振器 DC-DC 已達功率級效率 99%、功率密度 5.7 kW/cm³［來源 25］。

### 2.3 穿金屬壁（TMW）供電與通訊
- **概念起源**：Connor 等人 1997 年專利首次提出用超音波穿金屬壁傳輸功率與感測資料，架構為兩顆同軸對準的 PZT 貼於壁兩側［來源 9］。
- **綜述**：*Sensors* 2015, 15(12), 29870「Through-Metal-Wall Power Delivery and Data Transmission for Enclosed Sensors: A Review」是本領域標準入門文獻［來源 9］。
- **RPI（Lawry / Wilt / Scarton）**：全雙工穿壁通訊與供電系統、頻率追蹤、曲面金屬（管件）通訊；相關專利 US9455791、US10594409B2；早期海軍艦體概念專利 US6625084［來源 12,13,14,30,31,32］。
- **核能**：乾式貯存桶（dry cask）自供電穿壁通訊（*Annals of Nuclear Energy*, 2022）；PNNL 在全尺寸乏燃料罐 mock-up 上做非侵入式超音波內部狀態感測；Sandia/DOE 的 CURIE 文件涉及乾儲罐液態水偵測感測器開發［來源 11,33,34］。專利 US11415555「Ultrasonic through-wall sensors」。
- **陸軍**：arXiv 2607.13797「Experimental Characterization and Prediction of Radial and Thickness Mode Power Transfer Capability in Through-Metal Acoustic Power Transfer」，由 **Army Research Laboratory 合作協議 W911NF2220007** 資助［來源 35］。這是本領域仍有實質軍方資金的直接證據。
- **可攜/可拆式**：Stevens Institute 的「dry-coupled detachable transmitter」（*Ultrasonics*, 2024）針對耦合劑問題提出乾耦合可拆卸發射端［來源 36,37］。
- **管件/曲面**：多層曲面（管壁）功率與資料傳輸已有專文［來源 38］。
- **商用**：**查無**具名的商用產品或 ATEX/IECEx 認證方案。搜尋結果 100% 是論文與專利——**這本身就是一條重要的反面訊號：技術存在近 30 年，仍未見商品化玩家。**

### 2.4 醫療隔離
- IEC 60601-1：一般病人漏電流 <100 µA；**CF 型 <10 µA**；輸入-輸出最低 4000 VAC、輸入-地 1500 VAC；BF/CF 輸出-地 1500 VAC；2×MOPP 需 ≥8 mm 爬電［來源 15,16,17,39］。
- 電外科（Ethicon 系列專利，如 US9060776、US11090104、RE47996）明確描述：隔離變壓器的雜散電容使一次側電位耦合到二次側，造成病人漏電流；被動解法是加洩漏電容，但**感應漏電流可能超出被動電容的能力**，因此需要**主動漏電流抵消**［來源 40］。→ 這說明「把跨障壁電容做到極低」在電外科是真痛點。
- 有一篇低層級期刊（SCIRP）提出用 PLZT 塊材加兩根鉑金屬植入線做 ECG 隔離器，宣稱高 CMRR 與低漏電流［來源 41］——**未驗證，期刊層級低，僅列為存在性證據。**
- 搜尋中另外出現兩件專利「Gate driver coreless transformers for **magnetic resonance imaging** power electronics」（US11777487、US12206394）［來源 42,43］——這暗示 **MRI 腔內功率電子的無磁閘驅是一個已被專利佈局的真實需求**（磁芯在 1.5 T/3 T 靜磁場中飽和且產生影像偽影）。**這是本輪最被低估的線索。**

---

## 3. 關鍵數字表

| 項目 | 數字 | 條件 | 來源 |
|---|---|---|---|
| 穿壁功率+資料（最高記錄） | **50 W + 12.4 Mb/s，同時連續** | 63.5 mm 實心鋼塊 | 12,13,14 |
| 穿壁效率（薄壁） | **60%**，50 kb/s | 1.045 MHz、11 mm 鋼 | 9 |
| 穿壁穩壓輸出 | **15.7 W DC，整體效率 27.7%** | 40 mm 不鏽鋼 | 10 |
| 穿壁高速資料 | **4 Mb/s，功率效率 >30%** | 雙鋼壁 15.97+10.92 mm，88.3 mm 水柱 | 9 |
| 穿壁最大壁厚（文獻） | 63.5 mm 鋼；50 mm 鋁（傳影像） | — | 9,12 |
| SAW 隔離閘驅 隔離電容 | **0.032 pF** | 1.25 mm 聲程，LiNbO₃ | 3,4 |
| SAW 隔離閘驅 耐壓 | 2.75 kV | 同上 | 3,4 |
| SAW 隔離閘驅 輸出 | 13.4 V 開路 / 44.4 mA 短路（≈150 mW，本文推導） | 同上 | 3,4 |
| SAW 隔離閘驅 溫度範圍 | **0.5 K – 544 K** | 同上 | 3,4 |
| SAW 驅動 GaN 開通時間 | 108.8 ns | buck 驗證 | 3,4 |
| 磁性低電容變壓器 | **<1 pF，5 W，12 kV 連續**；HTX7045C 0.75 pF | 商用量產 | 2 |
| 10 kV SiC 閘驅電源需求 | 耐壓 **>20 kV**、耦合電容 **<2 pF** | 學術共識 | 5,6 |
| 10 kV SiC IAPS 最佳實測 | **1.03 pF @ 2.5 W** | 13.8 kV/100 kW 三相 | 5 |
| PCB 無芯變壓器 | 5.85 pF @ >10 kV RMS | — | 5 |
| 位移電流 | 10 pF @ 100 kV/µs → **1 A** | — | 5 |
| 位移電流（本文推導） | 1 pF → 100 mA；0.032 pF → **3.2 mA** | 100 kV/µs | 本文推導 |
| CMTI 產業要求 | **≥100 kV/µs，趨勢 200 kV/µs** | SiC/GaN | 20 |
| ADuM4121 CMTI | >150 kV/µs | 商用 | 18 |
| Infineon 1ED3124 | CMTI >200 kV/µs、14 A、~90 ns | 商用 | 20 |
| PT 頻寬限制 | Q≈1000、f<數十 MHz → 頻寬僅**數十 kHz** | 物理上限 | 3 |
| PT 隔離閘驅（早期） | 隔離電容 1.6 pF（4 mm 氣隙）（**未驗證**） | — | 22 |
| PT 串列隔離 | 4 kV 隔離、效率 >95%（**未驗證**） | — | 23 |
| Berkeley 隔離 PT | 峰值 97.6%；93.8% @ 250→117 V, 50 W；損耗比 −17× | 徑向模、~100 W 級 | 24,25 |
| 單埠壓電諧振器 DC-DC | 99% 功率級效率、5.7 kW/cm³ | 非隔離 | 25 |
| IEC 60601-1 CF 漏電流 | **<10 µA**（AC+DC） | ECG/導管 | 15,16,17 |
| CF 所需障壁總電容（本文推導） | **≲100 pF** @ 240 V/60 Hz | — | 本文推導 |
| 海軍加裝穿線成本 | 乾塢/圍堰，**數月、數百萬美元** | 已服役艦艇 | 12,13 |

---

## 4. 「新能力型」應用機會

### 機會 4.1 ★★★★★ 穿實心金屬壁／密封艙的功率與資料傳輸（不開孔）
- **新能力是什麼**：在**完全不破壞密封或結構完整性**的前提下，把數瓦到數十瓦功率與 Mb/s 級資料送進一個**全金屬密閉容器**。同一顆壓電體同時是致動器（發射聲波）、感測器（接收）、與被動諧振通道——**這正是客戶「主動/被動兩用」概念的教科書級落地**。
- **為什麼以前做不到**：RF 被法拉第籠擋死（文獻直言「不切實際且極度無效率」）；有線需鑽孔，而在核能圍阻體、乾儲罐、潛艇殼、壓力容器上鑽孔等於摧毀認證基礎；電池內置壽命不夠且不可更換［來源 11］。
- **是否真非替代**：**是（強）**。這不是「更小/更便宜」，是「原本零，現在有」。乾式貯存桶目前**根本沒有**任何內部直接量測手段［來源 11］。
- **誰在做**：RPI（Lawry/Wilt/Scarton）、Penn State（乾儲罐自供電穿壁通訊）、PNNL/Sandia（DOE 乏燃料罐）、Army Research Laboratory（W911NF2220007）、Stevens Institute（乾耦合可拆式）［來源 11,12,33,34,35,36］。
- **TRL**：實驗室完整系統演示 + 全尺寸 mock-up 測試 ⇒ **TRL 4–6**（依應用而異；核能側較高，商用側仍為 0）。
- **市場訊號**：**中等偏弱但真實**。持續的軍方/能源部資金與專利佈局（US11415555、US9455791、US10594409B2、US6625084）是正訊號；**查無任何商用產品或公司**是強負訊號——技術存在近 30 年未商品化。
- **技術難點**：耦合劑（乾涸、腐蝕、高溫脫氣）、對準敏感度（小角度/橫向偏移即嚴重劣化）、壁內多重回波與共振使通道函數隨溫度漂移、高溫/高輻射下壓電材料與電子件壽命、以及**認證路徑**（核能與船級社的合格化成本可能遠高於研發成本）［來源 36,44］。

### 機會 4.2 ★★★★☆ 極端溫度／全無磁環境的隔離供電與閘驅
- **新能力是什麼**：在 **0.5 K 到 544 K（−272.6 °C 至 271 °C）**、以及 **1.5 T/3 T 強靜磁場**環境中提供隔離電源與閘極驅動。SAW 元件已實測涵蓋此溫域［來源 3,4］。
- **為什麼以前做不到**：磁芯有居里溫度且在強場中飽和、在 MRI 中產生影像偽影；光耦的 LED 在高溫與輻射下快速老化、在深冷下效率崩潰；電解電容與多數半導體在 0.5 K 不工作。
- **是否真非替代**：**是**（在溫度/磁場極端點上）；在常溫常規場景則**否**。
- **誰在做**：Jin et al.（*Communications Engineering*，SAW 隔離閘驅）；MRI 側已有「Gate driver coreless transformers for MRI power electronics」專利（US11777487、US12206394）表示產業已在解此題，但用無芯變壓器而非壓電［來源 3,4,42,43］。
- **TRL**：SAW 閘驅 **TRL 3–4**（已在 buck 中驗證，但功率僅百毫瓦級）。
- **市場訊號**：量子計算低溫控制電子、井下（>200 °C）、航太、MRI 梯度/RF 功率電子——**皆為高單價、低量、對元件成本不敏感的市場**，正好避開客戶最擔心的「壓電單價貴」問題。
- **技術難點**：功率必須從 ~150 mW 拉到 0.5–2 W 才能驅動實用 SiC/GaN 模組；PZT 居里點不足以支撐 544 K，必須走 LiNbO₃ / AlN / 鑭鎵矽酸鹽等高溫材料，這改變整條材料與製程供應鏈。

### 機會 4.3 ★★★☆☆ 中壓串聯堆疊／SST／MMC 的「超低耦合電容」浮動驅動電源
- **新能力是什麼**：把跨障壁耦合電容從目前最佳的 **~1 pF 降到 <0.1 pF**，同時維持 **>20 kV 隔離耐壓與 1–3 W 功率**。三者兼具目前**無人達成**（SAW 有 0.032 pF 但只有 2.75 kV、~150 mW；磁性有 1.03 pF/2.5 W 但停在 pF 級）。
- **為什麼以前做不到 / 為什麼有價值**：串聯 N 顆開關時共模位移電流線性累加。100 kV/µs 下，1 pF 即 100 mA/顆；十顆堆疊就是 1 A 級共模電流灌回控制側，這是限制串聯層數與 dv/dt 的實質天花板。降到 0.032 pF 等於把這個限制推開 30 倍［來源 5 + 本文推導］。
- **是否真非替代**：**半**。它仍在做「隔離電源」這件既有的事，但性能跨越一個數量級後會**解鎖原本做不到的拓撲**（更高 dv/dt、更多串聯層、更快的固態斷路器）。誠實地說：**這是「量變到質變」型，不是純粹的新能力。**
- **誰在做**：CPES（Virginia Tech）與多個中壓 SiC 團隊做磁性 IAPS；聲學側只有 SAW 論文一篇。**壓電/聲學在此領域基本無人佔位。**
- **TRL**：概念到元件級 **TRL 2–3**。
- **市場訊號**：10 kV SiC 模組、SST、MMC、電網固態斷路器、中壓馬達驅動——市場真實但量小、認證期長（電網級產品驗證常需 5–10 年）。
- **技術難點**：**耐壓與低電容是直接衝突的**——聲程拉長可降電容、提耐壓，但同時提高聲學損耗與插入損失；1.25 mm 聲程只換到 2.75 kV，要到 20 kV 可能需要 10 mm 級聲程，效率如何是未知數。另外 PT 的 Q≈1000 → 數十 kHz 頻寬問題會限制電源迴路的動態響應［來源 3］。

### 機會 4.4 ★★★☆☆ 穿壁「供電＋通訊＋結構健康監測」三合一（主動/被動同體）
- **新能力是什麼**：同一組壓電換能器，平時作為穿壁能量/資料通道（被動傳輸媒介），閒時切換為主動超音波 NDT 探頭，量測壁厚減薄、腐蝕、應力與溫度——**通道本身就是量測工具**。
- **為什麼以前做不到**：傳統上穿壁通訊與壁體 NDT 是兩套獨立硬體與兩次現場作業。
- **是否真非替代**：**是**（功能融合），但**證據薄弱**：PNNL 確有「非侵入式超音波感測乏燃料罐內部狀態」的工作［來源 34］，但我**查無**同一元件同時做功率傳輸與 NDT 的直接文獻。**此機會為推論，需下一輪驗證。**
- **TRL**：**推測 TRL 2–3（未驗證）**。
- **技術難點**：能量傳輸模式與成像/量測模式的頻率與阻抗需求不同；高功率激勵後的餘振會遮蔽微弱回波。

### 機會 4.5 ★★☆☆☆ 醫療 CF 級超低漏電流隔離
- **新能力是什麼**：極低 Y 電容的隔離電源，用於 ECG、心導管、電外科。
- **是否真非替代**：**否（大部分情況）**。本文推導顯示 CF 的 10 µA 只要求障壁總電容 ≲100 pF，而現有醫療電源與低電容變壓器（0.75 pF）已遠優於此。**壓電在此屬於「更好但非必要」，權重應調低。**
- **例外（半新能力）**：電外科生成器在高頻高壓下的感應漏電流**已超出被動洩漏電容的處理能力，廠商被迫做主動漏電流抵消**［來源 40］——這裡若能用聲學障壁把耦合電容壓到 fF 級，可能省掉整套主動抵消電路，屬於真實痛點。另 MRI 相容設備（無磁）見機會 4.2。
- **TRL**：概念級 **TRL 2**；ECG 壓電隔離器僅見一篇低層級期刊［來源 41］（**未驗證**）。

### 機會 4.6 ★☆☆☆☆（明確標示為替代品）一般 1200 V SiC/GaN 隔離閘驅電源
- **這是替代品，不是新能力。** 對手是 ADI iCoupler（>150 kV/µs）、Infineon 1ED3124（>200 kV/µs、14 A、90 ns）、Coilcraft <1 pF/5 W/12 kV 的成熟量產件［來源 2,18,20］。壓電在此既沒有性能跨越，單價又高於磁性與矽整合方案，且 PT 的數十 kHz 頻寬先天不足以支援 WBG 閘驅［來源 3］。**建議明確排除，與客戶排除「取代電感」的理由完全同構。**

---

## 5. 反面證據、失敗案例與物理上限

1. **PT 的頻寬天花板是硬的**：Q≈1000、工作頻率 <數十 MHz ⇒ 固有頻寬僅數十 kHz，明文被判定「不足以支援 WBG 功率電子的先進閘極驅動」［來源 3］。想同時傳能與傳高速訊號，必須離開低頻 bulk-mode PT，走 MHz–GHz 的 SAW/BAW，而那是完全不同的材料與晶圓製程（LiNbO₃、AlN），**與傳統 PZT 陶瓷產線無共通性**。
2. **PT 的電容性負載使驅動電路笨重**：瞬時功率遠大於平均有效功率，導致傳統驅動電路（尤其電感）過大［來源 3］——**諷刺的是，這削弱了「壓電可以消滅電感」的核心賣點**。
3. **PT 產業曾經歷一次完整的商業崩潰**：1980 年代末日本廠商推動 PT 用於 CCFL 背光高壓驅動，2000 年代末 LCD 背光轉向 LED，高壓 PT 銷售逐步崩跌，**多數主要供應商停止高量生產**［來源 45,46］。同一文獻也指出「以分立元件實作精巧可靠的控制電路很複雜，勸退了許多研究者」。**供應鏈與量產經驗已經流失一次，重建成本必須計入。**
4. **磁性方案已經佔住「低電容」高地**：<1 pF、12 kV、5 W 已是可買到的量產品［來源 2］；學術中壓 IAPS 已做到 1.03 pF［來源 5］。壓電必須證明能到 **0.1 pF 以下且仍有瓦級功率**，否則沒有立足點。
5. **SAW 隔離閘驅目前只有百毫瓦級與 2.75 kV**：13.4 V 開路 / 44.4 mA 短路（≈150 mW，本文推導），且 2.75 kV 遠低於中壓需要的 >20 kV［來源 3,4］。**離實用中壓應用有 1–2 個數量級的差距。**
6. **穿金屬壁技術近 30 年未商品化**：起源可追至 1997 年 Connor 專利，2011 年 RPI 已有 50 W/12.4 Mb/s 的媒體級成果，2015 年已有完整綜述——但 **2026 年仍查無任何具名商用產品或 ATEX/IECEx 認證方案**［來源 9,12］。這是本 dossier 最重要的警訊：**技術可行 ≠ 市場可行。**
7. **耦合劑是實際部署的第一號殺手**：凝膠耦合劑會乾涸、需反覆塗抹、殘留難清且加速腐蝕；高溫下市售耦合劑會熱脫氣、喪失機械黏結，**會先造成量測數據漂移再造成連結失效**［來源 36,44］。永久黏合則喪失可維護性。Stevens 的乾耦合可拆式發射端是針對此的最新嘗試（2024）［來源 36］。
8. **對準容差是系統級瓶頸**：文獻明言「即使中等程度的角度或橫向偏移都會顯著劣化聲學耦合與傳輸效率」［來源 44］。這對現場安裝（船體、管線、罐體）是嚴重的工程約束。
9. **穿壁效率隨壁厚急劇下降**：11 mm 鋼 60%，40 mm 不鏽鋼降到 27.7%［來源 9,10］。厚壁（乾儲罐、潛艇殼可達 50–100 mm+）意味著大部分能量變成壁體發熱與回波。
10. **市場規模訊號偏弱**：某市場研究網站宣稱壓電變壓器市場 2033 年達 4.658 億美元、CAGR 9.8%［來源 47］——**此數字為第三方市調網站自報，未驗證，可信度低，僅供參考**。即便為真，這個量級對建立新的高溫壓電材料產線而言偏小。

---

## 6. 未解問題（給下一輪研究）

1. **Berkeley Boles 團隊的隔離式 PT，其隔離耐壓與一次-二次耦合電容究竟是多少 pF？** 這是判定機會 4.3 生死的唯一關鍵數字，本輪**查無**。應直接查 APEC 2025 論文全文（IEEE Xplore 10977397）與 UC Berkeley 技轉頁 NCD 33842。
2. **聲程長度 vs 隔離耐壓 vs 插入損失的定量標度律是什麼？** SAW 用 1.25 mm 換到 2.75 kV；要到 20 kV 需要多長聲程、效率掉多少、是否還能傳 1 W？沒有這條曲線就無法判斷機會 4.3 是否物理可達。
3. **穿金屬壁至今無商品化的真正原因是什麼？** 是認證成本、耦合劑可靠度、單位成本、還是缺乏 killer app？必須找到**具體失敗案例或已放棄的商業化嘗試**（本輪額度不足未能查）。建議查：核電廠實際部署案例、船級社/NRC 對非侵入式感測的認證要求、以及是否有新創公司曾募資後倒閉。
4. **子題 (d) 井下/密封無穿線馬達與致動器完全未查**，以及 MMC 子模組輔助電源、固態斷路器、800 V/1500 V 電動車與儲能的隔離電源規格亦未查。這些是本 dossier 最大的覆蓋缺口。
5. **MRI 相容無磁功率電子**（US11777487 / US12206394 所指向的需求）是本輪意外發現的高潛力線索，但完全未深入。誰是這兩件專利的受讓人？市場規模多大？壓電相對無芯變壓器的優勢是什麼？
6. **同一顆換能器同時做功率傳輸與 NDT 監測（機會 4.4）是否已有人做過？** 本輪為推論，需驗證。

---

## 7. 來源清單

1. A new MOSFET & IGBT gate drive insulated by a piezoelectric transformer — https://www.researchgate.net/publication/3917316_A_new_MOSFET_IGBT_gate_drive_insulated_by_a_piezoelectric_transformer — 早期用壓電變壓器隔離 MOSFET/IGBT 閘驅的代表文獻。
2. Coilcraft — Low-Capacitance Transformers for LLC Isolated Gate Driver Bias Supplies — https://www.coilcraft.com/en-us/applications/low-capacitance-transformers/ — 商用磁性方案 5 W/12 kV/<1 pF、HTX7045C 0.75 pF，壓電的直接對手。
3. Microwave-acoustic-based isolated gate driver for power electronics (arXiv preprint) — https://arxiv.org/pdf/2511.13412 — SAW 隔離閘驅 0.032 pF/2.75 kV/0.5–544 K，並明確指出傳統 PT 的頻寬與電容性缺陷。
4. Microwave-acoustic-based isolated gate driver for power electronics, *Communications Engineering* — https://www.nature.com/articles/s44172-026-00681-w — 同上之正式期刊版本。
5. CPES (Virginia Tech) — Power Supply with Low Input-Output Capacitance for Multiple Gate Driver Units of a 10 kV SiC-MOSFET Module — https://cpes.vt.edu/library/viewnugget/760 — 10 pF@100 kV/µs → 1 A 位移電流；中壓耦合電容目標值。
6. Design Considerations for High-Voltage-Insulated Gate Drive Power Supply for 10-kV SiC MOSFET — https://www.researchgate.net/publication/341909986_Design_Considerations_for_High-Voltage-Insulated_Gate_Drive_Power_Supply_for_10-kV_SiC_MOSFET_Applied_in_Medium-Voltage_Converter — 中壓閘驅電源需 >20 kV 耐壓、<2 pF。
7. High-Density Current-Transformer Based Gate-Drive Power Supply with Reinforced Isolation for 10 kV SiC MOSFET Modules — https://www.researchgate.net/publication/336069524_High-Density_Current-Transformer_Based_Gate-Drive_Power_Supply_with_Reinforced_Isolation_for_10_kV_SiC_MOSFET_Modules — 中壓 IAPS 磁性方案。
8. High-isolation Low-coupling-capacitance Standalone Gate Drive Power Supply for SiC-based Medium-Voltage Power Electronic Systems — https://www.researchgate.net/publication/337646472_High-isolation_Low-coupling-capacitance_Standalone_Gate_Drive_Power_Supply_for_SiC-based_Medium-Voltage_Power_Electronic_Systems — 同領域低耦合電容獨立閘驅電源。
9. Through-Metal-Wall Power Delivery and Data Transmission for Enclosed Sensors: A Review, *Sensors* 2015 — https://www.mdpi.com/1424-8220/15/12/29870 — 本領域標準綜述，含 1.045 MHz/11 mm/60%/50 kb/s、4 Mb/s 雙壁、63.5 mm 壁厚、Connor 1997 起源。
10. An Ultrasonic Through-Metal-Wall Power Transfer System with Regulated DC Output, *Applied Sciences* 2018 — https://www.mdpi.com/2076-3417/8/5/692 — 40 mm 不鏽鋼、15.7 W 穩壓輸出、27.7% 效率。
11. Self-powered Through-wall Communication for Dry Cask Storage Monitoring, *Annals of Nuclear Energy* — https://www.sciencedirect.com/science/article/abs/pii/S0306454922003413 — 乾式貯存桶內「目前無任何內部感測系統」的 non-substitutional 論證。
12. RPI News — Student Innovation Transmits Data and Power Wirelessly Through Submarine Hulls — https://news.rpi.edu/luwakkey/2836 — 50 W + 12.4 Mb/s 穿 2.5 吋鋼；海軍鑽孔/乾塢成本。
13. ScienceDaily 版本 — https://www.sciencedaily.com/releases/2011/03/110307142226.htm — 同上（此版寫 megabytes/s，與 RPI 版不一致）。
14. New Atlas 報導 — https://newatlas.com/ultrasonic-data-and-power-transmission-through-metal/18097/ — 同一成果的第三方報導。
15. XP Power — Overcoming patient leakage current in medical applications — https://www.xppower.com/resources/blog/overcoming-patient-leakage-current-issues — 病人漏電流與 Y 電容關係。
16. Advanced Energy — Safety Requirements in Medical Equipment: BF and CF — https://www.advancedenergy.com/en-us/about/news/blog/safety-requirements-in-medical-equipment-designing-for-bf-and-cf-classifications/ — CF <10 µA、隔離電壓要求。
17. Bridgeport Magnetics — IEC 60601 Leakage Current Requirements For Medical Isolation Transformers — https://bridgeportmagnetics.com/iec-60601-leakage-current-requirements-medical-isolation-transformer/ — 醫療隔離變壓器漏電流規範。
18. Analog Devices — Inside iCoupler Technology: Measuring CMTI — https://www.analog.com/en/resources/technical-articles/inside-icoupler-technology-measuring-cmti.html — iCoupler CMTI 量測與 >100 kV/µs 數據。
19. Analog Devices — Implementing an Isolated Half-Bridge Gate Driver — https://www.analog.com/en/resources/analog-dialogue/articles/implementing-an-isolated-half-bridge-gate-driver.html — ADuM 系列應用背景。
20. Infineon Developer Community — Common mode transient immunity (CMTI) in gate drivers — https://community.infineon.com/t5/Knowledge-Base-Articles/Common-mode-transient-immunity-CMTI-in-gate-drivers/ta-p/1114529 — SiC/GaN 需 ≥100 kV/µs、趨勢 200 kV/µs；1ED3124 規格。
21. A High CMTI GaN-on-SOI Gate Driver With Quad-Drive Control for High dV/dt 1700-V SiC Power Switch, IEEE — https://ieeexplore.ieee.org/document/10506900/ — 半導體整合式高 CMTI 驅動器（>100 V/ns）。
22. Piezoelectric transformer for integrated MOSFET and IGBT gate driver — https://www.researchgate.net/publication/3280843_Piezoelectric_transformer_for_integrated_MOSFET_and_IGBT_gate_driver — 早期 PT 閘驅，摘要提及 1.6 pF/4 mm 氣隙（未驗證）。
23. Galvanic Isolating Power Supplies with Piezoelectric Transformer: From PCB Integration to Chip Integration — https://www.researchgate.net/publication/279487394_Galvanic_Isolating_Power_Supplies_with_Piezoelectric_Transformer_From_PCB_Integration_to_Chip_Integration_from_Analogue_to_Digital_Driving — PT 串列 4 kV 隔離、>95% 效率（未驗證）。
24. High-Efficiency Isolated Piezoelectric Transformers for Magnetic-less DC-DC Power Conversion, IEEE APEC 2025 — https://ieeexplore.ieee.org/iel8/10977026/10977027/10977397.pdf — Naval/Xu/Touhami/Boles 原始論文。
25. 同上（ResearchGate 條目，含效率數字摘要）— https://www.researchgate.net/publication/391376205_High-Efficiency_Isolated_Piezoelectric_Transformers_for_Magnetic-less_DC-DC_Power_Conversion — 97.6% 峰值、17× 損耗降低、單埠 PR 99%/5.7 kW/cm³。
26. Boles Lab @ UC Berkeley — Research — https://www.boleslab.org/research — 團隊研究方向與壓電被動元件能量密度主張。
27. EECS at Berkeley — BPEC wins four Best Presentation Awards at IEEE APEC 2025 — https://eecs.berkeley.edu/news/bpec-wins-four-best-presentation-awards-at-ieee-apec-2025/ — Sourav Naval 獲最佳口頭報告獎。
28. Berkeley Power and Energy Center 同一消息 — https://bpec.berkeley.edu/bpec-wins-four-best-presentation-awards-at-ieee-apec-2025/ — 交叉驗證。
29. UC Berkeley 技轉 — Piezoelectric Transformers For Power Conversion — https://techtransfer.universityofcalifornia.edu/NCD/33842.html — 該技術已列為可授權，商業化訊號。
30. A full-duplex ultrasonic through-wall communication and power delivery system (PubMed) — https://pubmed.ncbi.nlm.nih.gov/23475924/ — RPI 全雙工穿壁系統原始論文。
31. US10594409B2 — System for ultrasonic communication across curved metal surfaces — https://patents.google.com/patent/US10594409B2/en — 曲面金屬（管件/罐體）穿壁通訊專利。
32. US6625084 — System for acoustically passing electrical signals through a hull — https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/6625084 — 早期艦體聲學穿壁傳訊專利。
33. PNNL — Non-invasive ultrasonic sensing of internal conditions on a partial full-scale spent nuclear fuel canister mock-up — https://www.pnnl.gov/publications/non-invasive-ultrasonic-sensing-internal-conditions-partial-full-scale-spent-nuclear — 全尺寸罐體 mock-up 實測，TRL 佐證。
34. CURIE/Sandia — Sensor Development for Liquid Water Detection in Dry Storage Casks (FY19 Status) — https://curie.pnnl.gov/sites/default/files/sandiadocs/M3SF-19PN010201034-Sensor-Development-for-Liquid-Water-Detection-in-Dry-Storage-Casks-FY19-Status.pdf — DOE 乾儲罐感測器計畫文件。
35. Experimental Characterization and Prediction of Radial and Thickness Mode Power Transfer Capability in Through-Metal Acoustic Power Transfer (arXiv) — https://arxiv.org/html/2607.13797 — Army Research Laboratory 合作協議 W911NF2220007 資助，證明軍方仍在投資。
36. Portable through-metal ultrasonic power transfer using a dry-coupled detachable transmitter, *Ultrasonics* 2024 — https://www.sciencedirect.com/science/article/abs/pii/S0041624X2400101X — 針對耦合劑問題的乾耦合解法（Stevens Institute）。
37. Stevens Institute 該論文條目 — https://researchwith.stevens.edu/en/publications/portable-through-metal-ultrasonic-power-transfer-using-a-dry-coup/ — 機構歸屬確認。
38. Ultrasonic Power and Data Transfer through Multiple Curved Layers Applied to Pipe Instrumentation (PMC) — https://pmc.ncbi.nlm.nih.gov/articles/PMC6806064/ — 管線曲面多層穿壁傳能傳訊。
39. SII — Did you know that even 10 uA of current is hazardous for a human — https://sii.pl/blog/en/did-you-know-that-even-10-ua-of-current-is-hazardous-for-a-human/ — 10 µA 心臟風險背景說明。
40. US9060776 — Surgical generator for ultrasonic and electrosurgical devices — https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/9060776 — 明述雜散電容造成病人漏電流、被動洩漏電容不足、需主動漏電流抵消（同族另有 US11090104、RE47996、US9050093 等）。
41. Piezoelectric Ceramic Controlled with Platinum Implant as New Isolator in ECG (SCIRP) — https://file.scirp.org/Html/11-7701265_45552.htm — PLZT 壓電 ECG 隔離器（低層級期刊，未驗證）。
42. US11777487 — Gate driver coreless transformers for magnetic resonance imaging power electronics — https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/11777487 — MRI 環境無磁閘驅需求的專利佐證。
43. US12206394 — 同族後續案 — https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/12206394 — 同上。
44. Recent advances in transducers for through-tissue ultrasonic power transfer, IOPscience — https://iopscience.iop.org/article/10.1088/2516-1091/ae5f8a — 明述對準偏移為系統級瓶頸（雖為穿組織，換能器對準問題同構）。
45. Piezoelectric Transformers: An Historical Review, *Actuators* 2016 — https://www.mdpi.com/2076-0825/5/2/12 — CCFL→LED 轉換導致高壓 PT 停產的商業失敗史。
46. 50 Years Of Piezoelectric Transformers — Trends In The Technology (PDF) — https://www.mmech.com/images/stories/Standard_Products/Transformers/PT_Introduction/50_Years.pdf — 同一失敗史的另一來源，並指出控制電路複雜度勸退研究者。
47. Piezoelectric Transformers Market（第三方市調網站）— https://www.futuremarketreport.com/industry-report/piezoelectric-transformers-market — 宣稱 2033 年 4.658 億美元、CAGR 9.8%（**未驗證，市調網站自報，可信度低**）。
48. Optimized Design of an Ultrasonic-Based High-Efficiency Wireless Passive Monitoring System for Sealed Metal Compartments (PMC) — https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10820569/ — 密封金屬艙無線被動監測系統設計。
49. US11415555 — Ultrasonic through-wall sensors — https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/11415555 — 穿壁超音波感測器專利。
50. US9455791 — Full-duplex ultrasonic through-wall communication and power delivery system with frequency tracking — https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/9455791 — 頻率追蹤全雙工穿壁系統專利。
