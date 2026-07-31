# 應用A2：靜電/介電彈性體致動器驅動 → 人工肌肉、軟體機器人、電黏附、電潤濕、電子紙

> 一句話結論：這個領域的「非替代性新能力」不在於用壓電變壓器（PT）把 kV 做得更小，而在於 **PT 的機械共振腔可以把「電容性負載」本身吃進諧振系統裡** —— 同時做到 (a) kV 級升壓、(b) 每週期無耗散的能量回收、(c) 用諧振頻率偏移做零額外元件的負載自感測 —— 這三件事合一，才能生出「服裝級自帶電源的靜電離合器」「高頻循環致動（撲翼/微泵）」「軟體致動器的無感測器閉迴路控制」這類今天做不到的東西；而且與客戶排除的 DC-DC 取代電感路線不同，這裡的**對手不是 0.1 美元的電感，而是一顆 50–420 美元、數十到數百公克的灌封高壓模組**，成本天花板高出兩到三個數量級。

---

## 0. 研究方法與限制（誠實揭露）

- **工具限制**：本環境 `WebFetch` 被 egress policy 全面封鎖（任何 URL 皆 403），因此**完全沒有讀過任何一篇原始論文或 datasheet 全文**。所有事實均來自 `WebSearch` 回傳的「連結清單 + 模型彙整摘要」。
- **實際執行**：本 agent 成功執行 **32 次 WebSearch**（HASEL 驅動電壓、PT 驅動 DEA、DEA 高壓電源小型化、Artimus、DEA 能量回收、電黏附夾具市場、靜電夾盤 ESC、Varioptic 液態鏡頭、數位微流體、E Ink 驅動電壓、可變形鏡、CMUT 偏壓、MIT 離子風飛機、可攜質譜 ESI、EMCO Q 系列、XP Power、PT 功率密度、PT 廠商、PT 電漿、PT 電容負載限制、靜電離合器、Artificial Muscle Inc/Bayer、DEA 壽命、Tanvas、PT 自感測、PT 雙向能量回收、無纜軟體機器人電源重量、昆蟲尺度 DEA 飛行器、Ventiva 離子風散熱、Etulipa 電潤濕看板、人工肌肉市場、Bosch/Arioso 靜電微揚聲器）。
- **被中斷**：第 33 次查詢起，session 層級的 WebSearch 配額（200/200，與其他平行 agent 共用）耗盡。以下 4 條原本規劃的查詢**沒有執行**，其資訊在本文中標為「查無」：
  1. Ventiva 融資輪次與其電極實際工作電壓
  2. PT 靜電消除棒 / 離子產生器的商用型號與價格
  3. PT 驅動 PMT / SiPM 偏壓的低功耗應用
  4. 靜電揚聲器/耳機的偏壓電源規格
- **明確查無的項目**（不是我沒查，是查了但摘要沒給）：
  - Volta Labs / Baebies / Illumina 數位微流體產品的**具體驅動電壓**（只查到通用 DMF 為 300–450 V DC、HV507 驅動晶片上限 300 V）。
  - MIT Barrett 團隊 EAD 飛機的**高壓轉換器重量與實際工作電壓**（摘要只給機體約 5 lb、「輕量化功率轉換器」，未給數字）。
  - Artificial Muscle Inc. 在 Bayer 收購後**是否被關閉**（摘要只確認 2003 SRI 分拆、2010 被 Bayer MaterialScience 收購、推出 ViviTouch，未確認結局）。
  - Tanvas 觸控面板的**實際驅動電壓**。
  - Etulipa 電潤濕看板的**驅動電壓**（只有功耗 7 W/m²）。
  - Bosch/Arioso NED 微揚聲器的**驅動電壓**。
- **零編造承諾**：本文未出現任何我無法對應到第 7 節某個 URL 的專利號、型號、公司名或數字。標「推論」的段落是我的工程推導，不是查到的事實。

---

## 1. 結論摘要

