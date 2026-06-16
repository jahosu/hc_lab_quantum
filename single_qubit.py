"""
Week 1 – Task 2: Single-Qubit Playground

TODOs:
- Implement basic single-qubit state preparations (|0⟩, |1⟩, |+⟩).
- Implement run_and_plot() to execute circuits and optionally save histograms.
- Use main() to orchestrate the runs and dump plots into results/week1/.
"""

from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator, AerError
import matplotlib.pyplot as plt
from pathlib import Path


def get_simulator():
    return AerSimulator(method="statevector")


def prepare_zero():
    """
    TODO:
    - Build a minimal circuit that measures the default |0⟩ state.
    """
    qc = QuantumCircuit(1, 1)
    qc.measure(0, 0)
    return qc


def prepare_one():
    """
    TODO:
    - Create a single-qubit circuit, flip it to |1⟩, and record the result.
    """
    qc = prepare_zero()
    qc.x(0)
    qc.measure(0, 0)
    return qc


def prepare_plus():
    """
    TODO:
    - Produce the |+⟩ state from |0⟩, then measure.
    """    
    qc = prepare_zero()
    qc.h(0)
    qc.measure(0, 0)
    return qc

def run_and_plot(circuit, shots, title, save_path=None):
    """
    TODO:
    - Execute the provided circuit with the simulator, report counts,
      and optionally store a simple matplotlib histogram.
    """
    simulator = get_simulator()
    qc_t = transpile(circuit, simulator)
    result = simulator.run(qc_t, shots=shots).result()
    counts = result.get_counts()
    print(f"Counts of {title}: {counts}")
    pass


def main(shots=1000):
    """Run the single-qubit routines and persist plots under results/week1/."""
    Path("results/week1").mkdir(parents=True, exist_ok=True)

    # TODO:
    # Build the three circuits, run them via run_and_plot, and save the figures.
    qc_zero = prepare_zero()
    run_and_plot(qc_zero, shots, "Zero state")

    qc_one = prepare_one()
    run_and_plot(qc_one, shots, "one state")

    qc_plus = prepare_plus()
    run_and_plot(qc_plus, shots, "plus state")

if __name__ == "__main__":
    main()