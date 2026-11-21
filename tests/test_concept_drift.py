from src.monitoring.concept_drift import SlidingWindowDriftMonitor

def test_concept_drift_monitor():
    mon = SlidingWindowDriftMonitor(window_size=5, max_error_rate=0.6)
    assert mon.record_prediction(is_error=False) is False
    assert mon.record_prediction(is_error=True) is False
    assert mon.record_prediction(is_error=True) is True
