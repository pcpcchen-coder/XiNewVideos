# 補查（檢索版）：隔離／穿壁的關鍵缺口與中壓可行性邊界

> 一句話結論：**這一輪實際檢索到的三個數字，把前一輪從第一原理推導出來的「中壓聲學隔離機會」直接關掉了——(1) 磁性／非壓電方案在 12 kV 連續電壓下已做到「5 W ＋ <1 pF」（US11356015），在 27 kV 絕緣等級下已做到「100 W ＋ 2.78 pF」，換算成 pF/W 分別是 <0.2 與 0.028，而 SAW 隔離閘驅的 0.032 pF/149 mW ＝ 0.215 pF/W，且只在 2.75 kV；(2) LiNbO₃ 在 GHz 頻段的 SAW 傳播損耗實測為 2.51–9.67 dB/mm，1.25 mm 聲程本身就已燒掉 3–12 dB，把聲程拉到中壓所需的 mm–cm 級在物理上不可行；(3) 降頻到 100 MHz 雖可換到 ~31 mm 聲程，但實測插入損耗 11.5 dB（＝ 93% 功率損失），做不成電源。因此壓電／聲學在隔離領域確實還有立足點，但那個窗口是「≤150 mW、≤3 kV、晶片級整合、且環境本身排除磁性材料（<77 K 深冷、>200 °C、或強磁場 MRI）」，不是「中壓」。**

---

## 0. 研究方法與限制（誠實揭露）

**本輪實際執行的 WebSearch：29 次**（前一輪為 0 次，前前一輪部分項目連續兩輪查無）。WebFetch / curl 依環境限制完全未使用，因此**所有事實均來自搜尋結果摘要，未讀原文全文**。

**本輪保留前一輪的內容**：第一原理推導出的兩條標度律（傳播延遲 ≈256 ns/mm；功率與耦合電容線性正比），以及共平面電容對聲程的對數關係。這些在第 3.2 節原樣保留，並在本輪找到部分實測交叉驗證。

**仍然查無的必查項目（誠實列出）**：
1. **Berkeley Boles 團隊隔離式壓電變壓器的隔離耐壓（kV）與一次／二次耦合電容（pF）——連續第三輪查無。** 搜尋 APEC 2025 論文、UC Berkeley 技轉頁 NCD 33842、Boles Lab 官網、ResearchGate 條目，四個來源的摘要**全部沒有提到 pF 或 kV**，只講效率、功率密度、magnetic-less。本輪新增的間接線索見 2.1。
2. **任何一家在賣「穿金屬壁供電＋傳資料」產品的公司——連續第三輪查無。** 本輪唯一新增的間接證據是 Design News 報導稱該技術「尚未商業化，但正被商業機構測試中」（未驗證，僅為搜尋摘要轉述）。
3. **穿壁技術「已放棄的具名計畫」或「募資後倒閉的新創」——查無。** 三輪皆無。
4. **ATEX/IECEx 對「聲學功率傳輸」的認證成本與時程數字——查無。** 但本輪查到一個關鍵的反向事實（見 2.4），改變了對這件事的判讀。
5. **Coilcraft HTX7045C 的額定功率（W）與售價——查無。** 官方頁面摘要只給電容與 hipot，不給功率與價格。
6. **Payton、Premo 的隔離變壓器具名規格——查無。** 搜尋不回傳這兩家的產品頁。
7. **SAW 隔離閘驅是否有新創公司——查無。** 只查到「Virginia Tech 已就此工作提出專利申請」（未驗證，搜尋摘要轉述，未取得申請號）。

**標註規則**：`【本輪查證】`＝本輪搜尋摘要直接支持；`【未驗證】`＝僅見於搜尋摘要、未讀原文、或來源歸屬不完全確定；`【本文推導】`＝從物理／算術導出；`【查無】`＝本輪確實搜尋過但沒有結果；`【轉引】`＝沿用本 repo 既有 dossier。

**本文件未出現任何我編造的專利號、論文標題、公司名、型號或實測數字。**

---

## 1. 結論摘要

