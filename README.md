# The Brain of Magod (工科硕士毕业论文格式规范、学术制图与文献管理 Skill)

> 面向工科硕士毕业论文的高质量学术写作、科学制图、公式标准化排版与参考文献智能检索归档技能包（Antigravity AI Agent Skill，支持通过 `/the-brain-of-magod` 或 `/geshi` 快捷命令直接调用）。

[![Antigravity Skill](https://img.shields.io/badge/Antigravity-Agent%20Skill-blue.svg)](https://deepmind.google/technologies/gemini/)
[![Slash Command](https://img.shields.io/badge/Command-%2Fthe--brain--of--magod-brightgreen.svg)](#-快速使用-quick-start)
[![Alias Command](https://img.shields.io/badge/Alias-%2Fgeshi-green.svg)](#-快速使用-quick-start)
[![MathType Compatible](https://img.shields.io/badge/MathType-OLE%20DSMT4-green.svg)](https://www.wiris.com/en/mathtype/)
[![Python 3.8+](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

---

## 📖 项目简介 (Introduction)

本仓库提供了一套完整的工科硕士毕业论文写作、制图、公式排版与参考文献全流程工程化 **Skill (`The Brain of Magod`)**（附带项目级 **Rule** 全局约束），严格对标工科硕士学位论文规范与参考论文排版体系。

在撰写包含大量实验数据、复杂数学模型与传感器算法的毕业论文章节时，AI 往往容易出现“正文残留原始 LaTeX 代码”、“公式排版偏移/编号出界”、“公式间距过大或上下裁切”、“流程图框内文字溢出/编号冗长”、“分组柱状图密集文字重叠”、“双子图高矮不一对齐失衡”、“硬件传感器臆造”以及“参考文献散乱未归档/缺少关键权威原文”等痛点。

本项目历经实际论文各章节撰写与迭代修改，沉淀提炼出 **9 大核心排版与文献管理标准** 与全套自动化工具链，彻底根除上述格式与学术规范隐患。

---

## 🎯 核心规范与特性 (Core Features)

### 0. 全篇括号一律采用英文半角括号 `( )` 铁律 (Parentheses Invariant)
* **100% 英文半角括号**：正文叙述、图表标题、变量说明、时序子相位划分、三级标题技术模块编号、公式引用等所有括号，**必须 100% 统一使用英文半角括号 `( )`**，严禁使用中文全角括号 `（ ）`。
* **`(1)`、`(2)` 编号规范**：三级标题下的核心大技术模块分割写为 `(1) xxx主要内容：……`、`(2) xxx主要内容：……`，严禁使用 `（1）`、`（2）`。

### 1. 科学插图与流程图规范 (Academic Scientific Figures & Flowcharts)
* **插图严禁文字遮挡曲线与波峰（防遮挡留白铁律）**：图内所有文字、标注箭头与图例框绝对严禁遮挡数据曲线、峰值与波谷，必须通过坐标轴范围向上扩展 25%~35%（留足“无数据纯净天空区”）或将图例置于低数据密度空白角，确保波形 100% 完整展现。
* **全图文字统一小五号 (9.0 pt) 与 600 DPI 高清输出**：图内中文采用宋体 (SimSun)，西文与数字采用 Times New Roman，数学公式采用 STIX；字号严格统一为小五号 (9.0 pt)（`FONT_SIZE = 9.0`），刻度数字与图例微调为 8.5~9.0 pt。
* **100% 真实代码与参数驱动绘图**：所有波形、频域、散点、极限环与柱状图必须 100% 由真实实验数据和算法代码运行生成，严禁使用预定既定数值或假图。
* **框内彻底去章节编号**：流程图、总体架构图内部框体只写精炼功能名称（如“惯性数据采集”、“运动信号预处理”），**严禁在框体内标注章节编号（如 2.2.1、2.3.1 等）**，防止编号冗长挤爆边框。
* **文字防溢出安全缓冲 ($\ge 30\%$)**：框内文字必须严格居中，单行文字长度不得超过框宽的 70%，四周留足至少 30% 安全呼吸间距，**文字严禁超出框格或接触边框**。
* **连接箭头安全避让**：跨阶段绕行连接箭头必须预留充足转折避让间距（拐角留空 $\ge 0.2$ 坐标单位），**严禁箭头穿刺、接触或遮挡框内文字**。
* **柱状图明确数字标识与紧凑排版铁律**：
  * **柱顶明确数字标注**：所有的单指标柱状图与多指标分组柱状图，必须在每根柱子顶端标注明确、清晰、真实的数值标识。
  * **横向数字排版与零重叠**：柱顶数值一律采用原生横向居中显示（`rotation=0`、Times New Roman 6.2~6.5 pt），相邻细柱间保留正向安全间距，彻底杜绝文字粘连。
  * **纵坐标上界紧凑化**：纵坐标 $y$ 轴上界紧缩至“刚刚好能够完整容纳柱顶横向数字与安全呼吸间距”，图例移至图框上方居中，杜绝大面积空旷断层。
* **横向对比双子图严格尺寸对称**：横向并排的两个子图 `(a)` 与 `(b)`，必须在图像生成后通过补白（`pad_to_canvas`）统一为 **100% 完全相同的像素宽高**，并在 Word 嵌入表格中指定完全相同的图形 `extent`（如 `cx="2736000" cy="2251217"`），杜绝“一高一矮”、“一胖一瘦”的视觉失衡。
* **纯黑字体与无填充线框**：图内所有轴标签、刻度数字、图例、框内文字一律使用纯黑（`#000000`）；图框采用透明底或纯白底（严禁背景色彩填充），线条分明。
* **骨骼连线与图例避让规范**：骨骼中心线（如股骨轴）必须绘制为干净中性的连续实线，**严禁在骨骼连线上绘制向下箭头**；图例必须置于图像顶部独立无数据的预留空白区，严禁遮挡任何散点簇、支持向量或超平面。
* **版面高度与物理真实性**：单张图片高度严格控制在单页论文篇幅的 **1/5 左右**（约 4.5 ~ 5.5 cm）；涉及人体的姿态图，脚底必须真实接触台阶踏面，符合人体运动学与物理接触面，严禁悬空。

### 2. 数学公式与正文符号规范 (MathType OLE & MathTab)
* **100% MathType 原生嵌入 (`Equation.DSMT4`)**：正文中所有行内物理量与独立公式全部编译为原生 MathType OLE 对象，正文 0 原始 LaTeX 标记，0 下划线纯文本。
* **方括号转义防漏编**：所有包含方括号的 TeX 字符串自动转义为 `\left[` 与 `ight]`，防止与 MathType 快捷键定界符冲突。
* **独立公式 MathTab 黄金标准**：
  * **版心参数**：左边距 2.50 cm、右边距 2.50 cm（版心精准 16.00 cm = 9074 dxa）。
  * **段落零缩进**：公式段落显式声明 `firstLine="0"`, `left="0"`，严禁继承正文 2 字符首行缩进。
  * **双制表位精确对齐**：首个制表符跳至居中制表符 `4540`（正中 8.01 cm），第二个制表符跳至右对齐制表符 `9080`（右边缘 16.02 cm）。
  * **行距最小值 22 磅与段前段后 0 磅**：强制配置 `w:spacing w:line="440" w:lineRule="atLeast" w:before="0" w:after="0"`，彻底消除公式段落过大空旷间距，同时确保高大分式与上下标绝不被垂直裁切。
  * **公式相邻正文紧凑化**：公式前序段落段后强制设为 0 磅，后续段落（如“式中……”）段前强制设为 0 磅、行距最小值 22 磅。
* **变量说明排版与百分号防乱码铁律**：正文叙述中的百分比数值与步长（如 1% 步长），直接使用原生中文文本百分号，**严禁将 `%` 放入 TeX 切换源码 `$...$`**，避免 TeX 注释字符引发 MathType 转换失效或生成空框、乱码。
* **正文行内字符间距净化**：正文叙述中所有 MathType 行内公式、数字、单位与汉字之间，一律剔除孤立的多余半角空格（如 `在20 Hz以上`，严禁出现 `在   20 Hz   以上`）。

### 3. 章节学术架构引言“黄金三段式”与小结单段化
* **引言黄金三段式**：各章开头引言（如 2.1、3.1）必须严格采用结构紧凑的黄金三段式架构（第一段：宏观背景与分层控制枢纽；第二段：传感技术横向对比与三大工程难点；第三段：全章贡献与两阶段架构概览），杜绝段落碎片化。
* **本章小结单段化**：各章小结强制要求仅需一整段总结，彻底杜绝列出 (1) 至 (5) 类的分点列表，全面涵盖技术链路、量化指标并形成承上启下支撑。

### 4. 硬件设定真实性 (Hardware Realism)
* **严格忠实于实验配置**：明确采用**位于双侧大腿外侧的 2 组 6 轴 IMU（3 轴加速度计 + 3 轴陀螺仪）**，型号 WT901BLECL5.0，采样频率 100 Hz，加速度量程 $\pm 16g$，角速度量程 $\pm 2000^\circ/\mathrm{s}$。
* **绝对禁止臆造“9 轴 IMU”或“磁力计”**。
* **穿戴试验结构归集**：物理外骨骼样机整机穿戴测试、受试者试验与人机协同效果评估统一归集至**第 5 章**展开。

### 5. 参考文献智能检索、多源下载、分类管理与按序归档 (Literature Management Standards)
* **专属目录归集 (`参考文献/`) 与根目录纯净化**：所有中英文期刊、会议论文、学位论文、开源基准数据集论文与开题报告，100% 统一存放于专属 `参考文献\` 文件夹，根目录彻底纯净化零散落。
* **权威多源检索与自动化补充下载**：论文中涉及的核心理论（DMP/CPG）、滤波算法（零相位/STA去噪）、分类器（SVM/MLP/LSTM/RF）与基准数据（如 Camargo 2021 Nature Scientific Data），必须主动通过 OpenAlex、Europe PMC、PubMed、arXiv 及官方 OA 通道检索并下载官方完整 PDF。
* **双位数字严格按序规范重命名**：统一遵循 `[两位数序号] 第一作者_年份_论文精炼标题 (期刊/会议/单位).pdf` 格式，杜绝 hash 码与乱码，确保跨操作系统自然排序整齐。
* **动态维护检索总览与章节映射**：持续维护 `00_参考文献总览与引用检索目录.md`，提供 Mermaid 学术分类图谱、详细索引表格与正文第 1 ~ 5 章的技术支撑映射矩阵。
* **数据迁移完整性与安全防丢失**：转移前严格执行字节校验，并主动解除 Windows 只读属性（`os.chmod(fpath, stat.S_IWRITE)`），确保零数据丢失。

---

## 📁 目录结构 (Repository Structure)

```text
├── SKILL.md                          # Antigravity 技能主定义文件 (/the-brain-of-magod & /geshi)
├── README.md                         # 项目中文说明与使用手册 (The Brain of Magod)
├── references/
│   └── thesis_standards.md           # 硕士论文版面、字号、边距、图表与文献管理参数标准表
├── rules/
│   └── thesis-invariants.md          # 全局不可逾越的硬性准则 (Invariants)
├── scripts/
│   ├── batch_mathtype_converter.py   # Word 文档 MathType 公式批量编译工具
│   ├── postprocess_mathtab.py        # Word XML MathTab 居中/贴右/行距紧凑后处理工具
│   ├── plot_template.py              # Matplotlib 学术论文标准绘图代码模板
│   └── manage_references.py          # 参考文献扫描、规范重命名、迁移归档与索引生成工具
└── .agents/                          # Antigravity 自动化发现工作区目录结构
    ├── rules/
    │   └── thesis-invariants.md
    └── skills/
        ├── the-brain-of-magod/
        │   ├── SKILL.md
        │   ├── references/
        │   └── scripts/
        └── geshi/
            ├── SKILL.md
            ├── references/
            └── scripts/
```

---

## 🚀 快速使用 (Quick Start)

### 方式 1：在 Antigravity 交互会话中快捷调用 (推荐)
在会话中直接输入以下任意命令：
```text
/the-brain-of-magod
```
或使用简写别名：
```text
/geshi
```
即可直接激活本技能，自动加载所有格式规范、绘图准则、排版后处理指令与参考文献管理规范。

### 方式 2：作为工作区 Skill 使用
将本仓库克隆至你的论文工程根目录下的 `.agents/skills/the-brain-of-magod`：
```bash
git clone https://github.com/xbywithly/The-Brain-of-Magod.git .agents/skills/the-brain-of-magod
```

### 方式 3：作为全局 Skill 安装
将该文件夹复制到 Antigravity 全局配置目录：
```powershell
Copy-Item -Recurse .agents\skills	he-brain-of-magod ~\.gemini\config\skills```

### 方式 4：独立命令行脚本使用
#### 1. 批量编译 Word 文档中的 MathType 公式
```powershell
python scripts/batch_mathtype_converter.py "D:\path	o\your_thesis_chapter.docx"
```

#### 2. 自动化排版 MathTab 双制表位与行距
```powershell
python scripts/postprocess_mathtab.py "D:\path	o\your_thesis_chapter.docx"
```

#### 3. 运行标准学术绘图与画布对齐模板
```powershell
python scripts/plot_template.py
```

#### 4. 自动化管理与索引参考文献
```powershell
python scripts/manage_references.py
```

---

## 🛠️ 技术要求 (Requirements)

* **操作系统**：Windows 10 / 11 (64-bit)
* **办公软件**：Microsoft Office Word (2016 / 2019 / 2021 / Office 365)
* **公式编辑器**：Wiris MathType 7.x（需已加载至 Word 加载项）
* **Python 依赖**：
  ```bash
  pip install pywin32 python-docx matplotlib numpy pillow pypdf
  ```

---

## 📄 开源许可证 (License)

本项目基于 [MIT License](LICENSE) 开源发布。
