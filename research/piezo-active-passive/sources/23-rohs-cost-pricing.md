# 23 — RoHS 含鉛豁免時鐘與壓電元件成本錨點

> 前輪 agent 的「豁免窗口可能已關閉」是誤判：業界（RoHS Umbrella Industry Project）已於 2025-12-12 提出 7(c)-I 續期申請，7(c)-V／7(c)-VI 一併涵蓋，四項豁免的到期日目前依 RoHS 第 5(5) 條「凍結（suspended）」至執委會做出新決定為止；真正的成本結論則是——量產壓電元件的價格下限是 **US$0.10–0.27（陶瓷諧振器）**，多層高壓元件的分銷價是 **US$15–300**，兩者差距的主因是「層數 × 內電極貴金屬（Ag/Pd、Pt）」而非材料本身，因此一顆兩用元件的合理量產目標成本落在 **US$1.5–6（10 萬顆/年）**、售價 **US$5–20**。

---

## 0. 研究方法與限制（誠實揭露）

- **本輪實際執行 WebSearch 24 次**後，session 全域額度（200 次）用盡，系統拒絕後續搜尋。原任務要求 30–45 次，未達標，缺口已在下方逐項標示。
- **WebFetch 全面 403；額外測試 `curl` 直連 Digi-Key 亦被 proxy 以 `CONNECT tunnel failed, response 403` 阻擋**。因此：
  - 所有法規條文**未能直接讀取 EUR-Lex 原文**，僅能靠搜尋摘要與二手合規機構（TÜV、SGS、CIRS、Assent、GreenSoft）轉述交叉比對。條文編號與日期已由 ≥3 個獨立來源互證，但**條文精確措辭標為「二手轉述」**。
  - **無法取得完整 1/10/100/1k/10k 階梯價**。分銷商頁面只能靠搜尋引擎快照吐出的片段價格。取得完整階梯者僅 Murata MZB1001T02 一項；其餘多為單價點。
- **查無 / 未能驗證的項目（重要）**：
  1. `rohs.exemptions.oeko.info` 的 2026 年最新公告頁無法開啟，**「是否有一份獨立、明確指名 7(c)-VI 的續期申請在 2026-06-30 前送出」無法直接證實**，只能引用二手來源稱「7(c)-V 與 7(c)-VI 受 7(c)-I 續期申請涵蓋／影響、到期日已凍結」。這是本 dossier 最大的單一未驗證點，客戶應直接向 Oeko-Institut / ECHA 查證。
  2. 個別申請人名單（EPCIA、JEITA、TDK、Murata 是否具名申請）**查無**。僅能確認歷史（Pack 22）申請人包含 Bourns 與 Umbrella Project。
  3. CeraPlas HF 出現 **US$142.25 與 US$300.00 兩個互相衝突的 Digi-Key 價格快照**，未能仲裁，兩者並列。
  4. TDK PowerHap 1204H018V060、xMEMS 喇叭、Lee Ventus Disc Pump 的公開單價**查無**（皆需詢價）。
  5. 美國聯邦層級是否有對應限鉛規範**未驗證**；搜尋中出現的「EPA TSCA Section 6 限制電子用鉛」說法來自一個明顯 AI 生成的市場報告站（MarkWide），**判定為不可信，不採用**。
  6. UK（GB RoHS）7(c)-I 對應到期日**查無**，僅能確認 GB 有獨立豁免制度。
- 市場規模數字（如「KNN 市場 2025 年 4.18 億美元」）來自 futuremarketinsights / BCC 等付費市調摘要，**一律標為低可信度**，不作為決策依據。

---

## 1. 結論摘要

1. **前輪三項時間點全部為真**：Commission Delegated Directive **(EU) 2025/2363，日期 2025-09-08**，新增 **7(c)-VI（PZT 壓電陶瓷 + PTC 陶瓷），效期至 2027-12-31**；**7(c)-I 效期至 2027-06-30**；會員國轉置期限 **2026-06-30**、自 **2026-07-01** 適用。**但 OJ 刊登日是 2025-11-21，不是 9 月 8 日**（9/8 是通過日）。同批共三份：2025/1802（高熔點焊料）、2025/2363（玻璃／陶瓷）、2025/2364（鋼/鋁/銅合金元素）。
2. **「續期窗口已關閉」是誤判 —— 窗口已被使用，且已凍結時鐘**。依 RoHS Art. 5(5)，續期申請須於到期前 18 個月提出（7(c)-I 到期 2027-06-30 → 死線 2025-12-31）。**RoHS Umbrella Industry Project 公開宣示將於 2025-12-31 前提交 6(a)-I、6(a)-II、6(c)、7(a)、7(c)-I 的續期申請**；二手來源指 **7(c)-I 的續期申請於 2025-12-12 送出**，一批續期申請集中在 **2025-12-11～12-17** 收件；**7(c)-I／-II／-V／-VI 的到期日因此「suspended」**，在執委會作出決定前持續有效。
3. **即使被駁回，也不是斷崖**：RoHS 實務上對駁回案給予 **12–18 個月過渡期**；且**已上市（placed on the market）的產品不受追溯**。合規決策時間軸因此至少到 **2029 年前後**，不是 2027。
4. **法規主管機關正在換手**：**Directive (EU) 2025/2456 於 2026-01-01 生效**，把 RoHS 的科學／技術評估任務移交 **ECHA**，實質效力自 **2027-08-13** 起；ECHA 將於 2026 或 2027 公布統一的豁免申請格式與指引。**這代表 2027 年之後的續期審查會用 ECHA 的證據標準（更嚴、更資料驅動）**，比目前的 Oeko-Institut 流程更難過關。另 EN IEC 63000:2018 的修訂已於 2025-12-18 由執委會發函 CENELEC 啟動。
5. **軍工／太空／大型固定裝置根本不在 RoHS 範圍內**（Art. 2(4)：軍品、送入太空的設備、大型固定工業工具、大型固定裝置、以及專為上述設備設計且只能被同款件替換的零件）。若客戶的兩用元件鎖定國防／太空／大型工業設備，RoHS 含鉛議題直接歸零。
6. **無鉛材料在「高功率共振」這個最關鍵指標上仍未追上硬式 PZT**。硬式 PZT 經受體摻雜後 Qm 可由 ~80 提升至 >1000，高功率應用需 Qm > 500；而 KNN 領域的權威回顧（National Science Review, 2022）把「Qm 突破 500 且 d33 達 ~300 pC/N」列為**未來研究目標**，等於承認當時尚未達成。2025 年 Nature Communications 有 Cu 摻雜缺陷偶極 + 相界工程提升 KNN Qm 的新進展，但屬實驗室級。
7. **價格錨點的極端值差 1,000 倍**：最便宜的量產壓電元件是 Murata CSTNE/CSTCE 陶瓷諧振器（Digi-Key **US$0.27**@1；LCSC 量產價自 **US$0.116**）與壓電蜂鳴片（LCSC **US$0.146**、Digi-Key PKM22 **US$0.66**）；最貴的是 TDK CeraPlas HF（**US$142.25 或 US$300**，來源衝突）。中間是 PowerHap 穿戴型致動器 **US$15.21**、Bartels mp6 微泵 **~US$66**、Murata 微型鼓風機 MZB1001T02 **US$18.33@1 → US$12.28@100**。
8. **價差主因不是 PZT 粉體**：多層共燒壓電體的內電極必須耐 ~1200 °C 硬式 PZT 燒結溫度，因而被迫用 Ag/Pd（高 Pd 比）或 Pt；文獻明言「隨著疊層數增加，**電極成本主導元件總成本**」、「高 Pd 或 Pt 讓元件價格劇增」。**賤金屬（Cu/Ni）共燒是唯一能把多層壓電件拉進 US$1 級距的槓桿。**

