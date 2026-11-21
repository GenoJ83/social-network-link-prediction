import random
from typing import List, Callable, Dict

class PermutationImportance:
    @staticmethod
    def calculate(score_fn: Callable[[List[List[float]]], float], data: List[List[float]], feature_names: List[str]) -> Dict[str, float]:
        if not data or not feature_names:
            return {}
        baseline_score = score_fn(data)
        importances = {}
        n_features = len(feature_names)
        for col_idx in range(n_features):
            permuted = [list(row) for row in data]
            col_vals = [row[col_idx] for row in permuted]
            random.shuffle(col_vals)
            for row_idx in range(len(permuted)):
                permuted[row_idx][col_idx] = col_vals[row_idx]
            new_score = score_fn(permuted)
            importances[feature_names[col_idx]] = round(max(0.0, baseline_score - new_score), 4)
        return importances
