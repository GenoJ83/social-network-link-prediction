from src.monitoring.drift_detector import KsDriftDetector

def test_drift_detector():
    base = [1.0, 2.0, 3.0, 4.0, 5.0]
    curr_same = [1.1, 2.1, 2.9, 4.1, 4.9]
    d_same = KsDriftDetector.compute_ks_statistic(base, curr_same)
    assert KsDriftDetector.is_drifted(d_same, threshold=0.5) is False

    curr_drift = [10.0, 11.0, 12.0, 13.0, 14.0]
    d_drift = KsDriftDetector.compute_ks_statistic(base, curr_drift)
    assert KsDriftDetector.is_drifted(d_drift, threshold=0.5) is True
