"""GraphSAGE mean neighborhood aggregator architecture."""
import torch
import torch.nn as nn

class GraphSAGELayer(nn.Module):
    def __init__(self, in_dim: int, out_dim: int):
        super().__init__()
        self.weight = nn.Linear(in_dim * 2, out_dim)

    def forward(self, x, adj_norm):
        neighbor_agg = torch.spmm(adj_norm, x)
        concat = torch.cat([x, neighbor_agg], dim=-1)
        return torch.relu(self.weight(concat))
