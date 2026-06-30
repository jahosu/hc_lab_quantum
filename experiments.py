"""
Week 3 – Mini Project: Experiments 

This module contains experiment loops:
- build circuits (via project.circuits)
- run them on Aer backends
- return numerical results (counts / overlap estimates) 

In Week 3 we want a clean separation:
    circuits.py     -> circuit construction only
    experiments.py  -> running circuits + collecting numbers   
    analysis.py     -> CSV saving + plotting (provided helper)
    main.py         -> entry point (provided helper)

Required TODOs in this file:
- get_backend(...)
- _transpile(...)
- estimate_overlap_squared(...)
- run_similarity_search(...)

Optional extension:
- run_depth_noise_study(...)

 technical points (so your results make sense):
- If noise_model is provided, use method='density_matrix' (noise is non-unitary).
- For depth studies, keep optimization_level=0 so identity layers are not optimized away.
-  seeds make runs reproducible across machines.
"""

from __future__ import annotations

from pathlib import Path
from typing import Optional, List, Dict, Any, Tuple

from qiskit import transpile
from qiskit_aer import AerSimulator
from qiskit_aer.noise import NoiseModel

from .circuits import build_swap_test, build_swap_test_with_identity_layers


def ensure_results_dir() -> None:
    """Create results/week3/ if it does not exist."""
    Path("results/week3").mkdir(parents=True, exist_ok=True)


def _clip01(x: float) -> float:
    return max(0.0, min(1.0, x))


def get_backend(noise_model: Optional[NoiseModel] = None) -> AerSimulator:
    """
    Return an Aer backend.

    Hint:
      - Ideal simulation 
      - Noisy simulation
    """
    # TODO: implement
    if noise_model is None:
        return AerSimulator(method="statevector")
    return AerSimulator(method="density_matrix", noise_model=noise_model)


def _transpile(
    qc,
    backend: AerSimulator,
    *,
    noise_model: Optional[NoiseModel] = None,
    seed_transpiler: Optional[int] = None,
    optimization_level: int = 0,
):
    """
    Transpile helper to keep behaviour consistent across experiments.

    Hint:
      - If a noise_model is provided, set basis_gates=noise_model.basis_gates
        (so transpile stays within the gate set where noise is attached).
      - For this lab, use optimization_level=0.
    """
    # TODO: implement
    if noise_model is not None:
        return transpile(qc, backend, basis_gates=noise_model.basis_gates, seed_transpiler=seed_transpiler, optimization_level=optimization_level)
    else:
        return transpile(qc, backend, seed_transpiler=seed_transpiler, optimization_level=optimization_level)


def estimate_overlap_squared(
    vx,
    vy,
    shots: int = 2000,
    noise_model: Optional[NoiseModel] = None,
    seed_simulator: Optional[int] = None,
    seed_transpiler: Optional[int] = None,
) -> Tuple[float, Dict[str, int]]:
    """
    Run swap test and estimate |<x|y>|^2.

    Returns:
        (overlap_sq, counts)

    Relationship:
        p0 = P(ancilla=0) = (1 + |<x|y>|^2)/2
        => |<x|y>|^2 = clip(2*p0 - 1, 0, 1)

    """
    # TODO: implement
    sim = get_backend()
    qc = build_swap_test(vx, vy)
    qc_t = _transpile(qc, sim, noise_model=noise_model, seed_transpiler=seed_transpiler)
    # TODO: perform the simulation, process counts, and return the result.
    result = sim.run(qc_t, shots=shots, seed_simulator=seed_simulator).result()
    counts = result.get_counts()
    p_zero = counts['0'] / shots
    return max(min(2 * p_zero - 1, 1), 0), counts


def run_similarity_search(
    query: Dict[str, Any],
    database: List[Dict[str, Any]],
    shots: int = 2000,
    seed_simulator: Optional[int] = None,
    seed_transpiler: Optional[int] = None,
) -> List[Dict[str, Any]]:
    """
    - compute overlaps between query and each vector in database
    - rank by overlap (descending)

    Expected return format (list of dicts), e.g.:
      [{"label":"A","vector":(1,0),"overlap_sq":1.0}, ...]
    """
    # TODO: implement
    results = []
    for row in database:
        overlap_sq, _ = estimate_overlap_squared(query["vector"], row["vector"], shots)
        results.append({"label": row["label"], "vector": row["vector"], "overlap_sq": overlap_sq})
    return results

def run_depth_noise_study(
    vx,
    vy,
    depths,
    shots: int = 2000,
    noise_model: Optional[NoiseModel] = None,
    seed_simulator: Optional[int] = None,
    seed_transpiler: Optional[int] = None,
) -> List[float]:
    """
    (Optional extension)
    Run overlap estimation for a list of depths by inserting identity layers.

    Hint:
      - use build_swap_test_with_identity_layers(vx, vy, depth_layers=d)
      - keep optimization_level=0 so layers are not optimized away
      - return a list of overlap_sq values aligned with depths
    """
    # Optional TODO: implement if you do the extension
    sim = get_backend()
    overlap_sq_list = []
    for depth in depths:
        qc = build_swap_test_with_identity_layers(vx, vy, depth)
        qc_t = _transpile(qc, sim, noise_model=noise_model, seed_transpiler=seed_transpiler)
        # TODO: perform the simulation, process counts, and return the result.
        result = sim.run(qc_t, shots=shots, seed_simulator=seed_simulator).result()
        counts = result.get_counts()
        p_zero = counts['0'] / shots
        overlap_sq_list.append(max(min(2 * p_zero - 1, 1), 0))
    return overlap_sq_list
