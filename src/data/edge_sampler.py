"""Positive and negative edge split sampling for link prediction."""
import torch
import random
import networkx as nx

def sample_link_splits(G: nx.Graph, test_ratio: float = 0.2):
    edges = list(G.edges())
    random.seed(42)
    random.shuffle(edges)
    
    n_test = int(len(edges) * test_ratio)
    pos_test = edges[:n_test]
    pos_train = edges[n_test:]

    # Negative sampling (non-edges)
    non_edges = list(nx.non_edges(G))
    random.shuffle(non_edges)
    neg_test = non_edges[:n_test]
    neg_train = non_edges[n_test:n_test + len(pos_train)]

    return pos_train, pos_test, neg_train, neg_test