1. **【本輪最重要・推翻前一輪的樂觀修正】「5 W ／ 12 kV 連續 ／ <1 pF」這個數字是真的，只是被前一輪錯誤地掛在 Coilcraft 名下。** 本輪查到它的實際出處是 **US11356015「Modular medium voltage fast chargers」**（DOE 資助案號 DE-EE0006521），該專利明述「a pulse transformer can generate 5 W output power with 12 kV continuous operating voltage and less than 1 pF primary-to-secondary coupling capacitance」，並說明降低電容的手段是「core 與 bobbin 之間的氣隙切斷經由磁芯的耦合路徑」［S6, S7］。**因此前一輪「商用磁性在 >4 kV 還沒佔住 sub-pF 高地、壓電還有空間」的結論必須撤回：非壓電方案在 12 kV 已經同時做到 5 W 與 <1 pF。**
2. **【本輪第二重要・徹底關門】在 27 kV 絕緣等級下，非壓電方案已做到 100 W ／ 2.78 pF ／ 92.78% 效率（48 V→48 V DC-DC，CLLC-CL 拓樸）**［S8, S9］。換算 **0.0278 pF/W**。對照 SAW 隔離閘驅的 **0.215 pF/W @ 2.75 kV**，磁性／電容耦合方案在**十倍的電壓等級下，pF/W 還好 7.7 倍**。**依前一輪推導的「功率與電容線性正比」標度律，聲學方案沒有任何一個角落在這個三維空間（功率 × 電容 × 耐壓）中是佔優的。**（來源歸屬須注意：該 27 kV 設計的論文標題含「ultra high voltage capacitive driving」，可能是電容耦合而非純磁耦合；但無論哪種，都是非壓電的競爭方案，結論不變。）【未驗證・歸屬待確認】
3. **【本輪第三重要・物理天花板首次量化】前一輪列為「最大未知數」的 SAW 衰減係數 α，本輪查到了：LiNbO₃ 在 GHz 頻段的 SAW 傳播損耗為 2.51–9.67 dB/mm**（400 nm 薄膜 SH0 模態 9.67 dB/mm、等效 Q＝712；LiNbO₃-on-sapphire 於 275 K 為 4.37 dB/mm、於 5 K 降到 3.5 dB/mm；YX-LiNbO₃/SiO₂/sapphire 於 830 MHz 為 2.51 dB/mm）［S10, S11, S12］。**代入論文的 1.25 mm 聲程：3.1–12 dB 的傳播損耗，即 51%–94% 的功率在路上就沒了。這正好解釋為什麼該元件的功率只有百毫瓦級。**把聲程拉到 10 kV 線性外推所需的 4.5 mm → **11–44 dB**；拉到爬電規範所需的 20–25 mm → **50–240 dB**。**中壓所需聲程在 GHz 頻段物理上不可能。**
4. **【本輪第四重要】降頻可以買到聲程，但買不到效率。** 1968 年 *Applied Physics Letters* 的經典 LiNbO₃ 延遲線（Y 切、Z 軸傳播、五對指叉電極）在 **100 MHz** 下達成 **8.9 µs 延遲、插入損耗 11.5 dB、−3 dB 頻寬 24 MHz**［S13］。以 YZ-LiNbO₃ 群速 3,488 m/s 反推，8.9 µs ≈ **31 mm 聲程**——**足以承載中壓爬電距離。但 11.5 dB 插入損耗 ＝ 只有 7% 的功率通過。** 而且同一批文獻明指「LiNbO₃ 的強熱彈阻尼使其在低頻的衰減比石英更嚴重」［S12］。**「長聲程（＝高耐壓）」與「高效率（＝可當電源）」在 LiNbO₃ 上互斥，這是材料層級的限制，不是設計問題。**
5. **【SAW 論文完整身分已查明】** 作者為 **Liyang Jin, Zichen Xi, Joseph G. Thomas, Jun Ji, Yuanzhi Zhang, Nuo Chen, Yizheng Zhu, Linbo Shao, Liyan Zhu**，主導者 **Linbo Shao（Virginia Tech ECE，Hybrid Nanoscale Systems Research Group）**［S1, S2, S3, S4］。**Virginia Tech 已就此工作提出專利申請（未驗證，未取得申請號）；查無任何新創公司或技轉授權動作。** 前一輪標為「作者歸屬有內部矛盾（16 號寫 Jin et al.）」——**16 號是對的**，第一作者確為 Liyang Jin。
6. **【Boles 團隊・第三輪查無，但有間接答案】** 本輪查到**壓電變壓器的一般性物理常數**：PT 的一次／二次寄生耦合電容**約 1 pF**、崩潰電壓**約 5 kV**［S14］【未驗證，來源為搜尋摘要對 EP3127172B1 及相關文獻的綜述，未讀原文】。**若這個量級對隔離式 PT 普遍成立，則 Boles 團隊的隔離式 PT 是「無磁」而非「低電容」——它的 pF 與磁性方案同級，而耐壓只有磁性方案的 1/2 到 1/5。** 這與前一輪「論文標題只強調效率與 magnetic-less、不強調低電容」的弱推論方向一致。另查到該工作已延伸為 **IEEE TPEL 2026 期刊版**，以及 **COMPEL 2025 的「a new class of topologies for isolated piezoelectric-based power conversion」**［S18］。
7. **【穿壁的功率數字本輪收斂，且比既有 dossier 更高】** 本輪查到多個實測點：3 mm 鋁板、1 MHz 下 **83% AC-AC 效率**，DC-DC 峰值 **68% ＠ 17.5 W**；用商用元件達成 **17.37 Mbps ＋ 50 W**；實驗室通道 **>70% 效率、>100 W 送入假負載**；特殊換能器幾何在薄金屬壁上 **>1 kW**［S15, S16, S17］。**前一輪標為「50 W 與 32.5 W 未收斂」的矛盾，本輪偏向支持 50 W 這一版（且資料率是 17.37 Mbps 而非 12.4 Mbps）。技術能力沒有問題——問題從來就不在技術。**
8. **【ATEX 判讀反轉】前一輪把 ATEX/IECEx 列為「認證路徑不確定、成本無法估算」的門檻。本輪查到反例：本質安全（intrinsically safe）超音波感測器已有現成的 ATEX/IECEx/ANZEx 認證商品**（例如 Migatron `RPS-409A-IS2`、`RPS-429A-IS`，配合認證的本安柵欄可用於 Zone 0/1/2 與 20/21/22）［S19, S20］。**但這個反例同時也是新的壞消息：本質安全的定義就是「限制可用於點火的電能與熱能」，一顆 mW 級感測器可以本安，一條 17.5–50 W 的聲學功率鏈路在定義上就不可能本安，只能走隔爆（Ex d）或其他保護型式。** 換言之：認證路徑存在，但**穿壁供電這個應用剛好落在本安路徑之外**。
9. **【耦合劑・本輪取得機制級證據】** 液態耦合劑會「乾掉、滲漏、從感測器底下流失」，且介面會因蒸發或化學／物理變化而隨時間改變傳導能力；**更關鍵的是：作為替代方案的黏著劑鍵合「失效率高，因鍵合層隨時間劣化與斷裂，且超音波感測器本身輸入的能量可能加劇此一過程」**［S21, S22］。**「元件自己的振動能量會破壞自己的耦合層」是一個自我拆解型的失效機制，比單純的乾涸嚴重得多。實測壽命數據仍查無。**
10. **【對決策的一句話】在隔離領域，壓電／聲學的立足點存在但極窄，而且不在中壓。** 詳見第 4 節的窗口圖。**任何以「中壓 SiC 閘驅隔離電源」為題的投入案，本輪證據足以否決。**

---

## 2. 查證結果

### 2.1 Berkeley Boles 隔離式壓電變壓器：連續第三輪查無 pF 與 kV

本輪搜尋四個獨立入口，全部沒有隔離耐壓與耦合電容：
- **APEC 2025 論文正式書目已確認**：S. Naval, W. Xu, M. Touhami, J. D. Boles, *High-Efficiency Isolated Piezoelectric Transformers for Magnetic-less DC-DC Power Conversion*, 2025 IEEE APEC, **pp. 1012–1019**［S5］。**（頁碼為本輪新增的查證細節。）**
- **UC Berkeley 技轉頁 NCD 33842** 的摘要說明：非隔離型單埠壓電諧振器已達 **功率級效率 99%、壓電諧振器功率處理密度達 5.7 kW/cm³**，多埠 PT 則「提供同樣優勢並擴展到更廣的應用」——**全文不提 pF 與 kV**［S23］。
- Boles Lab 官網、ResearchGate 條目同樣不提。ResearchGate 摘要重申「相較先前的隔離式 magnetic-less PT DC-DC 設計，損耗比降低 17×」［S24］。
- **本輪新增線索**：該工作已延伸為 **IEEE Transactions on Power Electronics 2026** 期刊版；同團隊另在 **IEEE COMPEL 2025** 發表「a new class of topologies for isolated piezoelectric-based power conversion」［S18］。**這代表這條路線仍在推進，但持續三年不公布隔離規格，強烈暗示隔離規格不是賣點。**

**間接答案**：一般性 PT 的一次／二次寄生耦合電容 **~1 pF**、崩潰電壓 **~5 kV**［S14］【未驗證】。同一份摘要另給一組實驗值：PT 輸入電容 200 pF、輸出電容 220 pF（此為各埠對地電容，非跨障壁電容，勿混用）。

**判讀**：若 ~1 pF / ~5 kV 成立，隔離式 PT 相對於 US11356015 的 5 W/12 kV/<1 pF 沒有優勢；它的賣點只剩「無磁芯、無繞線、可平面化」。

### 2.2 SAW 隔離閘驅（*Communications Engineering* 2026）：身分與數字全部確認

