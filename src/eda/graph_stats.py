"""Graph topological metrics: Degree distribution, density, clustering."""
import networkx as nx
from src.data.graph_generator import generate_social_graph

def analyze_graph_topology():
    G, _, _ = generate_social_graph(150, 3)
    stats = {
        "num_nodes": G.number_of_nodes(),
        "num_edges": G.number_of_edges(),
        "graph_density": round(nx.density(G), 4),
        "average_clustering": round(nx.average_clustering(G), 4),
        "is_connected": nx.is_connected(G)
    }
    print("Graph Topological Properties:", stats)
    return stats

if __name__ == "__main__":
    analyze_graph_topology()
