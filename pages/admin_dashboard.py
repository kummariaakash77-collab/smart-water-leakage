import streamlit as st
import pandas as pd
import os
from utils.report_manager import get_all_reports, update_status

def show_admin_page():

    st.title("👨‍💼 Admin Dashboard")

    # Login Section
    if "admin_logged_in" not in st.session_state:
        st.session_state.admin_logged_in = False

    if not st.session_state.admin_logged_in:

        st.subheader("🔐 Admin Login")

        username = st.text_input("Username")
        password = st.text_input("Password", type="password")

        if st.button("Login"):

            if username == "admin" and password == "admin123":
                st.session_state.admin_logged_in = True
                st.success("Login Successful!")
                st.rerun()
            else:
                st.error("Invalid Username or Password")

        return

    st.success("✅ Logged in as Admin")

    reports = get_all_reports()

    if not reports:
        st.warning("No reports available.")
        return

    st.subheader("📋 Submitted Reports")

    for report in reports:

        report_id = report[1]
        reporter = report[2]
        location = report[3]
        issue_type = report[4]
        description = report[5]
        severity = report[6]
        image_path = report[7]
        status_text = report[8]
        date_reported = report[9]

        with st.expander(f"📌 {report_id} | {location}"):

            st.write(f"**Reporter:** {reporter}")
            st.write(f"**Issue Type:** {issue_type}")
            st.write(f"**Description:** {description}")
            st.write(f"**Severity:** {severity}")
            st.write(f"**Status:** {status_text}")
            st.write(f"**Date:** {date_reported}")

            if image_path and os.path.exists(image_path):
                st.image(
                    image_path,
                    caption=f"Leakage Image - {report_id}",
                    use_container_width=True
                )
            else:
                st.warning("No image available")

    st.divider()

    st.subheader("🔄 Update Report Status")

    report_id = st.text_input("Enter Report ID")

    status = st.selectbox(
        "Select Status",
        ["Pending", "In Progress", "Resolved"]
    )

    if st.button("Update Status"):

        update_status(report_id, status)

        st.success("✅ Status Updated Successfully")

    if st.button("Logout"):
        st.session_state.admin_logged_in = False
        st.rerun()