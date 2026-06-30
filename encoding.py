
"""
Week 3 – Mini Project: Encoding

Goal:
- Provide reusable encoding functions for the rest of the project.
- Reuse ideas from Week 1 and Week 2.

"""

from qiskit import QuantumCircuit
import math


def normalize_2d(v):
    """
    Normalize a 2D real vector.

    Returns:
        (v0_norm, v1_norm, norm)

    TODO:
    - compute Euclidean norm
    - raise ValueError for the zero vector
    """
    v0, v1 = v
    norm = math.sqrt(v0 * v0 + v1 * v1)
    if norm == 0.0:
        raise ValueError("Cannot normalize the zero vector.")
    return v0 / norm, v1 / norm, norm


def amplitude_encode_2d(qc: QuantumCircuit, qubit: int, v):
    """
    Amplitude-encode a 2D real vector v=(v0,v1) on the given qubit
    using a single RY rotation.

    
    TODO:
    - implement the encoding on 'qc'
    """
    nomalized_v = normalize_2d(v)
    nomalized_v = [-1 * nomalized_v[0], -1 * nomalized_v[1]] if nomalized_v[0] < 0 else nomalized_v
    thetta = 2 * math.acos(nomalized_v[0])

    qc.ry(thetta, qubit)


def angle_encode_scalar(qc: QuantumCircuit, qubit: int, x, theta_fn=None):
    """
    Angle-encode a scalar x into a 1-qubit state via RY(theta(x)).

    Default mapping:
        theta(x) = pi * x

    TODO:
    - define default theta mapping if theta_fn is None
    - apply RY(theta) on the target qubit
    """
    theta = x * math.pi if theta_fn is None else theta_fn(x)
    qc.ry(theta, qubit)
    return qc
