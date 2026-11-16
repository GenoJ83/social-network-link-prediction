from typing import List

class MagnitudePruner:
    @staticmethod
    def compute_mask(weights: List[float], target_sparsity: float = 0.5) -> List[int]:
        if not weights:
            return []
        sorted_abs = sorted(abs(w) for w in weights)
        threshold_idx = int(len(weights) * target_sparsity)
        threshold = sorted_abs[min(threshold_idx, len(sorted_abs) - 1)]
        return [1 if abs(w) >= threshold else 0 for w in weights]

    @staticmethod
    def prune_weights(weights: List[float], mask: List[int]) -> List[float]:
        return [w * m for w, m in zip(weights, mask)]
