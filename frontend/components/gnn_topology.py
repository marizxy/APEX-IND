"""
AICTE Nexus India - Modular UI Component: GNN Topology Visualizer
Interactive Graph Neural Network (GNN) graph representation, spectral node layout,
and multi-college proxy syndicate network inspection.
"""

import streamlit as st
import plotly.graph_objects as go
import networkx as nx

def render_gnn_topology_component(graph: nx.Graph = None, highlighted_nodes=None):
    """
    Renders an interactive NetworkX + Plotly topology graph of the GNN bipartite network.
    """
    if graph is None:
        graph = nx.Graph()
        # Seed default topology
        nodes = [
            ("IIT Madras", {"type": "institution", "tier": "Tier 1"}),
            ("Anna University", {"type": "institution", "tier": "Tier 2"}),
            ("R.M.D. Engg College", {"type": "institution", "tier": "Tier 3"}),
            ("Aditya Verma", {"type": "student", "risk": "Low"}),
            ("Karthick Ram", {"type": "student", "risk": "High"}),
            ("Karthikeyan R", {"type": "student", "risk": "High"}),
            ("Priya Nair", {"type": "student", "risk": "Low"})
        ]
        graph.add_nodes_from(nodes)
        edges = [
            ("IIT Madras", "Aditya Verma"),
            ("Anna University", "Karthick Ram"),
            ("R.M.D. Engg College", "Karthikeyan R"),
            ("IIT Madras", "Priya Nair"),
            ("Karthick Ram", "Karthikeyan R")  # Proxy ring edge
        ]
        graph.add_edges_from(edges)

    pos = nx.spring_layout(graph, seed=42)
    edge_x = []
    edge_y = []
    for edge in graph.edges():
        x0, y0 = pos[edge[0]]
        x1, y1 = pos[edge[1]]
        edge_x.extend([x0, x1, None])
        edge_y.extend([y0, y1, None])

    edge_trace = go.Scatter(
        x=edge_x, y=edge_y,
        line=dict(width=1.5, color='#475569'),
        hoverinfo='none',
        mode='lines'
    )

    node_x = []
    node_y = []
    node_text = []
    node_color = []
    node_size = []

    for node in graph.nodes():
        x, y = pos[node]
        node_x.append(x)
        node_y.append(y)
        node_data = graph.nodes[node]
        node_type = node_data.get("type", "node")
        
        if node_type == "institution":
            node_color.append('#38bdf8')
            node_size.append(26)
            node_text.append(f"🏛️ Institution: {node}")
        elif "High" in str(node_data.get("risk", "")):
            node_color.append('#f43f5e')
            node_size.append(22)
            node_text.append(f"🚨 Proxy Flagged: {node}")
        else:
            node_color.append('#10b981')
            node_size.append(18)
            node_text.append(f"👤 Enrolled: {node}")

    node_trace = go.Scatter(
        x=node_x, y=node_y,
        mode='markers+text',
        hoverinfo='text',
        text=[n for n in graph.nodes()],
        textposition="top center",
        marker=dict(
            showscale=False,
            color=node_color,
            size=node_size,
            line=dict(width=2, color='#ffffff')
        )
    )

    fig = go.Figure(data=[edge_trace, node_trace],
                 layout=go.Layout(
                    title=dict(text="AICTE Bipartite Identity Graph (GraphSAGE Convolution Topology)", font=dict(color="#f8fafc", size=14)),
                    showlegend=False,
                    hovermode='closest',
                    margin=dict(b=10, l=10, r=10, t=35),
                    plot_bgcolor="rgba(15, 23, 42, 0.4)",
                    paper_bgcolor="rgba(15, 23, 42, 0)",
                    xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                    yaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                    height=360
                 ))

    st.plotly_chart(fig, use_container_width=True)
