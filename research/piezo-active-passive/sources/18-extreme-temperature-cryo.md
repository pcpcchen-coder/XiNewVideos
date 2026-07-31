# 應用B4：極端溫度——高溫（井下/渦輪/太空）與極低溫（量子運算）

> 一句話結論：**本輪 31 次實查後，「極端溫度＝壓電無可替代」這個直覺被證據大幅削弱——高溫端磁性元件沒死（MnZn 鐵氧體 Tc 250–330 °C、商用 200 °C 變壓器在賣、NASA 甚至有 500 °C 變壓器研究），低溫端 GaN+磁性也已在 4 K 做出 91.6 % 效率 / 7.6 W 的升壓轉換器；壓電真正無可取代的只剩兩塊：(a) >300 °C 的「無源無線 SAW 感測」（因為那裡電池 200 °C 就死、IC 225–300 °C 就死，不是壓電比較好，而是根本沒有電子可用），(b) 20 mK 下 Q ≈ 10⁹–10¹⁰ 的聲學共振器做量子記憶體（室溫任何技術差 3–4 個數量級）。至於「高溫主動致動」與「低溫功率轉換」，本輪證據直接否定。**

---

## 0. 研究方法與限制（誠實揭露）

- **本輪實際完成 31 次 WebSearch**（前一版為 0 次，本檔已完整重做並覆寫）。第 32 次查詢時 session 額度（200 次）耗盡，最後一項「低溫壓電變壓器」因此未查成。
- **WebFetch / curl 在本環境全面 403**，全程未使用。因此**所有事實均來自搜尋結果摘要，我沒有開啟過任何一篇論文全文**。
- 標記規則：
  - **【查證】**＝本輪 WebSearch 直接回傳、且有明確 URL 對應。
  - **【未驗證】**＝搜尋摘要有提到、但我無法確認是哪一份來源的原文數字，或數字本身看起來需要原文覆核。
  - **【轉引】**＝來自本專案姊妹 dossier（03/04/15/16），本輪未再獨立核對。
  - **【本文推算】**＝我用查到的兩個數字自己算的，算式寫出來給客戶自行檢查。
- **本輪查無（誠實列出）**：
  - **Piezocryst（奧地利）** 的型號、溫度規格、價格——完全查無，一筆都沒有。
  - **Fuji Ceramics** 高溫加速規規格——查無。
  - 任何高溫壓電感測器的**價格**（Kistler、Piezocryst 皆查無報價）。
  - 井下電池（Li-SOCl₂）的**單價**——查無。
  - **低溫壓電變壓器**的任何實驗數據——最後一次查詢被額度擋掉，等於未查。
  - **imec / Delft / Quantum Motion** 的 cryo-CMOS 功耗具名數字——本輪未查到（只查到 Intel）。
  - **npoint** 低溫規格——查無。
  - Baker Hughes 的 HTHP 溫度分級——查無（只查到 SLB 與 Halliburton）。
  - **壓電陶瓷 Qm 在 4 K 的實測上升倍數**——查無（只查到石英 BAW 的絕對 Q 值，見 §3）。

---

## 1. 結論摘要

1. **【查證】高溫端最重要的反證：磁性元件並沒有在 200 °C 死掉。** MnZn 功率鐵氧體的居里溫度落在**約 250–330 °C**［S12, S13］；奈米晶磁芯耐溫**約 200 °C**（真正的限制常是外殼材料：聚酯 +130 °C、Rynite +155 °C）［S14, S15］；BH Electronics 直接在賣**標稱 200 °C（含環境溫度＋溫升）的變壓器/雙電感**［S16］；NASA 更有**500 °C 級電源變壓器與電感**的研究報告與「高居里溫度磁芯 + 氣隙」路線［S17, S18］，以及 2025 年 R&D 100 獲獎的 **VulcanAlloy，宣稱運作於 500 °C 以上**［S19］。**「壓電取代高溫下無法工作的磁性元件」這個論述，證據上不成立。**
2. **【查證】高溫端真正死掉的是「化學電池」與「矽半導體」，不是磁芯。** Li-SOCl₂ 電池的安全上限約 **165–200 °C**，物理根因是鋰熔點 180.5 °C，一般鋰電限於約 160 °C，加 10 % Mg 合金化才勉強推到 200 °C，且「幾乎不可能再往上」［S8, S9］。SOI 製程 IC 商用合格點約 **225 °C**，部分可到 300 °C［S10, S11］；市售 IC **約 85 % 只到 85 °C、10–12 % 到 125 °C、僅 2–3 % 更高**［S4，未驗證來源歸屬］。**這才是「>300 °C 沒有電子可用」的真正物理牆——而這道牆正好是「無源無線 SAW 感測」的機會所在。**
3. **【查證】高溫壓電感測不是新機會，是 Kistler 已經賣了幾十年的成熟生意。** Kistler 6636A2 / 7636A2 缸壓感測器耐 **350 °C**、過載範圍 450 bar；6124A 為 0–300 bar @ 最高 350 °C、熱靈敏度漂移 ≤±1 %、線性度 ≤±0.3 %，用自家 **PiezoStar 晶體（靈敏度為石英的最高 5 倍）**［S20, S21］；高溫加速規（8209A/8211A 系列，燃氣渦輪監測用）**可量測 >700 °C，短時可到 1000 °C**［S22, S23］。**客戶若想切入這塊，是與 Kistler 正面對打，不是開新戰場。**
4. **【查證】高溫壓電真正的「以前做不到」是無源無線 SAW 感測。** Langasite SAW 諧振器已做出 **600 °C 無線無電池溫度感測**（Vectron International GmbH 參與）［S24, S25］；GaPO₄ SAW 實驗已達 **700 °C**［S26］；化學計量比 LiNbO₃ 晶體的無線 SAW 可到 **600 °C**［S27］。**這是真新能力：在 400–700 °C，既沒有電池也沒有 IC，只有「用射頻打過去、靠聲波回聲讀值」的元件能活。**
5. **【查證，致命反證】但 LiNbO₃ 在高溫是「壽命」問題不是「能不能開機」問題。** LiNbO₃ SAW 元件壽命約 **400 °C 下 10 天、425 °C 下 1 天、450 °C 下只有 2 小時**［S28，未驗證］；LiNbO₃ 化學分解**約 300 °C 就開始**（Li₂O 外擴散），實用上限約 600 °C，>650 °C 缺氧且電阻率崩壞［S29, S30］；LiNbO₃–LiTaO₃ 固溶體的損耗在**約 500 °C 以上急劇上升**［S31, S32］。**姊妹 dossier 引用的「LiNbO₃ MEMS 共振器在空氣中 500 °C 運作」［轉引 03-34］必須加上「能撐多久」的問號。**
6. **【查證】高溫材料的供應鏈是空的。** 文獻直接寫 GaPO₄ 的電聲性能略遜於 langasite，且「**目前市場上沒有好品質的晶體可買**」［S26］。同時 **CISSOID 因 X-FAB 於 2025 年 3 月停產 XI10 製程，被迫對其 175/225 °C 高溫產品線發出 Last Time Buy**（訂單截止 2024-12-30、交貨截止 2025-06-30），且明言「**市場上沒有 XI10 的等效品，這造成供應鏈重大斷裂**」［S10, S33］。**高溫電子這個市場小到連既有玩家都守不住製程——這是對市場規模最直接的負面訊號。**
7. **【查證】低溫端最重要的反證：4 K 的功率轉換已經被 GaN 做掉了。** 已發表「**首個在 4 K 全功能運作的功率轉換器**」：GaN 功率 IC、100 kHz 升壓、輸出達 40 V、**7.6 W 輸出下峰值效率 91.6 %**，且 GaN HEMT 在低溫**導通電阻比室溫下降 4 倍**、無動態 Ron 劣化［S34］。低溫 LDO 也已成熟：22 nm FDSOI 自時脈數位 LDO **效率 98 %**［S35］；capless LDO 從室溫到約 4 K 全溫域**輸出偏差 <2 %**［S36］。**「低溫壓電功率轉換」在這個對照組面前是替代品，不是新能力。**
8. **【查證】低溫端壓電唯一無可取代的是「Q 值」。** 石英 BAW 共振器在 **20 mK** 下 Q **達 10⁹ 量級（15.6 與 65.4 MHz）**，接近 1 GHz 時 **Q 逼近 10¹⁰**［S37, S38］；高階泛音在 4 K 與 20 mK 皆可達 **Q ≈ 10⁹** 且可電控調頻［S39, S40］。**室溫石英 Q 約 10⁶ 量級，這是 3–4 個數量級的差距，任何電磁式共振器都做不到。這是本 dossier 唯一一個「物理上室溫不可能複製」的能力。**

