"""
Week 2 – Task 3: Noise Sensitivity Study (Depth Sweep)

You will:
- build an overlap estimation circuit (swap test),
- run it on an ideal simulator and on a noisy simulator,
- increase circuit depth by inserting *identity layers*,
- record how the overlap estimate degrades with depth under noise,
- save a CSV + plot under results/week2/.

  technical notes:
1) Noisy simulation should use method='density_matrix'.
2) Identity layers must NOT be optimized away:
   - insert barriers in the identity blocks
   - use transpile(..., optimization_level=0)
3) Noise must be attached to gates that actually appear after transpilation:
   - the identity layers explicitly use H gates, so include noise for 'h'
     and/or for the one-qubit basis gates produced by transpilation
   - the controlled-SWAP may appear as 'cswap' or be decomposed into
     one- and two-qubit gates; attach noise to the gate names that actually occur
4) Use separate depolarizing_error objects for 1q, 2q, and 3q gates:
   - depolarizing_error(p1, 1)
   - depolarizing_error(p2, 2)
   - depolarizing_error(p3, 3)


"""

from __future__ import annotations

from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator, AerError
from qiskit_aer.noise import NoiseModel, depolarizing_error
from pathlib import Path
import csv
import matplotlib.pyplot as plt

# Reuse your encoding from Task 1:
from week2_inner_products import prepare_vector_state

DEFAULT_SEED = 123


def get_backend(noise_model: NoiseModel | None = None):
    """
    Return an Aer backend.

    Recommended approach:
    - ideal (noise_model is None): statevector
    - noisy: density_matrix with noise_model
    """
    if noise_model is None:
        return AerSimulator(method="statevector")
    return AerSimulator(method="density_matrix", noise_model=noise_model)


def build_noise_model(p1: float = 0.01, p2: float = 0.02, p3: float = 0.03) -> NoiseModel:
    """
    Build a simple depolarizing noise model.

    NOTE:
    - We attach noise to a conservative list of gate names to ensure it matches
      the transpiled circuit.

    TODO:
    - Create depolarizing errors for 1q/2q/3q gates, register them for the relevant operations, and return the model.
    """
    pass


def _add_identity_layer(qc: QuantumCircuit, qubits: list[int]):
    """Add an identity layer that survives transpiler optimizations."""
    for q in qubits:
        qc.h(q)
    qc.barrier(*qubits)
    for q in qubits:
        qc.h(q)
    qc.barrier(*qubits)


def build_overlap_circuit_with_depth(vx, vy, depth_layers: int) -> QuantumCircuit:
    """
    Build an overlap estimation circuit (swap test) for fixed vectors vx, vy,
    and increase circuit depth by inserting 'identity layers'.

    Identity layer example:
      - H on some qubits, barrier, H again (overall identity)

    TODO:
    - Prepare both encodings, wrap the swap-test sequence, sprinkle the requested identity blocks, and finish with measurement.
    """
    qc = QuantumCircuit(3, 1)
    anc, qx, qy = 0, 1, 2

    # TODO: fill in the described structure.
    return qc


def estimate_overlap_from_counts(counts: dict, shots: int) -> float:
    """Estimate |<x|y>|^2 from ancilla counts."""
    p0 = counts.get("0", 0) / shots
    overlap_sq = 2 * p0 - 1
    return max(0.0, min(1.0, overlap_sq))


def run_study():
    Path("results/week2").mkdir(parents=True, exist_ok=True)

    vx = (1.0, 0.0)
    vy = (1.0, 1.0)

    depths = [0, 1, 2, 3, 4, 5]
    shots = 4000
    seed = DEFAULT_SEED

    # TODO:
    # Build the noise model plus the ideal and noisy backends.
    rows = []

    # TODO:
    # Loop over depths, generate the circuit, run both simulations with optimization_level=0,
    # store the overlap estimates, and print progress.
    pass

    # TODO:
    # Write rows to results/week2/noise_overlap_vs_depth.csv.
    # Plot the curves and save results/week2/noise_overlap_vs_depth.png.
    pass


def main():
    run_study()


if __name__ == "__main__":
    main()