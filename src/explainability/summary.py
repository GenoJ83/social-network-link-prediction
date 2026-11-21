from typing import Dict, List

def top_k_features(attributions: Dict[str, float], k: int = 3) -> List[str]:
    return [name for name, _ in sorted(attributions.items(), key=lambda x: abs(x[1]), reverse=True)[:k]]
