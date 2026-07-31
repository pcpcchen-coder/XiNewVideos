# 現有商品化產品盤點：已經在賣的壓電「兩用/非電感」產品與價格

> 一句話結論：**壓電「陶瓷本體」確實便宜（Murata CERALOCK 諧振器量產價 USD 0.233–0.245／顆，這是全領域的成本地板），但今天市場上所有被當成「主動＋被動兩用」在賣的壓電產品，一律以「系統／儀器」而非「元件」定價（USD 90 → 4,000）——唯一的例外是 Boréas 的壓電驅動 IC（USD 3.71–5.71，DigiKey 現貨）。而本輪最重要的更正是：前版「壓電高壓源比傳統模組便宜 35 倍」的論證站不住腳——TDK CeraPlas HF 實驗樣品在 DigiKey 約 USD 142，對手 XP Power Q101-5（10 kV／0.5 W 完整穩壓模組）約 USD 365–420，差距只有 2.6–2.9 倍，而且 CeraPlas 還需要外掛驅動電路。**

---

## 0. 研究方法與限制（誠實揭露）

**與前一版的關係**：前一版（本檔）自承 WebSearch 有效查詢 **0 次**、全部內容為轉引其他 dossier。**本輪已完整重做並覆寫。**

**本輪實際執行**：

1. **本輪有效 WebSearch = 22 次。** 在第 22 次之後，系統回覆 `this session has used its web search budget (200 of 200 WebSearch calls)`，額度被硬性截斷。任務指派的 30–45 次未能完成，第 23 次起全部失敗。**200 次上限由本 session 多個 agent 共用，並非本 agent 獨用。**
2. **WebFetch 與 curl 在本環境全面 403**，無法用抓網頁替代搜尋。因此**所有價格與規格都來自 WebSearch 回傳的摘要文字，我沒有親自開啟任何一個 URL**。
3. **標記規則（本版重新定義，比前版嚴格）**：
   - `【本輪查得】` = 本輪 WebSearch 摘要直接回傳的內容，附對應 URL。
   - `【未驗證】` = 只出現在單一搜尋摘要、無交叉比對，或來源是報價聚合／中間商網站（Quarktwin、Worldictown、Octopart、easybom、Kynix 等）。**這類價格常有虛報，不可直接用於商業決策。**
   - `【查無】` = 本輪查過但摘要未回傳。
   - `【本輪未查】` = 額度耗盡導致完全沒查。
   - `【前版轉引，本輪未重驗】` = 沿用前一版的二手資料，明確標示。
4. **本輪完成的必查項目**：CeraPlas（部分價格）、relyon piezobrush（**價格首次查到**）、Boréas 全系列（**單價首次查到**）、xMEMS 五款產品規格、TDK PowerHap／PiezoListen（**PiezoListen 價格首次查到**）、Murata CERALOCK（**成本地板首次量化**）與 microblower、Bartels mp6（**價格首次查到**）、Lee Ventus Disc Pump（壽命）、XP Power Q101-5、Coilcraft HTX7045C（**更正前版錯誤**）、離子產生器模組價格地板。
5. **本輪仍未完成（額度截斷）**：
   - 對照組**功率電感／磁性變壓器**的實際階梯價 →【本輪未查】。
   - **CeraPlas 是否已停產／EOL**（2026 年狀態）→【本輪未查】。
   - **超音波無線供電、穿金屬壁供電**是否有商品 →【本輪未查】（前版有一份專門 dossier 結論為「零商品化」，見第 5 節）。
   - **PI / Nanomotion / PiezoMotor / Xeryon 的實際價格級距** →【查無】，只拿到 Xeryon「每多一軸 +€300」一個數字。
   - **臭氧模組**、**汽車負離子模組具名型號** →【本輪未查】。
   - Murata **壓電蜂鳴器**單價 →【本輪未查】。
   - relyon **PZ2 停產時點**本輪未重驗（前版稱 2021-11-30）。
6. **本文件未捏造任何型號、專利號、公司名或數字。**

---

## 1. 結論摘要

1. **【成本地板已被釘死】壓電陶瓷元件的量產價是 USD 0.23–0.25／顆。** Murata CERALOCK 陶瓷諧振器 `CSTNE8M00G550000R0` 3,000 顆整卷 USD 735 ＝ **USD 0.245／顆**；6,000–27,000 顆 **USD 0.239**；30,000+ **USD 0.233**【未驗證，單一摘要】。這是 3.2×1.3 mm、含內建負載電容、SMD reel 包裝的完整量產件。**「壓電本質上貴」是錯的——貴的是低量、貴的是系統整合，不是陶瓷。**（來源 61、60）
2. **【本輪最大更正】壓電高壓源相對傳統高壓模組的價格優勢只有 2.6–2.9 倍，不是前版說的 35 倍。** DigiKey 上 CeraPlas HF 實驗樣品 `Z63000Z2910Z1Z60` 約 **USD 142.25**【未驗證】；對手 XP Power／EMCO `Q101-5`（10 kV／50 µA／0.5 W，輸入 0.7–5 V 比例控制，含穩壓）在 Worldictown 標 **USD 365.27**（庫存 2,019 顆），前版轉引 DigiKey **USD 420.06**。**而 Q101-5 是完整模組，CeraPlas 還要自己做 50 kHz 驅動級。前版拿 STEMINC USD 11.88 的裸 PT 去比 USD 420 的完整模組，是不對等比較。**（來源 2、75、74）
3. **【首次查到】relyon piezobrush PZ3 Professional Set 官方售價 EUR 2,540.00**（relyon 線上商店），美國牙科通路 Chairside Solutions 標 **USD 3,789.00**。relyon 另提供 **PZ3 租借機（Leihgerät）**。PZ3-i 自動化版價格仍【查無】（Intertronics、igus rbtx 皆未公開）。（來源 15、16、17、18）
4. **【首次查到】Boréas 壓電驅動 IC 是本領域唯一「元件級定價」的兩用產品**：DigiKey 單價 `BOS0614CWR` **USD 3.71**（四通道）、`BOS1921CQR` **USD 4.16**（24-VFQFN）、`BOS1931CWR` **USD 5.12**、`BOS1921CWR` **USD 5.71**（20-WFBGA）【未驗證，單一摘要】。全部從 3–5.5 V 供電輸出 **190 Vpp**，僅需 7 顆被動元件，啟動 <300 µs。（來源 26、27、28、30）
5. **【重要產品線變動】BOS1901 已不建議用於新設計**，官方分流為 **BOS1921（觸覺）** 與 **BOS1931（微泵）**；`BOS1901-KIT-B02` 在 DigiKey 已標 obsolete。**Boréas 另開了一條「微泵液冷（Micropump Liquid Cooling）」應用線**——這代表壓電驅動 IC 的成長點正從觸覺移向散熱／流體。（來源 25、32、39）
6. **【新能力訊號最強的一條】xMEMS `XMC-2400` µCooling「晶片上的風扇」**：9.26 × 7.6 × 1.08 mm、**< 150 mg**、比非矽主動散熱方案**小輕 96%**、氣流 **39 cc/s**、背壓 **1,000 Pa**、耗電僅約 **30 mW**、以超音波頻率運作故**人耳完全聽不到**、**IP58**。2025 Q1 送樣，CES 2025 創新獎。**台灣由益登科技（EDOM）代理**。公開單價【查無】。（來源 44、45、46）
7. **【反面證據】壓電喇叭的元件價格高得離譜**：TDK PiezoListen `PHUA3030-049B-00-000`（30×30 mm、0.49 mm 厚、400 Hz–20 kHz、≤24 Vpp 出 80 dB）在 **DigiKey USD 93.83／Mouser USD 93.42**，九家通路報價區間 USD 78.24–93.42【未驗證】。相對於一顆傳統動圈微喇叭（< USD 1 級），**這是壓電「兩用」在消費電子撞牆的直接證據**。（來源 54、55、56）
8. **【反面證據】離子產生這條路已經被 USD 0.80 封死**：非壓電的針尖式負離子模組 OEM 價 **USD 0.80／顆 @1,000+**（浙江樂清 Yueqing Yilerck，搜尋摘要，【未驗證】），零售模組規格 −9.0 ± 0.5 kV、耗電 < 1 W（12 V／20 mA）、≥3,200 萬 ions/cm³。**壓電變壓器在這個價格帶完全沒有進入空間。**（來源 81、82）
9. **【前版錯誤更正】Coilcraft `HTX7045C` 不是 12 kV。** Coilcraft 官網頁面標示：繞組間電容**低至 0.7 pF**、隔離 **2800 Vrms／4000 VDC（1 分鐘 hipot）**，用於開迴路 LLC 拓樸的隔離閘極驅動偏壓電源（SiC／GaN／IGBT）。**前版寫「0.75 pF / 5 W / 12 kV」，其中 12 kV 本輪查無佐證，請勿再引用。** 價格【查無】。（來源 79、80）
10. **【可買到的微泵價格首次落地】Bartels `mp6` 壓電微泵在 DigiKey Marketplace 約 USD 65.65–67／顆，MOQ 10**，現貨 960 顆、1,360 顆在途（2026-04-25 到貨）、預估備貨 10,000 顆、前置期 12 週【未驗證】。（來源 66、67）

