# 應用B5：壓電當「主動元件」——piezotronics、PET 邏輯、壓電 NEMS 開關、共振體電晶體、聲波訊號處理

> 一句話結論：**「用壓電效應本身做出具增益／邏輯功能的電晶體」（piezotronics、IBM PET）在物理與商業上都已被證明是死路，不建議投入；但同一個技術樹上有三條真正「以前做不到」的支線——(1) 零靜態功耗的壓電 MEMS 喚醒開關、(2) 無磁性材料的聲學非互易元件（取代 ferrite 循環器）、(3) 壓電光機量子轉換器（超導量子位元 ↔ 光纖）——這三條的共同點是：壓電不是去當「更好的電晶體」，而是去當「電子電路根本沒有的那個自由度」（機械域的慢波、非互易、與量子相干介面）。**

---

## 0. 研究方法與限制（誠實揭露，請務必先讀完）

**本回合的限制極為嚴重，必須在引用本文件任何一句話之前理解：**

1. **WebFetch 在本環境被 egress policy 全面封鎖**（任何 URL 回 403）。此為既定條件，任務說明已載明。
2. **本 session 的 WebSearch 配額在我這一輪「開始之前」就已被前面的 agent 耗盡（200/200）。** 我在本輪實際成功執行的搜尋次數是 **0 次**——我發出的第 1 批 2 次查詢即全部回傳 `this session has used its web search budget (200 of 200 WebSearch calls)`。任務要求的 25–35 次查詢**一次都沒有執行成功**。
3. **因此：本文件中沒有任何一條事實是本回合驗證過的。** 我沒有取得任何一個搜尋結果 URL。任務書要求的「每個關鍵事實都要對應到來源清單裡的某個 URL」**本回合無法滿足**，這是本輪的失敗，我不會用假的 URL 去填。
4. 為了不讓這一輪完全歸零，我改為輸出一份**「模型內部知識的假說地圖 + 逐項查證指令」**。所有內容標註三種等級：
   - **【M-高】**：教科書級／領域內廣為人知，我認為被推翻的機率低，但**仍未於本回合驗證**。
   - **【M-中】**：我記得的具體細節（作者、年份、期刊、數量級），**數字可能有偏差，人名與年份可能錯置**。
   - **【M-低】**：具體數值、金額、型號、融資輪次——**視同未知，禁止直接對外引用**，我把它寫出來只是為了給下一輪「該去查什麼」。
   - **【推算】**：由公開物理公式與明示假設自行計算，讀者可自行複核算式，不依賴任何文獻。
   - **【查無】**：我確實不知道，不猜。
5. **我沒有捏造任何專利號。本文件中不出現任何專利號。** 論文標題與公司名若出現，一律附帶信心標籤與查證檢索式。
6. **給協調 agent 的建議**：本題（B5）應在 `CLAUDE_CODE_MAX_WEB_SEARCHES_PER_SESSION` 提高後**整題重跑**，並以第 6 節的檢索式清單為起點。本文件的定位是「重跑時的假說清單與查證計畫」，不是可交付的情報結論。

---

## 1. 結論摘要

1. **【M-高】＋【推算】「壓電電晶體」這個大方向的根本問題是：機械域沒有增益，只有轉換。** 壓電效應是線性的能量轉換（電→機、機→電），本身**不提供功率增益**。要做出邏輯閘所需的 fan-out > 1，必須靠第二個非線性元件（半導體接面、Mott 相變材料、接點通斷）來提供增益。所以所有「壓電主動元件」在架構上都是**「壓電致動器 + 某個真正的開關」的複合體**，壓電只是傳動機構。這一句話同時解釋了 piezotronics 為何做不出邏輯、IBM PET 為何要去找 SmSe、以及壓電 NEMS 開關為何本質上是「繼電器」。**客戶如果期待「壓電體自己就是電晶體」，物理上不存在。**

2. **【M-中】Piezotronics（Zhong Lin Wang，Georgia Tech／北京奈米能源與系統研究所 BINN）的機制是「應變當閘極」，但它調變的是蕭特基能障，不是通道反轉層。** 應變在纖鋅礦半導體（ZnO、GaN、InN、CdS、單層 MoS₂）中產生壓電位（piezopotential），改變金半接觸的能障高度，因而改變電流。代表性成果包括 Science 級的**垂直奈米線壓電電晶體陣列做觸覺成像（taxel-addressable tactile imaging，約 2013）**與 **Nature 級的單原子層 MoS₂ 壓電性與 piezotronics（約 2014）**。**這兩篇的卷期頁碼我不確定，必須查證。** 它的真實定位是**高靈敏應變／觸覺感測器**，不是邏輯元件。