- **正式版**：https://www.nature.com/articles/s44172-026-00681-w（2026 年 5 月刊出）；預印本 arXiv:2511.13412［S1, S2］。
- **作者**：Liyang Jin, Zichen Xi, Joseph G. Thomas, Jun Ji, Yuanzhi Zhang, Nuo Chen, Yizheng Zhu, Linbo Shao, Liyan Zhu［S3］。
- **機構**：Virginia Tech ECE / 物理系，Linbo Shao 的 Hybrid Nanoscale Systems Research Group［S4, S25］。該組的定位是「LiNbO₃、鑽石等平台上的混合古典／量子多物理系統，用於訊號處理、感測、量子資訊」——**閘驅是這個組的外溢應用，不是主業。這對「後續是否會有人推進到中壓」是負面訊號。**
- **數字全部重新確認**：2.75 kV 隔離、**0.032 pF** 隔離電容、**1.25 mm** 機械傳播長度、13.4 V 開路電壓、44.4 mA 短路電流、驅動 GaN HEMT 導通時間 **108.8 ns**、已在降壓轉換器驗證、工作溫度 **0.5 K（−272.6 °C）至 544 K（271 °C）**、宣稱固有 EMI 免疫與多半導體平台異質整合潛力［S1, S2］。
- **商業化**：Virginia Tech 已提專利申請【未驗證】；**查無新創、查無授權、查無產業合作對象。**

**【本文推導】功率上限**：由 V_oc × I_sc / 4 ＝ 13.4 × 0.0444 / 4 ＝ **149 mW**，這是最大功率傳輸定理下的**上界**，實際可用功率更低。所有以 150 mW 為基準的外推都應理解為樂觀值。

### 2.3 磁性／非壓電方案的真實極限（本輪最重要的更正）

| 方案 | 功率 | 跨障壁電容 | 耐壓 | **pF/W** | 來源 |
|---|---|---|---|---|---|
| SAW 隔離閘驅（Jin et al.） | 0.149 W【推導】 | **0.032 pF** | 2.75 kV | **0.215** | S1, S2 |
| Coilcraft `HTX7045C` | 查無 | 0.7 pF | 2800 Vrms / 4000 VDC | — | S26 |
| **US11356015 脈衝變壓器** | **5 W** | **<1 pF** | **12 kV 連續** | **<0.2** | **S6, S7** |
| CPES 中壓 IAPS | 2.5 W | 1.03 pF | PDIV >15 kV rms | 0.412 | S27, S28 |
| **SST 輔助電源（CLLC-CL）** | **100 W** | **2.78 pF** | **27 kV** | **0.0278** | **S8, S9** |
| PCB 無芯變壓器 | 查無 | 5.85 pF | >10 kV rms | — | S28 |
| 4 mm 氣隙鬆耦合變壓器 | 查無 | 1.6 pF | 查無 | — | S29 |
| 某拓樸族 | 查無 | <10 pF | **>40 kV** | — | S29 |
| 閘驅原型（50 MHz） | 查無 | 3.4 pF @50 MHz、13 pF @100 MHz | >100 kV DC | — | S28 |

**結論**：**pF/W 這個品質因數上，非壓電方案的最佳值（0.0278 @ 27 kV）比 SAW（0.215 @ 2.75 kV）好 7.7 倍，而且是在 10 倍的電壓等級上達成的。前一輪推導的「電壓越高、聲學相對優勢越大」這條假說，被實測數據否證了——磁性／電容耦合方案的 pF/W 並沒有隨耐壓劣化到聲學可以趁虛而入的程度。**

**CPES 中壓 IAPS 的其他細節（本輪新增）**：外形 **61 × 24 × 30 mm**；60 Hz AC 下 PDIV >13.5 kV RMS；在 100 kHz、5 kV PWM、**dv/dt = 100 V/ns** 下無局部放電；宣稱「免除光纖與笨重閘驅電源，相較傳統 10 kV 隔離閘驅體積縮小 10 倍以上，並有整合進 MV SiC 封裝的潛力」［S27, S30］。**這就是聲學方案在中壓要正面對決的對手，而且它已經是工程完成品。**

### 2.4 穿金屬壁：技術早已達標，未商品化的原因不是技術

**技術面（本輪查到的實測點）**：
- 3 mm 鋁板、1 MHz：**83% AC-AC 效率**；DC-DC 峰值 **68% ＠ 17.5 W**［S15］。
- 商用元件系統：**17.37 Mbps ＋ 50 W**［S16］。
- 實驗室通道：**>70% 效率、>100 W** 送入假負載；特殊換能器幾何在薄金屬壁上 **>1 kW**［S17］。

**未商品化原因（本輪查到的具體障礙，全部來自 2015 年 *Sensors* 綜述及相關文獻）**［S17］：
1. **對準敏感度**：「換能器對準對通道能力有顯著影響，即使少量偏移也會使功率傳輸效率大幅下降」——這是部署現場的致命傷，因為現場沒有實驗室的對準夾具。
2. **材料參數依賴**：模型精度完全依賴通道各部件的準確參數；當材料與零件參數不明時「建模方法無能為力」。對「既有設備事後加裝」的商業模式（＝最大的市場）尤其致命，因為既有壓力容器的壁厚、材質、內部襯裡往往無文件可查。
3. **知識缺口**：超音波能量的非熱效應貢獻仍是「商業化的瓶頸之一」。
4. **應用面窄**：綜述自陳這項技術「適用於介質導電、厚度可觀、且結構完整性關鍵的場合」——**這句話本身就界定了一個非消費、非量產的小眾市場。**

**耦合劑（本輪取得機制級證據）**［S21, S22］：
- 傳統液態耦合劑「乾掉、滲漏、從感測器底下流失，造成訊號問題，只能提供暫時或短期的聲學傳導」。
- UT 換能器與表面的接觸介面「會因蒸發或其他化學／物理變化而隨時間改變」。
- **黏著劑鍵合作為替代方案「失效率高，因鍵合劣化與斷裂，且可能由超音波感測器本身輸入的能量所加劇」。**
- 已有號稱長效的產品（乙二醇基、矽基；某些配方宣稱數月至數年不乾不流失），但**具體壽命實測數據仍查無**。

**現況與資金**：
- **美國陸軍 ARL 合作協議 W911NF2220007** 確認存在，資助 arXiv:2607.13797「Experimental Characterization and Prediction of Radial and Thickness Mode Power Transfer Capability in Through-Metal Acoustic Power Transfer」，該文自陳 TM-APT 的目標功率「often targeting hundreds of watts」［S31, S32］。**預算金額查無。**
- **EPRI Extended Storage Collaboration Program (ESCP)** 涵蓋「檢測、監測與感測器」，並與大學合作［S33]。
- **NEUP CFA-21-24261「Internal Wireless Sensors for Dry Cask Storage」，PI: Dr. Travis W. Knight（University of South Carolina）**，DOE-ID NEPA CX 編號 DOE-ID-21-098［S34, S35］。**注意：該案的技術路線是「裝填時就把無線感測器放進去」＋輻射屏蔽，並非穿壁聲學鏈路——這是穿壁方案的直接競爭路線，且更簡單。**
- **PNNL 全尺寸乏燃料罐 mock-up 非侵入式超音波感測**［轉引 S36］。
- **商業產品：查無（連續第三輪）。**

### 2.5 電外科漏電流：痛點與門檻數字確認

