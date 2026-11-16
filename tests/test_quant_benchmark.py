from src.quantization.benchmark import QuantizationBenchmark

def test_quant_benchmark():
    res = QuantizationBenchmark.compare_latency(lambda: sum(range(100)), lambda: sum(range(50)), iterations=20)
    assert res["iterations"] == 20
    assert "speedup_ratio" in res
