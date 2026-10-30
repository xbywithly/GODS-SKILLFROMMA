# -*- coding: utf-8 -*-
"""
Thesis Standard Scientific Plotting Template
Conforms strictly to the master thesis standards:
1. All text strictly in pure black (#000000).
2. Fonts: SimSun for Chinese, Times New Roman for English/digits, STIX for math.
3. Font size: 小五号 (9.0 pt) globally.
4. Anti-occlusion rule: curves, peaks, and valleys must NEVER be obscured by text or legends.
   Y-limits must provide 25%~35% headroom above peaks for legends.
5. Boxes/patches have no background fill (transparent or white, black outline only).
6. Aspect ratio designed for ~1/5 page height (width 12-16cm, height 4.5-5.5cm).
7. High DPI (600 DPI) for ultimate clarity.
8. 100% data and code driven.
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

FONT_SIZE = 9.0  # 小五号 (9.0 磅)

def setup_thesis_plot_style():
    """Configures global matplotlib rcParams to match thesis requirements."""
    plt.rcParams.update({
        'font.family': 'serif',
        'font.serif': ['SimSun', 'Times New Roman'],
        'mathtext.fontset': 'stix',
        'axes.unicode_minus': False,
        'text.color': '#000000',
        'axes.labelcolor': '#000000',
        'xtick.color': '#000000',
        'ytick.color': '#000000',
        'axes.edgecolor': '#000000',
        'axes.linewidth': 0.8,
        'font.size': FONT_SIZE,
        'axes.titlesize': FONT_SIZE,
        'axes.labelsize': FONT_SIZE,
        'xtick.labelsize': FONT_SIZE,
        'ytick.labelsize': FONT_SIZE,
        'legend.fontsize': FONT_SIZE,
        'xtick.direction': 'in',
        'ytick.direction': 'in',
        'xtick.major.size': 3.5,
        'ytick.major.size': 3.5,
        'figure.dpi': 600,
        'savefig.dpi': 600,
    })

def create_standard_curve_figure():
    """Example 1: Signal or curve plot occupying ~1/5 page height with anti-occlusion headroom."""
    setup_thesis_plot_style()
    
    # 1/5 page height: width 13.5cm (~5.3 inches), height 5.0cm (~2.0 inches)
    fig, ax = plt.subplots(figsize=(5.31, 2.10), dpi=600)
    
    t = np.linspace(0, 1.0, 200)
    y_raw = np.sin(2 * np.pi * 2 * t) + 0.15 * np.random.randn(len(t))
    y_filtered = np.sin(2 * np.pi * 2 * t)
    
    ax.plot(t, y_raw, color='#777777', linestyle=':', linewidth=1.0, label='原始角速度')
    ax.plot(t, y_filtered, color='#000000', linestyle='-', linewidth=1.2, label='零相位滤波')
    
    ax.set_xlabel('时间 / s', fontsize=FONT_SIZE)
    ax.set_ylabel(r'角速度 / ($^\circ\cdot\mathrm{s}^{-1}$)', fontsize=FONT_SIZE)
    ax.set_xlim(0, 1.0)
    
    # Anti-occlusion: peak is at +1.15, extend y-limit to 1.7 to reserve 35% clean sky zone for legend
    ax.set_ylim(-1.5, 1.7)
    
    # Transparent box, no fill, placed in dedicated sky zone
    legend = ax.legend(frameon=False, loc='upper right', fontsize=FONT_SIZE, handlelength=1.2, borderpad=0.2)
    
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.grid(True, linestyle=':', alpha=0.5, color='#CCCCCC')
    
    plt.tight_layout(pad=0.3)
    return fig, ax

def create_standard_flowchart_figure():
    """Example 2: Flowchart / structural diagram without background fill."""
    setup_thesis_plot_style()
    
    fig, ax = plt.subplots(figsize=(5.31, 1.85), dpi=600)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 3)
    ax.axis('off')
    
    # Box 1: No fill, pure black stroke
    box1 = patches.FancyBboxPatch((0.5, 0.8), 2.2, 1.4, boxstyle="round,pad=0.04",
                                  edgecolor="#000000", facecolor="#FFFFFF", linewidth=1.0)
    ax.add_patch(box1)
    ax.text(1.6, 1.8, "惯性数据采集", ha="center", va="center", color="#000000", fontsize=FONT_SIZE)
    ax.text(1.6, 1.2, r"$\mathbf{a}^S(t), \boldsymbol{\omega}^S(t)$",
            ha="center", va="center", color="#000000", fontsize=FONT_SIZE)
    
    # Arrow: Pure black
    ax.annotate("", xy=(3.8, 1.5), xytext=(2.7, 1.5),
                arrowprops=dict(arrowstyle="-|>", color="#000000", lw=1.1, mutation_scale=8))
    
    # Box 2: Zero-phase Butterworth filter
    box2 = patches.FancyBboxPatch((3.8, 0.8), 2.4, 1.4, boxstyle="round,pad=0.04",
                                  edgecolor="#000000", facecolor="#FFFFFF", linewidth=1.0)
    ax.add_patch(box2)
    ax.text(5.0, 1.8, "零相位滤波去噪", ha="center", va="center", color="#000000", fontsize=FONT_SIZE)
    ax.text(5.0, 1.2, r"$f_c=6\,\mathrm{Hz}$", ha="center", va="center", color="#000000", fontsize=FONT_SIZE)
    
    # Arrow
    ax.annotate("", xy=(7.3, 1.5), xytext=(6.2, 1.5),
                arrowprops=dict(arrowstyle="-|>", color="#000000", lw=1.1, mutation_scale=8))
    
    # Box 3: Feature vector output
    box3 = patches.FancyBboxPatch((7.3, 0.8), 2.2, 1.4, boxstyle="round,pad=0.04",
                                  edgecolor="#000000", facecolor="#FFFFFF", linewidth=1.0)
    ax.add_patch(box3)
    ax.text(8.4, 1.8, "时空特征提取", ha="center", va="center", color="#000000", fontsize=FONT_SIZE)
    ax.text(8.4, 1.2, r"$\mathbf{f}_k \in \mathbb{R}^5$", ha="center", va="center", color="#000000", fontsize=FONT_SIZE)
    
    plt.tight_layout(pad=0.2)
    return fig, ax
