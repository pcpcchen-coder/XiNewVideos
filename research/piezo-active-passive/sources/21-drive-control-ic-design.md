# 工程實作面：驅動與控制電路/IC——要讓「兩用元件」真的能用，電路端得解決什麼

> 一句話結論：現貨已經能讓你在**兩週內**做出「驅動＋自感測同體」的 PoC（Boréas BOS1921／BOS0614、ADI MAX77501），但**自研 IC 的核心手法（帶電感的雙向 boost-buck 從負載電容回收能量）已被 Harvard US10931199B2 明確請求，且 Boréas 宣稱 30+ 專利**；真正值得投入的技術缺口不在「怎麼把電打進去」，而在「**大訊號下的操作點選擇（fs 與 fp 之間才有最高 Qm）**」與「**開關式含能量回收驅動下，既有的遲滯／自感測補償模型是否還成立**」——後者本輪窮盡檢索後仍**完全查無文獻**，這既是最大風險，也是最乾淨的技術空白。

---

## 0. 研究方法與限制（誠實揭露）

1. **本輪執行 52 次 WebSearch**（前一版僅 2 次，內容已全部作廢重寫）。WebFetch 在本環境全面 403，**沒有任何一手 PDF／原文查核**，所有外部事實均來自搜尋引擎回傳的結果摘要。
2. 標記慣例：
   - **【已檢索】**＝本輪搜尋摘要直接回傳，附 URL。因為未開原文，摘要本身可能有誤讀風險，凡屬關鍵數字我會註明其來源型態（廠商宣稱／論文摘要／通路頁）。
   - **【轉引】**＝引用本專案同目錄 `01-pt-power-conversion-sota.md`、`02-dual-use-active-passive-concept.md` 已列 URL，我未親自驗證。
   - **【查無】**＝本輪確實搜過但未取得。
3. **本輪確認查無的項目**（不編造）：
   - **儀器公開報價全部查無**。Keysight E4990A 官網明示「超過價格門檻，須聯繫採購團隊」；Polytec 新機價、Trek/Advanced Energy 2220 新機價、Aigtek ATA-2022H 價格皆無公開數字。**只取得一筆二手參考點**（見 §3）。
   - **COMSOL 授權價格**：搜尋額度在此耗盡，查無。
   - **ROHM 專用壓電驅動 IC**：搜尋未回傳任何對應產品，判定 ROHM 在此品類**查無現貨**。
   - **Boréas 各料號的實際效率百分比（η）**：全部型錄與新聞稿只給「相對倍數」（10×、9–11×、90% 電流下降），**沒有任何一個絕對效率數字**。這是重要的資訊不對稱訊號。
   - **開關式含能量回收驅動下遲滯模型是否成立**：專門搜尋一次，**零結果**。
4. 我沒有捏造任何專利號、論文標題、型號或價格。

---

## 1. 結論摘要

1. **CapDrive 的核心專利找到了，而且權利人不是 Boréas 而是 Harvard。** `US10931199B2「Driver for a circuit with a capacitive load」`，受讓人 **President and Fellows of Harvard College**，為 `PCT/US2016/053915「Driver for a High Voltage Capacitive Actuator」`（2016-09-27 申請）之接續案，主張 2015-09-28 與 2015-12-11 兩件臨時案優先權。發明人 Simon Chaput 即 Boréas 創辦人，該架構為其 Harvard 博士研究成果。【已檢索 S12/S15】
2. **該專利的請求標的直接覆蓋「主動能量回收」這件事本身，不只是某種實作。** 摘要載明：耦合至直流電壓源的**雙向同步功率轉換器**（第一開關＋第二開關＋電感元件），輸出峰值**至少為輸入電壓的兩倍**，以 boost-buck 方式運作——**正向 boost 模式把能量送進容性負載、反向 buck 模式把能量從負載取回**。若你的自研 IC 用「電感＋雙向半橋＋從壓電體回收」這個最自然的架構，撞牆機率極高。【已檢索 S12】
3. **但這道牆有明確的縫：ADI 已經在賣同類產品。** `MAX77501`（110 Vpk-pk 單端、2.8–5.5 V 輸入、可驅動 **2 µF**）官方描述其為「**energy recycling scheme which yields virtually no losses, except switching losses and finite RDS(ON)**」。ADI 在美國市場公開販售，代表這條路徑存在可迴避的實作空間（或已授權）。**這同時也是壞消息：市場已有兩家整合大廠，自研 IC 的差異化空間被壓縮。**【已檢索 S16】
4. **fs 還是 fp 的爭議，本輪找到明確答案，而且是好消息：兩者之間才是最佳點。** Shekhani & Uchino 實驗證實**最高機械品質因數出現在共振與反共振之間**，實測最高 Qm = **1900**；另一份 Rev. Sci. Instrum. 研究指出，以最佳頻率驅動相較於以共振頻率驅動，**所需功率降低 39%** 且溫升更小。物理解釋：反共振為定 D（電位移）驅動，機電損耗近乎為零；共振為定 E（電場）驅動，機電損耗大。【已檢索 S23/S24】**這實質上解掉了前一版列為「最核心架構矛盾」的問題——功率與致動不必打架，兩者都應該操作在 fs–fp 之間，只是最佳點不同。**
5. **傳統 PLL 追頻的失效模式已被具名記載，而且正好是「兩用元件」會遇到的情境。** 文獻明列三種失效：**失鎖（loss of lock）、誤鎖到反共振點、大追蹤誤差**，且「**重載換能器因負載機械損耗大而 Qm 降低**」時最容易發生。改良法為靜態電容寬頻補償（SCBC），追蹤精度 **±9 Hz** 且對反共振免疫。【已檢索 S21】兩用元件的定義就是負載會在兩種用途間切換 → 這正是 PLL 最脆弱的工況。
6. **遲滯不是問題，遲滯補償在開關式驅動下還成不成立才是問題。** 電荷驅動可把遲滯從電壓驅動的 **10–15% 壓到約 2%**，數位電荷放大器實測**降低 91%**；Prandtl–Ishlinskii 逆模型實測**降低約 90% 追蹤誤差**、線性度誤差 **10% → <1%**。但這些全部建立在線性放大器驅動下。**本輪專門搜尋「開關式 + 電荷回收驅動下的遲滯模型有效性」，零結果。**【已檢索 S19/S20；空白為本輪查無】
7. **「用壓電省掉電感」在驅動端會自我矛盾——這次有精確的物理界線。** 經電阻對電容充電，**恆有 50% 能量損失，與電阻值無關**（即使 R→0，損失也只是從熱轉為輻射）；唯一的例外是**經低電阻電感諧振（絕熱）充電，效率可趨近 100%**。文獻明載：開關式壓電功率放大器「**可回收儲存在致動器中約 50% 的電荷**」。**要突破一半必須放電感。**【已檢索 S17/S18】
8. **現貨的規格天花板已經清楚：190 Vpp（單通道，含感測）、120 V（車規）、60 V × 4 通道（含感測）、±80 V × 16 通道（超音波脈衝，無感測）。kV 級一顆都沒有。** 這確認了前一版的架構結論：**kV 必須由陶瓷體自己升壓（CeraPlas 12–24 Vpp → 20 kV），IC 側停在低壓 BCD，不必碰高壓製程。**【現貨規格為本輪已檢索；kV 為【轉引】D1-S9/D1-S25】

---

## 2. 現況：現貨驅動 IC 全盤點（本輪核心交付）

### 2.1 帶能量回收的壓電驅動 IC（唯二陣營）

