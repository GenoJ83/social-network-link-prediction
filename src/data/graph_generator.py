"""Synthetic scale-free social network graph generator (Barabasi-Albert)."""
import networkx as nx
import numpy as np
import torch

def generate_social_graph(n_nodes: int = 200, m_edges: int = 3, feature_dim: int = 16):
    rng = np.random.default_rng(42)
    G = nx.barabasi_albert_graph(n_nodes, m_edges, seed=42)
    
    # Generate node interest features
    node_features = rng.normal(0, 1, size=(n_nodes, feature_dim)).astype(np.float32)
    
    edge_list = list(G.edges())
    edge_index = torch.tensor(edge_list, dtype=torch.long).t().contiguous()
    # Undirected graph: add reverse edges
    edge_index = torch.cat([edge_index, edge_index.flip(0)], dim=1)

    return G, torch.tensor(node_features), edge_index
