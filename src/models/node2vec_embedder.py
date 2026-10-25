"""Node2Vec biased random walk generator."""
import random
import networkx as nx

class RandomWalkGenerator:
    def __init__(self, G: nx.Graph, walk_length: int = 10, p: float = 1.0, q: float = 1.0):
        self.G = G
        self.walk_length = walk_length
        self.p = p
        self.q = q

    def generate_walk(self, start_node: int):
        walk = [start_node]
        curr = start_node
        for _ in range(self.walk_length - 1):
            neighbors = list(self.G.neighbors(curr))
            if not neighbors:
                break
            curr = random.choice(neighbors)
            walk.append(curr)
        return walk
