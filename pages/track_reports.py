import streamlit as st
from utils.report_manager import get_reports

def show_track_page(language):

    texts = {
        "English": {
            "title": "📋 Track Reports"
        },
        "Hindi": {
            "title": "📋 रिपोर्ट ट्रैक करें"
        },
        "Telugu": {
            "title": "📋 రిపోర్ట్ ట్రాక్ చేయండి"
        },
        "Tamil": {
            "title": "📋 அறிக்கைகளை கண்காணிக்க"
        },
        "Kannada": {
            "title": "📋 ವರದಿಗಳನ್ನು ಟ್ರ್ಯಾಕ್ ಮಾಡಿ"
        }
    }

    t = texts[language]

    st.title(t["title"])

    reports = get_reports()

    if not reports:
        st.info("No reports found")
    else:
        for r in reports:
            st.write(r)