# -*- coding: utf-8 -*-
"""生成知乎文章封面（标题卡片，16:9）。"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm
from matplotlib.patches import FancyBboxPatch

for w in ["Regular", "Bold", "Medium"]:
    fm.fontManager.addfont(f"/usr/local/share/fonts/思源黑体CN-{w}.otf")
plt.rcParams["font.family"] = "Source Han Sans CN"
plt.rcParams["axes.unicode_minus"] = False

BLUE, BLUE_L = "#2F6BD8", "#EAF1FD"
TEAL, TEAL_L = "#0E9C8C", "#E4F6F4"
AMBER, AMBER_L = "#D98324", "#FBF0E0"
PURP, PURP_L = "#7B5BD6", "#EFEAFB"
GRAY, GRAY_L = "#5A6572", "#F1F3F6"
DARK = "#2B3440"
MID = "#5A6572"

OUT = "/home/william/工作文档/projects_code/course_summary/images/"

fig = plt.figure(figsize=(16, 9))
ax = fig.add_axes([0, 0, 1, 1])
ax.set_xlim(0, 100)
ax.set_ylim(0, 100)
ax.set_aspect("auto")
ax.axis("off")

# 纯白底 + 左侧蓝色竖条
ax.add_patch(plt.Rectangle((0, 0), 100, 100, fc="#FFFFFF", ec="none", zorder=0))
ax.add_patch(plt.Rectangle((0, 0), 1.6, 100, fc=BLUE, ec="none", zorder=1))

# 小标签
ax.text(50, 79, "DeepLearning.AI 短课 · 深度解读", ha="center", va="center",
        fontsize=15, color=BLUE, fontweight="bold")

# 主标题
ax.text(50, 61, "Claude Code 高阶使用技巧", ha="center", va="center",
        fontsize=42, color=DARK, fontweight="bold")

# 副标题
ax.text(50, 45, "把 Claude Code 用成靠谱的 AI 助理", ha="center", va="center",
        fontsize=18, color=MID)
ax.text(50, 36, "吴恩达 × Anthropic 主讲", ha="center", va="center",
        fontsize=14, color=MID)

# 底部关键词 chips
chips = [
    ("CLAUDE.md", BLUE, BLUE_L),
    ("Plan Mode", TEAL, TEAL_L),
    ("subagents", AMBER, AMBER_L),
    ("hooks", PURP, PURP_L),
    ("git worktree", GRAY, GRAY_L),
    ("MCP", BLUE, BLUE_L),
]
cw, ch, gap, y = 14.2, 9, 1.6, 16
total = len(chips) * cw + (len(chips) - 1) * gap
x0 = (100 - total) / 2
for i, (label, color, light) in enumerate(chips):
    x = x0 + i * (cw + gap)
    ax.add_patch(FancyBboxPatch((x, y), cw, ch,
                                boxstyle="round,pad=0.2,rounding_size=1.6",
                                fc=light, ec=color, lw=1.4, zorder=2))
    ax.text(x + cw / 2, y + ch / 2, label, ha="center", va="center",
            fontsize=12, color=color, fontweight="bold", zorder=3)

fig.savefig(OUT + "封面_标题卡.png", dpi=220, facecolor="white")
plt.close(fig)
print("done")