| 料號 | 廠商 | 輸出 | 供電 | 感測 | 介面／特色 | 生命週期／通路 |
|---|---|---|---|---|---|---|
| **BOS1901** | Boréas | **190 Vpk-pk**；100 nF @190 Vpp/300 Hz 僅 **350 mW**；容性負載上限 **820 nF** | 3–5.5 V（數位 I/O 1.8–5.0 V） | 有（壓力感測） | SPI ＋ 64 樣本 FIFO；啟動 **<300 µs**；QFN／WLCSP | **DigiKey 標示 BOS1901CQR 已停產（obsolete）**；`BOS1901-KIT-B` 亦標示不再製造 |
| **BOS1921** | Boréas | 190 Vpk-pk | 3–5.5 V | **有**（進階感測，可做力回饋） | I²C/I³C；24-QFN 4×4；WLCSP **2.1×1.7×0.625 mm** | 在產；**DigiKey 列價 US$4.16**（單顆），Mouser 整卷 2500 顆 | 
| **BOS1931** | Boréas | 190 Vpk-pk | 3–5.5 V | **無**（僅驅動） | 啟動 <300 µs；散熱／微幫浦冷卻優化 | 在產（DigiKey product highlight, 2025） |
| **BOS0614** | Boréas | **60 V × 4 通道** | — | **有**，10 kSps 感測介面；按壓偵測延遲 **100 µs**；Zero Power Sensing 可從 SLEEP 喚醒 | I³C/I²C；波形合成器 WFS ＋ **2 kB on-chip RAM**；需外掛 **10 µH** 電感；4× GPIO 可做 open-drain 取代機械按鍵 | 在產 |
| **BOS1211** | Boréas | **120 V**（可驅 TDK PowerHap 120 V） | **12 V**（車用） | 有 | 整合 **low-side ＋ high-side NMOS 閘極驅動器供 buck-boost**（即功率 FET 外掛）；**已通過 AEC-Q100 Grade 2**；開發套件可堆疊 **4 片**驅動板 | 在產 |
| **MAX77501** | ADI／Maxim | **110 Vpk-pk 單端**；可驅 **2 µF** | 2.8–5.5 V 或單顆 Li+ | 未載明 | **25 MHz SPI**；記憶體播放＋即時串流；啟動 **600 µs**；SHUTDOWN **<1 µA** | 在產，有 `MAX77501EVKIT` |

**對客戶的三個直接可行動結論：**
- **不要再設計 BOS1901**，它在 DigiKey 已標為停產、其開發套件亦已停產。**要「驅動＋感測同體」請直接上 BOS1921**（單通道）或 **BOS0614**（四通道）。【已檢索 S3/S5】
- **BOS1211 是唯一車規（AEC-Q100 Grade 2）選項**，而且它的架構最接近「可客製」——功率 FET 外掛，代表你可以自己選 FET 改變功率等級，是自研前最好的架構學習平台。【已檢索 S25】
- **MAX77501 應該被列為必須採購的對照組**，因為它是唯一非 Boréas 的能量回收壓電驅動 IC，直接量它與 BOS1921 的效率差，就能推估 CapDrive 專利到底值多少錢。

### 2.2 無能量回收的傳統陣營（TI）——效率是結構性的差，但便宜

| 料號 | 架構 | 輸出能力（@300 Hz） | 啟動 | 特色 |
|---|---|---|---|---|
| **DRV8662** | 105 V boost ＋ 整合功率二極體 ＋ 全差動放大器 | **100 nF @200 Vpp／150 nF @150 Vpp／330 nF @100 Vpp／680 nF @50 Vpp** | **1.5 ms** | 4 段 GPIO 選增益 28.8／34.8／38.4／40.7 dB；過熱保護 |
| **DRV2665** | 同上＋整合 **DAC** | 同級 | 2 ms | 與 DRV2667 腳位相容 |
| **DRV2667** | 同上＋**波形記憶體＋波形合成器** | 40–200 Vpp 可控 | 2 ms | 與 DRV8662 腳位相似 |

**效率的量級**：AllAboutCircuits 的壓電驅動器設計系列文明確給出估算——**Class-AB 線性級約 60%，boost 級約 85%，串聯後約 51%**；而且「**Class-B 放大器在純電抗負載下效率為零**」，因為從負載返回的能量全部在輸出電晶體上變成熱。相對地，**Class-D 在壓電驅動應用可達最高 96%**。【已檢索 S13/S26】

> **這裡有一個容易被忽略的架構代價**：該文同時指出，Class-D 的效率優勢**要求電源「既能供電也能吸收電力」**。也就是說，你不能只換輸出級，前面的 boost／電池介面必須是雙向的——這正是 CapDrive／MAX77501 真正的技術含量所在，也是專利的落點。

### 2.3 高壓多通道（超音波脈衝發生器）陣營——有高壓、沒感測、沒回收

| 廠商 | 料號 | 規格 |
|---|---|---|
| **ST** | **STHV200** | 整合線性＋脈衝驅動器；**3 A 線性／2 A 脈衝**；線性驅動器為非反相運放、4 段可程式增益，輸出達 **180 Vpp**；整體輸出可達 **200 Vpp**；支援 PW／CW／彈性成像模式，切換邊緣可微調 |
| **ST** | **STHV748S** | 四通道獨立高壓高速脈衝產生器；明示可驅動壓電／電容式／MEMS 換能器 |
| **ST** | **STHV800** | 八通道單晶片，工作頻率達 **20 MHz** |
| **Microchip** | **HV7358** | **16 通道三階高壓超音波發射器，內建可程式波束成形器**；每通道 **±80 V**，含 T/R 開關與主動放電回 0 V 電路 |
| **Microchip** | **HV7350** | 八通道 RTZ pulser；有 `HV7350DB1` 展示板（**8ch ±60 V, ±1.0 A**） |
| **Microchip** | **HV738 / HV7360 / HV7361** | 4 通道／內建快速 RTZ 阻尼 FET／再加整合式低噪 T/R 開關；RS 標示 HV7360GA-G、HV7361GA-G 為 **35 MHz** 級 |
| **TI** | **PGA460 / PGA460-Q1** | 超音波 SoC：低噪放大器＋時變增益＋ADC＋DSP；輸出級為互補低邊驅動器，可**驅動中心抽頭變壓器**升壓，或搭外部高邊 FET 直驅。**DigiKey 約 US$4.66–5.49** |
| **Renesas** | **DA728x** | **不是高壓壓電驅動**——為 LRA/ERM 觸覺驅動，1 kHz、**閒置電流 360 nA**、內建 **LRA 共振頻率追蹤**。其追頻演算法概念可借鑑，電壓等級不適用 |
| **ROHM** | — | **本輪查無**專用壓電／高壓致動驅動 IC |

**這一節最重要的判讀**：超音波 pulser 生態提供了「多通道 ±數十~百伏、高 slew rate、可陣列化」的現貨路徑，但**它們沒有任何感測回授、沒有能量回收、也不做任意波形**。它們是「發射器」不是「驅動器」。若你的兩用元件需要陣列 + 收發同體，pulser IC 只能解決發射半邊。

### 2.4 分立式高壓放大器（實驗室基準）

- **PI（Physik Instrumente）E-480／E-481／E-482 系列**：採用**能量回收 ＋ PWM** 架構，最高 **2000 W**。廠商宣稱：「**PI 能量回收放大器只消耗同等輸出功率線性放大器約 20% 的電力**」、「**節能可達 80%**」。這是目前找到的**能量回收技術在商用高功率產品上最具體的節能宣稱**。【已檢索 S14】
- **Trek 2220（現屬 Advanced Energy）**：**±2 kV、20 mA、至 7.5 kHz、40 W 級**。這是實驗室做 kV 級開迴路激振的標準工具。**價格查無。**【已檢索 S27】