1. **成本對照的關鍵事實**：低功率 kV 電源的現行標竿是 XP Power / EMCO Q 系列 —— 5 kV 輸出僅 0.125 in³（≈2.05 cm³）、10 kV 僅 0.614 in³、輸出 0.5 W；Digi-Key 上 Q101-5（10 kV / 0.5 W）單價 **USD 420.06**（qty 1）。這代表在本應用域，PT 的競爭對手是**每瓦數百美元的灌封模組**，而非客戶擔心的低價磁性元件 —— 客戶對「壓電打不過磁性元件成本」的顧慮，在 kV/µA 域**不成立**。［來源 15, 16］
2. **HASEL/DEA 的電源就是系統瓶頸，而且已被量化**：HASEL 需 >5 kV、主要工作區 2–8 kV、需 ≥4 kV 且 ≥5 W；Keplinger 團隊 2019 的無纜示範中，含電池的高壓電源約 **100 g**（5 W、0–10 kV 放大器，由 3.7 V / 500 mAh LiPo 供電），驅動 3 疊 × 22 顆致動器、8 kV 下對 1 kg 負載達 40% 應變；2022 的十通道「口袋型」電源進步到 **250 g、8.4 × 13.3 × 2 cm**。致動器本身只有數公克，**電源比肌肉重一到兩個數量級**。［來源 1, 5, 25］
3. **能量回收的槓桿被低估**：DEA 實測能量轉換效率僅約 26%（壓克力、定電荷）與 18%（矽膠、定電壓），但**加入電荷回收後理論可拉到約 60%**，理論上限約 90%。目前最務實的被動回收（2 顆二極體 + 1 顆電阻）只能回收約一半電荷。這是 PT 諧振式雙向能流最直接的切入點。［來源 17, 24］
4. **反應功率遠大於有效功率，這是「新能力」的物理來源**（推論，基於來源 26 的 350 Hz 撲翼數據）：1 nF 致動器充到 5 kV，單次儲能 E=½CV²=12.5 mJ；若以 350 Hz 循環，反應功率達 **4.4 W**，而實際機械輸出可能只有數十 mW。今天的驅動器把這 4.4 W 全部丟掉。能把它循環回來，就是撲翼/微泵/高頻觸覺這些「今天做不到」的應用的入場券。
5. **PT 的電容性負載特性同時是缺點也是最大的機會**：並聯電容負載會使 PT 的串聯與並聯諧振頻率**同時下降**，且在並聯諧振附近對負載電容變化最敏感。這在傳統設計裡被當成「必須用鎖頻電路對抗的干擾」；但 DEA/HASEL 的電容值本身正比於形變量 —— 因此**同一顆 PT 可以在驅動的同時，用頻率偏移量讀出致動器的位移**，不需要任何額外感測器、也不需要浮在 5 kV 上的隔離量測電路。這是最貼近客戶「主動/被動兩用」命題的一條。［來源 21, 20］
6. **PT 產業本身處於萎縮後的低谷，是風險也是機會**：CCFL 背光被 LED 取代後，多數主要供應商已停止高壓 PT 的大量生產。現存供應商包括 Steminc、TAMURA、Nihon Ceratec（宣稱升壓比 >80、效率 >90%）、Face International，以及**台灣的 ELECERAM TECHNOLOGY（誠遠/易鼎系，多層 PT 與 CCFL 逆變器）**。供應鏈薄但在地有玩家。［來源 18, 19］
7. **兩個被客戶點名的目標其實不是 kV 負載，必須剔除**：Corning Varioptic Arctic 39N0 液態鏡頭工作於 **39–58 V**（極限 24–70 V，1136 Hz 方波 AC 驅動）；E Ink 電泳顯示的標準驅動電壓為 **±15 V**。這兩者用 PT 是殺雞用牛刀，沒有任何新能力可言，應從機會清單移除。［來源 8, 10］
8. **已在市場上、且真的需要 kV 的「新能力型」產品確實存在**：Ventiva 的 ICE（Ionic Cooling Engine）已在 CES 展示可為 Lunar Lake 筆電移除約 25 W 熱、2025 年宣布上看 100 W、2027 年上看 40 W TDP 筆電設計、噪音 <15 dBA、省下最多 40% 板面積，並取得 Intel / Dell 關注。離子風本質上就是 kV/µA 純電容+電暈負載。［來源 29］

---

## 2. 現況：技術 / 產品 / 玩家

### 2.1 負載端（誰需要 kV × µA × 純電容）

| 類別 | 代表玩家 | 典型電壓 | 是否 kV 級 |
|---|---|---|---|
| HASEL / Peano-HASEL 電液致動器 | Artimus Robotics（Keplinger @ CU Boulder 分拆） | 2–8 kV，需 ≥4 kV | **是** |
| 介電彈性體致動器 DEA | SRI 系譜（Artificial Muscle Inc → Bayer → ViviTouch）、EPFL Shea 團隊 | 50–120 V/µm 電場，實用 1–6 kV | **是** |
| 靜電離合器 / 電黏附制動器 | DextrES（ETH/EPFL）、各大 VR 觸覺研究 | 約 kV 級（新設計已降 4–20×） | **是（下降中）** |
| 電黏附夾具 | Grabit Inc.（SRI 分拆）、Festo、Schunk、OnRobot、Piab、Zimmer | kV 級 | **是** |
| 靜電夾盤 ESC（半導體） | Trek/Advanced Energy、Comdel、Matsusada、Spellman | ±1 kV ~ ±15 kV | **是** |
| 離子風散熱 EHD | **Ventiva（ICE9）** | kV（查無具體值） | **是** |
| 離子源 / 電噴霧 ESI | 可攜 CE-ESI（±25 kV HVPS）、Purdue Mini 12（2–10 kV） | 3–25 kV | **是** |
| 壓電直接放電電漿 PDD | 已商品化的手持冷電漿筆類產品 | kV（PT 直接產生） | **是** |
| 數位微流體 DMF | Volta Labs / Baebies（型號電壓查無）；通用平台 | 300–450 V DC；HV507 上限 300 V | 否（百 V） |
| 可變形鏡 / MEMS 微鏡 | 天文自適應光學、自由空間光通訊 | 200–300 V（5–8 µm 行程需 ~200 V） | 否（百 V） |
| CMUT 偏壓 | 超音波影像 | 100–300 V DC bias | 否（百 V） |
| 電潤濕液態鏡頭 | Corning Varioptic | **39–58 V** | **否** |
| 電泳電子紙 | E Ink | **±15 V** | **否** |
| 電潤濕戶外看板 | Etulipa（Philips/Miortech 系） | 查無；功耗 7 W/m² | 未知 |
| 靜電 MEMS 微揚聲器 | Bosch Sensortec / Arioso（NED 原理） | 查無；強調低電容省電 | 未知 |

**判讀**：真正屬於「kV × 微安 × 純電容 × 需要極輕小電源」的交集，只有表格前 8 列。後面 6 列是百伏或數十伏負載，PT 沒有結構性優勢，應從本應用域剔除或大幅降權。

### 2.2 電源端（現行方案與其代價）

