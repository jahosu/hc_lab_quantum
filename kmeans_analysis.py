"""
CSV and plotting helpers for the Week 3 Hybrid Quantum K-means


"""

from __future__ import annotations

from pathlib import Path
from typing import Any, Dict, Iterable, List, Sequence
import csv

import matplotlib.pyplot as plt


def save_csv(rows: Iterable[Dict[str, Any]], fieldnames: Sequence[str], path: str) -> None:
    """Save dictionaries as a CSV file."""
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def plot_quantum_kmeans_clusters(data, assignments, centroids, save_path: str) -> None:
    """Plot final 2D cluster assignments and centroids."""
    Path(save_path).parent.mkdir(parents=True, exist_ok=True)

    plt.figure()
    for cluster_id in sorted(set(assignments)):
        xs = [item["vector"][0] for item, a in zip(data, assignments) if a == cluster_id]
        ys = [item["vector"][1] for item, a in zip(data, assignments) if a == cluster_id]
        labels = [item.get("label", "") for item, a in zip(data, assignments) if a == cluster_id]
        plt.scatter(xs, ys, label=f"cluster {cluster_id}")
        for x, y, label in zip(xs, ys, labels):
            if label:
                plt.text(x, y, f" {label}")

    cx = [c["vector"][0] for c in centroids]
    cy = [c["vector"][1] for c in centroids]
    plt.scatter(cx, cy, marker="x", s=100, label="centroids")
    for idx, (x, y) in enumerate(zip(cx, cy)):
        plt.text(x, y, f" c{idx}")

    plt.xlabel("v0")
    plt.ylabel("v1")
    plt.title("Hybrid Quantum K-means clusters")
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.tight_layout()
    plt.savefig(save_path)
    plt.close()


def plot_quantum_kmeans_convergence(convergence_rows: List[Dict[str, Any]], save_path: str) -> None:
    """Plot number of changed assignments per iteration."""
    Path(save_path).parent.mkdir(parents=True, exist_ok=True)

    iterations = [int(r["iteration"]) for r in convergence_rows]
    num_changed = [int(r["num_changed"]) for r in convergence_rows]

    plt.figure()
    plt.plot(iterations, num_changed, marker="o")
    plt.xlabel("iteration")
    plt.ylabel("changed assignments")
    plt.title("Hybrid Quantum K-means convergence")
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(save_path)
    plt.close()
