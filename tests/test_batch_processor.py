from src.pipeline.batch_processor import BatchFeatureProcessor

def test_batch_processor():
    records = list(range(25))
    res = BatchFeatureProcessor.process_batch(records, lambda x: x * 2, chunk_size=10)
    assert len(res) == 25
    assert res[0] == 0 and res[-1] == 48
