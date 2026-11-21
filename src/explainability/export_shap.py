import json
import csv
import io
from typing import Dict, Any

class ExplanationExporter:
    @staticmethod
    def to_json(sample_id: str, attributions: Dict[str, float]) -> str:
        return json.dumps({"sample_id": sample_id, "attributions": attributions}, indent=2)

    @staticmethod
    def to_csv(attributions: Dict[str, float]) -> str:
        output = io.StringIO()
        writer = csv.writer(output)
        writer.writerow(["feature", "attribution"])
        for k, v in attributions.items():
            writer.writerow([k, v])
        return output.getvalue()
