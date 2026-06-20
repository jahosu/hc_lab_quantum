# Outputs and reports for the first week assignment of HCLAB Quantum Computing

Team: 
    HCLAB3

Members:
    - Matin Heidari Khayat
    - Joshua Heitbreder

## Task1 - Environment Setup Check
### Output:
```
Counts: {'0': 10}
```

## Task2 -  Single-Qubit Playground
### Output:
```
{'0': 1000}

{'1': 1000}

{'1': 506, '0': 494}
```
### Explanation
Measurement frequencies approximate the theoretical probabilities predicted by quantum mechanics. The states |0⟩ and |1⟩ always produce outcomes 0 and 1 respectively, while |+⟩ produces 0 and 1 with approximately equal frequency. Small deviations from the expected probabilities occur because only a finite number of shots are measured.

## Task3 - Two Qubits & Bell State
### Output:
```
Basis State |00>
{'00': 2000}

Basis State |01>
{'01': 2000}

Basis State |10>
{'10': 2000}

Basis State |11>
{'11': 2000}

Bell State |Φ⁺>
{'00': 993, '11': 1007}
```

## Task4 - Angle Encoding
### Output:
| x    | θ (rad) | Theory p(1) | Empirical p(1) |
| ---- | ------- | ----------- | -------------- |
| 0.00 | 0.000   | 0.000       | 0.000          |
| 0.25 | 0.785   | 0.146       | 0.150          |
| 0.50 | 1.571   | 0.500       | 0.483          |
| 0.75 | 2.356   | 0.854       | 0.835          |
| 1.00 | 3.142   | 1.000       | 1.000          |



### Explanation:
The empirical frequencies closely matched the theoretical probabilities for all tested values of (x). For example, the predicted probabilities of 0.146, 0.500, and 0.854 corresponded to observed frequencies of 0.150, 0.483, and 0.835, respectively. The small discrepancies are expected due to statistical fluctuations from using a finite number of measurement shots.
