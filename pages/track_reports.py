import streamlit as st
import pandas as pd
from utils.report_manager import get_all_reports

def show_track_page():

    st.title("📋 Track Reports")

    reports = get_all_reports()

    if not reports:
        st.warning("No reports found.")
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

    st.subheader("🔍 Search Report")

    search_id = st.text_input(
        "Enter Report ID"
    )

    # 📥 Download CSV
    csv = df.to_csv(index=False).encode("utf-8")

    st.download_button(
        label="📥 Download Reports CSV",
        data=csv,
        file_name="water_leakage_reports.csv",
        mime="text/csv"
    )

    if search_id:
        filtered_df = df[
            df["Report ID"].astype(str).str.contains(
                search_id,
                case=False,
                na=False
            )
        ]

        if filtered_df.empty:
            st.error("No matching report found.")
        else:
            st.dataframe(
                filtered_df,
                use_container_width=True
            )
    else:
        st.dataframe(
            df,
            use_container_width=True
        )