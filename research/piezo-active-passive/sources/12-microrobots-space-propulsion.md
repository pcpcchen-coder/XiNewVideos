# 應用A3：昆蟲級機器人、微型衛星電推進、微型化平台的自帶高壓電源

> **一句話結論**：本輪（第 3 次嘗試）28 次 WebSearch 全部成功，把前兩輪全部留白的規格補齊，結果是**大幅下修**：昆蟲級機器人的機上高壓電子**已經做到 91 mg / 84.6% 效率**（不是「做不到」），FEEP 的 ±10 kV PPU **已經只有 230 g / 660 cm³ / 85%**，手持 XRF 需要 **40–50 kV**（壓電 X 光的 14 keV 差 3.5 倍），而 NASA/DTIC 的太空用壓電變壓器實測功率密度 **3.5 W/cm³，明確低於同規格磁性變壓器**。三個原本被寄望的子題（偵測器偏壓、微型 X 光、質譜）都被**同一條物理**殺死：**PT 的最佳負載阻抗在 10⁵–10⁶ Ω 量級，而這些應用的負載都在 10⁷–10⁹ Ω，差 2–3 個數量級**。唯一仍站得住的是**「壓電體同時是高壓源＋放電／發射電極」的功能合併**——而這條路 NASA SBIR 在 20 多年前就做過（PPT piezo-igniter，明言可省掉點火變壓器＋放電電容＋高壓開關），至今沒有產品，這件事本身就是最重要的警訊。

---

## 0. 研究方法與限制（誠實揭露）

**本輪實際 WebSearch 次數：28 次，全部成功回傳結果**（前兩輪成功次數皆為 0）。任務書預算 25–30 次，本輪用滿 28 次後主動停止。

**WebFetch 與 curl 依任務書載明全面 403，全程未嘗試。所有內容均來自 WebSearch 摘要與 repo 內姊妹檔案。**

**證據分層標記（全文適用）**：
- **【V】** ＝本輪 WebSearch 直接取得，附 URL。**但必須注意：我只讀到搜尋引擎回傳的摘要，未開啟原始 PDF/網頁**，因此屬「摘要級驗證」，數字有被摘要器誤植的殘餘風險。
- **【V2】** ＝來自本 repo 姊妹檔案、由該檔 agent 標為已驗證並附 URL 者（二手信心）。
- **【M】** ＝模型記憶，無 URL 佐證。
- **【C】** ＝本檔自行推算，輸入假設均寫出供檢驗。

**本輪相對前兩輪的實質變化（4 項判斷被推翻）**：
1. **【推翻】** 前版【M】記憶「RoboBee X-Wing 用串聯堆疊太陽能電池繞開升壓器」——**錯誤**。X-Wing 實際是「6 顆太陽能電池產生約 5 V → 機下的電力電子板升到約 200 V」【V・S5, S6】。太陽能是繞開電池，不是繞開升壓器。
2. **【推翻】** 前版【M】記憶「Accion Systems 2024 年停業」——**未獲證實**。2025 年中資料顯示公司仍營運（年營收約 USD 3.8M、約 11 名員工），SpaceNews 另有「Accion Systems gets new owner」報導；但一份 2026 年 3 月的資料庫條目顯示「不再活躍」【V・S16, S17】。**狀態衝突，判為「未定，需一手查證」，前版該條應整條刪除。**
3. **【推翻】** 前版核心論證「毫克級高壓源在磁性方案中不存在」——**部分錯誤**。sub-100 mg 的高壓驅動電路**早已存在且已飛過**：90 mg 雙級（40 mg 轉換 + 50 mg 驅動）、60 mg 單級、91 mg @ 84.6% 效率【V・S3, S4】。壓電不是進入無人區，是進入一個**已被佔領且對手成績不差**的區間。
4. **【新增否決性物理】** PT 效率最大化的條件是「負載電阻＝二次側阻尼電容在共振頻率的阻抗」【V・S28】。由此推得 PT 的甜蜜點負載約 10⁵–10⁶ Ω，而偵測器偏壓（10⁸–10⁹ Ω）與 FEEP 穩態（~10⁷ Ω）差 2–3 個數量級【C】。**這是一條統一殺死三個子題的物理，前兩輪完全沒有。**

**本輪仍查無的項目**：
- Accion TILE 系列的**工作電壓（kV）**——多方查詢僅得質量／功率／推力，電壓未公開。
- Morpheus Space nanoFEEP 的完整電壓／質量規格（僅得行銷文字）。
- 908 Devices MX908 的**高壓需求**（僅得整機 4.3 kg / 尺寸 / 電池時數）。
- 太空級 DC-DC 模組（VPT / Crane Interpoint）的**質量（g）與價格**——兩家官方資料均只給功率與抗輻射等級。
- 壓電變壓器在真空中的 multipaction 行為專門研究。
- PT 諧振能量回收的**往返效率**數字（第 2 版指出這是機會 B 的存亡數字，本輪仍查無）。
- 日文檢索完全未做（額度用盡）。

---

## 1. 結論摘要

1. **昆蟲級機器人的機上高壓電子已經很好，「以前做不到」的前提失效**：RoboBee 機上電力電子單元 **70 mg / 290 mW**，可驅動 4 顆 15 nF 負載於 200 V / 100 Hz【V・S1, S2】；另一版 **91 mg（不含 PCB）、14×12×4 mm、84.6% 效率**【V・S3】；文獻中已有 **90 mg 雙級與 60 mg 單級**電路，升壓比達 60、功率密度 >1600 W/kg【V・S4】。**壓電要贏，門檻是「<60 mg 且 >84.6%」，不是「從無到有」。**
2. **但「電源鏈是整機質量的主宰」這件事被數字強力證實**：RoboBee 本體僅 **60 mg**（2.4 cm 高、3 cm 翼展、110 Hz、最高 6 m/s）【V・S1】，而它的驅動電子 70–91 mg——**電源比機體還重**。RoboBee X-Wing 整機 **259 mg**，其中 6 顆太陽能電池各 10 mg（合計 60 mg，占 23%），飛行需約 **120 mW**【V・S5, S6, S7】。
3. **鋰電池根本進不了場**：昆蟲級自主飛行器懸停耗 **400 mW**，可分配的電池質量上限 **100 mg**；以鋰電 200 Wh/kg 與升壓電子 10–20% 轉換效率計，續航僅 **2–5 分鐘**【V・S9】。相對地，次克級射頻受電器功率密度達 **4,900 W/kg，是同質量鋰聚合物電池的 5 倍**【V・S8】。**這說明真正的瓶頸是能源儲存，不是電壓轉換——壓電變壓器解錯了題。**
4. **FEEP 的電壓需求確認，PPU 質量也確認，而且已經很輕**：Enpulsion IFM Nano 啟動放電電壓 **6 kV 與 7 kV**，輸入功率 10–40 W（最低約 8 W），推力 ≤0.35 mN，Isp 2000–6000 s，銦 LMIS、28 針發射器【V・S12, S13】。FOTEC 為 FEEP 開發的低成本 PPU：**±10 kV、90×94×78 mm（≈660 cm³）、<230 g、總效率 85%（含高壓倍壓級與保護電路）、量產成本 <€1,000**，架構是「兩相交錯升壓 + 變壓器 + Cockcroft-Walton 倍壓」【V・S18】。**Cockcroft-Walton 級本來就沒有磁性元件——壓電連「消除磁芯」的差異化都只剩下前級。**
5. **【最強反面證據】太空用壓電變壓器的實測功率密度輸給磁性**：NASA / DTIC《Piezoelectric Transformers for Space Applications》原型達 **1.5 kV/5 W 與 4.5 kV/20 W，功率密度 3.5 W/cm³，明確低於同電壓同功率的磁性變壓器**【V・S22, S23】。**這直接反駁「壓電比磁性更小」的核心賣點，而且是在太空這個目標場域上、由 NASA 資助的工作說的。**
6. **機會 A 的先例存在，而且已經失敗過一次**：NASA SBIR《Pulsed Plasma Thruster Piezo-Igniter for Small Satellite》針對 <40 kg 小衛星，明言此壓電方案「**可完全省去點火變壓器、放電電容與高壓開關，並可整合進推進器的火星塞內**」，Phase I 已證明可降低推進系統質量與體積【V・S24】。**論證與本檔機會 A 完全相同——但那是 2000 年代的 SBIR，至今沒有商品。這是本輪最重要的警訊。**
7. **手持 XRF 需要 40–50 kV，壓電 X 光的 14 keV 判定死亡**：SciAps X-550 為 **40 kV/200 µA（Rh）與 50 kV/200 µA（Au）**；Evident Vanta Max 為 **8–50 kV、4 W 管**；Bruker Tracer III-SD 上限 40 keV【V・S25, S26】。對照組硬體：**Moxtek ULTRA-LITE MAGNUM 一體式（管＋高壓電源同一模組）25×46×148 mm（≈170 cm³）、250 g、5–50 kV、5–200 µA、輸出 4 W／耗電約 9 W、50 kV 下穩定度 ±100 V（0.2%）**【V・S27】。壓電加速電位上限 ~14 keV【V2・S37】**差 3.5 倍，且是加速電位的物理上限。剔除，無爭議。**
8. **【本輪最重要的推導】PT 的最佳負載阻抗與這些應用完全錯配**：已驗證的 PT 效率最佳化條件是「負載電阻＝二次側阻尼電容在共振頻率的阻抗」，且**負載電流過小時 PT 被迫工作在遠離共振的低效率區，效率顯著下降**【V・S28】。【C】取典型 PT 輸出電容 10 pF、f = 100 kHz ⇒ R_opt ≈ 160 kΩ（與 CCFL 燈管阻抗吻合，這正是 PT 唯一量產過的應用）。而：蓋革管 500 V/1 µA ⇒ 5×10⁸ Ω；PMT 1 kV/10 µA ⇒ 10⁸ Ω；FEEP 6 kV/100 µA ⇒ 6×10⁷ Ω。**全部高出 PT 甜蜜點 2–3 個數量級。這一條物理同時殺死偵測器偏壓、微型 X 光電源與 FEEP 穩態供電三個子題。**
9. **mg 級 PT 的實際成績單也不好看**：薄膜 PZT-on-Si 諧振變壓器（文獻明言動機正是「為毫米／毫克級微型機器人平台做電源」）**效率僅約 60%（負載 240 Ω 與 75 Ω），共振頻率 14–20 MHz**【V・S29】。**60% vs 對照組 84.6%——這是目前唯一可直接比較的同尺度數字，壓電輸。**

