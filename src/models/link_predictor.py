"""Link prediction dot-product and bilinear scoring decoder."""
import torch
import torch.nn as nn

class LinkPredictor(nn.Module):
    def __init__(self, embed_dim: int = 16):
        super().__init__()
        self.bilinear = nn.Bilinear(embed_dim, embed_dim, 1)

    def decode_edges(self, embeddings, edge_pairs):
        u_idx = [e[0] for e in edge_pairs]
        v_idx = [e[1] for e in edge_pairs]
        u = embeddings[u_idx]
        v = embeddings[v_idx]
        scores = torch.sigmoid(self.bilinear(u, v).squeeze(-1))
        return scores
