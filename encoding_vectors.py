"""
Week 1 – Task 4: Data Encoding

TODOs:
- Implement angle encoding for scalars in [0,1].
- (Optional) Implement simple amplitude encoding for 2D vectors.
- (Optional) Implement basis encoding for 2-bit strings.
"""

from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator, AerError
import math
from pathlib import Path
from qiskit.quantum_info import Statevector

def get_simulator():
    return AerSimulator(method="statevector")


def build_angle_encoding_circuit(x: float):
    """
    Build a 1-qubit circuit that encodes a scalar x in [0,1]
    using an Ry rotation and then measures.

    Suggestion:
    - Map x to a single-qubit rotation, apply it, and finish with a measurement.
    """
    qc = QuantumCircuit(1)
    theta = x * math.pi
    qc.ry(theta, 0)
    return qc
 

def run_angle_encoding(xs, shots=1000):
    """
    For a list xs of scalars: build and run a circuit for each,
    and output the frequency of outcome '1'.

    TODO:
    - Use the simulator to iterate over xs, execute the encoding, and report the observed p(1).
    """
    simulator = get_simulator()
    for x in xs:
        x_enc = build_angle_encoding_circuit(x)
        qc_t = transpile(x_enc, simulator)

        # Get the exact statevector
        state = Statevector.from_instruction(qc_t)

        # Get the probability of measuring 1
        prob_1 = state.probabilities(qargs=[0])[1]
        print(prob_1)


def build_amplitude_encoding_circuit(v0: float, v1: float):
    """
    (Optional)
    Build a 1-qubit circuit that prepares (v0, v1), after normalization,
    approximately as the amplitudes of the qubit.

    Idea:
    - Normalize the vector.
    - Fix a phase convention: if the first normalized component is negative,
      multiply the whole normalized vector by -1.
    - Then choose an RY rotation for the nonnegative first component and, if the
      adjusted second component is negative, apply Z to encode the relative sign.
    """
    pass


def run_amplitude_encoding(vectors, shots=1000):
    """
    (Optional)
    For a list of 2D vectors: build and run circuits and observe
    qualitative differences in the measurement statistics.

    TODO:
    - For every vector, simulate the encoding, inspect counts, and relate p(1) to the second component.
    """
    pass


def basis_encoding_2bit(bitstrings, shots=1000):
    """
    (Optional) Basis encoding for 2-bit vectors into two qubits.
    Checks whether the measurement results match the bitstrings.

    NOTE:
    - We follow Qiskit's output convention: qubit 0 is the rightmost bit.
      So the bitstring "01" means qubit1=0, qubit0=1.

    TODO:
    - Validate each bitstring, prepare the matching computational basis state, run the simulator, and show the counts.
    """
    pass


def main():
    Path("results/week1").mkdir(parents=True, exist_ok=True)

    xs = [0.0, 0.25, 0.5, 0.75, 1.0]
    run_angle_encoding(xs, shots=1000)

    # Optional parts:
    # vectors = [(1, 0), (0, 1), (1, 1), (1, -1)]
    # run_amplitude_encoding(vectors, shots=1000)
    # basis_encoding_2bit(["00", "01", "10", "11"], shots=1000)


if __name__ == "__main__":
    main()