---

## 2. 現況 / 查證結果

### 2.1 井下（油氣 / 地熱）：溫度分級與失效

- **【查證】溫度分級**：SLB 的 HPHT 分類是以「電子、機件、密封件的穩定極限」為界劃出的壓力—溫度邊界［S1, S2］。實務數字：Halliburton 廠內建造並測試過 **175 °C** 的 4-3/4" 密度測井工具，感測器實驗室測到 **175 °C 與 200 °C 存活**；Halliburton/Sperry Sun 的 DOE 合約產出**合格於 195 °C** 的系統；北海現場測試在 **>15,000 ft、最高 186 °C** 成功；依客戶需求規劃的 MWD 工具規格為 **200 °C（392 °F）/ 206 MPa（30,000 psi）、單次作業最長 150 小時**［S3］。
- **【查證】失效與 MTBF**：文獻宣稱井下電子元件經測試在 **225 °C 有 5 年以上壽命**；地質導向與測井電子則被要求在 **>250 °C 連續運作 5 年**，因為停機成本可達每日數百萬美元［S4, S5］。同時文獻直接指出「**每元件 250,000 小時（28.5 年）的 MTBF 對含有運動件的井下系統是不切實際的**」［S4，未驗證來源歸屬］。**「5 年 @225 °C」與「MTBF 不切實際」同時出現，代表這個領域的可靠度宣稱彼此矛盾，客戶不應把任何單一數字當定論。**
- **【查證】地熱（>300 °C）**：Sandia 指出 SOI 元件已商用合格到 **225 °C、許多可續用到 300 °C**，並做出以 **HT83C51 微控制器**為核心、**可到 300 °C（少數限制元件僅 250 °C）且不需保溫瓶（dewarless）**的資料記錄器［S6, S7］。商用端 Thermochem 推出可耐 **400 °C** 的測井工具，鎖定超臨界地熱與深層 EGS［S41］。
- **【查證】電池是硬牆**：Li-SOCl₂ 上限 165–200 °C（根因鋰熔點 180.5 °C）［S8, S9］。**價格查無。**

### 2.2 太空高溫：NASA HOTTech 與 Venus

- **【查證】HOTTech（Hot Operating Temperature Technology）**：目標是讓機器人任務能在**接近或超過 500 °C** 的環境（金星表面、水星、氣態巨行星深層大氣）運作，明確要求「**在金星表面 500 °C 至少長期運作 60 天**」［S42, S43］。**經費規模：早期一輪選出 8＋4 件提案，每件約 US$600k、最長 3 年**［S44］。單一大案例：**GE Research 獲 3 年、US$1.7M**，開發可耐金星環境的自發光 UV 成像器［S45］。
- **【查證】NASA GRC 的 SiC 電子是這條路線的既有霸主**：4H-SiC JFET 積體電路在 **500 °C 空氣中穩定運作 >1000 小時**，>100 電晶體的 IC 達 **>5000 小時**，雙層互連版本**在 500 °C 空氣中運作超過 1 年**，並在 **460 °C / 9.3 MPa 的金星地表模擬腐蝕環境中運作 60 天**；更早的里程碑是 **521 小時，比先前金星任務電子長 100 倍**［S46, S47, S48, S49］。
- **判讀**：**在 460–500 °C，NASA 的既有解是 SiC 邏輯電路，不是壓電。** 壓電在此處若有位置，是「不需供電的感測/共振」與「訊號隔離傳遞」，不是取代 SiC。

### 2.3 高溫壓電材料與商品

見 §3 表。要點：
- **【查證】鉍層狀（BLSF / 鈦酸鉍 Bi₄Ti₃O₁₂）**：訊號產出為天然晶體的 **3–4 倍**、可用到 **510 °C**，居里—外斯溫度約 **650 °C**，被視為取代 PZT 的高溫候選；並有作為高溫＋核輻射環境超音波換能器的實績［S22, S50］。
- **【查證】langasite / GaPO₄ / LiNbO₃**：見 §1.4–1.6。**langasite 是唯一同時有 600 °C 實績、有工業參與者（Vectron）、且晶體買得到的材料。**
- **【轉引】YCOB（800 °C 時 ρ ≈ 2×10⁸ Ω·cm、至 ~1500 °C 無相變）、BLSF 陶瓷 d33 = 32 pC/N / Tc 648 °C / 500 °C 時 ρ = 1.2×10⁸ Ω·cm** ［轉引 03-51, 03-52, 03-54］，本輪未再核對。

### 2.4 量子運算低溫端：熱預算的實際數字

- **【查證】稀釋冰箱冷卻功率**：Bluefors **XLD1000sl 在 4.5 K 運作時 4 K 法蘭約 2000 mW**；**LD450 在 5 K 時約 1500 mW**［S51, S52］。低溫端：**100 mK 約 400 µW、20 mK 約 20 µW**［S53］。成本敏感度極高：「400 µW @100 mK 的系統遠貴於 50 µW @100 mK 的系統，因為要更大的混合室、更多 ³He 循環量與更多泵浦」［S54］。
- **【查證】cryo-CMOS 功耗**：Intel Horse Ridge（4 mm × 4 mm）**消耗 10–140 mW，對應時脈 100 MHz–1.6 GHz**；Horse Ridge II 為 22 nm FinFET（22FFL），已在 **4 K 驗證功能**，可驅動至多 16 個自旋量子位元［S55, S56, S57］。
- **【本文推算】這就是低溫供電瓶頸的算式**：以 16 qubit/晶片、每晶片 10–140 mW 計，控制 **1000 個 qubit 需約 63 顆晶片 → 0.63–8.8 W**，而 4 K 級冷卻功率只有 **1.5–2 W**［S51, S52, S55］。**即使取最樂觀的 10 mW/晶片，1000 qubit 也已吃掉 4 K 預算的三分之一；取中位數就直接超標。這是「低溫供電是真瓶頸」最乾淨的一條算式。**（算式：63 × 10 mW = 0.63 W；63 × 140 mW = 8.8 W。）
- **【查證】同軸線熱負載**：被動熱負載**與線徑平方成正比**，而衰減約與線徑一次方成正比，故從 0.085" 換到 0.047" 可**把被動熱負載降到約 1/4**［S58, S59］。針對 Bluefors XLD1000-SL 的熱模擬顯示，處理器規模 100–225 qubit 時，**若同軸線整合密度提高 3 倍，才能支撐 150 qubit 的運作**［S60］。業界也直陳：同軸線體積與熱負載「**超出稀釋冰箱冷卻容量，是提高 qubit 數的主要物理與熱障礙**」［S61, S62］。
- **【查證】低溫端做電壓調節的現有方案**：綜述論文明列有線供電的四大問題（**級間熱負載、焦耳熱、雜訊耦合、佈線可擴展性**），並提出取消實體佈線、改用**輻射式無線功率傳輸（工作在 >10 GHz 以避開 qubit 的 1–10 GHz 頻段，發射端用相位陣列波束成形，接收端接天線→AC/DC→LDO 穩壓）**［S63］。**注意：這條路線的載體是電磁波，不是聲波——壓電在這份綜述裡沒有位置。**

### 2.5 低溫壓電：致動器與係數

- **【查證】壓電係數在低溫是單調下降的（「低溫極化凍結效應」）**：300–4.2 K 區間，壓電係數與相對介電常數**一致下降**，主因是壓電性的「外在貢獻（extrinsic contribution）」被凍結［S64, S65, S66］。
- **【查證】最關鍵的量化數字**：**PZT 壓電陶瓷做的致動器冷到約 4 K 時，行程約剩室溫的 1/4**［S67，未驗證］。同一份 MADMAX 研究另記：某 PM 壓電冷到 20 K 時電容降到 0.975 µF、對應行程 2.6 µm［S67］。低溫下**電容大幅下降**與**應變係數下降**同時發生［S68］。
- **【查證】補救路線一：摻雜降 Tc**。以 La、Sn 摻雜刻意降低 PZT 的居里溫度以補償外在貢獻的損失，可在 **30 K 達 d33 ≈ 250 pC/N**，優於傳統 DOD 型 PZT 的 **~100 pC/N**［S69］。
- **【查證】補救路線二：弛豫鐵電單晶**。PMN-PT / PZN-PT 單晶**到 20 K 仍保有可觀壓電活性**，且「**30 K 時的 d33 約等於 PZT-5A 在室溫的 d33**」［S70, S71, S72］。**這是低溫端最有價值的材料情報：單晶不是「比較好一點」，而是把低溫的 d 拉回到室溫陶瓷的水準。**
- **【查證】商用生態已存在**：attocube 的低溫奈米定位器以鈦為結構材（輕、非磁、熱膨脹匹配壓電）［S73, S74］；JPE 的 Cryo Linear Actuator（CLA）三支等邊三角配置，步進速度數 µm/s、解析度依溫度 1–5 nm，內含壓電元件可在步進解析度內做 **<<1 nm 類比定位**，工作至 **4.5 K**［S75, S76］。**低溫壓電致動是成熟商品，不是機會。**

