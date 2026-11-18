from src.monitoring.alert_dispatcher import DriftAlertDispatcher

def test_alert_dispatcher():
    payload = DriftAlertDispatcher.build_alert_payload("ks_feature_age", 0.35, "CRITICAL")
    assert payload["alert"] == "MODEL_DRIFT_DETECTED"
    assert payload["action_required"] == "RETRAIN_RECOMMENDED"
