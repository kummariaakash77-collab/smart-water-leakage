import streamlit as st
from utils.report_manager import get_all_reports

def show_admin_page(language):

    texts = {
        "English": {
            "title": "👨‍💼 Admin Dashboard"
        },
        "Hindi": {
            "title": "👨‍💼 एडमिन डैशबोर्ड"
        },
        "Telugu": {
            "title": "👨‍💼 అడ్మిన్ డ్యాష్‌బోర్డ్"
        },
        "Tamil": {
            "title": "👨‍💼 நிர்வாக டாஷ்போர்ட்"
        },
        "Kannada": {
            "title": "👨‍💼 ಆಡ್ಮಿನ್ ಡ್ಯಾಶ್‌ಬೋರ್ಡ್"
        }
    }

    t = texts[language]

    st.title(t["title"])

    data = get_all_reports()

    if data is None or len(data) == 0:
        st.info("No data available")
    else:
        st.dataframe(data)