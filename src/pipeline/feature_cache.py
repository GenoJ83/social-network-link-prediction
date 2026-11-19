import hashlib
import json
from typing import Dict, Any, Optional

class FeatureVectorCache:
    def __init__(self, capacity: int = 500):
        self.capacity = capacity
        self.cache: Dict[str, Any] = {}

    def _hash_key(self, raw_input: Any) -> str:
        s = json.dumps(raw_input, sort_keys=True)
        return hashlib.sha256(s.encode()).hexdigest()[:16]

    def get(self, raw_input: Any) -> Optional[Any]:
        return self.cache.get(self._hash_key(raw_input))

    def put(self, raw_input: Any, features: Any) -> None:
        if len(self.cache) >= self.capacity:
            oldest = next(iter(self.cache))
            del self.cache[oldest]
        self.cache[self._hash_key(raw_input)] = features