### 2.6 量子聲學

- **【查證】超高 Q**：見 §1.8。石英 BAW 在 20 mK 的 Q 約 10⁹、近 1 GHz 逼近 10¹⁰［S37, S38, S39, S40］。
- **【查證】與超導 qubit 耦合**：Chu et al.（Science 2017）將 transmon 耦合到藍寶石 HBAR，達到**強耦合區**，聲子模式壽命 **>10 µs**［S77, S78］。磊晶式 HBAR（NbN 底電極 / GaN 壓電膜 / SiC 基板）達**聲子壽命 500 µs**［S79］。文獻另稱微加工 HBAR 在 >10 GHz 有**超過 1 ms 的相干時間**［S80，未驗證，數字需原文覆核］。
- **【查證】Cleland（UChicago/Argonne）**：2025 年 2 月於 *Nature Communications* 發表「**分處兩片獨立基板的兩個機械共振器之間的確定性多聲子糾纏**」，各自的 SAW 共振器接自己的超導 qubit［S81, S82］；Cleland 於 2024 年獲美國國防部 **Vannevar Bush Faculty Fellow**，明列研究方向為聲子基量子運算［S81］。其他活躍方向：SAW 飛行聲子的片上量子通訊［S83］、超強耦合區可調非線性量子聲學［S84］、懸浮 LiNbO₃ 上的 GHz Lamb 波量子聲學腔［S85］、以 qubit 耦合聲子偵測器搜尋超輕暗物質與高頻重力波［S86］。ETH Zurich 的 Yiwen Chu 組已示範 transmon + HBAR 的混合架構可執行雙位元閘與量子演算法［S87, S88］。

---

## 3. 關鍵數字表

| 項目 | 數字 | 等級 | 來源 |
|---|---|---|---|
| **高溫：邊界** | | | |
| 井下 HPHT 工具實際分級 | 建造/測試 **175 °C**；感測器 175 / 200 °C 存活；DOE 系統合格 **195 °C**；現場 **186 °C @ >15,000 ft**；規劃 MWD **200 °C / 206 MPa / 150 h** | 查證 | S3 |
| 井下電子壽命宣稱 | **5 年 @ 225 °C**；地質導向要求 **5 年連續 @ >250 °C** | 查證 | S4, S5 |
| 市售 IC 溫度分佈 | **~85 % 僅 85 °C、10–12 % 到 125 °C、僅 2–3 % 更高** | 未驗證 | S4 |
| MTBF 現實 | **250,000 h/元件對含動件的井下系統不切實際** | 未驗證 | S4 |
| Li-SOCl₂ 電池上限 | **165–200 °C**；根因 Li 熔點 **180.5 °C**；Li-10%Mg 才到 200 °C；「幾乎不可能再往上」 | 查證 | S8, S9 |
| 商用高溫 IC | SOI 商用合格 **225 °C**，部分續用到 **300 °C**；X-REL 閘驅 **230 °C 環境溫度**；X-FAB HT SOI 接面溫度 **225 °C** | 查證 | S6, S10, S11 |
| 地熱測井 | Sandia dewarless 資料記錄器 **300 °C**（少數元件僅 250 °C，HT83C51）；Thermochem 商用工具 **400 °C** | 查證 | S6, S7, S41 |
| NASA HOTTech | **500 °C、金星表面至少 60 天**；早期一輪 8＋4 案、**每案約 $600k / 最長 3 年**；GE Research **$1.7M / 3 年** | 查證 | S42, S43, S44, S45 |
| NASA GRC SiC IC | 500 °C 空氣 **>1000 h**（100+ 電晶體 **>5000 h**、雙層互連 **>1 年**）；金星模擬 **460 °C / 9.3 MPa 下 60 天**；早期 **521 h = 前代 100 倍** | 查證 | S46–S49 |
| **高溫：磁性元件（反證）** | | | |
| MnZn 功率鐵氧體 Tc | **約 250–330 °C**（另有 100–300 °C 的較寬說法）；核損最低點在 **30–100 °C** | 未驗證 | S12, S13 |
| 奈米晶磁芯 | 耐溫 **約 200 °C**；但常見外殼僅聚酯 **+130 °C**、Rynite **+155 °C** | 查證 | S14, S15 |
| 商用高溫磁性元件 | BH Electronics **200 °C（含環境＋溫升）**變壓器/電感在售 | 查證 | S16 |
| 極高溫磁性研究 | NASA **500 °C 電源變壓器/電感**；「高 Tc 磁芯＋氣隙」在 **200–550 °C 以上**維持穩定低量級電感；**VulcanAlloy >500 °C** | 查證 | S17, S18, S19 |
| **高溫：壓電材料/商品** | | | |
| Kistler 缸壓感測器 | 6636A2 / 7636A2 耐 **350 °C**、過載 450 bar；6124A **0–300 bar @ ≤350 °C**、熱漂移 ≤±1 %、線性 ≤±0.3 %；PiezoStar 靈敏度為石英最高 **5 倍** | 查證 | S20, S21 |
| Kistler 高溫加速規 | 可量測 **>700 °C，短時 1000 °C**（燃氣渦輪監測 8209A/8211A） | 查證 | S22, S23 |
| 鈦酸鉍（BiTi/BLSF） | 訊號產出為天然晶體 **3–4 倍**、可用至 **510 °C**、Tc ≈ **650 °C** | 查證 | S22, S50 |
| Langasite SAW | **600 °C 無線無電池溫度感測**（Vectron 參與）；高溫應變感測亦有實績 | 查證 | S24, S25 |
| GaPO₄ SAW | 實驗達 **700 °C**；但**市場上無好品質晶體可買** | 查證 | S26 |
| LiNbO₃ 高溫上限 | 分解 **約 300 °C 起**（Li₂O 外擴散）；實用上限 **600 °C**；**>650 °C 缺氧、電阻率崩壞** | 查證 | S29, S30 |
| **LiNbO₃ SAW 壽命（致命）** | **400 °C：10 天；425 °C：1 天；450 °C：2 小時** | 未驗證 | S28 |
| LiNbO₃–LiTaO₃ 損耗 | **>約 500 °C 急劇上升** | 查證 | S31, S32 |
| **低溫：熱預算** | | | |
| 稀釋冰箱 4 K 級冷卻功率 | **XLD1000sl ≈ 2000 mW @4.5 K**；**LD450 ≈ 1500 mW @5 K** | 查證 | S51, S52 |
| 稀釋冰箱低溫級 | **100 mK ≈ 400 µW；20 mK ≈ 20 µW** | 查證 | S53 |
| cryo-CMOS 功耗 | Intel Horse Ridge **10–140 mW/晶片**（100 MHz–1.6 GHz）；Horse Ridge II 22FFL，4 K 驗證，驅動 ≤16 自旋 qubit | 查證 | S55, S56, S57 |
| **1000 qubit 控制功耗** | **0.63–8.8 W** vs 4 K 冷卻 **1.5–2 W → 超標** | **本文推算** | S51,S52,S55 |
| 同軸線熱負載 | **∝ 線徑²**；0.085"→0.047" 熱負載降至 **約 1/4**；150 qubit 需同軸整合密度 **提高 3 倍** | 查證 | S58, S59, S60 |
| **低溫：電力電子（反證）** | | | |
| 4 K GaN 功率轉換器 | 首個 4 K 全功能：100 kHz 升壓、**輸出 40 V、7.6 W 下峰值效率 91.6 %**；GaN HEMT **Ron 比室溫降 4 倍**、無動態 Ron 劣化 | 查證 | S34 |
| 低溫 LDO | 22 nm FDSOI 數位 LDO **效率 98 %**；capless LDO 室溫→4 K **輸出偏差 <2 %** | 查證 | S35, S36 |
| **低溫：壓電** | | | |
| **PZT 致動器 4 K 行程** | **約剩室溫的 1/4** | 未驗證 | S67 |
| 低溫效應機制 | 「低溫極化凍結」：300→4.2 K 壓電係數與介電常數**單調下降**；電容大幅下降 | 查證 | S64–S66, S68 |
| La/Sn 摻雜 PZT | **30 K 時 d33 ≈ 250 pC/N**（vs DOD 型 ~100 pC/N） | 查證 | S69 |
| PMN-PT / PZN-PT 單晶 | 到 **20 K 仍保有可觀壓電活性**；**30 K 的 d33 ≈ PZT-5A 室溫值** | 查證 | S70, S71 |
| 商用低溫致動器 | JPE CLA：**4.5 K**，步進數 µm/s、解析度 1–5 nm、類比 **<<1 nm** | 查證 | S75, S76 |
| **低溫：Q 值（唯一新能力）** | | | |
| 石英 BAW @20 mK | **Q ≈ 10⁹（15.6 / 65.4 MHz）**；近 1 GHz **Q 逼近 10¹⁰** | 查證 | S37, S38 |
| 石英 BAW 可調頻 | 4 K 與 20 mK 高階泛音 **Q 高達 10⁹**，可電控調頻 | 查證 | S39, S40 |
| HBAR 聲子壽命 | 藍寶石 HBAR + transmon 強耦合、**>10 µs**；磊晶 GaN/SiC/NbN **500 µs**；微加工 HBAR 宣稱 **>1 ms** | 查證 / 末項未驗證 | S77–S80 |
| **跨溫域** | | | |
| SAW 隔離閘驅工作溫域 | **0.5 K – 544 K**；0.032 pF、2.75 kV、驅動 650 V/11 A GaN 導通 108.8 ns、~150 mW | **轉引** | S89, S90 |

