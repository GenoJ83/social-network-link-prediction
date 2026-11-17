from typing import List

def compute_sparsity_ratio(weights: List[float]) -> float:
    if not weights:
        return 0.0
    zero_count = sum(1 for w in weights if abs(w) < 1e-9)
    return round(zero_count / len(weights), 4)
