import streamlit as st
import pandas as pd
import plotly.express as px

from utils.report_manager import (
    get_report_counts,
    get_all_reports
)

def show_analytics_page(language):

    st.title("📊 Analytics Dashboard")

    # ================= DATA =================
    total, pending, resolved = get_report_counts()
    reports = get_all_reports()

    # ================= METRICS =================
    col1, col2, col3 = st.columns(3)

    col1.metric("📄 Total Reports", total)
    col2.metric("⏳ Pending", pending)
    col3.metric("✅ Resolved", resolved)

    # ================= EMPTY CHECK =================
    if not reports:
        st.warning("⚠ No reports available")
        return

    # ================= DATAFRAME =================
    df = pd.DataFrame(reports, columns=[
        "ID",
        "Report ID",
        "Name",
        "Location",
        "Issue Type",
        "Description",
        "Severity",
        "Image",
        "Status",
        "Date"
    ])

    # ================= PIE CHART =================
    st.subheader("📌 Status Distribution")

    pie_df = pd.DataFrame({
        "Status": ["Pending", "Resolved"],
        "Count": [pending, resolved]
    })

    fig1 = px.pie(
        pie_df,
        names="Status",
        values="Count",
        title="Report Status Distribution",
        hole=0.4
    )

    st.plotly_chart(fig1, use_container_width=True)

    # ================= BAR CHART =================
    st.subheader("📍 Reports by Location")

    location_df = df["Location"].value_counts().reset_index()
    location_df.columns = ["Location", "Reports"]

    fig2 = px.bar(
        location_df,
        x="Location",
        y="Reports",
        title="Reports by Location",
        text="Reports"
    )

    fig2.update_traces(textposition="outside")

    st.plotly_chart(fig2, use_container_width=True)

    # ================= SEVERITY CHART (NEW ADDITION) =================
    st.subheader("⚠ Severity Analysis")

    severity_df = df["Severity"].value_counts().reset_index()
    severity_df.columns = ["Severity", "Count"]

    fig3 = px.bar(
        severity_df,
        x="Severity",
        y="Count",
        title="Severity Level Distribution",
        text="Count"
    )

    fig3.update_traces(textposition="outside")

    st.plotly_chart(fig3, use_container_width=True)

    # ================= TABLE =================
    st.subheader("📋 Full Reports Data")

    st.dataframe(df, use_container_width=True)