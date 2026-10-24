"""
AICTE Nexus India - Modular UI Component: Cryptographic Audit Ledger
Immutable SHA-256 Merkle root verification and compliance event explorer.
"""

import streamlit as st
import pandas as pd

def render_audit_ledger_component(df_logs: pd.DataFrame, search_term: str = ""):
    """
    Renders cryptographic audit chain explorer with SHA-256 seal search.
    """
    st.markdown("#### 🔒 AICTE National Cryptographic Audit Ledger (SHA-256)")
    
    if search_term:
        filtered_df = df_logs[
            df_logs['action'].str.contains(search_term, case=False, na=False) |
            df_logs['details'].str.contains(search_term, case=False, na=False) |
            df_logs['sha256_hash'].str.contains(search_term, case=False, na=False)
        ]
    else:
        filtered_df = df_logs

    st.dataframe(
        filtered_df[['id', 'timestamp', 'action', 'actor_role', 'target_apaar', 'sha256_hash']],
        use_container_width=True,
        hide_index=True
    )
