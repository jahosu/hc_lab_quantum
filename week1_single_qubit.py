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
from qiskit.visualization import plot_histogram

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
    print(f"\n{counts}")
    
    fig = plot_histogram(counts, title=title)

    if save_path:
        fig.savefig(save_path, bbox_inches="tight")

    plt.close(fig)

    return counts


def main(shots=1000):
    """Run the single-qubit routines and persist plots under results/week1/."""
    output_dir = Path("results/week1/task2")
    output_dir.mkdir(parents=True, exist_ok=True)

    # TODO:
    # Build the three circuits, run them via run_and_plot, and save the figures.
    circuits = [
        ("|0>", prepare_zero(), output_dir / "zero_hist.png"),
        ("|1>", prepare_one(), output_dir / "one_hist.png"),
        ("|+>", prepare_plus(), output_dir / "plus_hist.png"),
    ]

    for title, qc, save_path in circuits:
        run_and_plot(
            qc,
            shots,
            title,
            save_path
        )

if __name__ == "__main__":
    main()