### 2.5 噴墨產業的既有解法（可直接借鑑的工程經驗）

- Class-D 已在近年被用來取代 Class-AB 驅動壓電噴墨頭；但為了達到噴墨所需的波形精度，**Class-D 振盪頻率必須做到 1–8 MHz，約為音訊應用的 20 倍**。【已檢索 S28】
- 噴墨產業另有 **Class-G 電壓放大 IC**，設計目標是「在波形下降段從噴墨元件的容性負載**回收至少一部分**儲存能量」；以及**電感式能量回收**（能量在電感與電容間循環）。
- 產業共識的痛點描述值得直接引用給客戶：「單顆壓電元件可模型化為單一電容，但驅動電路可能要並聯驅動**數百顆**；它們幾乎不消耗功率，**但那些功率必須在驅動電路裡被消耗掉**。」

---

## 3. 關鍵數字表

| # | 項目 | 數字 | 度量定義 | 來源 | 可信度 |
|---|---|---|---|---|---|
| 1 | BOS1901 驅動功耗 | 100 nF @190 Vpp/300 Hz → **350 mW** | 系統平均功耗 | S1 | 廠商規格書摘要 |
| 2 | BOS1921 單價 | **US$4.16**（DigiKey 單顆） | 通路零售價，非 1kU | S5 | 通路頁摘要 |
| 3 | BOS0614 感測延遲 | **100 µs**；感測率 **10 kSps** | 按壓偵測到觸發 | S3 | 廠商規格書摘要 |
| 4 | BOS1211 | **120 V 輸出／12 V 供電／AEC-Q100 Grade 2** | 車規 | S25 | 廠商新聞稿 |
| 5 | MAX77501 | **110 Vpk-pk／2 µF／600 µs 啟動／<1 µA 關機** | 規格 | S16 | 廠商規格書摘要 |
| 6 | DRV8662 負載能力 | 100 nF@200 Vpp／330 nF@100 Vpp／680 nF@50 Vpp（皆 300 Hz） | 規格 | S9 | 廠商頁摘要 |
| 7 | **Class-AB 壓電驅動總效率** | **約 60% × 85% ≈ 51%** | 線性級 × boost 級 | S13 | 技術文章估算，非量測 |
| 8 | **Class-D 壓電驅動效率上限** | **最高 96%** | 輸出級 | S26 | 技術文章引用 |
| 9 | **電阻式充電損失** | **恆為 50%，與 R 無關** | ½CV² 中的一半 | S17 | 物理定律 |
| 10 | **開關式壓電放大器可回收電荷** | **約 50%** | 儲存於致動器之電荷 | S18 | 論文摘要 |
| 11 | **PI 能量回收放大器節能** | 僅耗線性放大器的 **~20%**；節能達 **80%** | 相對耗電 | S14 | 廠商宣稱 |
| 12 | **最高 Qm 位置** | **在 fs 與 fp 之間**；實測最高 **Qm=1900** | Shekhani & Uchino | S23 | 論文摘要 |
| 13 | **最佳頻率 vs 共振頻率驅動** | **所需功率 −39%**，溫升更小 | Rev. Sci. Instrum. 87, 105003 | S24 | 論文摘要 |
| 14 | **PZT 振動速度上限** | **難以超過 ~1 m/s** | 受發熱與 Qm 退化限制 | S22 | 論文摘要 |
| 15 | **SCBC 改良 PLL 追頻精度** | **±9 Hz**，且對反共振免疫 | IEEE Xplore 6156822 | S21 | 論文摘要 |
| 16 | **電荷驅動遲滯** | **~2%**（vs 電壓驅動 **10–15%**）；數位電荷放大器 **−91%** | 遲滯百分比 | S20 | PI 技術頁＋論文摘要 |
| 17 | **PI 逆模型遲滯補償** | 追蹤誤差 **−90%**；線性度 **10% → <1%** | 補償後殘差 | S19 | 論文摘要 |
| 18 | **AlN BAW 跨模態隔離** | **近 60 dB** | 模態分割的實測上界參考 | S30 | 論文摘要 |
| 19 | **功率／資料頻率分割換能器** | **1 MHz 下 70% 頻寬**；反射態 vs 吸收態差 **10 dB** | backscatter 調變深度 | S29 | 論文摘要 |
| 20 | **Boréas 廠商宣稱** | 電流消耗最多 **−90%**、比競品壓電 IC **10×**、BOS1921 比其他壓電驅動器省電 **9–11×** | **皆為相對倍數，無絕對效率** | S2/S6/S31 | 廠商宣稱 |
| 21 | **E4990A 二手成交參考** | **US$37,566**（原廠整新，eBay 刊登於 2017 年結束） | 唯一取得的價格錨點 | S32 | 通路歷史刊登 |
| 22 | **台灣類比 IC 設計工程師年薪中位數** | **178 萬元**（2025 報導）／**171 萬元**（2026 報導）；數位 IC **157 萬**；硬體研發主管 **181 萬** | 104 薪資報告轉述 | S33/S34 | 媒體轉述 |

> **度量陷阱（延續前版警告，本輪更精確）**：Boréas 至今在公開資料中**沒有給出任何一個絕對轉換效率數字**，全部是「比競品 10×」「電流少 90%」這類相對量。而 TI 陣營的 51% 是技術文章的估算、不是量測。**因此「CapDrive 效率到底多少」在公開資訊中是無解的**——這正是為什麼 §4 把「買 BOS1921 與 MAX77501 各一片、自己量」列為第一優先任務。

---

## 4. 任務拆解（可直接轉為 WBS 與採購單）

### 4.1 Phase 0：現貨對打（0–2 個月，成本 <NT$30 萬，價值最高）

**T0-1 三片評估板對打（本輪新增，取代原本的單一 Boréas 驗證）**
- 採購 `BOS1921-KIT-B01`（190 V，含感測）、`BOS0614` 開發套件（4ch 60 V，含 ZPS）、`MAX77501EVKIT`（110 V，ADI 能量回收），外加 `BOS1211-KIT`（120 V 車規、FET 外掛，最接近可客製架構）。
- **必須量三件事**：(a) 相同壓電負載下三者的**實際輸入 DC 功率**（黑盒法，避開相位量測誤差）；(b) 致動訊號洩漏到感測路徑的**串音（dB）**；(c) 感測解析度與延遲（BOS0614 標稱 100 µs，實測驗證）。
- **這一步的產出是 go/no-go 依據**：若 BOS1921 的串音已經滿足需求，「自研 IC」的理由就只剩下電壓等級與通道數，而不是效能。

**T0-2 等效電路萃取流水線**
- 依 **ANSI/IEEE 176-1987（IEEE Standard on Piezoelectricity）** 與 **ANSI/IEEE 177-1966** 的程序做 BVD 四參數（C0、C1、L1、R1）萃取；IEEE 176 明確**推薦 Van Dyke 模型**代表自由壓電諧振體在共振附近的阻抗，並給出厚度、厚度剪切、長度、長度-厚度模態的分析方程。多模態時每模態掛一支獨立 RLC 串聯支路並聯到同一 C0。【已檢索 S35】
- 進一步做 **Mason / KLM 三端口模型**（1 電端口 + 2 聲端口）以納入機械側負載。【轉引 D2-35/D2-36】
- **交付物**：吃阻抗分析儀 .csv → 吐 SPICE subckt 的腳本；以及 −40／25／85／125 °C 下的 BVD 參數表。

