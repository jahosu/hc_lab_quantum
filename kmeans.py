"""
Hybrid Quantum K-means.

"""

from __future__ import annotations

from typing import Any, Callable, Dict, List, Optional, Sequence, Tuple
import math
import random

try:
    from experiments import estimate_overlap_squared
except Exception:  # pragma: no cover - only used if package imports are incomplete
    estimate_overlap_squared = None

Vector2 = Tuple[float, float]
Item = Dict[str, Any]
OverlapResult = Tuple[float, Dict[str, int]]
OverlapFn = Callable[[Vector2, Vector2, int, Optional[int], Optional[int]], OverlapResult]


def _as_vector(item: Any) -> Vector2:
    """Return a 2D vector from either a dict with key 'vector' or a tuple/list."""
    if isinstance(item, dict):
        item = item["vector"]
    if len(item) != 2:
        raise ValueError("Expected a 2D vector.")
    return (float(item[0]), float(item[1]))


def _label(item: Any, fallback: str) -> str:
    if isinstance(item, dict):
        return str(item.get("label", fallback))
    return fallback


def _norm(v: Vector2) -> float:
    return math.sqrt(v[0] * v[0] + v[1] * v[1])


def classical_overlap_squared(
    vx: Vector2,
    vy: Vector2,
    shots: int = 0,
    seed_simulator: Optional[int] = None,
    seed_transpiler: Optional[int] = None,
) -> OverlapResult:
    """
    Classical debugging helper: compute squared cosine similarity exactly.

    This is useful for testing your K-means logic before running quantum circuits.
    """
    nx = _norm(vx)
    ny = _norm(vy)
    if nx == 0 or ny == 0:
        raise ValueError("Cannot compare zero vectors.")
    dot = vx[0] * vy[0] + vx[1] * vy[1]
    return (dot / (nx * ny)) ** 2, {}


def quantum_overlap_squared(
    vx: Vector2,
    vy: Vector2,
    shots: int = 1000,
    seed_simulator: Optional[int] = None,
    seed_transpiler: Optional[int] = None,
) -> OverlapResult:
    """Call the swap-test estimator from the existing Week 3 experiment code."""
    if estimate_overlap_squared is None:
        raise RuntimeError("Could not import project.experiments.estimate_overlap_squared.")
    return estimate_overlap_squared(
        vx,
        vy,
        shots=shots,
        seed_simulator=seed_simulator,
        seed_transpiler=seed_transpiler,
    )


def initialize_centroids(data: Sequence[Item], k: int, seed: int = 123) -> List[Item]:
    """
    Pick k initial centroids.

    TODO
    """
    centroids = random.choices(data, k=k)
    return centroids


def assign_points_quantum(
    data: Sequence[Item],
    centroids: Sequence[Item],
    shots: int = 1000,
    seed_simulator: Optional[int] = None,
    seed_transpiler: Optional[int] = None,
    overlap_fn: Optional[OverlapFn] = None,
    iteration: int = 0,
) -> Tuple[List[int], List[Dict[str, Any]], List[Dict[str, Any]]]:
    """
    Assign every point to the centroid with the largest overlap_sq.

    Returns:
        assignments:
            list of cluster IDs, one per data point
        assignment_rows:
            one row per data point with the winning cluster
        score_rows:
            one row per point-centroid comparison

    TODO:
    - loop over points and centroids
    - estimate overlap_sq(point, centroid)
    - choose the centroid with the largest overlap_sq
    - store enough information for CSV analysis
    """

    
    score_rows = []
    assignment_rows = []
    for point in data:
        point_centroid_distanceq = []
        for centroid in centroids:
            s = estimate_overlap_squared(_as_vector(point), _as_vector(centroid), shots, None, seed_simulator, seed_transpiler)
            score_rows.append({"point_label": point["label"], "centroid_label": centroid["label"], "overlap_sq": s, "distance_q": 1-s})
            point_centroid_distanceq.append([point["label"], centroid["label"], 1-s])
        point_centroid_distanceq.sort(key=lambda x: x[2])
        assignment_rows.append({"point_label": point["label"], "centroid_label": centroid["label"]})
    assignments = list(map(lambda x: x["centroid_label"], assignment_rows))
    return assignments, assignment_rows, score_rows


def update_centroids_classical(
    data: Sequence[Item],
    assignments: Sequence[int],
    k: int,
    old_centroids: Optional[Sequence[Item]] = None,
) -> List[Item]:
    """
    Update each centroid as the arithmetic mean of assigned raw vectors.

    TODO:
    - collect points by cluster ID
    - compute the mean vector for each non-empty cluster
    - decide how to handle empty clusters, 
    """
    raise NotImplementedError("TODO: implement update_centroids_classical(...)")


def run_quantum_kmeans(
    data: Sequence[Item],
    k: int = 2,
    max_iter: int = 5,
    shots: int = 1000,
    seed: int = 123,
    initial_centroids: Optional[Sequence[Item]] = None,
    overlap_fn: Optional[OverlapFn] = None,
) -> Dict[str, Any]:
    """
    Run the full hybrid Quantum K-means loop.

    TODO:
    - initialize centroids
    - alternate assignment and centroid update
    - stop when assignments do not change
    - return a dict with final centroids, assignments, and CSV rows
    """
    raise NotImplementedError("TODO: implement run_quantum_kmeans(...)")