---

## 2. 查證結果

### 2.1 昆蟲級飛行機器人：電源鏈確實是質量主宰，但已被解決到 sub-100 mg

| 對象 | 已驗證數字 |
|---|---|
| RoboBee（Harvard Microrobotic Fly） | 整機 **60 mg**、高 2.4 cm、翼展 3 cm、拍翅 **110 Hz**、最高 6 m/s【V・S1】 |
| RoboBee 驅動電壓 | **200–300 V**（部分報導稱「高達 300 V」）【V・S1, S2】 |
| RoboBee 機上電力電子單元 | **70 mg、290 mW**；驅動 4 路高壓訊號、對應 2 顆雙晶片致動器；量測條件為 4×15 nF 負載、200 V、100 Hz【V・S1, S2】 |
| 低質量電力電子單元（IEEE TPEL） | **91 mg（不含電路板）、14×12×4 mm、效率 84.6%**【V・S3】 |
| 更早的拓樸探索（Karpelson/Wood） | 雙級 **90 mg**（40 mg 轉換級 + 50 mg 驅動級）、單級 **60 mg**；升壓比達 **60**、功率密度 **>1600 W/kg**【V・S4】 |
| RoboBee X-Wing（Nature 2019, Jafferis et al.） | **259 mg**、4 翼、**170 Hz**、翼展 3.5 cm、高 6.5 cm；飛行需約 **120 mW**；6 顆太陽能電池置於翼上，**每顆 10 mg**、滿日照 **0.76 mW/mg**；**太陽能約 5 V → 機下電力電子板升到約 200 V**【V・S5, S6, S7】 |
| RoboFly（UW, Fuller 團隊） | 雷射照射光伏片，**7 V → 240 V** 升壓電路；ICRA 2018【V・S10】 |
| 昆蟲級自主飛行的能量預算 | 懸停 **400 mW**、電池質量上限 **100 mg**；鋰電 200 Wh/kg + 升壓電子 **10–20% 轉換效率** ⇒ 續航 **2–5 分鐘**【V・S9】 |
| 射頻供電替代路線（Nature Electronics 2021） | 次克級射頻受電器 **4,900 W/kg**，為同質量 LiPo 的 **5 倍**【V・S8】 |
| 直驅式壓電昆蟲機（2025, *Chinese J. Aeronautics*） | 翼展 70 mm、**160 mg**、升重比 **2.8:1**，PZT 雙晶片直驅、無傳動機構【V・S11】 |
| 現行升壓架構的已知缺點 | 「升壓轉換器串接開關電容電路以取得高壓，但此結構需要大量幫浦電容，增大體積並降低功率密度」【V・S4】 |
| 壓電致動器的兩大電源挑戰（文獻原話） | (1) 工作電壓數十至數千伏；(2) **機電耦合係數低，因此必須回收未用電能**【V・S4】 |

**判讀**：
- 「電源是 payload 瓶頸」**成立且有數字**：60 mg 的 RoboBee 配 70–91 mg 的驅動電子，電源比機體重；X-Wing 259 mg 中太陽能占 60 mg。
- 但**瓶頸的位置被誤判了**。S9 明說限制續航的是「缺乏輕量高功率密度電池」，而 S8 的解法是換能源（射頻），不是換變壓器。**壓電變壓器最多改善 259 mg 中的電力電子那一塊（量級 70–91 mg），而且對手已經有 84.6% 效率。**
- 唯一真正有利的數字是 S9 的「升壓電子轉換效率 10–20%」——**但這個 10–20% 幾乎確定包含了致動器的機電轉換損失（壓電雙晶片耦合係數本來就低），不能與 S3 的 84.6%（純電子轉換）直接相減**。兩者數量級差太多，我判斷是量測邊界不同。**這個矛盾必須先釐清，否則「壓電能改善多少」這題無法作答。列為未解問題 #1。**
- 【C】致動器電容的相容性問題：RoboBee 致動器 **15 nF**，而典型 PT 的輸出電容在 pF 量級——**負載電容是 PT 自身輸出電容的約 1000 倍，會完全主宰諧振腔**（姊妹檔已驗證：並聯電容使串聯與並聯共振頻率同時下降【V2・S40】）。這既是最大的設計障礙，也是最明確的 IP 切入點（「PT 腔與致動器電容聯合設計」）。

### 2.2 立方衛星電推進：電壓確認、PPU 質量確認，且對手已經很輕

| 對象 | 已驗證數字 |
|---|---|
| **Enpulsion IFM Nano**（銦 FEEP） | 輸入功率 **10–40 W**（最低約 8 W）、推力 ≤**0.35 mN**、Isp **2000–6000 s**、**啟動放電電壓 6 kV 與 7 kV**；多孔鎢冠狀 LMIS、**28 根針狀多孔發射器**、毛細被動供料【V・S12, S13】 |
| **Accion TILE 3** | 總衝量 **755 N·s**、Isp **1650 s**、濕質量 **1.25 kg**、最大軸向推力 **0.45 mN**、體積 **1U**、待機 1.5 W、最大 **20 W**；**工作電壓查無**【V・S14, S15】 |
| **Accion 公司狀態** | **衝突**：2025 年中資料顯示仍營運（營收約 USD 3.8M、約 11 人）；SpaceNews 有「gets new owner to scale up」報導；一份 2026-03 資料庫條目顯示「不再活躍」【V・S16, S17】 |
| **FOTEC 低成本 FEEP PPU**（ESPC 2017） | **發射極 +10 kV／萃取極 −10 kV**、含升壓＋推進劑加熱＋中和器功能、**90×94×78 mm（≈660 cm³）、<230 g、總效率 85%**（含高壓倍壓級與保護電路）、**量產成本 <€1,000**；架構＝**兩相交錯升壓 + 變壓器 + Cockcroft-Walton 倍壓**【V・S18】 |
| 電噴霧 PPU（Illinois, 多模式推進） | 目標 **3.25 kV**、標稱電流 **350 µA**【V・S19】 |
| NASA 微型化 PPU 研究 | 元件級質量 **0.475 kg**，飛行版估計 **<1 kg**；效率 0.90（標稱）～95%（EM）【V・S20】 |
| ExoTerra Halo PPU | 質量 **<0.45 kg**、效率 **96–98%**【V・S21】 |
| UWE-4（1U CubeSat 電推進） | PPU 產生 **>5 kV**【V・S30】 |
| Busek BIT-3 | 56–80 W 輸入、2.5 cm 柵極射頻離子、推力 ≤1.25 mN、Isp ≤2300 s、**濕重 3 kg（含 1.5 kg 推進劑）**、13 kg CubeSat @75 W 可得 3.2 km/s；RF 電源效率約 90%【V・S31】 |
| ThrustMe NPT30-I2（1U） | 總衝量 ≤5500 N·s、推力 1.1 mN、固態碘、發射時非受壓【V・S32】 |
| Morpheus Space nanoFEEP | 僅得行銷描述（「推力高 10 倍」），**規格查無**【V・S33】 |