**T0-3 大訊號地圖（本輪升級為高優先）**
- 前版只說「要量」，本輪有了具體理由與方法：文獻已建立**高功率特性量測系統**，可在**定電壓／定電流／定振動速度／定輸入功率**四種條件下量阻抗-導納曲線；另有 **burst/transient 法**（在共振點激振後強制短路或開路，觀察衰減）可分離損耗。【已檢索 S22】
- **必量**：fs 與 Qm 隨振動速度的變化，直到接近 **~1 m/s 的 PZT 實務上限**。
- **交付物**：fs(T, v, t) 三維查表 ＋ 誤差帶；以及「最高 Qm 出現在 fs–fp 之間哪個位置」的實測曲線——這張圖直接決定 Phase 1 的控制目標點。

### 4.2 Phase 1：控制演算法（2–9 個月）

**T1-1 操作點與追頻（本輪有明確設計指引）**
- **設計預設值改為：操作在 fs 與 fp 之間**，而非 fs。理由見 §1.4（最高 Qm 在兩者之間；最佳頻率驅動較共振驅動省 39% 功率）。致動用途仍需驗證位移是否足夠，但**「功率要電感性區間、致動要 fs」的二分法是過度簡化**。
- 追頻三選一，建議並行：
  1. **PLL ＋ 靜態電容寬頻補償（SCBC）**：已驗證 ±9 Hz、對反共振免疫。**必須做 C0 補償**，否則相位零點 ≠ 機械共振點。
  2. **運動電流感測**：arXiv 2605.15279 提出 **ring-dot 形壓電變壓器為基礎的運動電流感測**，特性為低延遲、低損耗、**本質隔離**；配套控制僅需**有限狀態機 ＋ PI 迴路 ＋ 低速 ADC ＋ 數顆比較器**，實測在降壓 PR 轉換器上達成**單一切換週期內全部轉態 ZVS**，且可**自啟動**。【已檢索 S36】**這仍是我推薦的主線**，因為它同時解「追頻」與「自感測解耦」。
  3. 擾動觀察／MPPT 式：慢、有穩態抖動，作為 fallback。
- **必測失效模式**（本輪有具名文獻支撐）：負載突變導致 **Qm 下降 → PLL 失鎖或誤鎖反共振**。必須設計 frequency guard band 與失鎖偵測。

**T1-2 自感測解耦**
- **橋式電容平衡**：文獻明載致命弱點——「由於電子元件標準化與環境條件變動，**橋式電路的電容精確匹配難以取得**」。已有的解法是**自適應補償**：以前饋路徑補償量測訊號，其增益由**數位電位器**調整；另有以 **LMS 演算法**自動化的橋平衡（針對每一條掃描線振幅調整平衡增益，補償遲滯造成的橋失衡）。【已檢索 S37】
- **觀測器／模型基礎法**：以 BVD 做狀態觀測器，從驅動電壓與總電流反推機械狀態；已有 observer-based self-sensing 用於壓電結構robust振動控制的文獻。
- **溫漂**：文獻提出的務實作法是「**在每次校正事件重新辨識致動器的電氣特性**」，以此隱性補償熱致特性漂移。
- **串音預算是本節唯一必須交付的數字**：建議以 §3-#18 的 **60 dB 跨模態隔離**作為「模態分割能達到的最好情況」上界，以 T0-1 實測的 BOS1921 串音作為「現貨能達到的水準」下界，兩者之間定規格。

**T1-3 遲滯與潛變——以及本輪最重要的未解風險**
- 若走**線性／電荷驅動**：電荷驅動把遲滯壓到 ~2%（vs 電壓 10–15%），數位電荷放大器 −91%；PI 逆模型 −90% 追蹤誤差。**這條路的數字很紮實。**
- 若走**開關式 ＋ 能量回收**（也就是你真正想要的高效率路線）：**本輪窮盡搜尋，找不到任何一篇討論「PI／Preisach 逆模型在含電荷回收的開關式驅動下是否仍成立」的文獻。** 物理上有明確理由懷疑會失效——遲滯是電荷歷程的函數，而能量回收路徑會**主動改變電荷歷程**（把電荷抽回去再打進來），且高 dv/dt 會激發不同的疇壁動態。
- **這是一個乾淨的研究空白，也是本專案最值得先做的實驗**：拿同一顆壓電體，分別以 Trek 線性放大器與 BOS1921 開關式驅動器施加相同的電壓波形，比對位移-電壓遲滯迴線是否重合。**若不重合，所有現成的遲滯補償文獻對你的架構都不適用**——這既是最大風險，也可能是最強的專利立足點。

**T1-4 多埠共存策略（本輪補實）**

| 策略 | 已驗證證據 | 量化上界 | 風險 |
|---|---|---|---|
| **時間分割** | 單片 MFC 時間多工做應變感測＋能量採集【轉引 D2-41】 | — | Q≈1000 ⇒ 切換後需等 ~Q 個週期讓機械暫態衰減，這是硬性等待 |
| **頻率分割** | 超音波植入式裝置以**頻率多工**把功率與資料分到不同頻段，達成**不中斷取電同時 backscatter 通訊**；換能器實測 **1 MHz 下 70% 頻寬**、反射態與吸收態差 **10 dB**【已檢索 S29】 | 調變深度 10 dB | 需要寬頻換能器 ⇒ 與高 Q 直接衝突 |
| **模態分割** | AlN BAW 多係數本徵模態架構達 **近 60 dB 跨模態隔離**【已檢索 S30】；壓電喇叭陣列以**框架分隔**把振動侷限在各自區域達成無串音【已檢索 S30】 | 60 dB | 模態間機械耦合；泛音 k² 較低；框架分隔是**機械**解法，會改變封裝設計 |
| **backscatter 調變** | 調變接在壓電接收器上的**電阻抗**，改變其**聲阻抗**，進而改變反射訊號振幅【已檢索 S29】 | — | 反射即損失取電功率（除非頻率多工） |

### 4.3 Phase 2：IC 化（9–24 個月，只在 Phase 0/1 證明現貨不夠時才做）

- **專利先行**：在畫任何一張電路圖之前，先請專利事務所對 `US10931199B2` 及其同族做 **FTO（freedom-to-operate）分析**，特別確認「輸出峰值 ≥ 2× 輸入電壓」「正向 boost／反向 buck 雙模」這兩個限制條件是否可繞開。若不可，考慮：(a) 授權；(b) 走 ADI MAX77501 的實作方向（既然 ADI 能賣，就存在可行空間）；(c) 走 Class-G 分段電源回收（噴墨產業既有做法，專利年代較早）。
- **製程**：預設 BCD（若遵守「kV 由陶瓷體升壓」原則，IC 側可壓在數十伏）；陣列化才考慮 SOI（醫用超音波 pulser 的標準選擇）。
- **必須整合**：升壓級 → 雙向 H 橋（含回收路徑）→ C0 補償／運動電流感測前端 → ADC → 追蹤環路 → 波形記憶體 → I²C/I³C/SPI。BOS0614 的 **2 kB on-chip RAM ＋ 波形合成器**是規格參考點。
- **不要低估數位**：追頻、自適應橋平衡、遲滯逆模型三者都要 MAC；BOS0614 已內建 WFS，代表這是市場預期的基本配備。

### 4.4 人才組合與市場薪資（台灣）

