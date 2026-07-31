# 「主動/被動兩用」壓電元件的概念家族與學術基礎

> 一句話結論：「同一顆壓電體同時做主動與被動」在學術上已經被拆解成七個成熟的概念家族、量產案例也確實存在（TDK CeraPlas、Boréas BOS1901、Qualcomm 3D Sonic、xMEMS Cypress），但**真正具「以前做不到」性質的，幾乎全部集中在「機械共振器同時是能量儲存體與訊號/場的發射源」這一類**（VLF 機械天線、mm³ 級超音波植入物、穿金屬壁供電＋通訊、單顆陶瓷產生 15 kV 冷電漿）；而 shunt damping / self-sensing 這一支雖然論文最多，商業化紀錄卻是**做出來又下架**（HEAD i.S18 網球拍），屬於「更省一顆感測器」的替代型改良，權重應調低。

> 研究限制聲明：本次執行環境的 HTTPS 對外連線被組織 egress policy 阻擋（除 github.com 等少數白名單外，`arxiv.org`、`mdpi.com`、`nature.com`、`patents.google.com`、`ieeexplore.ieee.org`、`tdk-electronics.tdk.com`、`ncbi.nlm.nih.gov` 等全部回 403 CONNECT denial），故**無法執行 WebFetch 抓一手全文**。以下所有數字均來自 26 次網頁搜尋所回傳的原文摘錄，URL 均為可點連結，但**未經一手頁面二次核對者已逐條標註「未驗證」**。

---

## 1. 結論摘要

