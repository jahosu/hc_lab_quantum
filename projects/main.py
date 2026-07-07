"""
Week 3 – Mini Project: Main Entry Point 

Run:
    python -m project.main

Expected outputs (after you implement the TODOs in encoding.py / circuits.py):
- results/week3/similarity_search.csv
- results/week3/similarity_ranking.png
"""

from __future__ import annotations

from .experiments import (
    ensure_results_dir as ensure_exp_dir,
    run_similarity_search,
)
from ..analysis import (
    ensure_results_dir as ensure_ana_dir,
    save_csv,
    plot_similarity_ranking,
)

DEFAULT_SEED = 123


def run_topic_a_similarity_search():
    """
    quantum similarity search on a tiny 2D database.

    After you implemented encoding + swap test, this should run end-to-end and generate
    outputs under results/week3/.
    """
    database = [
        {"label": "A", "vector": (1.0, 0.0)},
        {"label": "B", "vector": (0.0, 1.0)},
        {"label": "C", "vector": (1.0, 1.0)},
        {"label": "D", "vector": (1.0, -1.0)},
    ]
    query = {"label": "q", "vector": (1.0, 0.0)}

    shots_list = [200, 500, 1000, 2000, 4000]
    seed = DEFAULT_SEED

    rows = []
    print(" Week 3: Similarity search (swap test) ")
    print(f"Seed: {seed}")
    print(f"Query: {query['vector']}")
    print("Database:")
    for item in database:
        print(f"  {item['label']}: {item['vector']}")
    print()

    for shots in shots_list:
        results = run_similarity_search(
            query,
            database,
            shots=shots,
            seed_simulator=seed,
            seed_transpiler=seed,
        )
        print(
            f"Shots = {shots:<5d}  Ranking: "
            + ", ".join([f"{r['label']}({r['overlap_sq']:.3f})" for r in results])
        )
        for r in results:
            v0, v1 = r["vector"]
            rows.append({"shots": shots, "label": r.get("label"), "v0": v0, "v1": v1, "overlap_sq": r["overlap_sq"]})

    csv_path = "results/week3/similarity_search.csv"
    save_csv(rows, fieldnames=["shots", "label", "v0", "v1", "overlap_sq"], path=csv_path)

    max_shots = max(shots_list)
    best_rows = [r for r in rows if r["shots"] == max_shots]
    plot_path = "results/week3/similarity_ranking.png"
    plot_similarity_ranking(best_rows, save_path=plot_path)

    print()
    print(f"Saved CSV : {csv_path}")
    print(f"Saved plot: {plot_path}")
    print("\nIf you got an exception above, it is likely because you still have TODOs in project/encoding.py or project/circuits.py.")


def main():
    ensure_exp_dir()
    ensure_ana_dir()
    run_topic_a_similarity_search()


if __name__ == "__main__":
    main()