---

## 2. 現況：技術 / 產品 / 玩家

### 2.1 冷電漿：唯一 TRL 9、且本輪終於問到價格的兩用元件

同一片硬質 PZT 同時是（i）機械共振器、（ii）Rosen 型升壓變壓器（被動）、（iii）放電電極（主動）。TDK 技術文獻明確描述其材料為**可與內電極銅共燒的硬 PZT**，兼具高且穩定的機械 Q 值與良好機電耦合、低損耗（來源 6）。

**元件層規格（注意本輪查到的新矛盾）**

| 來源 | 輸入 | 頻率 | 輸出 |
|---|---|---|---|
| TDK tech-library「Cold plasma from a single component」【本輪查得】 | **12 Vpp** | **52 kHz** | 「several kV」 |
| 前版轉引 datasheet | 12–24 V | ~50 kHz | **< 15 kV**、升壓比 > 1000、8.0 W max |
| 前版轉引 TDK featured story | 12–24 Vpp | 50 kHz | 最高 **20 kV** |

**三個來源三組數字（「several kV」／「< 15 kV」／「20 kV」）。本輪新增的 TDK 官方技術文章寫的是最保守的一組。做功率／絕緣設計前必須向 TDK 取得正式 datasheet 定案。**

**價格（本輪首次取得，但全部標未驗證）**

| 訂購碼 | 品名 | 通路 | 價格 |
|---|---|---|---|
| `Z63000Z2910Z1Z60` | CeraPlas HF 實驗樣品（DK# 495-77395-ND） | DigiKey | **≈ USD 142.25**【未驗證】 |
| `Z63000Z2910Z 1Z61` | CeraPlas HF Development Kit | DigiKey / epcos.zeano-de | 【查無】 |
| `Z63000Z2910Z01Z69` | CeraPlas Evaluation Kit V2 | Quarktwin（聚合商） | **USD 653.40(1) / 588.06(10) / 529.25(100) / 476.33(500) / 428.70(1k)**【未驗證，中間商報價】 |
| `Z63000Z2910Z 1Z68` | F series packaged component | Sekorm（轉載） | 【查無】 |

> **必須警告**：`Z63000Z2910Z` 是 TDK 通用的樣品／套件訂購碼前綴，同一前綴下 DigiKey 還有 `1Z-2`（USD 32.93）、`1Z-4`（USD 87.81）、`1Z-5`（USD 186.84）等【未驗證】，但這些被歸類在 **Motors/Actuators**，**極可能是 PowerHap 或其他致動器套件，不是 CeraPlas**。除 `1Z60` 外不要把這些數字當成 CeraPlas 價格。

**評估套件工作點**：前版轉引 key-components，24 V 單電源、預設約 4.5 W、可選 2–7 W（比「最大 8 W」低）【前版轉引，本輪未重驗】。

**系統層（relyon plasma GmbH，TDK 子公司）**

- **piezobrush PZ3**：手持機，PDD®（Piezoelectric Direct Discharge）技術，核心即 CeraPlas；整機最大功耗 **18 W**、電漿 < 50 °C、五種可換模組（Standard／Nearfield／Needle／Nearfield Needle／Multigas）。**Professional Set = 主機 ＋ Standard 模組（處理塑膠等非導體）＋ Nearfield 模組（處理不鏽鋼、CFRP 等導體）**（來源 15、24）。
- **價格：EUR 2,540.00（relyon 官方商店）／USD 3,789.00（Chairside Solutions 牙科通路）**。relyon 另有**租借機（Leihgerät PZ3）**產品頁——**這是一個很重要的商業訊號：需要提供租借，代表客戶對 EUR 2,540 的購買門檻有抵抗。**（來源 15、17、18）
- **piezobrush PZ3-i**：自動化整合版，可作機器人末端執行器，已上架 **igus rbtx**；英國 Intertronics、Ulbrich Group 均為通路。**價格全部不公開**（來源 19、21、23）。
- TDK 官網直接托管 **piezobrush PZ3 操作手冊 PDF**（`tdk-electronics.tdk.com/inf/130/Cold_Plasma/Operating_Instructions.pdf`），顯示元件商與系統商在文件層面高度綁定（來源 22）。

### 2.2 壓電驅動 IC：本領域唯一「元件級定價」的兩用產品

Boréas Technologies（加拿大）的 **CapDrive** 是一種帶能量回收的高壓壓電驅動架構，從 3–5.5 V 供電產生最高 **190 Vpp** 波形，僅需 **7 顆被動元件**，啟動時間 < 300 µs（來源 25、35）。

| 型號 | 定位 | 關鍵規格【本輪查得】 | DigiKey 單價 |
|---|---|---|---|
| `BOS1901` | 單通道，第一代 | 190 Vpp；SPI；**已不建議新設計** | 停售中 |
| `BOS1921CQR` / `CWR` | 單通道，帶進階感測（觸覺） | 190 Vpp，3–5.5 V | **USD 4.16 / 5.71**【未驗證】 |
| `BOS1931CWR` | 單通道（**微泵／散熱**） | 190 Vpp；MIPI I3C（相容 I²C）；內建波形合成器＋2 KB RAM；SYNC 腳可讓多顆在 **2 µs** 內同步動作；啟動 < 300 µs「以動態反應熱尖峰」 | **USD 5.12**【未驗證】 |
| `BOS0614CWR` | **四通道**，整合感測 | 可驅動 4 顆 **60 V** 致動器；**零功耗感測（ZPS）可取代機械按鍵**；10 kSPS 感測介面；4 個 GPIO 低延遲觸發；I3C；2 kB RAM；觸控取樣至 10 kHz、延遲 < 100 µs | **USD 3.71**【未驗證】 |
| `BOS1211AQR` | **車規**，搭 TDK PowerHap | **12 V 供電輸出 120 V**；整合 low-side / high-side NMOS 閘驅做 buck-boost；整合壓電感測 | 【查無】 |

**開發套件**：`BOS1211` Premium Development Kit **USD 1,047.39**、`BOS0614-KIT-B03` **USD 304.03**、`BOS1901-KIT-B02` USD 180(1) → 118.10(1k)（已 obsolete）【皆未驗證】（來源 34、29、3）。

**台灣路徑已確認**：**益登科技（EDOM）同時代理 Boréas BOS1901 與 xMEMS XMC-2400**（來源 38、45）。取樣與 FAE 支援在台灣是通的。

**Boréas 也賣現成的機構件**：`EXT-BT-1204 Haptic Round Button`（Mouser 有頁），內含 TDK PowerHap 1204——**這說明「壓電按鍵」已經是可以整包買現貨做 PoC 的成熟度**（來源 37）。

### 2.3 xMEMS：本盤點中「新能力」訊號最強的一家

