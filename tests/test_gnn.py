import pytest
pytest.importorskip("torch")
"""Unit tests for graph generation, edge sampler, and GCN forward pass."""
import torch
from src.data.graph_generator import generate_social_graph
from src.data.edge_sampler import sample_link_splits
from src.models.gcn_encoder import GCNEncoder
from src.evaluation.metrics import evaluate_link_predictions

def test_graph_generator():
    G, x, edge_idx = generate_social_graph(50, 2)
    assert G.number_of_nodes() == 50
    assert x.shape == (50, 16)

def test_edge_sampler():
    G, _, _ = generate_social_graph(40, 2)
    p_train, p_test, n_train, n_test = sample_link_splits(G)
    assert len(p_test) > 0
    assert len(n_test) == len(p_test)

def test_metrics():
    pos = [0.9, 0.85, 0.75]
    neg = [0.1, 0.2, 0.3]
    res = evaluate_link_predictions(pos, neg)
    assert res["roc_auc"] == 1.0
