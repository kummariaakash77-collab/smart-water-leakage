import streamlit as st
import pandas as pd
import plotly.express as px

from utils.report_manager import (
    get_report_counts,
    get_all_reports
)

def show_analytics_page(language):

    st.title("📊 Analytics Dashboard")

    total, pending, resolved = get_report_counts()

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("📄 Total Reports", total)

    with col2:
        st.metric("⏳ Pending", pending)

    with col3:
        st.metric("✅ Resolved", resolved)

    reports = get_all_reports()

    if not reports:
        st.info("No reports available")
        return

    df = pd.DataFrame(
        reports,
        columns=[
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
        ]
    )

    st.subheader("📌 Status Distribution")

    pie_data = pd.DataFrame({
        "Status": ["Pending", "Resolved"],
        "Count": [pending, resolved]
    })

    pie_chart = px.pie(
        pie_data,
        names="Status",
        values="Count",
        title="Reports Status"
    )

    st.plotly_chart(
        pie_chart,
        use_container_width=True
    )

    st.subheader("📍 Reports by Location")

    location_count = (
        df["Location"]
        .value_counts()
        .reset_index()
    )

    location_count.columns = [
        "Location",
        "Reports"
    ]

    bar_chart = px.bar(
        location_count,
        x="Location",
        y="Reports",
        title="Reports by Location"
    )

    st.plotly_chart(
        bar_chart,
        use_container_width=True
    )

    st.subheader("📋 Full Analytics Data")

    st.dataframe(
        df,
        use_container_width=True
    )