---

## 2. 查證結果 / 現況

### 2.1 逐條查證前輪 agent 的說法

| 前輪說法 | 判定 | 正確版本與來源 |
|---|---|---|
| 2025-09-08 執委會通過修訂 | **真** | Commission Delegated Directive (EU) 2025/2363 **of 8 September 2025**；同日還有 2025/1802、2025/2364 |
| 新增 7(c)-VI 涵蓋 PZT 與 PTC，效期至 2027-12-31 | **真** | 7(c)-VI：陶瓷中之鉛，用於 (a) 壓電鋯鈦酸鉛（PZT）陶瓷、(b) 賦予陶瓷正溫度係數（PTC）特性；適用所有類別，惟排除 Annex III 之 7(c)-II、7(c)-III、7(c)-IV 及 Annex IV 第 14 點涵蓋之應用。**條文措辭為二手轉述，未讀 EUR-Lex 原文** |
| 原 7(c)-I 效期至 2027-06-30 | **真** | 7(c)-I（電容器介電陶瓷以外之玻璃或陶瓷中的鉛，如壓電元件）適用所有類別，到期 2027-06-30 |
| 會員國轉置 2026-06-30、2026-07-01 生效 | **真** | 三份 Delegated Directive 均載明 |
| 續期須於期滿前 18 個月提出，2026-06-30 前，窗口可能已關 | **部分錯誤／結論錯誤** | 18 個月規則為真（Art. 5(5)）。但 7(c)-I 的死線是 **2025-12-31**（不是 2026-06-30），且**已於 2025-12-12 提出**；7(c)-V／-VI 被二手來源指為「受 7(c)-I 續期申請影響／涵蓋」，四項到期日皆已凍結 |
| — | **前輪未提到的重點** | OJ 刊登日 2025-11-21；ECHA 接手（Directive (EU) 2025/2456，2026-01-01 生效）；駁回有 12–18 個月過渡期；Art. 2(4) 軍工／太空排除 |

### 2.2 誰提出了續期申請？

- **可確認**：**RoHS Umbrella Industry Project** —— 自 2013 年 RoHS II 上路即運作、由**全球 70 餘個公協會**組成的產業聯合體，設有策略管理小組（SMT）與各豁免項目的技術工作小組。它公開宣示會在 2025-12-31 前替 **6(a)-I、6(a)-II、6(c)、7(a)、7(c)-I** 提出續期申請。其設計目的正是「集中資源、減少重複申請」。
- **歷史對照（Pack 22, 2020–2022）**：7(c)-I 的申請文件檔名顯示至少三位申請人 —— `Application_UP_7_c_-I_Exemption_Request_31Jan2020_final.pdf`（UP = Umbrella Project）、`Ex_7c-I_Applicant_1_Bourns_response...`（**Bourns**）、`Ex_7c-I_Applicant_3_OFP_Response...`（申請人 3 代號 OFP，**未能確認全名，不臆測**）。
- **查無**：EPCIA、JEITA、日本電子情報技術產業協會、TDK、Murata 是否於 2025-12 具名申請。一則二手摘要稱「執委會收到 8 份 7(c)-I 續期請求」，**但無法確認是指 2025 這一輪或前一輪，標為未驗證**。

### 2.3 若豁免真的到期，實際後果

1. **禁止「投放市場」，不禁止已上市品**：豁免到期後，新製造／新投放歐盟市場的含 PZT 產品即不符合 RoHS；**到期前已 placed on the market 的 EEE 可繼續留在市場**（無追溯召回）。
2. **駁回附過渡期**：執委會決定若為駁回，依實務給予 **12–18 個月**過渡期，讓業者調整製程。
3. **執法後果**：不符合 RoHS 的產品面臨海關扣留、罰款、下架、召回。（有二手來源給出「€10,000–€100,000+」罰款區間，**來源為合規軟體商部落格，可信度低，僅供參考**。）
4. **醫療（Cat. 8）／監控儀器（Cat. 9）另有 Annex IV**：Annex IV 第 14 點為「用於超音波換能器之**單晶**壓電材料中的鉛」，**僅適用 Cat. 9 工業用**。注意這是「單晶」（PMN-PT／PZN-PT 類），不涵蓋一般多晶 PZT 陶瓷。多晶 PZT 在 Cat. 8/9 仍靠 Annex III 的 7(c)-I / 7(c)-VI。
5. **範圍排除（Art. 2(4)）**：軍品／軍用武器彈藥、送入太空的設備、大型固定工業工具、大型固定裝置、以及專為上述而設計且只能以同款件替換之設備 —— **完全不在 RoHS 適用範圍**。這是含鉛 PZT 在國防／航太／重工業的永久避風港。

### 2.4 其他地區

