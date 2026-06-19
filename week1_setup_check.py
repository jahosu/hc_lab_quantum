
"""
Week 1 – Task 1: Environment Setup Check

"""

from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator, AerError


def get_simulator():
    return AerSimulator(method="statevector")


def build_circuit():
    qc = QuantumCircuit(1, 1)
    qc.measure(0, 0)
    return qc
    


def main():
    simulator = get_simulator()
    qc = build_circuit()
    qc_t = transpile(qc, simulator)
    result = simulator.run(qc_t, shots=10).result()
    counts = result.get_counts()
    print("Counts:", counts)
    


if __name__ == "__main__":
    main()