3. **【M-高】Piezotronics 最硬的物理上限是「自由載子屏蔽」。** 壓電位要存在，半導體必須夠絕緣；但要導電，又必須有載子。ZnO 天生是 n 型且本底施體濃度高，壓電位會被自由電子屏蔽掉大部分。文獻上常見的說法是摻雜濃度必須壓到 ~10¹⁷ cm⁻³ 以下壓電位才明顯【M-中】。加上 **ZnO 的壓電係數本來就小（d₃₃ 約 12 pm/V 級，相較 PZT 的數百 pm/V 差 1–2 個數量級【M-中】）**，這是「訊號小 + 會被屏蔽」的雙重夾殺。

4. **【M-中】IBM 的 Piezoelectronic Transduction（PET）邏輯是本題最重要的失敗案例，必須列為決策的核心警訊。** 架構：壓電體（PZT/PMN-PT）在低電壓下產生位移 → 透過剛性軛（yoke）把位移轉成壓力 → 壓在**壓阻材料（稀土硫族化物，SmSe／SmS）**上 → 觸發壓力誘發的絕緣體–金屬（Mott）轉變 → 電阻變化數個數量級。宣稱可在**遠低於 CMOS 的電壓（0.1 V 級）**下開關並大幅降低功耗。主要作者群我記得包含 **Dennis Newns、Glenn Martyna、Bruce Elmegreen、Paul Solomon（IBM T.J. Watson）**，論文期間約 **2012–2017**【M-中】。**具體的效能數字（切換能量 aJ 數、延遲 ps/ns 數、SmSe 的觸發壓力 GPa 數）我一律標為【M-低】，不填。**

5. **【推算】PET 的速度在「聲波渡越時間」上其實不是瓶頸，瓶頸在別處——這點對客戶評估任何「機械式主動元件」都通用。** 壓電體中縱波聲速取 5,000 m/s，若元件厚度縮到 100 nm，機械訊號渡越時間 = 100 nm ÷ 5,000 m/s = **20 ps**；1 µm 厚則 200 ps。也就是說 **奈米尺度的機械元件在原理上可以到 GHz–10 GHz**，速度不是致命傷。致命傷是：(a) 壓電薄膜在 100 nm 以下有嚴重的尺寸效應與基板箝制（clamping），有效 d₃₃ 掉一大截；(b) 位移量絕對值太小（100 nm 厚 × d₃₃ 500 pm/V × 0.1 V = **0.05 nm**，比原子間距還小），必須靠機械放大結構；(c) 10¹⁵ 次以上的機械疲勞壽命；(d) SmSe 這類稀土硫族化物與 CMOS 後段製程（溫度、污染、EPI 品質）不相容。**(b) 與 (d) 是我判斷 PET 停擺的主因【M-中，屬推論】。**

6. **【M-中】反過來，「壓電 MEMS 開關／繼電器」是同一棵樹上唯一有商業實證的分支，但要注意：市場實證的那家（Menlo Micro）用的很可能不是壓電。** 我的記憶是 **Menlo Micro 的 Ideal Switch 是靜電致動 + 專有金屬合金懸臂樑（MM-alloy）於玻璃基板上**，2016 年自 **GE Research** 分拆【M-中】。若屬實，它對本題的意義是**對照組**：它證明了「MEMS 機械開關」這個市場是真的（有客戶、有錢、有量產），但**它證明的是靜電式的可行性，不是壓電式的**。壓電式對靜電式的理論優勢是：**無 pull-in 不穩定、位移與電壓成線性、驅動電壓可從數十 V 降到數 V**【M-高，物理層面】。**Menlo 的產品型號、規格、融資金額全部標【M-低】，本回合查無法證。**

7. **【M-中】Resonant Body Transistor（Dana Weinstein）與「未釋放共振器（unreleased resonators）」是本題中 CMOS 相容性最好的一條。** RBT 概念：把 FET 通道本身當作聲波共振的感測元件（場效感測取代電容感測），在元件內部完成機械→電的轉換並帶增益，約 **2010 年 Nano Letters**、Weinstein 與 Sunil Bhave（Cornell）【M-中】。後續更重要的是 Weinstein 在 MIT／Purdue 的「**不需釋放（no release step）的固態聲波共振器**」——用**聲子晶體（phononic crystal）／布拉格反射層**在標準 CMOS 的既有層別中把聲能關住，因此**不需要任何 MEMS 後製程**，可以直接長在先進節點上（我記得的節點包含 **IBM 32 nm SOI**、**GlobalFoundries 22FDX**）【M-中】。**Intel 是否有對應的 ScAlN on CMOS 共振器工作——【查無】，不確認。**