**判讀**：
- **FEEP 的 6–10 kV、µA–次 mA 電氣特性確認**，紙面上仍與 PT「高升壓比、高輸出阻抗」相符。
- **但 PPU 已經只有 230 g / 660 cm³ / 85%，而整個 TILE 3 系統是 1.25 kg。** 把 230 g 砍到 50 g，對系統只省 14%。【C】這是**優化**，不是新能力。
- **最致命的是架構**：FOTEC PPU 的高壓段是 Cockcroft-Walton 倍壓器——**本來就沒有磁芯**。壓電能取代的只有前級的升壓＋變壓器，而那一級在 660 cm³ 中占比不明（查無）。
- **DTIC/NASA 已經量過壓電在太空的功率密度：3.5 W/cm³，低於磁性**【V・S22, S23】。這是本輪最硬的反證：不是「沒人試過」，是「試過而且輸了」。

### 2.3 壓電變壓器在太空：已被 NASA 做過，包括機會 A 的完整論證

- **NASA NTRS 20050215145**《Novel High-Voltage, High-Power Piezoelectric Transformer Developed and Demonstrated for Space Communications Applications》【V・S22】。
- **DTIC ADA429524**《Piezoelectric Transformers for Space Applications》（另有 MRS Proceedings 版本）：原型 **1.5 kV/5 W** 與 **4.5 kV/20 W**，模組化拓樸；**功率密度 3.5 W/cm³，明確低於同電壓同功率的磁性變壓器**【V・S23】。
- **NASA SBIR 164415**《Pulsed Plasma Thruster Piezo-Igniter for Small Satellite》【V・S24】：針對 <40 kg 小衛星的放電啟動（DI）系統；Phase I 已證明可降低推進系統質量與體積；**明言此方案「可完全省去點火變壓器、放電電容與高壓開關」，且「預期整合進推進器的火星塞內」**。搜尋摘要另提及在 **10⁻⁶–10⁻⁷ torr 高真空下累積測試逾 50,000 次循環**（此句歸屬於 SBIR 還是 DTIC 報告，摘要語意不清，**標為未驗證**）。
- **MDPI *Actuators* 13(8):312**《The Challenges of Piezoelectric Actuators and Motors Application in a Space Environment》——壓電在太空的真空除氣、輻射、熱循環挑戰的專門回顧【V・S34】；另有真空除氣的緩解手段（材料選擇、真空烘烤、保護鍍層）【V・S35】。

**判讀**：這是本輪最重要的發現，而且**方向與客戶期待相反**。機會 A 的論證（元件即電極、省掉變壓器與高壓開關）**不是新洞見，是 NASA 20 多年前 SBIR 的原始提案語言**。Phase I 成功、然後沒有產品——**這種模式通常代表 Phase II 或商業化階段出現了未公開的障礙**。在投入前，**找出這個 SBIR 為何沒有下文，比任何新實驗都重要且便宜**。

### 2.4 偵測器高壓偏壓：對照組便宜到不可能贏

| 對象 | 已驗證數字 |
|---|---|
| 蓋革管高壓模組（RH Electronics） | 輸出 **420 V 或 500 V**（跳線選擇）、輸入 **3.5–5.5 V**、**500 V 下最大 50 µA**、靜態電流 **<1 mA**（背景時 0.1–0.9 mA）、含 ~5 µs TTL 脈衝輸出；電商標價約 **USD 50**【V・S36】 |
| XP Power / EMCO 系列 | **P 系列（穩壓）≤2 kV；Q 系列（比例式）≤10 kV；C 系列（穩壓）≤8 kV**；EMCO 另有 **GPMT 型號專為 PMT 偏壓設計**【V・S37, S38】 |
| XP Power / EMCO Q 系列（前輪數字） | **5 kV @ 0.125 in³（≈2 cm³）**、10 kV @ 0.614 in³、輸出 **0.5 W**；Q101-5 單價 **USD 420.06**【V2・S39】 |
| SiPM 偏壓 | 需「升壓轉換器產生高壓 + 線性穩壓給出精確偏壓」的兩級架構；ADI CN0536 為公開參考設計【V・S41】 |
| 可攜輻射偵測市場 | 可攜輻射監測儀 **USD 255M（2024）→ 332M（2031）、CAGR 3.9%**；個人輻射偵測器 **USD 0.71B（2024）**；輻射偵測／監測／安全整體市場 **USD 1.53B（2023）→ 2.52B（2030）、CAGR 7.4%**【V・S42, S43, S44】 |

**判讀：明確剔除。** 三重否決：
1. **物理**：負載阻抗 10⁸–10⁹ Ω，比 PT 甜蜜點高 2–3 個數量級【C by S28】；PT 在小電流下被迫離開共振點，效率顯著下降【V・S28】。
2. **對照組**：500 V 蓋革模組 USD 50、靜態電流 <1 mA、指甲大小；5 kV 模組 2 cm³ / USD 420。
3. **架構**：這類模組內部是「返馳 + Cockcroft-Walton」，**倍壓級本來就無磁性**——壓電拿不出差異化。
4. **市場**：整個可攜輻射監測市場只有 USD 255M/年，CAGR 3.9%，且高壓模組只是其中一個零件。

### 2.5 微型 X 光源：分母端補齊，判定死亡

| 對象 | 已驗證數字 |
|---|---|
| SciAps X-550 | **40 kV/200 µA（Rh 靶，合金）**；**50 kV/200 µA（Au 靶，其他應用）**【V・S25】 |
| SciAps X-50 | 40 kV Rh（合金）／50 kV（地化、土壤）；7 mm² SDD【V・S25】 |
| Evident（Olympus）Vanta Max / Core | **4 W X 光管，8–50 kV Rh**；Core 為 8–50 kV Ag 或 8–40 kV Rh/W【V・S26】 |
| Bruker Tracer III-SD | 上限 **40 keV**【V・S26】 |
| Amptek Mini-X2 | 最大高壓 **50 kV 或 70 kV**、最大功率 **4 W 或 10 W**（例：50 kV/20 µA）、焦點約 2 mm；模組含管＋HVPS＋控制＋USB【V・S45】 |
| **Moxtek ULTRA-LITE MAGNUM 50 kV** | **25×46×148 mm（≈170 cm³）、250 g**、**5–50 kV、5–200 µA**、輸出 ≤4 W、耗電約 9 W；**單體式（monoblock）將 X 光管與高壓電源整合為單一輕量單元**；12 V 電池滿功率 >3 h；50 kV 下穩定 ±100 V（0.2%）【V・S27】 |
| 壓電加速電子的實測上限 | 最大軔致輻射能量 **~14 keV**【V2・S46】 |

**判讀**：需求 40–50 kV，壓電上限 14 keV，**差 3.5 倍且是加速電位的物理上限，不是工程問題**。更糟的是：**Moxtek 已經做到「管＋高壓電源單體整合」——「功能合併」這個壓電的核心賣點在這個應用上已被競爭對手用傳統技術實現了**。**剔除，本題結案。**

### 2.6 微型質譜儀

- **908 Devices MX908**：整機 **≤4.3 kg（9.5 lb）**、**29.8×21.6×12.2 cm**、可熱插拔鋰電池 **>3 h**、質量範圍 50–500 AMU、IP54【V・S47, S48】。**高壓需求查無**（官方規格表不列）。
- 姊妹檔已驗證的可攜質譜高壓數字：**±25 kV HVPS、整系統 <4 lb、12 V 鋰電約 10 h；Mini 12 為 2–10 kV**【V2・S49】。
- **判讀**：MX908 已達 4.3 kg，高壓電源在其中占比很小；±25 kV 超出 PT 商用上限（CeraPlas 20 kV）【V2・S50】；2–10 kV 檔雖落在 PT 範圍，但同樣受 §2.4 的負載阻抗錯配所限。**判為替代品，降權。**

