"""
AICTE Nexus India - Modular UI Component: Geospatial Heatmap & Budget DSS
Interactive state-level bubble density mapping and fiscal scholarship allocation.
"""

import streamlit as st
import plotly.express as px
import pandas as pd

def render_geospatial_heatmap_component(geospatial_engine=None):
    """
    Renders interactive geospatial telemetry bubble map and state statistics.
    """
    st.markdown("#### 🗺️ All-India Institutional Density & Anomaly Hotspots")
    
    if geospatial_engine is None:
        try:
            from backend.geospatial_dss import geospatial_engine
        except (ImportError, ValueError):
            from geospatial_dss import geospatial_engine

    col_ctrl1, col_ctrl2 = st.columns([1, 2])
    with col_ctrl1:
        metric_choice = st.selectbox(
            "Geospatial Projection Metric:",
            ["Student Enrollment Density", "Integrated Colleges", "Anomaly Hotspots"],
            key="geo_comp_metric"
        )
    
    metric_key = "students" if "Student" in metric_choice else ("institutions" if "Colleges" in metric_choice else "anomalies")
    fig = geospatial_engine.generate_heatmap_figure(metric_key)
    st.plotly_chart(fig, use_container_width=True)