8. **【推算】聲波元件真正無可取代的物理優勢只有一條：慢波（velocity ~10⁻⁵ c）。** 同頻率下聲波波長比電磁波短約 5 個數量級：5 GHz 電磁波在真空中 λ = 6 cm，而 AlN 縱波（取 v ≈ 10,400 m/s）在 5 GHz 的 λ ≈ **2.1 µm**——**面積縮小約 10⁸–10⁹ 倍**。延遲線更誇張：1 µs 延遲用同軸線需 ~300 m 線長（取 0.66c），用聲波（取 4,000 m/s）只需 **4 mm**。**這條「慢波」優勢是磁性元件、電感電容、與純電子電路都無法提供的，是本題所有「新能力」的物理根源。** 但同時要誠實：這條優勢已經被 SAW/BAW 濾波器（每年數十億美元市場）吃了三十年，**單純的「小型化」不是新能力，是替代品**。

---

## 2. 現況：技術 / 產品 / 玩家

### 2.1 六條支線的定位速覽

| 支線 | 壓電體扮演什麼 | 增益／開關由誰提供 | 本質判定 |
|---|---|---|---|
| (a) Piezotronics / piezo-phototronics | 應變→壓電位，當「閘極」 | **半導體蕭特基接面** | 高靈敏**感測器**，不是邏輯元件 |
| (b) IBM PET 邏輯 | 低壓致動器（位移源） | **SmSe 的 Mott 相變** | 複合式開關；已停擺 |
| (c) 壓電 MEMS/NEMS 開關 | 致動器 | **金屬接點的物理通斷** | 繼電器；零漏電是真賣點 |
| (d) Resonant Body Transistor | 共振腔（被動）＋機電轉換 | **FET 通道（真增益）** | 唯一「主動＋被動同體」的正統解 |
| (e) 聲波訊號處理（延遲、非互易、參數放大） | 慢波介質＋非線性介質 | 視應用；非互易可無需增益 | **新能力密度最高** |
| (f) 鐵電記憶體 / NC-FET | （不是壓電，是同源鐵電材料） | 極化翻轉 | **對照組：錢最多、離產品最近** |

### 2.2 各支線玩家（全部未驗證）

- **(a) Piezotronics**：Zhong Lin Wang（Georgia Tech；後主導北京 BINN），以及大量中國大陸跟隨團隊。**商品化：【查無】——我不知道任何一顆在賣的「piezotronic transistor」產品。** 該團隊的實際商業外溢主要在 **TENG（摩擦奈米發電機）**與自供電感測器，不在邏輯元件。
- **(b) PET**：IBM Research（T.J. Watson）。**現況：我認為已停止，但「IBM 官方宣布終止」這件事我沒有證據，只有「2017 年後我記不得有新論文」這個弱證據【M-低】。**
- **(c) MEMS 開關**：Menlo Micro（靜電，對照組）【M-中】；Analog Devices 有 MEMS 開關產品線（我記得型號前綴 ADGM，但**致動機制與型號請視為【M-低】**）；學界的壓電 AlN 開關散見於 Carnegie Mellon、UPenn（Gianluca Piazza）、Northeastern、Purdue【M-中】。
- **(d) RBT / unreleased resonators**：Dana Weinstein（Purdue，先前 MIT；博士於 Cornell 師從 Sunil Bhave）【M-中】。
- **(e) 聲波非互易**：Andrea Alù（UT Austin → CUNY ASRC）的**聲學循環器（Science，約 2014，以環流介質的角動量偏壓在空氣聲學中做出非互易）**【M-中】；晶片級的時空調變非互易聲波元件我記得 UIUC（Songbin Gong）、Northeastern（Cristian Cassella、Matteo Rinaldi）、Sandia 有工作【M-中】。
- **(e2) 零功耗喚醒**：**DARPA N-ZERO（Near Zero Power RF and Sensor Operations）**，約 2015–2020，我記得專案經理是 **Troy/Roy Olsson**（後來到 UPenn 做 AlScN 鐵電）【M-中】。Northeastern（Rinaldi）的**電漿子增強紅外 + 壓電 MEMS 共振開關做零靜態功耗喚醒感測器**是這條路線的代表【M-中】。
- **(e3) 量子聲學／微波–光轉換**：Yale（Robert Schoelkopf、Yiwen Chu，後者現於 ETH Zürich）的**體聲波共振器耦合超導量子位元**；Chalmers（Per Delsing）的**傳播聲子耦合人造原子（SAW）**；Stanford（Amir Safavi-Naeini）、Caltech（Oskar Painter）的壓電光機轉換。新創我記得有荷蘭 Delft 出身的 **QphoX** 專做微波–光量子轉換【M-中】。
- **(f) 鐵電**：**HfO₂ 鐵電性由 NaMLab／Qimonda 的 Böscke 等人於 2011 年 APL 發表**【M-中】；**Ferroelectric Memory Company（FMC，德國德勒斯登，NaMLab 分拆）**與 GlobalFoundries 22FDX 合作做 FeFET【M-中】；SK Hynix、Micron、Kioxia 均有鐵電記憶體投入【M-中】。**NC-FET 由 Salahuddin 與 Datta 於 2008 年 Nano Letters 提出**【M-高】。

