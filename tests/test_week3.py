
from project.experiments import run_similarity_search


def test_similarity_search_ranking_top_is_identical():
    database = [
        {"label": "A", "vector": (1.0, 0.0)},
        {"label": "B", "vector": (0.0, 1.0)},
        {"label": "C", "vector": (1.0, 1.0)},
        {"label": "D", "vector": (1.0, -1.0)},
    ]
    query = {"label": "q", "vector": (1.0, 0.0)}

    results = run_similarity_search(query, database, shots=4096, seed_simulator=123)
    assert len(results) == len(database)

    # highest overlap should be for the identical vector (1,0)
    top = results[0]
    assert top["label"] == "A"
    assert top["overlap_sq"] > 0.8