---

## 3. 關鍵數字表

| 項目 | 數值 | 層 | 來源 |
|---|---|---|---|
| RoboBee 整機質量 | **60 mg**（2.4 cm 高、3 cm 翼展、110 Hz、6 m/s） | V | S1 |
| RoboBee 驅動電壓 | **200–300 V** | V | S1, S2 |
| **RoboBee 機上電力電子** | **70 mg / 290 mW**（4×15 nF @ 200 V, 100 Hz） | V | S1, S2 |
| **低質量電力電子單元（最佳）** | **91 mg（不含 PCB）、14×12×4 mm、效率 84.6%** | V | S3 |
| sub-100 mg 電路家族 | 雙級 **90 mg**（40+50）、單級 **60 mg**；升壓比 60；>1600 W/kg | V | S4 |
| **RoboBee X-Wing** | **259 mg**、4 翼 170 Hz、翼展 3.5 cm、高 6.5 cm、飛行需 **~120 mW** | V | S5, S6, S7 |
| X-Wing 太陽能 | 6 顆，**每顆 10 mg**、**0.76 mW/mg**（滿日照）；**~5 V → ~200 V 由機上電子升壓** | V | S5, S6 |
| RoboFly | 光伏 **7 V → 240 V** 升壓 | V | S10 |
| **昆蟲級能量預算** | 懸停 **400 mW**、電池上限 **100 mg**、鋰電 200 Wh/kg、升壓電子 **10–20%** ⇒ **2–5 min** | V | S9 |
| 射頻供電受電器 | **4,900 W/kg**，為同質量 LiPo 的 **5×** | V | S8 |
| 直驅壓電昆蟲機（2025） | 翼展 70 mm、**160 mg**、升重比 **2.8:1** | V | S11 |
| **Enpulsion IFM Nano** | **6 kV / 7 kV 啟動放電**、10–40 W、≤0.35 mN、Isp 2000–6000 s、28 針銦發射器 | V | S12, S13 |
| **Accion TILE 3** | 濕質量 **1.25 kg**、1U、755 N·s、Isp 1650 s、≤0.45 mN、待機 1.5 W／最大 20 W；**電壓查無** | V | S14, S15 |
| **FOTEC FEEP PPU** | **±10 kV、<230 g、90×94×78 mm（≈660 cm³）、效率 85%、成本 <€1,000**；升壓+變壓器+**Cockcroft-Walton** | V | S18 |
| 電噴霧 PPU 工作點 | **3.25 kV / 350 µA** | V | S19 |
| CubeSat PPU 質量對照 | NASA 元件級 **0.475 kg**（飛行版 <1 kg）；ExoTerra **<0.45 kg / 96–98%** | V | S20, S21 |
| Busek BIT-3 | 56–80 W、≤1.25 mN、Isp ≤2300 s、**濕重 3 kg** | V | S31 |
| **太空用 PT 實測功率密度** | **3.5 W/cm³（1.5 kV/5 W、4.5 kV/20 W）——明確低於同規格磁性變壓器** | V | S23 |
| **NASA SBIR PPT piezo-igniter** | 針對 <40 kg 衛星；**省去點火變壓器＋放電電容＋高壓開關；擬整合進火星塞** | V | S24 |
| 蓋革高壓模組（對照組） | **420/500 V、3.5–5.5 V 輸入、50 µA @500 V、靜態 <1 mA、約 USD 50** | V | S36 |
| XP Power/EMCO 系列 | P ≤2 kV、C ≤8 kV、Q ≤10 kV；GPMT 專為 PMT 偏壓 | V | S37, S38 |
| XP Power/EMCO Q（前輪） | **5 kV @ 2 cm³ / 0.5 W**；Q101-5 **USD 420.06** | V2 | S39 |
| **手持 XRF 實際需求** | **40–50 kV / 200 µA**（SciAps X-550）；Vanta 8–50 kV / 4 W；Bruker Tracer 上限 40 keV | V | S25, S26 |
| **Moxtek ULTRA-LITE MAGNUM** | **250 g、25×46×148 mm（≈170 cm³）、5–50 kV、5–200 µA、≤4 W 輸出／~9 W 耗電、管＋HV 單體整合** | V | S27 |
| Amptek Mini-X2 | 50 kV 或 70 kV、4 W 或 10 W（例 50 kV/20 µA） | V | S45 |
| 壓電 X 光上限 | **~14 keV** ⇒ 與 40–50 kV 需求差 **3.5×** | V2 + C | S46 |
| **PT 最佳負載條件** | **R_load = 二次側阻尼電容在共振頻率的阻抗**；**電流過小 ⇒ 遠離共振 ⇒ 效率顯著下降** | V | S28 |
| **⇒ PT 甜蜜點負載** | **~10⁵–10⁶ Ω**（10 pF @100 kHz ⇒ 160 kΩ，與 CCFL 燈管吻合） | C | 由 S28 推算 |
| ⇒ 目標應用負載 | 蓋革 5×10⁸ Ω；PMT 10⁸ Ω；FEEP 6×10⁷ Ω ⇒ **高出 2–3 個數量級** | C | — |
| **薄膜 PZT-on-Si 諧振變壓器** | **效率約 60%**（240 Ω 與 75 Ω 負載）、共振 **14–20 MHz**；動機明言為 mm/mg 級微型機器人電源 | V | S29 |
| 可攜輻射監測市場 | **USD 255M（2024）→ 332M（2031）、CAGR 3.9%**；個人偵測器 0.71B（2024） | V | S42, S43 |
| MX908 手持質譜 | **≤4.3 kg**、29.8×21.6×12.2 cm、電池 >3 h；**高壓需求查無** | V | S47, S48 |
| PT 商用電壓上限 | CeraPlas **20 kV**（12–24 Vpp 輸入、47.3×20×20 mm、TRL 9） | V2 | S50 |
| 壓電陶瓷機械去極化 | **約 10 MPa** | V2 | S51 |
| PZT gamma 劣化 | **400 kGy → 介電性能 −25%** | V2 | S52 |
| 太空磁潔淨 | 磁強計需測 **10 pT**、船體 DC **<10 nT**；JUICE 伸桿 **10.6 m** | V2 | S53 |

---

## 4. 對決策的意涵：逐項判定「真新能力」還是「更小的替代品」

**判準（任務書給定）**：壓電要贏，必須進入 **<2 cm³ 或 <100 mg**，或提供磁性方案物理上沒有的功能。

| 子題 | 對照組硬數字 | 壓電要達到 | 判定 |
|---|---|---|---|
| **A. 昆蟲機器人機上高壓** | **91 mg / 84.6% / 14×12×4 mm**（已飛過）【V・S3】；單級 60 mg【V・S4】 | **<60 mg 且 >84.6%**。目前 mg 級 PT 的可比數字是薄膜 PT **60% 效率**【V・S29】 | **更小的替代品，且目前落後**。★★（前版 ★★☆ → 續降） |
| **B. FEEP／電噴霧 PPU** | **230 g / 660 cm³ / 85% / €1,000**（±10 kV 全功能）【V・S18】；系統本體 1.25 kg【V・S14】 | 省 180 g ＝ 系統的 14%。且高壓段是無磁芯的 C-W 倍壓 | **替代品，邊際效益低**。★ |
| **C. PT 即放電／發射電極（機會 A）** | **無對照組**——磁性方案的高壓必須經導線引到獨立電極 | 需在真空中證明增益不崩塌、耐發射振動 | **真新能力（唯一）**，但 **NASA SBIR 20 年前做過 Phase I 且無後續**【V・S24】。★★★（前版 ★★★★ → 降） |
| **D. 偵測器偏壓（PMT/SiPM/GM）** | **500 V 模組 USD 50 / <1 mA 靜態**【V・S36】；5 kV @ 2 cm³ / USD 420【V2・S39】 | 負載阻抗差 2–3 個數量級，物理上不匹配【C by S28】 | **剔除**（物理不合格＋對照組已極便宜） |
| **E. 微型 X 光源** | 需 **40–50 kV**；Moxtek 單體 **250 g / 170 cm³**【V・S26, S27】 | 壓電上限 **14 keV** | **剔除**（物理上限，差 3.5×） |
| **F. 微型質譜** | MX908 **4.3 kg**【V・S47】；可攜 CE-MS 需 **±25 kV**【V2・S49】 | 超出 PT 商用 20 kV 上限；系統減重邊際小 | **剔除／降權** |
| **G. 磁潔淨高壓源** | 伸桿 8.5–10.6 m 是系統級大宗質量【V2・S53】 | **前提未驗證**：查無任何壓電轉換器的實測磁簽章 | **未定，價值＝0 直到量測** |