---

## 3. 關鍵數字表

> **全表為【M-低／推算】等級。凡標「推算」者可自行複核；凡標「記憶」者一律視為未知，禁止對外引用。**

| 項目 | 數值 | 等級 | 說明 / 查證方式 |
|---|---|---|---|
| ZnO d₃₃ | ~12 pm/V | 記憶 | 對照 PZT 300–600 pm/V；查 `ZnO piezoelectric coefficient d33 pm/V` |
| 壓電位存續所需 ZnO 施體濃度 | < ~10¹⁷ cm⁻³ | 記憶 | 屏蔽長度決定；查 `piezopotential screening free carriers ZnO doping` |
| 100 nm 壓電體聲波渡越時間 | **20 ps**（v=5,000 m/s） | 推算 | 說明機械速度不是 PET 的瓶頸 |
| 100 nm 厚 × d₃₃ 500 pm/V × 0.1 V 位移 | **0.05 nm** | 推算 | 小於原子間距 → 必須機械放大 |
| AlN 5 GHz 聲波波長（v≈10,400 m/s） | **≈ 2.1 µm** | 推算 | 同頻電磁波 6 cm → 面積縮小 ~10⁸ |
| 1 µs 延遲：同軸 vs 聲波 | **300 m vs 4 mm** | 推算 | 慢波優勢的核心量化 |
| 靜電 MEMS 開關驅動電壓 | 數十 V（~30–90 V） | 記憶 | 壓電式宣稱可降到數 V |
| MEMS 金屬接點壽命需求 vs 現況 | 需 10¹²–10¹⁵ 次；學術常見 10⁸–10¹⁰ | 記憶 | **這是壓電 MEMS 開關最關鍵的待查數字** |
| ScAlN 相對 AlN 的 d₃₃ 提升 | 約 4–5 倍（Sc ~40%） | 記憶 | 查 `ScAlN d33 enhancement scandium concentration` |
| AlScN 鐵電矯頑場 | 數 MV/cm 級 | 記憶 | 遠高於 HfO₂ / PZT；耐久性是問題 |
| BAW/SAW 濾波器年市場 | 數十億美元級 | 記憶 | 用來對照「新能力」的規模基準 |
| Menlo Micro 累計融資 | > 1 億美元級 | **低** | **完全未驗證，禁引** |
| PET 宣稱操作電壓 | 0.1 V 級 | **低** | **完全未驗證，禁引** |

---

## 4. 「新能力型」應用機會

### 4.1 零靜態功耗喚醒開關（Zero-Standby-Power Wake-Up Switch）— **最強候選**

- **新能力是什麼**：一顆感測器在待機時消耗**真正的 0 µA**（不是 1 µA、不是 100 nA），只有在目標訊號（特定頻率的 RF、特定波段的紅外、特定聲學特徵）出現時，壓電／熱機械元件才被入射能量本身驅動並**物理性地閉合一個接點**，喚醒後端系統。
- **為什麼以前做不到**：任何主動電路（比較器、LNA、時脈）都有洩漏電流，這是 CMOS 次臨界導通的物理下限；**「零」與「奈安培」之間隔的不是工程，是元件物理**。壓電／機械元件在未受激時是完全斷路的絕緣體，沒有洩漏路徑可言。
- **是否真的非替代性**：**是（真新能力）**。它不是「更省電的喚醒接收器」，而是把待機壽命的限制從「電池自放電以外還要扣電路耗電」變成「只剩電池自放電」。對於埋在牆裡／地下／體內、十年不換電池的節點，這是質變。
- **誰在做**：DARPA N-ZERO 計畫下的 Northeastern（Rinaldi）等【M-中】。商業化【查無】。
- **TRL**：**3–5**（有 DARPA 資助的實驗室原型與部分外場展示，無商用料號）【M-中，屬估計】。
- **市場訊號**：DARPA 曾投錢是強訊號；但**十年過去仍無商品，代表有硬傷（見 5.3）**。
- **最大技術障礙**：靈敏度（要在極微弱入射功率下產生足夠位移閉合接點）、**接點的可靠性與長期潔淨度（十年不動作後還能不能導通）**、誤觸發率、以及選擇性（如何只對目標訊號反應）。