- **超高增益開關轉換器（UHG converter）**：可達約 **1000× 轉換比**，由約 5–10 V 輸入產生 5 kV，專為 HASEL 軟體移動機器人設計。［來源 5］
- **四象限 DEA 高壓電源**：可獨立產生 **100 V 至 6000 V**、任意波形、可調頻率。［來源 3］
- **雙向返馳（bidirectional flyback）**：可將電活性致動器在 **0 V ↔ 2.5 kV** 之間充放電並回收能量。［來源 23］
- **被動電荷回收**：僅需 2 顆二極體 + 1 顆電阻，可回收約一半電荷。［來源 24］
- **市售灌封模組**：XP Power / EMCO Q 系列（5 kV / 0.125 in³、10 kV / 0.614 in³、0.5 W、輸入 5/12/15/24 V、輸出與輸入成正比、內建 I/O 隔離）；Q101-5 於 Digi-Key 單價 USD 420.06。［來源 15, 16］
- **PT 既有驅動 DEA 的先例**：已有文獻把 PT 最佳化為 **24 V 輸入 → 2.5 kV 輸出**，用於微機器人的介電致動器介面；也有「低電壓驅動、整合 PT 驅動器的 DEAP 致動器」。這條路**不是全新的**，過去十餘年斷續有人做，但沒有形成產品。［來源 2］

### 2.3 PT 本體的性能天花板

- 最佳化單層 PT 功率密度 **40 W/cm³**；疊層 PT 效率 **>94%**、功率密度 **>13 W/cm³**。［來源 17］
- 商用宣稱：Nihon Ceratec 升壓比 **>80**、效率 **>90%**；部分設計文獻提到電壓增益 **500–2000**（取決於輸入輸出條件）。［來源 18, 17］
- **致命弱點**：PT 輸出阻抗高、增益對負載極度敏感 —— 負載電阻大則增益大，一旦負載電阻下降（例如電漿點燃），Q 值被拉低、輸出電壓急劇下降。設計準則明白寫著「PT 不應對輸出負載呈現陡峭依賴」，但這正是 PT 難以做到的事。［來源 20］

---

## 3. 關鍵數字表

| 項目 | 數值 | 來源 |
|---|---|---|
| HASEL 工作電壓區間 | 2–8 kV（zipping 主要發生區），需 >5 kV 才有足夠性能 | [1] |
| HASEL 系統需求 | 供電 ≥4 kV、功率 ≥5 W（但電流極低） | [5] |
| Artimus HALVE 低壓版 | 同等力—應變下驅動電壓降低 **4.9–6.6×** | [4] |
| 無纜 HASEL 電源（2019） | 含電池 **≈100 g**；5 W、0–10 kV（0–5 V 輸入）；3.7 V/500 mAh LiPo | [25] |
| 該電源驅動能力 | 3 疊 × 22 顆致動器，8 kV 下 1 kg 負載達 **40% 應變** | [25] |
| 口袋型十通道 HVPS（2022） | **250 g**，8.4 × 13.3 × 2 cm | [25] |
| UHG 轉換器轉換比 | 約 **1000×**，5–10 V → 5 kV | [5] |
| DEA 實測能量效率 | 壓克力定電荷 **≈26%**；矽膠定電壓 **≈18%** | [17-DEA] |
| 加入電荷回收後 | **≈60%**（理論上限約 90%） | [17-DEA] |
| 被動電荷回收（2 極體+1 電阻） | 回收約 **50%** 電荷 | [24] |
| DEA 所需電場 | **50–120 V/µm** | [22] |
| DEA 壽命（Elastosil 2030） | 100 V/µm、85 °C、85% RH 下 MTTF **1.6 h**；20% RH 下 **>200 h** | [22] |
| 封裝層改善 | 壽命提升 **>1 個數量級**，應變損失可忽略 | [22] |
| PT 功率密度 | 單層最佳化 **40 W/cm³**；疊層 **>13 W/cm³**、效率 **>94%** | [17] |
| PT 商用升壓比/效率 | **>80** / **>90%**（Nihon Ceratec） | [18] |
| EMCO Q 系列尺寸 | 5 kV @ **0.125 in³**；10 kV @ **0.614 in³**；0.5 W | [15] |
| EMCO Q101-5 價格 | **USD 420.06**（10 kV / 0.5 W，Digi-Key qty 1） | [15] |
| ESC 電源規格 | Trek 646：0–±3 kV / 6.5 mA；Matsusada：±1–±10 kV；Comdel：15 kV @ 1 mA | [7] |
| 電黏附夾具市場 | 2024 年 **USD 412.3 M** → 2033 年 **USD 1,344.2 M**（CAGR 15.8%）**（低信度市調）** | [6] |
| 人工肌肉市場 | 2024 年 **USD 1.98 B** → 2030 年 **USD 3.44 B**（CAGR 9.62%）**（低信度市調）** | [31] |
| DextrES 觸覺手套 | **<8 g**，每指 **20 N** 保持力 | [21-clutch] |
| 進階靜電離合器手套 | **1.3 mm 厚**、5 顆離合器、每指 **50 N**；另一系統 **130 g** | [21-clutch] |
| 電黏附離合器改良幅度 | 電壓降 **4–20×**、重量輕 **3–30×**、能耗少 **340–750×** | [21-clutch] |
| 昆蟲尺度 DEA 蜻蜓機器人 | **317 mg**，4 翼 **350 Hz**，升重比 **1.49** | [26] |
| Ventiva ICE 散熱能力 | Lunar Lake 筆電移除 **≈25 W**；2025 宣布上看 **100 W**；2027 目標 40 W TDP | [29] |
| Ventiva 噪音與板面積 | **<15 dBA**；釋放最多 **40%** 板面積 | [29] |
| 可攜 CE-ESI 電源 | **±25 kV** HVPS，系統 **<4 lb**，12 V 鋰電池運作 **≈10 h** | [14] |
| Etulipa 電潤濕看板功耗 | **7 W/m²**（黑白版 <3 W，可太陽能離網 24/7） | [30] |
| Bosch/Arioso NED 微揚聲器 | 有效晶片面積 **10 mm²** 產生 **>120 dB** | [32] |

