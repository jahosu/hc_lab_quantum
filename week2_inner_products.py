"""
Week 2 – Task 1: Inner Products & Distances (Swap Test)

You will:
- amplitude-encode 2D real vectors into 1-qubit states,
- build a swap test circuit to estimate the overlap |<x|y>|^2,
- compare to classical cosine similarity and Euclidean distance,
- write a small summary text file 

Reminder (swap test):
  p(ancilla=0) = (1 + |<x|y>|^2) / 2
  => |<x|y>|^2 = 2*p0 - 1


"""

from __future__ import annotations

from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator, AerError
import math
from pathlib import Path

DEFAULT_SEED = 123


def get_simulator():
    return AerSimulator(method="statevector")


def normalize_2d(v):
    """Normalize a 2D real vector and return (v0_n, v1_n, norm)."""
    v0, v1 = v
    norm = math.sqrt(v0 * v0 + v1 * v1)
    if norm == 0.0:
        raise ValueError("Cannot normalize the zero vector.")
    return v0 / norm, v1 / norm, norm


def prepare_vector_state(qc: QuantumCircuit, qubit: int, v):
    """
    Amplitude-encode a 2D real vector v=(v0, v1) on the given qubit.

    
    TODO:
    - Implement the encoding on the provided circuit.
    """
    pass


def build_swap_test_circuit(vx, vy):
    """
    Build a 3-qubit swap-test circuit to estimate |<x|y>|^2.

    Qubit 0: ancilla
    Qubit 1: data qubit for |x>
    Qubit 2: data qubit for |y>

    Steps:
    - Prepare both states, execute the standard swap-test pattern, and measure the ancilla.
    """
    qc = QuantumCircuit(3, 1)
    anc, qx, qy = 0, 1, 2

    # TODO: insert the swap-test routine.
    return qc


def estimate_overlap_squared(
    vx,
    vy,
    shots: int = 2000,
    seed_simulator: int | None = None,
    seed_transpiler: int | None = None,
):
    """
    Run the swap-test circuit and estimate |<x|y>|^2 from measurement counts.

    Returns:
      (overlap_sq, counts)

    TODO:
    - Execute the transpiled circuit with the chosen seeds, infer p(ancilla=0), and convert it to |<x|y>|^2.
    """
    sim = get_simulator()
    qc = build_swap_test_circuit(vx, vy)

    qc_t = transpile(qc, sim, optimization_level=0, seed_transpiler=seed_transpiler)

    # TODO: perform the simulation, process counts, and return the result.
    pass


def classical_cosine_similarity(vx, vy):
    """
    Classical cosine similarity:
      cos(x, y) = (x·y) / (||x|| * ||y||)

    TODO:
    - Implement the basic dot-product formula with normalization and proper error handling.
    """
    pass


def classical_distance(vx, vy):
    """
    Classical Euclidean distance:
      ||x - y||_2

    TODO:
    - Compute the standard L2 distance for two 2D vectors.
    """
    pass


def main():
    Path("results/week2").mkdir(parents=True, exist_ok=True)

    shots = 4000
    seed = DEFAULT_SEED

    pairs = [
        ((1.0, 0.0), (1.0, 0.0)),    # identical
        ((1.0, 0.0), (0.0, 1.0)),    # orthogonal
        ((1.0, 0.0), (-1.0, 0.0)),   # opposite direction: cosine=-1, overlap=1
    ]

    lines = []
    lines.append("=== Inner products and distances (quantum vs classical) ===\n")

    for vx, vy in pairs:
        # TODO:
        # Use the helper functions to gather quantum and classical metrics, then log the comparison.
        pass

    # TODO: dump the collected summary into results/week2/task1_summary.txt and print it.
    pass


if __name__ == "__main__":
    main()