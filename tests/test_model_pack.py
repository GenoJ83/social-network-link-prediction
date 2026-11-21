from src.quantization.model_pack import ModelPacker

def test_model_packer():
    meta = {"model_name": "net", "version": "1.0"}
    weights = {"w1": [1, 2, 3]}
    payload = ModelPacker.serialize_to_json(meta, weights)
    restored = ModelPacker.deserialize_from_json(payload)
    assert restored["metadata"]["model_name"] == "net"
    assert restored["weights"]["w1"] == [1, 2, 3]