---

## 4. 「新能力型」應用機會

### 4.1 機會 A：**服裝整合、自帶電源的靜電離合器／制動器**（觸覺手套、被動外骨骼）
- **新能力是什麼**：讓 kV 級電黏附離合器從「桌面上一台高壓電源 + 一條線」變成「縫在布料裡、以鈕扣電池供電、整件衣服 <50 g」的東西。目標是**可整天穿戴、不需外接高壓箱**的力回饋服裝與無動力（unpowered）外骨骼。
- **為什麼以前做不到**：離合器本體已經非常輕（DextrES <8 g、每指 20 N；1.3 mm 厚手套每指 50 N）—— 瓶頸完全在電源。今天最好的多通道 kV 電源是 250 g / 8.4×13.3×2 cm 的口袋盒，比手套重 30 倍。EMCO Q 系列雖然小（5 kV/2 cm³）但每通道 400 美元，10 通道就 4000 美元且無法整合進布料。［來源 15, 25, 21-clutch］
- **是否真非替代性**：**半**。離合器本身不是新東西（已有 2018–2022 的研究原型），PT 換掉的是電源。但由於「重量/形狀因子」是這個應用能否存在的**充分必要條件**，我認為這已越過「更小更薄的替代品」的界線，接近「有了才做得到」。誠實標記：如果只做到「跟現有 250 g 電源一樣但 150 g」，那就純粹是替代品，價值有限；必須做到 **<10 g/通道且可撓** 才算新能力。
- **誰在做**：學術端 DextrES（ETH/EPFL 系）、多相位靜電煞車（EStatiG）、圓柱形低成本靜電離合器；產品端查無以 PT 供電的商用案例。
- **TRL**：離合器本體 TRL 4–5；PT 供電的整合體 **TRL 2–3**。
- **市場訊號**：人工肌肉市場 1.98 B→3.44 B USD（2024→2030，低信度市調）；VR 觸覺與復健外骨骼是被明確點名的驅動力。
- **技術難點**：(i) 離合器電容小（數 nF）而 PT 增益對電容負載敏感，需寬範圍鎖頻；(ii) 每指獨立控制 → 需多通道，PT 一顆一通道的話重量又回來了，必須發展**單 PT 多輸出分時充放**或多輸出結構；(iii) 布料環境的濕度與汗會嚴重降低擊穿場強（見第 5 節）。

### 4.2 機會 B：**高頻循環致動的反應功率回收**（撲翼微飛行器、電滲/靜電微泵、高頻觸覺）
- **新能力是什麼**：把致動器電容做成 PT 諧振腔的一部分，使每個週期的 ½CV² 在機械共振與電場之間**來回震盪而非被丟棄**，讓 kV 級軟體致動器第一次可以「長時間高頻運轉」。
- **為什麼以前做不到**：以 317 mg 蜻蜓機器人 4 翼 350 Hz 為例（來源 26），若致動器電容 1 nF、驅動 5 kV，單次充電能量 12.5 mJ、350 Hz 下反應功率 **4.4 W**（推論計算），而 100 mg 級電池能提供的持續功率遠低於此。今天的驅動器（UHG、四象限、雙向返馳）全部是**開關式**，充放電路徑上必有開關與二極體損耗，被動回收上限只有約 50%。這直接把 DEA 飛行器的續航壓在秒級。［來源 5, 23, 24, 26］
- **是否真非替代性**：**是**。這不是「同一件事做小一點」，而是「續航從秒變分鐘」的相變。用磁性元件也可以做諧振回收（LC tank），但要在 5 kV 做高 Q 的電感在體積與線圈寄生電容上非常不利，而 PT 的高 Q（機械 Q 可達千級）本來就是它的物理本錢。
- **誰在做**：查無任何團隊把 PT 諧振腔與 DEA 電容做聯合設計。既有 PT 能量回收文獻（HAL / IEEE ECCE 系列）是針對 PT 自身箝制電容的回收，不是針對外部致動器。**這是一個明顯的空白。**
- **TRL**：**2**（概念可推導，未見實證）。
- **市場訊號**：弱且遠。昆蟲尺度飛行器目前無商業市場；但同一機制可轉用於「壓電/靜電微泵」與「高頻觸覺」，後者有 VR/汽車 HMI 需求。
- **技術難點**：(i) DEA 電容在行程中會變化 20–30%（推論），諧振點是移動靶；(ii) 機械共振頻率（PT 通常數十至數百 kHz）與致動器所需的機械頻率（數百 Hz）差 2–3 個數量級，必須用調變 —— 這會破壞「單一諧振腔」的美好圖像，是最大的物理障礙，必須誠實面對；(iii) 高場下 PZT 的非線性與發熱。