| 角色 | 人數（Phase 0–1 / Phase 2） | 為什麼非要不可 | 台灣年薪參考 |
|---|---|---|---|
| **類比／電源 IC 設計** | 1 / 3–4 | 雙向高壓開關、回收路徑、低噪感測前端 | **中位數 178 萬**（104 報告，非主管職第一名）；資深/主管級可參考硬體研發主管 **181 萬** |
| **機電耦合建模（最稀缺）** | 1 / 1–2 | BVD/Mason/KLM 萃取、COMSOL 壓電多物理、模態辨識與雜模排除。**台灣電源 IC 公司幾乎不存在此角色，需從超音波／MEMS／機械所挖** | **查無專門薪資統計**；實務上需以類比 IC 等級或更高開價才挖得動 |
| **控制／DSP／韌體** | 1 / 2 | PLL＋SCBC、LMS 自適應橋平衡、觀測器、遲滯逆模型 | 數位 IC 設計工程師中位數 **157 萬**可作下界參考 |
| **壓電材料／陶瓷製程** | 0.5 / 1 | 決定 Qm、溫漂、去極化邊界 | **查無** |
| **可靠性** | 0.5 / 1 | 熱去極化（安全溫度約居里溫度一半）、機械去極化、循環疲勞【轉引 D1-S28/D1-S5】 | **查無** |
| **量測工程** | 1 / 1 | 阻抗掃頻自動化、LDV 校正、高功率特性量測（定振動速度／burst 法）、EMC | **查無** |

**最小可行團隊：Phase 0–1 約 5 人**（類比 1、建模 1、控制 1、量測 1、材料/可靠性合併 1）。以類比 IC 178 萬為錨，5 人年度人事成本量級約 **NT$700–900 萬**（含加給與 fringe，**此為推算，非查證數字**）。

### 4.5 設備清單與費用等級（**價格誠實揭露：幾乎全部查無公開報價**）

| 設備 | 用途 | 價格狀態 |
|---|---|---|
| 阻抗／材料分析儀（Keysight E4990A，20 Hz–10/20/30/50/120 MHz） | BVD 參數萃取，最核心的一台 | **Keysight 官網明示「超過價格門檻，須聯繫採購」，無公開列價。** 唯一取得的錨點：**eBay 原廠整新機 US$37,566**（刊登結束於 2017）。另有 ATEC／TRS RenTelco／Electro Rent／Testworld 提供租賃，**建議 Phase 0 先租不買** |
| 高壓功率放大器（Trek 2220：**±2 kV／20 mA／7.5 kHz／40 W**） | 開迴路激振、線性 vs 開關式遲滯對照實驗（T1-3 的關鍵器材） | **新機價查無**；`piezopvdf.com` 有整新機銷售頁（價格未取得） |
| 雷射都卜勒測振儀（Polytec 單點，如 OFV-5000 系列，DC–24 MHz） | 量真實機械位移／振動速度，驗證自感測可信度、量到 ~1 m/s 上限 | **新機價查無**；二手市場僅見**控制器單體 US$3,000**（首爾，不含光學頭，不可視為系統價）。ATEC 提供 LDV 租賃 |
| 高壓差動探棒＋高頻寬示波器＋電流探棒 | 效率量測 | 查無 |
| 熱像儀、環境箱（−40～150 °C）、功率分析儀 | 損耗熱點、溫漂地圖、系統效率交叉驗證 | 查無 |
| COMSOL Multiphysics（MEMS/Acoustics 模組）或 ANSYS | 模態預測、雜模辨識 | **本輪查無**（搜尋額度耗盡） |

**量測方法學警告（維持前版並強化）**：驅動容性負載時 V 與 I 相位差接近 90°，`cos φ` 在 φ≈90° 附近斜率最大，**探棒 de-skew 沒做好，效率數字可差好幾個百分點**。務必以「輸入 DC 功率 vs 輸出有效功」的黑盒法交叉驗證 AC 相位法。

### 4.6 現成參考設計與可壓縮的時程

| 資源 | 內容 | 可壓縮時程（估算） |
|---|---|---|
| **Boréas 開發套件**：`BOS1921-KIT-B01`、`BOS0614` kit、`BOS1211-KIT`（可堆疊 4 片）、`BOS1901-KIT-B02` | 含 USB 連 PC 軟體，可手動產生波形；`BOS1901-KIT-B` **已停產**，請避開 | 「驅動＋感測同體」的 PoC 從 **6 個月 → 2 週** |
| **ADI `MAX77501EVKIT`** | 非 Boréas 的能量回收對照組 | 提供專利迴避可行性的第一手證據 |
| **TI `DRV2667EVM-CT`、`DRV8662EVM`** | Class-AB 基準 | 建立效率對照基線 |
| **Microchip `HV7350DB1`** | 8ch ±60 V ±1.0 A 超音波 pulser 展示板 | 多通道高壓陣列的現成平台 |
| **開源：`github.com/leacog/PLL-ultrasonic-driver`** | KiCad 專案檔 ＋ Arduino 程式，**低成本簡易 PLL 壓電超音波換能器驅動器** | 追頻演算法的免費起點；適合當學生實習專案 |
| **TI `DRV8662-2665-2667_DESIGN_TOOL`** | 官方計算工具 | 省下負載-電壓-頻率折衷的手算 |
| **學術**：MIT PER 群組 `per.mit.edu` 的 PT converter 論文；Nature Communications (2026) Ko/Liu/Mercier「A hybrid piezoelectric resonator-based DC-DC converter」（以 flying capacitor 做多路徑輸出並降低壓電體**內部電荷重分配損耗**） | 最新拓樸方向 | 提供下一代架構的參考，**非開源硬體，需自行復現** |

### 4.7 台灣通路

- **益登科技 EDOM 為 Boréas Technologies 授權代理商**，台灣（`edomtech.com/tw`）與中國（`edomtech.com.cn`）皆設有 Boréas 製造商頁與 Piezo Haptic Driver 產品頁，並提供技術團隊支援；其行動通訊解決方案頁面已把 Boréas 壓電觸覺驅動 IC 納入平台方案。**取樣與 FAE 路徑是通的。**【已檢索 S38】
- 其他：TI／ST／Microchip／ADI 在台皆有既有代理體系與 DigiKey／Mouser 直購管道，**評估板可線上直接下單，不需經代理**。
- **Trek（Advanced Energy）在台有 `en.autech.com.tw`（宏昇/Autech）列出 2200 系列頁面**，可作為高壓放大器詢價起點。【已檢索 S27】

---

## 5. 反面證據、失敗案例與物理／法律上限

