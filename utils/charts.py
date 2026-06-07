import matplotlib.pyplot as plt
import matplotlib
matplotlib.use("Agg")

def progress_pie(completed: int, total: int):
    remaining = total - completed
    fig, ax = plt.subplots(figsize=(4, 4))
    ax.pie(
        [completed, remaining],
        labels=["Completed", "Remaining"],
        colors=["#4CAF50", "#FF5252"],
        autopct="%1.0f%%",
        startangle=90,
        wedgeprops={"edgecolor": "white", "linewidth": 2}
    )
    ax.set_title("Study Progress", fontsize=13, fontweight="bold")
    plt.tight_layout()
    return fig

def subject_bar(plan: list):
    from collections import Counter
    counts = Counter(e["subject"] for e in plan if e["completed"])
    if not counts:
        return None
    fig, ax = plt.subplots(figsize=(6, 3))
    ax.bar(counts.keys(), counts.values(), color="#2196F3", edgecolor="white")
    ax.set_title("Completed Sessions by Subject", fontsize=12)
    ax.set_ylabel("Sessions")
    plt.xticks(rotation=20, ha="right")
    plt.tight_layout()
    return fig