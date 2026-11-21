from src.pipeline.feature_cache import FeatureVectorCache

def test_feature_cache():
    cache = FeatureVectorCache(capacity=2)
    k1 = {"feature_a": 10}
    k2 = {"feature_a": 20}
    k3 = {"feature_a": 30}
    cache.put(k1, [1.0, 0.0])
    cache.put(k2, [2.0, 0.0])
    assert cache.get(k1) == [1.0, 0.0]
    cache.put(k3, [3.0, 0.0])
    assert len(cache.cache) == 2