---

## 4. 「新能力型」機會

### 4.1 ★★★★☆ 400–700 °C 無源無線 SAW 感測（真新能力）

- **新能力**：在一個**既沒有電池也沒有 IC** 的溫度區間，用射頻詢答＋聲學回聲讀出溫度/應變/壓力，元件本身**零供電、零電子**。
- **為什麼以前做不到**：這不是「壓電比較好」，是**其他所有東西都死了**——Li-SOCl₂ 電池 200 °C 是硬牆（鋰熔點 180.5 °C）［S8, S9］，SOI IC 商用合格只到 225 °C、極限 300 °C［S6, S10］。**在 400 °C 以上，「有電子的感測器」這個類別本身不存在。**
- **是否真非替代**：**是（真新能力）**。這是本 dossier 高溫端唯一通過「以前根本做不到」測試的項目。
- **誰在做**：Vectron International GmbH（langasite 600 °C 無線溫度感測）［S24］；學界的 langasite 應變感測［S25］、GaPO₄ 700 °C［S26］、化學計量比 LiNbO₃ 600 °C［S27］。
- **TRL**：**4–5**（有具名工業參與者、有完整無線鏈路 demo，但無明確量產型號）。
- **市場訊號**：地熱（Thermochem 400 °C 工具已商用化［S41］）、燃氣渦輪、NASA HOTTech（500 °C / 60 天，每案約 $600k）［S42, S44］。
- **技術難點**：**(a) 材料供應鏈是空的**——GaPO₄「市場上無好品質晶體」［S26］，langasite 供應商極少；**(b) 這是晶圓製程不是陶瓷燒結**［轉引 16-§5.1］；**(c) 是被動元件不是兩用元件**——它完全不做主動端，客戶的「主動/被動兩用」主張在這裡只成立一半。

### 4.2 ★★★★☆ 20 mK 級超高 Q 聲學共振器 / 量子記憶體（真新能力，但已被學界佔滿）

- **新能力**：Q ≈ 10⁹–10¹⁰ 的機械共振器，能把微波光子存成聲子並保持相干［S37–S40, S77–S79］。體積比同頻微波腔小數個數量級（聲速比光速慢 10⁵ 倍）。
- **為什麼以前做不到**：**這是溫度直接買來的物理**——室溫石英 Q 約 10⁶ 量級，20 mK 下 10⁹–10¹⁰，**3–4 個數量級**，來自聲子—聲子散射與二能階系統損耗機制在深冷下凍結。**任何電磁式共振器（含超導腔）都無法在同體積下提供這個 Q。**
- **是否真非替代**：**是，而且是本 dossier 最乾淨的一個「是」。**
- **誰在做**：UWA（Tobar / Goryachev，石英 BAW）［S37–S40］；Yale/ETH（Chu、Schoelkopf，HBAR）［S77, S79, S87］；UChicago/Argonne（Cleland，SAW 聲子糾纏，2025-02 *Nature Comms*；2024 Vannevar Bush Fellow）［S81, S82］。
- **TRL**：**3–4**（實驗室物理，非產品）。
- **技術難點**：**(a) 這是量子元件不是電力元件**，與客戶的「儲能/變壓/隔離/阻尼」主張無交集；**(b) 學術佔位已極密集**，台灣團隊要切入需要 20 mK 級實驗設施與超導量子製程；**(c) 材料純度是天花板**——LiNbO₃ BAW 的低溫性能已被證實受**微量重離子雜質**限制［轉引 03-31］。
- **誠實評註**：**這條路的正確定位是「賣共振器晶片給量子公司」，不是「做兩用功率元件」。**

### 4.3 ★★★☆☆ 極端溫域的隔離供電 / 閘極驅動（半新能力，但對照組變強了）

- **新能力**：以聲學路徑（而非磁耦合/光耦）跨越隔離障壁傳遞功率與訊號，實測涵蓋 **0.5 K – 544 K**［轉引 S89, S90］。
- **為什麼以前做不到**：磁芯有 Tc、光耦 LED 在高溫/輻射老化且在深冷效率崩潰、電解電容與多數矽半導體在液氦溫區不工作。
- **是否真非替代**：**降級為「半」。** 本輪查到兩組硬對照：**(a) 高溫端**——磁性元件並沒有在 200 °C 死（MnZn Tc 250–330 °C、商用 200 °C 變壓器在賣、NASA 有 500 °C 磁性方案）［S12–S19］；**(b) 低溫端**——GaN + 傳統拓撲已在 4 K 做出 **91.6 % / 7.6 W**［S34］。**壓電的唯一剩餘優勢是「同一顆元件橫跨 0.5 K–544 K」這個「單一元件、全溫域」特性，而不是「在任一端點無可取代」。**
- **TRL**：**3–4**（功率僅約 150 mW，離實用 SiC/GaN 模組所需 0.5–2 W 差 3–13 倍）。
- **技術難點**：功率量級；且 **PZT 的 Tc 撐不到 544 K，必須走 LiNbO₃/AlN/langasite**，而 LiNbO₃ 在 400 °C 只有 10 天壽命［S28］——**544 K（271 °C）勉強在 LiNbO₃ 的安全區內，但 400 °C 以上這條路就斷了。**

### 4.4 ★★☆☆☆ 低溫端「省電容、省驅動功率」的壓電式功率調節（半／偏替代）

- **潛在新能力**：低溫下壓電體**電容大幅下降**［S68］，代表驅動無效功（CV²f）同步下降，這對「4 K 只有 1.5–2 W 冷卻功率」的環境**理論上有利**；同時 d 只剩 1/4［S67］但可用 PMN-PT 單晶補回（30 K 的 d33 ≈ PZT-5A 室溫值）［S70, S71］。
- **是否真非替代**：**否，目前是替代品。** 對照組（GaN 4 K 轉換器 91.6 %／FDSOI LDO 98 %）［S34, S35］已經解決同一問題，且該領域的權威綜述在討論低溫供電時，提出的替代方案是**輻射式無線功率傳輸（>10 GHz 電磁波）**，**完全沒有提到壓電/聲學**［S63］。
- **誠實評註**：**「低溫壓電變壓器」本輪的實驗證據是零（最後一次搜尋被額度擋掉）。在沒有任何一篇實驗論文的情況下，這只是一個假說。**

### 4.5 ★☆☆☆☆ 高溫致動（>300 °C 閥門 / 引擎 / 渦輪）（本輪證據直接否定）

- 高溫壓電材料的 d 常數比 PZT 低一個數量級（BLSF d33 = 32 pC/N［轉引 03-51］），而低溫端的補救材料（PMN-PT 單晶）在高溫完全不適用。加上高振速自發熱→Qm 下降→更熱的正回饋［轉引 04-S4/S8］，在已經 300 °C 的環境裡等於「從熱失控起跑點開跑」。
- **判定：不建議投入。** 除非出現 d33 > 200 pC/N 且 Tc > 600 °C 的材料，本項不需重評。

