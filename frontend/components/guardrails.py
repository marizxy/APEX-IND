"""
AICTE Nexus India - Modular UI Component: Scholarship & Attrition Guardrails
Predictive retention monitoring, risk tier breakdown, and multi-portal financial safeguards.
"""

import streamlit as st
import plotly.express as px
import pandas as pd

def render_guardrails_kpi_component(df_students: pd.DataFrame, is_registrar: bool = False, selected_college: str = ""):
    """
    Renders high-level predictive attrition metrics and distribution charts.
    """
    total_students = len(df_students)
    stable_count = len(df_students[df_students['dropout_risk'] == 'Low (Stable)'])
    monitor_count = len(df_students[df_students['dropout_risk'] == 'Moderate (Monitor)'])
    critical_count = len(df_students[df_students['dropout_risk'].isin(['Critical (Action Req.)', 'Critical', 'High (Action Req.)'])])
    retention_pct = (stable_count / max(1, total_students)) * 100.0

    k1, k2, k3, k4 = st.columns(4)
    k1.metric("Monitored Cohort Size", f"{total_students:,}")
    k2.metric("Predictive Retention Rate", f"{retention_pct:.1f}%")
    k3.metric("Moderate Watchlist", f"{monitor_count:,}")
    k4.metric("Critical Action Required", f"{critical_count:,}", delta=f"-{critical_count}" if critical_count > 0 else "0", delta_color="inverse")