| 地區 | 制度 | 對含鉛壓電陶瓷的實際效果 | 可信度 |
|---|---|---|---|
| **歐盟** | RoHS 2 (2011/65/EU) + Annex III/IV 豁免 | 目前**豁免中**（7(c)-I / 7(c)-VI），到期日凍結中 | 高（多源交叉） |
| **中國** | 《電器電子產品有害物質限制使用管理辦法》（八部門令第 32 號，China RoHS 2）+《達標管理目錄》 | 目錄第一批僅 **12 類產品**（冰箱、空調、洗衣機、電熱水器、印表機、影印機、傳真機、電視、顯示器、微型電腦、行動電話、電話單機）；**目錄外產品只需標識，不需符合限值**。豁免清單約 **39 項**，架構對標 EU Annex III。2019-11-01 起製造／進口之目錄內產品須完成合格評定 | 中（二手，未讀原文清單） |
| **台灣** | **CNS 15663**（限用物質含有情況標示），2017-07-01 起為 BSMI 應施檢驗商品之強制要求 | **本質是「含有標示」制度（第 5 節），不是市場禁令**。限值：Pb/Hg/Cr(VI)/PBB/PBDE 1000 ppm、Cd 100 ppm。含鉛 PZT 只要標示即可銷售 | 中高 |
| **日本** | **J-Moss / JIS C 0950**，2006-07-01 生效 | **標示制度**，非禁令 | 中 |
| **韓國** | 《전기·전자제품 및 자동차의 자원순환에 관한 법률》（法律第 8405 號），2008-01-01 生效 | 管制內容對標 RoHS + ELV | 中 |
| **美國** | 無聯邦 RoHS | **查無**可信的聯邦層級電子含鉛限制。搜尋中出現的 TSCA §6 說法來自 AI 生成內容站，**判定不可信、不採用** | — |
| **英國（GB）** | RoHS Regulations 2012 (SI 2012/3032)，**獨立於 EU 的豁免制度** | 到期日可能與 EU 分歧，**GB 版 7(c)-I 到期日查無** | 低 |
| **越南／巴西／烏茲別克** | 2026 年有 RoHS 相關更新（Compliance & Risks 報導） | **未細查** | 低 |

**對台灣客戶的關鍵洞見**：亞洲主要市場（台、日、韓）與中國目錄外產品，**含鉛 PZT 實務上只是「標示」義務，不是禁令**。真正的市場准入壓力只來自歐盟，且歐盟目前處於豁免有效 + 時鐘凍結狀態。

### 2.5 無鉛替代的實際成熟度

**KNN（鈮酸鉀鈉）**
- 學界共識指標：權威回顧（*National Science Review* 9(8), nwac101, 2022）明列「未來研究目標是讓 **Qm 突破 500、d33 達 ~300 pC/N**，以匹敵商用硬式 PZT」——反證當時尚未達成。
- 2025 年 *Nature Communications* 論文「Excellent hardening effect in lead-free piezoceramics by embedding local Cu-doped defect dipoles in phase boundary engineering」提出以 Cu 摻雜缺陷偶極打破 d33–Qm 的傳統取捨，屬**實驗室級突破，非量產**。
- **量產者**：Honda Electronics（本田電子）明確聲稱已把無鉛壓電陶瓷產品實用化，並供應 15 kHz–400 MHz 全頻段之感測器／換能器；PI Ceramic 有無鉛壓電陶瓷產品型錄（`PI-Ceramic-BRO-Lead-Free-Piezoceramic-Materials.pdf`）。市調來源另列 Sumitomo Chemical、CTS 為主要玩家，**市調來源可信度低，標未驗證**。
- **BNT / BCTZ**：本輪**查無**足夠的量產證據。專利面可見 NBT 系高功率材料（US 8,501,031 / RE46,445「NBT based lead-free piezoelectric materials for high power applications」），顯示產業曾投入，但商業化證據不足。

**LiNbO₃（鈮酸鋰，天生無鉛）**
- 居里溫度 **1210 °C**，高 Qm、低損耗，已用於超音波致動器、2 MHz NDT 1-3 複合材、Z-cut 換能器。多層 LiNbO₃ 致動器在**性能與環保兩方面**皆被文獻認為優於 PZT 換能器。
- **上限**：機電耦合與介電常數遠低於 PZT，同樣位移需更高電壓；且為單晶，成本結構與陶瓷完全不同（切割、無法多層低成本共燒）。

**AlN / ScAlN（天生無鉛）**
- AlN d33 ≈ **8.4 pC/N**；Sc 摻雜 33.2% 時 d33 ≈ **23.6 pC/N**，35–43% 飽和。
- 2025 *Nature Communications*：熱退火可將 ScAlN 的 d33 由 12.3 → **45.5 pC/N**（3.5 倍，約為商用 5G AlN 的 8 倍）。
- 2025 *Adv. Electron. Mater.*：MBE 成長 ScAlN-on-Si(111)，Sc 30% 時 d33 ≈ **25.7 pC/N**，伸張模 BAW 共振器 **Q = 97k @ 70.28 MHz**。
- arXiv 2504.20014：ScAlN BAW 在 **12.5 GHz** 達 Q = 208、k² = 9.5%。
- **上限**：d33 僅為 PZT 的 1/10～1/20（硬式 PZT d33 常在 200–300 pC/N，軟式 >500）。ScAlN 的優勢是**極高 Q、CMOS/晶圓相容、高頻**，不是大位移或大功率密度。Sc 靶材成本被引為 >US$4,000/kg（**來源為 AI 生成的專利分析站，可信度低**）。

---

## 3. 關鍵數字表

### 3.1 法規時鐘

| 項目 | 數值／日期 | 來源可信度 |
|---|---|---|
| Delegated Directive 編號（玻璃/陶瓷含鉛） | **(EU) 2025/2363** | 高（EUR-Lex ELI 可查） |
| 通過日 | **2025-09-08** | 高 |
| OJ 刊登日 | **2025-11-21** | 中高（多家合規機構一致） |
| 同批其他兩份 | (EU) 2025/1802（高熔點焊料）、(EU) 2025/2364（鋼/鋁/銅合金元素） | 高 |
| 會員國轉置期限 | **2026-06-30** | 高 |
| 適用起日 | **2026-07-01** | 高 |
| 7(c)-I 名目到期日 | **2027-06-30**（全類別） | 高 |
| 7(c)-V 名目到期日（玻璃） | **2027-12-31** | 中高 |
| 7(c)-VI 名目到期日（PZT + PTC 陶瓷） | **2027-12-31**（全類別，排除 7(c)-II/III/IV 與 Annex IV 第 14 點） | 中高 |
| 續期申請提前期（Art. 5(5)） | **18 個月** | 高 |
| 7(c)-I 續期死線 | **2025-12-31** | 高（推算 + 二手確認） |
| 7(c)-I 續期申請實際送出日 | **2025-12-12**；同批 2025-12-11～17 | **中**（二手，未直讀官方頁） |
| 續期申請人 | **RoHS Umbrella Industry Project**（70+ 公協會） | 中高（其自身公告） |
| 目前狀態 | 7(c)-I／-II／-V／-VI 到期日 **suspended**，續期決定前持續有效 | **中**（二手，需客戶自行向 ECHA/Oeko 複核） |
| 執委會決定所需時間 | 自申請日起 **18–24 個月** | 中（ZVEI factsheet） |
| 駁回時之過渡期 | **12–18 個月** | 中高 |
| ECHA 接手法源 | **Directive (EU) 2025/2456**，2026-01-01 生效，實質效力 **2027-08-13** | 中高 |
| EN IEC 63000:2018 修訂啟動 | **2025-12-18**（執委會發函 CENELEC） | 中 |

