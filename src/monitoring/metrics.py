from typing import Dict, Any

def summarize_drift(metrics: Dict[str, float]) -> Dict[str, Any]:
    return {"total_features_monitored": len(metrics), "drifted_features": [k for k, v in metrics.items() if v > 0.25]}
