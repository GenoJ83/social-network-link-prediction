# Quantization & Model Optimization Guide

This module enables int8 post-training quantization, magnitude-based weight pruning, and model size optimization for high-throughput edge and production serving.

- **Int8Quantizer**: Linear min-max zero-point calibration
- **MagnitudePruner**: Unstructured pruning with configurable sparsity ratios
- **Latency Benchmark**: Automated fp32 vs int8 inference throughput testing
