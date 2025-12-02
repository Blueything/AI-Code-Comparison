import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyArrowPatch

# ---------- dark mode colors ----------
bg_color       = "#0f172a"
gemini_color   = "#10b981"
chatgpt_color  = "#3b82f6"
question_color = "#1e293b"
text_light     = "#f1f5f9"
text_muted     = "#94a3b8"
arrow_color    = "#475569"
line_color     = "#334155"

# ---------- figure setup ----------
fig, ax = plt.subplots(figsize=(12, 14), facecolor=bg_color)
ax.set_facecolor(bg_color)
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_axis_off()

# ---------- helper functions ----------
def draw_box(x, y, text, color, width=0.22, height=0.05, fontsize=10, bold=True):
    rect = mpatches.FancyBboxPatch(
        (x - width/2, y - height/2),
        width, height,
        boxstyle="round,pad=0.01,rounding_size=0.015",
        facecolor=color,
        edgecolor=color if color == question_color else color,
        linewidth=2,
        alpha=0.9
    )
    ax.add_patch(rect)
    
    weight = "bold" if bold else "normal"
    ax.text(x, y, text, ha="center", va="center",
            fontsize=fontsize, fontweight=weight, color=text_light)


def draw_question_box(x, y, text):
    width, height = 0.26, 0.055
    rect = mpatches.FancyBboxPatch(
        (x - width/2, y - height/2),
        width, height,
        boxstyle="round,pad=0.01,rounding_size=0.015",
        facecolor=question_color,
        edgecolor=line_color,
        linewidth=2
    )
    ax.add_patch(rect)
    ax.text(x, y, text, ha="center", va="center",
            fontsize=11, fontweight="bold", color=text_light)


def draw_result_box(x, y, label, model, model_color):
    # Label text
    ax.text(x, y + 0.015, label, ha="center", va="center",
            fontsize=9, color=text_muted)
    
    # Model box
    width, height = 0.18, 0.045
    rect = mpatches.FancyBboxPatch(
        (x - width/2, y - 0.025 - height/2),
        width, height,
        boxstyle="round,pad=0.01,rounding_size=0.015",
        facecolor=model_color,
        edgecolor=model_color,
        linewidth=0,
        alpha=0.2
    )
    ax.add_patch(rect)
    
    border = mpatches.FancyBboxPatch(
        (x - width/2, y - 0.025 - height/2),
        width, height,
        boxstyle="round,pad=0.01,rounding_size=0.015",
        facecolor="none",
        edgecolor=model_color,
        linewidth=2
    )
    ax.add_patch(border)
    
    ax.text(x, y - 0.025, model, ha="center", va="center",
            fontsize=10, fontweight="bold", color=model_color)


def draw_line(x1, y1, x2, y2):
    ax.plot([x1, x2], [y1, y2], color=line_color, lw=2, solid_capstyle="round")


def draw_arrow(x1, y1, x2, y2):
    ax.annotate(
        "",
        xy=(x2, y2),
        xytext=(x1, y1),
        arrowprops=dict(
            arrowstyle="-|>",
            lw=2,
            color=line_color,
            mutation_scale=15
        )
    )


# ---------- positions ----------
start_y = 0.92
q1_y = 0.82
branch1_y = 0.72
q2_y = 0.58
branch2_y = 0.48
q3_y = 0.34
branch3_y = 0.24

main_x = 0.55
left_x = 0.25

# ---------- draw title ----------
ax.text(
    0.5, 0.97,
    "Decision Tree: Gemini 3 Pro vs ChatGPT-5",
    ha="center", va="center",
    fontsize=16, fontweight="bold",
    color=text_light
)

# ---------- START ----------
draw_box(main_x, start_y, "START", "#334155", width=0.12, height=0.04)

# Line: START → Q1
draw_arrow(main_x, start_y - 0.02, main_x, q1_y + 0.03)

# ---------- QUESTION 1 ----------
draw_question_box(main_x, q1_y, "What do you need?")

# Branch lines from Q1
draw_line(main_x, q1_y - 0.03, main_x, branch1_y + 0.05)
draw_line(main_x, branch1_y + 0.05, left_x, branch1_y + 0.05)
draw_arrow(left_x, branch1_y + 0.05, left_x, branch1_y - 0.01)

# ChatGPT-5 result (left branch)
draw_result_box(left_x, branch1_y - 0.04, "Fast ideas / UI experiments", "ChatGPT-5", chatgpt_color)

# Continue line to Q2
draw_arrow(main_x, branch1_y + 0.05, main_x, q2_y + 0.03)

# Gemini label on the continuing path
ax.text(main_x + 0.15, (branch1_y + 0.05 + q2_y + 0.03) / 2, "Polished, structured output",
        ha="left", va="center", fontsize=9, color=text_muted)

# ---------- QUESTION 2 ----------
draw_question_box(main_x, q2_y, "What matters?")

# Branch lines from Q2
draw_line(main_x, q2_y - 0.03, main_x, branch2_y + 0.05)
draw_line(main_x, branch2_y + 0.05, left_x, branch2_y + 0.05)
draw_arrow(left_x, branch2_y + 0.05, left_x, branch2_y - 0.01)

# ChatGPT-5 result (left branch)
draw_result_box(left_x, branch2_y - 0.04, "Quick UI/UX tweaks", "ChatGPT-5", chatgpt_color)

# Continue line to Q3
draw_arrow(main_x, branch2_y + 0.05, main_x, q3_y + 0.03)

# Gemini label on the continuing path
ax.text(main_x + 0.15, (branch2_y + 0.05 + q3_y + 0.03) / 2, "Clean code & comments",
        ha="left", va="center", fontsize=9, color=text_muted)

# ---------- QUESTION 3 ----------
draw_question_box(main_x, q3_y, "Project type?")

# Branch lines from Q3
draw_line(main_x, q3_y - 0.03, main_x, branch3_y + 0.05)
draw_line(main_x, branch3_y + 0.05, left_x, branch3_y + 0.05)
draw_arrow(left_x, branch3_y + 0.05, left_x, branch3_y - 0.01)

# ChatGPT-5 result (left branch)
draw_result_box(left_x, branch3_y - 0.04, "Creative / playful", "ChatGPT-5", chatgpt_color)

# Final Gemini result (continue down)
draw_arrow(main_x, branch3_y + 0.05, main_x, branch3_y - 0.01)
draw_result_box(main_x, branch3_y - 0.04, "Stable / client-ready", "Gemini 3 Pro", gemini_color)

# ---------- legend ----------
ax.text(0.08, 0.08, "●", fontsize=14, color=chatgpt_color, ha="center", va="center")
ax.text(0.12, 0.08, "ChatGPT-5 — Fast, expressive, experimental", 
        fontsize=10, color=text_muted, ha="left", va="center")

ax.text(0.08, 0.04, "●", fontsize=14, color=gemini_color, ha="center", va="center")
ax.text(0.12, 0.04, "Gemini 3 Pro — Polished, stable, structured", 
        fontsize=10, color=text_muted, ha="left", va="center")

plt.tight_layout(pad=1)
plt.savefig("decision_tree_vertical.png", dpi=250, facecolor=bg_color, bbox_inches="tight")
plt.show()