### 4.1 給客戶的三句話

1. **A3 的「以前做不到」論證，在昆蟲機器人與 CubeSat PPU 兩條線上已被本輪數字否決**——對手不是不存在，是已經做到 91 mg / 84.6% 與 230 g / 85%，而壓電在同尺度的可比數字（薄膜 PT 60%、太空 PT 3.5 W/cm³ 低於磁性）目前是落後的。
2. **唯一保留的是「元件即電極」**（機會 C＝原機會 A）。但這條路 NASA SBIR 已走過 Phase I，明言可省掉點火變壓器＋放電電容＋高壓開關，然後沒有商品。**投入前的第一件事不是做實驗，是弄清楚這個 SBIR 為何斷掉。**
3. **本輪發現的統一物理否決線（PT 最佳負載 ~10⁵–10⁶ Ω vs 目標應用 10⁷–10⁹ Ω）應該成為整個專案的篩選器**：任何「kV 級電壓 + µA 級電流」的應用，都要先算 R_load 與 1/(ωC_d2) 差幾個數量級。這一步不用花錢，可以在會議室裡殺掉大半候選應用。

---

## 5. 反面證據與物理上限

### 5.1 【本輪最重要】太空用壓電變壓器的功率密度輸給磁性——NASA 資助的工作自己說的
DTIC ADA429524：1.5 kV/5 W 與 4.5 kV/20 W 原型，**功率密度 3.5 W/cm³，明確低於同電壓同功率的磁性變壓器**【V・S23】。這與姊妹檔引用的「壓電理論 330 W/cm³、實務 33 W/cm³」【V2・S54】並不矛盾——33 W/cm³ 是**低升壓比、低電壓**的最佳條件；一旦要求 kV 級輸出，絕緣、電極間距、應力邊界會把有效功率密度打到 3.5 W/cm³。**「高壓」與「高功率密度」在壓電上是互斥的，這是本輪最有價值的單一數字。**

### 5.2 mg 級高壓電源不是無人區，而且對手成績不差
90 mg 雙級、60 mg 單級、91 mg @ 84.6%【V・S3, S4】。**前兩版把這裡當作「磁性方案不存在」的無人區，是錯的。** 這些電路確實用了電感，但已經縮到 mg 級並飛上天。壓電唯一可比的同尺度成績是薄膜 PZT-on-Si 的 **60% 效率 @ 14–20 MHz**【V・S29】。

### 5.3 PT 的最佳負載阻抗與所有 µA 級高壓應用錯配【C，統一否決線】
已驗證：PT 效率最大化條件為 R_load = 二次側阻尼電容在共振頻率的阻抗；**負載電流太小時，PT 被迫工作在遠離共振點的低效率區，效率顯著下降**【V・S28】。
【C】假設：輸出電容 C_d2 = 10 pF、f = 100 kHz ⇒ R_opt = 1/(2πfC) ≈ **160 kΩ**（與 CCFL 燈管阻抗吻合——PT 唯一量產過的應用正好落在這裡，這是強力的旁證）。
對照：蓋革 500 V/1 µA = 5×10⁸ Ω；PMT 1 kV/10 µA = 10⁸ Ω；FEEP 6 kV/100 µA = 6×10⁷ Ω；壓電 X 光 14 kV/nA 級 = 10¹⁰ Ω 以上。
**全部高出 2–3（甚至 5）個數量級。** 要把 R_opt 拉到 6×10⁷ Ω，在 100 kHz 下需 C_d2 ≈ **26 fF**——比典型 PT 輸出電容小 3 個數量級，在物理上不可實現。
**這條線同時殺死 §2.4、§2.5、以及機會 B 的 FEEP 穩態供電。** 唯一不受此線影響的是**放電／點火**（電漿形成後負載電阻反而過低），但那正好落進另一個已驗證陷阱：**電漿一形成、負載電阻下降、PT 增益崩塌**【V2・S55】。**PT 在「太高阻」與「太低阻」之間只有一個窄窗口。**

### 5.4 機會 A 的先例已經失敗過：NASA SBIR piezo-igniter
《Pulsed Plasma Thruster Piezo-Igniter for Small Satellite》【V・S24】的提案語言與本專案機會 A 完全相同（省去點火變壓器、放電電容、高壓開關，整合進火星塞）。Phase I 成功。**至今無商品。** 論文活躍、Phase I 成功、零商品——這是姊妹檔 07 已歸納過的危險模式（超音波穿牆、壓電 X 光同型）。**必須先解釋這個空白，再決定是否投入。**

### 5.5 昆蟲機器人的真正瓶頸是能源儲存，不是電壓轉換
S9 明說：限制續航的是「缺乏輕量高功率密度電池」；即使升壓效率完美，100 mg 鋰電（200 Wh/kg）也只夠 400 mW 飛 **數分鐘**。S8 的解法是換掉電池（射頻受電 4,900 W/kg，5× LiPo）。**壓電變壓器改善的是那 70–91 mg 的電子，而不是那 100 mg 的能量。就算把電子做到 0 mg，續航只從 2–5 分鐘變成約 4–8 分鐘（線性外推，【C】），仍然不是可用的產品。**

### 5.6 Moxtek 已經用傳統技術實現了「功能合併」
ULTRA-LITE MAGNUM 是 **monoblock：X 光管與高壓電源整合為單一 250 g 單元**【V・S27】。**「把高壓源與負載合併成一個元件」不是壓電獨有的架構優勢——在 X 光這個應用上，競爭對手已經用灌封＋整合封裝做到了。** 這削弱了「元件即電極」論證的普適性（它在放電／離子發射上仍然成立，因為那需要電極表面直接暴露在真空中，這是灌封做不到的）。

### 5.7 頻率與電容的雙重錯配（昆蟲機器人）
PT 機械共振數十–數百 kHz（薄膜版更達 14–20 MHz【V・S29】），撲翼機械頻率 110–350 Hz【V・S1, S5】，差 2–4 個數量級。且 RoboBee 致動器 **15 nF**，比典型 PT 輸出電容大約 1000 倍【C】，會完全主宰諧振腔並把共振點大幅拉低【V2・S40】。**「一顆諧振體同時做功率轉換與致動」在物理上不成立**；只能做「高頻 PT 腔 + 低頻包絡調變」，而該架構的往返效率**三輪皆查無**。

### 5.8 Accion 狀態不明本身就是市場訊號
2025 年中約 11 名員工、年營收 USD 3.8M【V・S16】；一份 2026 年 3 月的資料庫顯示「不再活躍」【V・S17】；另有「換了新東家以擴大規模」的報導【V・S16】。**不論真相為何，一家做了十年電噴霧推進的公司在 2025 年只有 11 人與 380 萬美元營收，就是「這個市場很小」的直接證據。**

### 5.9 市場規模天花板
可攜輻射監測儀全球僅 **USD 255M/年、CAGR 3.9%**【V・S43】；整個輻射偵測／監測／安全市場 USD 1.53–2.52B【V・S42】。昆蟲級飛行器**無商業市場**【V2・S56】。CubeSat 推進單品是 kg 級、單價數萬美元的低量產品。**這三個市場加起來都撐不起一條陶瓷產線的固定成本**——而 PT 產業已經因 CCFL 消失而崩塌過一次（年銷 2,500–3,000 萬顆 → 多數領導供應商退出高壓 PT 量產）【V2・S57】。

### 5.10 物理上限清單（A3 專用，本輪更新）