### 3.2 分銷商價格錨點（USD，皆為搜尋快照，日期未標；標「@n」表示該數量之單價）

| 元件 | 廠商／料號 | 價格 | 通路 | 備註 |
|---|---|---|---|---|
| 陶瓷諧振器 8 MHz | Murata **CSTNE8M00G550000R0** | **$0.27 @1** | Digi-Key | 成本下限錨點 |
| 陶瓷諧振器 8 MHz（舊款） | Murata **CSTCE8M00G55-R0** | **$0.1161 起** | LCSC | **EOL，LTB 2019-09-30** |
| 壓電蜂鳴器 φ13 | Murata **PKM13EPYH4000-A0** | **$0.1460 起**（LCSC）／$0.248（Blikai） | LCSC | Digi-Key 需報價、非常備 |
| 壓電蜂鳴器 φ22 | Murata **PKM22EPPH4001-B0** | **$0.66 @1** | Digi-Key | |
| 壓電蜂鳴片 φ27（裸片） | 通用（eBay/Amazon） | 10 pcs **$8.06**（≈$0.81/pc 零售） | eBay | 零售價，非量產價 |
| 超音波換能器 40 kHz（收） | Murata **MA40S4R** | **$5.77 @1 → $3.917 @1080**（−32%） | Digi-Key | 斜率錨點 |
| 壓電微型鼓風機 | Murata **MZB1001T02** | **$18.33 @1 / $15.05 @10 / $13.80 @25 / $12.90 @50 / $12.28 @100**（1→100 降 33%） | Digi-Key | **本輪唯一完整階梯** |
| 壓電微泵 | Bartels **mp6** | **~$65.65–$67** | Digi-Key Marketplace / Blikai | |
| 壓電碟式泵 | Lee Ventus (TTP) **Disc Pump / XP** | **未公開，需詢價** | — | 查無 |
| 壓電觸覺致動器（穿戴） | TDK PowerHap **Z63000Z2910Z001Z48** | **$15.21 @1** | Digi-Key | |
| 壓電觸覺致動器 | TDK **1204H018V060** | **查無公開單價** | — | 僅見於 Starter Kit |
| 壓電冷電漿產生元件 | TDK CeraPlas HF **Z63000Z2910Z1Z60** | **$142.25** 或 **$300.00**（來源衝突） | Digi-Key | 47.3 × 20 × 20 mm，PZT 本體 + 塑膠外殼 |
| CeraPlas 評估套件 | TDK **Z63000Z2910Z1Z61** | **查無** | Digi-Key | |
| 壓電驅動 IC | Boréas **BOS1901CQR** | **已停產（obsolete）** | Digi-Key / Mouser | **重大情報：BOS1901 已 EOL** |
| 壓電驅動 IC（替代） | Boréas **BOS1921CQR** | **$6.65** | Digi-Key | 原廠指定替代料 |
| 壓電變壓器（陸廠） | AS-313T 類 2 W SMD | 樣品 **$7** | Alibaba | 未驗證規格 |
| 臭氧／電漿用壓電變壓器模組 | 陸廠通用 | **$19.27 起（量產）** | Alibaba | 未驗證 |
| MEMS 喇叭 | xMEMS Cypress / Montara | **未公開單價**。二手：二代 Cowell 方案成本較動圈高 **70–80%**，新方案可收斂至 **30% 以內** | Digitimes 訪談 | 低可信度，轉述 |
| **對照組**：功率電感 10 µH | Würth 74438324100 / 7447709100 | **階梯價查無**（搜尋未吐出數字） | Digi-Key | 本輪失敗項 |

---

## 4. 對決策的意涵

### 4.1 材料選擇：**不必為了 RoHS 跳過 PZT，但要為了「戰略韌性」把無鉛留成第二軌**

- **不必跳過 PZT 的理由**：(a) 豁免時鐘已被業界凍結，決定尚未做出；(b) 即使駁回也有 12–18 個月過渡期 + 已上市品不追溯，實質壓力最快落在 **2029 年前後**；(c) 亞洲主場（台、日、韓、中國目錄外）對含鉛 PZT 只有標示義務；(d) 軍工／太空／大型固定裝置完全不在 RoHS 範圍。
- **但要留第二軌的理由**：ECHA 於 2027-08-13 起接手評估，證據門檻會提高；Umbrella Project 每一輪都必須重新舉證「無替代品」，而每一篇 KNN 進展論文都在削弱這個論證。**一個 2026 年才啟動研發、2029–2031 才量產的元件，其產品生命週期正好落在 ECHA 標準生效之後。**
- **LiNbO₃ / AlN / ScAlN 是否因此「戰略上更正確」？——條件式為真**：
  - **若元件的價值主張是「高 Q、高頻、低損耗、CMOS 整合、極端溫度」**（例如濾波／隔離／時鐘／感測／微型化 PMUT），則 **ScAlN 或 LiNbO₃ 明確更正確**：天生無鉛、法規風險為零、且性能優勢與 PZT 不重疊（ScAlN BAW Q 可達 97k @ 70 MHz、12.5 GHz 仍可運作）。
  - **若元件的價值主張是「大位移、大功率密度、高壓昇壓」**（致動、微泵、電漿、超音波清洗、壓電變壓器），則 **ScAlN/AlN 物理上做不到**（d33 僅 PZT 的 1/10–1/20），LiNbO₃ 也需更高驅動電壓；此時**含鉛 PZT 沒有真正的替代品**，法規風險必須用「應用選在 RoHS 範圍外」或「同步養 KNN 配方」來對沖。
  - **對「兩用元件」的直接推論**：同一顆壓電體要同時吃「被動（儲能／濾波／隔離）」與「主動（致動／高壓／輻射）」，材料選擇會被**主動側的功率需求**綁死。**建議把產品線一開始就分成兩條 SKU**：高功率線走硬式 PZT（並鎖定 RoHS 範圍外或 Cat. 9 應用），高頻/整合線走 ScAlN 或 LiNbO₃。單一材料通吃是幻覺。

### 4.2 成本結構：價差來自哪裡（第 8 題拆解）

從「CSTCE $0.12–0.27」到「CeraPlas $142–300」約 **1,000 倍**的價差，可拆解為：