1. **法律上限（本輪最重要的新發現）**：`US10931199B2` 的請求標的是「以雙向同步功率轉換器（開關＋開關＋電感）驅動容性負載，輸出 ≥2× 輸入，正向 boost 送能／反向 buck 回收」。這幾乎就是「主動能量回收壓電驅動器」的通用描述。**受讓人是 Harvard**，代表即使 Boréas 倒了，權利仍在，且大學技轉單位通常樂於對第三方授權——這是好消息也是壞消息（**你逃不掉，但你可以談**）。專利族優先權 2015-09-28，美國申請日 2016-09-27，**名目 20 年期估算到約 2036 年**（**此為推算，未查證 PTA／terminal disclaimer，不可用於法律決策**）。
2. **物理上限（本輪更精確）**：經電阻對電容充電**恆損失 50%**，與電阻值無關；即使 R→0，損失只是由熱轉為輻射。**要突破一半，必須用低電阻電感做諧振（絕熱）充電。** 這代表「用壓電取代電感」的敘事在驅動端**必然自我矛盾**：高效率的壓電驅動器裡面一定有電感（BOS0614 明載需外掛 10 µH；BOS1211 整合的正是 buck-boost 的閘極驅動器）。**這一點必須在對外簡報中誠實處理，否則會被懂行的人當場問倒。**
3. **材料上限**：PZT 系陶瓷的振動速度**難以超過 ~1 m/s**，受發熱與 Qm 退化限制。這直接封死了「單顆元件做很大功率」的想像空間，功率密度必須靠面積或陣列換。
4. **業界最頂級的應用不用自感測**：PI 高階奈米定位仍採外部電容式 direct metrology【轉引 D2-3】。本輪找到的自感測文獻**全部承認橋式匹配「難以取得」**，解法都是自適應補償（數位電位器、LMS）——也就是說，**自感測不是「省掉感測器」，而是「用演算法換感測器」，成本從 BOM 轉到 NRE 與韌體**。
5. **PLL 有具名的三種失效模式**：失鎖、誤鎖反共振、大追蹤誤差，且在**重載低 Qm** 時最嚴重——這正是兩用元件切換負載時的工況。
6. **現貨的生命週期風險已經發生**：`BOS1901CQR` 在 DigiKey 已標為停產、`BOS1901-KIT-B` 亦已不再製造。**這家公司成立於 2016 年、規模不大，把產品線押在單一新創供應商有實質的 EOL 風險。**
7. **Boréas 從不公布絕對效率**，只給相對倍數。這在半導體行銷中通常意味著絕對數字不夠好看，或高度應用相依。**不要把「10×」寫進任何對投資人的簡報。**
8. **Class-D 的效率不是免費的**：它要求電源能雙向吞吐；且噴墨產業經驗顯示，要達到波形精度，**開關頻率得推到 1–8 MHz**——EMI 與開關損耗會吃掉一部分優勢。
9. **產業已經失敗過一次**：CCFL 時代壓電變壓器年銷 2,500–3,000 萬顆，LED 取代後供應商成建制退場【轉引 D1-S3】。壓電方案的生存依賴「沒有磁性替代品」的利基。
10. **本輪最誠實的空白就是一條反面證據**：我**仍然沒有**在任何來源找到「專為壓電主動/被動兩用元件設計」的商用驅動 IC 或參考設計。現貨全部落在四個既有市場：觸覺致動、微幫浦冷卻、超音波收發、噴墨。**這既可能代表機會，也可能代表被評估過而不划算。**

---

## 6. 未解問題

1. **【最高優先】開關式＋能量回收驅動下，Preisach／Prandtl–Ishlinskii 遲滯逆模型是否仍成立？** 本輪專門搜尋，**零結果**。這是可以用一台 Trek + 一片 BOS1921 + 一台 LDV 在兩週內做出答案的實驗，且答案若為「否」，就是一個乾淨的專利與論文題材。
2. **`US10931199B2` 的 claim 1 完整文字與同族地域覆蓋（EP/CN/JP/TW）為何？** 本輪只取得摘要層級描述，**未讀 claim 原文**。這必須由專利事務所以正式 FTO 補上，不能靠搜尋摘要決策。
3. **ADI MAX77501 是如何迴避（或授權）該專利的？** 若能拆解 MAX77501 的架構差異，就等於拿到迴避設計的路線圖。**本輪查無 MAX77501 的專利對應關係。**
4. **儀器實際報價全部未取得。** E4990A 只有一筆 2017 年 US$37,566 的二手錨點；Polytec、Trek、COMSOL 皆查無。**Phase 0 建議先租後買**，並把詢價列為第一週的行政任務。

---

## 7. 來源清單

**注意**：S 系列為本輪 52 次 WebSearch 回傳（僅摘要，未開原文）；D1/D2 系列為轉引本專案同目錄 dossier，URL 由該檔提供，未親自驗證。

### 本輪已檢索（S 系列）

