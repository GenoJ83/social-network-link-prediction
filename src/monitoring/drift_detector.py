from typing import List, Tuple

class KsDriftDetector:
    @staticmethod
    def compute_ks_statistic(baseline: List[float], current: List[float]) -> float:
        if not baseline or not current:
            return 0.0
        s_base = sorted(baseline)
        s_curr = sorted(current)
        all_vals = sorted(list(set(s_base + s_curr)))
        max_d = 0.0
        n1, n2 = len(s_base), len(s_curr)
        for v in all_vals:
            cdf1 = sum(1 for x in s_base if x <= v) / n1
            cdf2 = sum(1 for x in s_curr if x <= v) / n2
            d = abs(cdf1 - cdf2)
            if d > max_d:
                max_d = d
        return round(max_d, 4)

    @staticmethod
    def is_drifted(statistic: float, threshold: float = 0.25) -> bool:
        return statistic >= threshold