### 4.2 無磁性材料的聲學非互易元件 / 晶片級循環器與隔離器 — **物理上最正當**

- **新能力是什麼**：在**不使用鐵氧體（ferrite）與外加磁場**的前提下做出循環器／隔離器，且尺寸小到可與 CMOS 整合。手段是**時空調變（spatiotemporal modulation）**——用行進波方式調變聲波介質的剛性／速度，打破時間反轉對稱性。
- **為什麼以前做不到**：非互易在物理上必須破壞時間反轉對稱性，傳統唯一實用手段是**磁化的鐵氧體**（法拉第旋轉）。鐵氧體**不能與 CMOS 共製程、不能微縮、且引入磁場**。所以「無磁循環器」不是成本問題，是**過去根本不存在的能力**。
- **是否真的非替代性**：**是**。而且與本次調查其他章節（15-magnetic-immune-clean）主題一致：這是「非磁」路線的旗艦應用。
- **誰在做**：Alù（聲學循環器，空氣聲學，約 2014）【M-中】；晶片級 AlN／LiNbO₃ 時空調變：UIUC（Gong）、Northeastern（Cassella、Rinaldi）、Cornell/Purdue（Bhave）【M-中】。注意：**Columbia（Krishnaswamy）的 CMOS 無磁循環器走的是 N-path 電路，不是聲波**，是這條路線最強的競爭者，必須查證比較【M-中】。
- **TRL**：**2–4**。
- **市場訊號**：全雙工（full-duplex）通訊、雷達收發共用天線、量子計算讀出鏈（稀釋制冷機內的循環器又大又貴又怕磁場）——**最後這個是最被低估的入口市場**。
- **最大技術障礙**：**插入損耗**。聲波元件的機電耦合係數 k² 有限，調變深度有限，導致隔離度與插入損耗難以兼顧；功率處理能力（聲波非線性）也是硬限制。

### 4.3 壓電光機量子轉換器（微波 ↔ 光學）— **價值最高、最遠**

- **新能力是什麼**：把超導量子位元的 **~5–10 GHz 微波光子**相干轉換成 **~193 THz 的光纖光子**，中介物是**壓電體激發的聲子**（微波→聲子由壓電完成，聲子→光子由光機耦合完成）。這是「量子網路／分散式量子計算」的必要零件。
- **為什麼以前做不到**：微波與光學相差 4–5 個數量級的頻率，直接非線性轉換效率極低；**聲子是唯一同時能與微波電路（透過壓電）和光學模態（透過光彈效應）強耦合的中介物**。沒有壓電就沒有這條路。
- **是否真的非替代性**：**是**，而且是「壓電體不可替代」的少數案例之一。
- **誰在做**：Stanford（Safavi-Naeini）、Caltech（Painter）、Yale/ETH（Chu）、Chalmers（Delsing）；新創 QphoX【M-中】。
- **TRL**：**1–3**（實驗室級，轉換效率與加入雜訊仍未達門檻）。
- **市場訊號**：量子計算資金充沛；但這是**十年期、且客戶數量以「機構」計**的市場。
- **最大技術障礙**：轉換效率、**壓電材料在毫開爾文溫度的雙能階系統損耗（TLS）**、雷射加熱破壞超導。**對台灣廠商而言真正的機會不是做轉換器，是做「低損耗壓電薄膜／薄膜鈮酸鋰異質基板」。**

### 4.4 未釋放式 CMOS 內建聲波共振器（unreleased resonator in logic die）— **半新能力**

- **新能力是什麼**：在**標準 CMOS 製程、不加任何 MEMS 釋放步驟**的前提下，於邏輯晶片內部做出 GHz 級高 Q 聲波共振器，用聲子晶體把聲能關在既有的金屬／介電層結構中。
- **為什麼以前做不到**：傳統 MEMS 共振器需要犧牲層與釋放蝕刻，與先進邏輯製程不相容，因此永遠只能是**外掛的第二顆晶片**。
- **是否真的非替代性**：**半**。它提供的功能（時脈、濾波）本來就存在，是**整合度**的躍進而非全新功能；但「零額外光罩地在 5 nm 邏輯晶片裡放進數千顆高 Q 共振器」會打開**新的架構可能**（每個 IP 區塊自帶頻率參考、晶片內聲波互連、多頻帶可重構前端）。
- **誰在做**：Weinstein 團隊 + IBM 32 nm SOI / GF 22FDX【M-中】。
- **TRL**：**3–4**。
- **最大技術障礙**：先進節點中可用的壓電材料極少（**ScAlN 是主要希望，但 Sc 含量高時漏電與缺陷急增**）；Q 值受限於未釋放結構的聲學漏失；以及**代工廠是否願意為此改製程（商業障礙大於技術障礙）**。