| # | 標題 | URL | 說明 |
|---|---|---|---|
| S1 | BOS1901 Product Brief / Piezo Haptic Driver Product Description | https://mm.digikey.com/Volume0/opasdata/d220001/medias/docus/306/BOS1901_PB_8-9-19.pdf | 190 Vpp、100 nF@190 Vpp/300 Hz 僅 350 mW、820 nF 負載上限、SPI+64 FIFO、<300 µs 啟動 |
| S2 | CapDrive Technology — Boréas | https://www.boreas.ca/pages/capdrive-technology | 「從致動器內部負載電容回收能量並再利用」；10× 效率宣稱 |
| S3 | CapDrive Multi-Channel Piezo Driver (BOS0614) | https://www.boreas.ca/products/bos0614-piezo-haptic-driver | 4×60 V、10 kSps 感測、100 µs 按壓延遲、ZPS、2 kB RAM、需 10 µH 電感 |
| S4 | BOS0614 Product Datasheet (DigiKey 託管 PDF) | https://mm.digikey.com/Volume0/opasdata/d220001/medias/docus/6662/2158_BOS0614CWR.pdf | BOS0614 完整規格 |
| S5 | BOS1901CQR — DigiKey 產品頁 | https://www.digikey.com/en/products/detail/boreas-technologies/BOS1901CQR/13171314 | **標示 obsolete／不再製造**；並提供 BOS1921CQR US$4.16 之替代參考 |
| S6 | BOS1921/BOS1931 Product Datasheet BT015DDS01.01 | https://mm.digikey.com/Volume0/opasdata/d220001/medias/docus/6662/2158_BOS19_Datasheet.pdf | 兩者皆 190 Vpp／3–5.5 V；1931 僅驅動、1921 含感測 |
| S7 | BOS1921CQR — Mouser | https://www.mouser.com/ProductDetail/Boreas-Technologies/BOS1921CQR?qs=HoCaDK9Nz5eesZrKztNBcQ%3D%3D | 24-QFN 4×4、I²C/I³C、整卷 2500 顆 |
| S8 | BOS1931 High-Efficiency Piezo Driver — DigiKey | https://www.digikey.com/en/product-highlight/b/boreas/bos1931-high-efficiency-piezo-driver | BOS1931 現況與定位 |
| S9 | DRV8662 — TI | https://www.ti.com/product/DRV8662 | 105 V boost＋全差動放大器；100 nF@200 Vpp、330 nF@100 Vpp、680 nF@50 Vpp；1.5 ms；四段增益 |
| S10 | DRV2665 — TI | https://www.ti.com/product/DRV2665 | 105 V boost ＋ DAC；2 ms |
| S11 | DRV2667 — TI | https://www.ti.com/product/DRV2667 | 40–200 Vpp、波形記憶體＋波形合成器 |
| S12 | **US10931199B2 — Driver for a circuit with a capacitive load** | https://patents.google.com/patent/US10931199B2/en | **CapDrive 核心專利**：Harvard 受讓；雙向同步功率轉換器、輸出 ≥2×Vin、forward-boost/reverse-buck；PCT/US2016/053915（2016-09-27）之接續案；臨時案 2015-09-28、2015-12-11 |
| S13 | Evaluating the Class AB Output Stage for Piezo Driver Design (AllAboutCircuits) | https://www.allaboutcircuits.com/technical-articles/evaluating-the-class-ab-output-stage-for-piezo-driver-design/ | Class-AB ~60% × boost ~85%；純電抗負載下 Class-B 效率為零 |
| S14 | PI E-480 High Voltage Piezo Driver: Energy Recovery | https://www.pi-usa.us/en/products/piezo-drivers-controllers-power-supplies-high-voltage-amplifiers/pztcontrolelectronics-6-18 | 能量回收＋PWM；僅耗線性放大器 ~20% 電力；節能達 80%；至 2000 W |
| S15 | Driver for a Circuit with a Capacitive Load — Harvard（FreePatentsOnline） | https://www.freepatentsonline.com/y2020/0243744.html | 受讓人為 President and Fellows of Harvard College 之佐證 |
| S16 | MAX77501 — Analog Devices | https://www.analog.com/en/products/max77501.html | 110 Vpk-pk、2.8–5.5 V、2 µF、energy recycling、25 MHz SPI、600 µs、<1 µA |
| S17 | Why did half of the capacitor charging energy go in parasitic resistance…（ResearchGate 討論）／相關物理討論串 | https://www.researchgate.net/post/Is-the-charging-efficiency-of-a-capacitor-bound-by-50 | 電阻式充電恆損 50%；電感諧振（絕熱）充電可近 100% |
| S18 | Bidirectional Drive with Inhibited Hysteresis for Piezoelectric Actuators (PMC) | https://pmc.ncbi.nlm.nih.gov/articles/PMC8879597/ | 開關式功率放大器「可回收致動器中約 50% 儲存電荷」 |
| S19 | Real-time inverse hysteresis compensation of piezoelectric actuators with a modified Prandtl-Ishlinskii model | https://pubmed.ncbi.nlm.nih.gov/22755661/ | 追蹤誤差降約 90%；線性誤差 10% → <1% |
| S20 | Piezo Drivers / Piezo Motion Controllers（PI 技術頁） | https://www.physikinstrumente.com/en/expertise/technology/controllers-software/piezo-controllers-piezo-drivers | 電荷控制遲滯 ~2% vs 電壓控制 10–15% |
| S21 | An improved phase-locked loop method for automatic resonance frequency tracing based on static capacitance broadband compensation | https://ieeexplore.ieee.org/document/6156822/ | PLL 三種失效模式；SCBC 追蹤精度 ±9 Hz、免疫反共振 |
| S22 | High Power Characterization of Piezoelectrics（PSU 論文） | https://etda.libraries.psu.edu/files/final_submissions/5726 | 定電壓/定電流/定振動速度/定輸入功率量測系統；burst/transient 法；PZT 振動速度難超 ~1 m/s |
| S23 | High power characteristics at antiresonance frequency of piezoelectric transducers | https://www.sciencedirect.com/science/article/abs/pii/0041624X9500082E | 反共振為定 D 驅動、機電損耗近零；Shekhani & Uchino 最高 Qm 在 fs–fp 之間，實測 1900 |
| S24 | Driving frequency optimization of a piezoelectric transducer and the power supply development (Rev. Sci. Instrum. 87, 105003) | https://pubs.aip.org/aip/rsi/article/87/10/105003/368465/Driving-frequency-optimization-of-a-piezoelectric | 最佳頻率驅動較共振驅動所需功率降 39%、溫升更小 |
| S25 | Boréas Successfully Completes AEC-Q100 Grade 2 Automotive Qualification for BOS1211 | https://www.boreas.ca/blogs/press-center/boreas-completed-aec-q100-grade-2-automotive-qualification-for-bos1211-piezo-haptic-driver | BOS1211 車規認證 |
| S26 | Class AB vs. Class D: Understanding the Trade-Offs for Piezo Driver Design | https://www.allaboutcircuits.com/technical-articles/class-ab-vs-class-d-understanding-the-trade-offs-for-piezo-driver-design/ | Class-D 最高 96%；但需能雙向吞吐的電源；LC 濾波器選型 |
| S27 | Trek 2200 Series（Advanced Energy） | https://www.advancedenergy.com/en-us/products/high-voltage-amplifiers/systems-up-to-5-kv/up-to-50-w/trek-2200-series/ | 2220：±2 kV／20 mA／7.5 kHz／40 W 級 |
| S28 | Driving piezoelectric actuators in industrial inkjet printers (Power Electronics News) | https://www.powerelectronicsnews.com/driving-piezoelectric-actuators-in-industrial-inkjet-printers/ | Class-D 取代 Class-AB；需 1–8 MHz 開關頻率；數百顆並聯電容負載的功耗都落在驅動電路 |
| S29 | Piezoelectric transducer design for simultaneous ultrasonic power transfer and backscatter communication (Smart Mater. Struct.) | https://iopscience.iop.org/article/10.1088/1361-665X/ac7b57 | 頻率多工分離功率與資料；1 MHz 下 70% 頻寬；反射/吸收態差 10 dB |
| S30 | Multi-coefficient eigenmode operation… AlN piezoelectric BAW gyroscopes (PMC) | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9945455/ | 近 60 dB 跨模態隔離 |
| S31 | Boréas Technologies Unlocks Active Cooling for Smartphones | https://www.boreas.ca/blogs/press-center/boreas-technologies-unlocks-active-cooling-for-smartphones | BOS1921 功耗較其他壓電驅動器低 9–11×；WLCSP 2.1×1.7×0.625 mm；已量產於 PC 觸控板與行動裝置 |
| S32 | Keysight E4990A — How to Buy | https://www.keysight.com/us/en/howtobuy/E4990A/impedance-analyzer-20-hz-10-20-30-50-120-mhz.html | 官方明示「超過價格門檻，須聯繫採購團隊」；二手錨點見 eBay 刊登 https://www.ebay.com/p/1792761469 |
| S33 | 半導體人才薪資揭密 類比IC設計工程師年薪中位數178萬居冠（經濟日報） | https://money.udn.com/money/story/5612/8900673 | 類比 IC 178 萬、數位 IC 157 萬、硬體研發主管 181 萬 |
| S34 | 軟體工程時代翻盤！類比IC工程師年薪中位數171萬元霸榜（數位時代） | https://www.bnext.com.tw/article/90804/taiwan-tech-jobs-shift-from-software-to-chip-design-and-ai | 2026 年版：類比 IC 171 萬居非主管職第一 |
| S35 | IEEE 176-1987 IEEE Standard on Piezoelectricity | https://webstore.ansi.org/standards/ieee/1761987 | 推薦 Van Dyke 模型（C0/C1/L1/R1）；厚度、厚度剪切、長度等模態方程；搭配 ANSI/IEEE 177-1966 |
| S36 | Motional-Current-Sensing Method and Simplified Closed-Loop Control Strategy for PR-based DC-DC Converters (arXiv 2605.15279) | https://arxiv.org/abs/2605.15279 | ring-dot PT 運動電流感測；FSM+PI+低速 ADC+比較器；全轉態 ZVS；可自啟動 |
| S37 | An Overview of Piezoelectric Self-Sensing Actuation for Nanopositioning Applications | https://www.researchgate.net/publication/336951005_An_Overview_of_Piezoelectric_Self-Sensing_Actuation_for_Nanopositioning_Applications_Electrical_Circuits_Displacement_and_Force_Estimation | 橋式電容精確匹配難以取得；自適應前饋（數位電位器）；LMS 橋平衡 |
| S38 | Boréas Technologies 授權代理商 — 益登科技 EDOM | https://www.edomtech.com.cn/manufacturers-detail/boreas/ | EDOM 為 Boréas 授權代理；台灣頁 https://www.edomtech.com/tw/product/ins.php?index_id=817 |
| S39 | STHV200 相關報導（ST 新聞） | https://newsroom.st.com/media-center/press-item.html/n4554.html | 3 A 線性／2 A 脈衝；線性驅動器 4 段增益至 180 Vpp；輸出達 200 Vpp |
| S40 | STHV800 — STMicroelectronics | https://www.st.com/en/switches-and-multiplexers/sthv800.html | 八通道、至 20 MHz、可驅壓電/電容/MEMS 換能器 |
| S41 | HV7358 — Microchip | https://www.microchip.com/en-us/product/hv7358 | 16 通道三階、±80 V、內建可程式波束成形器、T/R 開關與主動放電 |
| S42 | HV7350DB1 Demo Board — Microchip | https://www.microchip.com/en-us/development-tool/hv7350db1 | 8 通道 ±60 V ±1.0 A 展示板 |
| S43 | PGA460 — TI | https://www.ti.com/product/PGA460 | 超音波 SoC；可驅中心抽頭變壓器或外部高邊 FET；DigiKey 約 US$4.66–5.49 |
| S44 | Haptic Drivers — Renesas | https://www.renesas.com/en/products/interface/haptic-drivers | DA728x：1 kHz、閒置 360 nA、LRA 共振頻率追蹤（非高壓壓電） |
| S45 | PLL-ultrasonic-driver（開源） | https://github.com/leacog/PLL-ultrasonic-driver | KiCad ＋ Arduino 低成本 PLL 壓電超音波換能器驅動器 |
| S46 | A hybrid piezoelectric resonator-based DC-DC converter (Nature Communications, 2026) | https://www.nature.com/articles/s41467-026-70494-0 | Ko/Liu/Mercier：flying capacitor 多路徑輸出、降低壓電體內部電荷重分配損耗 |
| S47 | A power boost for mobile technologies — Harvard OTD | https://otd.harvard.edu/news/a-power-boost-for-mobile-technologies/ | Simon Chaput 於 Harvard 博士期間發明壓電驅動 IC 架構；題目為「用 3–4 V 鋰電池產生 200–300 V」 |
| S48 | Simon Chaput — Boréas Technologies | https://www.boreas.ca/pages/simon-chaput | 創辦人背景；「30+ 專利」宣稱 |
| S49 | BOS1211 Development-Kit — Boréas | https://www.boreas.ca/products/bos1211-kit | 可堆疊 4 片驅動板；USB 連 PC 軟體 |
| S50 | BOS1901-KIT-B — DigiKey | https://www.digikey.com/en/products/detail/boreas-technologies/BOS1901-KIT-B/10258692 | **標示不再製造**；替代為 BOS1901-KIT-B02 |
| S51 | Trek 2200 系列（台灣 Autech 頁） | https://en.autech.com.tw/trek-2200-series-piezo-drivers-high-voltage-amplifiers.html | 台灣詢價起點 |
| S52 | Polytec Single-point vibrometers | https://www.polytec.com/eu/vibrometry/products/single-point-vibrometers | 單點 LDV 產品線（**價格查無**；二手控制器單體參考見 machinio/wotol 刊登） |