| 價差來源 | 貢獻方向 | 證據強度 |
|---|---|---|
| **材料體積** | CSTCE 陶瓷體約 mm³ 級；CeraPlas 為 47.3 × 20 × 20 mm 外形的多層長條體，陶瓷用量高 2–3 個數量級 | 高（尺寸為原廠公開） |
| **層數 × 內電極貴金屬** | **最大單一驅動因子**。硬式 PZT 燒結 ~1200 °C，逼迫內電極用 Ag/Pd（高 Pd）或 Pt；文獻明言「疊層數增加後，**電極成本主導元件總成本**」、「高 Pd 或 Pt 使元件價格劇增」 | **高**（同儕評閱回顧） |
| **極化（poling）與頻率分選** | 高壓多層件的極化需高電壓、長時間、且良率損失；共振件需頻率分選（binning），分選會直接放大單價 | 中（推論，未取得具體良率數字） |
| **封裝與高壓絕緣** | CeraPlas 需塑膠外殼 + 高壓爬電距離；蜂鳴片幾乎無封裝 | 中高 |
| **認證與應用支援** | 電漿／醫療級元件需安規、EMC、臭氧排放等驗證；諧振器只需一般元件規格 | 中（推論） |
| **量（規模）** | CSTCE 屬 10⁸–10⁹ 顆/年級別的通用時序件；CeraPlas 為利基件，年出貨量可能只有 10⁴–10⁵ | 中（無公開出貨量，屬推論） |
| **壟斷／技術溢價** | CeraPlas 目前無直接同級競品（PDD® 冷電漿），TDK 具定價權；PowerHap 亦然 | 中（無競品即為證據，但無成本資料佐證溢價幅度） |

**結論性判斷**：價差裡**「量 × 電極貴金屬」約占主導，材料（PZT 粉體）本身占比極小**。這代表**降本的槓桿不在材料採購，而在 (1) 賤金屬（Cu/Ni）共燒、(2) 減少層數改用更高驅動電壓、(3) 把單一品項的年量推上 10⁶ 以上**。

### 4.3 從階梯價斜率反推固定成本占比（第 9 題）

可用的兩條斜率：

| 元件 | 1 → 100（或 1k）降幅 | 推論 |
|---|---|---|
| Murata MZB1001T02 | $18.33 → $12.28（100 pcs），**−33%** | 1→100 只降三分之一 |
| Murata MA40S4R | $5.77 → $3.917（1,080 pcs），**−32%** | 同樣約降三分之一 |

**反推**：
- 兩條完全不同類型（模組 vs 換能器）的元件在 1→10²–10³ 區間呈現**幾乎相同的 −32~33%**，說明這一段斜率**主要由分銷商的訂單處理／庫存成本結構決定，而非製造規模效應**。分銷通路的固定成本（picking、包裝、最小訂單處理）約占 qty-1 價格的三分之一。
- **真正的製造規模效應在 10³ 以上才開始顯現，而分銷商階梯價完全看不到這一段。** 業界經驗值（**此為推論，非查證數字**）：原廠對 10⁵–10⁶ 顆/年客戶的報價，通常落在 Digi-Key 1k 階梯價的 **30–50%**。
- 套用到 MZB1001T02：Digi-Key 100 pcs = $12.28 → 推估原廠 10⁵ 級報價 **$4–6**，工廠成本 **$2–3.5**。
- 套用到 CeraPlas（取較保守的 $142.25）：推估原廠 10⁴–10⁵ 級報價 **$40–70**，工廠成本 **$20–40**。**這對「電漿／高壓」類應用而言仍是高得離譜的價格，正是這條路線市場一直打不開的原因。**

### 4.4 目標成本與可接受售價（第 10 題）

| 情境 | 元件形態 | 年量 | 目標工廠成本 | 合理 ASP | 能吃下的應用 |
|---|---|---|---|---|---|
| **A. 極致降本線** | 單層／少層 PZT 圓片或方片，Ag 電極，無複雜封裝 | 10⁷+ | **US$0.10–0.40** | **US$0.3–1.0** | 消費性蜂鳴／觸覺／簡易感測。**兩用價值極低，不建議進入** |
| **B. 主戰場（建議）** | **10–40 層共燒，賤金屬（Cu/Ni）內電極**，SMD 或引腳封裝，兼具共振被動功能與致動／昇壓主動功能 | 10⁵–10⁶ | **US$1.5–6** | **US$5–20** | 汽車觸覺、微流體／微泵、可攜式醫療、工業隔離閘驅、氣體感測、AIoT 致動 |
| **C. 利基高值線** | 高壓／高功率多層（Ag/Pd 或 Pt），含安規與應用支援 | 10⁴–10⁵ | **US$15–40** | **US$50–150** | 冷電漿、臭氧、消毒、牙科／美容儀器、NDT、太空／國防（RoHS 範圍外） |

**判斷**：
- **情境 B 是唯一同時具備「新能力」與「可規模化」的區間**。它的成敗完全繫於**能否用賤金屬共燒把多層件做到 US$1.5–6**——這正是文獻指出的成本主導因子。若客戶不具備賤金屬共燒（還原氣氛燒結、抗還原 PZT 配方）的能力或授權，情境 B 在成本上不可能成立，只能退回情境 C。
- **US$5–20 的 ASP 能被吃下的判準**：終端產品 BOM > US$50 且該元件能**同時取代兩個以上既有零件**（例如同時吃掉一顆致動器 + 一顆變壓器 + 一顆濾波元件）。若只是「多一顆」，US$5 以上的元件在消費性市場沒有機會。
- **對照組（功率電感／變壓器）的價格未能查證**，這是本輪的重大缺口。但既有認知是：同等級功率電感單價常在 **US$0.1–1**，繞線變壓器 **US$0.5–5**。**若客戶的兩用元件要價 US$5–20，它必須賣的是「一顆抵三顆 + 磁免疫 + 薄型化」，而不是價格。**（此段對照數字為**未查證的既有認知**，客戶須自行複核。）

---

## 5. 反面證據與上限

