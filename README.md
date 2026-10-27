# Thesis Chapter Writer (毕业论文学术写作与排版规范 Skill)

> 面向工科硕士毕业论文的高质量学术写作、科学制图与公式标准化排版技能包（Antigravity AI Agent Skill）。

[![Antigravity Skill](https://img.shields.io/badge/Antigravity-Agent%20Skill-blue.svg)](https://deepmind.google/technologies/gemini/)
[![MathType Compatible](https://img.shields.io/badge/MathType-OLE%20DSMT4-green.svg)](https://www.wiris.com/en/mathtype/)
[![Python 3.8+](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

---

## 📖 项目简介 (Introduction)

本仓库提供了一套完整的工科硕士毕业论文写作与排版标准化 **Skill**（附带项目级 **Rule** 全局约束），严格对标知名高校工科硕士学位论文规范与参考论文排版体系。

在撰写包含大量实验数据、复杂数学模型与传感器算法的毕业论文章节时，AI 往往容易出现“正文残留原始 LaTeX 代码”、“公式排版偏移/编号出界”、“公式上下裁切显示不全”、“插图配色混乱/文字被遮挡”、“硬件传感器臆造”等痛点。本项目沉淀了一整套工程化工具链与确定性规则，彻底根除上述问题。

---

## 🎯 核心规范与特性 (Core Features)

### 1. 科学插图规范 (Academic Scientific Figures)
* **纯黑字体与无填充线框**：图内所有轴标签、刻度数字、图例、框内文字一律使用纯黑（`#000000`）；图框采用透明底或纯白底（无背景填充），线条清晰分明。
* **精炼文案与符号优先**：图内文字极简，凡有物理/数学符号的量一律直接使用标准符号（如 $\omega_y, a_x, \theta, f_c$），杜绝冗余中文。
* **1.5 倍放大与高清分辨率**：坐标轴与文字相比基准放大 1.5 倍（标题 12~13 pt，刻度 10~11 pt），保存分辨率 $\ge 350\ \text{DPI}$，保证缩放打印高清锐利。
* **防遮挡与物理真实性**：文字严禁超出图框边界，严禁被图标或连线遮挡；人体姿态图必须真实接触台阶踏面，符合人体运动学与物理接触面。
* **版面高度控制**：单张图片高度严格控制在单页论文篇幅的 **1/5 左右**（约 4.5 ~ 5.5 cm），避免单图过度侵占版面。

### 2. 数学公式与正文符号规范 (MathType OLE & MathTab)
* **100% MathType 原生嵌入 (`Equation.DSMT4`)**：正文中所有行内物理量与独立公式全部编译为原生 MathType OLE 对象，正文 0 原始 LaTeX 标记，0 下划线纯文本。
* **方括号转义防漏编**：所有包含方括号的 TeX 字符串自动转义为 `\left[` 与 `\right]`，防止与 MathType 快捷键定界符冲突。
* **独立公式 MathTab 黄金标准**：
  * **版心参数**：左边距 2.50 cm、右边距 2.50 cm（版心精准 16.00 cm = 9074 dxa）。
  * **段落零缩进**：公式段落显式声明 `firstLine="0"`, `left="0"`，严禁继承正文 2 字符首行缩进。
  * **双制表位精确对齐**：首个制表符跳至居中制表符 `4540`（正中 8.01 cm），第二个制表符跳至右对齐制表符 `9080`（右边缘 16.02 cm）。
  * **22 磅最小值行距**：行距统一设置为“最小值 22 磅”（`line="440" lineRule="atLeast"`），段前段后 6 磅，彻底杜绝公式垂直裁切。

### 3. 硬件设定真实性 (Hardware Realism)
* **严格忠实于实验配置**：明确采用**位于双侧大腿外侧的 2 组 6 轴 IMU（3 轴加速度计 + 3 轴陀螺仪）**，绝对严禁臆造“9 轴 IMU”或“磁力计”。
* **参数主动确认**：凡遇任何未明确的实验超参数、滤波频率或算法阈值，主动向用户确认，切勿盲目自定。

---

## 📁 目录结构 (Repository Structure)

```text
├── SKILL.md                          # Antigravity 技能主定义文件
├── README.md                         # 项目中文/英文使用说明
├── references/
│   └── thesis_standards.md           # 硕士论文版面、字号、边距、图表排版参数标准表
├── rules/
│   └── thesis-invariants.md          # 全局不可逾越的硬性准则 (Invariants)
├── scripts/
│   ├── batch_mathtype_converter.py   # Word 文档 MathType 公式批量编译工具
│   ├── postprocess_mathtab.py        # Word XML MathTab 居中/贴右/行距自动后处理工具
│   └── plot_template.py              # Matplotlib 学术论文标准绘图代码模板
└── .agents/                          # Antigravity 自动化发现工作区目录结构
    ├── rules/
    │   └── thesis-invariants.md
    └── skills/
        └── thesis-chapter-writer/
            ├── SKILL.md
            ├── references/
            └── scripts/
```

---

## 🚀 快速使用 (Quick Start)

### 方式 1：作为 Antigravity 工作区 Skill 使用
将本仓库克隆至你的论文工程根目录下的 `.agents/skills/thesis-chapter-writer`，或直接作为整个仓库克隆：
```bash
git clone https://github.com/xbywithly/NewRepo.git .agents/skills/thesis-chapter-writer
```
Antigravity 将在每次需要撰写论文、修改图表或排版公式时自动激活该 Skill。

### 方式 2：作为全局 Skill 安装
将该文件夹复制到 Antigravity 全局配置目录：
```powershell
Copy-Item -Recurse .agents\skills\thesis-chapter-writer ~\.gemini\config\skills\
```

### 方式 3：独立命令行脚本使用
#### 1. 批量编译 Word 文档中的 MathType 公式
```powershell
# 在 Windows 交互桌面调度运行：
python scripts/batch_mathtype_converter.py "D:\path\to\your_thesis_chapter.docx"
```

#### 2. 自动化排版 MathTab 双制表位与行距
```powershell
python scripts/postprocess_mathtab.py "D:\path\to\your_thesis_chapter.docx"
```

#### 3. 运行标准学术绘图模板
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
  pip install pywin32 python-docx matplotlib numpy
  ```

---

## 📄 开源许可证 (License)

本项目基于 [MIT License](LICENSE) 开源发布。
