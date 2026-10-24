"""
AICTE Nexus India - RLHF Copilot & Neural RAG Package
Site-Aware RAG Engine, In-Memory Vector Indexing, Policy Knowledge Retrieval,
and Zero-Hallucination Regulatory Synthesis.
"""

from .rag_engine import rag_engine, AICTE_STATUTORY_POLICIES
from .policy_copilot import PolicyCopilotHandler, policy_copilot

__all__ = [
    "rag_engine",
    "AICTE_STATUTORY_POLICIES",
    "PolicyCopilotHandler",
    "policy_copilot"
]