1. **「豁免凍結」是二手資訊，且凍結不等於獲准**。到期日 suspended 只是程序性保護；執委會（未來 ECHA）仍可駁回並給 12–18 個月過渡期。歷史上 Oeko-Institut 對 7(c)-I 的評估已多次建議**縮窄範圍**（2025 年的拆分為 7(c)-I / -II / -V / -VI 正是縮窄的結果）。**趨勢明確是「切碎、縮窄、逐步淘汰」，不是永久豁免。**
2. **拆分本身就是壞消息**。把一個大豁免拆成多個細項，等於逐項獨立評估、逐項獨立到期——**未來任何一項被砍，不會拖累其他項，執委會砍起來更沒有阻力**。前輪把「新增 7(c)-VI」讀成利多，實際上是**風險被精準化**。
3. **無鉛替代的證據會隨時間越來越強，不會越來越弱**。2025 年 Nature Communications 的 KNN 硬化研究若被複製並產業化，Umbrella Project 在下一輪（2029 前後）論證「無可替代」的難度將顯著上升。
4. **ScAlN／AlN 在功率密度上有硬性物理上限**：d33 8.4–45.5 pC/N vs 硬式 PZT 200–300 pC/N，差 5–30 倍。**任何需要大位移或高機械功率的「主動」功能，ScAlN 都做不到**，不能因為「天生無鉛」就當成 PZT 的通用替代。
5. **價格資料本身不可靠**：CeraPlas 出現 $142.25 與 $300 兩個衝突快照；多個關鍵料件（PowerHap 1204H018V060、Lee Ventus、xMEMS）**無公開價格**；BOS1901 已停產（顯示這個利基市場的商業存活率不高）。**用分銷價反推工廠成本的方法，誤差可能達 2–3 倍。**
6. **BOS1901 停產是一個負面訊號**：Boréas 是壓電觸覺驅動 IC 的旗手，其第一代旗艦料號停產、由 BOS1921 取代（$6.65），說明**壓電驅動 IC 的單價無法下探到大眾消費性的價格帶**——US$6.65 的驅動 IC 就已經吃掉整個 TWS／穿戴 BOM 的可觀比例。**兩用元件的隱藏成本是驅動電路，不是壓電體本身。**
7. **市調數字全部不可用**：搜尋回傳的 KNN 市場規模、CAGR、廠商市占（Sumitomo 14% 等）皆來自明顯為 AI 生成或付費摘要的網站，其中一則甚至捏造了「EPA TSCA §6 限制電子用鉛」。**本 dossier 拒絕採用任何此類數字。**

---

## 6. 未解問題

1. **（最高優先）7(c)-VI 是否有獨立的續期申請在 2026-06-30 前送出？** 二手來源稱其「被 7(c)-I 續期申請涵蓋／影響」，但 7(c)-VI 是 2025-11-21 才刊登的**新豁免**，其法定續期死線為 2026-06-30 —— 而今天是 2026-07-31。**必須直接向 Oeko-Institut（rohs.exemptions.oeko.info）或 ECHA 查證**，這是本案唯一可能真正致命的時間點。
2. **續期申請人具名清單**：EPCIA、JEITA、TDK、Murata 是否個別具名？申請文件中對「無鉛替代不可行」的論證用了哪些數據？這決定了論證的脆弱度。**查無。**
3. **Digi-Key / Mouser 完整階梯價（1/10/100/1k/10k）**：本輪因 WebFetch 與 curl 雙雙 403 而失敗。**建議客戶用瀏覽器或 Octopart/Findchips API 直接抓取**，特別是 CeraPlas 的價格衝突需仲裁。
4. **對照組（同等級功率電感／變壓器）單價**：完全未取得。這是判斷「兩用元件能否在成本上說服客戶」的必要基準。
5. **賤金屬（Cu/Ni）共燒硬式 PZT 的產業化現況**：文獻指出這是成本主導因子的解方，但**誰已量產、良率如何、專利誰持有，本輪完全未查**。這應是下一輪研究的第一優先。
6. **中國 China RoHS 39 項豁免清單中，壓電陶瓷含鉛的確切條號與到期安排**：未讀原文清單。

---

## 7. 來源清單

**法規（歐盟）**
1. Commission Delegated Directive (EU) 2025/2363 of 8 September 2025 — https://eur-lex.europa.eu/eli/dir_del/2025/2363/oj/eng — 修訂 RoHS Annex III 之 7(c)-I、7(c)-II，新增 7(c)-V、7(c)-VI（本案核心法源；未能直接讀取內文）
2. Commission Delegated Directive (EU) 2025/2364 — https://eur-lex.europa.eu/eli/dir_del/2025/2364/oj/eng — 同批，鋼/鋁/銅中作為合金元素之鉛
3. Commission Delegated Directive (EU) 2025/1802 — https://eur-lex.europa.eu/eli/dir_del/2025/1802/oj/eng — 同批，高熔點焊料中之鉛
4. Directive 2011/65/EU 原文（OJ L 174, 2011）— https://eur-lex.europa.eu/LexUriServ/LexUriServ.do?uri=OJ%3AL%3A2011%3A174%3A0088%3A0110%3Aen%3APDF — Art. 2(4) 範圍排除、Art. 5(5) 18 個月續期規則之法源
5. RoHS Annex IV 條文（lexparency 鏡像）— https://lexparency.org/eu/32011L0065/ANX_IV/ — 醫療與監控儀器專用豁免，含第 14 點「超音波換能器用單晶壓電材料中的鉛」
6. European Commission — RoHS Directive implementation / Exemptions Procedure — https://environment.ec.europa.eu/topics/waste-and-recycling/rohs-directive/rohs-directive-implementation_en — 官方豁免程序說明
7. ECHA — EU RoHS legislation profile — https://echa.europa.eu/legislation-profile/-/legislationprofile/EU-ROHS — ECHA 接手後的官方入口
8. European Parliament Legislative Train — Revision of RoHS (REFIT) — https://www.europarl.europa.eu/legislative-train/theme-a-european-green-deal/file-revision-of-eu-rules-restricting-the-use-of-hazardous-substances-in-electronics — RoHS recast 狀態

**豁免評估與續期程序**
9. RoHS Exemptions（Oeko-Institut）News — https://rohs.exemptions.oeko.info/news — 官方豁免評估公告頁（本輪無法開啟內容）
10. Umbrella Project 7(c)-I 豁免申請書（Pack 22, 2020-01-31）— https://rohs.exemptions.oeko.info/fileadmin/user_upload/RoHS_Pack_22/Exemptions/7c_I/Application_UP_7_c_-I_Exemption_Request_31Jan2020_final.pdf — 歷史申請人與論證結構
11. Bourns 對 7(c)-I 澄清問卷之回覆（Pack 22）— https://rohs.exemptions.oeko.info/fileadmin/user_upload/RoHS_Pack_22/Exemptions/7c_I/Ex_7c-I_Applicant_1_Bourns_response_2021_Clarification_Questions_final_.pdf — 證明 Bourns 為歷史申請人之一
12. RoHS Pack 22 最終報告（2022-02 修訂版）— https://rohs.exemptions.oeko.info/fileadmin/user_upload/RoHS_Pack_22/RoHS_Pack-22_final_report_amended_February_2022.pdf — 7(c)-I 的無鉛替代技術評估；含「無鉛壓電材料介電與彈性性質及其溫度相依性與含鉛材料顯著不同」之論述
13. ZVEI Factsheet — Exemption processes in RoHS and ELV (2024-12-03) — https://www.zvei.org/fileadmin/user_upload/Presse_und_Medien/Publikationen/2024/Dezember/Ausnahmeprozesse_in_den_europaeischen_Richtlinien_RoHS_und_ELV_-_Faktenblatt/ZVEI-Factsheet-exemption-processes-in-RoHS-and-ELV-20241203_en.pdf — 續期流程、18–24 個月決策期、12–18 個月過渡期之來源
14. Oeko-Institut — Pack 9 專案頁（含 7(c)-I）— https://www.oeko.de/en/projects/detail/study-to-assess-renewal-requests-for-29-rohs-2-annex-iii-exemptions-no-1a-to-e-lighting-purpose-no-1f-special-purpose-no-2a-no-2b3-no-2b4-no-3-no-4a-no-4b-no-4c-no-4e-no-4f-no-5b-no-6a-no-6b-no-6c-no-7a-no-7c-i-no-7c-ii-no-7c-iv-no-8b-no-9-no-15-no-18b-no-21-no-24-no-29-no-32-no-34-no-37-pack-9/ — 歷史評估專案

