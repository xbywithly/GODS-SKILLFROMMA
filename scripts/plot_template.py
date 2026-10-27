# -*- coding: utf-8 -*-
"""
Thesis Standard Scientific Plotting Template
Conforms strictly to the master thesis standards:
1. All text strictly in pure black (#000000).
2. Boxes/patches have no background fill (transparent or white, black outline only).
3. Text minimized; standard math/physical symbols preferred over verbose Chinese descriptions.
4. Scale 1.5x for axes tick labels and titles (11-13pt).
5. Aspect ratio designed for ~1/5 page height (width 12-16cm, height 4.5-5.5cm).
6. Tight bounding box with pad_inches=0.02 and high DPI (>= 350).
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

def setup_thesis_plot_style():
    """Configures global matplotlib rcParams to match thesis requirements."""
    plt.rcParams.update({
        'font.sans-serif': ['Microsoft YaHei', 'SimHei', 'Arial'],
        'axes.unicode_minus': False,
        'text.color': '#000000',
        'axes.labelcolor': '#000000',
        'xtick.color': '#000000',
        'ytick.color': '#000000',
        'axes.edgecolor': '#000000',
        'axes.linewidth': 1.2,
        'font.size': 11,           # Base font size scaled 1.5x
        'axes.titlesize': 12,
        'axes.labelsize': 12,
        'xtick.labelsize': 11,
        'ytick.labelsize': 11,
        'legend.fontsize': 10,
        'figure.dpi': 350,
        'savefig.dpi': 350,
        'mathtext.fontset': 'stix',
    })

def create_standard_curve_figure():
    """Example 1: Signal or curve plot occupying ~1/5 page height."""
    setup_thesis_plot_style()
    
    # 1/5 page height: width 15cm (~6 inches), height 4.8cm (~1.9 inches)
    fig, ax = plt.subplots(figsize=(6.2, 2.0))
    
    t = np.linspace(0, 1.0, 200)
    y_raw = np.sin(2 * np.pi * 2 * t) + 0.15 * np.random.randn(len(t))
    y_filtered = np.sin(2 * np.pi * 2 * t)
    
    ax.plot(t, y_raw, color='#777777', linestyle='--', linewidth=1.0, label=r'Raw $\omega_y$')
    ax.plot(t, y_filtered, color='#000000', linestyle='-', linewidth=1.5, label=r'Filtered $\omega_y$')
    
    ax.set_xlabel(r'Time $t$ / s')
    ax.set_ylabel(r'$\omega_y$ / (rad/s)')
    ax.set_xlim(0, 1.0)
    
    # Transparent box, no fill
    legend = ax.legend(frameon=True, loc='upper right', framealpha=1.0)
    legend.get_frame().set_edgecolor('#000000')
    legend.get_frame().set_facecolor('#ffffff')  # pure white or transparent
    legend.get_frame().set_linewidth(1.0)
    
    plt.tight_layout(pad=0.2)
    return fig, ax

def create_standard_flowchart_figure():
    """Example 2: Flowchart / structural diagram without background fill."""
    setup_thesis_plot_style()
    
    fig, ax = plt.subplots(figsize=(6.2, 2.2))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 4)
    ax.axis('off')
    
    # Box 1: No fill, pure black stroke
    box1 = patches.FancyBboxPatch((0.5, 1.2), 2.2, 1.6, boxstyle="round,pad=0.1",
                                  edgecolor="#000000", facecolor="none", linewidth=1.2)
    ax.add_patch(box1)
    ax.text(1.6, 2.0, r"$\mathbf{a}^S(t), \boldsymbol{\omega}^S(t)$",
            ha="center", va="center", color="#000000", fontsize=11)
    
    # Arrow: Pure black
    ax.annotate("", xy=(3.8, 2.0), xytext=(2.8, 2.0),
                arrowprops=dict(arrowstyle="->", color="#000000", lw=1.2))
    
    # Box 2: Zero-phase Butterworth filter
    box2 = patches.FancyBboxPatch((3.9, 1.2), 2.4, 1.6, boxstyle="round,pad=0.1",
                                  edgecolor="#000000", facecolor="none", linewidth=1.2)
    ax.add_patch(box2)
    ax.text(5.1, 2.0, r"Butterworth ($f_c=6\,\mathrm{Hz}$)",
            ha="center", va="center", color="#000000", fontsize=11)
    
    # Arrow
    ax.annotate("", xy=(7.4, 2.0), xytext=(6.4, 2.0),
                arrowprops=dict(arrowstyle="->", color="#000000", lw=1.2))
    
    # Box 3: Feature vector output
    box3 = patches.FancyBboxPatch((7.5, 1.2), 2.0, 1.6, boxstyle="round,pad=0.1",
                                  edgecolor="#000000", facecolor="none", linewidth=1.2)
    ax.add_patch(box3)
    ax.text(8.5, 2.0, r"$\mathbf{X} \in \mathbb{R}^d$",
            ha="center", va="center", color="#000000", fontsize=11)
    
    plt.tight_layout(pad=0.1)
    return fig, ax

def create_standard_grouped_bar_figure():
    """
    Example 3: Academic grouped bar chart.
    Avoids redundant/overlapping text above narrow adjacent bars.
    Relies on precise y-axis ticks and clean legend.
    """
    setup_thesis_plot_style()
    
    fig, ax = plt.subplots(figsize=(3.4, 2.7))
    x = np.arange(4)
    width = 0.22
    prec = [98.1, 97.8, 98.6, 97.4]
    rec  = [98.2, 97.6, 98.8, 97.1]
    f1   = [98.1, 97.7, 98.7, 97.2]
    
    ax.bar(x - width, prec, width, label='精确率', color='#222222', edgecolor='k')
    ax.bar(x, rec, width, label='召回率', color='#777777', edgecolor='k')
    ax.bar(x + width, f1, width, label='F1得分', color='#CCCCCC', edgecolor='k')
    
    ax.set_xticks(x)
    ax.set_xticklabels([r'$S_1$', r'$S_2$', r'$S_3$', r'$S_4$'], fontsize=10.0)
    ax.set_ylabel(r'$\mathrm{Score}\ /\ (\%)$', fontsize=10.5)
    ax.set_ylim(92, 105.0)
    ax.grid(True, linestyle=':', linewidth=0.5, color='#CCCCCC', alpha=0.7)
    ax.legend(loc='upper center', ncol=3, fontsize=8.0, framealpha=1.0, edgecolor='#000000',
              fancybox=False, handletextpad=0.3, columnspacing=0.8)
    
    plt.tight_layout(pad=0.1)
    return fig, ax

def pad_figures_to_identical_canvas(path_a, path_b):
    """
    Helper function: Pads two horizontal subfigures onto an identical canvas
    so that side-by-side display in Word table cells has 100% identical aspect ratio and dimensions.
    """
    from PIL import Image
    ima = Image.open(path_a)
    imb = Image.open(path_b)
    tw = max(ima.size[0], imb.size[0]) + 60
    th = max(ima.size[1], imb.size[1]) + 60
    def pad(im):
        c = Image.new('RGB', (tw, th), (255, 255, 255))
        c.paste(im, ((tw - im.size[0]) // 2, (th - im.size[1]) // 2))
        return c
    pad(ima).save(path_a, dpi=(600, 600))
    pad(imb).save(path_b, dpi=(600, 600))
    print(f"Unified horizontal paired figures to canvas: ({tw}, {th})")

if __name__ == "__main__":
    fig1, _ = create_standard_curve_figure()
    fig1.savefig("demo_curve.png", dpi=350, bbox_inches="tight", pad_inches=0.02)
    print("Demo curve saved.")
    
    fig2, _ = create_standard_flowchart_figure()
    fig2.savefig("demo_flowchart.png", dpi=350, bbox_inches="tight", pad_inches=0.02)
    print("Demo flowchart saved.")

    fig3, _ = create_standard_grouped_bar_figure()
    fig3.savefig("demo_bar.png", dpi=350, bbox_inches="tight", pad_inches=0.02)
    print("Demo grouped bar chart saved.")
