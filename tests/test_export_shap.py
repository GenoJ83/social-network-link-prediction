import json
from src.explainability.export_shap import ExplanationExporter

def test_export_shap():
    attr = {"feat1": 0.5, "feat2": -0.2}
    raw_json = ExplanationExporter.to_json("sample_99", attr)
    data = json.loads(raw_json)
    assert data["sample_id"] == "sample_99"
    assert data["attributions"]["feat1"] == 0.5

    raw_csv = ExplanationExporter.to_csv(attr)
    assert "feature,attribution" in raw_csv
    assert "feat1,0.5" in raw_csv
