import streamlit as st
import pandas as pd
import plotly.express as px
from utils.report_manager import get_all_reports


def show_analytics_page():

    st.title("📊 Water Leakage Analytics")

    reports = get_all_reports()

    if not reports:
        st.warning("No reports available.")
        return

    df = pd.DataFrame(
        reports,
        columns=[
            "ID",
            "Report ID",
            "Reporter",
            "Location",
            "Issue Type",
            "Description",
            "Severity",
            "Image",
            "Status",
            "Date"
        ]
    )

    st.subheader("Reports by Status")

    status_chart = px.pie(
        df,
        names="Status",
        title="Report Status Distribution"
    )

    st.plotly_chart(
        status_chart,
        use_container_width=True
    )

    st.subheader("Reports by Severity")

    severity_chart = px.bar(
        df,
        x="Severity",
        title="Severity Distribution"
    )

    st.plotly_chart(
        severity_chart,
        use_container_width=True
    )

    st.subheader("Reports by Issue Type")

    issue_chart = px.histogram(
        df,
        x="Issue Type",
        title="Issue Type Distribution"
    )

    st.plotly_chart(
        issue_chart,
        use_container_width=True
    )