# geshi (工科硕士毕业论文格式规范与学术排版 Skill)

> 面向工科硕士毕业论文的高质量学术写作、科学制图与公式标准化排版技能包（Antigravity AI Agent Skill，支持通过 `/geshi` 快捷命令直接调用）。

[![Antigravity Skill](https://img.shields.io/badge/Antigravity-Agent%20Skill-blue.svg)](https://deepmind.google/technologies/gemini/)
[![Slash Command](https://img.shields.io/badge/Command-%2Fgeshi-brightgreen.svg)](#-快速使用-quick-start)
[![MathType Compatible](https://img.shields.io/badge/MathType-OLE%20DSMT4-green.svg)](https://www.wiris.com/en/mathtype/)
[![Python 3.8+](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

---

## 📖 项目简介 (Introduction)

本仓库提供了一套完整的工科硕士毕业论文写作与排版工程化 **Skill (`geshi`)**（附带项目级 **Rule** 全局约束），严格对标工科硕士学位论文规范与参考论文排版体系。

在撰写包含大量实验数据、复杂数学模型与传感器算法的毕业论文章节时，AI 往往容易出现“正文残留原始 LaTeX 代码”、“公式排版偏移/编号出界”、“公式间距过大或上下裁切”、“流程图框内文字溢出/编号冗长”、“分组柱状图密集文字重叠”、“双子图高矮不一对齐失衡”、“硬件传感器臆造”等痛点。

本项目历经实际论文各章节撰写与迭代修改，沉淀提炼出 **8 大核心排版标准** 与全套自动化工具链，彻底根除上述格式与排版隐患。

---

## 🎯 核心规范与特性 (Core Features)

### 1. 流程图与科学插图规范 (Academic Scientific Figures & Flowcharts)
* **框内彻底去章节编号**：流程图、总体架构图内部框体只写精炼功能名称（如“惯性数据采集”、“运动信号预处理”），**严禁在框体内标注章节编号（如 2.2.1、2.3.1 等）**，防止编号冗长挤爆边框。
* **文字防溢出安全缓冲 ($\ge 30\%$)**：框内文字必须严格居中，单行文字长度不得超过框宽的 70%，四周留足至少 30% 安全呼吸间距，**文字严禁超出框格或接触边框**。
* **连接箭头安全避让**：跨阶段绕行连接箭头必须预留充足转折避让间距（拐角留空 $\ge 0.2$ 坐标单位），**严禁箭头穿刺、接触或遮挡框内文字**。
* **分组柱状图杜绝文字重叠与冗余**：多指标并排相邻细柱图（如 Precision/Recall/F1 并排柱），**严禁在每根狭窄柱子上方强行标注重复密集的小数字**，杜绝横向文字粘连重叠与视觉重复，主要依托刻度严密的 $y$ 轴网格线进行视觉判读；单指标对比图允许在柱顶居中垂直偏移标注黑色加粗数字。
* **横向对比双子图严格尺寸对称**：横向并排的两个子图 `(a)` 与 `(b)`，必须在图像生成后通过补白（`pad_to_canvas`）统一为 **100% 完全相同的像素宽高**，并在 Word 嵌入表格中指定完全相同的图形 `extent`（如 `cx="2736000" cy="2251217"`），杜绝“一高一矮”、“一胖一瘦”的视觉失衡。
* **纯黑字体与无填充线框**：图内所有轴标签、刻度数字、图例、框内文字一律使用纯黑（`#000000`）；图框采用透明底或纯白底（严禁背景色彩填充），线条分明。
* **骨骼连线与图例避让规范**：骨骼中心线（如股骨轴）必须绘制为干净中性的连续实线，**严禁在骨骼连线上绘制向下箭头**；图例必须置于图像顶部独立无数据的预留空白区，严禁遮挡任何散点簇、支持向量或超平面。
* **版面高度与物理真实性**：单张图片高度严格控制在单页论文篇幅的 **1/5 左右**（约 4.5 ~ 5.5 cm）；涉及人体的姿态图，脚底必须真实接触台阶踏面，符合人体运动学与物理接触面，严禁悬空。

### 2. 数学公式与正文符号规范 (MathType OLE & MathTab)
* **100% MathType 原生嵌入 (`Equation.DSMT4`)**：正文中所有行内物理量与独立公式全部编译为原生 MathType OLE 对象，正文 0 原始 LaTeX 标记，0 下划线纯文本。
* **方括号转义防漏编**：所有包含方括号的 TeX 字符串自动转义为 `\left[` 与 `\right]`，防止与 MathType 快捷键定界符冲突。
* **独立公式 MathTab 黄金标准**：
  * **版心参数**：左边距 2.50 cm、右边距 2.50 cm（版心精准 16.00 cm = 9074 dxa）。
  * **段落零缩进**：公式段落显式声明 `firstLine="0"`, `left="0"`，严禁继承正文 2 字符首行缩进。
  * **双制表位精确对齐**：首个制表符跳至居中制表符 `4540`（正中 8.01 cm），第二个制表符跳至右对齐制表符 `9080`（右边缘 16.02 cm）。
  * **行距最小值 22 磅与段前段后 0 磅**：强制配置 `w:spacing w:line="440" w:lineRule="atLeast" w:before="0" w:after="0"`，彻底消除公式段落过大空旷间距，同时确保高大分式与上下标绝不被垂直裁切。
* **正文行内字符间距净化**：正文叙述中所有 MathType 行内公式、数字、单位与汉字之间，一律剔除孤立的多余半角空格（如 `在20 Hz以上`，严禁出现 `在   20 Hz   以上`）。

### 3. 章节学术架构引言“黄金三段式”
各章开头引言（如 2.1、3.1）必须严格采用结构紧凑的黄金三段式架构，杜绝段落碎片化：
* **第一段（宏观背景、运动挑战与分层控制必要性）**：外骨骼运动场景高负荷挑战与步态相位在分层控制中的枢纽作用。
* **第二段（传感技术横向对比与移动惯性技术瓶颈）**：对比压力鞋垫、sEMG、光学动捕局限，论证大腿贴附式 MEMS IMU 优势，剖析三大核心难点（踏步瞬态冲击、STA 软组织伪影、步频时变切片）。
* **第三段（全章核心贡献与阶段结构概览）**：阐述全章两阶段架构（阶段一：硬件采集与预处理；阶段二：切片特征提取与分类评估），明确对后续章节的支撑关系。

### 4. 硬件设定真实性 (Hardware Realism)
* **严格忠实于实验配置**：明确采用**位于双侧大腿外侧的 2 组 6 轴 IMU（3 轴加速度计 + 3 轴陀螺仪）**，型号 WT901，采样频率 100 Hz，加速度量程 $\pm 16g$，角速度量程 $\pm 2000^\circ/\mathrm{s}$。
* **绝对禁止臆造“9 轴 IMU”或“磁力计”**。
* **参数主动确认**：凡遇任何未明确的实验超参数、滤波频率或算法阈值，主动向用户确认，切勿盲目自定。

---

## 📁 目录结构 (Repository Structure)

```text
├── SKILL.md                          # Antigravity 技能主定义文件 (/geshi)
├── README.md                         # 项目中文说明与使用手册
├── references/
│   └── thesis_standards.md           # 硕士论文版面、字号、边距、图表排版参数标准表
├── rules/
│   └── thesis-invariants.md          # 全局不可逾越的硬性准则 (Invariants)
├── scripts/
│   ├── batch_mathtype_converter.py   # Word 文档 MathType 公式批量编译工具
│   ├── postprocess_mathtab.py        # Word XML MathTab 居中/贴右/行距紧凑后处理工具
│   └── plot_template.py              # Matplotlib 学术论文标准绘图代码模板
└── .agents/                          # Antigravity 自动化发现工作区目录结构
    ├── rules/
    │   └── thesis-invariants.md
    └── skills/
        └── geshi/
            ├── SKILL.md
            ├── references/
            │   └── thesis_standards.md
            └── scripts/
                ├── batch_mathtype_converter.py
                ├── postprocess_mathtab.py
                └── plot_template.py
```

---

## 🚀 快速使用 (Quick Start)

### 方式 1：在 Antigravity 交互会话中快捷调用 (推荐)
在会话中直接输入：
```text
/geshi
```
即可直接激活本技能，自动加载所有格式规范、绘图准则与排版后处理指令。

### 方式 2：作为工作区 Skill 使用
将本仓库克隆至你的论文工程根目录下的 `.agents/skills/geshi`：
```bash
git clone https://github.com/xbywithly/GODS-SKILLFROMMA.git .agents/skills/geshi
```

### 方式 3：作为全局 Skill 安装
将该文件夹复制到 Antigravity 全局配置目录：
```powershell
Copy-Item -Recurse .agents\skills\geshi ~\.gemini\config\skills\
```

### 方式 4：独立命令行脚本使用
#### 1. 批量编译 Word 文档中的 MathType 公式
```powershell
# 在 Windows 交互桌面调度运行：
python scripts/batch_mathtype_converter.py "D:\path\to\your_thesis_chapter.docx"
```

#### 2. 自动化排版 MathTab 双制表位与行距
```powershell
python scripts/postprocess_mathtab.py "D:\path\to\your_thesis_chapter.docx"
```

#### 3. 运行标准学术绘图与画布对齐模板
```powershell
python scripts/plot_template.py
```

---

## 🛠️ 技术要求 (Requirements)

* **操作系统**：Windows 10 / 11 (64-bit)
* **办公软件**：Microsoft Office Word (2016 / 2019 / 2021 / Office 365)
* **公式编辑器**：Wiris MathType 7.x（需已加载至 Word 加载项）
* **Python 依赖**：
  ```bash
  pip install pywin32 python-docx matplotlib numpy pillow
  ```

---

## 📄 开源许可证 (License)

本项目基于 [MIT License](LICENSE) 开源发布。