Ethicon Endo-Surgery 專利族（US10263171、US9039695、US12408967 等）明述［S37, S38, S39］：
- 隔離變壓器的**雜散電容使電氣隔離不完全**，一次側電位影響二次側電位，造成病人漏電流。
- 在電外科的高頻（**500 kHz – 1 MHz**）下，對地雜散電容提供另一條接地參考路徑。
- 漏電流可用「二次側對地的洩漏電容」被動降低，但「**感應漏電流可能超出被動洩漏電容把它壓在 10 µA 以下的能力**」，故需主動抵消。
- 更早的先例：**US3946738A**（以串聯 LC 並聯於雜散電容加以抵消）、**US4437464A**。

**【本文推導】**：**10 µA** 是明確的門檻數字。以 500 kHz / 3 kV 計，I ＝ 2πfCV，要把漏電流壓到 10 µA 需要 **C < 1.06 fF**。**即使 SAW 的 0.032 pF（＝32 fF）也超標 30 倍。** 前一輪認為「0.032 pF ⇒ 0.24 mA，是數量級對得上的醫療切入點」——**本輪修正：對得上的是「從 mA 降到亞 mA」，但離法規門檻的 10 µA 仍差 30 倍，所以主動抵消電路仍然省不掉。這個機會應調降。**

### 2.6 井下與密封無穿線致動器

- **US9500074「Acoustic coupling of electrical power and data between downhole devices」**：以壓電陶瓷疊層在井下管柱壁上收發應力波，把接收到的聲波轉成電訊號，用以驅動井下感測器或流體控制系統［S40］。**這是「穿壁供電驅動井下裝置」最接近具名的既有專利。**
- 其他：US8416098（井下工具聲學通訊）、US20110192222A1（井下用壓電致動器）［S41, S42］。
- 密封壓電致動器本身是成熟商品：「充惰性氣體的氣密封裝版本可用於嚴苛環境；不鏽鋼外殼封裝提升陶瓷致動器堅固性」；壓電疊層致動器已用於 **200 °C** 級井下即時感測與資料通訊［S43］。
- **「完全無電氣穿線的密封馬達」作為一個具名商品或計畫：查無。**

---

## 3. 關鍵數字表

### 3.1 本輪查證與更正

| 項目 | 數字 | 狀態 | 來源 |
|---|---|---|---|
| **磁性 12 kV 級極限** | **5 W / <1 pF / 12 kV 連續**（脈衝變壓器，氣隙切斷磁芯耦合路徑） | 【本輪查證・更正前一輪】 | S6, S7 |
| **磁性/電容 27 kV 級極限** | **100 W / 2.78 pF / 27 kV / 92.78%**（48→48 V，CLLC-CL） | 【本輪查證・歸屬待確認】 | S8, S9 |
| CPES 中壓 IAPS | 2.5 W / 1.03 pF / PDIV >15 kV rms / 61×24×30 mm / dv/dt 100 V/ns 無 PD | 【本輪查證】 | S27, S30 |
| 磁性 >40 kV 級 | 絕緣 >40 kV、耦合電容 <10 pF | 【本輪查證】 | S29 |
| 磁性 >100 kV DC 級 | 3.4 pF @50 MHz、13 pF @100 MHz | 【本輪查證】 | S28 |
| Coilcraft `HTX7045C` | 0.7 pF；2800 Vrms / 4000 VDC（1 min hipot）；匝比 A~F（1:1 至 2.5:1）；chip-style | 【本輪查證】 | S26 |
| **LiNbO₃ SAW 傳播損耗 @GHz** | **9.67 dB/mm**（400 nm 薄膜 SH0，Q＝712）；**4.37 dB/mm**（on sapphire, 275 K）；**3.5 dB/mm**（5 K）；**2.51 dB/mm**（830 MHz, YX/SiO₂/sapphire） | 【本輪查證】 | S10, S11, S12 |
| **LiNbO₃ 延遲線 @100 MHz** | **8.9 µs 延遲、11.5 dB 插入損耗、−3 dB 頻寬 24 MHz**（Y 切 Z 傳播、5 對指叉） | 【本輪查證】 | S13 |
| LiNbO₃ 低頻特性 | 強熱彈阻尼 ⇒ 低頻衰減比石英更嚴重 | 【本輪查證】 | S12 |
| SAW 隔離閘驅 | 0.032 pF / 2.75 kV / 1.25 mm / 13.4 V / 44.4 mA / 108.8 ns / 0.5–544 K | 【本輪查證】 | S1, S2 |
| SAW 隔離閘驅功率 | **149 mW（上界）** | 【本文推導】 | — |
| PT 一般寄生耦合電容 | **~1 pF**；崩潰電壓 **~5 kV** | 【未驗證】 | S14 |
| 穿壁最佳實測 | 83% AC-AC（3 mm 鋁 @1 MHz）；68% DC-DC @17.5 W；17.37 Mbps ＋ 50 W；>100 W；薄壁 >1 kW | 【本輪查證】 | S15, S16, S17 |
| 電外科漏電流法規門檻 | **10 µA**；工作頻率 500 kHz–1 MHz | 【本輪查證】 | S37 |
| 達成 10 µA 所需電容 | **<1.06 fF**（@500 kHz / 3 kV） | 【本文推導】 | — |
| 本安超音波感測器 | ATEX/IECEx/ANZEx 認證商品存在（Migatron RPS-409A-IS2/RPS-429A-IS，Zone 0/1/2、20/21/22） | 【本輪查證】 | S19, S20 |

### 3.2 標度律（前一輪推導，保留；本輪加註實測交叉驗證）

**(a) 耦合電容 vs 聲程 S**（共平面電極保角映射，W ＝ 0.1 mm）：$C' \propto 1/(\ln 2 + \tfrac12\ln(S/W))$

| 聲程 S | 相對電容 | 由 0.032 pF 外推 |
|---|---|---|
| 1.25 mm（基準） | 1.00 | 0.032 pF |
| 5 mm | 0.74 | 0.024 pF |
| 10 mm | 0.65 | 0.021 pF |
| 20 mm | 0.585 | 0.019 pF |
| 40 mm | 0.53 | 0.017 pF |