| 產品 | 定位 | 規格【本輪查得】 | 狀態／價格 |
|---|---|---|---|
| **Cypress** ＋ **Alta-S** 驅動 ASIC | 全音域 MEMS 喇叭（sound-from-ultrasound） | 業界首款可滿足 ANC TWS 音壓需求的全固態音訊方案 | 2025-09 宣布量產就緒、立即送樣，**客戶量產出貨預計 2026 年**；價格【查無】 |
| **Montara** / **Cowell** | 第一／第二代 | DigiTimes 專訪提到「搭 Montara 的藍牙耳機平均 US$1,500」「Cowell … 價格 US$120」——**這兩個數字讀起來是終端耳機售價而非晶片價，語意有歧義，不可當成元件價引用**【未驗證】 | Cowell 已在 TWS 市場有斬獲 |
| **Sycamore** | 1 mm 薄近場全音域微喇叭（智慧錶／XR 眼鏡／開放式耳機） | **8.41 × 9 × 1.13 mm、150 mg**；體積為傳統動圈的 **1/7**、厚度 **1/3** | 2024-11 發表；CES 2025 首次公開展示；CES 2026 續展；價格【查無】 |
| **Skyline DynamicVent** | 全固態 MEMS 閥（主動環境音控制） | **5.0 × 4.0 × 1.15 mm LGA**；搭 **Alpine DynamicVent 驅動 IC**（單／雙通道，**1.5 × 1.8 × 0.6 mm WLCSP**） | 2023-01 發表；價格【查無】 |
| **XMC-2400 µCooling** | 「晶片上的風扇」 | **9.26 × 7.6 × 1.08 mm、< 150 mg**；比非矽主動散熱**小輕 96%**；**39 cc/s** 氣流、**1,000 Pa** 背壓、**~30 mW**；超音波驅動故無聲；**IP58**；兩種封裝：`XMC-2400-S` 側出風（可與 AP 疊構）／`XMC-2400` 頂出風 | 2025 Q1 送樣；CES 2025 創新獎；**EDOM 代理**；價格【查無】 |

**xMEMS 沒有任何一顆產品有公開單價**——這是評估其成本可行性的最大盲點。

### 2.4 微泵與微流體：價格已經落地

- **Bartels `mp6`**：DigiKey Marketplace **≈ USD 65.65–67／顆、MOQ 10**；現貨 960、在途 1,360（2026-04-25）、預估備貨 10,000、前置期 12 週【未驗證】。壽命 > 5,000 h【前版轉引】。
- **Lee Ventus（原 TTP Ventus，已被 The Lee Company 併購）Disc Pump**：五條產品線 **LT / BL / HP / XP / US**。**LT 系列連續運轉超過 17,000 小時（≈ 連續兩年）才開始出現性能衰退，累計超過 1 兆次循環**（BusinessWire 2022-10-31）；規格 **270 mbar(g) 壓力／−220 mbar(g) 真空／1.2 L/min 自由流量**。**價格【查無】**（Lee 全系列均需詢價）。（來源 69、70、71）
- **Murata microblower `MZB1001T02`**：**20.0 × 20.0 × 1.85 mm**；操作 **10–20 Vpp**（絕對最大 30 Vpp）；**24–27 kHz**；流量 **0.7 L/min**、最大靜壓 **1,500 Pa @15 Vpp**（另一摘要寫 1.9 kPa，**矛盾**）、耗電 **0.18 W**；0–70 °C。**價格【查無】，且供貨訊號不佳**：Walmart 頁面顯示「Price when purchased online: Not Available」，TTI 顯示補貨前置期 **14 週**。（來源 63、64、65）

> **1 兆次循環（Lee Ventus）是本盤點中最強的壓電可靠度數字**，可直接反駁「壓電陶瓷疲勞壽命不夠」的通論——但它是在超音波共振、微位移工作點下取得的，不能外推到大位移致動器。

### 2.5 壓電變壓器（PT）供應鏈與馬達：仍然是資訊黑洞

- **PT 供應商**：Metoree 的 2025 年排名列出 **Steminc、Analog Devices、TAMURA**（「Analog Devices」出現在壓電變壓器製造商榜上高度可疑，很可能是該站分類雜訊，**不採信**）。**TAMURA 官網目前仍有活躍的壓電變壓器產品頁**（`tamuracorp.com/global/products/piezo-ceramics/piezo-transformer/`）——這是本輪唯一確認的、日系大廠仍在賣 PT 的證據。**CTS**（含 Noliac）有多層壓電產品線；**Micromechatronics（mmech.com）有「Piezoelectric Transformers and DC-DC Piezo Converters」頁面**。**所有 PT 價格【查無】。**（來源 88、89、90、91）
- **台灣 ELECERAM TECHNOLOGY 是否仍生產多層 PT** →【本輪未查】（額度耗盡），**仍是對客戶最關鍵的在地線索，下一輪務必優先。**
- **壓電馬達價格**：`PiezoMotor Piezo LEGS LL06`（6.5 N、**16 g**、直驅無背隙、可次奈米微步）、`LT20`／`LT40` 雙腿型，線性系列涵蓋 6.5–40 N——**官方價格全部不公開，只有 eBay 二手機標價**。**Xeryon 唯一公開的價格資訊是「每增加一軸 +EUR 300，最多 6 軸」**。PI、Nanomotion 價格【查無】。（來源 85、86、87）

---

## 3. 關鍵數字表

> 排序：由便宜到貴。這張表本身就是本份 dossier 的主要結論。

| # | 項目 | 價格 / 數值 | 年份/狀態 | 可信度 | 來源 |
|---|---|---|---|---|---|
| 1 | **非壓電**針尖式負離子模組（OEM，中國） | **USD 0.80／顆 @1,000+** | 現行 | 低【未驗證】 | 81 |
| 2 | **Murata CERALOCK 陶瓷諧振器**（`CSTNE8M00G550000R0`）30,000+ | **USD 0.233／顆** | 現行 | 中【未驗證】 | 61 |
| 3 | 同上，3,000 顆整卷 USD 735 | **USD 0.245／顆** | 現行 | 中【未驗證】 | 61 |
| 4 | Murata 陶瓷諧振器（RS Online，1,500+） | **USD 0.374／顆** | 現行 | 中 | 60 |
| 5 | **Boréas `BOS0614CWR`**（4 通道＋感測） | **USD 3.71** | 現行 | 中【未驗證】 | 28 |
| 6 | **Boréas `BOS1921CQR`** | **USD 4.16** | 現行 | 中【未驗證】 | 27 |
| 7 | **Boréas `BOS1931CWR`**（微泵版） | **USD 5.12** | 現行 | 中【未驗證】 | 30 |
| 8 | **Boréas `BOS1921CWR`**（WFBGA） | **USD 5.71** | 現行 | 中【未驗證】 | 26 |
| 9 | **Bartels `mp6` 壓電微泵**（MOQ 10） | **USD ~65.65–67** | 現行 | 中【未驗證】 | 66、67 |
| 10 | **TDK PiezoListen `PHUA3030-049B-00-000`** | **DigiKey USD 93.83／Mouser USD 93.42**（9 家 78.24–93.42） | 現行 | 中【未驗證】 | 54、55、56 |
| 11 | **TDK CeraPlas HF 樣品 `Z63000Z2910Z1Z60`** | **≈ USD 142.25** | 現行 | 低【未驗證】 | 2 |
| 12 | **Boréas `BOS0614-KIT-B03`** 評估板 | **USD 304.03** | 現行 | 中【未驗證】 | 29 |
| 13 | **XP Power `Q101-5`**（10 kV／50 µA／0.5 W，完整穩壓模組） | **USD 365.27**（Worldictown，庫存 2,019）／**USD 420.06**（DigiKey，前版轉引） | 現行 | 中 | 75、74 |
| 14 | **CeraPlas Evaluation Kit V2 `…01Z69`** | **USD 653.40(1) → 428.70(1k)** | 現行 | 低【未驗證，中間商】 | 3 |
| 15 | **Boréas `BOS1211` Premium Dev Kit** | **USD 1,047.39** | 現行 | 中【未驗證】 | 34 |
| 16 | **relyon piezobrush PZ3 Professional Set** | **EUR 2,540.00** | 現行 | **高（官方商店）** | 15、16 |
| 17 | 同上，美國牙科通路 | **USD 3,789.00** | 現行 | 中 | 17 |
| 18 | **STEMINC 單層 PT `SMSTF50P2S6`**（2 W 級） | USD 23.76／2 顆 ≈ 11.88／顆 | 現行 | 中【前版轉引，本輪未重驗】 | — |

**非價格關鍵規格**