### 4.3 機會 C：**驅動即感測（driver-as-sensor）的 PT 高壓級**
- **新能力是什麼**：同一顆 PT，一邊輸出 kV 驅動 DEA/HASEL/電黏附墊，一邊由**輸入側**量測諧振頻率／輸入導納偏移，反推負載電容 → 反推致動器位移、接觸狀態、甚至即將發生的擊穿。**輸入側量測意味著量測電路在低壓側、不需要浮在 5 kV 上的隔離放大器。**
- **為什麼以前做不到**：軟體致動器沒地方裝感測器（本體就是可拉伸薄膜），現行 DEA 自感測要在驅動波形上疊加低頻探測訊號並在高壓側量電流，需要高壓隔離的量測前端，成本與體積都不可接受。而 PT 的物理特性剛好給了免費的傳感通道：**並聯電容負載會同時降低 PT 的串聯與並聯諧振頻率，且在並聯諧振附近對負載電容變化最敏感**。［來源 21, 20］
- **是否真非替代性**：**是**。這是「同一顆被動元件同時當主動感測器」的教科書級案例，完全命中客戶「主動/被動兩用」的命題，而且沒有等價的磁性元件替代方案（變壓器沒有機械諧振可供讀取）。
- **誰在做**：壓電致動器的阻抗自感測（同時感測位移與力）已有文獻；PT 的負載電容偵測在「共振變壓器負載調整」文獻中被視為干擾而非資訊。**把兩者接起來用於軟體致動器，查無先例。**
- **TRL**：**2–3**。
- **市場訊號**：間接但強。它是機會 A 與 B 的使能技術（閉迴路控制、擊穿前預警可直接改善第 5 節的壽命問題）。
- **技術難點**：(i) 溫度漂移與 PZT 老化同樣會移動諧振點，需分離「負載變化」與「元件漂移」兩個訊號源；(ii) 電容變化與位移之間的映射在 HASEL（電液 zipping）上高度非線性；(iii) 頻率解析度 vs. 控制頻寬的取捨。

### 4.4 機會 D：**離子風固態散熱與可攜離子源**（EHD 冷卻、手持電漿、無人機載電噴霧）
- **新能力是什麼**：把 kV 產生器做進 2–5 mm 厚的筆電殼內、或做進手持/機載儀器裡。Ventiva ICE 已證明市場真的要這個（<15 dBA、無移動件、釋放 40% 板面積、Intel/Dell 關注）。可攜質譜端，現行 ±25 kV 電源系統 <4 lb 但仍以磅計；PT 若能做到數十克，就打開「無人機載/現場化學偵測」。［來源 29, 14］
- **為什麼以前做不到**：離子風與電噴霧的負載是「純電容 + 電暈電流」，功率極低但電壓極高，磁性方案的體積由絕緣與匝數決定，難以進入毫米級厚度。
- **是否真非替代性**：**半**。Ventiva 的產品本身是新能力（無風扇散熱），但 PT 在其中只是「更薄的高壓源」—— 屬於使能元件而非新能力創造者。**應標記並降權**。但商業訊號是本清單中最強的，適合當「先賺錢的橋頭堡」。
- **誰在做**：Ventiva（ICE9，已展示產品）；壓電直接放電（PDD）冷電漿已有商品化的手持式電漿源，本質上就是 PT 直接生電漿，證明 PT 在此域可量產。［來源 29, 19］
- **TRL**：PDD 電漿 **6–8**（已有產品）；PT 版 EHD 冷卻 **3–4**（推論，查無實證）。
- **市場訊號**：最強。筆電/邊緣裝置/資料中心散熱是十億美元級市場。
- **技術難點**：(i) **PT 本身會機械共振發聲** —— 用在「靜音散熱」產品上是諷刺性的風險，需確認基頻在超音波且無可聞次諧波；(ii) 電漿/電暈點燃後負載阻抗驟降 → PT 增益崩塌（來源 20 明確記載），需要主動的頻率/相位控制；(iii) 熱管理：PZT 在散熱器旁邊工作，居禮溫度與去極化是硬限制。

### 4.5 機會 E（低優先）：**真空/太空環境的電黏附夾持**
- 新能力：真空中無法用真空吸盤，靜電夾持是少數可行方案；PT 在真空中無電暈問題（推論）。半導體 ESC 已是成熟市場（Trek 646、Comdel 15 kV、Matsusada ±1–10 kV），但這些是機架式電源、對體積不敏感 → **純替代，降權**。太空碎片捕捉是真新能力但市場極小。**建議不投入。**

### 4.6 明確剔除
- **電潤濕液態鏡頭（39–58 V）、E Ink 電子紙（±15 V）、數位微流體（300–450 V）、可變形鏡（200–300 V）、CMUT（100–300 V）**：這些都不是 kV 負載，PT 相對於一般的返馳/電荷幫浦沒有結構性優勢，屬於「更小的替代品」，本應用域內建議全部移出。［來源 8, 10, 9, 11, 12］

---

## 5. 反面證據、失敗案例與物理上限

