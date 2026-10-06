"""Topological link prediction baselines: Jaccard and Adamic-Adar."""
import networkx as nx

def compute_topological_scores(G: nx.Graph, edge_pairs):
    jaccard_scores = [score for _, _, score in nx.jaccard_coefficient(G, edge_pairs)]
    adamic_scores = [score for _, _, score in nx.adamic_adar_index(G, edge_pairs)]
    return {"jaccard": jaccard_scores, "adamic_adar": adamic_scores}