| 項目 | 數值 | 來源 |
|---|---|---|
| Boréas CapDrive 輸出 | **190 Vpp，供電 3–5.5 V，7 顆被動元件，啟動 < 300 µs** | 25、35 |
| BOS1211 車規輸出 | **12 V → 120 V**，整合 HS/LS NMOS 閘驅＋壓電感測 | 33 |
| BOS0614 感測 | 4×60 V；**零功耗感測 ZPS**；10 kSPS；觸控 10 kHz、延遲 < 100 µs | 36 |
| xMEMS XMC-2400 | 9.26×7.6×1.08 mm、**<150 mg**、**39 cc/s**、**1,000 Pa**、**~30 mW**、IP58、超音波無聲 | 44、46 |
| xMEMS Sycamore | 8.41×9×1.13 mm、150 mg、體積 1/7、厚度 1/3 | 49 |
| xMEMS Skyline / Alpine | 5.0×4.0×1.15 mm LGA / 1.5×1.8×0.6 mm WLCSP | 48 |
| TDK PowerHap `1204H018V060` | 12×4×1.8 mm；60 V 下驅動 100 g 質量達 **5 g(pk)**、位移 **27 µm**；每次回饋 **0.35 或 0.6 mJ**；響應 **< 1 ms**；具感測功能 | 51、52 |
| PowerHap 按鍵組（`EXT-BT-1204` 系統值） | 0–95 V、35 µm、4.5 g、共振 175 Hz、按鍵直徑 40 mm、動質量 15 g、最大壓縮力 80 N、機械放大 2:1 | 51 |
| TDK PiezoListen | 400 Hz–20 kHz、**≤24 Vpp 出 80 dB**、厚 **0.49 mm**、最大 34 W、阻抗 2–100 Ω；型號 PHUA2010/3015/3030/6630 | 57、58 |
| Murata `MZB1001T02` | 20×20×1.85 mm、10–20 Vpp、24–27 kHz、0.7 L/min、1,500 Pa、0.18 W | 63、64 |
| Lee Ventus LT 系列 | **> 17,000 h 連續運轉、> 1 兆次循環**；270 mbar(g)／−220 mbar(g)／1.2 L/min | 69、70、71 |
| Coilcraft `HTX7045C` | **繞組間電容低至 0.7 pF；隔離 2800 Vrms / 4000 VDC 1 min**（**非 12 kV**） | 79、80 |
| piezobrush PZ3 | 最大 18 W、< 50 °C、5 種模組 | 24 |
| CeraPlas（TDK 技術文章版） | **12 Vpp / 52 kHz / 輸出「several kV」** ← 與 datasheet 的 <15 kV、featured story 的 20 kV **三者互相矛盾** | 6 |

---

## 4. 「新能力型」應用機會

> 判定標準：**是** = 以前物理上做不到；**半** = 以前能做但形態改變、開出新場景；**否** = 純粹更小更便宜的替代（依客戶方向限制應降權）。

### 4.1 無聲、無旋轉件、可疊在晶片上的固態氣流源（xMEMS µCooling 路線）

- **新能力**：把「產生 39 cc/s 氣流 ＋ 1,000 Pa 背壓」壓縮進 **1.08 mm 厚、150 mg、30 mW**、且因為工作在超音波頻段而**完全無噪音**、IP58 防塵防水、可與應用處理器**疊構**的固態元件。
- **為什麼以前做不到**：軸流／離心風扇有軸承、有可聽噪音、厚度下不到 3 mm、進灰即死；熱管與均熱片是被動的，無法在偵測到熱尖峰後 **300 µs 內**主動加大氣流。壓電是唯一能同時滿足「薄到 1 mm、無移動軸承、無聽感噪音、mW 級耗電」的致動原理。
- **是否真非替代**：**是**。這不是把風扇做小，是在風扇物理上不存在的尺寸／噪音象限開新格。
- **誰在做**：xMEMS（XMC-2400，2025 Q1 送樣，CES 2025 創新獎，**EDOM 台灣代理**）；Boréas 已開「微泵液冷」應用線並推出 `BOS1931` 專用驅動 IC（USD 5.12），**驅動側的現貨問題已經解掉**。
- **TRL**：**7–8**（送樣中，尚未見量產機種公告）。
- **市場訊號**：AI PC／AI 穿戴的散熱瓶頸是真需求；CES 2026 xMEMS 仍以 µCooling ＋ Sycamore 主打 AI 穿戴。
- **最大技術障礙**：(1) **公開單價完全查無**，若落在 USD 10+ 則對 NB/手機 BOM 是硬傷；(2) 39 cc/s 對筆電 SoC 級熱源仍偏小，需陣列化，陣列則要處理相位同步（`BOS1931` 的 SYNC 腳 2 µs 同步正是為此而設）與**進氣路徑積塵**。

### 4.2 「零功耗感測 ＋ 主動回饋」的固態按鍵陣列（BOS0614 路線）

- **新能力**：同一片壓電，**待機時作為零功耗（ZPS）力量感測器**，被按下時**同一片**立刻輸出 60 V 觸覺回饋；四通道、10 kHz 取樣、< 100 µs 延遲，一顆 **USD 3.71** 的 IC 取代「機械開關 ＋ 力感測器 ＋ LRA ＋ 驅動器」四件套。
- **為什麼以前做不到**：電容式觸控要持續耗電掃描；機械開關無法感測力道且會磨損進水；LRA 有質量塊與 ms 級啟動延遲。**「不通電也能被按醒」＋「同一顆立刻回打」以前必須是兩顆不同元件。**
- **是否真非替代**：**半**。功能上是替代（省一顆感測器 ＋ 省電），但 ZPS 讓「整機深度睡眠時仍可被實體按鍵喚醒且零靜態電流」成為可能，這在 IP68 全密封／無開孔工業設備上是新形態。
- **誰在做**：Boréas（`BOS0614` 四通道、`BOS1921` 單通道、`BOS1211` 車規 120 V）；元件側 TDK PowerHap；**Boréas 直接賣現成的 `EXT-BT-1204` 圓形觸覺按鍵**，PoC 可以直接買整包。**EDOM 台灣代理。**
- **TRL**：**9**。
- **最大技術障礙**：**這條路已被 Boréas 佔位且價格壓到 USD 3.71**，自研 IC 幾乎沒有成本空間；CapDrive 的能量回收專利範圍未知（前版已列為未解問題，本輪額度不足未查）。**依客戶方向限制，建議定位為「用它，不是做它」。**

### 4.3 可拋棄／可耗材化的 kV 級冷電漿頭

- **新能力**：升壓段本身就是一片幾克重的陶瓷，主機端只剩 24 V 低壓線。第一次讓「把高壓源做成一次性無菌耗材」在成本與安規上可談。
- **為什麼以前做不到**：傳統高壓源是整機最貴、最重、最需安規認證的部分（見 4.4 的 Q101-5 對照），不可能拋棄；高壓連接器插拔本身就是失效與漏電風險點。
- **是否真非替代**：**是**（系統拓樸改變，不是元件縮小）。
- **誰在做**：**查無公開商品化案例**。最接近的骨架是 TDK CeraPlas ExploreKit 與已在牙科通路銷售的 PZ3。
- **TRL**：3–4。
- **最大技術障礙**：**CeraPlas 樣品單價 ≈ USD 142（未驗證），對「耗材」而言貴了 1–2 個數量級**；且壽命／連續放電時數【查無】，沒有壽命數字就無法把「短壽命」轉化成「一次性」的賣點。

### 4.4 低功率 kV 級電場源的成本重構（**本輪已大幅降級**）

- **前版主張**：STEMINC PT USD 11.88 vs XP Power Q101-5 USD 420 → 「量級差 35 倍，壓電壓倒性優勢」。
- **本輪更正**：真正對等的比較是 **CeraPlas HF USD 142（裸元件，需外掛驅動）vs Q101-5 USD 365–420（完整穩壓模組）**，**差距只有 2.6–2.9 倍**，而且加上驅動級 BOM 與研發成本後可能歸零。**在低階市場另一頭，非壓電負離子模組只要 USD 0.80。壓電被夾在中間。**
- **是否真非替代**：**否到半**。降級為「條件性機會」：只有在**同時**需要 kV 電場 ＋ 極薄／極輕 ＋ 無電磁干擾 ＋ 可直接當電極（省掉高壓走線）的場合，壓電才有結構性優勢；純粹「產生高壓」不是。
- **TRL**：8–9（元件可買）。
- **最大技術障礙**：**價格論證已被本輪自己的資料推翻，請客戶不要再用「便宜 35 倍」這個說法。**

### 4.5 機器人末端的點狀選擇性表面活化（既有生意，可對標但難插入）

