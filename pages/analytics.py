import streamlit as st
import pandas as pd
import plotly.express as px

from utils.report_manager import get_report_counts, get_all_reports


def show_analytics_page(language):

    texts = {
        "English": {
            "title": "📊 Analytics Dashboard",
            "total": "📄 Total Reports",
            "pending": "⏳ Pending",
            "resolved": "✅ Resolved",
            "no_reports": "⚠ No reports available",
            "status_dist": "📌 Status Distribution",
            "reports_location": "📍 Reports by Location",
            "severity_analysis": "⚠ Severity Analysis",
            "full_data": "📋 Full Reports Data",
            "status_title": "Report Status Distribution",
            "location_title": "Reports by Location",
            "severity_title": "Severity Level Distribution",
        },
        "Hindi": {
            "title": "📊 एनालिटिक्स डैशबोर्ड",
            "total": "📄 कुल रिपोर्ट",
            "pending": "⏳ लंबित",
            "resolved": "✅ समाधान",
            "no_reports": "⚠ कोई रिपोर्ट उपलब्ध नहीं",
            "status_dist": "📌 स्थिति वितरण",
            "reports_location": "📍 स्थान अनुसार रिपोर्ट",
            "severity_analysis": "⚠ गंभीरता विश्लेषण",
            "full_data": "📋 सभी रिपोर्ट डेटा",
            "status_title": "रिपोर्ट स्थिति वितरण",
            "location_title": "स्थान अनुसार रिपोर्ट",
            "severity_title": "गंभीरता स्तर वितरण",
        },
        "Telugu": {
            "title": "📊 విశ్లేషణల డ్యాష్‌బోర్డ్",
            "total": "📄 మొత్తం రిపోర్టులు",
            "pending": "⏳ పెండింగ్",
            "resolved": "✅ పరిష్కరించబడినవి",
            "no_reports": "⚠ రిపోర్టులు అందుబాటులో లేవు",
            "status_dist": "📌 స్థితి పంపిణీ",
            "reports_location": "📍 ప్రాంతాల వారీగా రిపోర్టులు",
            "severity_analysis": "⚠ తీవ్రత విశ్లేషణ",
            "full_data": "📋 పూర్తి రిపోర్ట్ డేటా",
            "status_title": "రిపోర్ట్ స్థితి పంపిణీ",
            "location_title": "ప్రాంతాల వారీగా రిపోర్టులు",
            "severity_title": "తీవ్రత స్థాయి పంపిణీ",
        },
        "Tamil": {
            "title": "📊 பகுப்பாய்வு டாஷ்போர்டு",
            "total": "📄 மொத்த அறிக்கைகள்",
            "pending": "⏳ நிலுவையில்",
            "resolved": "✅ தீர்க்கப்பட்டது",
            "no_reports": "⚠ அறிக்கைகள் இல்லை",
            "status_dist": "📌 நிலை விநியோகம்",
            "reports_location": "📍 இட வாரியான அறிக்கைகள்",
            "severity_analysis": "⚠ தீவிரம் பகுப்பாய்வு",
            "full_data": "📋 முழு அறிக்கை தரவு",
            "status_title": "அறிக்கை நிலை விநியோகம்",
            "location_title": "இட வாரியான அறிக்கைகள்",
            "severity_title": "தீவிர நிலை விநியோகம்",
        },
        "Kannada": {
            "title": "📊 ವಿಶ್ಲೇಷಣಾ ಡ್ಯಾಶ್‌ಬೋರ್ಡ್",
            "total": "📄 ಒಟ್ಟು ವರದಿಗಳು",
            "pending": "⏳ ಬಾಕಿ",
            "resolved": "✅ ಪರಿಹರಿಸಲಾಗಿದೆ",
            "no_reports": "⚠ ಯಾವುದೇ ವರದಿಗಳು ಲಭ್ಯವಿಲ್ಲ",
            "status_dist": "📌 ಸ್ಥಿತಿ ವಿತರಣೆ",
            "reports_location": "📍 ಸ್ಥಳವಾರು ವರದಿಗಳು",
            "severity_analysis": "⚠ ತೀವ್ರತೆ ವಿಶ್ಲೇಷಣೆ",
            "full_data": "📋 ಸಂಪೂರ್ಣ ವರದಿ ಡೇಟಾ",
            "status_title": "ವರದಿ ಸ್ಥಿತಿ ವಿತರಣೆ",
            "location_title": "ಸ್ಥಳವಾರು ವರದಿಗಳು",
            "severity_title": "ತೀವ್ರತೆ ಮಟ್ಟ ವಿತರಣೆ",
        },
    }

    t = texts.get(language, texts["English"])

    st.title(t["title"])

    total, pending, resolved = get_report_counts()
    reports = get_all_reports()

    col1, col2, col3 = st.columns(3)

    col1.metric(t["total"], total)
    col2.metric(t["pending"], pending)
    col3.metric(t["resolved"], resolved)

    if not reports:
        st.warning(t["no_reports"])
        return

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
            "Date",
        ],
    )

    st.subheader(t["status_dist"])

    pie_df = pd.DataFrame(
        {"Status": ["Pending", "Resolved"], "Count": [pending, resolved]}
    )

    fig1 = px.pie(
        pie_df, names="Status", values="Count", title=t["status_title"], hole=0.4
    )

    st.plotly_chart(fig1, width="stretch")

    st.subheader(t["reports_location"])

    location_df = df["Location"].value_counts().reset_index()
    location_df.columns = ["Location", "Reports"]

    fig2 = px.bar(
        location_df,
        x="Location",
        y="Reports",
        title=t["location_title"],
        text="Reports",
    )

    fig2.update_traces(textposition="outside")

    st.plotly_chart(fig2, width="stretch")

    st.subheader(t["severity_analysis"])

    severity_df = df["Severity"].value_counts().reset_index()
    severity_df.columns = ["Severity", "Count"]

    fig3 = px.bar(
        severity_df, x="Severity", y="Count", title=t["severity_title"], text="Count"
    )

    fig3.update_traces(textposition="outside")

    st.plotly_chart(fig3, width="stretch")

    st.subheader(t["full_data"])

    st.dataframe(df, width="stretch")