### 4.5 聲波類比訊號處理：延遲線、脈衝壓縮、參數放大 — **明確標示：多為舊能力**

- **誠實判定：這一項大部分不是新能力。** SAW 延遲線與 chirp 濾波器在 1970–80 年代雷達脈衝壓縮中已大量使用，**後來是被數位化（ADC + DSP）取代的**。要主張「新能力」必須說明為什麼數位方案這次贏不了。
- **唯一站得住的論點是【推算】的能耗－頻寬乘積**：在 10 GHz 級瞬時頻寬下做 µs 級延遲，數位方案需要極高取樣率 ADC 與大量記憶體（瓦特級），而聲波延遲線是**被動的、幾乎不耗電**。**所以真正的新能力窗口在「超寬頻 + 極低功耗 + 邊緣端」，不在一般訊號處理。**
- **TRL**：延遲線本身 9（成熟老技術）；「用它做低功耗類比前處理／物理儲備池計算」TRL 2–3。
- **相關**：物理神經網路／儲備池計算曾使用機械－聲學介質作為運算層（我記得 Cornell 的 Peter McMahon 團隊 2022 年 Nature 的 deep physical neural networks 用過聲學／機械板作為其中一種物理層）【M-中】。

### 4.6 壓電 MEMS 繼電器（零漏電開關）— **半新能力，但可靠性是死結**

- **新能力**：真正的**零關斷洩漏**（斷開是物理氣隙）+ **無 pull-in 不穩定的線性致動**（靜電式做不到）+ 低驅動電壓。
- **判定**：對 RF 開關而言是**替代品**（與靜電式 MEMS、PIN 二極體、SOI CMOS 開關競爭）；對**極低功耗邏輯／功率閘控（power gating）**而言接近新能力（省掉整個休眠域的漏電）。
- **最大障礙**：**接點壽命**。這是整個 MEMS 開關產業四十年沒解決的問題，見 5.4。

---

## 5. 反面證據、失敗案例與物理上限

### 5.1 Piezotronics：高引用 ≠ 高 TRL，且有方法學爭議

- **【M-高】** ZL Wang 是全球引用數最高的材料學者之一，但**引用數與商品化完全脫鉤**：piezotronics 提出約二十年，**沒有任何一顆商用 piezotronic 電晶體**。
- **【M-中】** 該領域（特別是相鄰的 ZnO 奈米發電機）在 2008–2012 年間曾有**量測假影（artifact）爭議**：外部團隊質疑所測到的輸出可能來自摩擦電、接觸電位或量測系統本身，而非壓電。我記得質疑方包含 **Max Planck Institute Halle 的 Marin Alexe / Dietrich Hesse 團隊，題名近似 "Energy Harvesting Using Nanowires?"，發表於 Advanced Materials 約 2008 年**【M-中，標題與年份必須查證】。後續該領域普遍採用「**極性反轉測試（switching-polarity test）**」作為標準對照，正是對此爭議的回應【M-中】。
- **【M-高】物理上限**：自由載子屏蔽 + ZnO 壓電係數小 + 應變閘控的等效跨導遠低於場效閘控 → **不可能做出可級聯的邏輯**。它的正確定位是感測器。

### 5.2 IBM PET：這是「模擬數字很漂亮但材料不給力」的教科書案例

- **【M-中】** PET 的效能宣稱大量來自**多物理模擬**（壓電-機械-電輸運耦合模型），實驗端我記得停留在**單顆元件的部分驗證**，從未見到功能性邏輯閘或環形振盪器。
- **【M-中，屬推論】停擺的三個結構性原因**：(1) **SmSe 這類稀土硫族化物的薄膜品質與 CMOS 相容性**——它們對氧極度敏感、需要磊晶、熱預算不合；(2) **微縮悖論**——PET 要低電壓就要薄壓電層，但薄壓電層位移只有皮米–埃級（見 §1.5 推算），必須加機械放大結構，而放大結構又佔面積且降低速度；(3) **在 PET 論文發表的同一時期，CMOS 陣營自己把電壓與功耗持續往下推（FinFET、後來的 GAA），把 PET 的機會窗口關掉**。
- **給客戶的教訓**：**任何「用機械取代電子開關」的提案，都必須先回答「你的位移量在目標尺寸下還剩幾埃」和「你的材料能不能進 fab」。** 這兩題 PET 都沒答好。

