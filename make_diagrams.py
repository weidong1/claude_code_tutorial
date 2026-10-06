# -*- coding: utf-8 -*-
"""生成知乎文章《吴恩达 Claude Code 课》的 4 张自绘示意图。"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Ellipse

# ---- 字体 ----
for w in ["Regular", "Bold", "Medium"]:
    fm.fontManager.addfont(f"/tmp/cjkfonts/NotoSansCJKsc-{w}.ttf")
plt.rcParams["font.family"] = "Noto Sans CJK SC"
plt.rcParams["axes.unicode_minus"] = False

# ---- 配色 ----
BLUE, BLUE_L   = "#2F6BD8", "#EAF1FD"
TEAL, TEAL_L   = "#0E9C8C", "#E4F6F4"
AMBER, AMBER_L = "#D98324", "#FBF0E0"
PURP, PURP_L   = "#7B5BD6", "#EFEAFB"
RED, RED_L     = "#D9534F", "#FBE9E7"
GRAY, GRAY_L   = "#5A6572", "#F1F3F6"
DARK           = "#2B3440"
MID            = "#5A6572"

OUT = "/home/william/工作文档/projects_code/course_summary/images/"

def new_ax(w, h, xlim, ylim):
    fig = plt.figure(figsize=(w, h))
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(*xlim); ax.set_ylim(*ylim)
    ax.set_aspect("equal"); ax.axis("off")
    return fig, ax

def box(ax, x, y, w, h, text="", fc=BLUE_L, ec=BLUE, tc=DARK, fs=13, bold=False,
        lw=1.6, rounding=1.4, ls="-"):
    p = FancyBboxPatch((x, y), w, h,
                       boxstyle=f"round,pad=0.2,rounding_size={rounding}",
                       fc=fc, ec=ec, lw=lw, linestyle=ls, mutation_aspect=1, zorder=2)
    ax.add_patch(p)
    ax.text(x + w/2, y + h/2, text, ha="center", va="center", fontsize=fs,
            color=tc, fontweight="bold" if bold else "normal", zorder=3, linespacing=1.5)
    return p

def txt(ax, x, y, s, fs=11, c=MID, bold=False, ha="center", va="center"):
    ax.text(x, y, s, fontsize=fs, color=c, fontweight="bold" if bold else "normal",
            ha=ha, va=va, zorder=3, linespacing=1.4)

def arrow(ax, x1, y1, x2, y2, c=GRAY, lw=2.0, ms=15, rad=0.0):
    a = FancyArrowPatch((x1, y1), (x2, y2), arrowstyle="-|>", mutation_scale=ms,
                        color=c, lw=lw, connectionstyle=f"arc3,rad={rad}", zorder=2)
    ax.add_patch(a)
    return a

# ============================================================
# 图1 · 三大实战项目总览（能力曲线）
# ============================================================
fig, ax = new_ax(10, 6.2, (0, 100), (0, 62))
txt(ax, 50, 57.5, "一门课 · 三大实战项目", fs=19, c=DARK, bold=True)
txt(ax, 50, 52.5, "一条「读码 → 改码 → 造应用」的能力曲线", fs=12, c=MID)

cards = [
    (5,  BLUE, "01 · RAG 聊天机器人", "理解代码库\n添加功能\n测试 / 调试 / 重构\n多实例并行开发"),
    (37, TEAL, "02 · 电商数据仪表盘", "杂乱的 Jupyter Notebook\n重构为生产级代码\n转化为交互式 Web 仪表盘"),
    (69, PURP, "03 · Figma → Web App", "Figma 设计稿\n自动生成可用应用\nPlaywright + Figma MCP"),
]
for x, color, title, body in cards:
    box(ax, x, 24, 26, 26, "", fc="#FFFFFF", ec=color, lw=1.6)
    # 标题条
    box(ax, x, 42, 26, 8, title, fc=color, ec=color, tc="#FFFFFF", fs=12.5, bold=True)
    txt(ax, x + 13, 34, body, fs=10.5, c=DARK)

# 底部能力曲线
arrow(ax, 8, 15, 92, 15, c=GRAY, lw=2.5, ms=20)
txt(ax, 18, 11, "读码", fs=13, c=BLUE, bold=True)
txt(ax, 50, 11, "改码", fs=13, c=TEAL, bold=True)
txt(ax, 82, 11, "造应用", fs=13, c=PURP, bold=True)
txt(ax, 18, 7.5, "理解陌生代码库", fs=9, c=MID)
txt(ax, 50, 7.5, "添加/重构/调试", fs=9, c=MID)
txt(ax, 82, 7.5, "从设计到成品", fs=9, c=MID)

fig.savefig(OUT + "图1_三大项目总览.png", dpi=220, facecolor="white")
plt.close(fig)

# ============================================================
# 图2 · Agentic Coding 闭环
# ============================================================
fig, ax = new_ax(10, 6.4, (0, 100), (0, 66))
txt(ax, 40, 62, "Agentic Coding：一个自主的闭环", fs=18, c=DARK, bold=True)

nodes = [
    (26, 42, BLUE,  "规划 Plan",   "拆解任务\n制定步骤"),
    (52, 20, TEAL,  "执行 Act",    "调用工具\n读写 / 运行 / 终端"),
    (26, 2,  AMBER, "观察 Observe", "读取结果\n与报错"),
    (6,  20, PURP,  "迭代 Iterate", "修正方案\n继续循环"),
]
for x, y, color, title, note in nodes:
    box(ax, x, y, 20, 12, "", fc="#FFFFFF", ec=color, lw=1.6)
    txt(ax, x + 10, y + 8.5, title, fs=12, c=color, bold=True)
    txt(ax, x + 10, y + 3.6, note, fs=8.8, c=DARK)

# 闭环箭头（顺时针）
arrow(ax, 46, 48, 58, 32, c=BLUE, rad=-0.22)
arrow(ax, 62, 20, 46, 14, c=TEAL, rad=-0.22)
arrow(ax, 26, 8, 22, 16, c=AMBER, rad=-0.22)
arrow(ax, 16, 32, 30, 42, c=PURP, rad=-0.22)

# 中心
ell = Ellipse((36, 22), 16, 12, fc=GRAY_L, ec=GRAY, lw=1.4, zorder=1)
ax.add_patch(ell)
txt(ax, 36, 24, "智能体", fs=11.5, c=DARK, bold=True)
txt(ax, 36, 20, "自主闭环", fs=9.5, c=MID)

# 右侧对比框
box(ax, 76, 16, 23, 16, "", fc=GRAY_L, ec=GRAY, lw=1.4, ls="--")
txt(ax, 87.5, 28, "传统问答式", fs=11.5, c=GRAY, bold=True)
txt(ax, 87.5, 23, "你问 → 它答", fs=10, c=DARK)
txt(ax, 87.5, 19.5, "单回合 · 不自主", fs=9, c=MID)

fig.savefig(OUT + "图2_Agentic闭环.png", dpi=220, facecolor="white")
plt.close(fig)

# ============================================================
# 图3 · RAG 聊天机器人架构
# ============================================================
fig, ax = new_ax(10, 6.6, (0, 100), (0, 68))
txt(ax, 50, 64, "RAG 聊天机器人 · 架构", fs=18, c=DARK, bold=True)

# React 前端
box(ax, 30, 50, 40, 9, "React 前端 · 聊天界面", fc=BLUE_L, ec=BLUE, tc=BLUE, fs=13, bold=True)
# FastAPI 后端
box(ax, 30, 30, 40, 9, "FastAPI 后端 · API 服务", fc=TEAL_L, ec=TEAL, tc=TEAL, fs=13, bold=True)
# 向量库 + LLM
box(ax, 4, 4, 40, 11, "向量数据库\n检索相关文档", fc=AMBER_L, ec=AMBER, tc=AMBER, fs=11.5, bold=True)
box(ax, 56, 4, 40, 11, "大模型 LLM\n生成回答", fc=PURP_L, ec=PURP, tc=PURP, fs=11.5, bold=True)

# 箭头 + 编号标签
arrow(ax, 43, 50, 43, 39, c=BLUE)            # ① 前端 → 后端
txt(ax, 39, 44.5, "① 提问", fs=9.5, c=BLUE, ha="right")
arrow(ax, 57, 39, 57, 50, c=TEAL)            # ⑤ 流式返回（后端→前端）
txt(ax, 61, 44.5, "⑤ 流式返回", fs=9.5, c=TEAL, ha="left")

arrow(ax, 34, 30, 24, 15, c=AMBER)           # ② 后端 → 向量库
txt(ax, 22, 23, "② 检索", fs=9.5, c=AMBER, ha="right")
arrow(ax, 26, 15, 40, 30, c=AMBER)           # ③ 向量库 → 后端
txt(ax, 38, 23, "③ 上下文", fs=9.5, c=AMBER, ha="left")

arrow(ax, 66, 30, 76, 15, c=PURP)            # ④ 后端 → LLM
txt(ax, 79, 23, "④ 生成", fs=9.5, c=PURP, ha="left")

fig.savefig(OUT + "图3_RAG架构.png", dpi=220, facecolor="white")
plt.close(fig)

# ============================================================
# 图5 · git worktree 并行开发
# ============================================================
fig, ax = new_ax(10, 6.6, (0, 100), (0, 68))
txt(ax, 50, 64, "git worktree 并行开发：一个仓库，多个 Claude Code 实例", fs=16, c=DARK, bold=True)

# main 主仓库
box(ax, 4, 26, 26, 14, "main 主仓库", fc=GRAY_L, ec=GRAY, tc=DARK, fs=13, bold=True)

# 三个 worktree
wts = [
    (52, 46, BLUE, "worktree A · 实例 #1", "开发功能 A"),
    (52, 28, TEAL, "worktree B · 实例 #2", "开发功能 B"),
    (52, 10, AMBER, "worktree C · 实例 #3", "修复 Bug"),
]
for x, y, color, title, note in wts:
    box(ax, x, y, 40, 11, "", fc="#FFFFFF", ec=color, lw=1.6)
    txt(ax, x + 20, y + 7, title, fs=11.5, c=color, bold=True)
    txt(ax, x + 20, y + 3.5, note, fs=10, c=DARK)

# 合并框
box(ax, 16, 2, 30, 10, "合并回 main / 提 PR", fc=PURP_L, ec=PURP, tc=PURP, fs=11.5, bold=True)

# 分支箭头 main → worktree
arrow(ax, 30, 40, 52, 54, c=GRAY, rad=-0.15)
arrow(ax, 30, 34, 52, 36, c=GRAY, rad=0.0)
arrow(ax, 30, 28, 52, 18, c=GRAY, rad=0.15)
txt(ax, 41, 50, "git worktree add", fs=9, c=MID)

# 合并箭头 worktree → merge
arrow(ax, 62, 46, 40, 12, c=GRAY, rad=0.15)
arrow(ax, 62, 28, 36, 12, c=GRAY, rad=0.05)
arrow(ax, 62, 10, 40, 11, c=GRAY, rad=-0.05)

fig.savefig(OUT + "图5_git_worktree并行.png", dpi=220, facecolor="white")
plt.close(fig)

print("done")
