"""Graph Convolutional Network (GCN) node embedding encoder."""
import torch
import torch.nn as nn

class GCNLayer(nn.Module):
    def __init__(self, in_features: int, out_features: int):
        super().__init__()
        self.linear = nn.Linear(in_features, out_features)

    def forward(self, x, adj_matrix):
        # A * X * W message passing
        support = self.linear(x)
        out = torch.spmm(adj_matrix, support)
        return torch.relu(out)

class GCNEncoder(nn.Module):
    def __init__(self, in_dim: int = 16, hidden_dim: int = 32, out_dim: int = 16):
        super().__init__()
        self.conv1 = GCNLayer(in_dim, hidden_dim)
        self.conv2 = GCNLayer(hidden_dim, out_dim)

    def forward(self, x, adj):
        h = self.conv1(x, adj)
        return self.conv2(h, adj)