→ 32 倍聲程只換到 1.9 倍電容下降。**【本輪新增判讀】既然電容對聲程不敏感，而聲程對衰減極度敏感（見 (c')），拉長聲程是純虧本的操作。**

**(b) 耐壓 vs 聲程**：實測點 2.75 kV / 1.25 mm ＝ **2.2 kV/mm**。
- 線性外推（樂觀）：10 kV → 4.5 mm；20 kV → 9.1 mm。
- IEC 60664 級爬電慣例（約 2–2.5 mm/kV，空氣、污染度 2）：10 kV → 20–25 mm；20 kV → 40–50 mm。
- **警語保留**：2.2 kV/mm 比爬電規範激進 4–5 倍，強烈暗示 2.75 kV 是短時 hipot 而非可認證的持續耐壓。

**(c) 傳播延遲 vs 聲程**（v ≈ 3,900 m/s）：**≈256 ns/mm**

| 聲程 | 單向延遲 |
|---|---|
| 0.4 mm | ≈100 ns（＝商用閘驅延遲預算上限） |
| 1.25 mm | 320 ns |
| 4.5 mm | 1.15 µs |
| 10 mm | 2.6 µs |
| 20 mm | 5.1 µs |
| 50 mm | 12.8 µs |

**【本輪交叉驗證】** S13 的 100 MHz 延遲線實測 8.9 µs；以 YZ-LiNbO₃ 群速 3,488 m/s 反推聲程約 **31 mm**，與本標度律一致【本文推導】。**⇒ 256 ns/mm 成立，>0.4 mm 聲程不可能作為 PWM 訊號路徑的結論維持。**

**(c') 【本輪新增】傳播損耗 vs 聲程 vs 頻率**（實測 α 代入）

| 聲程 | @GHz 最佳 α＝2.51 dB/mm | @GHz 最差 α＝9.67 dB/mm | 功率通過率（最佳 / 最差） |
|---|---|---|---|
| 1.25 mm | 3.1 dB | 12.1 dB | 49% / 6% |
| 4.5 mm（10 kV 樂觀） | 11.3 dB | 43.5 dB | 7.4% / 0.004% |
| 10 mm | 25.1 dB | 96.7 dB | 0.31% / ~0 |
| 20 mm（10 kV 保守） | 50.2 dB | 193 dB | 0.001% / ~0 |

→ **這張表是本輪最有殺傷力的內容。在 GHz 頻段，中壓所需的聲程對應 11–193 dB 的損耗，物理上不可能做電源。**
→ 降到 100 MHz 可換到 31 mm 聲程（S13 實測），但總插入損耗 11.5 dB ＝ **只有 7% 功率通過**，且頻寬掉到 24 MHz（−3 dB）。**「聲程 × 效率」的乘積是被材料鎖死的。**

**(d) 功率 vs 電容（線性取捨）**：$P \propto W_a$，$C_{iso} \propto W_a$ ⇒ $C_{iso} \propto P$

| 目標功率 | SAW 外推電容 | 對照（本輪查證的非壓電最佳） |
|---|---|---|
| 0.149 W（基準） | 0.032 pF @2.75 kV | — |
| 1 W | 0.21 pF @2.75 kV | **US11356015：5 W / <1 pF / 12 kV** |
| 2.5 W | 0.54 pF @2.75 kV | CPES：1.03 pF @>15 kV PDIV |
| 5 W | 1.07 pF @2.75 kV | **US11356015 在 12 kV 已優於此** |
| 100 W | 21.5 pF @2.75 kV | **SST APS：2.78 pF @27 kV（好 7.7 倍、電壓高 10 倍）** |

**pF/W 排名（越小越好）**：SST APS **0.0278**（27 kV）＜ US11356015 **<0.2**（12 kV）＜ SAW **0.215**（2.75 kV）＜ CPES **0.412**（>15 kV PDIV）。

**(e) 位移電流**（I ＝ C·dv/dt @100 kV/µs）：10 pF → 1 A；2.78 pF → 278 mA；1 pF → 100 mA；0.032 pF → 3.2 mA。
**(f) 電外科漏電流**（I ＝ 2πfCV @500 kHz / 3 kV）：10 pF → 94 mA；1 pF → 9.4 mA；0.032 pF → **0.30 mA**；**法規門檻 10 µA 需 <1.06 fF**。

---

## 4. 明確回答：在隔離領域，壓電／聲學到底有沒有立足點？

**有，但窗口比前一輪判斷的小一個數量級，而且不在中壓。**

### 4.1 三個維度上，聲學各在哪裡被關門

| 維度 | 聲學做得到 | 非壓電方案做得到 | 判定 |
|---|---|---|---|
| **pF/W** | 0.215（@2.75 kV） | **0.0278（@27 kV）** | **輸 7.7 倍，且對手電壓高 10 倍** |
| **絕對功率** | 149 mW（實測上界） | **100 W**（單模組） | **輸 3 個數量級** |
| **絕對耐壓** | 2.75 kV（可能是短時 hipot） | **27 kV 絕緣 / >40 kV（另一族）** | **輸 1 個數量級** |
| **傳播延遲** | 320 ns @1.25 mm | ~90 ns（Infineon 1ED3124） | **輸 3.5 倍，且隨聲程線性惡化** |
| **可承受聲程** | GHz：≤1.25 mm；100 MHz：~31 mm 但只剩 7% 功率 | 不適用 | **材料鎖死** |
| **工作溫度下限** | **0.5 K** | 鐵氧體在深冷下磁導率崩潰；無芯方案體積大、電容高 | **贏** |
| **工作溫度上限** | **544 K（271 °C）** | 鐵氧體居里點約 200–250 °C | **贏** |
| **磁場環境** | 無磁材料 | 需鐵氧體或大體積無芯 | **贏（MRI）** |
| **晶片級整合** | 單晶片、可異質整合 | 12 kV 脈衝變壓器與 27 kV APS 皆為 cm 級離散件（61×24×30 mm） | **贏** |
| **EMI** | 宣稱固有免疫 | 需屏蔽設計 | **可能贏，未量化** |

### 4.2 那個窗口的形狀

**窗口 ＝ 「功率 ≤ 0.15 W（樂觀 ≤0.5 W）」×「電壓 ≤ 3 kV」×「聲程 ≤ 1.5 mm」×「環境本身排除磁性材料」**

具體來說，只剩三塊：

- **★★★☆☆ 深冷電子（<77 K，尤其 <4 K）的隔離偏壓與遙測。** 0.5 K 實測是本輪唯一沒被關門的差異化能力。應用面：超導量子計算的低溫控制電子、超導磁體保護、深冷功率電子。**功率需求本來就是 mW 級，剛好落在窗口內。**
- **★★★☆☆ 強磁場環境（MRI 梯度放大器、磁約束裝置）的隔離偏壓。** 無磁材料是硬需求，且既有專利佈局（US11777487 / US12206394 無芯變壓器、US11796613 光隔離只能傳訊號不能傳功率）證明產業有此缺口。**功率需求同樣是驅動級 mW–數百 mW。**
- **★★☆☆☆ >200 °C 的隔離感測／遙測。** 544 K 上限打敗鐵氧體。但注意：LiNbO₃ 在 400 °C 只有 10 天壽命（轉引 18 號），實際可用區間是 200–300 °C，且與台灣既有 PZT 產線無共通性。

**明確排除**：
- **✗ 中壓（≥10 kV）SiC/GaN 閘驅隔離電源**——被 4.1 的三個維度同時關門，且 (c') 的傳播損耗表證明物理上做不到。**這是本輪最重要的否決。**
- **✗ 1200 V 級隔離閘驅**——前一輪已排除，本輪的 pF/W 對照再次確認。
- **✗ 電外科主 RF 路徑**——功率差 3 個數量級。
- **△ 電外科輔助路徑**——降級。0.032 pF 距離 10 µA 法規門檻所需的 1.06 fF 仍差 30 倍，主動抵消電路省不掉。
- **△ 穿金屬壁**——技術面已達標（>1 kW 曾驗證），但障礙是對準敏感度、既有設備參數不可知、耦合層的自我拆解型失效、市場本質為小眾。**且 50 W 級聲學鏈路在定義上不可能取得本質安全認證。**

### 4.3 對投入決策的一句話

**如果客戶的題目是「壓電做隔離元件」，那麼唯一值得投入的版本是「晶片級、mW 級、極端環境（深冷／高溫／無磁）的隔離偏壓＋遙測」，而不是任何形式的中壓電力電子。前者的市場規模與台灣既有 PZT 產線的關聯度都很低（必須走 LiNbO₃／AlN），這件事本身就應該進入投資決策。**

---

## 5. 反面證據與物理上限

1. **【本輪最強】非壓電方案在 12 kV 已達 5 W / <1 pF，在 27 kV 已達 100 W / 2.78 pF。** 前一輪基於「Coilcraft 只有 2800 Vrms」而重開的中壓機會之窗，本輪確認應該關閉。［S6, S7, S8, S9］
2. **【本輪第二強】LiNbO₃ 的 SAW 傳播損耗在 GHz 為 2.51–9.67 dB/mm。** 前一輪列為「最大未知數」的 α，答案是**壞消息**：1.25 mm 就已經是實用極限，中壓所需聲程對應 11–193 dB。［S10, S11, S12］
3. **降頻救不了。** 100 MHz 可換到 31 mm 聲程，但插入損耗 11.5 dB（7% 通過率）、頻寬只剩 24 MHz；且 LiNbO₃ 的強熱彈阻尼使低頻衰減比石英更嚴重。**「長聲程 × 高效率」是材料層級的互斥。**［S12, S13］
4. **電外科的法規門檻是 10 µA，需 <1.06 fF，SAW 的 0.032 pF 仍超標 30 倍。** 前一輪把這個機會評為「痛點有名有姓、數量級對得上」——本輪修正為「數量級仍差 30 倍，主動抵消電路省不掉」。【本文推導 ＋ S37】
5. **PT 的一般性寄生耦合電容約 1 pF、崩潰約 5 kV。** 若成立，Boles 團隊的隔離式 PT 相對於磁性方案沒有電容或耐壓優勢。［S14】【未驗證】
6. **Boles 團隊連續三年（APEC 2025 → COMPEL 2025 → TPEL 2026）不公布隔離規格。** 一個以「隔離」為標題的工作三年不講耐壓與耦合電容，最合理的解釋是那不是賣點。【本文推導，弱推論】
7. **Shao 組的主業是量子／訊號處理，閘驅是外溢應用。** 沒有新創、沒有授權、沒有產業合作。**推進到中壓的可能性低。**［S4, S25］
8. **穿壁的四個具體障礙全部是「部署」而非「技術」問題**：對準敏感度、既有設備材料參數不可知、非熱效應知識缺口、市場本質小眾。技術面早在 2013–2015 年就達成 >100 W 與 Mbps 級。**問題從來不在能不能做。**［S17］
9. **耦合層有自我拆解型失效機制**：黏著劑鍵合失效率高，且「可能由超音波感測器本身輸入的能量所加劇」。**元件自己的振動會破壞自己的耦合層。**［S22］
10. **本質安全路徑對穿壁供電關閉。** ATEX/IECEx 的本安認證商品存在（mW 級感測器），但本安的定義就是限制可用能量；17.5–50 W 的聲學功率鏈路只能走隔爆或其他保護型式，成本與時程不可估。［S19, S20】【本文推導】
11. **乾儲罐監測有更簡單的競爭路線**：NEUP CFA-21-24261（USC, PI Travis W. Knight）走的是「裝填時放入無線感測器＋輻射屏蔽」，完全不需要穿壁聲學鏈路。**需求存在不代表穿壁是解法。**［S34, S35］
12. **Avago/Broadcom 的 FBAR 聲學隔離（US7525398）20 年未成主流**，同族還有 US7514844、US7586392。一家有 FBAR 量產能力且本身賣隔離器的公司都做不起來。［S44, S45, S46］
13. **本輪自身的限制**：全部事實來自搜尋摘要，未讀任何原文。特別是 27 kV / 2.78 pF / 100 W 這個對結論最關鍵的數字，其來源歸屬（磁耦合 vs 電容耦合）本輪未能完全確認。**若該數字實為電容耦合方案，則「磁性」的極限應退回 US11356015 的 5 W / 12 kV / <1 pF——但那仍然足以否決中壓聲學機會。**

---

## 6. 未解問題

1. **【仍是最高優先・第三輪查無】Boles 團隊隔離式 PT 的耐壓與耦合電容。** 建議查法改變：直接取得 IEEE TPEL 2026 期刊版全文（比 APEC 會議版更可能有完整規格表），或直接寫信給 UC Berkeley 技轉辦公室詢問 NCD 33842 的 datasheet。
2. **27 kV / 2.78 pF / 100 W 的 SST 輔助電源，究竟是磁耦合還是電容耦合？** 這決定「磁性方案的真正極限在哪」。若是電容耦合，則值得單獨評估「電容耦合 vs 聲學耦合」的對決——**這條軸線本 repo 完全沒查過，可能是被忽略的真正對手。**
3. **AlN 與鑭鎵矽酸鹽（langasite）的 α(f) 是多少？** LiNbO₃ 被本輪的衰減數據否決了長聲程路線，但 AlN（本輪查到 arXiv:2603.19409「Single-Crystal AlN Wafer-Based Bulk Acoustic Resonators for Piezoelectric Power Conversion」）與 langasite 的衰減特性未查。**若某材料在 VHF 有顯著較低的 α，中壓窗口可能重開——但這是低機率的翻盤條件。**
4. **2.75 kV 是短時 hipot 還是可認證的持續耐壓？PDIV 是多少？** 對照組 CPES IAPS 的 PDIV >15 kV rms 是明確標示的；SAW 論文查無 PDIV。**若 SAW 的 2.75 kV 只是 1 分鐘 hipot，則實際可用電壓還要再打折。**
5. **深冷（<4 K）隔離電源的市場規模與現有解法為何？** 本輪判定這是聲學唯一沒被關門的窗口，但完全沒查過該市場的規模、現有供應商、單價與量。**這應該是下一輪的第一優先。**
6. **穿壁技術有沒有人真的嘗試過商業化？** 第三輪仍查無失敗個案。**「找不到失敗案例」＋「技術早在 2013 年就達標」＋「軍方仍在出錢」這三件事並存，最合理的解讀是：這是一個永遠停在政府研發合約階段的技術，沒有人相信它能成為產品。這對投入決策是比「試過失敗」更差的訊號。**

---

## 7. 來源清單

1. **S1** — Microwave-acoustic-based isolated gate driver for power electronics, *Communications Engineering*（2026 年 5 月）— https://www.nature.com/articles/s44172-026-00681-w — SAW 隔離閘驅正式期刊版；0.032 pF / 2.75 kV / 1.25 mm / 13.4 V / 44.4 mA / 108.8 ns / 0.5–544 K。
2. **S2** — 同上，arXiv 預印本 2511.13412 — https://arxiv.org/pdf/2511.13412 — 全文 PDF。
3. **S3** — arXiv:2511.13412 作者列表 — https://arxiv.org/pdf/2511.13412 — Liyang Jin, Zichen Xi, Joseph G. Thomas, Jun Ji, Yuanzhi Zhang, Nuo Chen, Yizheng Zhu, Linbo Shao, Liyan Zhu。
4. **S4** — Hybrid Nanoscale Systems Research Group, Virginia Tech ECE（Linbo Shao）— https://shaogroup.ece.vt.edu/ — 主導團隊；主業為 LiNbO₃／鑽石平台的量子與訊號處理。
5. **S5** — S. Naval, W. Xu, M. Touhami, J. D. Boles, *High-Efficiency Isolated Piezoelectric Transformers for Magnetic-less DC-DC Power Conversion*, 2025 IEEE APEC, pp. 1012–1019 — https://www.researchgate.net/publication/391376205_High-Efficiency_Isolated_Piezoelectric_Transformers_for_Magnetic-less_DC-DC_Power_Conversion — **摘要不含 pF 與 kV（第三輪查無）。**
6. **S6** — US11356015「Modular medium voltage fast chargers」— https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/11356015 — **「脈衝變壓器可產生 5 W 輸出、12 kV 連續工作電壓、一次-二次耦合電容 <1 pF」；DOE 資助 DE-EE0006521。本輪最關鍵的更正來源。**
7. **S7** — US11356015 書目頁（TREA）— https://trea.com/information/modular-medium-voltage-fast-chargers/patentgrant/25a64f52-db69-45a7-8332-3342da202956 — 同上專利之申請與優先權資訊（2018/05/05 申請，優先權 62/504,247）。
8. **S8** — Auxiliary power supply for solid state transformer with ultra high voltage capacitive driving — https://www.researchgate.net/publication/282374727_Auxiliary_power_supply_for_solid_state_transformer_with_ultra_high_voltage_capacitive_driving — **100 W / 2.78 pF / 27 kV 絕緣 / 92.78% 效率（48→48 V，CLLC-CL）。歸屬（磁 vs 電容耦合）待確認。**
9. **S9** — Auxiliary Power Supply for Medium-/High-Voltage and High-Power Solid-State Transformers — https://www.researchgate.net/publication/335864169_Auxiliary_Power_Supply_for_Medium-High-Voltage_and_High-Power_Solid-State_Transformers — 同一研究線的後續。
10. **S10** — Acoustic Loss in Thin-Film Lithium Niobate: An Experimental Study — https://www.researchgate.net/publication/352911885_Acoustic_Loss_in_Thin-Film_Lithium_Niobate_An_Experimental_Study — **400 nm 薄膜 SH0 於 GHz 傳播損耗 9.67 dB/mm、等效 Q＝712。**
11. **S11** — Cryogenic Characterization of Low-Loss Thin-film Lithium Niobate on Sapphire Shear Horizontal Surface Acoustic Wave Devices — https://pubmed.ncbi.nlm.nih.gov/40030408/ — **275 K 為 4.37 dB/mm、5 K 為 3.5 dB/mm。**
12. **S12** — Low Propagation Loss Acoustic Delay Lines based on YX-LiNbO₃/SiO₂/Sapphire, IEEE — https://ieeexplore.ieee.org/document/10307572/ — **830 MHz 下 2.51 dB/mm；另註 LiNbO₃ 強熱彈阻尼使低頻衰減比石英嚴重。**
13. **S13** — High-Performance Lithium Niobate Acoustic Surface Wave Transducers and Delay Lines, *Applied Physics Letters* 13(9), 312 — https://pubs.aip.org/aip/apl/article/13/9/312/41334/HIGH-PERFORMANCE-LITHIUM-NIOBATE-ACOUSTIC-SURFACE — **100 MHz、Y 切 Z 傳播、5 對指叉：8.9 µs 延遲、11.5 dB 插入損耗、−3 dB 頻寬 24 MHz。本輪「降頻換聲程」定量依據。**
14. **S14** — EP3127172B1「Galvanic isolated piezoelectric transformer based voltage sensors」（QorTek）— https://patents.google.com/patent/EP3127172B1/en — **PT 一次／二次寄生耦合電容 ~1 pF、崩潰電壓 ~5 kV【未驗證，摘要轉述】；QorTek 專利公告頁 https://qortek.com/news/patent-announcement-galvanic-isolated-based-voltage-sensors/**
15. **S15** — An Ultrasonic Through-Metal-Wall Power Transfer System with Regulated DC Output, *Applied Sciences* 8(5), 692 — https://www.mdpi.com/2076-3417/8/5/692 — **3 mm 鋁板 @1 MHz：83% AC-AC；DC-DC 峰值 68% @17.5 W。**
16. **S16** — A high-performance ultrasonic system for the simultaneous transmission of data and power through solid metal barriers — https://pubmed.ncbi.nlm.nih.gov/23287924/ — **17.37 Mbps ＋ 50 W（商用元件）。修正既有 dossier 的 12.4 Mbps / 32.5 W。**
17. **S17** — Through-Metal-Wall Power Delivery and Data Transmission for Enclosed Sensors: A Review, *Sensors* 15(12), 29870 — https://www.mdpi.com/1424-8220/15/12/29870 — **>70% 效率 / >100 W；薄壁 >1 kW；四大商業化障礙（對準敏感度、材料參數不可知、非熱效應知識缺口、市場小眾）。**
18. **S18** — （由搜尋摘要指出的後續文獻）IEEE COMPEL 2025「a new class of topologies for isolated piezoelectric-based power conversion」；IEEE Transactions on Power Electronics 2026 期刊版 — 未取得直接 URL【未驗證】。
19. **S19** — Migatron ATEX & IECEx Certified Ultrasonic Sensors — https://www.migatron.com/atex-iecex-certified-sensors/ — **本安超音波感測器已有認證商品（RPS-409A-IS2、RPS-429A-IS），Zone 0/1/2 與 20/21/22。**
20. **S20** — Endress+Hauser — Intrinsic safety with ATEX instruments — https://www.endress.com/en/endress-hauser-group/capabilities-efficient-safe-operations/process-safety-field-instrumentation/intrinsic-safety — 本安的定義為限制可用於點火的電能與熱能。
21. **S21** — Ultrasonic Transducers for In-Service Inspection and Continuous Monitoring in High-Temperature Environments, *Sensors* 23(7), 3520 — https://www.mdpi.com/1424-8220/23/7/3520 — 長期安裝換能器的耦合介面隨蒸發與化學／物理變化而劣化。
22. **S22** — US8408065「Dry-coupled permanently installed ultrasonic sensor linear array」— https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/8408065 — **液態耦合劑乾涸／滲漏／流失；黏著劑鍵合失效率高，且可能由超音波感測器本身的能量輸入所加劇。**
23. **S23** — UC Berkeley 技轉 NCD 33842「Piezoelectric Transformers For Power Conversion」— https://techtransfer.universityofcalifornia.edu/NCD/33842.html — 非隔離單埠壓電諧振器功率級效率 99%、功率密度達 5.7 kW/cm³；**不含隔離規格。**
24. **S24** — Boles Lab @ UC Berkeley — https://www.boleslab.org/ — 團隊定位與研究方向；**不含隔離規格。**
25. **S25** — Linbo Shao, Virginia Tech ECE 教師頁 — https://ece.vt.edu/people/profile/shaolb.html — 機構歸屬確認。
26. **S26** — Coilcraft `HTX7045C` LLC Half-Bridge Transformers — https://www.coilcraft.com/en-us/products/transformers/power-transformers/power-converter-transformers/htx7045c/ — 繞組間電容低至 0.7 pF；2800 Vrms / 4000 VDC（1 分鐘 hipot）；chip-style；匝比 1:1 至 2.5:1。**功率與價格查無。**
27. **S27** — Medium-Voltage Isolated Auxiliary Power Supply Design for High Insulation Capability, Ultra-Low Coupling Capacitance, and Small Size（OSTI）— https://www.osti.gov/servlets/purl/1974608 — **2.5 W / 1.03 pF / PDIV >15 kV rms / 61×24×30 mm；10 kV SiC 的 13.8 kV·100 kW 三相變流器用。**
28. **S28** — CPES (Virginia Tech) — Power Supply with Low Input-Output Capacitance for Multiple Gate Driver Units of a 10 kV SiC-MOSFET Module — https://cpes.vt.edu/library/viewnugget/760 — <2 pF / >20 kV 門檻；PCB 無芯 5.85 pF @>10 kV rms；>100 kV DC 原型 3.4 pF@50 MHz、13 pF@100 MHz。
29. **S29** — A galvanically isolated gate driver with low coupling capacitance for medium voltage SiC MOSFETs — https://www.researchgate.net/publication/309640066_A_galvanically_isolated_gate_driver_with_low_coupling_capacitance_for_medium_voltage_SiC_MOSFETs — 4 mm 氣隙 1.6 pF；另一族拓樸絕緣 >40 kV、電容 <10 pF。
30. **S30** — 同 S27 的 OSTI 書目頁 — https://www.osti.gov/pages/biblio/1974608 — PD-free @100 kHz / 5 kV PWM / dv/dt 100 V/ns；相較傳統 10 kV 隔離閘驅體積縮小 10 倍以上。
31. **S31** — Experimental Characterization and Prediction of Radial and Thickness Mode Power Transfer Capability in Through-Metal Acoustic Power Transfer（arXiv:2607.13797）— https://arxiv.org/abs/2607.13797 — **ARL 合作協議 W911NF2220007 資助；TM-APT 目標功率「often targeting hundreds of watts」。**
32. **S32** — 同上 HTML 全文 — https://arxiv.org/html/2607.13797 — 致謝段落含完整合約編號。
33. **S33** — EPRI Used Fuel and High-Level Waste Management Program（含 Extended Storage Collaboration Program）— https://www.epri.com/portfolio/programs/061149 — 涵蓋 canister 完整性、檢測、監測與感測器、大學合作。**預算數字查無。**
34. **S34** — NEUP CFA-21-24261「Internal Wireless Sensors for Dry Cask Storage」，PI: Dr. Travis W. Knight（University of South Carolina）— https://neup.inl.gov/content/uploads/14/2024/07/CFA-21-24261_TechnicalAbstract_2021_CFA_Technical_Abstract_21-24261.pdf — **競爭路線：裝填時放入無線感測器＋輻射屏蔽，不需穿壁聲學。**
35. **S35** — DOE-ID NEPA CX 決定書 DOE-ID-21-098 — https://www.energy.gov/nepa/articles/cx-025503-internal-wireless-sensors-dry-cask-storage-university-south-carolina — 同上計畫之環評豁免。
36. **S36** — PNNL — Non-invasive ultrasonic sensing of internal conditions on a partial full-scale spent nuclear fuel canister mock-up — https://www.pnnl.gov/publications/non-invasive-ultrasonic-sensing-internal-conditions-partial-full-scale-spent-nuclear 〔轉引既有 dossier〕
37. **S37** — Ethicon Endo-Surgery US10263171「Surgical generator for ultrasonic and electrosurgical devices」— https://uspto.report/patent/grant/10263171 — **雜散電容造成病人漏電流；500 kHz–1 MHz；被動洩漏電容不足以維持在 10 µA 以下，故需主動抵消。**
38. **S38** — 同族 US9039695 — https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/9039695
39. **S39** — US3946738A「Leakage current cancelling circuit for use with electrosurgical instrument」— https://patents.google.com/patent/US3946738A/en — 以串聯 LC 並聯於雜散電容加以抵消（最早先例）；另 US4437464A https://patents.google.com/patent/US4437464A/en
40. **S40** — US9500074「Acoustic coupling of electrical power and data between downhole devices」— https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/9500074 — **壓電陶瓷疊層經管柱壁收發應力波，供電井下感測器與流體控制系統。**
41. **S41** — US8416098「Acoustic communication apparatus for use with downhole tools」— https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/8416098
42. **S42** — US20110192222A1「Piezoelectric actuator for downhole applications」— https://patents.google.com/patent/US20110192222
43. **S43** — PI (Physik Instrumente) — Piezo Actuators — https://www.pi-usa.us/en/products/piezo-actuators-stacks-benders-tubes — 氣密封裝／不鏽鋼外殼壓電致動器；井下應用至 200 °C。
44. **S44** — US7525398「Acoustically communicating data signals across an electrical isolation barrier」（Avago／今 Broadcom，John D. Larson III 等）— https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/7525398 — **聲學隔離 20 年未起飛的直接證據。**
45. **S45** — US7514844「Acoustic data coupling system and method」— https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/7514844 — 同族。
46. **S46** — US7586392「Dual path acoustic data coupling system and method」— https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/7586392 — 同族。
47. **S47** — Data Passes Through Metal Like Magic With a New Twist on ADL, *Design News* — https://www.designnews.com/electronics/data-passes-through-metal-like-magic-with-a-new-twist-on-adl — **稱該超音波 ADL 技術「尚未商業化，但正被商業機構測試中」【未驗證，摘要轉述】。**
48. **S48** — Single-Crystal AlN Wafer-Based Bulk Acoustic Resonators for Piezoelectric Power Conversion（arXiv:2603.19409）— https://arxiv.org/pdf/2603.19409 — AlN 路線（未解問題 3 的查證入口）。
49. **S49** — Infineon — Common mode transient immunity (CMTI) in gate drivers — https://community.infineon.com/t5/Knowledge-Base-Articles/Common-mode-transient-immunity-CMTI-in-gate-drivers/ta-p/1114529 — 1ED3124 傳輸延遲 ≈90 ns、CMTI >200 kV/µs（延遲對照基準）〔轉引既有 dossier〕
50. **S50** — US11777487 / US12206394「Gate driver coreless transformers for magnetic resonance imaging power electronics」— https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/11777487 — MRI 無磁閘驅需求佐證〔轉引既有 dossier〕；US11796613「Opto-isolator circuitry for MRI applications」— https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/11796613 — 訊號可光隔離、功率不行。
