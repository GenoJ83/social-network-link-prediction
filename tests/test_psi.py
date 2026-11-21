from src.monitoring.psi import PsiCalculator

def test_psi_calculator():
    base = [float(i) for i in range(100)]
    targ_similar = [float(i) for i in range(100)]
    psi_stable = PsiCalculator.calculate_psi(base, targ_similar)
    assert PsiCalculator.categorize_psi(psi_stable) == "STABLE"

    targ_drift = [float(i + 50) for i in range(100)]
    psi_drift = PsiCalculator.calculate_psi(base, targ_drift)
    assert PsiCalculator.categorize_psi(psi_drift) in ["MODERATE_DRIFT", "SIGNIFICANT_DRIFT"]
