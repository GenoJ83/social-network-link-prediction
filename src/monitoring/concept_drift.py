from typing import List

class SlidingWindowDriftMonitor:
    def __init__(self, window_size: int = 20, max_error_rate: float = 0.3):
        self.window_size = window_size
        self.max_error_rate = max_error_rate
        self.history: List[int] = []

    def record_prediction(self, is_error: bool) -> bool:
        self.history.append(1 if is_error else 0)
        if len(self.history) > self.window_size:
            self.history.pop(0)
        current_error_rate = sum(self.history) / len(self.history)
        return current_error_rate > self.max_error_rate