1. **DEA 的壽命問題還沒解，而且對濕度極度敏感。** Elastosil 2030 基 DEA 在 100 V/µm、85 °C、85% RH 下 MTTF 僅 **1.6 小時**；濕度降到 20% RH 才 >200 h。濕度的影響**大於**溫度。這意味著任何「穿在人身上（有汗）」的 DEA 應用面臨結構性障礙 —— 這直接打擊機會 A 的可穿戴版本（靜電離合器因為不靠介電形變、電場較低，受害較小，但仍受影響）。［來源 22］
2. **DEA 需要 50–120 V/µm 的電場才有工業級應變**，這是與擊穿強度的直接拉鋸；文獻明白寫「性能與壽命之間存在權衡」，且動態致動下容易提前擊穿。物理上限清楚：**你不能同時要大應變與長壽命。**［來源 22］
3. **這條路上已有大玩家投入並且沒有留下產品。** SRI 於 2003 分拆 Artificial Muscle Inc.，2006 得獎，2010 被 Bayer MaterialScience 收購並推出 ViviTouch 觸覺產品（用於手機、遊戲控制器、平板）。今天市場上看不到 ViviTouch。**（結局未驗證 —— 搜尋摘要未確認是否關閉，但也未顯示任何在售產品。）** 這是至少 15 年、跨越一家化工巨頭的投入未能成功商業化。［來源 27］
4. **PT 產業自己剛經歷過一次崩塌。** CCFL 背光被 LED 取代後，高壓 PT 產量大幅下滑，多數領先供應商已停止大量生產。這代表：(a) 供應鏈薄、產能與良率經驗流失；(b) 單價高企（客戶原本的成本顧慮在此仍部分成立）；(c) 但也代表產能與 know-how 閒置、可能便宜取得。［來源 18］
5. **PT 對負載的敏感性是本質性的，不是工程細節。** PT 輸出阻抗高，負載電阻下降會直接拉低 Q 與輸出電壓；文獻在電漿應用上明確觀察到「電漿一形成、負載電阻下降、增益就下降」。設計準則說「PT 不應對負載呈陡峭依賴」—— 但這正是最難達成的。對機會 D（電漿/電暈）尤其致命。［來源 20］
6. **PT 增益宣稱值落差極大，不可輕信。** 商用宣稱 >80，設計文獻談 500–2000，UHG 開關式方案已達 ~1000×。也就是說**開關式方案已經追上 PT 的升壓比**，PT 不再有「唯一能做高升壓比」的護城河，剩下的差異化只有體積、EMI、隔離、與（本文主張的）諧振能量回收與自感測。［來源 17, 18, 5］
7. **PT 功率密度數字（13–40 W/cm³）在此應用域幾乎沒有意義。** 本域負載只有 0.5–5 W，體積瓶頸來自**絕緣與抗電暈**（空氣中約 3 kV/mm 的電暈起始場強，推論），不是功率密度。因此「PT 功率密度很高」不能拿來當賣點 —— 這是我在既有文獻宣傳中看到的最常見誤導。
8. **電黏附本身有已被記錄的物理副作用**：電黏附觸控面板存在「優先性汙染（preferential contamination）」現象，已有專門論文研究其機制與多物理模型（Advanced Materials Technologies 2023）。這說明電黏附界面在真實環境中的長期可靠度不是已解問題。［來源 28］
9. **市場數字信心度低。** 電黏附夾具 412.3 M USD（2024）與人工肌肉 1.98 B USD（2024）皆來自二手市調報告（dataintelo、Verified Market Research 系），沒有交叉驗證，**不應作為投資決策的定量依據**，只能當「這個領域有人在賣報告，代表有關注度」的弱訊號。［來源 6, 31］

---

## 6. 未解問題（給下一輪研究）

1. **PT 諧振腔 + 外部電容性致動器的聯合諧振設計，到底有沒有人做過？** 本輪查無。下一輪應直接搜尋 "piezoelectric transformer resonant tank load capacitance co-design DEA"、"resonant charge recovery dielectric elastomer piezoelectric transformer"，以及專利檢索（USPTO/Espacenet）關鍵字 "piezoelectric transformer" AND "electroactive polymer"。若真的空白，這是最有價值的 IP 機會；若已有人做且失敗，必須知道為什麼。
2. **頻率尺度落差怎麼解？** PT 機械諧振通常在數十至數百 kHz，而 DEA/HASEL 所需機械致動頻率是 0.1–350 Hz。這代表「單一諧振腔」的敘事在物理上站不住，必須改成「PT 高頻諧振腔 + 低頻包絡調變 + 雙向能流」。這個架構的實際往返效率（round-trip efficiency）是多少？沒有這個數字，機會 B 無法定案。**這是最關鍵的未解問題。**
3. **Ventiva ICE 的實際電極電壓、電流與電源模組規格為何？** 本輪查無（配額耗盡）。若其工作點是 2–5 kV / 數百 µA，PT 是極佳匹配；若是 10 kV+ 或需要數 mA，則需重新評估。同時應查 Ventiva 融資與量產時程，判斷是否值得作為第一個客戶。
4. **台灣供應鏈的實際能力**：ELECERAM TECHNOLOGY（多層 PT、CCFL 逆變器）目前是否還在生產？多層 PT 的量產良率與單價區間為何？這決定客戶能否在本地取得 pilot 產能，也是「成本打不打得過」的最終答案。本輪僅查到公司存在與產品線描述，未查到產能與價格。

---

## 7. 來源清單

