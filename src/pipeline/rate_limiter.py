import time

class InferenceRateLimiter:
    def __init__(self, max_qps: int = 100):
        self.interval = 1.0 / max_qps
        self.last_call = 0.0

    def allow(self) -> bool:
        now = time.time()
        if now - self.last_call >= self.interval:
            self.last_call = now
            return True
        return False
