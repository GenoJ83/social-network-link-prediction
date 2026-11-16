import time
from typing import Callable, Dict, Any

class QuantizationBenchmark:
    @staticmethod
    def compare_latency(fp_fn: Callable, quant_fn: Callable, iterations: int = 50) -> Dict[str, Any]:
        t0 = time.perf_counter()
        for _ in range(iterations): fp_fn()
        fp_time = time.perf_counter() - t0

        t1 = time.perf_counter()
        for _ in range(iterations): quant_fn()
        quant_time = time.perf_counter() - t1

        return {
            "iterations": iterations,
            "fp32_ms": round((fp_time / iterations) * 1000, 3),
            "int8_ms": round((quant_time / iterations) * 1000, 3),
            "speedup_ratio": round(fp_time / (quant_time + 1e-9), 2)
        }