### 5.3 零功耗喚醒：DARPA 投了錢，十年後仍無商品

- **【M-中】** N-ZERO 約 2015 年啟動，至今（2026）我**不知道任何一顆可購買的零靜態功耗壓電喚醒開關**。
- **推測的硬傷**（未驗證）：靈敏度不足導致實際偵測距離太短；接點在長期靜置後的黏著／氧化；環境溫濕度造成誤觸發；以及**競爭者其實很強**——次微瓦級的 CMOS 喚醒接收器已經做到 nW 等級，「nW vs 0」對多數應用不值得換一顆貴 10 倍且可靠性未知的 MEMS。**這正是客戶要求的誠實判定：新能力成立，但市場可能不需要那個新能力。**

### 5.4 MEMS 開關的四十年詛咒：接點可靠性

- **【M-高】** 金屬－金屬接點的失效機制（微焊接、材料轉移、有機污染成膜、蠕變）與致動方式無關——**換成壓電致動不會解決接點問題**。壓電只解決「怎麼把它壓下去」，不解決「壓下去之後接不接得通、能不能再彈起來」。
- 這解釋了為何 Menlo Micro 的核心賣點是**專有金屬合金材料**而不是致動方式【M-中】——**產業共識是價值在接點冶金，不在致動器**。**這對客戶是關鍵警訊：若客戶的核心能力是壓電材料，那麼在 MEMS 開關這條路上，客戶握有的是價值較低的那一半。**

### 5.5 聲波非互易的效能天花板

- **【M-高】** 時空調變的非互易強度正比於調變深度 × 調變頻率，而**壓電介質可達成的彈性模數調變深度很小（通常 ≪1%）**，因此需要很長的作用長度或很高的調變功率才能達到 20 dB 以上隔離度——**代價是插入損耗與功耗**。「無磁循環器」在原理上成立，但**是否能贏過已經商用化的 N-path CMOS 循環器與簡單的收發開關**，是必須誠實面對的問題。

### 5.6 對照組的殘酷提醒：錢都在鐵電記憶體，不在壓電主動元件

- **【M-中】** 同樣是「非線性介電材料」，**HfO₂ 鐵電記憶體（FeFET/FeRAM）吸走了這個材料家族絕大多數的產業資金**（FMC、GlobalFoundries、SK Hynix、Micron、Kioxia），原因很簡單：**它不需要機械運動、完全 CMOS BEOL 相容、且對應一個已存在的兆元級市場（記憶體）**。
- **【M-中】** NC-FET（Salahuddin & Datta, 2008）雖然引爆了整個領域，但**「穩態負電容是否存在」至今仍有爭議**，多數批評指出量測到的次-60 mV/dec 是**暫態或遲滯造成的假象**；我記得 Purdue 的 Muhammad Alam 等人寫過批判性回顧（約 2019）【M-中】。**這是另一個「論文很紅、產品沒出」的案例，與 piezotronics 同型。**
- **對客戶的推論**：如果客戶的真實資產是**材料＋薄膜製程**，那麼「AlScN 鐵電 + 壓電雙用薄膜」可能比「壓電主動元件」更接近錢——同一片膜既可做濾波器／共振器（被動），又可做鐵電記憶體／可重構元件（主動），**這反而最貼近客戶「主動被動兩用」的原始命題，而且有真實市場拉力**。**這是本篇最值得下一輪深挖的一條線。**

---

## 6. 未解問題（給下一輪研究）＋ 建議檢索式

**本節是本回合最有價值的產出，請下一輪 agent 直接照做。**