- **新能力**：< 18 W、< 50 °C、寬 5–29 mm 的電漿源直接裝在機械手臂上，只活化要塗膠的那條膠道。
- **是否真非替代**：**半**。
- **誰在做**：relyon PZ3-i（已上架 igus rbtx；Intertronics、Ulbrich 為通路）。**TRL 9，但價格 EUR 2,540 級、且母公司正在被出售（見第 5 節）。**
- **最大技術障礙**：處理速率只有數 cm²/s（前版轉引），一要整片就輸給電暈；**這是既有玩家的生意，客戶要進入只能做元件供應或做出更便宜的整機。**

### 4.6 明確標為「替代品」、應排除的方向

- **用 PT 做隔離閘極驅動**：本輪確認 Coilcraft `HTX7045C` 已做到 **0.7 pF 繞組間電容 ＋ 2800 Vrms 隔離**，且是為 SiC/GaN 開迴路 LLC 專門設計的量產件。壓電在此既無性能跨越、單價又高、頻寬先天不足。**排除，理由與客戶排除「取代電感」同構。**
- **取代針尖式離子產生器**：對手 **USD 0.80**。**排除。**
- **取代動圈微喇叭**：PiezoListen 一顆 **USD 93**。**排除。**

---

## 5. 反面證據、失敗案例與物理上限

1. **【本輪最重要的自我否定】前版的核心價格論證是錯的。** 「壓電高壓源比傳統模組便宜 35 倍」建立在拿 USD 11.88 的裸 PT 比 USD 420 的完整模組。本輪查到 CeraPlas HF 樣品約 **USD 142**，對比 Q101-5 的 **USD 365–420**，優勢縮到 2.6–2.9 倍，而且**壓電那一邊還要自己做驅動級**。任何以「壓電便宜」為前提的商業計畫都必須重算。
2. **壓電產品的定價邏輯是「系統」不是「元件」。** 觀察本輪整條價格階梯：陶瓷本體 USD 0.23 → 驅動 IC USD 3.7–5.7 → 微泵 USD 66 → 喇叭 USD 93 → 電漿元件 USD 142 → 高壓模組 USD 365 → 整機 EUR 2,540。**中間差了四個數量級，而差距不在材料，在量與整合。** 換句話說：**壓電兩用元件的成本問題本質是「沒有量」，不是「物理上貴」。** 這對客戶是雙面刃——有機會，但需要先找到能吃量的應用。
3. **relyon 需要提供「租借機」。** relyon 官方商店同時上架 `piezobrush PZ3 Professional Set`（EUR 2,540）與 `Leihgerät PiezoBrush PZ3`（租借）。**一個成熟產品需要租借方案，通常代表購買轉換率不佳。**
4. **TDK 八年後退場。** 2018 年 EPCOS 取得 relyon 50.2% 股權；2026-03-04 Viromed Medical AG 簽 LOI 收購、2026-07-27 完成盡職調查，對價「低至中雙位數百萬歐元」【前版轉引，本輪未重驗】。以 EUR 2,540 的單價回推，這個對價對應的年出貨量級極小。**合理解讀：CeraPlas 八年沒有找到任何一個能吃掉百萬顆／年的應用。**
5. **壓電喇叭的價格反證。** TDK PiezoListen 30×30 mm 一顆 **USD 93**，九家通路最低也要 USD 78。相對傳統動圈微喇叭（< USD 1），這是「壓電做被動聲學元件」在消費電子完全沒有成本立足點的直接證據。（xMEMS 走的是完全不同的 MEMS 矽製程路線，成本結構不同，但同樣**沒有公開單價**。）
6. **離子產生市場已被 USD 0.80 封死。** 非壓電負離子模組 −9 kV、< 1 W、OEM USD 0.80／顆 @1k。**任何「用壓電做便宜高壓源」的論證，在這個市場自動失效。**
7. **Murata microblower 的供貨訊號不佳。** `MZB1001T02` 在 Walmart 顯示無法線上購買、TTI 顯示補貨前置期 14 週。**這是一顆 2014 年就有 datasheet 的老產品，十二年後仍是這個供貨狀態，說明壓電微氣泵在消費市場並沒有跑出量。**
8. **BOS1901 的世代更替說明產品線在收斂而非擴張**：第一代已不建議新設計，並被拆成觸覺（1921）與微泵（1931）兩條——**Boréas 把資源從「觸覺」分了一半到「散熱／流體」，本身就是「觸覺市場不夠大」的訊號。**
9. **CeraPlas 的規格三方矛盾未解**：TDK 自家技術文章寫 12 Vpp / 52 kHz / 「several kV」，datasheet 系來源寫 < 15 kV / 8 W，另一篇 TDK featured story 寫最高 20 kV。**一個上市八年的產品，官方文獻對輸出電壓給不出一致數字，這件事本身就值得警惕。**
10. **前版引用的 Coilcraft「12 kV」為錯誤資訊**，本輪確認官方頁面為 2800 Vrms / 4000 VDC。**請下游文件一併更正。**
11. **物理上限（沿用前版，本輪未重驗）**：單顆 CeraPlas F 最大 8 W、PZ3 整機 18 W；Rosen 型 PT 受機械應力極限與自發熱／Q 值下降雙重限制；陣列化受 4 cm 最小間距（寄生耦合）限制，面功率密度約 0.5 W/cm² 量級。**靠單顆或陣列放大功率在物理上是死路。**
12. **穿金屬壁供電近 30 年零商品化**【前版轉引，本輪未重驗】：實驗室已達 63.5 mm 鋼上 50 W ＋ 12.4 Mb/s，但 2026 年仍查無任何具名商用產品或 ATEX/IECEx 方案。
13. **業界最嚴苛應用否決自感測**【前版轉引】：Physik Instrumente 高階奈米定位仍用外部電容式 direct metrology。**若客戶賣點是「省掉感測器」，這個案例必須先被回答。**（不過本輪的 BOS0614 ZPS 與 PowerHap 的感測功能顯示，在**低精度、大訊號**的按鍵／泵浦場景，自感測已經商品化——差別在精度等級。）

---

## 6. 未解問題

1. **【最高優先，且本輪已證實有效】直接向通路詢價，不要靠搜尋。** 本輪證明 DigiKey／Mouser／官方商店的價格是查得到的（Boréas、PiezoListen、piezobrush 都查到了），查不到的只有 TDK CeraPlas 與 xMEMS。應直接發詢價信：
   - **TDK Electronics / Mouser / DigiKey**：`Z63000Z2910Z1Z60`（CeraPlas HF）與 CeraPlas F 的 **1k / 10k / 100k 階梯價**，並索取 reliability report（連續放電時數、輸出電壓衰退曲線、MTBF）。**同時確認 CeraPlas 是否已 EOL——這是本輪未查完的關鍵風險。**
   - **xMEMS / 益登科技（EDOM）**：`XMC-2400` 的量產階梯價與最小起訂量。**EDOM 同時代理 Boréas 與 xMEMS，是台灣客戶一次問到兩條線的最短路徑。**
   - **TAMURA**：壓電變壓器量產單價與最小起訂量（本輪確認其產品頁仍在線）。
   - **ELECERAM TECHNOLOGY（台灣）**：是否仍生產多層 PT、pilot 產能、良率與單價區間。**本輪額度不足未查，仍是台灣在地 PoC 的關鍵。**
   - **The Lee Company（Lee Ventus）**：LT/HP/XP 系列價格（唯一有 1 兆次循環背書的壓電泵）。
2. **CeraPlas 輸出電壓的三方矛盾（several kV / < 15 kV / 20 kV）必須以原始 datasheet 定案。** 本輪反而讓矛盾從兩方變成三方。
3. **對照組完全缺席**：同等級功率電感、磁性變壓器的實際階梯價本輪完全未查（額度耗盡）。**沒有這組數字，「壓電 vs 磁性」的成本比較無法收斂。** 下一輪應查 Coilcraft/Würth/TDK 的 10 µH/3 A 級電感在 1k/10k 的單價，以及 `HTX7045C` 的實際報價。
4. **Boréas CapDrive 的專利範圍**：若「從致動器負載電容回收能量」已被圈死，客戶自研驅動 IC 會直接撞牆。本輪額度不足未查，**建議以 Boréas Technologies 為受讓人做專利檢索**。
5. **xMEMS 的製程與成本結構**：xMEMS 走的是矽 MEMS 壓電薄膜（非塊材 PZT），成本曲線與 TDK/Murata 的陶瓷路線完全不同。**客戶若要投入，必須先決定站在「塊材陶瓷」還是「薄膜 MEMS」這一邊——這是兩個不同的產業。** 本輪資料不足以判斷。
6. **Viromed × relyon 交易是否完成交割**、Viromed 要推哪條醫材適應症【本輪未查】。**這是未來 12 個月最能證實／證偽本領域的單一事件。**

