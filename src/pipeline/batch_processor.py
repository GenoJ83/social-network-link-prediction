from typing import List, Callable, Generator, Any

class BatchFeatureProcessor:
    @staticmethod
    def chunk_records(records: List[Any], chunk_size: int = 10) -> Generator[List[Any], None, None]:
        for i in range(0, len(records), chunk_size):
            yield records[i:i + chunk_size]

    @staticmethod
    def process_batch(records: List[Any], transform_fn: Callable[[Any], Any], chunk_size: int = 10) -> List[Any]:
        results = []
        for chunk in BatchFeatureProcessor.chunk_records(records, chunk_size):
            for item in chunk:
                results.append(transform_fn(item))
        return results