**合規機構解讀（二手，用於交叉比對）**
15. TÜV Rheinland — Directive (EU) 2025/2363 amending RoHS… 7(c)-I, 7(c)-II, 7(c)-V, 7(c)-VI — https://www.tuv.com/regulations-and-standards/en/europe-directive-eu-2025-2363-amending-rohs-directive-on-exemptions-for-lead-in-glass-or-ceramic-components-7-c-i-7-c-ii-7-c-v-7-c-vi.html — 豁免編號與到期日之主要交叉來源
16. TÜV SÜD — EU comprehensive updates to lead exemptions under RoHS — https://www.tuvsud.com/en/knowledge-hub/technical-updates/consumer-products-and-retail-essentials/eu-comprehensive-updates-to-lead-exemptions-under-rohs-directive — 同上
17. CIRS Group — EU RoHS Directive Update: Comprehensive Refinement of Lead Exemption Clauses — https://www.cirs-group.com/en/chemicals/eu-rohs-directive-update-comprehensive-refinement-of-lead-exemption-clauses — 7(c)-VI 涵蓋 PZT 與 PTC、到期 2027-12-31 之來源
18. Normachem — Update of RoHS Annex III lead exemptions: three new Delegated Directives published — https://www.normachem.com/en/normachem-informs/update-of-rohs-annex-iii-lead-exemptions-three-new-delegated-directives-published — OJ 刊登日 2025-11-21
19. Assent — Final Delegated Directives for Key RoHS Lead Exemptions Adopted — https://www.assent.com/blog/draft-expiry-dates-for-key-rohs-lead-exemptions-published/ — 到期日與適用範圍
20. GreenSoft Technology — 2026 EU RoHS Exemption Updates — https://greensofttech.com/blog-2026-eu-rohs-exemption-updates/ — **「7(c)-I、-II、-V、-VI 到期日 suspended，因 2025 年 12 月提出續期申請」之主要來源；2025-12-11～17 收件批次**
21. EcoComply — RoHS Exemptions 2026–2027: Critical Deadlines — https://ecocomply.ai/blog/rohs-exemptions-2026 — 7(c)-I 續期申請 2025-12-12；不合規之執法後果（罰款區間為低可信度）
22. Compliance & Risks — RoHS in 2026: Essential Updates From the EU, Uzbekistan, Vietnam, and Brazil — https://www.complianceandrisks.com/blog/rohs-in-2026-essential-updates-from-the-eu-uzbekistan-vietnam-and-brazil/ — 2026 年全球 RoHS 動態
23. ComplyMarket — EU RoHS Compliance 2026: Latest Updates, Lead Exemptions, ECHA Changes — https://www.complymarket.com/en/blogs/eu-rohs-updates-2026 — **Directive (EU) 2025/2456、ECHA 接手、EN IEC 63000 修訂之來源**
24. Source Intelligence — EU RoHS Compliance in 2026 — https://blog.sourceintelligence.com/eu-rohs-compliance — 同上交叉
25. RoHS Guide — RoHS Annex 3 Lead Exemptions 2025-2027 — https://www.rohsguide.com/rohs-lead-exemptions.htm — 豁免清單彙整
26. Enviropass — RoHS Annex IV 豁免清單（2025-08-27）— https://getenviropass.com/wp-content/uploads/2025/08/RoHS-exemptions-Annex-IV-Medical-Monitoring-and-Control-August-27-2025.pdf — Cat. 8/9 專用豁免
27. GOV.UK — Regulations: restriction of hazardous substances (RoHS) — https://www.gov.uk/guidance/rohs-compliance-and-guidance — GB RoHS 獨立豁免制度

**其他地區**
28. SGS 台灣 — 台灣 RoHS CNS 15663 — https://www.sgs.com.tw/service/page/4/2/40-electric-electronic-restricted-substances-testing-services/255-tw-rohs-38 — 台灣限用物質含有標示制度
29. 經濟部標準檢驗局 — 電機電子類應施檢驗商品納入限用有害物質(RoHS)含有標示規定 — https://www.bsmi.gov.tw/wSite/public/Data/f1464658734896.pdf — BSMI 官方簡報
30. TÜV SÜD 中國 — 中國 RoHS 2.0 FAQ — https://www.tuvsud.cn/zh-cn/services/global-market-access/china/china-rohs-ii-faq — 達標管理目錄、合格評定、豁免清單

