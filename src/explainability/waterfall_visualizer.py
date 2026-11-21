from typing import Dict

class AsciiWaterfallVisualizer:
    @staticmethod
    def render(attributions: Dict[str, float], base_value: float = 0.0) -> str:
        lines = [f"Base Value: {base_value:.2f}"]
        accum = base_value
        for name, val in attributions.items():
            accum += val
            sign = "+" if val >= 0 else "-"
            lines.append(f"{name:<18} | {sign}{abs(val):>6.2f} => {accum:>6.2f}")
        lines.append(f"Final Prediction: {accum:.2f}")
        return "\n".join(lines)