---

## 5. 反面證據、失敗案例與物理上限

1. **【最致命】高溫下磁性元件沒死，「取代磁性」的論述在高溫也不成立。** MnZn Tc 250–330 °C［S12, S13］、奈米晶到 200 °C［S14, S15］、BH Electronics 賣 200 °C 商用變壓器［S16］、NASA 有 500 °C 磁性方案與 VulcanAlloy［S17–S19］。**真正死掉的是電池與矽 IC，不是電感。客戶若把「高溫」當成壓電取代磁性的理由，方向是錯的。**
2. **【致命】低溫功率轉換已被 GaN 做掉。** 4 K、100 kHz 升壓、40 V 輸出、**7.6 W 下 91.6 %**，且 GaN 的 Ron 在低溫**變好 4 倍**［S34］。**低溫對矽/GaN 半導體是加分，不是扣分——這與「高溫」的直覺完全相反，客戶容易誤推。**
3. **【致命】LiNbO₃ 在高溫是「壽命」而非「開機」問題。** 400 °C 十天、450 °C 兩小時［S28］。**姊妹 dossier 的「500 °C 空氣中運作」若沒有壽命數字，實務上可能毫無意義。**
4. **【市場級警訊】高溫電子市場小到既有玩家守不住。** CISSOID 因 X-FAB 停產 XI10（2025 年 3 月），對 175/225 °C 全線發 Last Time Buy，並明言「**市場上沒有等效品，造成供應鏈重大斷裂**」［S10, S33］。CISSOID 更早還接手過 Honeywell 停產的高溫微電子產品線［S34a］。**這個市場已經連續讓兩家玩家退出。**
5. **【供應鏈上限】高溫壓電晶體買不到。** 文獻直陳 GaPO₄「目前市場上沒有好品質的晶體」［S26］。**材料論文有 ≠ 晶圓買得到。**
6. **【低溫端的天花板】壓電係數在低溫是單調下降的物理，不是工程問題。** 「低溫極化凍結」使外在貢獻被凍結，PZT 4 K 行程剩 1/4［S64–S67］。**補救方案（PMN-PT 單晶、La/Sn 摻雜降 Tc）只是把 d 拉回室溫陶瓷的水準，沒有超越。**
7. **【定位錯位】低溫供電領域的權威綜述沒有提到壓電。** arXiv 2511.13965 討論低溫可擴展量子系統的供電時，列出的解方是有線＋LDO 與**輻射式無線功率傳輸（>10 GHz）**，聲學/壓電完全不在候選名單［S63］。**在一個領域的 review 裡完全缺席，通常代表該領域的人已經評估過並排除了它，而不是他們沒想到。**
8. **【既有霸主】高溫壓電感測是 Kistler 的成熟生意（350 °C 缸壓、>700 °C 加速規、自有 PiezoStar 晶體）［S20–S23］；低溫壓電致動是 attocube / JPE 的成熟生意（4.5 K，<<1 nm）［S73–S76］。** 客戶在這兩端都不是開拓者，是後進者。
9. **【方法論反證，沿用前版仍成立】** 本輪 31 次搜尋，**沒有查到任何一家公司在賣「高溫壓電主被動兩用元件」或「低溫壓電功率元件」**。有的是感測器、致動器、量子共振器——全部是**單一功能**產品。**「兩用」這個概念本身，在極端溫度領域找不到任何商業存在。**

---

## 6. 未解問題

1. **低溫壓電變壓器有沒有任何實驗數據？**（本輪唯一被額度擋掉的查詢）核心問題：低溫下 k² 下降但 Qm 上升，而 PT 的增益與效率大致 ∝ k²·Qm——**這個乘積在 4 K 是變好還是變壞？** 若變好，§4.4 從「替代品」升格為「新能力」；若變壞，該項應直接刪除。建議查：`cryogenic piezoelectric transformer 4K efficiency` / `piezoelectric resonator quality factor 4 K measurement PZT` / `k2 Qm product cryogenic piezoelectric`。
2. **高溫 SAW 感測器的實際壽命—溫度曲線（langasite 與 GaPO₄，不只 LiNbO₃）。** LiNbO₃ 已知 400 °C 十天［S28］，但 langasite 的對應數字本輪查無。這是 §4.1 能否商業化的單一決定性數字。建議查：`langasite SAW resonator long term stability 600C hours drift`。
3. **Piezocryst / Fuji Ceramics 的規格與價格（本輪全查無），以及 Kistler 高溫感測器的實際售價。** 沒有價格就無法判斷 §4.1 的毛利空間。
4. **imec / Delft / Quantum Motion / Google 的 cryo-CMOS 每 qubit 功耗**（本輪只查到 Intel）。這決定 §2.4 的推算是保守還是樂觀。建議查：`imec cryo-CMOS power per qubit` / `Google cryogenic control chip power budget`。

---

## 7. 來源清單

> S1–S88 為**本輪 31 次 WebSearch 實際回傳**的來源。S89–S90 標【轉引】，來自姊妹 dossier，本輪未再核對。

### 井下 / HPHT
| # | 標題 | URL | 說明 |
|---|---|---|---|
| S1 | The Defining Series: HPHT Wells (SLB) | https://www.slb.com/resource-library/oilfield-review/defining-series/defining-hpht | SLB 的 HPHT 分類以電子/機件/密封件穩定極限劃界 |
| S2 | High-Pressure, High-Temperature Technologies (SLB Oilfield Review) | https://www.slb.com/-/media/files/oilfield-review/high-pressure-high-temperature | HPHT 技術總覽 |
| S3 | An Innovative High-Temperature High-Pressure LWD Tool (NETL/DOE 最終報告 NT41835) | https://www.netl.doe.gov/sites/default/files/2018-05/NT41835_FinalReport.pdf | ★ 175 °C 工具、195 °C 合格系統、北海 186 °C 現場、MWD 200 °C/206 MPa/150 h |
| S3a | High-Temperature Logging While Drilling Tool (NETL) | https://www.netl.doe.gov/node/3698 | 同上專案頁 |
| S4 | Downhole Electronic Components: Achieving Performance Reliability | https://www.researchgate.net/publication/276346165_Downhole_Electronic_Components_Achieving_Performance_Reliability | 5 年 @225 °C；MTBF 250,000 h 不切實際；IC 溫度分佈（來源歸屬未驗證） |
| S5 | Reliable Electronics for High-Temperature Downhole Applications (SPE-56438-MS) | https://onepetro.org/SPEATCE/proceedings-abstract/99ATCE/99ATCE/SPE-56438-MS/60022 | 高溫井下電子可靠度統計資料庫 |
| S6 | Elimination of Heat-Shielding for Geothermal Tools Operating Up To 300 °C (OSTI) | https://www.osti.gov/biblio/14093 | ★ SOI 商用合格 225 °C、多數可到 300 °C |
| S7 | Dewarless Logging Tool – 1st Generation (Sandia, OSTI) | https://www.osti.gov/servlets/purl/763144 | 300 °C 資料記錄器、HT83C51、少數元件僅 250 °C |
| S8 | 3.6V High Temperature Li-SOCl₂ Batteries (Serui) | https://www.serui-battery.com/News/gongsidongtai/high-temperature-lithium-thionyl-chloride-li-socl2-batteries.html | Li-SOCl₂ 商用溫度上限 165–200 °C |
| S9 | US 9118045 — High temperature lithium battery | https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/9118045 | ★ 鋰熔點 180.5 °C；一般鋰電限 ~160 °C；Li-10%Mg 到 200 °C；「幾乎不可能再高」 |
| S9a | MWD/LWD Downhole Batteries (Excell Battery) | https://excellbattery.com/products/downhole-batteries/ | 井下電池商用供應商 |
| S9b | High-Temperature Battery for Drilling Applications (NETL) | https://www.netl.doe.gov/node/3585 | DOE 高溫井下電池計畫 |
| S41 | First commercial high-temp logging tool introduced by Thermochem | https://www.thinkgeoenergy.com/first-commercial-high-temp-logging-tool-introduced-by-thermochem/ | ★ 商用 400 °C 測井工具（超臨界地熱／深層 EGS） |
| S41a | Long-Term High-Temperature High-Pressure Cable for Geothermal Logging Tools (OSTI) | https://www.osti.gov/biblio/2516861 | 地熱測井纜線的高溫長期問題 |

