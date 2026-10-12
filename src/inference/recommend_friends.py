"""Friend suggestion and potential social edge ranker."""
import torch
import numpy as np

class FriendRecommender:
    def __init__(self, embeddings: torch.Tensor):
        self.embeddings = embeddings

    def recommend_for_node(self, node_idx: int, top_k: int = 5):
        target_emb = self.embeddings[node_idx]
        # Dot product cosine similarity across all nodes
        scores = torch.matmul(self.embeddings, target_emb)
        scores[node_idx] = -1e9 # Exclude self
        top_nodes = torch.topk(scores, k=top_k).indices.tolist()
        return top_nodes