| 上限 | 內容 | 層 |
|---|---|---|
| **高壓下的功率密度** | **kV 級輸出時實測 3.5 W/cm³，低於磁性變壓器**（低壓下可達 33 W/cm³）| V |
| **最佳負載阻抗** | **R_opt = 1/(ωC_d2) ≈ 10⁵–10⁶ Ω**；µA@kV 應用（10⁷–10⁹ Ω）不可匹配 | V + C |
| 加速電位 | 壓電加速電子軔致輻射上限 **~14 keV**（需求 40–50 kV）| V2 + V |
| 電壓 | 商用 PT 單體 ≤**20 kV**（CeraPlas）| V2 |
| 頻率 | 機械共振 kHz–MHz vs 撲翼 110–350 Hz，差 2–4 個數量級 | V |
| 負載電容 | 致動器 15 nF ≫ PT 輸出電容（pF 級）約 1000 倍，主宰諧振腔 | C |
| 放電負載 | 電漿形成 ⇒ 負載電阻下降 ⇒ **增益崩塌** | V2 |
| 機械 | ~10 MPa 即去極化；節點支撐（高 Q）與抗發射振動直接對立 | V2 + C |
| 熱 | 真空無對流；節點支撐是最差熱通路 | V2 |
| 輻射 | PZT 400 kGy → −25%；耐輻射與高 k² 材料層級衝突 | V2 |
| 能源（系統級） | 100 mg 鋰電 @200 Wh/kg 供 400 mW ⇒ 數分鐘，與轉換器無關 | V + C |

---

## 6. 未解問題

1. **【最高優先】S9 的「升壓電子轉換效率 10–20%」與 S3 的「84.6%」為何差 4–8 倍？** 前者幾乎確定包含致動器機電轉換損失。**釐清邊界後才能回答「壓電到底能改善多少」。** 檢索式：`piezoelectric microrobot system efficiency breakdown electrical to mechanical boost converter transduction`。
2. **【最高優先】NASA SBIR 164415（PPT piezo-igniter）為何沒有 Phase II／商品？** 檢索式：`"Pulsed Plasma Thruster" piezoelectric igniter Phase II results failure`；並直接查 SBIR.gov 該案的 Phase II 紀錄與承包商後續。**這是最便宜、否決力最高的一步。**
3. **Accion Systems 的真實現況。** 檢索式：`Accion Systems 2026 status`；`accion-systems.com news`。若已停業，電噴霧子題整體降權。
4. **PT 在 µA 級負載下的實測效率曲線。** S28 只給了定性趨勢，缺數字。檢索式：`piezoelectric transformer efficiency versus load resistance megaohm measured curve`。
5. **PT 諧振能量回收的往返效率**（三輪皆查無，仍是機會 B 的存亡數字），需與已知的「雙向返馳 0↔2.5 kV」與「2 二極體+1 電阻回收約一半電荷」直接比較【V2・S58, S59】。
6. **Accion TILE 的工作電壓**（本輪多方查詢未果，可能是商業機密）。
7. **壓電轉換器的實測磁簽章**（剩磁矩 A·m²／交流磁場 nT@距離）——機會 G 的存亡前提，姊妹檔 15 已建議兩週實驗。
8. **高 Q 壓電體通過發射段隨機振動的驗證**——公開文獻仍查無，應列為 gate 1。

---

## 7. 來源清單

**S1–S48 為本輪 WebSearch 直接取得（摘要級驗證）；S49 起為姊妹檔提供的二手來源【V2】。所有 URL 均出現在實際搜尋結果中，無任何一個由我自行產生。**