1. Low-voltage electrohydraulic actuators for untethered robotics（PMC 版）— HASEL 需 >5 kV、工作區 2–8 kV、Peano-HASEL 於 5–6 kV 的表現。https://pmc.ncbi.nlm.nih.gov/articles/PMC10775996/
2. Piezoelectric transformer-based high conversion ratio interface for driving dielectric actuator in microrobotic applications（ResearchGate）— PT 24 V 輸入 → 2.5 kV 輸出驅動介電致動器的既有先例。https://www.researchgate.net/publication/308944819
3. High-Voltage Power Supply for Four-Quadrant Dielectric Elastomer Actuators（MDPI Sensors 24(18):6080）— 四象限 DEA 電源，100 V–6000 V 任意波形。https://www.mdpi.com/1424-8220/24/18/6080
4. Low-voltage electrohydraulic actuators for untethered robotics（Science Advances, adi9319）— HALVE 設計較線性介電電液致動器降低驅動電壓 4.9–6.6×。https://www.science.org/doi/10.1126/sciadv.adi9319
5. An Ultra High Gain Converter for Driving HASEL Actuator Used in Soft Mobile Robots（MDPI Biomimetics 8(1):53）— UHG 轉換器約 1000× 轉換比、5–10 V → 5 kV；HASEL 需 ≥4 kV、≥5 W。https://www.mdpi.com/2313-7673/8/1/53
6. Electroadhesive Gripper Market Research Report 2033（Dataintelo，**低信度市調**）— 2024 年 412.3 M USD → 2033 年 1,344.2 M USD，CAGR 15.8%；玩家含 Grabit、Festo、Schunk、OnRobot、Piab、Zimmer。https://dataintelo.com/report/electroadhesive-gripper-market/amp
7. Trek 646 Electrostatic Chuck Supply（DirectIndustry PDF 目錄）— 0 至 ±3 kV、0 至 ±6.5 mA（峰值 10 mA）。https://pdf.directindustry.com/pdf/trek-inc/646-electrostatic-chuck-esc-supply/72064-772158.html ；另見 Matsusada ESC 電源（±1–±10 kV）https://www.matsusada.com/product/electrostatic-chuck-power-supplies/ 與 Advanced Energy Trek 645-HT（0 至 ±1 kV）https://www.advancedenergy.com/en-us/products/high-voltage-power-supplies/e-chuck/bipolar/trek-645-ht-series/
8. Corning Varioptic Lenses Technology / Brochure — Arctic 39N0 工作電壓 39–58 V、極限 24–70 V、1136 Hz 方波 AC 驅動。https://www.corning.com/worldwide/en/products/advanced-optics/product-materials/corning-varioptic-lenses/varioptic-technology.html
9. On the droplet velocity and electrode lifetime of digital microfluidics（Microfluidics and Nanofluidics）— DMF 於 300–450 V DC 的致動比較；HV507 驅動晶片上限 300 V。https://link.springer.com/article/10.1007/s10404-014-1467-y
10. On driving Eink displays（FASANI）— E Ink 標準驅動電壓 ±15 V，由 +22 V/−20 V 降壓供給。https://fasani.de/2025/01/03/on-driving-eink-displays/
11. Chip-scale integrated driver for electrostatic DM control（SPIE 6113）— 每電極可達 300 V 的晶片級驅動器。https://www.spiedigitallibrary.org/conference-proceedings-of-spie/6113/61130X/Chip-scale-integrated-driver-for-electrostatic-DM-control/10.1117/12.651328.short
12. Biasing of Capacitive Micromachined Ultrasonic Transducers（PubMed 27810808）— CMUT 需 100–300 V DC 偏壓。https://pubmed.ncbi.nlm.nih.gov/27810808/
13. MIT proof-of-concept demo of ionic wind propulsion for aircraft（Green Car Congress）— Barrett 團隊固態推進飛行示範，機體約 5 lb，使用輕量化功率轉換器（**具體電壓與轉換器重量查無**）。https://www.greencarcongress.com/2018/11/20181122-mitead.html
14. Portable, Battery Operated Capillary Electrophoresis with ... Ionization Source for Mass Spectrometry（J. Am. Soc. Mass Spectrom.）— ±25 kV HVPS、系統 <4 lb、12 V 鋰電池運作約 10 h。https://link.springer.com/article/10.1007/s13361-015-1314-8 ；Mini 12（2–10 kV）https://pubs.acs.org/doi/10.1021/ac403766c
15. XP Power Q Series 產品頁與 Digi-Key 料號 — 5 kV @ 0.125 in³、10 kV @ 0.614 in³、0.5 W、輸入 5/12/15/24 V、輸出正比於輸入；Q101-5（10 kV/0.5 W）單價 USD 420.06。https://www.xppower.com/product/Q-Series ；https://azcus.digikey.com/en/products/detail/xp-power/Q101-5/5873625
16. Next-Generation, Miniature High Voltage Power Modules（XP Power 白皮書）— 微型高壓模組的體積/整合取捨。https://www.xppower.com/storage/documents/technical-articles/High-Voltage_WP_Next_Gen_Modules.pdf
17. Optimal design of piezoelectric transformer for high efficiency and high power density（Sensors & Actuators A）— 單層最佳化 40 W/cm³；疊層 >94% 效率、>13 W/cm³。https://www.sciencedirect.com/science/article/abs/pii/S0924424705001585 ；另 Power Density of Piezoelectric Transformers Improved Using a Contact Heat Transfer Structure https://www.researchgate.net/publication/221794976
17-DEA. Experimental Study of Dielectric Elastomer Actuator Energy Conversion Efficiency（ResearchGate）— 壓克力定電荷 ≈26%、矽膠定電壓 ≈18%、電荷回收後 ≈60%、理論上限約 90%。https://www.researchgate.net/publication/260330742
18. Piezoelectric Transformers and DC-DC Piezo Converters / 50 Years of Piezoelectric Transformers（mmech.com）— Nihon Ceratec 升壓比 >80、效率 >90%；CCFL 被 LED 取代後高壓 PT 大量生產停止。https://www.mmech.com/transformers ；https://www.mmech.com/images/stories/Standard_Products/Transformers/PT_Introduction/50_Years.pdf ；供應商清單見 https://us.metoree.com/categories/3997/ 與 ELECERAM TECHNOLOGY https://www.etradeasia.com/supplier-2165/ELECERAM-TECHNOLOGY-CO-LTD-/products-c14986/Piezoelectric-transformer.html
19. Piezoelectric direct discharge plasma（Wikipedia）與 Atmospheric pressure plasma jet powered by piezoelectric direct discharge（Korzec 等, Plasma Processes and Polymers 2020）— PT 直接放電產生冷電漿，緊湊、高效、便宜。https://en.wikipedia.org/wiki/Piezoelectric_direct_discharge_plasma ；https://onlinelibrary.wiley.com/doi/full/10.1002/ppap.202000053
20. Effects of capacitive versus resistive loading on high transformation ratio piezoelectric transformers（ResearchGate）與 Discharge plasmas generated by piezoelectric transformers（IOP PSST 15(2):S07）— PT 輸出阻抗高、增益隨負載電阻下降而急劇下降；電漿點燃後增益崩塌。https://www.researchgate.net/publication/260742523 ；https://iopscience.iop.org/article/10.1088/0963-0252/15/2/S07
21. Simultaneous quasi-static displacement and force self-sensing of piezoelectric actuators by detecting impedance（Sensors & Actuators A）— 以阻抗/諧振頻率變化做壓電自感測；並聯電容負載使串聯與並聯諧振頻率同時下降，並聯諧振附近最敏感。https://www.sciencedirect.com/science/article/abs/pii/S0924424717317478
21-clutch. DextrES: Wearable Haptic Feedback for Grasping in VR via a Thin Form-Factor Electrostatic Brake（ACM UIST 2018）— <8 g、每指 20 N。https://dl.acm.org/doi/10.1145/3242587.3242657 ；Glove- and Sleeve-Format Variable-Friction Electrostatic Clutches（Adv. Intell. Syst. 2022，1.3 mm 厚、每指 50 N）https://advanced.onlinelibrary.wiley.com/doi/10.1002/aisy.202200174 ；電黏附離合器電壓降 4–20×、輕 3–30×、能耗少 340–750× https://www.eedesignit.com/electroadhesive-clutch-substitutes-conventional-ones-in-robotics/
22. Lifetime of dielectric elastomer actuators under DC electric fields（EPFL Infoscience）— Elastosil 2030 於 100 V/µm、85 °C、85% RH 下 MTTF 1.6 h，20% RH 下 >200 h；濕度影響大於溫度；封裝層提升壽命 >1 數量級；DEA 需 50–120 V/µm。https://infoscience.epfl.ch/bitstreams/c969c4b3-480e-4a5e-a8b5-21d598824119/download
23. Bidirectional Flyback Converter with Multiple Series Connected Outputs for High Voltage Capacitive Charge and Discharge Applications（ResearchGate）— 0 V ↔ 2.5 kV 充放電與能量回收。https://www.researchgate.net/publication/269398568
24. Power-Efficient Driver Circuit for Piezo Electric Actuator with Passive Charge Recovery（MDPI Energies 13(11):2866）— 2 顆二極體 + 1 顆電阻可回收約一半電荷。https://doi.org/10.3390/en13112866
25. An Easy-to-Implement Toolkit to Create Versatile and High-Performance HASEL Actuators for Untethered Soft Robots（Advanced Science 2019, PMC6662077）— 含電池電源約 100 g、5 W、0–10 kV（0–5 V 輸入）、3.7 V/500 mAh LiPo、3×22 顆致動器在 8 kV 下對 1 kg 達 40% 應變。https://pmc.ncbi.nlm.nih.gov/articles/PMC6662077/ ；A Pocket-Sized Ten-Channel High Voltage Power Supply for Soft Electrostatic Actuators（Adv. Mater. Technol. 2022，250 g、8.4×13.3×2 cm）https://advanced.onlinelibrary.wiley.com/doi/full/10.1002/admt.202101469
26. Design, Characterization, and Liftoff of an Insect-Scale Soft Robotic Dragonfly Powered by Dielectric Elastomer Actuators（MDPI Micromachines 13(7):1136）— 317 mg、4 翼 350 Hz、升重比 1.49。https://www.mdpi.com/2072-666X/13/7/1136 ；Portable, High-Frequency, and High-Voltage Control Circuits for Untethered Miniature Robots Driven by DEA（arXiv）https://arxiv.org/pdf/2502.06166
27. 75 Years of Innovation: Artificial Muscle（SRI International）與 Bayer MaterialScience acquires Artificial Muscle, Inc.（chemeurope）— 2003 SRI 分拆 AMI、2006 得獎、2010 被 Bayer 收購、推出 ViviTouch 觸覺產品；**結局未驗證**。https://www.sri.com/75-years-of-innovation/75-years-of-innovation-artificial-muscle/ ；https://www.chemeurope.com/en/news/114742/bayer-materialscience-acquires-artificial-muscle-inc.html
28. Preferential Contamination in Electroadhesive Touchscreens: Mechanisms, Multiphysics Model, and Solutions（Advanced Materials Technologies 2023）— 電黏附界面的汙染機制，可靠度未解問題。https://advanced.onlinelibrary.wiley.com/doi/full/10.1002/admt.202300213 ；Tanvas 技術說明 https://tanvas.co/blog/what-is-tanvastouch
29. Ventiva 技術頁與新聞稿 — ICE9 固態 EHD 散熱、Lunar Lake 筆電移除約 25 W、2025 宣布上看 100 W、2027 目標 40 W TDP、<15 dBA、釋放最多 40% 板面積、Intel/Dell 關注。https://ventiva.com/technology/ ；https://www.businesswire.com/news/home/20250518248653/en/Ventiva-Unveils-Intelligent-Air-Cooling-Solution-for-Electronics-that-Delivers-Up-To-100-Watts ；https://www.pcworld.com/article/2570821/ventivas-fanless-laptop-cooler-wins-intel-and-dell-over.html
30. Electro Wetting Display technology (EWD)（Etulipa）— 戶外電潤濕看板功耗 7 W/m²，黑白版 <3 W 可太陽能離網運作；**驅動電壓查無**。https://etulipa.com/electro-wetting-display-technology/
31. Artificial Muscle Research Report 2025（GlobeNewswire，**低信度市調**）— 2024 年 1.98 B USD → 2030 年 3.44 B USD，CAGR 9.62%。https://www.globenewswire.com/news-release/2025/12/02/3198178/0/en/Artificial-Muscle-Research-Report-2025-Market-to-Reach-3-44-Billion-by-2030-Driven-by-Advanced-Prosthetics-Soft-Robotics-and-Innovations-in-Electroactive-Polymer-Materials.html
32. Bosch Sensortec Acquires MEMS Microspeaker Innovator Arioso Systems（audioXpress）— NED（Nanoscopic Electrostatic Drive）原理、10 mm² 有效面積產生 >120 dB、強調低電容省電；**驅動電壓查無**。https://audioxpress.com/news/bosch-sensortec-acquires-mems-microspeaker-innovator-arioso-systems
