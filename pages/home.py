import streamlit as st
from utils.report_manager import get_report_counts

def show_home():

    total, pending, resolved = get_report_counts()

    high_severity = pending

    st.title(
        "💧 Smart Water Leakage Reporting System"
    )

    st.markdown("""
    Report water leakages quickly and help authorities
    resolve issues faster.
    """)

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "💧 Total Reports",
            total
        )

    with col2:
        st.metric(
            "⚠️ Pending Issues",
            pending
        )

    with col3:
        st.metric(
            "✅ Resolved Issues",
            resolved
        )

    with col4:
        st.metric(
            "🚨 High Priority",
            high_severity
        )

    st.success(
        "Welcome to the Smart Water Leakage Reporting Portal"
    )

    st.info(
        "Use the sidebar to report leakages, track reports, manage updates, and view analytics."
    )