| # | 標題 | URL | 一句話說明 |
|---|---|---|---|
| S1 | Building RoboBees: How Harvard Engineers Are Revolutionizing Micro-Robotics (Harvard Magazine) | https://www.harvardmagazine.com/science-technology/harvard-robot-bees-future-robotic-engineering | RoboBee 需高達 300 V；60 mg、2.4 cm 高、3 cm 翼展、110 Hz、6 m/s |
| S2 | Recent Advances in the Application of Piezoelectric Materials in Microrobotic Systems (*Micromachines* 13(9):1422) | https://www.mdpi.com/2072-666X/13/9/1422 | RoboBee 驅動 200–300 V；70 mg / 290 mW 的高壓驅動電子；4×15 nF @200 V/100 Hz |
| S3 | A Low Mass Power Electronics Unit to Drive Piezoelectric Actuators for Flying Microrobots (IEEE) | https://ieeexplore.ieee.org/document/7927723/ | **91 mg（不含 PCB）、14×12×4 mm、效率 84.6%**——本檔最重要的對照組 |
| S4 | Milligram-scale high-voltage power electronics for piezoelectric microrobots (IEEE / Harvard VLSI-Arch) ／ Power Electronics Design Choice for Piezoelectric Microrobots (Berkeley, Steltz) | https://ieeexplore.ieee.org/document/5152319/ ；https://vlsiarch.eecs.harvard.edu/publications/milligram-scale-high-voltage-power-electronics-piezoelectric-microrobots ；https://people.eecs.berkeley.edu/~ronf/PAPERS/steltz-iros06.pdf | 雙級 90 mg（40+50）、單級 60 mg；升壓比 60、>1600 W/kg；升壓+開關電容需大量幫浦電容；壓電兩大挑戰＝高壓與低耦合需能量回收 |
| S5 | Untethered flight of an insect-sized flapping-wing microscale aerial vehicle (*Nature* 2019, Jafferis et al.) | https://www.nature.com/articles/s41586-019-1322-0 | RoboBee X-Wing 原始論文 |
| S6 | RoboBee breaks free (*Nature Electronics*) | https://www.nature.com/articles/s41928-019-0280-8 | 6 顆太陽能電池置於翼上；**約 5 V → 約 200 V 由機下電力電子轉換**；整機 259 mg |
| S7 | The RoboBee flies solo (Harvard SEAS / Wyss Institute) | https://seas.harvard.edu/news/2019/06/robobee-flies-solo ；https://wyss.harvard.edu/news/the-robobee-flies-solo/ | 259 mg、4 翼 170 Hz、翼展 3.5 cm、高 6.5 cm；需約 120 mW；太陽能電池每顆 10 mg、0.76 mW/mg |
| S8 | A wireless radiofrequency-powered insect-scale flapping-wing aerial vehicle (*Nature Electronics* 2021) | https://www.nature.com/articles/s41928-021-00669-8 | 次克級射頻受電器 4,900 W/kg，為同質量 LiPo 的 5 倍 |
| S9 | Hybrid locomotion at the insect scale (*Science Advances*) | https://www.science.org/doi/10.1126/sciadv.adu4474 | **懸停 400 mW、電池上限 100 mg、鋰電 200 Wh/kg、升壓電子 10–20% ⇒ 2–5 min**；飛行改跳躍可省 64% 功率、載重增 10 倍 |
| S10 | The first wireless flying robotic insect takes off (UW News) | https://www.washington.edu/news/2018/05/15/robofly/ | RoboFly：光伏 7 V → 240 V 升壓電路；ICRA 2018 |
| S11 | A high liftoff speed insect-scale aerial robot direct-driven with piezoelectric bimorph PZT actuator (*Chinese J. Aeronautics* 2025) | https://www.sciencedirect.com/science/article/pii/S1000936125001001 | 翼展 70 mm、160 mg、升重比 2.8:1；直驅無傳動 |
| S12 | Full Performance Mapping of the IFM Nano Thruster (JoSS) ／ Performance Mapping and Qualification of the IFM Nano (IEPC 2017) | https://jossonline.com/wp-content/uploads/2019/10/Final-Krejci-Full-Performance-Mapping-of-the-IFM-Nano-Thruster-Including-Direct-Thrust-Measurements.pdf ；https://electricrocket.org/IEPC/IEPC_2017_24.pdf | 10–40 W、≤0.35 mN、Isp 2000–6000 s；**啟動放電電壓 6 kV 與 7 kV** |
| S13 | IFM Nano Thruster (SatCatalog) | https://www.satcatalog.com/component/ifm-nano-thruster/ | 銦 LMIS、多孔鎢冠、28 針發射器、毛細被動供料 |
| S14 | TILE 3 (SatCatalog) ／ TILE 3 Datasheet (Accion, Nov 2020) | https://www.satcatalog.com/component/tile-3/ ；https://catalog.orbitaltransports.com/content/brands/accion/Accion%20Systems%20TILE%203%20Datasheet_Nov%202020.pdf | 755 N·s、Isp 1650 s、濕質量 1.25 kg、≤0.45 mN、1U、待機 1.5 W／最大 20 W |
| S15 | Accion TILE Propulsion（官網） | https://accion-systems.com/tile-propulsion/ | TILE 產品線與離子液體電噴霧原理 |
| S16 | Accion Systems gets new owner to scale up propulsion system (SpaceNews) ／ Crunchbase Accion Systems | https://spacenews.com/accion-systems-gets-new-owner-to-scale-up-propulsion-system/ ；https://www.crunchbase.com/organization/accion-systems | 換新東家的報導；2025 年中約 11 人、年營收約 USD 3.8M |
| S17 | Accion Systems – 2026 Company Profile (Tracxn) | https://tracxn.com/d/companies/accionsystems/__cWN-h6IL8TOJAYN0DjzxIHXw5cSYrWonOxHrLdzFoBY | 2026-03 條目顯示「不再活躍」——與 S16 衝突，狀態未定 |
| S18 | Development of a Low Cost PPU for FEEP Electric Propulsion Using COTS Components (E3S Web Conf., ESPC 2017, FOTEC) | https://www.e3s-conferences.org/articles/e3sconf/pdf/2017/04/e3sconf_espc2017_15003.pdf | **±10 kV、<230 g、90×94×78 mm、85% 總效率、量產成本 <€1,000；升壓+變壓器+Cockcroft-Walton** |
| S19 | Electrospray Power Processing Unit for a Monopropellant-Electrospray Multimode Thruster (Eisen MS Thesis, UIUC) | https://eplab.ae.illinois.edu/Publications/EisenMSThesis.pdf | 目標 3.25 kV、標稱電流 350 µA |
| S20 | Miniaturized Power Processing Unit Study: A CubeSat Electric Propulsion Technology Enabler (NASA NTRS) | https://ntrs.nasa.gov/citations/20140011254 | PPU 元件級 0.475 kg、飛行版估 <1 kg；效率 0.90–0.95 |
| S21 | Test Results of ExoTerra's Halo Micro Electric Propulsion System (IEPC 2019) | https://electricrocket.org/2019/664.pdf | PPU <0.45 kg、效率 96–98% |
| S22 | Novel High-Voltage, High-Power Piezoelectric Transformer Developed and Demonstrated for Space Communications Applications (NASA NTRS) | https://ntrs.nasa.gov/citations/20050215145 | NASA 對太空用高壓 PT 的正式研發紀錄 |
| S23 | Piezoelectric Transformers for Space Applications (DTIC ADA429524 ／ MRS Proc.) | https://apps.dtic.mil/sti/tr/pdf/ADA429524.pdf ；https://www.cambridge.org/core/services/aop-cambridge-core/content/view/009FF7DF2B9C8D91CE9A03AE3E0FF54F/S1946427400097505a.pdf/div-class-title-piezoelectric-transformers-for-space-applications-div.pdf | **1.5 kV/5 W 與 4.5 kV/20 W；功率密度 3.5 W/cm³，明確低於同規格磁性變壓器**——本檔最強反證 |
| S24 | Pulsed Plasma Thruster Piezo-Igniter for Small Satellite (NASA SBIR 164415) | https://www.sbir.gov/sbirsearch/detail/164415 | 針對 <40 kg 衛星；**省去點火變壓器＋放電電容＋高壓開關，擬整合進火星塞**；Phase I 成功；「10⁻⁶–10⁻⁷ torr、>50,000 循環」句歸屬未驗證 |
| S25 | SciAps X-550 ／ X-50 (Malvern Panalytical) | https://www.sciaps.com/products/xrf/x-550 ；https://www.malvernpanalytical.com/en/products/product-range/x-series/x-50 | 手持 XRF **40 kV/200 µA（Rh）、50 kV/200 µA（Au）** |
| S26 | Vanta Handheld XRF Analyzer (Evident) ／ Bruker Tracer III-SD 訓練手冊 (UC Berkeley ARF) | https://ims.evidentscientific.com/en/products/xrf-analyzers/vanta ；https://arf.berkeley.edu/files/webfiles/all/arf/equipment/field/archaeometry/bruker/tracerxrf_training.pdf | Vanta Max 4 W、8–50 kV Rh；Bruker Tracer 上限 40 keV |
| S27 | 50kV MAGNUM X-ray Source (Moxtek) ／ Moxtek's ULTRA-LITE X-ray Source (Spectroscopy Online) ／ X-ray Sources for Handheld XRF (Moxtek) | https://moxtek.com/wp-content/uploads/pdfs/50kv-magnum-x-ray-source/Magnum_X-ray_Tube_50kV.pdf ；https://www.spectroscopyonline.com/view/moxteks-ultra-lite-x-ray-source ；https://moxtek.com/wp-content/uploads/pdfs/Handheld-XRF-sources.pdf | **250 g、25×46×148 mm、5–50 kV、5–200 µA、≤4 W 輸出／~9 W 耗電；管＋高壓電源單體整合** |
| S28 | Design and Analysis of Piezoelectric Transformer Converters (Chih-yi Lin, VT thesis) ／ Modelling and Analysis of Piezoelectric Transformers (DTIC ADA429546) ／ 相關 PT 專利 | https://vtechworks.lib.vt.edu/server/api/core/bitstreams/200e5dfd-0a75-4ff3-9711-8b3330047c65/content ；https://apps.dtic.mil/sti/tr/pdf/ADA429546.pdf | **PT 效率最大於 R_load ＝二次側阻尼電容在共振頻率的阻抗；負載電流過小 ⇒ 遠離共振 ⇒ 效率顯著下降**——本檔統一否決線的物理依據 |
| S29 | Thin-Film Piezoelectric-on-Silicon Resonant Transformers | https://www.researchgate.net/publication/260710940_Thin-Film_Piezoelectric-on-Silicon_Resonant_Transformers | **效率約 60%（240 Ω / 75 Ω 負載）、共振 14–20 MHz**；動機明言為 mm/mg 級微型機器人電源 |
| S30 | UWE-4: First Electric Propulsion on a 1U CubeSat (*Aerospace* 7(7):98) | https://www.mdpi.com/2226-4310/7/7/98 | 1U CubeSat 上的 PPU 產生 >5 kV |
| S31 | BIT-3 RF Ion Thruster (Busek) ／ BIT-3 (SatCatalog) | https://www.busek.com/bit3 ；https://www.satcatalog.com/component/bit-3/ | 56–80 W、≤1.25 mN、Isp ≤2300 s、濕重 3 kg（含 1.5 kg 推進劑）；RF 電源約 90% 效率 |
| S32 | NPT30-I2 (ThrustMe) | https://www.thrustme.fr/products/npt30-i2 | 1U 版 ≤5500 N·s、1.1 mN、固態碘、非受壓 |
| S33 | Morpheus Space nanoFEEP Datasheet (SatCatalog) | https://satcatalog.s3.amazonaws.com/components/981/SatCatalog_-_Morpheus_Space_-_nanoFEEP_-_Datasheet.pdf?lastmod=20210710023905 | 僅得行銷描述，**規格查無** |
| S34 | The Challenges of Piezoelectric Actuators and Motors Application in a Space Environment (*Actuators* 13(8):312) | https://www.mdpi.com/2076-0825/13/8/312 | 壓電在太空的真空／輻射／熱循環挑戰回顧 |
| S35 | Piezoelectricity In Space Systems: Vacuum Outgassing, Radiation And Thermal Cycling (PatSnap Eureka) | https://eureka.patsnap.com/report-piezoelectricity-in-space-systems-vacuum-outgassing-radiation-and-thermal-cycling | 真空除氣緩解手段：材料選擇、真空烘烤、保護鍍層（**商業報告，可信度中等**） |
| S36 | High Voltage Geiger Probe Driver Power Supply Module 420V/550V (RH Electronics) | https://www.rhelectronics.store/high-voltage-geiger-probe-driver-power-supply-module-420v-550v-with-ttl-digitized-pulse-output | **420/500 V、3.5–5.5 V 輸入、50 µA @500 V、靜態 <1 mA、約 USD 50** |
| S37 | G Series (EMCO High Voltage) ／ 2018 High Voltage Selector Guide (EMCO/XP Power) | http://www.emcohighvoltage.com/proportional/gseries.php ；https://heliosps.com/wp-content/uploads/2019/05/High-Voltage-Power-Supplies-Selector-Guide-EMCO-XP-Power.pdf | P ≤2 kV、C ≤8 kV、Q ≤10 kV；**GPMT 型號專為 PMT 偏壓設計** |
| S38 | Next-Generation, Miniature High Voltage Power Modules (XP Power 白皮書) | https://www.xppower.com/storage/documents/technical-articles/High-Voltage_WP_Next_Gen_Modules.pdf | 每立方吋瓦數提升、降低耗電、加入控制與安全智慧功能 |
| S39 | XP Power Q Series ／ Digi-Key Q101-5【V2】 | https://www.xppower.com/product/Q-Series ；https://azcus.digikey.com/en/products/detail/xp-power/Q101-5/5873625 | 5 kV @ 0.125 in³（≈2 cm³）、10 kV @ 0.614 in³、0.5 W；Q101-5 USD 420.06 |
| S40 | Simultaneous quasi-static displacement and force self-sensing of piezoelectric actuators by detecting impedance (*Sens. Actuators A*)【V2】 | https://www.sciencedirect.com/science/article/abs/pii/S0924424717317478 | 並聯電容負載使串聯與並聯共振同時下降，並聯共振附近最敏感 |
| S41 | CN0536 Circuit Note (Analog Devices) | https://www.analog.com/en/resources/reference-designs/circuits-from-the-lab/cn0536.html | SiPM 偏壓：升壓 + 線性穩壓兩級架構的公開參考設計 |
| S42 | Radiation Detection, Monitoring And Safety Market Report (Grand View Research) | https://www.grandviewresearch.com/industry-analysis/radiation-detection-monitoring-and-safety-market | USD 1.53B（2023）→ 2.52B（2030）、CAGR 7.4% |
| S43 | Portable Radiation Monitors Research (openPR) ／ Personal Radiation Detectors Market (Business Research Insights) | https://www.openpr.com/news/4292793/portable-radiation-monitors-research-the-global-market-size ；https://www.businessresearchinsights.com/market-reports/personal-radiation-detectors-market-109319 | 可攜輻射監測儀 USD 255M（2024）→ 332M（2031）、CAGR 3.9%；個人偵測器 0.71B（2024）（**市場研究報告，數字互相不一致，僅供量級參考**） |
| S44 | Radiation Detection Monitoring and Safety Market (Precedence Research) | https://www.precedenceresearch.com/radiation-detection-monitoring-and-safety-market | 2034 年達 USD 3.44B 的另一組估計 |
| S45 | Mini-X2 X-Ray Source Specs (Amptek) | https://www.amptek.com/-/media/ametekamptek/documents/resources/products/specs/mini-x2-specs.pdf | 最大 50 kV 或 70 kV、4 W 或 10 W（例 50 kV/20 µA）、焦點約 2 mm；含管＋HVPS＋控制＋USB |
| S46 | Ceramic Piezoelectric Transformer in Vacuum for Acceleration of Electrons and Production of X-Rays (PMC6073904)【V2】 | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6073904/ | 壓電加速電子的實測最大軔致輻射能量 ~14 keV |
| S47 | MX908 Handheld Mass Spec (908 Devices) | https://908devices.com/products/mx908/ | 產品頁；**高壓需求未公開** |
| S48 | 908 Devices MX908 (Fisher Scientific) | https://www.fishersci.com/shop/products/mx908-handheld-mass-spectrometer/17000688 | ≤4.3 kg（9.5 lb）、29.8×21.6×12.2 cm、熱插拔鋰電 >3 h、50–500 AMU、IP54 |
| S49 | Portable, Battery Operated Capillary Electrophoresis … for Mass Spectrometry (*JASMS*) ／ Mini 12 (*Anal. Chem.*)【V2】 | https://link.springer.com/article/10.1007/s13361-015-1314-8 ；https://pubs.acs.org/doi/10.1021/ac403766c | 可攜質譜 ±25 kV HVPS、系統 <4 lb；Mini 12 為 2–10 kV |
| S50 | Cold plasma from a single component (TDK) ／ CeraPlas 產品資料【V2】 | https://www.tdk-electronics.tdk.com/en/373562/tech-library/articles/applications-cases/applications-cases/cold-plasma-from-a-single-component/1109546 ；https://www.tdk-electronics.tdk.com/download/2307712/39eb3392c71d1191b103aa31c6a0f1c5/ceraplas-db.pdf | CeraPlas：12–24 Vpp → 最高 20 kV、47.3×20×20 mm、TRL 9 |
| S51 | Loss mechanisms and high power piezoelectrics (*J. Mater. Sci.*) ／ Piezoelectric resonators in DC-DC converters (Power Electronics News)【V2】 | https://link.springer.com/article/10.1007/s10853-005-7201-0 ；https://www.powerelectronicsnews.com/piezoelectric-resonators-in-dc-dc-converters-current-status-and-limits/ | ~10 MPa 機械去極化；節點支撐與散熱的架構矛盾；負載調節能力弱 |
| S52 | Effects and mechanisms of gamma irradiation on electrical properties of PZT (*Ceramics International*)【V2】 | https://www.sciencedirect.com/science/article/abs/pii/S0272884226034942 | 400 kGy → PZT 介電性能約 −25% |
| S53 | 姊妹檔 `15-magnetic-immune-clean.md`（含 Solar Orbiter MAG）【V2】 | https://link.springer.com/article/10.1007/s11214-023-00989-5 | 磁強計需測 10 pT、船體 DC <10 nT；JUICE 10.6 m / Europa Clipper 8.5 m 伸桿；壓電磁簽章查無 |
| S54 | Power density of piezoelectric transformers improved using a contact heat transfer structure (PubMed 22293737)【V2】 | https://pubmed.ncbi.nlm.nih.gov/22293737/ | 理論功率密度 330 W/cm³、實務上限 33 W/cm³ |
| S55 | Discharge plasmas generated by piezoelectric transformers (*PSST* 15(2):S07)【V2】 | https://iopscience.iop.org/article/10.1088/0963-0252/15/2/S07 | 「PT 同時作為高壓產生器與放電電極」的原始論證；電漿點燃後負載電阻下降導致增益崩塌 |
| S56 | 姊妹檔 `11-electrostatic-actuators-artificial-muscle.md`（*Micromachines* 13(7):1136）【V2】 | https://www.mdpi.com/2072-666X/13/7/1136 | 昆蟲尺度 DEA 蜻蜓機器人 317 mg / 350 Hz / 升重比 1.49；昆蟲尺度飛行器目前無商業市場 |
| S57 | Piezoelectric Transformers: An Historical Review (*Actuators* 5(2):12)【V2】 | https://www.mdpi.com/2076-0825/5/2/12 | CCFL 時代年銷 2,500–3,000 萬顆；LED 取代後多數供應商停止高壓 PT 量產 |
| S58 | Bidirectional Flyback Converter with Multiple Series Connected Outputs for High Voltage Capacitive Charge and Discharge【V2】 | https://www.researchgate.net/publication/269398568 | 磁性方案已做到 0 V ↔ 2.5 kV 高壓容性充放電與能量回收 |
| S59 | Power-Efficient Driver Circuit for Piezo Electric Actuator with Passive Charge Recovery (*Energies* 13(11):2866)【V2】 | https://doi.org/10.3390/en13112866 | 2 顆二極體＋1 顆電阻可回收約一半電荷 |

---

### 附註：對客戶決策的一句話建議

**A3 在本輪從「最有希望的應用域」降為「大部分應被剔除，只剩一條窄路且該路有 20 年失敗前科」。** 三個原本的子題（偵測器偏壓、微型 X 光、微型質譜）被同一條物理殺死——**PT 的最佳負載阻抗 10⁵–10⁶ Ω 與這些 µA@kV 應用的 10⁷–10⁹ Ω 差 2–3 個數量級**；昆蟲機器人與 CubeSat PPU 則被對照組的實績殺死（91 mg / 84.6%、230 g / 85%），而且 NASA 自己量到高壓下壓電功率密度 3.5 W/cm³ 低於磁性。**唯一保留的機會仍是「壓電體同時是高壓源與放電／發射電極」，但下一步不是做實驗，而是花一週查清 NASA SBIR 164415（PPT piezo-igniter）為何在 Phase I 成功後消失——那份答案的價值高於本專案任何一項自製實驗。**
