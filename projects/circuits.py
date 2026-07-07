"""
Week 3 – Mini Project: Circuit Builders 

Goal:
- Provide small circuit-building functions used by experiments.
- Keep this file focused on constructing circuits (not running them).

uses:
- build_swap_test(vx, vy)

Optional depth/noise extension uses:
- build_swap_test_with_identity_layers(vx, vy, depth_layers)

 technical note:
If you increase depth with identity operations, the transpiler may optimize them away.
To avoid that, insert barriers in your identity blocks and transpile with
optimization_level=0 (already done in experiments.py).
"""

from __future__ import annotations

from qiskit import QuantumCircuit
from .encoding import amplitude_encode_2d
import math

def _add_identity_layer(qc: QuantumCircuit, qubits: list[int]):
    """Add an identity layer that survives transpiler optimizations."""
    for q in qubits:
        qc.h(q)
    qc.barrier(*qubits)
    for q in qubits:
        qc.h(q)
    qc.barrier(*qubits)


def build_swap_test(vx, vy):
    """
    Build a 3-qubit swap test circuit to estimate |<x|y>|^2.

    Qubits:
        0 ancilla
        1 holds |x>
        2 holds |y>

    Measurement:
        ancilla -> classical bit 0

    TODO:
    - Create a full swap test circuit using amplitude_encode_2d to prepare |x> and |y>.
    - Return the circuit.

    """

    qc = QuantumCircuit(3, 1)
    anc, qx, qy = 0, 1, 2

    amplitude_encode_2d(qc, qx, vx)
    amplitude_encode_2d(qc, qy, vy)
    
    qc.h(anc)
    qc.cswap(anc, qx, qy)
    qc.h(anc)
    qc.measure(anc, 0)
    return qc


def build_swap_test_with_identity_layers(vx, vy, depth_layers: int):
    """
    (Optional extension)
    Swap test with additional identity layers to increase depth.

    The identity layers do not change the logical function, but they increase gate count,
    so noise has more opportunities to corrupt the computation.

    TODO:
    - Start with the swap test circuit from build_swap_test.
    - Add `depth_layers` identity layers  between the state preparation and the CSWAP gate.
    - Return the circuit.
    """
    qc = build_swap_test(vx, vy)
    qubits = [] if depth_layers == 0 else range(3, depth_layers+3) 
    _add_identity_layer(qc, qubits)
    qc.measure_all()
    return qc
