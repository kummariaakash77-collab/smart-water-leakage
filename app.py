import streamlit as st
from utils.db import create_tables

st.set_page_config(
    page_title="Smart Water Leakage Reporting",
    page_icon="💧",
    layout="wide"
)

def load_css():
    with open("assets/styles.css", "r", encoding="utf-8") as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )

load_css()

create_tables()

page = st.sidebar.radio(
    "Navigation",
    [
        "🏠 Home",
        "💧 Report Leakage",
        "📋 Track Reports",
        "👨‍💼 Admin Dashboard",
        "📊 Analytics"
    ]
)

if page == "🏠 Home":
    from pages.home import show_home
    show_home()

elif page == "💧 Report Leakage":
    from pages.report_leakage import show_report_page
    show_report_page()

elif page == "📋 Track Reports":
    from pages.track_reports import show_track_page
    show_track_page()

elif page == "👨‍💼 Admin Dashboard":
    from pages.admin_dashboard import show_admin_page
    show_admin_page()

elif page == "📊 Analytics":
    from pages.analytics import show_analytics_page
    show_analytics_page()