---

## 7. 來源清單

> 標註規則：`【本輪】` = 本輪 WebSearch 摘要直接回傳；`【聚合】` = 報價聚合／中間商網站，價格可信度低。所有 URL 均未經 WebFetch 開啟驗證（環境限制）。

### 7.1 TDK CeraPlas（元件層）

1. DigiKey — `Z63000Z2910Z01Z69`（CeraPlas Evaluation Kit V2，歸類 Development Boards/Kits）。【本輪】 https://www.digikey.com/en/products/detail/epcos-tdk-electronics/Z63000Z2910Z01Z69/13174397
2. DigiKey (BG) — `Z63000Z2910Z1Z60`（CeraPlas HF 樣品，DK# 495-77395-ND）。**摘要報 USD 142.25**。【本輪／未驗證】 https://digikey.bg/product-detail/en/epcos-tdk/Z63000Z2910Z1Z60/495-77395-ND/9698000
3. Quarktwin — `Z63000Z2910Z01Z69` CeraPlas Evaluation Kit V2 階梯價 **653.40 / 588.06 / 529.25 / 476.33 / 428.70**。【聚合／未驗證】 https://www.quarktwin.com/product-detail/epcos---tdk-electronics-z63000z2910z01z69/7200374
4. micro-processor.pl — 托管 `e0-z63000z2910z1z60.pdf`「CeraPlas Element Piezoelectric Based Cold Plasma Generator」datasheet。【本輪】 https://www.micro-processor.pl/parts-file/e0-z63000z2910z1z60.pdf
5. epcos.zeano-de.com — `Z63000Z2910Z1Z61` CERAPLAS HF DEVELOPMENT KIT。【本輪，價格未回傳】 https://epcos.zeano-de.com/product/Z63000Z2910Z1Z61/03906789
6. TDK Electronics tech-library —「Cold plasma from a single component」。**12 Vpp / 52 kHz / 輸出 several kV；硬 PZT 共燒銅內電極**。【本輪】 http://en.tdk.eu/tdk-en/373562/tech-library/articles/applications---cases/applications---cases/cold-plasma-from-a-single-component/1109546
7. Mouser (IN) — CeraPlas HF Piezoelectric Plasma Generator 產品頁。【本輪，價格未回傳】 https://www.mouser.in/new/epcos/epcos-ceraplas-hf/
8. relyon plasma — CeraPlas HF plasma generator from EPCOS/TDK。【本輪】 https://www.relyon-plasma.com/plasma-technology/ceraplas-en/?lang=en
9. TDK — CeraPlas ExploreKit for decontamination。【本輪】 https://www.tdk-electronics.tdk.com/en/2910748/products/product-catalog/cold-plasma-technology/ceraplas-explorekit
10. DigiKey — Compact CeraPlas for Cold Plasma Tech（product highlight）。【本輪】 https://www.digikey.com/en/product-highlight/e/epcos/compact-ceraplas-for-cold-plasma-technology
11. GlobeNewswire — TDK Introduces CeraPlas HF（2018-11-13 上市）。【本輪】 https://www.globenewswire.com/news-release/2018/11/13/1650541/0/en/TDK-Introduces-CeraPlas-HF-Compact-Cold-Plasma-Generator-Element.html
12. TDK 新聞稿 — Compact CeraPlas HF element for cold plasma。訂購碼 `Z63000Z2910Z 1Z60`（樣品）、`1Z61`（含控制電子的套件）。【本輪】 https://www.tdk-electronics.tdk.com/en/373388/company/press-center/press-releases/press-releases/plasma-generators-compact-ceraplas-hf-element-for-cold-plasma/2435688
13. Sekorm — `Z63000Z2910Z 1Z68` F series packaged component 初步資料。【本輪】 https://en.sekorm.com/doc/2581106.html
14. Texim Europe — Cold atmospheric pressure plasma（通路商技術文件 PDF）。【本輪】 https://www.texim-europe.com/getfile.ashx?id=113097

### 7.2 relyon plasma（系統層）與通路

15. relyon plasma 官方商店 — piezobrush PZ3 Professional Set。**EUR 2,540.00**；內含主機＋Standard 模組＋Nearfield 模組。【本輪，可信度高】 https://www.relyon-plasma.com/produkt/piezobrush-pz3-professional-set/
16. AERA-Online — PiezoBrush PZ3 Professional Set 價格比較頁。【本輪】 https://www.aera-online.de/Asps/Artikel.asp?gArtikelID=1212191
17. Chairside Solutions（美國牙科通路）— piezobrush PZ3 Professional Set **USD 3,789.00**。【本輪】 https://www.chairsidesolutions.com/shop/p/relyonplasmapiezobrush
18. relyon plasma — **Leihgerät（租借機）PiezoBrush PZ3**。【本輪，商業訊號】 https://www.relyon-plasma.com/produkt/leihgeraet-piezobrush-pz3/
19. Intertronics（UK）— PiezoBrush PZ3-i（半自動／自動化整合版）。【本輪，價格未公開】 https://www.intertronics.co.uk/product/piezobrush-pz3-i-plasma-surface-treatment-for-semi-automated-or-automated-use/
20. Intertronics Shop — PiezoBrush PZ3 手持機。【本輪，價格未回傳】 https://intertronics.shop/product/piezobrush-pz3-handheld-plasma-surface-treatment/
21. igus rbtx — piezobrush PZ3-i 作為機器人末端執行器上架。【本輪】 https://rbtx.com/en-US/components/end-effectors/cold-plasma-device-improved-adhesion-ink-glue-relyon-plasma-piezobrush-pz3-i
22. TDK Electronics 托管 — piezobrush PZ3 Operating Instructions（PDF）。【本輪】 https://www.tdk-electronics.tdk.com/inf/130/Cold_Plasma/Operating_Instructions.pdf
23. Ulbrich Group — PIEZOBRUSH PZ3i 通路頁。【本輪】 https://www.ulbrich-group.com/piezobrush-pz3i
24. relyon plasma — piezobrush PZ3 產品頁（18 W、< 50 °C、五模組）。【本輪】 https://www.relyon-plasma.com/piezobrush-pz3/?lang=en

### 7.3 Boréas Technologies（驅動 IC）