### 高溫電子 / 半導體
| # | 標題 | URL | 說明 |
|---|---|---|---|
| S10 | CISSOID High Temperature Last Time Buy | https://www.cissoid.com/products/high-temperature/high-temperature-last-time-buy | ★★ X-FAB 2025-03 停產 XI10 → 175/225 °C 全線 LTB；「市場無等效品，供應鏈重大斷裂」 |
| S33 | Last Time Buy for CISSOID High Temperature Components (APC Tech) | https://apctech.com/cissoid-last-time-buy | 訂單截止 2024-12-30、交貨截止 2025-06-30 |
| S10a | CISSOID High Temperature Semiconductors | https://www.cissoid.com/products/high-temperature-products | −55 ~ +225 °C，測試至 −200 ~ +300 °C；SOI |
| S34a | CISSOID 接手 Honeywell 停產高溫微電子產品線 (NAC Semi) | https://www.nacsemi.com/products/cissoid/honeywellcissoidxref/ | 高溫電子市場的第二次退出案例 |
| S11 | X-REL Semiconductor (EASii IC) | https://easii-ic.com/en/x-rel/ | −60 ~ +230 °C 高可靠 IC；閘驅可在 230 °C 環境溫度 |
| S11a | Silicon Carbide Converters and MEMS Devices for High-temperature Power Electronics: A Critical Review (PMC6631602) | https://pmc.ncbi.nlm.nih.gov/articles/PMC6631602/ | 高溫功率電子綜述；X-FAB HT SOI 接面 225 °C |
| S11b | 12-bit Delta-Sigma ADC operating up to 250 °C in 0.18 µm SOI CMOS (arXiv 2501.00482) | https://arxiv.org/pdf/2501.00482 | 250 °C SOI CMOS ADC 實例 |

### NASA HOTTech / Venus
| # | 標題 | URL | 說明 |
|---|---|---|---|
| S42 | HOTTech Attempts to Tackle Venus (NASA Science) | https://science.nasa.gov/science-research/science-enabling-technology/hottech-attempts-to-tackle-venus/ | ★ 計畫目標：500 °C 級環境、金星表面 |
| S43 | Amendment 25: C.24 HOTTech Released (NASA Science) | https://science.nasa.gov/amendment-25-c24-hottech-released | 徵求內容：500 °C 下至少 60 天 |
| S44 | HOTTech Program Overview (VEXAG, LPI/USRA) | https://www.lpi.usra.edu/vexag/meetings/archive/vexag_15/presentations/2-Nguyen-HOTTech-Overview.pdf | ★ 早期一輪 8＋4 案、每案約 $600k、最長 3 年 |
| S44a | NASA High Operating Temperature Technology Program Overview (VEXAG 2017) | https://www.hou.usra.edu/meetings/vexag2017/pdf/8046.pdf | 同計畫另一份簡報 |
| S45 | GE Research Awarded NASA Grant... Venus (GE News) | https://www.ge.com/news/press-releases/ge-research-awarded-nasa-grant-to-develop-high-temperature-solutions-to-enhance | ★ $1.7M / 3 年，自發光 UV 成像器 |
| S46 | NASA Glenn Demonstrates Electronics for Longer Venus Surface Missions | https://www.nasa.gov/news-release/nasa-glenn-demonstrates-electronics-for-longer-venus-surface-missions/ | 521 小時，較前代長 100 倍 |
| S47 | Prolonged silicon carbide IC operation in Venus surface atmospheric conditions (AIP Advances 6, 125119) | https://pubs.aip.org/aip/adv/article/6/12/125119/991931/Prolonged-silicon-carbide-integrated-circuit | 460 °C / 9.3 MPa 金星模擬 |
| S48 | Prolonged 500 °C Operation of 100+ Transistor SiC ICs (NTRS 20170010414) | https://ntrs.nasa.gov/citations/20170010414 | ★ >1000 h、>5000 h @500 °C 空氣 |
| S49 | Progress Towards SiC ASICs for Extreme Temperature and Radiation Environments (NTRS 20240015144) | https://ntrs.nasa.gov/citations/20240015144 | 雙層互連版本 500 °C 空氣 >1 年、金星環境 60 天 |
| S49a | NASA Glenn 2025 R&D 100 Awards | https://www.nasa.gov/newsletters/aerospace-frontiers/nasa-glenn-teams-win-2025-rd-100-awards/ | VulcanAlloy 為 HOTTech 成果 |

### 高溫磁性元件（反證）
| # | 標題 | URL | 說明 |
|---|---|---|---|
| S12 | Development of a New MnZn-Ferrite Soft Magnetic Material for High Temperature Power Applications (J. Electroceramics) | https://link.springer.com/article/10.1007/s10832-004-5162-3 | MnZn 高溫功率鐵氧體開發 |
| S13 | New MnZn ferrite with high saturation flux density (JFE Steel 技報) | https://www.jfe-steel.co.jp/en/research/report/006/pdf/006-08.pdf | ★ Tc 約 250–330 °C；核損最低點 30–100 °C |
| S13a | MnZn core characteristics (magnet-tech) | https://www.magnet-tech.com/core/mnzn/characteristics.htm | Tc 100–300 °C 的較寬說法 |
| S14 | Nanocrystalline Cores (Magnetics via DigiKey) | https://www.digikey.com/en/product-highlight/m/magnetics/nanocrystalline-cores | 飽和 1.25 T；外殼聚酯 +130 °C、Rynite +155 °C |
| S15 | Nanocrystalline Cores for EMI, CT & Power (Acal BFi) | https://www.acalbfi.com/technologies/magnetics/magnetic-cores/nanocrystalline-cores/ | 奈米晶耐溫約 200 °C |
| S16 | High temperature (200 °C) Transformers/Inductors (BH Electronics) | https://www.bhelectronics.com/products/dc-dc-power-products/high-temperature.html | ★ **商用 200 °C 磁性元件在售**（含環境＋溫升） |
| S17 | Ultra High Temperature (500 °C) Power Transformers and Inductors (OSTI 4218367) | https://www.osti.gov/biblio/4218367 | ★ 200–550 °C 以上；高 Tc 磁芯＋氣隙維持穩定電感 |
| S18 | Soft Magnetic Materials (NASA EAP Technology) | https://www.nasa.gov/eap-technology/soft-magnetic-materials/ | NASA 高溫/高頻軟磁材料計畫 |
| S19 | Comparison of High Temperature, High Performance Magnetic Materials (NASA TM-105791) | https://ntrs.nasa.gov/api/citations/19920021154/downloads/19920021154.pdf | 高溫磁材比較的一手技術備忘錄 |
| S19a | High Temperature Magnetic Cores Based on PowderMEMS (PMC8954675) | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8954675/ | 高溫整合式電感磁芯 |
| S19b | High-Temperature Co-Fe-Si-B Amorphous Wire Fluxgate for MWD up to 175 °C (PMC12526687) | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12526687/ | 井下磁性感測元件到 175 °C 的實例 |

