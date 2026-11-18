from typing import Dict, Any

class DriftAlertDispatcher:
    @staticmethod
    def build_alert_payload(metric_name: str, score: float, severity: str) -> Dict[str, Any]:
        return {
            "alert": "MODEL_DRIFT_DETECTED",
            "metric": metric_name,
            "score": score,
            "severity": severity,
            "action_required": "RETRAIN_RECOMMENDED" if severity == "CRITICAL" else "MONITOR"
        }