25. Boréas — CapDrive Ultra-Low Power Piezo Driver (BOS1901)。**190 Vpp / 3–5.5 V / 7 顆被動元件 / 啟動 < 300 µs；已不建議新設計，改用 BOS1921（觸覺）與 BOS1931（微泵）**。【本輪】 https://www.boreas.ca/products/bos1901-piezo-haptic-driver
26. DigiKey — `BOS1921CWR`（20-WFBGA）**USD 5.71**。【本輪／未驗證】 https://www.digikey.com/en/products/detail/boreas-technologies/BOS1921CWR/21704163
27. Mouser — `BOS1921CQR`（24-VFQFN）**USD 4.16**（DigiKey 報價）。【本輪／未驗證】 https://www.mouser.com/ProductDetail/Boreas-Technologies/BOS1921CQR
28. DigiKey — `BOS0614CWR` **USD 3.71**。【本輪／未驗證】 https://www.digikey.com/en/products/detail/boreas-technologies/BOS0614CWR/25319328
29. DigiKey — `BOS0614-KIT-B03` **USD 304.03**。【本輪／未驗證】 https://www.digikey.com/en/products/detail/boreas-technologies/BOS0614-KIT-B03/25319334
30. Mouser — `BOS1931CWR`（DigiKey 報 **USD 5.12**）。【本輪／未驗證】 https://www.mouser.com/ProductDetail/Boreas-Technologies/BOS1931CWR
31. Boréas — CapDrive Ultra-Low Power Piezo Driver (BOS1931)。190 Vpp、MIPI I3C、2 KB RAM、SYNC 2 µs。【本輪】 https://www.boreas.ca/products/capdrive%C2%AE-ultra-low-power-piezo-driver-bos1931
32. Boréas — **Micropump Liquid Cooling Application** 頁。**產品線從觸覺擴向散熱／流體的證據**。【本輪】 https://www.boreas.ca/pages/micropump-liquid-cooling
33. Boréas — CapDrive Powerful Piezo Driver for Automotive (BOS1211)。**12 V → 120 V**，驅動 TDK PowerHap 120 V 致動器；整合 HS/LS NMOS 閘驅 ＋ 壓電感測。【本輪】 https://www.boreas.ca/products/bos1211-piezo-haptic-driver
34. DigiKey — BOS1211 Starter Development Kit（Premium Dev Kit **USD 1,047.39**）。【本輪／未驗證】 https://www.digikey.com/en/product-highlight/b/boreas/bos1211-starter-development-kit
35. DigiKey 托管 — BOS1921/BOS1931 Product Datasheet BT015DDS01.01 Issue 6（PDF）。【本輪】 https://mm.digikey.com/Volume0/opasdata/d220001/medias/docus/6662/2158_BOS19_Datasheet.pdf
36. DigiKey 托管 — BOS0614 Product Datasheet BT005EDS01.01 Issue 4（PDF）。ZPS、10 kSPS、< 100 µs。【本輪】 https://mm.digikey.com/Volume0/opasdata/d220001/medias/docus/6662/2158_BOS0614CWR.pdf
37. Boréas — `EXT-BT-1204` Haptic Round Button（內含 TDK PowerHap 1204，Mouser 有頁）。【本輪】 https://www.boreas.ca/products/ext-bt-1204-haptic-round-button
38. EDOM 益登科技 — BOS1901 Piezo Haptic Driver（**台灣代理**）。【本輪】 https://www.edomtech.com/en/product-detail/bos1901-piezo-haptic-driver/
39. DigiKey — `BOS1901-KIT-B`／`-B02`（B02 已 obsolete）。【本輪】 https://www.digikey.com/en/products/detail/boreas-technologies/BOS1901-KIT-B/10258692
40. Adafruit blog — EYE ON NPI: Boréas BOS1931 High-Efficiency Piezo Driver（2025-03-20，DigiKey 合作）。【本輪】 https://blog.adafruit.com/2025/03/20/eye-on-npi-boreas-technologies-bos1931-high-efficiency-piezo-driver-eyeonnpi-digikey-digikey

### 7.4 xMEMS

41. xMEMS 新聞稿 — Cypress 量產就緒（全音域 MEMS 喇叭）。【本輪】 https://xmems.com/press-release/xmems-announces-mass-production-readiness-of-cypress-the-worlds-first-full-range-mems-speaker-for-wireless-earbuds/
42. BusinessWire（2025-09-09）— 同上。**Cypress ＋ Alta-S 立即送樣，客戶量產出貨預計 2026 年**。【本輪】 https://www.businesswire.com/news/home/20250909860435/en/xMEMS-Announces-Mass-Production-Readiness-of-Cypress-The-Worlds-First-Full-Range-MEMS-Speaker-for-Wireless-Earbuds
43. DigiTimes — Q&A with xMEMS CEO Joseph Jiang。提到 Montara 耳機均價 US$1,500、Cowell US$120（**語意歧義：疑為終端售價，非晶片價**）。【本輪／未驗證】 https://www.digitimes.com/news/a20240325PD205/xmems-mems-speakers-ic.html
44. xMEMS 新聞稿 — 1mm-Thin Active Micro-Cooling "Fan on a Chip"（XMC-2400）。【本輪】 https://xmems.com/press-release/xmems-introduces-1mm-thin-active-micro-cooling-fan-on-a-chip/
45. EDOM 益登科技 — XMC-2400 µCooling Fan on a Chip（**台灣代理**）。【本輪】 https://www.edomtech.com/en/product-detail/xmc-2400-cooling-fan-on-a-chip/
46. CNX Software（2024-08-21）— XMC-2400 規格：9.26×7.6×1.08 mm、<150 mg、39 cc/s、1,000 Pa、~30 mW、IP58、兩種封裝。【本輪】 https://www.cnx-software.com/2024/08/21/xmems-xmc-2400-1mm-thin-micro-cooling-fan-on-a-chip-for-ultrathin-devices-and-ssds/
47. xMEMS — Micro Cooling (µCooling) 產品總覽。【本輪】 https://xmems.com/microcooling/
48. BusinessWire（2023-01-04）— Skyline，世界首款全固態 MEMS DynamicVent。**5.0×4.0×1.15 mm LGA ＋ Alpine 驅動 IC 1.5×1.8×0.6 mm WLCSP**。【本輪】 https://www.businesswire.com/news/home/20230104005123/en/xMEMS-Announces-Skyline-the-Worlds-First-Solid-State-MEMS-DynamicVent-Enabling-Active-Ambient-Control-for-Next-Generation-TWS-and-Hearing-Aids
49. BusinessWire（2024-11-19，經 financialcontent 轉載）— Sycamore：**8.41×9×1.13 mm、150 mg、體積 1/7、厚度 1/3**。【本輪】 https://markets.financialcontent.com/pennwell.cabling/article/bizwire-2024-11-19-xmems-introduces-sycamore-the-worlds-first-1-mm-thin-near-field-full-range-mems-micro-speaker-for-smart-watches-xr-glasses-and-goggles-open-fit-earbuds-and-other-applications
50. xMEMS — CES 2026 將展示 µCooling ＋ Sycamore（AI 穿戴）。【本輪】 https://xmems.com/press-release/xmems-to-showcase-breakthrough-%C2%B5cooling-and-sycamore-mems-loudspeaker-technologies-powering-the-next-generation-of-ai-wearables-at-ces-2026/

### 7.5 TDK PowerHap / PiezoListen

51. TDK — PowerHap `1204H018V060` datasheet（PDF）。12×4×1.8 mm；60 V 下 100 g 質量 5 g(pk)、位移 27 µm。【本輪】 https://product.tdk.com/system/files/dam/doc/product/sw_piezo/haptic/powerhap/data_sheet/20/10/ds/1204h018v060.pdf
52. TDK 新聞稿 — Mini PowerHap actuators for haptic feedback（0904H014V060 / 1204H018V060）。每次回饋 0.35 或 0.6 mJ、響應 < 1 ms、具感測功能。【本輪】 https://www.tdk-electronics.tdk.com/en/373388/company/press-center/press-releases/press-releases/piezo-actuators-mini-powerhap-actuators-for-haptic-feedback/2517752
53. DigiKey — PowerHap Development Starter Kit（product highlight）。【本輪，價格未回傳】 https://www.digikey.com/en/product-highlight/t/tdk/powerhap-development-starter-kit
54. DigiKey — PiezoListen `PHUA3030-049B-00-000` **USD 93.83**。【本輪／未驗證】 https://www.digikey.com/en/products/detail/tdk-corporation/PHUA3030-049B-00-000/10229239
55. Mouser — `PHUA3030-049B-00-000` **USD 93.42**。【本輪／未驗證】 https://www.mouser.com/ProductDetail/TDK/PHUA3030-049B-00-000
56. Octopart — `PHUA3030-049B-00-000` 九家通路報價 **USD 78.2353–93.42**。【聚合／未驗證】 https://octopart.com/phua3030-049b-00-000-tdk-102119464
57. TDK 新聞稿（2019-05-21）— PiezoListen 超薄壓電喇叭。400 Hz–20 kHz、≤24 Vpp 出 80 dB、厚 0.49 mm。【本輪】 https://www.tdk.com/en/news_center/press/20190521_01.html
58. TDK — PiezoListen 商用型錄 PHU（PDF）。最大 34 W、阻抗 2–100 Ω、PHUA2010/3015/3030/6630。【本輪】 https://product.tdk.com/system/files/dam/doc/product/sw_piezo/speaker/piezolisten/catalog/piezolisten_commercial_phu_en.pdf

### 7.6 Murata（成本地板與微氣泵）

