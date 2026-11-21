from typing import List, Dict

class FeatureAttributor:
    @staticmethod
    def compute_linear_attribution(weights: List[float], values: List[float], feature_names: List[str]) -> Dict[str, float]:
        attributions = {}
        for w, v, name in zip(weights, values, feature_names):
            attributions[name] = round(w * v, 4)
        return attributions
