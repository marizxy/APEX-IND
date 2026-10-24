"""
AICTE Nexus India - RLHF & Policy Copilot Prompt Handlers
High-precision prompt alignment, regulatory context injection, and executive query orchestration.
"""

from typing import Dict, Any, List
try:
    from .rag_engine import rag_engine, AICTE_STATUTORY_POLICIES
except (ImportError, ValueError):
    from rag_engine import rag_engine, AICTE_STATUTORY_POLICIES

class PolicyCopilotHandler:
    """
    Orchestrates user natural language regulatory queries against the neural RAG index
    and active database state.
    """
    def __init__(self):
        self.rag = rag_engine

    def answer_query(self, query: str, active_students=None, active_logs=None) -> Dict[str, Any]:
        """
        Execute RAG retrieval and synthesise an authoritative regulatory response.
        """
        rag_res = self.rag.query_copilot(query, students=active_students, logs=active_logs)
        return rag_res

policy_copilot = PolicyCopilotHandler()
