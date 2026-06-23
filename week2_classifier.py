"""
Week 2 – Task 2 : Tiny Quantum Classifier

- Pick two class prototypes in R^2.
- Compare overlap-based similarities with their classical cosine counterparts.
- Report how often both approaches agree on the label.
"""

from pathlib import Path
from week2_inner_products import estimate_overlap_squared, classical_cosine_similarity
import os 
 
def classify_quantum(x, c0, c1, shots: int = 4000):
    """
    Quantum classifier using overlap estimation.

    Returns:
      (predicted_label, overlap_sq_c0, overlap_sq_c1)
    where predicted_label in {0, 1, None}.

    TODO:
    - Estimate both overlaps via estimate_overlap_squared, choose the higher value (or None on ties), and return the scores.
    """
    overlap_sq_c0 = estimate_overlap_squared(x, c0, shots)
    overlap_sq_c1 = estimate_overlap_squared(x, c1, shots)
    if (overlap_sq_c0 > overlap_sq_c1):
        predicted_label = "0"
    elif (overlap_sq_c0 == overlap_sq_c1):
        predicted_label = "None"
    else:
        predicted_label = "1"
    return predicted_label, overlap_sq_c0, overlap_sq_c1


def classify_classical(x, c0, c1):
    """
    Classical reference classifier using cosine similarity.

    Returns:
      (predicted_label, cos_c0, cos_c1)

    TODO:
    - Evaluate classical_cosine_similarity for both prototypes, compare, and package the result.
    """
    cos_c0 = classical_cosine_similarity(x, c0)
    cos_c1 = classical_cosine_similarity(x, c1)
    if (cos_c0 > cos_c1):
        predicted_label = "0"
    elif (cos_c0 == cos_c1):
        predicted_label = "None"
    else:
        predicted_label = "1"
    
    return predicted_label, cos_c0, cos_c1


def main():
    output_dir = Path("results/week2")
    output_dir.mkdir(parents=True, exist_ok=True)

    # You can change these prototypes if you like.
    c0 = (1.0, 0.0)
    c1 = (0.0, 1.0)

    # Example test vectors
    test_vectors = [
        (1.0, 0.0),
        (0.8, 0.2),
        (0.2, 0.8),
        (0.0, 1.0),
        (1.0, 1.0),
        (1.0, -1.0),
    ]

    shots = 4000

    lines = []
    lines.append("=== Tiny quantum classifier ===")
    lines.append(f"class 0 prototype: {c0}")
    lines.append(f"class 1 prototype: {c1}\n")

    for x in test_vectors:
        # TODO:
        # Invoke both classifiers, note whether they agree, and append a formatted summary line.
        overlap_sq_label = classify_quantum(x, c0, c1, shots)
        cos_label = classify_classical(x, c0, c1)
        lines.append(f"Agreement: {"Agree" if overlap_sq_label[0] == cos_label[0] else "Not Agree"}, Overlap squared label: {overlap_sq_label}, Cosine label: {cos_label}")

    # TODO:
    # Persist the collected lines to results/week2/task2_classifier.txt and also print them.
    with open(os.path.join(output_dir, 'task2_classifier.txt'), "w") as file:
        file.writelines(lines)
    
    for line in lines:
        print(line)


if __name__ == "__main__":
    main()