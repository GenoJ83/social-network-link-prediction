from src.explainability.waterfall_visualizer import AsciiWaterfallVisualizer

def test_waterfall_visualizer():
    attr = {"feature_age": 1.25, "feature_income": -0.5}
    chart = AsciiWaterfallVisualizer.render(attr, base_value=10.0)
    assert "Base Value: 10.00" in chart
    assert "feature_age" in chart
    assert "Final Prediction: 10.75" in chart
