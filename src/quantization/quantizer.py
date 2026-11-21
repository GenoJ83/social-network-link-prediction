from typing import List, Tuple

class Int8Quantizer:
    @staticmethod
    def calibrate(values: List[float]) -> Tuple[float, int]:
        if not values:
            return 1.0, 0
        min_val, max_val = min(values), max(values)
        if min_val == max_val:
            return 1.0, 0
        scale = (max_val - min_val) / 255.0
        zero_point = int(round(-min_val / scale)) - 128
        zero_point = max(-128, min(127, zero_point))
        return scale, zero_point

    @staticmethod
    def quantize(values: List[float], scale: float, zero_point: int) -> List[int]:
        return [max(-128, min(127, int(round(v / scale)) + zero_point)) for v in values]

    @staticmethod
    def dequantize(quantized: List[int], scale: float, zero_point: int) -> List[float]:
        return [round((q - zero_point) * scale, 4) for q in quantized]
