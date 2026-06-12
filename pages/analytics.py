import streamlit as st
from utils.report_manager import get_report_counts

def show_analytics_page(language):

    texts = {
        "English": {
            "title": "📊 Analytics"
        },
        "Hindi": {
            "title": "📊 एनालिटिक्स"
        },
        "Telugu": {
            "title": "📊 విశ్లేషణలు"
        },
        "Tamil": {
            "title": "📊 பகுப்பாய்வு"
        },
        "Kannada": {
            "title": "📊 ವಿಶ್ಲೇಷಣೆ"
        }
    }

    t = texts[language]

    st.title(t["title"])

    total, pending, resolved = get_report_counts()

    st.metric("Total", total)
    st.metric("Pending", pending)
    st.metric("Resolved", resolved)