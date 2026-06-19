from qiskit import transpile
from qiskit_aer import AerSimulator

import week1_setup_check
import single_qubit
import week1_twoqubit_bell
import week1_encoding_vectors

_sim = AerSimulator(method="statevector")


def run_counts(circuit, shots=1024):
    circ_t = transpile(circuit, _sim)
    result = _sim.run(circ_t, shots=shots).result()
    return result.get_counts()


def test_setup_check_has_measure():
    qc = week1_setup_check.build_circuit()
    assert qc.num_qubits == 1
    assert qc.num_clbits == 1
    assert any(op[0].name == "measure" for op in qc.data)


def test_single_qubit_zero_one():
    qc0 = single_qubit.prepare_zero()
    counts0 = run_counts(qc0, shots=256)
    assert list(counts0.keys()) == ["0"]

    qc1 = single_qubit.prepare_one()
    counts1 = run_counts(qc1, shots=256)
    assert list(counts1.keys()) == ["1"]


def test_single_qubit_plus_superposition():
    qc_plus = single_qubit.prepare_plus()
    counts = run_counts(qc_plus, shots=2048)
    assert "0" in counts and "1" in counts
    p0 = counts["0"] / 2048
    p1 = counts["1"] / 2048
    assert 0.3 < p0 < 0.7
    assert 0.3 < p1 < 0.7


def test_twoqubit_basis_states():
    for bits in ["00", "01", "10", "11"]:
        qc = week1_twoqubit_bell.prepare_basis_state(bits)
        counts = run_counts(qc, shots=256)
        assert list(counts.keys()) == [bits]


def test_bell_state_phi_plus():
    qc = week1_twoqubit_bell.prepare_bell_phi_plus()
    counts = run_counts(qc, shots=4096)
    assert set(counts.keys()).issubset({"00", "11"})
    p00 = counts.get("00", 0) / 4096
    p11 = counts.get("11", 0) / 4096
    assert 0.35 < p00 < 0.65
    assert 0.35 < p11 < 0.65


def test_angle_encoding_runs():
    xs = [0.0, 0.5, 1.0]
    for x in xs:
        qc = week1_encoding_vectors.build_angle_encoding_circuit(x)
        counts = run_counts(qc, shots=256)
        assert set(counts.keys()).issubset({"0", "1"})