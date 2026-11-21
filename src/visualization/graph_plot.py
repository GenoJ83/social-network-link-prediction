"""Social graph visualization with predicted candidate links."""
import networkx as nx

def format_graph_summary(G: nx.Graph, recommended_pairs):
    lines = [f"Network has {G.number_of_nodes()} members and {G.number_of_edges()} existing links."]
    lines.append("Top Predicted Missing Connections:")
    for u, v in recommended_pairs:
        lines.append(f"  Connection candidate: Node {u} <---> Node {v}")
    return "\n".join(lines)
