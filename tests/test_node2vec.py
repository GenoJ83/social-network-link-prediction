"""Tests for Node2Vec walks."""
import networkx as nx
from src.models.node2vec_embedder import RandomWalkGenerator

def test_random_walk_length():
    G = nx.cycle_graph(10)
    gen = RandomWalkGenerator(G, walk_length=5)
    walk = gen.generate_walk(0)
    assert len(walk) == 5
    assert walk[0] == 0
