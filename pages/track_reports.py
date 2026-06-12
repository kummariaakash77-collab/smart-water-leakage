import streamlit as st
import pandas as pd
from utils.report_manager import get_reports

def show_track_page(language):

    st.title("📋 Track Reports")

    reports = get_reports()

    if not reports:
        st.info("No reports found")
        return

    search_id = st.text_input("🔍 Search Report ID")

    filtered_reports = reports

    if search_id:
        filtered_reports = [
            r for r in reports
            if search_id.lower() in str(r[1]).lower()
        ]

    df = pd.DataFrame(
        filtered_reports,
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

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True
    )

    csv = df.to_csv(index=False)

    st.download_button(
        "📥 Download Reports CSV",
        csv,
        "water_reports.csv",
        "text/csv"
    )