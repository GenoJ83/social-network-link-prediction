# Feature Extraction & Pipeline Architecture

This subsystem orchestrates streaming chunked batch processing, DAG execution stages, and feature vector caching.

- **BatchFeatureProcessor**: Memory-bounded stream chunking
- **FeatureVectorCache**: Content-addressed SHA-256 caching
- **DagStageRunner**: Deterministic stage composition
