from src.explainability.feature_attribution import FeatureAttributor

def test_feature_attribution():
    w = [0.5, -0.2, 1.5]
    x = [2.0, 10.0, 1.0]
    names = ["f1", "f2", "f3"]
    attr = FeatureAttributor.compute_linear_attribution(w, x, names)
    assert attr["f1"] == 1.0
    assert attr["f2"] == -2.0
    assert attr["f3"] == 1.5
