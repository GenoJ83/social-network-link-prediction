# Social Network Link Prediction: Graph Neural Networks (GCN & GraphSAGE)

![Graph ML](https://img.shields.io/badge/Graph%20ML-PyTorch-red)
![Models](https://img.shields.io/badge/Models-GCN%20%7C%20GraphSAGE-blue)
![NetworkX](https://img.shields.io/badge/NetworkX-Topology-orange)
![License](https://img.shields.io/badge/License-MIT-green)

A graph representation learning system for link prediction and friend recommendation on complex scale-free networks.

## Architecture
```mermaid
flowchart LR
    Graph[Social Graph & Node Features] --> GCN[GCN / GraphSAGE Encoder]
    GCN --> Embed[Node Latent Vectors]
    Embed --> Decoder[Bilinear Link Scorer]
    Decoder --> Recs[Ranked Candidate Edges]
```

## Quick Verification
```bash
python -c "from src.eda.graph_stats import analyze_graph_topology; analyze_graph_topology()"
```