1. **概念家族已經定型，不是新題目。** 2025 年的回顧論文把壓電 shunt 電路明確分成 passive / semi-passive / semi-active / active 四類，涵蓋傳統 R–L 共振、多模態共振、自適應調諧、開關式（SSD 家族）與負電容五種型態，並自陳「主要涵蓋 2019 年至今」——代表這個領域仍在出論文，但**分類學已經封閉**（[MDPI Appl. Sci. 15(11) 6035, 2025](https://www.mdpi.com/2076-3417/15/11/6035)）。想切入的話，護城河不會在「又想到一種 shunt 拓樸」。

2. **self-sensing actuator（SSA）唯一大量商業化的地方是觸覺回饋，不是精密定位。** Boréas Technologies 的 BOS1901 被明確描述為「市場上唯一能用同一顆致動器同時觸發觸覺與感測按壓力的壓電驅動 IC」，其 CapDrive 平台宣稱比 LRA 方案省電 20 倍、比競品壓電驅動 IC 省電 10 倍（[Boréas BOS1901](https://www.boreas.ca/products/bos1901-piezo-haptic-driver)、[CapDrive](https://www.boreas.ca/pages/capdrive-technology)）。TDK PowerHap 則是「致動器內建感測功能、可偵測最高 25 N 壓力、觸發力可個別設定，因而免除獨立觸控感測器」，激振頻寬 1 Hz–1000 Hz（[TDK PowerHap](https://product.tdk.com/en/products/sw_piezo/haptic/powerhap/index.html)）。

3. **反過來說，在最需要精度的納米定位市場，self-sensing 至今沒有取代外部感測器。** Physik Instrumente 現役的 P-621.1CD、P-628.1CD 等 PIHera 平台仍然標配電容式位移感測器做直接量測（direct metrology），理由是「傳動鏈、致動器、槓桿、導引機構的誤差不影響量測，漂移與遲滯自動被消除」（[PI Capacitive Sensors](https://www.physikinstrumente.com/en/expertise/technology/sensor-technologies/capacitive-sensors)）。這是最直接的反面證據。

4. **SSA 的物理死穴是橋式電路的電容失衡。** 綜述明確指出：固定設計的橋式電路在壓電電容 Cp 隨溫度、濕度、機械負載變動時，會抽出「被汙染的機械響應」，導致效能劣化甚至閉迴路不穩定（[IEEE, An Overview of Piezoelectric Self-Sensing Actuation for Nanopositioning](https://ieeexplore.ieee.org/document/8889413/)）。這解釋了為什麼 SSA 在「訊號只要能分辨有沒有按下去」的觸覺市場活得下來，在「要 nm 級絕對精度」的市場活不下來。

5. **SSD（開關式 shunt）確實比線性 shunt 強，量化差距約 2 倍（dB）。** 用 SSDV（Synchronized Switch Damping on Voltage source）在噪音穿透實驗中拿到 **16.1 dB** 衰減，而傳統 SSDI 只有 **8 dB**；另有以自適應頻率與 SSD 方法取得 10 dB 與 4.8 dB 振動速度衰減的紀錄（[Direct Adaptive SSDV Circuit, IEEE 2022](https://ieeexplore.ieee.org/document/9797239/)、[Semi-passive noise control by SSDV](https://www.academia.edu/6085630/Semi_passive_piezoelectric_noise_control_in_transmission_by_synchronized_switching_damping_on_voltage_source)）。

6. **被動 R–L shunt 的電感需求是它二十年不落地的主因。** 對典型壓電電容 **10–100 nF**，要把電氣共振調到結構低頻模態，需要 **10–1000 H** 等級的電感；這種電感的寄生耗散往往已超過最佳阻尼設計值，且線性 shunt 對參數飄移極度敏感、失諧即失效（[綜述整理](https://www.researchgate.net/publication/231126028_Reducing_the_inductance_requirements_of_piezoelectric_shunt_damping_systems)、[Frontiers Built Environ. 2019](https://www.frontiersin.org/journals/built-environment/articles/10.3389/fbuil.2019.00064/full)）。Fleming & Moheimani 的解法是用 DSP＋壓控電流源合成任意 shunt 阻抗（synthetic impedance），但這已經是「主動電路模擬被動元件」，能耗與成本都回到主動端（[Synthetic impedance](https://www.researchgate.net/publication/3382744_Synthetic_impedance_for_implementation_of_piezoelectric_shunt-damping_circuits)）。

7. **負電容 shunt 是「假被動」。** 由於使用 OP-AMP，兩個固有問題無法迴避：(i) 主動元件帶來的動態不穩定；(ii) 激振變大時 OP-AMP 輸出飽和；且 OP-AMP 的功耗隨負電容控制增益上升（[ECCOMAS SMART 2023, SM23_444339](https://files.eccomasproceedia.org/papers/smart-2023/SM23_444339.pdf)、[Penn State, Power output and dissipation of a negative capacitance shunt](https://pure.psu.edu/en/publications/power-output-and-dissipation-of-a-negative-capacitance-shunt-coup/)）。要宣稱「被動元件」時必須把這條講清楚。

8. **真正非替代性的證據集中在「壓電體同時是共振腔與輻射／耦合口」。** 三個硬指標：(a) 鈮酸鋰 Y∠36° 切向壓電共振器當可攜式 VLF 發射機，同電尺寸下輻射效率比先前技術高 **>300 倍**，並用共振的時間調變把頻寬推到 **超過 Bode-Fano 上限 83 倍**，元件尺度 10 cm 而波長 >1 km（[Nature Communications 2019, s41467-019-09680-2](https://www.nature.com/articles/s41467-019-09680-2)）；(b) StimDust 體積 **6.5 mm³**，同一顆壓電晶體同時做超音波受電與 backscatter 通訊，power-to-stimulation 效率 **82%**（[arXiv 1807.07590](https://arxiv.org/pdf/1807.07590)）；(c) 穿越 **63.5 mm 厚鋼壁**同時傳 **17.37 Mbps 資料＋50 W 功率**（早期系統為 6.3 cm 鋼、12.4 Mbps＋32.5 W）（[IEEE UFFC 6396499](https://ieeexplore.ieee.org/document/6396499/)）。這三者的共通點：**電磁路徑根本不存在**，所以不是替代品。

---

## 2. 現況：技術 / 產品 / 玩家

### 2.1 已量產（有型號、有客戶）

| 型態 | 產品 / 玩家 | 兩用性質 |
|---|---|---|
| self-sensing 觸覺驅動 IC | Boréas **BOS1901**（單通道）、**BOS0614**（四通道，2022 發表，整合感測）；與 Synaptics 合作壓電觸控板 | 同一顆壓電片：主動＝觸覺致動；被動／感測＝按壓力偵測 |
| 致動器內建感測 | TDK **PowerHap**（1204H018V060 等），Aito **HapticTouch** 控制器 | 致動＋壓力偵測（≤25 N），免外掛觸控感測器 |
| 壓電變壓器→冷電漿 | TDK **CeraPlas HF**（與 relyon plasma 合作） | 被動＝機械共振儲能升壓；主動＝直接在輸出端點燃大氣壓冷電漿 |
| PMUT 指紋辨識 | Qualcomm **3D Sonic**（24×8 PMUT 陣列，180 nm CMOS 綁定） | 同一批 PMUT 由 TX 模式切到 RX 模式做 pulse-echo 成像 |
| piezoMEMS 揚聲器／閥 | xMEMS **Cypress**（sound-from-ultrasound，2025 量產就緒）、**Skyline** DynamicVent（固態 MEMS 閥） | Cypress：同一 MEMS 同時做超音波載波調變與解調；Skyline：同一壓電結構既是聲學阻抗元件（閥）又是致動器 |
| 柴油壓電噴油嘴 | Continental 直驅式壓電噴油嘴＋閉迴路針閥控制（Needle Closing Control） | 同一壓電堆：主動＝開閥；被動／感測＝由針閥關閉的聲訊號回推關閉時刻 |
| 超音波打線 | 「smart transducer」內嵌 1 mm × 1 mm × 0.245 mm PZT 感測片，量測撞擊力、基頻與二次諧波、打線時間 | 換能器本體同時是製程監控感測器 |

### 2.2 已商業化又退場（重要警訊）

- **HEAD Intelligence 系列網球拍（i.S18 / i.X16 / Protector OS）**：Intellifiber 壓電纖維＋手柄內 ChipSystem，把擊球形變能轉成電能後回饋抑振。宣稱一般球拍衰減振動 20%，i.S18 可達 50%；有針對網球肘症狀的延伸臨床研究。**但該系列已停產，推測原因為成本過高**（[EE Times](https://www.eetimes.com/piezoelectric-rackets-add-professional-oomph/)、[延伸研究 PDF](https://www.researchgate.net/publication/226285635_An_Extended_Study_Investigating_the_Effects_of_Tennis_Rackets_with_Active_Damping_Technology_on_the_Symptoms_of_Tennis_Elbow)、專利 [US6974397B2](https://patents.google.com/patent/US6974397B2/en)「Racket with self-powered piezoelectric damping system」）。
- **K2 Smart Ski**（與 Cambridge, MA 的 Active Control eXperts / ACX 合作）：把壓電當被動阻尼元件放進滑雪板，同樣已非市場主流。
- **CCFL 背光用壓電變壓器**：1990 年代起飛，到 2000 年代初期估計有 **25–30%** 的 CCFL 背光電路採用壓電變壓器技術，Toshiba、NEC、Hitachi、Panasonic、Apple 都用過；2000 年代末 LCD 背光轉 LED，高壓壓電變壓器出貨崩跌，多數主要供應商停止大量生產，連專用 IC 都停產（[Actuators 2016, 5(2), 12 — Piezoelectric Transformers: An Historical Review](https://www.mdpi.com/2076-0825/5/2/12)）。

### 2.3 學術層面的關鍵譜系

- **APPN（Active-Passive hybrid Piezoelectric Networks）**：Penn State 的 K. W. Wang 團隊（Tsai & Wang、Morgan & Wang）是源頭。核心洞見不是「主動＋被動疊加」，而是**「shunt 電路若調諧得當，不只提供被動阻尼，還會放大主動控制權限（active action authority）」**，且整合式 APPN 比主動、被動元件分開放置更有效（[Smart Mater. Struct. 10(4) 325, 2001](https://iopscience.iop.org/article/10.1088/0964-1726/10/4/325)、[JIMSS 1998, 可變電阻 APPN](https://journals.sagepub.com/doi/10.1177/1045389X9800900708)、[SPIE 3045](https://www.spiedigitallibrary.org/conference-proceedings-of-spie/3045/0000/Some-insights-on-active-passive-hybrid-piezoelectric-networks-for-structural/10.1117/12.274191.short)）。相關的美國國防技術報告把這條路線推到「機械共振強化主動權限、無需在行程與出力間取捨」（[DTIC ADA429566](https://apps.dtic.mil/sti/pdfs/ADA429566.pdf)）。
- **能量採集介面電路（SSHI / SSHC / SECE）**：這是「同一顆壓電既是機械共振器又是電荷源」最工程化的一支。硬數字見第 3 節。
- **三端口／二端口網路觀念（Mason / KLM / BVD）**：Mason 等效電路把壓電體拆成 **1 個電端口 + 2 個聲端口**，中間以理想機電變壓器耦合；BVD 則以 C0（靜電容）並聯 R–L–C 動態支路描述單一共振。這是把壓電體當「網路元件」而非「材料」來設計電路的理論基礎，也是把主動／被動兩種角色統一在同一組 ABCD 參數裡的唯一嚴謹語言（[JPL/NASA, Mason vs KLM 比較](https://ndeaa.jpl.nasa.gov/ndeaa-pub/USDC/Kk_1-comparison.pdf)、[DTIC ADA231520](https://apps.dtic.mil/sti/tr/pdf/ADA231520.pdf)）。
- **參數放大（parametric amplification）**：在整合了壓電致動與壓電感測的微共振器上，實測增益可達 **18.2 dB**，Q 值提升可達 **14 倍**，但在高泵浦下因非線性阻尼而飽和（[PMC6356750](https://pmc.ncbi.nlm.nih.gov/articles/PMC6356750/)、[ENSAM 8827](https://sam.ensam.eu/handle/10985/8827)）。

---

## 3. 關鍵數字表

| 主題 | 數字 | 條件／備註 | 來源 |
|---|---|---|---|
| SSDV vs SSDI | **16.1 dB** vs **8 dB** | 傳遞聲壓衰減 | [IEEE 9797239](https://ieeexplore.ieee.org/document/9797239/) |
| SSD 自適應頻率 | **10 dB** / **4.8 dB** | 振動速度衰減 | 同上 |
| 被動 R–L shunt 電感需求 | **10–1000 H**（Cp = 10–100 nF） | 低頻模態調諧 | [RG 231126028](https://www.researchgate.net/publication/231126028_Reducing_the_inductance_requirements_of_piezoelectric_shunt_damping_systems) |
| P-SSHI 翻轉效率 | **>80%**（外掛電感 820 µH） | 模擬 | [JSemi 2018, 39(4) 045002](https://ui.adsabs.harvard.edu/abs/2018JSemi..39d5002L/abstract) |
| P-SSHI 鞋墊採集 | **83.02%**，**3.6 mW** | 1 Hz 步行、10 kΩ 負載、10 µF 儲能 | [PMC9966393](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9966393/) |
| P-SSHI 增益 | **231 µW**，**2.89×** vs 無 SSHI | 實測 | [MDPI Energies 12(16) 3166](https://www.mdpi.com/1996-1073/12/16/3166) |
| 無電感 SSHC（bias-flip） | **9.7×** 功率提升；翻轉效率 **80%**（8 顆切換電容）；0.35 µm CMOS | 相對理想全橋 | [Cambridge repository, Du et al.](https://www.repository.cam.ac.uk/bitstream/1810/266131/1/201609_SijunDU_revised.pdf) |
| 其他 bias-flip | **7.62×**（113.4 Hz 激振）；130 nm CMOS **417%** 提升 | | [MDPI Sensors 25(13) 4029, 2025](https://www.mdpi.com/1424-8220/25/13/4029) |
| 參數放大 | 增益 **18.2 dB**，Q 提升 **14×** | 壓電致動＋壓電感測微共振器 | [PMC6356750](https://pmc.ncbi.nlm.nih.gov/articles/PMC6356750/) |
| TDK CeraPlas HF | 輸入 **12–24 Vpp** → 輸出 **up to 15 kV**；**47.3 × 20 × 20 mm**；電漿溫度 **<50 °C**；硬質 PZT 共燒銅內電極，多層 Rosen 型 | 大氣壓、可離子化空氣 | [TDK tech library](https://www.tdk-electronics.tdk.com/en/373562/tech-library/articles/applications-cases/applications-cases/cold-plasma-from-a-single-component/1109546)、[GlobeNewswire 2018-11-13](https://www.globenewswire.com/news-release/2018/11/13/1650541/0/en/TDK-Introduces-CeraPlas-HF-Compact-Cold-Plasma-Generator-Element.html) |
| 壓電變壓器 CCFL 市佔 | **25–30%** 的 CCFL 背光電路（2000 年代初） | 歷史峰值 | [Actuators 5(2) 12](https://www.mdpi.com/2076-0825/5/2/12) |
| 現代 PT 轉換器效率 | 峰值 **98.3%**（損耗比降 ~27×）；**>40 W/cm³ @ >98%**；另有 **97.5%**（損耗比降 17×） | 隔離型 magnetic-less DC-DC | [RG 391376205](https://www.researchgate.net/publication/391376205_High-Efficiency_Isolated_Piezoelectric_Transformers_for_Magnetic-less_DC-DC_Power_Conversion)（未驗證） |
| PT 負載敏感度 | 負載失配（6 Ω 或 40 Ω）→ 損耗 **+50%**，效率降至 **97%** | 關鍵限制 | 同上（未驗證） |
| 壓電共振器 DC-DC | 功率密度 **1340 W/cm³**（比同級電感高一個數量級）；180 V→60 V、**89 W**、**97%**；IC **96.2%**（>9:1）；另有 **99%** 功率級效率、**5.7 kW/cm³** | **客戶已排除之路線，僅作對照** | [Power Electronics News](https://www.powerelectronicsnews.com/piezoelectric-resonators-in-dc-dc-converters-current-status-and-limits/)、[Stanford SUPERLAB](https://superlab.stanford.edu/publication/2021-03-18-Optimized-Resonators-Piezoelectric_Braun/index.html) |
| PT 效率的材料上限 | 效率 ∝ **k² × Qm** | 設計第一原理 | 同上 |
| 傳統 bulk-mode PT 頻寬 | 工作頻率 < 數十 MHz，Qm ≈ **1000** → 固有頻寬僅 **數十 kHz** | 不足以驅動 WBG 元件的 sub-µs 轉態 | [arXiv 2511.13412](https://arxiv.org/pdf/2511.13412) |
| VLF 壓電發射機 | 輻射效率 **>300×** 於同電尺寸先前技術；頻寬 **>83×** Bode-Fano 上限；LN Y∠36° 切、降伏應力 **>50 MPa**；元件 **10 cm** 級 vs 波長 **>1 km** | | [Nature Comm. 2019](https://www.nature.com/articles/s41467-019-09680-2) |
| StimDust | 體積 **6.5 mm³**；power-to-stimulation 效率 **82%**；每秒 **60** 個超音波脈衝 | 單顆壓電晶體同時受電＋backscatter | [arXiv 1807.07590](https://arxiv.org/pdf/1807.07590) |
| 穿金屬壁 | **17.37 Mbps + 50 W**（63.5 mm 鋼）；早期 **12.4 Mbps + 32.5 W**（6.3 cm 鋼） | | [IEEE UFFC 6396499](https://ieeexplore.ieee.org/document/6396499/) |
| EMI-SHM 工作頻段 | **30–400 kHz** 導納簽章 | PZT 同時是致動器與感測器 | [Wiley ACE 2010, 429148](https://onlinelibrary.wiley.com/doi/10.1155/2010/429148) |
| Qualcomm 3D Sonic | **24 × 8** PMUT 陣列；180 nm CMOS | TX/RX 模式切換於同一組電極 | [Yole 樣本報告](https://medias.yolegroup.com/uploads/2019/07/SP19465-YOLE_Qualcomm-3D-Sonic-Sensor-Fingerprint_Sample.pdf) |
| xMEMS Skyline | 開孔等效 **1.1 mm²**（雙顆 1.3 mm²）；100 Hz 衰減 **up to 25 dB** | 固態 MEMS 閥 | [audioXpress](https://audioxpress.com/news/xmems-announces-world-s-first-solid-state-mems-dynamicvent-enabling-active-ambient-control-for-next-generation-tws-and-hearing-aids) |
| xMEMS Cypress | 低頻 SPL **>130 dB** | 單片單體、sound-from-ultrasound | [xMEMS 新聞稿](https://xmems.com/press-release/xmems-announces-mass-production-readiness-of-cypress-the-worlds-first-full-range-mems-speaker-for-wireless-earbuds/) |
| TDK PowerHap | 壓力偵測 **≤25 N**；激振 **1 Hz–1000 Hz** | 免外掛觸控感測器 | [TDK](https://product.tdk.com/en/products/sw_piezo/haptic/powerhap/index.html) |
| Boréas CapDrive | 比 LRA 省電 **20×**、比競品壓電驅動 IC 省電 **10×** | 廠商宣稱，未獨立驗證 | [Boréas](https://www.boreas.ca/pages/capdrive-technology) |
| HEAD i.S18 | 振動衰減 **50%** vs 一般球拍 **20%** | 廠商宣稱；產品已停產 | [EE Times](https://www.eetimes.com/piezoelectric-rackets-add-professional-oomph/) |
| 壓電變壓器市場規模 | **各家報告互相矛盾**：USD 220.5 M(2025)→465.8 M(2033) @9.8%；USD 0.57 B(2023)→1.88 B(2030) @20.5%；~USD 500 M(2025)→950 M(2033) @8% | **低可信度，僅供參考** | [futuremarketreport](https://www.futuremarketreport.com/industry-report/piezoelectric-transformers-market)、[verifiedmarketreports](https://www.verifiedmarketreports.com/product/piezoelectric-transformers-market/) |

---

## 4. 「新能力型」應用機會

### 4.1 單顆陶瓷體的「高壓場產生器」：冷電漿 / 離子源 / 靜電致動偏壓

- **新能力是什麼**：一顆 47.3 × 20 × 20 mm 的多層 Rosen 型壓電陶瓷，用 **12–24 Vpp** 的低壓正弦輸入，直接在輸出端產生 **up to 15 kV** 並點燃大氣壓冷電漿，電漿溫度維持 **<50 °C**，可處理熱敏材料。
- **為什麼以前做不到**：要在這個體積、這個重量、這個輸入電壓下產生 15 kV，磁性變壓器需要繞組、鐵芯、絕緣距離與屏蔽；壓電體則靠「機械共振儲能 + 輸出段陶瓷本身即為高壓絕緣體」在單一單體內完成。壓電變壓器的先天優勢正是「無繞組、低 EMI、低外形」。
- **是否真的非替代性**：**是（高信心）**。這不是「更小的變壓器」，而是「把升壓器與電漿源合併成同一顆元件」——輸出電極就是放電電極，中間沒有第二個零件。同樣的邏輯可延伸到離子風扇、臭氧源、質譜離子源、MEMS 靜電致動的高壓偏壓源。
- **誰在做**：TDK Electronics（CeraPlas HF），與 relyon plasma 合作生產。
- **TRL**：**9（已量產、有 DigiKey 通路）**。
- **市場訊號**：TDK 將冷電漿列為獨立產品目錄（表面處理），並在企業級 featured story 推醫療應用。
- **技術難點**：硬質 PZT 與銅內電極共燒的製程；輸出端功率受材料非線性損耗與溫升限制；負載（電漿阻抗）高度非線性，需要跟蹤共振點的驅動 IC。
- **對客戶的意義**：這條路**沒有被排除**（不是取代電感做 DC-DC），而且已被 TDK 佔住。切入點應是「TDK 沒做的輸出型態」——例如更高頻、更小尺寸、或針對半導體/面板製程的點式電漿清洗。

### 4.2 壓電共振器當「機械天線」：VLF/ULF 發射

- **新能力是什麼**：把壓電體同時當作（被動）高 Q 機械共振腔與（主動）輻射用電偶極。實測在同電尺寸下輻射效率 **>300 倍**於既有技術；更關鍵的是**用時間調變共振本身，把頻寬推到 Bode-Fano 被動上限的 83 倍以上**——這是「主動地改變一個被動元件的參數」才做得到的事。
- **為什麼以前做不到**：VLF 波長 >1 km，傳統天線在 10 cm 尺度下輻射效率趨近於零，且必須外掛巨大的阻抗匹配網路。壓電輻射體「自己在聲波長上共振」，直接省掉匹配網路。
- **是否真的非替代性**：**是（高信心）**。這是被動網路理論（Bode-Fano）的**繞過**，不是元件微縮。
- **誰在做**：Nature Communications 2019（Kemp, Franzi, Haase 等，鈮酸鋰 Y∠36° 切，降伏應力 >50 MPa）；上游計畫為 DARPA **AMEBA**（A Mechanically Based Antenna，2017 起）。
- **TRL**：**4–5**（實驗室驗證／國防原型）。
- **市場訊號**：DARPA 計畫、後續多鐵性（multiferroic）機械天線專利持續產出（如 US12424736「Portable resonant multiferroic magnetoelectric antenna for ULF/VLF communication」）。
- **技術難點**：功率／應力上限（材料降伏）；調變導致的機械疲勞；發射效率仍遠低於全尺寸天線，只有在「尺寸受限」場景才贏。
- **對客戶的意義**：軍規／水下／地下通訊，台灣廠商切入門檻高（客戶、認證、法規），但**這是最乾淨的「新能力」示範**，可作為技術敘事的錨點。

### 4.3 mm³ 級超音波植入物：同一顆壓電同時受電與回傳資料

- **新能力是什麼**：StimDust 體積 **6.5 mm³**，其中一顆壓電晶體同時負責 (a) 把外部超音波的機械功率轉成電力（power-to-stimulation 效率 **82%**）與 (b) 藉由改變自身反射特性做 backscatter 通訊。Neural Dust 原型尺寸約 3 mm × 1 mm × 0.8 mm，每秒 60 個超音波脈衝驅動。
- **為什麼以前做不到**：mm 級電感線圈在生物組織中的 RF 耦合效率極差、且 RF 在組織中衰減嚴重；超音波在組織中的波長短、衰減低，且**同一顆壓電體天生就是雙向換能器**，因此「受電」與「回傳」不需要兩個元件。
- **是否真的非替代性**：**是（高信心）**。在 mm³ 尺度下沒有可用的電磁替代方案。
- **誰在做**：UC Berkeley（Neural Dust / StimDust），DARPA 資助；後續有 backscatter 通訊建模與體積效率最佳化的研究。
- **TRL**：**4–6**（動物實驗已完成，臨床未定）。
- **技術難點**：聲學對準與組織介面阻抗匹配；長期封裝；backscatter 的資料率上限；體積效率與 CMOS 功耗的取捨。
- **對客戶的意義**：這是壓電「主動/被動兩用」最強的產品化敘事，但屬醫材，法規週期長。

### 4.4 穿金屬壁的「功率＋資料」同軸通道

- **新能力是什麼**：在密閉金屬壓力容器、核反應器、潛艦艙壁上，不打孔就把 **50 W 功率與 17.37 Mbps 資料**同時送過 **63.5 mm 厚鋼壁**。部分嵌入式感測系統更進一步：**只用一顆壓電換能器**，靠頻率多工同時做不間斷的能量採集與 backscatter 通訊。
- **為什麼以前做不到**：金屬是電磁的完美屏蔽，無線電無法穿透；有線則必須破壞氣密／耐壓完整性。聲波是唯一的通道，而壓電體同時是「聲波激發器」與「聲波接收器」。
- **是否真的非替代性**：**是（高信心）**，前提是「不能打孔」這個約束成立。
- **誰在做**：RPI / Lawry 等（IEEE UFFC 2013），另有專利 [US20150049587A1](https://patents.google.com/patent/US20150049587)「Full-duplex ultrasonic through-wall communication and power delivery system with frequency tracking」、[US10594409B2](https://patents.google.com/patent/US10594409B2/en)（曲面金屬）。
- **TRL**：**5–6**（多篇實體原型；商業產品未見公開型號，**查無**）。
- **技術難點**：聲通道的多重反射與駐波導致嚴重 ISI，需要自動增益／載波控制；溫度造成通道漂移需頻率追蹤；耦合層（couplant）長期可靠度。
- **對客戶的意義**：工業利基但真實（石化、核能、離岸），單價容忍度高，**壓電單價高的劣勢在此不成立**。

### 4.5 EMI（電機械阻抗）結構健康監測：同一片 PZT 兼致動器與感測器

- **新能力是什麼**：把一片 PZT 貼上結構、掃 **30–400 kHz**，量到的電導納簽章直接反映主結構的機械阻抗，等效於取得結構的 FRF——**不需要任何外部感測器、不需要激振器**。
- **為什麼以前做不到**：傳統模態測試需要激振器＋加速度計＋線束；EMI 法把三者塌縮成一片陶瓷加一台阻抗分析儀。
- **是否真的非替代性**：**部分（中信心）**。功能上是替代（取代激振器＋感測器），但在「埋進混凝土裡的 smart aggregate」「複合材料內埋」這類**外部感測器物理上放不進去**的場景，才是真新能力。
- **誰在做**：學術界為主；專利 [US9664649B2](https://patents.google.com/patent/US9664649B2/en)（SHM system employing electromechanical impedance technology）；WiAMS 無線阻抗／導納監測裝置＋埋入式 smart aggregates。
- **TRL**：**5–7**（土木領域有現場部署，但無主流商品化系統）。
- **技術難點**：**溫度是頭號敵人**——已有專門研究指出溫度對阻抗簽章的影響足以掩蓋損傷訊號；黏著層老化；簽章與損傷位置的反演問題未解。

### 4.6 「同一顆壓電體上時間多工：感測 / 採集 / 致動」的自供電節點

- **新能力是什麼**：以 MFC 壓電片為單一多功能元件，在儲能不足時切到能量採集模式、儲能足夠時切到應變感測模式，形成完全自供電的節點；SSD 家族的 self-powered SSDI 更證明「只犧牲少量阻尼效能就能做到完全不需外部電源」。
- **為什麼以前做不到**：過去 harvester、sensor、actuator 是三個零件三套線路；時間多工＋自供電開關電路（僅需微瓦級）讓它們塌縮成一片。
- **是否真的非替代性**：**否／偏替代（低—中）**。這主要是整合度與 BOM 的改善，不是全新能力。**權重應調低**，除非把場景限定在「布線不可能」的旋轉件、密封件、拋棄式標籤。
- **誰在做**：[IEEE 7938680](https://ieeexplore.ieee.org/document/7938680/)（單一壓電換能器時間多工做應變感測與能量採集）；SSHC/SSHI IC 學界（Cambridge、NTU 等）。
- **TRL**：**3–5**。
- **技術難點**：採集功率（µW–mW 級）與致動所需功率（mW–W 級）差 3 個數量級，「自供電致動」在多數場景不成立。

### 4.7 用主動電路合成「不存在的被動元件」：負電容 / 合成阻抗 / 可程式化剛性

- **新能力是什麼**：以 OP-AMP 合成負電容，或以 DSP＋壓控電流源合成任意 shunt 阻抗，使壓電體對外呈現「自然界不存在的」阻抗，進而**即時改變結構的等效剛性與阻尼**（可正可負），做出可調帶隙的壓電超材料、可程式化 meta-ring。
- **為什麼以前做不到**：被動元件的阻抗是固定的；負電容讓 shunt 抵消壓電的固有電容 C0，把機電耦合「放大」到接近材料理論上限。
- **是否真的非替代性**：**是（中信心）**——「可即時改變剛性符號」確實是新能力；但**要誠實承認它需要供電、會不穩定，所以它不是被動元件**。
- **誰在做**：學術界（Penn State、法國 INSA/LGEF 系、中國多所）；2024–2025 有大量負電容超材料論文（[JSV 2024](https://www.sciencedirect.com/science/article/abs/pii/S0022460X2400107X)、[MSSP 可程式化 meta-ring](https://www.sciencedirect.com/science/article/abs/pii/S0888327023004259)）。
- **TRL**：**3–4**。
- **技術難點**：穩定性邊界緊、OP-AMP 飽和、功耗隨增益上升、對 C0 漂移敏感。

---

## 5. 反面證據、失敗案例與物理上限

1. **最完整的商業失敗紀錄：HEAD Intelligence 網球拍。** 這是「self-powered piezoelectric damping」少數真正大量上市的消費品，有專利、有臨床研究、有 50% vs 20% 的衰減宣稱，**結果停產，推測因成本**。這直接命中客戶的核心疑慮：壓電元件單價高，在消費品上打不過純機械／黏彈性方案。
2. **CCFL 壓電變壓器：技術沒輸，應用消失了。** 峰值時 25–30% 的 CCFL 背光電路採用壓電變壓器，Toshiba/NEC/Hitachi/Panasonic/Apple 都是客戶；LED 取代 CCFL 後，整條供應鏈（含專用 IC）停產。**教訓：壓電元件的商業命運被單一應用綁死，缺乏橫向遷移能力。**
3. **納米定位市場拒絕 self-sensing。** PI 現役產品仍用電容式感測器做 direct metrology，官方理由就是「傳動鏈誤差與漂移不影響量測」。SSA 的橋式電路在 Cp 隨溫濕度／負載漂移時會輸出被汙染的機械響應，甚至讓閉迴路不穩定——這不是工程細節，是原理性缺陷。
4. **被動 shunt 的電感牆。** 10–100 nF 對應 10–1000 H；這種電感的體積、重量與寄生電阻，在「輕量化」場景（航太）自我否定。合成電感（Riordan gyrator / 虛擬電感）能解體積，但要供電、要 OP-AMP，被動性隨即消失。
5. **負電容的主動性悖論。** 兩個公認問題：主動元件導致的動態不穩定、大激振下 OP-AMP 飽和；OP-AMP 功耗隨控制增益上升。有研究反而建議「讓 OP-AMP 跑在飽和區」以換穩定度，這說明線性工作區的穩定裕度有多窄。
6. **線性 shunt 的失諧脆弱性。** 綜述明確指出線性 shunt 對參數變動極敏感，電氣共振一旦偏離激振頻率就失效；SSD 家族之所以存在，本質就是為了繞開這個弱點——代價是需要開關與偵測電路。
7. **壓電變壓器的頻寬牆擋住了 gate driver 這條路。** bulk-mode PT 工作頻率 <數十 MHz、Qm ≈ 1000，固有頻寬只有數十 kHz，**不足以支援 WBG 元件所需的 sub-µs 轉態**。這是為什麼隔離式閘極驅動至今仍由 coreless transformer（Infineon EiceDRIVER，CMTI 100 kV/µs）與電容／RF 耦合（onsemi NCP5156x，>200 V/ns CMTI、5 kV 隔離）把持——**壓電在這裡是輸的**。想走「壓電變壓器做隔離」必須先解頻寬。
8. **壓電變壓器的負載相依性。** 負載失配（例 6 Ω 或 40 Ω）可讓損耗增加 50%、效率從 98%+ 掉到 97%；PT 的電壓增益與效率同時強烈依賴負載，這與磁性變壓器「增益基本上等於匝比」的行為完全不同，對系統設計是負擔（未驗證，來源為二手摘錄）。
9. **材料上限是硬的：效率 ∝ k² × Qm。** 這條關係同時決定了 PT、壓電共振器 DC-DC 與 shunt 阻尼的天花板。想突破只能換材料（鈮酸鋰、單晶 PMN-PT）或換振動模態，而不是換電路拓樸。
10. **自供電致動在功率上不成立。** 壓電採集典型輸出在 µW–mW（例：鞋墊 3.6 mW @ 1 Hz、231 µW），而有意義的致動需要 mW–W；「同一顆元件自己採集自己驅動」在絕大多數場景是數量級不足的幻覺。self-powered SSDI 之所以可行，是因為它只需要驅動一顆開關，不需要注入能量。
11. **成本面查無公開數據。** 本次搜尋**查無**壓電元件（PZT 多層片、MFC、PT）的公開單價 USD 數據，也**查無**與磁性元件的逐項 BOM 比較。壓電變壓器的市場規模報告彼此矛盾達 3 倍以上（220 M vs 570 M vs 500 M，年份與 CAGR 都不一致），**不應作為投資依據**。

---

## 6. 未解問題（給下一輪研究）

1. **成本**：PZT 多層致動片、MFC、Rosen 型 PT 的實際單價區間（1 k / 10 k / 100 k 量）？與同功能磁性元件、加速度計、電容式感測器的 BOM 差距？（本輪查無）
2. **CeraPlas 的實際出貨量與售價**，以及 TDK 的專利佈局範圍——若要做「壓電高壓場產生器」，繞得過去嗎？
3. **穿金屬壁供電＋通訊有沒有商業產品？** 本輪只找到論文與專利，**查無**具名商品型號。若真的沒有，是市場太小還是技術未過門檻？
4. **Boréas / TDK PowerHap 的實際年出貨量與 ASP**，以及 self-sensing 觸覺在汽車面板的滲透率。Synaptics 合作案是否已有量產機種？
5. **壓電變壓器頻寬問題有沒有突破路徑**（薄膜化、更低 Qm 材料、多模態）？arXiv 2511.13412 的 microwave-acoustic 方案數字（資料率、隔離電壓、CMTI、效率）需要取得全文核對。
6. **k² × Qm 的材料前沿**：LiNbO₃、PMN-PT、AlScN 的實測 k²·Qm 乘積各是多少？溫度範圍與可靠度？
7. **APPN 的量化效益**：Wang 團隊宣稱 shunt 可「增強主動控制權限」，但本輪**查無**具體百分比或 dB 數字，需要取得 IOP SMS 10(4) 325 與 DTIC ADA429566 全文。
8. **EMI-SHM 的溫度補償**目前最好能做到什麼程度？是否有商品化的補償演算法／標準？
9. **參數放大（18.2 dB 增益、Q×14）能否在巨觀壓電元件上重現**，還是僅限 MEMS 尺度？
10. 需要在網路可達的環境重跑一次 WebFetch，核對本文標「未驗證」的所有數字（特別是 PT 效率 98.3% / 40 W/cm³ / 負載失配 +50% 損耗三項）。

---

## 7. 來源清單

1. [Piezoelectric Transformers: An Historical Review — Actuators 2016, 5(2), 12](https://www.mdpi.com/2076-0825/5/2/12) — Rosen 型起源、CCFL 時代 25–30% 市佔、客戶名單與 LED 取代後的產業崩解，是壓電變壓器產業史的標準引用。
2. [An Overview of Piezoelectric Self-Sensing Actuation for Nanopositioning Applications — IEEE 8889413](https://ieeexplore.ieee.org/document/8889413/) — SSA 電路分類（橋式 / 觀測器）、電容漂移導致訊號汙染與閉迴路不穩的原理性說明。
3. [Physik Instrumente — Capacitive Sensors](https://www.physikinstrumente.com/en/expertise/technology/sensor-technologies/capacitive-sensors) — 高階納米定位仍採外部電容式 direct metrology 的反面證據。
4. [Boréas Technologies BOS1901 Piezo Haptic Driver](https://www.boreas.ca/products/bos1901-piezo-haptic-driver) — 市場上唯一同時觸發觸覺與感測按壓力的壓電驅動 IC。
5. [Boréas CapDrive Technology](https://www.boreas.ca/pages/capdrive-technology) — 比 LRA 省電 20×、比競品壓電 IC 省電 10× 的廠商宣稱。
6. [Boréas 四通道整合感測驅動 IC 新聞稿（BOS0614, 2022）](https://www.prnewswire.com/news-releases/boreas-technologies-announces-four-channel-haptic-driver-with-integrated-sensing-301563047.html) — 產品線擴張與市場訊號。
7. [Synaptics × Boréas 壓電觸控板合作新聞稿](https://www.synaptics.com/company/news/synaptics-partners-boreas-technologies-deliver-high-performance-piezo-haptic-trackpads) — 大廠採用訊號。
8. [TDK PowerHap Actuators 產品頁](https://product.tdk.com/en/products/sw_piezo/haptic/powerhap/index.html) — 致動器內建感測、≤25 N 壓力偵測、1 Hz–1000 Hz 激振。
9. [TDK Electronics — Cold plasma from a single component](https://www.tdk-electronics.tdk.com/en/373562/tech-library/articles/applications-cases/applications-cases/cold-plasma-from-a-single-component/1109546) — CeraPlas 12–24 Vpp → 15 kV、<50 °C、多層 Rosen 型硬 PZT 共燒銅電極。
10. [TDK CeraPlas HF 發表新聞稿（2018-11-13）](https://www.globenewswire.com/news-release/2018/11/13/1650541/0/en/TDK-Introduces-CeraPlas-HF-Compact-Cold-Plasma-Generator-Element.html) — 47.3 × 20 × 20 mm 尺寸與規格。
11. [TDK × relyon plasma 合作新聞稿](https://www.tdk-electronics.tdk.com/en/373388/company/press-center/press-releases/press-releases/piezo-transformers-and-plasma-generators-tdk-cooperates-with-relyon-plasma-to-develop-and-manufacture-cutting-edge-plasma-solutions/1416224) — 產業化路徑與夥伴。
12. [A high Q piezoelectric resonator as a portable VLF transmitter — Nature Communications 2019](https://www.nature.com/articles/s41467-019-09680-2) — 輻射效率 >300×、頻寬 >83× Bode-Fano、LN Y∠36°、10 cm 元件對 >1 km 波長。
13. [DARPA — Underwater Radio, Anyone?（AMEBA 計畫）](https://www.darpa.mil/news/2016/underwater-radio) — 機械天線計畫的官方脈絡與 ULF/VLF 頻段定義。
14. [StimDust: A mm-scale implantable wireless precision neural stimulator — arXiv 1807.07590](https://arxiv.org/pdf/1807.07590) — 6.5 mm³、82% power-to-stimulation、單顆壓電受電＋backscatter。
15. [DARPA — Implantable "Neural Dust"](https://www.darpa.mil/news/2016/implantable-neural-dust) — 3 × 1 × 0.8 mm 原型與壓電晶體雙用途的官方說明。
16. [A high-performance ultrasonic system for simultaneous data and power through solid metal barriers — IEEE UFFC 6396499](https://ieeexplore.ieee.org/document/6396499/) — 17.37 Mbps + 50 W / 63.5 mm 鋼；早期 12.4 Mbps + 32.5 W。
17. [US20150049587A1 — Full-duplex ultrasonic through-wall communication and power delivery with frequency tracking](https://patents.google.com/patent/US20150049587) — 全雙工穿壁供電＋通訊的專利路徑。
18. [US9664649B2 — SHM system employing electromechanical impedance technology](https://patents.google.com/patent/US9664649B2/en) — EMI 法的專利化證據。
19. [Structural Health Monitoring Using High-Frequency Electromechanical Impedance Signatures — Adv. Civil Eng. 2010](https://onlinelibrary.wiley.com/doi/10.1155/2010/429148) — PZT 作為 collocated actuator-sensor、30–400 kHz 導納簽章。
20. [溫度對阻抗式 SHM 壓電感測器的影響 — PMC3926611](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3926611/) — EMI 法的溫度脆弱性反面證據。
21. [A Review on Vibration Control Using Piezoelectric Shunt Circuits — MDPI Appl. Sci. 15(11) 6035, 2025](https://www.mdpi.com/2076-3417/15/11/6035) — passive / semi-passive / semi-active / active 四分類與 2019 年後進展。
22. [Shunt Piezoelectric Systems for Noise and Vibration Control: A Review — Frontiers in Built Environment 2019](https://www.frontiersin.org/journals/built-environment/articles/10.3389/fbuil.2019.00064/full) — shunt 家族的系統性整理與失諧敏感度。
23. [Vibration and noise control using shunted piezoelectric transducers: A review — MSSP 112:359, 2018](https://www.sciencedirect.com/science/article/abs/pii/S0888327018302437) — 另一份標準綜述。
24. [Direct Adaptive SSDV Circuit for Piezoelectric Shunt Damping — IEEE 9797239](https://ieeexplore.ieee.org/document/9797239/) — SSDV 16.1 dB vs SSDI 8 dB 的量化對比。
25. [Semi-passive piezoelectric noise control by SSDV](https://www.academia.edu/6085630/Semi_passive_piezoelectric_noise_control_in_transmission_by_synchronized_switching_damping_on_voltage_source) — SSDV 原始效能數據來源。
26. [Bidirectional energy-controlled piezoelectric shunt damping — Int. J. Mech. Syst. Dyn. 2024](https://onlinelibrary.wiley.com/doi/10.1002/msd2.12101) — 2024 年 SSD 家族最新變體。
27. [Reducing the inductance requirements of piezoelectric shunt damping systems](https://www.researchgate.net/publication/231126028_Reducing_the_inductance_requirements_of_piezoelectric_shunt_damping_systems) — 10–1000 H 電感牆的專門處理。
28. [Synthetic impedance for implementation of piezoelectric shunt-damping circuits — Fleming & Moheimani](https://www.researchgate.net/publication/3382744_Synthetic_impedance_for_implementation_of_piezoelectric_shunt-damping_circuits) — DSP＋VCCS 合成任意 shunt 阻抗的原始工作。
29. [An Autonomous Piezoelectric Shunt Damping System — Precision Mechatronics Lab](https://www.precisionmechatronicslab.com/wp-content/publications/D03a.pdf) — 自主式 shunt 阻尼系統。
30. [Strategies for reducing operational amplifier … negative capacitance — ECCOMAS SMART 2023](https://files.eccomasproceedia.org/papers/smart-2023/SM23_444339.pdf) — 負電容不穩定、飽和與功耗的量化討論。
31. [Power output and dissipation of a negative capacitance shunt — Penn State](https://pure.psu.edu/en/publications/power-output-and-dissipation-of-a-negative-capacitance-shunt-coup/) — 負電容 shunt 的功率收支。
32. [Active-passive hybrid piezoelectric networks for vibration control: comparisons and improvement — Smart Mater. Struct. 10(4) 325, 2001](https://iopscience.iop.org/article/10.1088/0964-1726/10/4/325) — APPN 概念的核心文獻（Penn State, K. W. Wang）。
33. [An Integrated Active-Parametric Control Approach for APPN with Variable Resistance — JIMSS 1998](https://journals.sagepub.com/doi/10.1177/1045389X9800900708) — Morgan & Wang 的可變電阻 APPN。
34. [Active Authority Enhancement of Piezoelectric Actuator Design via Mechanical Resonance — DTIC ADA429566](https://apps.dtic.mil/sti/pdfs/ADA429566.pdf) — 共振式致動系統同時取得高主動權限與穩健性。
35. [Comparison of the Mason and KLM Equivalent Circuits — JPL/NASA](https://ndeaa.jpl.nasa.gov/ndeaa-pub/USDC/Kk_1-comparison.pdf) — 壓電體 1 電端口 + 2 聲端口的三端口網路觀念。
36. [Equivalent Circuits for Resonators and Transducers — DTIC ADA231520](https://apps.dtic.mil/sti/tr/pdf/ADA231520.pdf) — BVD／Mason 等效電路的完整推導。
37. [An Inductorless Bias-Flip Rectifier for Piezoelectric Energy Harvesting — Cambridge repository (Du et al.)](https://www.repository.cam.ac.uk/bitstream/1810/266131/1/201609_SijunDU_revised.pdf) — SSHC 9.7× 提升、8 顆切換電容、80% 翻轉效率、0.35 µm CMOS。
38. [Advances in Interface Circuits for Self-Powered Piezoelectric Energy Harvesting Systems — MDPI Sensors 25(13) 4029, 2025](https://www.mdpi.com/1424-8220/25/13/4029) — SSHI/SSHC/SECE 的 2025 年最新彙整（7.62×、417% 等）。
39. [Study of a Low-Power-Consumption Piezoelectric Energy Harvesting Circuit Based on Synchronized Switching — MDPI Energies 12(16) 3166](https://www.mdpi.com/1996-1073/12/16/3166) — 231 µW / 2.89× 實測。
40. [Self-Powered Synchronized Switching Interface Circuit for Piezoelectric Footstep Energy Harvesting — PMC9966393](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9966393/) — 83.02% 效率、3.6 mW @ 1 Hz。
41. [Single Piezoelectric Transducer as Strain Sensor and Energy Harvester Using Time-Multiplexing — IEEE 7938680](https://ieeexplore.ieee.org/document/7938680/) — 單一 MFC 時間多工做感測與採集。
42. [A Study on Parametric Amplification in a Piezoelectric MEMS Device — PMC6356750](https://pmc.ncbi.nlm.nih.gov/articles/PMC6356750/) — 18.2 dB 增益、Q×14、非線性阻尼飽和。
43. [Efficient parametric amplification in micro-resonators with integrated piezoelectric actuation and sensing — ENSAM](https://sam.ensam.eu/handle/10985/8827) — 整合致動＋感測的參數放大原始工作。
44. [Piezoelectric resonators in DC-DC converters: current status and limits — Power Electronics News](https://www.powerelectronicsnews.com/piezoelectric-resonators-in-dc-dc-converters-current-status-and-limits/) — 1340 W/cm³、97% @ 89 W、效率 ∝ k²·Qm（客戶已排除路線的對照數據）。
45. [Optimized Resonators for Piezoelectric Power Conversion — Stanford SUPERLAB](https://superlab.stanford.edu/publication/2021-03-18-Optimized-Resonators-Piezoelectric_Braun/index.html) — Rivas-Davila 團隊的材料與振動模態最佳化。
46. [A hybrid piezoelectric resonator-based DC-DC converter — Nature Communications (2026)](https://www.nature.com/articles/s41467-026-70494-0) — 最新混合式壓電共振器轉換器（僅作技術前緣參考）。
47. [High-Efficiency Isolated Piezoelectric Transformers for Magnetic-less DC-DC Power Conversion](https://www.researchgate.net/publication/391376205_High-Efficiency_Isolated_Piezoelectric_Transformers_for_Magnetic-less_DC-DC_Power_Conversion) — 98.3% 峰值效率、>40 W/cm³、負載失配 +50% 損耗（**數字未一手驗證**）。
48. [Microwave-acoustic-based isolated gate driver for power electronics — arXiv 2511.13412](https://arxiv.org/pdf/2511.13412) — 明確指出 bulk-mode PT 因 Qm≈1000、頻寬僅數十 kHz 而不敷 WBG 閘極驅動。
49. [Infineon EiceDRIVER 隔離閘極驅動器](https://www.infineon.com/products/power/gate-driver-ics/galvanic-isolated-gate-driver) — coreless transformer、100 kV/µs CMTI，壓電方案的競爭基準。
50. [EE Times — Piezoelectric rackets add professional oomph](https://www.eetimes.com/piezoelectric-rackets-add-professional-oomph/) — HEAD i.S18 的 50% vs 20% 衰減宣稱。
51. [An Extended Study … Tennis Rackets with Active Damping Technology on Tennis Elbow](https://www.researchgate.net/publication/226285635_An_Extended_Study_Investigating_the_Effects_of_Tennis_Rackets_with_Active_Damping_Technology_on_the_Symptoms_of_Tennis_Elbow) — i.S18/i.X16/Protector OS 型號與停產說明。
52. [US6974397B2 — Racket with self-powered piezoelectric damping system](https://patents.google.com/patent/US6974397B2/en) — HEAD 自供電壓電阻尼的專利。
53. [WO2010091902A1 — Method for determining a needle closing in a piezo injector](https://patents.google.com/patent/WO2010091902A1/en) — 用壓電元件自身聲訊號判定針閥關閉時刻。
54. [Continental 新一代共軌壓電噴油嘴（直驅＋閉迴路針閥控制）](https://www.greencarcongress.com/2008/05/continental-int.html) — 量產級 self-sensing 致動的汽車案例。
55. [Smart ultrasonic transducer for wire-bonding applications](https://www.sciencedirect.com/science/article/abs/pii/S025405840200038X) — 內嵌 1 × 1 × 0.245 mm PZT 的智慧換能器與二次諧波製程監控。
56. [Qualcomm 3D Sonic Sensor Fingerprint — Yole 樣本報告](https://medias.yolegroup.com/uploads/2019/07/SP19465-YOLE_Qualcomm-3D-Sonic-Sensor-Fingerprint_Sample.pdf) — 24×8 PMUT 陣列、180 nm CMOS。
57. [Thin-film PMUTs: a review of over 40 years of research — Microsystems & Nanoengineering 2023](https://www.nature.com/articles/s41378-023-00555-7) — PMUT 收發共用元件的技術總覽。
58. [xMEMS Cypress 量產就緒新聞稿](https://xmems.com/press-release/xmems-announces-mass-production-readiness-of-cypress-the-worlds-first-full-range-mems-speaker-for-wireless-earbuds/) — sound-from-ultrasound 調變／解調同體、>130 dB SPL。
59. [xMEMS Skyline 固態 MEMS DynamicVent — audioXpress](https://audioxpress.com/news/xmems-announces-world-s-first-solid-state-mems-dynamicvent-enabling-active-ambient-control-for-next-generation-tws-and-hearing-aids) — 1.1 mm² 等效開孔、100 Hz 衰減 25 dB。
60. [Vibration suppression of a state-of-the-art wafer gripper — arXiv 2212.01854](https://arxiv.org/abs/2212.01854) — 半導體設備上壓電阻尼的實作（目標 ≥5% 阻尼比，PPF 控制）。
61. [Piezoelectric Shunt Damping for a Planar Motor Application under Cryogenic Conditions — MDPI Actuators 13(10) 405](https://www.mdpi.com/2076-0825/13/10/405) — 極端環境下 shunt 阻尼的近期實作。
62. [Piezoelectric Transformers Market 報告（futuremarketreport）](https://www.futuremarketreport.com/industry-report/piezoelectric-transformers-market) 與 [verifiedmarketreports 版本](https://www.verifiedmarketreports.com/product/piezoelectric-transformers-market/) — **兩份報告數字互相矛盾達 3 倍，僅列為低可信度市場訊號。**