### 高溫壓電材料 / 商品
| # | 標題 | URL | 說明 |
|---|---|---|---|
| S20 | New cylinder pressure sensors for large engines (Kistler) | https://www.kistler.com/INT/en/new-cylinder-pressure-sensors-for-monitoring-and-combustion-optimization-of-large-engines/C00000825 | ★ 6636A2/7636A2 耐 350 °C、過載 450 bar；PiezoStar 為石英 5 倍靈敏 |
| S21 | Cylinder pressure sensors for large bore engines 6019A (Kistler) | https://www.kistler.com/INT/en/cp/cylinder-pressure-sensors-for-large-bore-engines-6019a/P0001171 | 大缸徑引擎缸壓感測器產品線 |
| S22 | High temperature accelerometer (Kistler) | https://www.kistler.com/US/en/high-temperature-accelerometer/C00000118 | ★ >700 °C，短時 1000 °C |
| S23 | Piezoelectric accelerometers 8209A (Kistler) | https://www.kistler.com/INT/en/cp/piezoelectric-accelerometers-8209a/P0000490 | 燃氣渦輪永久振動監測 |
| S23a | Challenges to Develop and Design Ultra-high Temperature Piezoelectric Accelerometers (Springer) | https://link.springer.com/chapter/10.1007/978-3-030-47713-4_7 | BLSF 為超高溫加速規敏感元件；引擎監測需求到 900 °C |
| S50 | Use of Bismuth Titanate as an Ultrasonic Transducer for High Temperatures and Nuclear Radiation (PMC8471738) | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8471738/ | ★ BiTi 訊號為天然晶體 3–4 倍、可用至 510 °C、Tc ≈ 650 °C |
| S24 | C3.3 — A 600 °C Wireless and Passive Temperature Sensor Based on Langasite SAW-Resonators (AMA Science) | https://www.ama-science.org/proceedings/details/1995 | ★★ Vectron International GmbH 的 600 °C 無線無源 SAW |
| S25 | High-Temperature SAW Wireless Strain Sensor with Langasite (Sensors 15(11):28531) | https://www.mdpi.com/1424-8220/15/11/28531 | langasite 高溫無線應變感測 |
| S25a | High-temperature static strain langasite SAWR sensor (Sens. Actuators A) | https://www.sciencedirect.com/science/article/abs/pii/S0924424716311906 | 溫度補償與直接應變讀出 |
| S26 | Wireless SAW sensor for high temperature applications: Material point of view | https://www.researchgate.net/publication/253803198_Wireless_SAW_sensor_for_high_temperature_applications_Material_point_of_view | ★ GaPO₄ SAW 到 700 °C；「市場上無好品質晶體」 |
| S27 | Stoichiometric Lithium Niobate Crystals: Towards Identifiable Wireless SAW Sensors Operable up to 600 °C (arXiv 1907.09998) | https://arxiv.org/pdf/1907.09998 | 化學計量比 LN 到 600 °C |
| S28 | Wireless and Batteryless Surface Acoustic Wave Sensors for High Temperature Environments (arXiv 1907.09996) | https://arxiv.org/pdf/1907.09996 | ★ LN SAW 壽命 400 °C/10 天、425 °C/1 天、450 °C/2 h（未驗證來源歸屬） |
| S29 | High-temperature electrical conductivity and electromechanical properties of stoichiometric lithium niobate | https://www.researchgate.net/publication/382225269_High-temperature_electrical_conductivity_and_electromechanical_properties_of_stoichiometric_lithium_niobate | LN 實用上限 600 °C；>650 °C 缺氧、低電阻率 |
| S30 | Correlation of Electrical Properties and Acoustic Loss in LiNbO₃–LiTaO₃ at Elevated Temperatures (Crystals 11(4):398) | https://doi.org/10.3390/cryst11040398 | LN 分解自約 300 °C 起 |
| S31 | Charge transport and acoustic loss in LiNbO₃–LiTaO₃ up to 900 °C (J. Cryst. Growth) | https://www.sciencedirect.com/science/article/abs/pii/S016727382300005X | 損耗在 >500 °C 急劇上升 |
| S32 | Acoustic Loss in LiNb₁₋ₓTaₓO₃ at Temperatures up to 900 °C (phys. status solidi a, 2025) | https://onlinelibrary.wiley.com/doi/10.1002/pssa.202400106 | 同上，2025 年版 |
| S32a | Temperature-dependent acoustic loss at microwave frequencies in thin-film lithium niobate (arXiv 2602.02797) | https://arxiv.org/html/2602.02797 | 薄膜 LN 微波聲學損耗的溫度相依性 |
| S32b | 1–3 Connectivity lithium niobate composites for high temperature operation (Ultrasonics) | https://www.sciencedirect.com/science/article/abs/pii/S0041624X07000613 | LN 複合材料的高溫換能器路線 |

