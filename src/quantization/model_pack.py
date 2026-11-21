import json
from typing import Dict, Any

class ModelPacker:
    @staticmethod
    def serialize_to_json(metadata: Dict[str, Any], weights: Dict[str, Any]) -> str:
        return json.dumps({"metadata": metadata, "weights": weights}, indent=2)

    @staticmethod
    def deserialize_from_json(raw_json: str) -> Dict[str, Any]:
        return json.loads(raw_json)
