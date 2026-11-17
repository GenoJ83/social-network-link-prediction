import math
from typing import List

class PsiCalculator:
    @staticmethod
    def calculate_psi(baseline: List[float], target: List[float], bins: int = 5) -> float:
        if not baseline or not target:
            return 0.0
        min_v, max_v = min(baseline), max(baseline)
        if min_v == max_v:
            return 0.0
        step = (max_v - min_v) / bins
        psi = 0.0
        for i in range(bins):
            b_low = min_v + i * step
            b_high = b_low + step
            p_base = max(1e-5, sum(1 for x in baseline if b_low <= x < b_high) / len(baseline))
            p_targ = max(1e-5, sum(1 for x in target if b_low <= x < b_high) / len(target))
            psi += (p_targ - p_base) * math.log(p_targ / p_base)
        return round(abs(psi), 4)

    @staticmethod
    def categorize_psi(psi: float) -> str:
        if psi < 0.1: return "STABLE"
        if psi < 0.25: return "MODERATE_DRIFT"
        return "SIGNIFICANT_DRIFT"
