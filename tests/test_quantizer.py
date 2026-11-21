from src.quantization.quantizer import Int8Quantizer

def test_quantizer():
    data = [-1.0, 0.0, 0.5, 1.0]
    scale, zp = Int8Quantizer.calibrate(data)
    assert scale > 0
    q = Int8Quantizer.quantize(data, scale, zp)
    assert len(q) == 4
    assert all(-128 <= v <= 127 for v in q)
    deq = Int8Quantizer.dequantize(q, scale, zp)
    assert len(deq) == 4
