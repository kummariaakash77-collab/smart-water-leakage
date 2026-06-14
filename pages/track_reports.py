import streamlit as st
import pandas as pd
from utils.report_manager import get_reports

def show_track_page(language):

    texts = {
        "English": {
            "title": "📋 Track Reports",
            "search": "🔍 Search Report ID",
            "download": "📥 Download Reports CSV",
            "empty": "No reports found"
        },
        "Hindi": {
            "title": "📋 रिपोर्ट ट्रैक करें",
            "search": "🔍 रिपोर्ट आईडी खोजें",
            "download": "📥 रिपोर्ट CSV डाउनलोड करें",
            "empty": "कोई रिपोर्ट नहीं मिली"
        },
        "Telugu": {
            "title": "📋 రిపోర్టులను ట్రాక్ చేయండి",
            "search": "🔍 రిపోర్ట్ ID వెతకండి",
            "download": "📥 CSV డౌన్‌లోడ్ చేయండి",
            "empty": "రిపోర్టులు లభించలేదు"
        },
        "Tamil": {
            "title": "📋 அறிக்கைகளை கண்காணிக்க",
            "search": "🔍 அறிக்கை ஐடியை தேடுங்கள்",
            "download": "📥 CSV பதிவிறக்கவும்",
            "empty": "அறிக்கைகள் இல்லை"
        },
        "Kannada": {
            "title": "📋 ವರದಿಗಳನ್ನು ಟ್ರ್ಯಾಕ್ ಮಾಡಿ",
            "search": "🔍 ವರದಿ ID ಹುಡುಕಿ",
            "download": "📥 CSV ಡೌನ್‌ಲೋಡ್ ಮಾಡಿ",
            "empty": "ಯಾವುದೇ ವರದಿಗಳು ಕಂಡುಬಂದಿಲ್ಲ"
        }
    }

    t = texts.get(language, texts["English"])

    st.title(t["title"])

    reports = get_reports()

    if not reports:
        st.info(t["empty"])
        return

    search_id = st.text_input(t["search"])

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
        width="stretch",
        hide_index=True
    )

    csv = df.to_csv(index=False)

    st.download_button(
        t["download"],
        csv,
        "water_reports.csv",
        "text/csv"
    )