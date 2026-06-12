import streamlit as st
import pandas as pd
import os

from utils.report_manager import (
    get_all_reports,
    update_status
)

def show_admin_page(language):

    st.title("👨‍💼 Admin Dashboard")

    username = st.text_input("Admin Username")
    password = st.text_input(
        "Admin Password",
        type="password"
    )

    if username != "admin" or password != "admin123":
        st.warning("Login Required")
        return

    reports = get_all_reports()

    if not reports:
        st.info("No reports available")
        return

    search_id = st.text_input(
        "🔍 Search Report ID"
    )

    if search_id:
        reports = [
            r for r in reports
            if search_id.lower() in str(r[1]).lower()
        ]

    st.subheader("📋 Manage Reports")

    for report in reports:

        st.markdown("---")

        col1, col2 = st.columns([3, 1])

        with col1:

            st.write(f"**Report ID:** {report[1]}")
            st.write(f"**Name:** {report[2]}")
            st.write(f"**Location:** {report[3]}")
            st.write(f"**Issue Type:** {report[4]}")
            st.write(f"**Description:** {report[5]}")
            st.write(f"**Severity:** {report[6]}")
            st.write(f"**Current Status:** {report[8]}")
            st.write(f"**Date:** {report[9]}")

            new_status = st.selectbox(
                f"Update Status {report[1]}",
                [
                    "Pending",
                    "In Progress",
                    "Resolved"
                ],
                key=f"status_{report[1]}"
            )

            if st.button(
                f"Save Status {report[1]}",
                key=f"btn_{report[1]}"
            ):
                update_status(
                    report[1],
                    new_status
                )

                st.success(
                    f"Status updated to {new_status}"
                )

                st.rerun()

        with col2:

            image_path = report[7]

            if image_path:

                if os.path.exists(image_path):
                    st.image(
                        image_path,
                        width=250
                    )
                else:
                    st.warning(
                        "Image not found"
                    )

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

    csv = df.to_csv(index=False)

    st.download_button(
        "📥 Download All Reports",
        csv,
        "water_leakage_reports.csv",
        "text/csv"
    )