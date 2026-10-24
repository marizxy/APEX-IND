"""
AICTE Nexus India - Graph Neural Network (GNN) Engine Package
GraphSAGE multi-relational convolution, topological neighborhood aggregation,
fuzzy semantic sequence matching, and sub-15ms proxy admission ring interception.
"""

from .graphsage_engine import AIEngineV5, ai_engine_v5

# Alias for architectural clarity
GraphSAGEProxyEngine = AIEngineV5

__all__ = [
    "AIEngineV5",
    "GraphSAGEProxyEngine",
    "ai_engine_v5"
]
