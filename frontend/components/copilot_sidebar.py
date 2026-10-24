"""
AICTE Nexus India - Modular UI Component: AI APAAR Neural Copilot Sidebar
Site-Aware Neural RAG Assistant for Regulatory Inquiries and Real-Time Verification.
"""

import streamlit as st

def render_copilot_sidebar_component(rag_engine=None, active_students=None, active_logs=None):
    """
    Renders the unified, streamlined AI Copilot drawer in the left sidebar.
    """
    with st.expander("🤖 AI APAAR Copilot (Neural RAG)", expanded=False):
        st.caption("Ask queries regarding seat limits, duplicate admissions, UGC/AICTE notifications, or scholarship rules.")
        
        user_prompt = st.text_input("Regulatory Query / APAAR Prompt:", key="copilot_comp_prompt", placeholder="e.g. Can a college exceed its sanctioned intake?")
        submit_prompt = st.button("Query Copilot", key="copilot_comp_submit")
        
        if submit_prompt and user_prompt:
            if rag_engine is None:
                try:
                    from backend.rlhf_copilot import rag_engine
                except (ImportError, ValueError):
                    from rag_engine import rag_engine
                    
            with st.spinner("Retrieving Statutory Policies & Database Vectors..."):
                response = rag_engine.query_copilot(user_prompt, students=active_students, logs=active_logs)
                
            st.markdown(f"**AICTE Response:**\n\n{response.get('answer', '')}")
            if response.get("citations"):
                st.caption(f"📚 Citations: {', '.join(response.get('citations', []))}")
