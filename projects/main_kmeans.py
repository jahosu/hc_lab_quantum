"""
Entry point for the Week 3 Hybrid Quantum K-means .


"""

from __future__ import annotations

import argparse
from pathlib import Path

from .kmeans import run_quantum_kmeans, classical_overlap_squared
from .kmeans_analysis import (
    save_csv,
    plot_quantum_kmeans_clusters,
    plot_quantum_kmeans_convergence,
)

DEFAULT_SEED = 123


def build_demo_data():
    """Small 2D data set with two direction-based clusters."""
    return [
        {"label": "A", "vector": (1.0, 0.1)},
        {"label": "B", "vector": (0.9, 0.2)},
        {"label": "C", "vector": (0.1, 1.0)},
        {"label": "D", "vector": (0.2, 0.9)},
        {"label": "E", "vector": (0.8, 0.4)},
        {"label": "F", "vector": (0.4, 0.8)},
    ]


def run_topic_b_quantum_kmeans(k: int = 2, max_iter: int = 5, shots: int = 1000, classical_debug: bool = False):
    """Run the hybrid Quantum K-means extension and save CSV/plot outputs."""
    Path("results/week3").mkdir(parents=True, exist_ok=True)

    data = build_demo_data()
    overlap_fn = classical_overlap_squared if classical_debug else None

    result = run_quantum_kmeans(
        data,
        k=k,
        max_iter=max_iter,
        shots=shots,
        seed=DEFAULT_SEED,
        overlap_fn=overlap_fn,
    )

    save_csv(
        result["assignment_rows"],
        fieldnames=[
            "iteration",
            "point_id",
            "point_label",
            "x0",
            "x1",
            "assigned_cluster",
            "best_overlap_sq",
            "best_distance_q",
        ],
        path="results/week3/quantum_kmeans_assignments.csv",
    )

    save_csv(
        result["score_rows"],
        fieldnames=[
            "iteration",
            "point_id",
            "point_label",
            "x0",
            "x1",
            "cluster",
            "centroid_label",
            "c0",
            "c1",
            "shots",
            "overlap_sq",
            "distance_q",
            "count_0",
            "count_1",
        ],
        path="results/week3/quantum_kmeans_scores.csv",
    )

    save_csv(
        result["centroid_rows"],
        fieldnames=["iteration", "cluster", "centroid_label", "c0", "c1"],
        path="results/week3/quantum_kmeans_centroids.csv",
    )

    save_csv(
        result["convergence_rows"],
        fieldnames=["iteration", "num_changed", "stable"],
        path="results/week3/quantum_kmeans_convergence.csv",
    )

    plot_quantum_kmeans_clusters(
        data,
        result["assignments"],
        result["centroids"],
        save_path="results/week3/quantum_kmeans_clusters.png",
    )
    plot_quantum_kmeans_convergence(
        result["convergence_rows"],
        save_path="results/week3/quantum_kmeans_convergence.png",
    )

    mode = "classical debug overlap" if classical_debug else "swap-test overlap"
    print(f"Hybrid Quantum K-means finished using {mode}.")
    print("Final assignments:")
    for item, cluster_id in zip(data, result["assignments"]):
        print(f"  {item['label']}: cluster {cluster_id}")
    print("Saved outputs under results/week3/quantum_kmeans_*")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--k", type=int, default=2)
    parser.add_argument("--max-iter", type=int, default=5)
    parser.add_argument("--shots", type=int, default=1000)
    parser.add_argument(
        "--classical-debug",
        action="store_true",
        help="Use exact classical squared cosine instead of the swap-test estimator.",
    )
    args = parser.parse_args()
    run_topic_b_quantum_kmeans(
        k=args.k,
        max_iter=args.max_iter,
        shots=args.shots,
        classical_debug=args.classical_debug,
    )


if __name__ == "__main__":
    main()