1. **IBM PET 的真實終局**：`IBM piezoelectronic transistor PET logic Newns Martyna` / `piezoelectronic transduction SmSe Mott transition switch` / `Solomon piezoelectronic transduction logic device Nano Letters` / `why did IBM piezoelectronic transistor fail`。要找到：最後一篇論文年份、實驗達成的最佳數字、有無官方終止說明。
2. **Menlo Micro 的實際致動原理**（決定它是對照組還是競爭者）：`Menlo Micro Ideal Switch actuation mechanism electrostatic` / `Menlo Micro MM-alloy cantilever glass substrate` / `Menlo Micro funding round total raised` / `Menlo Micro switch lifetime billion cycles datasheet`。
3. **壓電 MEMS 開關的接點壽命實測數字**：`piezoelectric MEMS relay contact lifetime cycles` / `AlN piezoelectric switch hot switching endurance`。這個數字決定 4.6 是否值得做。
4. **零功耗喚醒是否已商品化**：`DARPA N-ZERO program results transition` / `zero power RF wake-up receiver piezoelectric MEMS commercial product` / `Rinaldi Northeastern zero power infrared digitizing sensor`。
5. **聲學非互易的最佳實測隔離度與插入損耗**：`acoustic isolator spatiotemporal modulation insertion loss isolation dB` / `magnet-free acoustic circulator on chip AlN` / `nonreciprocal MEMS acoustic device Gong Illinois`。**必須同時查 N-path CMOS 循環器的對應數字做公平比較。**
6. **未釋放共振器在先進節點的最新進展**：`unreleased resonator 22FDX GlobalFoundries Weinstein` / `CMOS-integrated acoustic resonator phononic crystal no release` / `ScAlN resonator advanced CMOS node Intel`。
7. **AlScN 鐵電＋壓電雙用薄膜（我判斷最有潛力的一條）**：`AlScN ferroelectric Fichtner 2019` / `ferroelectric AlScN memory Olsson Jariwala Penn` / `AlScN reconfigurable acoustic filter ferroelectric switching` / `ScAlN leakage current high Sc concentration reliability`。
8. **Piezotronics 的爭議文獻**：`Alexe Hesse energy harvesting using nanowires Advanced Materials` / `nanogenerator measurement artifact controversy switching polarity test` / `piezotronic transistor screening effect limitation`。
9. **量子聲學轉換器的最新效率數字與新創融資**：`piezo-optomechanical microwave to optical transducer efficiency 2025` / `QphoX funding quantum transducer` / `bulk acoustic wave resonator superconducting qubit Chu Schoelkopf`。
10. **鐵電記憶體的資金規模（對照組）**：`Ferroelectric Memory Company FMC funding round` / `FeFET 22FDX GlobalFoundries production` / `SK Hynix ferroelectric memory roadmap`。
11. **NC-FET 爭議**：`negative capacitance FET controversy steady state Alam critical review`。
12. **台灣可切入點**：`Taiwan piezoelectric MEMS foundry ScAlN` / `TSMC piezoelectric MEMS BAW filter foundry service` — 判斷客戶在供應鏈的位置。

---

## 7. 來源清單

> **本節必須誠實聲明：本回合成功執行的 WebSearch 次數為 0，因此我沒有任何一個「本回合取得並驗證過」的來源 URL。**
> 任務書要求「每個關鍵事實對應一個 URL」——**本回合未達成**。我拒絕填入未經取得的 URL 來充數。
> 以下列出的是**機構級入口網址（我認為存在但本回合未驗證）**，僅供下一輪 agent 作為起點；每一條都標為未驗證。

| # | 對象 | 網址（**未驗證**） | 用途 |
|---|---|---|---|
| 1 | IBM Research | https://research.ibm.com | 查 PET / piezoelectronic transduction 的官方頁面與出版清單 |
| 2 | Menlo Micro | https://www.menlomicro.com | 查 Ideal Switch 實際致動原理、產品規格、融資 |
| 3 | 北京奈米能源與系統研究所（BINN） | https://www.binn.cas.cn | 查 piezotronics 現況與是否有產業化子公司 |
| 4 | Ferroelectric Memory Company（FMC） | https://www.ferroelectric-memory.com | 對照組：鐵電記憶體的資金與量產狀態 |
| 5 | NaMLab（HfO₂ 鐵電起源） | https://www.namlab.com | 查 Böscke 2011 APL 與後續 |
| 6 | DARPA | https://www.darpa.mil | 查 N-ZERO 計畫頁面、成果轉移狀況 |
| 7 | Purdue ECE（Dana Weinstein） | https://engineering.purdue.edu | 查 RBT / unreleased resonator 出版清單 |
| 8 | Google Scholar | https://scholar.google.com | 逐一驗證第 6 節的論文標題、作者、年份、引用數 |
| 9 | arXiv | https://arxiv.org | 聲學非互易、量子聲學轉換的最新預印本 |
| 10 | Google Patents | https://patents.google.com | **本文件刻意不列任何專利號**；請於此處以第 6 節關鍵字自行檢索 |

**再次聲明**：本文件所有技術內容為模型內部知識，等級標籤已逐條標註；【推算】類的物理計算可獨立複核，其餘**在人工查證前不得引用於任何對外簡報或投資決策文件**。