59. DigiKey — `CSTCE16M0V53-R0`（16 MHz、內建 15 pF、±0.3%、3.2×1.3×0.9 mm）。**狀態：End of Life，Last Time Buy 2019-09-30**。【本輪】 https://www.digikey.com/en/products/detail/murata-electronics/CSTCE16M0V53-R0/584406
60. RS Online（AU）— Murata 陶瓷諧振器階梯價 **USD 0.389 (20–740) / 0.380 (760–1480) / 0.374 (1500+)**。【本輪／未驗證】 https://au.rs-online.com/web/p/ceramic-resonators/2166058
61. LCSC — Murata CERALOCK。**`CSTNE8M00G550000R0` 3,000 顆卷 USD 735 = 0.245/顆；6k–27k = 0.239；30k+ = 0.233**。**本領域成本地板錨點。**【本輪／未驗證】 https://www.lcsc.com/product-detail/Ceramic-Resonators_Murata-Electronics_CSTCE16M0V13C99-R0_Murata-Electronics-CSTCE16M0V13C99-R0_C118038.html
62. Octopart — `CSTCE20M0V53-R0` 多通路比價頁。【聚合】 https://octopart.com/part/murata/CSTCE20M0V53-R0
63. Murata — Microblower `MZB1001T02` 產品頁。20×20×1.85 mm、0.7 L/min、1,500 Pa、0.18 W。【本輪】 https://www.murata.com/en-us/products/mechatronics/fluid/overview/lineup/microblower_mzb1001t02
64. Mouser 托管 — `MZB1001T02` datasheet（2014-04）。10–20 Vpp（abs max 30 Vpp）、24–27 kHz、0–70 °C。【本輪】 https://www.mouser.com/datasheet/2/281/Murata_MZB1001T02_datasheet-1186478.pdf
65. TTI — `MZB1001T02` 零件頁。**補貨前置期 14 週**（供貨訊號）。【本輪】 https://www.tti.com/content/ttiinc/en/apps/part-detail.html?partsNumber=MZB1001T02&mfgShortname=MUR

### 7.7 壓電微泵

66. DigiKey Marketplace — Bartels Mikrotechnik `mp6 micropump`。**≈ USD 65.65–67，MOQ 10**；現貨 960、在途 1,360（2026-04-25）、前置期 12 週。【本輪／未驗證】 https://www.digikey.com/en/products/detail/bartels-mikrotechnik-gmbh/mp6-micropump/17752892
67. DistyParts — mp6 micropump（**零售 USD 67／顆**）。【本輪／未驗證】 https://distyparts.com/product/mp6-micropump
68. Darwin Microfluidics — Bartels BP7 Micropump（歐盟通路）。【本輪，價格未回傳】 https://darwin-microfluidics.com/products/bartels-bp7-micropump/
69. The Lee Company — LT Series Disc Pump。**> 17,000 h 連續運轉**；270 mbar(g) / −220 mbar(g) / 1.2 L/min。【本輪】 https://www.theleeco.com/product/lt-series-disc-pump/
70. BusinessWire（2022-10-31）— LEE Ventus Long Life Pump Exceeds **1 Trillion Cycles**。【本輪】 https://www.businesswire.com/news/home/20221031005024/en/LEE-Ventus-Long-Life-Pump-Exceeds-1-Trillion-Cycles
71. World Pumps — Lee Ventus long life disc pump exceeds 17,000 running hours。【本輪】 https://www.worldpumps.com/content/news/lee-ventus-long-life-disc-pump-exceeds-17-000-running-hours
72. The Lee Company — Disc Pumps 總覽（LT/BL/HP/XP/US 五系列）。【本輪，價格全需詢價】 https://www.theleeco.com/disc-pumps/
73. TTP Ventus / The Lee Co — TTP Ventus Acquisition 頁。【本輪】 https://www.ttpventus.com/technology

### 7.8 對照組：非壓電高壓模組、隔離變壓器、離子產生器

74. DigiKey — XP Power `Q101-5`（10 kV / 50 µA / 0.5 W，輸入 0.7–5 V）。【本輪，DigiKey 價格未回傳；前版轉引 USD 420.06】 https://www.digikey.com/en/products/detail/xp-power/Q101-5/5873625
75. Worldictown — `Q101-5` **USD 365.27**，庫存 2,019 顆。【聚合／未驗證】 https://worldictown.com/productdetail/Q101-5
76. TRC Electronics — `Q101-5` 產品頁（0.7–5 Vdc in、0–10 kVdc out、5 mA max、0.5 W、3 年保固）。【本輪】 https://www.trcelectronics.com/products/xp-power-q101-5
77. XP Power — Q Series 產品範圍頁。【本輪】 https://www.xppower.com/product/Q-Series
78. Advanced Energy（UltraVolt）— MPM Series：100–3000 VDC、最高 1.5 W、12/24 VDC 輸入；全線 0.1 W–250 W、最高 60 kV。**價格不公開。**【本輪】 https://www.advancedenergy.com/en-us/products/dc-dc-conversion-products/high-voltage-boost-(u-v)/microsize-(0-1w-to-6w-up-to-60kv)/mpm-series/
79. Coilcraft — `HTX7045C` LLC Half-Bridge Transformers（隔離閘驅偏壓電源用）。**繞組間電容低至 0.7 pF；2800 Vrms / 4000 VDC 1 min hipot**。**更正前版「12 kV」之誤。**【本輪】 https://www.coilcraft.com/en-us/products/transformers/power-transformers/power-converter-transformers/htx7045c/
80. Coilcraft — `HTX7045` Gate Drive Transformer 系列頁。【本輪】 https://www.coilcraft.com/en-us/products/transformers/power-transformers/gate-drive/htx7045/
81. Amazon — Electrodepot 12V DC Plasma Negative Ion Generator Module。**−9.0 ± 0.5 kV、< 1 W（12 V/20 mA）、≥3,200 萬 ions/cm³**；OEM 端（Yueqing Yilerck）**USD 0.80/顆 @1,000+**。【本輪／未驗證】 https://www.amazon.com/Variable-Density-Plasma-Negative-Generator/dp/B079YZYY11
82. ContactorDepot — Shopcorp 12VDC Variable Density Plasma Negative Ion Generator Module。【本輪】 https://contactordepot.com/products/variable-density-plasma-negative-ion-generator-12vdc-module-portable-air-ionizer
83. KEYENCE — 靜電消除器選型（價格）頁。**未能確認 KEYENCE 現售型號是否採用壓電變壓器。**【本輪／查無】 https://www.keyence.com/ss/products/static/static-casestudy/price/
84. Industrial Controls — SMC `IZS31-1500CP` 離子棒（1500 mm、PNP 輸出、矽電極針）。**是否為壓電式未證實。**【本輪／查無】 https://www.indctl.com/products/smc/izs311500cp/389943

### 7.9 壓電馬達與 PT 供應商

85. PiezoMotor — Piezo LEGS Linear `LL06`（6.5 N、16 g、直驅無背隙、次奈米微步）。**價格不公開。**【本輪】 https://piezomotor.com/linear-direct-drive-piezo-actuators/legs-linear-ll06-piezo-motor/
86. Xeryon — XRT 超音波旋轉平台。**唯一公開價格資訊：每增加一軸 +EUR 300，最多 6 軸。**【本輪】 https://xeryon.com/products/precision-rotation-stages/xrt-ultrasonic-rotation-stage/
87. PI (Physik Instrumente) — Piezo Motors / Stages / Actuators 總覽。**價格不公開。**【本輪】 https://www.pi-usa.us/en/products/piezo-motors-stages-actuators
88. Metoree — 3 Piezoelectric Transformer Manufacturers in 2025（Steminc / Analog Devices / TAMURA）。**「Analog Devices」高度可疑，判定為分類雜訊，不採信。**【本輪／未驗證】 https://us.metoree.com/categories/3997/
89. TAMURA — Piezoelectric Transformers 產品頁（**日系大廠仍在售 PT 的證據**）。【本輪，價格不公開】 https://www.tamuracorp.com/global/products/piezo-ceramics/piezo-transformer/
90. Micromechatronics — Piezoelectric Transformers and DC-DC Piezo Converters。【本輪，價格不公開】 https://www.mmech.com/transformers
91. CTS Corp — Multilayer Piezoelectric（含 Noliac 產品線）。【本輪，價格不公開】 https://www.ctscorp.com/Products/Piezoelectric/Multilayer

---

*本文件由本輪 22 次 WebSearch 重建。前一版所有未標來源的斷言已被移除或重新標註。第 5.1、5.10 節為對前版的明確更正，請下游文件同步修正。*