### 轉引自本專案 dossier 01（D1 系列，未親自驗證）

| # | 標題 | URL | 本文用途 |
|---|---|---|---|
| D1-S1 | A Piezoelectric-Resonator-Based DC–DC Converter Demonstrating 1 kW/cm³ Resonator Power Density | https://ieeexplore.ieee.org/document/9931991 | 理論 98.2% vs 最高功率點實測 93.3% |
| D1-S3 | Piezoelectric Transformers: An Historical Review (Actuators, MDPI) | https://www.mdpi.com/2076-0825/5/2/12 | CCFL 產業崩解的失敗案例 |
| D1-S5 | Piezoelectric resonators in DC-DC converters: current status and limits | https://www.powerelectronicsnews.com/piezoelectric-resonators-in-dc-dc-converters-current-status-and-limits/ | 雜模、節點支撐與散熱的架構矛盾 |
| D1-S7 | Loss mechanisms and high power piezoelectrics (J. Mater. Sci.) | https://link.springer.com/article/10.1007/s10853-005-7201-0 | Qm 每 0.1 m/s 振動速度退化 17% |
| D1-S9 | Cold plasma from a single component (TDK) | https://www.tdk-electronics.tdk.com/en/373562/tech-library/articles/applications-cases/applications-cases/cold-plasma-from-a-single-component/1109546 | 12–24 Vpp → 最高 20 kV，升壓由陶瓷體完成 |
| D1-S25 | CeraPlas Element 產品資料 | https://www.tdk-electronics.tdk.com/download/2307712/39eb3392c71d1191b103aa31c6a0f1c5/ceraplas-db.pdf | 52 kHz、8 W、12 Vpp、20 kV |
| D1-S28 | Thermal Degradation and Aging of High-Temperature Piezoelectrics | https://uknowledge.uky.edu/cgi/viewcontent.cgi?article=1568&context=gradschool_theses | 安全使用溫度約居里溫度一半 |
| D1-S36 | Microwave-acoustic-based isolated gate driver for power electronics (arXiv 2511.13412) | https://arxiv.org/pdf/2511.13412 | Q≈1000 ⇒ 頻寬僅數十 kHz |
| D1-S38 | Overtone Piezoelectric Resonator For Power Conversion (UC Berkeley 技轉) | https://techtransfer.universityofcalifornia.edu/NCD/33625.html | 泛音模態分離的可授權技術 |

### 轉引自本專案 dossier 02（D2 系列，未親自驗證）

| # | 標題 | URL | 本文用途 |
|---|---|---|---|
| D2-3 | Physik Instrumente — Capacitive Sensors | https://www.physikinstrumente.com/en/expertise/technology/sensor-technologies/capacitive-sensors | 最強反面證據：頂級奈米定位仍用外部電容式量測 |
| D2-8 | TDK PowerHap Actuators | https://product.tdk.com/en/products/sw_piezo/haptic/powerhap/index.html | BOS1211 的搭配致動器；內建感測、≤25 N |
| D2-16 | A high-performance ultrasonic system for simultaneous data and power through solid metal barriers | https://ieeexplore.ieee.org/document/6396499/ | 功率＋資料同軸 17.37 Mbps + 50 W |
| D2-17 | US20150049587A1 — Full-duplex ultrasonic through-wall communication and power delivery with frequency tracking | https://patents.google.com/patent/US20150049587 | 全雙工＋頻率追蹤專利路徑 |
| D2-35 | Comparison of the Mason and KLM Equivalent Circuits (JPL/NASA) | https://ndeaa.jpl.nasa.gov/ndeaa-pub/USDC/Kk_1-comparison.pdf | Mason vs KLM 三端口模型 |
| D2-36 | Equivalent Circuits for Resonators and Transducers (DTIC ADA231520) | https://apps.dtic.mil/sti/tr/pdf/ADA231520.pdf | BVD／Mason 推導 |
| D2-37 | An Inductorless Bias-Flip Rectifier for Piezoelectric Energy Harvesting | https://www.repository.cam.ac.uk/bitstream/1810/266131/1/201609_SijunDU_revised.pdf | SSHC 80% 翻轉效率——無電感電荷操作上限 |
| D2-41 | Single Piezoelectric Transducer as Strain Sensor and Energy Harvester Using Time-Multiplexing | https://ieeexplore.ieee.org/document/7938680/ | 時間分割多工實證 |
| D2-47 | High-Efficiency Isolated Piezoelectric Transformers for Magnetic-less DC-DC Power Conversion | https://www.researchgate.net/publication/391376205_High-Efficiency_Isolated_Piezoelectric_Transformers_for_Magnetic-less_DC-DC_Power_Conversion | 負載失配 → 損耗 +50%（該來源自註未一手驗證） |

### 本輪確認查無（誠實揭露的空白）

- **COMSOL Multiphysics 授權價格**：搜尋額度在此耗盡。
- **ROHM 專用壓電／高壓致動驅動 IC**：搜尋未回傳任何對應產品。
- **Keysight E4990A、Polytec LDV、Trek 2220、Aigtek ATA-2022H 之新機公開報價**：全部查無，僅得二手/歷史刊登錨點。
- **Boréas 任一料號的絕對轉換效率（η%）**：公開資料全部只有相對倍數。
- **開關式含電荷回收驅動下，Preisach／Prandtl–Ishlinskii 模型有效性**：專門搜尋，零結果。
- **`US10931199B2` claim 1 原文與同族地域覆蓋**：僅得摘要層級。
- **ADI MAX77501 與該 Harvard 專利的關係（授權或迴避）**：查無。
- **「壓電主動/被動兩用元件」專用驅動 IC 或參考設計**：**本輪仍查無任何一件。**
