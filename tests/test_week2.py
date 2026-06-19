
import math
import week2_inner_products as w2


def test_classical_metrics_basic():
    assert abs(w2.classical_cosine_similarity((1.0, 0.0), (1.0, 0.0)) - 1.0) < 1e-9
    assert abs(w2.classical_cosine_similarity((1.0, 0.0), (0.0, 1.0)) - 0.0) < 1e-9
    assert abs(w2.classical_distance((1.0, 0.0), (1.0, 0.0)) - 0.0) < 1e-9
    assert abs(w2.classical_distance((1.0, 0.0), (0.0, 1.0)) - math.sqrt(2)) < 1e-9


def test_swap_test_overlap_identical():
    overlap, _ = w2.estimate_overlap_squared((1.0, 0.0), (1.0, 0.0), shots=4096)
    assert overlap > 0.8


def test_swap_test_overlap_orthogonal():
    overlap, _ = w2.estimate_overlap_squared((1.0, 0.0), (0.0, 1.0), shots=4096)
    assert overlap < 0.2