**材料與物理上限**
31. National Science Review 9(8) nwac101 (2022) — (K,Na)NbO₃-based lead-free piezoceramics: one more step to boost applications — https://academic.oup.com/nsr/article/9/8/nwac101/6596159 — **「Qm 突破 500、d33 達 ~300 pC/N」為未來目標之關鍵反證**
32. Nature Communications (2025) — Excellent hardening effect in lead-free piezoceramics by embedding local Cu-doped defect dipoles in phase boundary engineering — https://www.nature.com/articles/s41467-025-58269-5 — KNN 高 Qm 最新進展（實驗室級）
33. Journal of Materiomics — Lead-free piezoceramics – Where to move on? — https://www.sciencedirect.com/science/article/pii/S2352847815300083 — 無鉛壓電陶瓷的系統性限制回顧
34. PI Ceramic — Lead-Free Piezoceramic Materials 型錄 — https://www.pi-usa.us/fileadmin/user_upload/pi_ceramic/files/brochure_BRO/PI-Ceramic-BRO-Lead-Free-Piezoceramic-Materials.pdf — 商用無鉛壓電陶瓷之公開產品線
35. Honda Electronics — Ceramics products — https://en.honda-el.co.jp/product/ceramics — 宣稱無鉛壓電陶瓷已實用化，涵蓋 15 kHz–400 MHz
36. Sensors and Actuators A — Utilizing multilayer lithium niobate elements for ultrasonic actuators — https://www.sciencedirect.com/science/article/abs/pii/S0924424710005091 — LiNbO₃ 多層致動器優於 PZT 換能器之論證
37. arXiv 2512.07718 — Bimorph Lithium Niobate Piezoelectric Micromachined Ultrasonic Transducers — https://arxiv.org/pdf/2512.07718 — LiNbO₃ PMUT 最新進展
38. Advanced Electronic Materials (2025) — MBE-Grown ScAlN-on-Si Films… Extensional Mode BAW Resonators — https://advanced.onlinelibrary.wiley.com/doi/10.1002/aelm.202500217 — ScAlN d33 25.7 pC/N @ Sc 30%、BAW Q = 97k @ 70.28 MHz
39. Nature Communications (2025) — Unprecedented enhancement of piezoelectricity of wurtzite nitride semiconductors via thermal annealing — https://www.nature.com/articles/s41467-025-59179-2 — ScAlN d33 12.3 → 45.5 pC/N
40. arXiv 2504.20014 — Thin-film ScAlN BAW resonator with high Q of 208 and K² of 9.5% at 12.5 GHz — https://arxiv.org/pdf/2504.20014 — ScAlN 高頻上限
41. Microsystems & Nanoengineering (2025) — Recent progress in AlN for piezoelectric MEMS mirror applications: enhancements with scandium doping — https://www.nature.com/articles/s41378-025-01053-8 — AlN d33 8.4 pC/N、Sc 33.2% 時 23.6 pC/N
42. Nature/Springer 專利 US 8,501,031 與 RE46,445 — NBT based lead-free piezoelectric materials for high power applications — https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/8501031 — BNT 系高功率無鉛材料專利

**成本結構**
43. Actuators（回顧）— Base Metal Co-Fired Multilayer Piezoelectrics — https://www.researchgate.net/publication/296625421_Base_Metal_Co-Fired_Multilayer_Piezoelectrics — **「疊層數增加後電極成本主導元件總成本」「高 Pd 或 Pt 使元件價格劇增」之關鍵來源**
44. Materials & Design — Low temperature co-fired multilayer piezoelectric transformers for high power applications — https://www.sciencedirect.com/science/article/abs/pii/S0264127517306986 — LTCC 多層壓電變壓器之製程與成本考量
45. Texas Instruments SLYT107 — Understanding piezoelectric transformers in CCFL backlight applications — https://www.ti.com/lit/an/slyt107/slyt107.pdf — 多層 PZT 設計「製程較貴但電壓增益 20–70」

**價格（分銷商頁面；價格為搜尋快照，需自行複核）**
46. Digi-Key — Murata MZB1001T02 微型鼓風機 — https://www.digikey.com/en/products/detail/murata-electronics/MZB1001T02/2442520 — **本輪唯一完整階梯價：$18.33/$15.05/$13.80/$12.90/$12.28 @1/10/25/50/100**
47. Digi-Key — TDK CeraPlas HF Z63000Z2910Z1Z60 — https://digikey.bg/product-detail/en/epcos-tdk/Z63000Z2910Z1Z60/495-77395-ND/9698000 — 價格快照出現 $142.25 與 $300.00 兩個衝突值
48. Digi-Key — TDK CeraPlas 評估板 Z63000Z2910Z1Z61 — https://www.digikey.com/product-detail/en/epcos-tdk/Z63000Z2910Z1Z61/495-77394-ND/9697999 — 價格查無
49. Digi-Key — TDK PowerHap Z63000Z2910Z001Z48 — https://www.digikey.com/en/products/detail/epcos-tdk-electronics/Z63000Z2910Z001Z48/19181849 — $15.21
50. Digi-Key — Boréas BOS1901CQR — https://www.digikey.com/en/products/detail/boreas-technologies/BOS1901CQR/13171314 — **已停產（obsolete）**
51. Mouser — Boréas BOS1921CQR — https://www.mouser.com/ProductDetail/Boreas-Technologies/BOS1921CQR?qs=HoCaDK9Nz5eesZrKztNBcQ%3D%3D — 原廠指定替代料，Digi-Key $6.65
52. Digi-Key — Murata CSTNE8M00G550000R0 陶瓷諧振器 — https://www.digikey.com/en/products/detail/murata-electronics/CSTNE8M00G550000R0/8747739 — $0.27 @1（成本下限錨點）
53. LCSC — Murata CSTCE8M00G55-R0 — https://www.lcsc.com/product-detail/Ceramic-Resonators_muRata_CSTCE8M00G55-R0_CSTCE8M00G55-R0_C70457.html — $0.1161 起；該料號已 EOL（LTB 2019-09-30）
54. Digi-Key — Murata PKM22EPPH4001-B0 壓電蜂鳴器 — https://www.digikey.com/en/products/detail/murata-electronics/PKM22EPPH4001-B0/1219323 — $0.66
55. LCSC — Murata PKM13EPYH4000-A0 — https://www.lcsc.com/product-detail/C162678.html — $0.1460 起
56. Digi-Key — Murata MA40S4R 40 kHz 超音波接收器 — https://www.digikey.in/en/products/detail/murata-electronics/MA40S4R/490-7706-ND/4358146 — $5.77 @1 → $3.917 @1080
57. Digi-Key Marketplace — Bartels Mikrotechnik mp6 micropump — https://www.digikey.com/en/products/detail/bartels-mikrotechnik-gmbh/mp6-micropump/17752892 — ~$65.65–$67
58. The Lee Company — XP Series Disc Pump — https://www.theleeco.com/product/xp-series-disc-pump/ — 需詢價，公開價格查無
59. Alibaba — 2W SMD Piezoelectric Ceramic Transformer AS-313T — https://www.alibaba.com/product-detail/2W-SMD-Piezoelectric-Ceramic-Transformer-AS_1601003377245.html — 樣品 $7（規格未驗證）
60. TDK Electronics — CeraPlas element 產品目錄 — https://www.tdk-electronics.tdk.com/en/2464638/products/product-catalog/cold-plasma-technology/cold-plasma-surface-treatment/ceraplas-element — 官方規格（47.3 × 20 × 20 mm、PZT 本體）
61. xMEMS — Cypress 量產就緒新聞稿（2025-09-09）— https://xmems.com/press-release/xmems-announces-mass-production-readiness-of-cypress-the-worlds-first-full-range-mems-speaker-for-wireless-earbuds/ — 無公開價格
62. Digitimes — Redefining MEMS speakers: Q&A with xMEMS CEO Joseph Jiang — https://www.digitimes.com/news/a20240325PD205/xmems-mems-speakers-ic.html — 「二代方案成本較動圈高 70–80%、新方案可收斂至 30% 內」之來源（轉述，低可信度）