### 低溫：熱預算與供電
| # | 標題 | URL | 說明 |
|---|---|---|---|
| S51 | XLDsl System (Bluefors) | https://bluefors.com/products/dilution-refrigerator-measurement-systems/xldsl-dilution-refrigerator-measurement-system/ | ★ XLD1000sl：4 K 法蘭約 2000 mW（@4.5 K） |
| S52 | LD System (Bluefors) | https://bluefors.com/products/dilution-refrigerator-measurement-systems/ld-dilution-refrigerator-measurement-system/ | ★ LD450：4 K 法蘭約 1500 mW（@5 K） |
| S53 | Cryogen-Free Dilution Refrigerator LD400 (A*STAR A*SEF) | https://asef.a-star.edu.sg/equipment/electronic-and-magnetic-properties-cryogen-free-dilution-refrigerator-ld400-imre | ★ 20 µW @20 mK；400 µW @100 mK |
| S54 | Dilution Refrigerator Price: Complete Cost Guide (OriginQC) | https://originqc.com/blogs/dilution-refrigerator-price | 冷卻功率對成本的非線性影響 |
| S54a | Increased Cooling Power Specifications for Bluefors Dilution Refrigerators | https://bluefors.com/news/increased-cooling-power-specifications-for-bluefors-dilution-refrigerators/ | 官方冷卻功率規格更新 |
| S55 | Intel Details Its Cryogenic Horse Ridge Quantum Control Chip (Tom's Hardware) | https://www.tomshardware.com/news/intel-details-its-cryogenic-horse-ridge-quantum-control-chip | ★ 4×4 mm 晶片消耗 10–140 mW（100 MHz–1.6 GHz） |
| S56 | Intel Debuts 2nd-Gen Horse Ridge Cryogenic Quantum Control Chip (Intel IR) | https://www.intc.com/news-events/press-releases/detail/1429/intel-debuts-2nd-gen-horse-ridge-cryogenic-quantum-control | Horse Ridge II：22FFL，4 K 驗證，≤16 自旋 qubit |
| S57 | Intel's Horse Ridge II Improves the Control for Quantum Computing (EE Times) | https://www.eetimes.com/intels-horse-ridge-ii-improves-the-control-for-quantum-computing/ | 同上技術細節 |
| S58 | Engineering cryogenic setups for 100-qubit scale superconducting circuit systems (EPJ Quantum Technology) | https://link.springer.com/article/10.1140/epjqt/s40507-019-0072-0 | ★ 熱負載 ∝ 線徑²；0.085"→0.047" 降至約 1/4 |
| S59 | 同上 arXiv 版 (arXiv 1806.07862) | https://arxiv.org/pdf/1806.07862 | 同上 |
| S60 | Cryogenic Thermal Modeling of Microwave High Density Signaling (arXiv 2502.01945) | https://arxiv.org/html/2502.01945v2 | ★ XLD1000-SL 熱模擬 100–225 qubit；150 qubit 需同軸密度 3 倍 |
| S61 | Overcoming Cryogenic Cabling Challenges within Dilution Refrigerators (FormFactor) | https://www.formfactor.com/blog/2025/overcoming-cryogenic-cabling-challenges-within-dilution-refrigerators-for-effectively-scaling-quantum-computing/ | 同軸線體積與熱負載為 qubit 擴展主要障礙 |
| S62 | Flexible cryogenic cables for dilution refrigerators could pave path to practical quantum computers (phys.org, 2026-06) | https://phys.org/news/2026-06-flexible-cryogenic-cables-dilution-refrigerators.html | 佈線瓶頸的近期報導 |
| S63 | Power Delivery for Cryogenic Scalable Quantum Applications: Challenges and Opportunities (arXiv 2511.13965) | https://arxiv.org/html/2511.13965 | ★★ 低溫供電權威綜述：有線四大問題；提出 >10 GHz 輻射式 WPT；**完全未提壓電/聲學** |
| S34 | First Demonstration of Cryogenic Power Converter Operational at 4 Kelvin using GaN Power IC | https://www.researchgate.net/publication/406967390_First_Demonstration_of_Cryogenic_Power_Converter_Operational_at_4_Kelvin_using_GaN_Power_IC | ★★ 4 K 100 kHz 升壓、40 V、7.6 W 下 91.6 %；GaN Ron 降 4 倍 |
| S35 | Self Clocked Digital LDO for Cryogenic Power Management in 22nm FDSOI with 98 % Efficiency (arXiv 2505.10234) | https://arxiv.org/abs/2505.10234 | 低溫 LDO 效率 98 % |
| S36 | Cryogenic Low-Drop-Out Regulators Fully Integrated with Quantum (UCD) | https://researchrepository.ucd.ie/rest/bitstreams/50631/retrieve | capless LDO 室溫→~4 K 偏差 <2 % |
| S36a | Integration and Resource Estimation of Cryoelectronics for Superconducting FTQC (arXiv 2601.03922) | https://arxiv.org/pdf/2601.03922 | 容錯量子電腦的低溫電子資源估算 |

### 低溫：壓電材料與致動器
| # | 標題 | URL | 說明 |
|---|---|---|---|
| S64 | Recent development in piezoelectric materials and devices for cryogenic environments (Sens. Actuators A 386, 2025) | https://www.sciencedirect.com/science/article/abs/pii/S0924424725001232 | ★ 低溫（<120 K）壓電綜述；多數材料失去大部分壓電性；relaxor-PT 例外 |
| S64a | 同上開放取用版 (NSF PAR) | https://par.nsf.gov/servlets/purl/10654738 | 同上，可免費取得 |
| S65 | Electromechanical performance evolution of PZT, PMN-PT, and 1–3 piezoelectric composites at cryogenic temperature (J. Appl. Phys. 138, 025101, 2025) | https://pubs.aip.org/aip/jap/article/138/2/025101/3351885/Electromechanical-performance-evolution-of-PZT-PMN | ★ 292→52 K 系統性量測；「低溫極化凍結效應」 |
| S66 | Electromechanical properties of PMN-PT and PZT ceramics at cryogenic temperatures (IEEE) | https://ieeexplore.ieee.org/document/5712258/ | 全部陶瓷隨降溫性能下降；歸因外在貢獻凍結 |
| S67 | Qualification of piezo-electric actuators for the MADMAX booster system at cryogenic temperatures and high magnetic fields (arXiv 2305.12808) | https://arxiv.org/pdf/2305.12808 | ★★ **PZT 致動器 4 K 行程約剩室溫 1/4**；20 K 時電容 0.975 µF / 行程 2.6 µm；4.5 K、5.3 T 實測 |
| S68 | Low-temperature nanopositioners (attocube) | https://www.attocube.com/en/products/nanopositioners/low-temperature-nanopositioners | 低溫下電容與應變係數皆大幅下降；鈦結構 |
| S69 | Cryogenic Piezoelectric Actuator (NASA NTRS 20090029957) | https://ntrs.nasa.gov/api/citations/20090029957/downloads/20090029957.pdf | ★ La/Sn 摻雜 PZT：30 K 時 d33 ≈ 250 pC/N（vs DOD 型 ~100） |
| S70 | Cryogenic actuators and motors using single crystal piezoelectrics (Penn State) | https://pure.psu.edu/en/publications/cryogenic-actuators-and-motors-using-single-crystal-piezoelectric/ | ★★ PMN-PT/PZN-PT 到 20 K 仍有可觀壓電活性；**30 K 的 d33 ≈ PZT-5A 室溫值** |
| S71 | Review on PMN-PT Relaxor Piezoelectric Single Crystal materials for cryogenic actuators (AIAA SciTech 2022) | https://arc.aiaa.org/doi/10.2514/6.2022-2240 | 低溫致動用弛豫單晶綜述 |
| S72 | Review of Cryogenic Piezoelectric Ultrasonic Motors for Aerospace Applications (AIAA SciTech 2025) | https://arc.aiaa.org/doi/abs/10.2514/6.2025-1090 | 低溫超音波馬達綜述（2025） |
| S73 | attocube ANSxyz50 piezoelectric positioner | https://www.directindustry.com/prod/attocube-systems-ag/product-50096-1994440.html | 商用低溫壓電定位器型號 |
| S74 | attocube Premium Line Positioners & Scanners User Manual | https://mrsec.utexas.edu/sites/default/files/Manual%20FlexPositioners%20&%20Scanner_v2.1.1.pdf | 官方手冊（第三方託管） |
| S75 | Cryo & UHV Products Overview (JPE) | https://www.jpe-innovations.com/cryo-uhv-products/ | JPE 低溫產品線 |
| S76 | Cryogenic positioning stage: High resonance (JPE) | https://www.jpe-innovations.com/precision-point/cryogenic-positioning-stage-high-resonance/ | ★ 三支 CLA、數 µm/s、1–5 nm 解析、類比 <<1 nm、至 4.5 K |
| S76a | Review of the application of piezoelectric actuators for SRF cavity tuners (arXiv 2305.06868) | https://arxiv.org/pdf/2305.06868 | 超導高頻腔調諧器的低溫壓電應用綜述 |
| S76b | Low temperature and high magnetic field performance of a commercial piezo-actuator probed via laser interferometry (Rev. Sci. Instrum. 92, 035002) | https://pubs.aip.org/aip/rsi/article/92/3/035002/1061665/Low-temperature-and-high-magnetic-field | 商用壓電致動器低溫＋強磁場實測 |

### 量子聲學
| # | 標題 | URL | 說明 |
|---|---|---|---|
| S37 | Observation of the Fundamental Nyquist Noise Limit in an Ultra-High Q-Factor Cryogenic BAW Cavity (APL 105, 153505) | https://pubs.aip.org/aip/apl/article-abstract/105/15/153505/384726/ | ★ 20 mK 石英 BAW Q 達 10⁹ 量級（15.6 / 65.4 MHz） |
| S38 | 同上 arXiv 版 (arXiv 1410.4293) | https://arxiv.org/pdf/1410.4293 | 同上 |
| S39 | Electro-mechanical tuning of high-Q bulk acoustic phonon modes at cryogenic temperatures (APL 122, 032202) | https://pubs.aip.org/aip/apl/article/122/3/032202/2867030/ | ★ 4 K 與 20 mK 高階泛音 Q 達 10⁹，可電控調頻 |
| S40 | 同上 arXiv 版 (arXiv 2207.01176) | https://arxiv.org/pdf/2207.01176 | 同上；Q 於接近 1 GHz 逼近 10¹⁰ |
| S77 | Quantum acoustics with superconducting qubits (Chu et al., Science 2017) | https://rsl.yale.edu/sites/default/files/2024-09/2017-Y.Chu-Quantum%20Acoustic-science.aao1511.pdf | ★ transmon + 藍寶石 HBAR 強耦合；聲子壽命 >10 µs |
| S78 | 同上 arXiv 版 (arXiv 1703.00342) | https://arxiv.org/pdf/1703.00342 | 同上 |
| S79 | Epitaxial bulk acoustic wave resonators as highly coherent multi-phonon sources (Nature Communications, 2020) | https://www.nature.com/articles/s41467-020-15472-w | ★ NbN/GaN/SiC 磊晶 HBAR，聲子壽命達 500 µs |
| S80 | Quantum Computing Modalities: Acoustic (Phononic) Quantum Systems | https://postquantum.com/quantum-modalities/acoustic-phononic-qc/ | 綜述性整理；「微加工 HBAR >10 GHz 相干 >1 ms」（未驗證） |
| S81 | UChicago scientists make major advance in quantum sound | https://news.uchicago.edu/story/uchicago-scientists-make-major-advance-quantum-sound | ★ Cleland 2025-02 Nature Comms：兩片獨立基板上機械共振器的確定性多聲子糾纏；2024 Vannevar Bush Fellow |
| S82 | Entangling two physically separate resonators (phys.org) | https://phys.org/news/2025-02-entangling-physically-resonators-enables-major.html | 同上報導 |
| S83 | Quantum communication with itinerant surface acoustic wave phonons (npj Quantum Information) | https://www.nature.com/articles/s41534-021-00511-1 | SAW 飛行聲子的片上量子通訊 |
| S84 | Quantum Acoustics with Tunable Nonlinearity in the Superstrong Coupling Regime (arXiv 2505.24865) | https://arxiv.org/pdf/2505.24865 | 超強耦合區可調非線性量子聲學 |
| S85 | GHz Lamb wave resonator cavities on suspended lithium niobate for quantum acoustics (arXiv 2601.13509) | https://arxiv.org/pdf/2601.13509 | 懸浮 LN 的 GHz Lamb 波量子聲學腔 |
| S86 | Listening for new physics with quantum acoustics (OSTI) | https://www.osti.gov/biblio/2477333 | qubit 耦合聲子偵測器搜尋暗物質／高頻重力波 |
| S87 | Best of two worlds: Superconducting qubits and mechanical resonators (ETH Zurich, 2026-05) | https://www.phys.ethz.ch/news-and-events/d-phys-news/2026/05/best-of-two-worlds-superconducting-qubits-and-mechanical-resonators-for-quantum-computing.html | Yiwen Chu 組：transmon + HBAR 執行雙位元閘與演算法 |
| S88 | Optomechanical control of long-lived bulk acoustic phonons in the quantum regime (Nature Physics, 2025) | https://www.nature.com/articles/s41567-025-02989-4 | 量子區長壽命體聲子的光機械控制 |

### 轉引（本輪未核對）
| # | 標題 | URL | 說明 |
|---|---|---|---|
| S89 | Microwave-acoustic-based isolated gate driver for power electronics (arXiv 2511.13412) | https://arxiv.org/pdf/2511.13412 | 【轉引 16】SAW 隔離閘驅：**0.5 K – 544 K**、0.032 pF、2.75 kV、~150 mW |
| S90 | 同上正式期刊版 (*Communications Engineering*) | https://www.nature.com/articles/s44172-026-00681-w | 【轉引 16】 |
