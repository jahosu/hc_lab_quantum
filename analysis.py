"""
Week 3 – Mini Project: Analysis & Plotting 

Goal:
- Save experiment results under results/week3/
- Generate at least one clear plot for your report

We provide these helpers so you can focus on:
- encoding
- circuit building
- the experiment question itself
"""

from __future__ import annotations

from pathlib import Path
import csv
import matplotlib.pyplot as plt


def save_csv(rows, fieldnames, path):
    """Save a list of dict rows to CSV."""
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def plot_overlap_vs_depth(depths, ideal_vals, noisy_vals=None, save_path=None):
    """
    (Optional extension)
    Plot overlap estimates vs circuit depth.
    """
    plt.figure()
    plt.plot(depths, ideal_vals, marker="o", label="ideal")
    if noisy_vals is not None:
        plt.plot(depths, noisy_vals, marker="o", label="noisy")
    plt.xlabel("extra identity layers (depth)")
    plt.ylabel("estimated |<x|y>|^2")
    plt.title("Overlap vs. circuit depth")
    plt.grid(True, alpha=0.3)
    if noisy_vals is not None:
        plt.legend()
    plt.tight_layout()
    if save_path is not None:
        Path(save_path).parent.mkdir(parents=True, exist_ok=True)
        plt.savefig(save_path)
        plt.close()
    else:
        plt.show()


def plot_similarity_ranking(results, save_path=None):
    """
    Plot overlap scores for similarity search ranking.

    results:
        list of dicts with keys:
            'label' (optional), 'vector' or ('v0','v1'), 'overlap_sq'
    """
    results_sorted = sorted(results, key=lambda r: float(r["overlap_sq"]), reverse=True)

    labels = []
    values = []
    for r in results_sorted:
        lbl = r.get("label")
        if lbl is None:
            if "vector" in r:
                lbl = str(r["vector"])
            elif "v0" in r and "v1" in r:
                lbl = f"({r['v0']},{r['v1']})"
            else:
                lbl = "item"
        labels.append(str(lbl))
        values.append(float(r["overlap_sq"]))

    plt.figure()
    plt.bar(labels, values)
    plt.xlabel("Database entry")
    plt.ylabel("estimated |<q|v>|^2")
    plt.title("Quantum similarity ranking (swap test)")
    plt.xticks(rotation=30, ha="right")
    plt.ylim(0, 1)
    plt.tight_layout()

    if save_path is not None:
        Path(save_path).parent.mkdir(parents=True, exist_ok=True)
        plt.savefig(save_path)
        plt.close()
    else:
        plt.show()


def ensure_results_dir():
    Path("results/week3").mkdir(parents=True, exist_ok=True)
