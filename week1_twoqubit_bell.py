"""
Week 1 – Task 3: Two Qubits & Bell State

TODOs:
- Provide basis-state preparation plus readout for 2 qubits.
- Create a circuit for the Bell state |Φ⁺⟩.
- Implement a helper that runs a 2-qubit circuit and reports the joint distribution (with optional plot).
- Use main() to execute the basis states and the Bell state, storing plots in results/week1/.
"""

from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator, AerError
import matplotlib.pyplot as plt
from pathlib import Path
from qiskit.visualization import plot_histogram

def get_simulator():
    return AerSimulator(method="statevector")


def prepare_basis_state(bits: str):
    """
    TODO:
    - Build a two-qubit circuit reflecting the requested bitstring, respecting Qiskit's bit-order, then measure both qubits.
    """
    qc = QuantumCircuit(2)
    for i, char in enumerate(reversed(bits)):
        if char == '1':
            qc.x(i)

    qc.measure_all()
    return qc


def prepare_bell_phi_plus():
    """
    TODO:
    - Assemble the standard |Φ⁺⟩ entangling routine, include measurements, and return the circuit.
    """
    '''
    qc_zero = prepare_basis_state("00")
    qc_one = prepare_basis_state("11")
    qc_zero.h(0)
    qc_zero.h(1)
    qc_zero.cx()
    '''
    qc = QuantumCircuit(2)
    qc.h(0)
    qc.cx(0, 1)
    qc.measure_all()
    return qc


def run_and_plot_joint(circuit, shots, title, save_path=None):
    """
    TODO:
    - Simulate the circuit, show the joint outcome counts, and optionally persist a histogram.
    """
    simulator = get_simulator()
    qc_t = transpile(circuit, simulator)
    result = simulator.run(qc_t, shots=shots).result()
    counts = result.get_counts()
    
    print(f"\n{title}")
    print(counts)

    fig = plot_histogram(counts, title=title)

    if save_path:
        fig.savefig(save_path, bbox_inches="tight")

    plt.close(fig)

    return counts


def main(shots=2000):
    """
    Run experiments for the four basis states (|00⟩, |01⟩, |10⟩, |11⟩) and the Bell state |Φ⁺⟩.
    Save joint histograms in results/week1/.
    """
    output_dir = Path("results/week1/task3")
    output_dir.mkdir(parents=True, exist_ok=True)

    # TODO:
    # Iterate over the basis states, run them through the helper, and finally do the same for |Φ⁺⟩.
    states = ["00", "01", "10", "11"]
    # Basis states
    for state in states:
        qc = prepare_basis_state(state)
        run_and_plot_joint(
            qc,
            shots,
            f"Basis State |{state}>",
            output_dir / f"basis_{state}.png"
        )

    # Bell state
    qc = prepare_bell_phi_plus()
    run_and_plot_joint(
        qc,
        shots,
        "Bell State |Φ⁺>",
        output_dir / "bell_phi_plus.png"
    )

if __name__ == "__main__":
    main()