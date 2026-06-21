import streamlit as st
import pandas as pd
import os

from utils.report_manager import get_all_reports, update_status


def show_admin_page(language):

    texts = {
        "English": {
            "title": "👨‍💼 Admin Dashboard",
            "username": "Admin Username",
            "password": "Admin Password",
            "login_required": "Login Required",
            "no_reports": "No reports available",
            "search": "🔍 Search Report ID",
            "manage": "📋 Manage Reports",
            "report_id": "Report ID",
            "name": "Name",
            "location": "Location",
            "issue": "Issue Type",
            "description": "Description",
            "severity": "Severity",
            "status": "Current Status",
            "date": "Date",
            "update": "Update Status",
            "save": "Save Status",
            "updated": "Status updated to",
            "image_missing": "Image not found",
            "download": "📥 Download All Reports",
        },
        "Telugu": {
            "title": "👨‍💼 అడ్మిన్ డ్యాష్‌బోర్డ్",
            "username": "అడ్మిన్ యూజర్ నేమ్",
            "password": "అడ్మిన్ పాస్‌వర్డ్",
            "login_required": "లాగిన్ అవసరం",
            "no_reports": "రిపోర్టులు అందుబాటులో లేవు",
            "search": "🔍 రిపోర్ట్ ID వెతకండి",
            "manage": "📋 రిపోర్టులను నిర్వహించండి",
            "report_id": "రిపోర్ట్ ID",
            "name": "పేరు",
            "location": "ప్రాంతం",
            "issue": "సమస్య రకం",
            "description": "వివరణ",
            "severity": "తీవ్రత",
            "status": "ప్రస్తుత స్థితి",
            "date": "తేదీ",
            "update": "స్థితిని మార్చండి",
            "save": "స్థితిని సేవ్ చేయండి",
            "updated": "స్థితి మార్చబడింది",
            "image_missing": "చిత్రం కనబడలేదు",
            "download": "📥 అన్ని రిపోర్టులను డౌన్‌లోడ్ చేయండి",
        },
        "Hindi": {
            "title": "👨‍💼 एडमिन डैशबोर्ड",
            "username": "एडमिन यूज़रनेम",
            "password": "एडमिन पासवर्ड",
            "login_required": "लॉगिन आवश्यक है",
            "no_reports": "कोई रिपोर्ट उपलब्ध नहीं है",
            "search": "🔍 रिपोर्ट आईडी खोजें",
            "manage": "📋 रिपोर्ट प्रबंधन",
            "report_id": "रिपोर्ट आईडी",
            "name": "नाम",
            "location": "स्थान",
            "issue": "समस्या प्रकार",
            "description": "विवरण",
            "severity": "गंभीरता",
            "status": "वर्तमान स्थिति",
            "date": "तारीख",
            "update": "स्थिति अपडेट करें",
            "save": "स्थिति सहेजें",
            "updated": "स्थिति अपडेट हुई",
            "image_missing": "छवि नहीं मिली",
            "download": "📥 सभी रिपोर्ट डाउनलोड करें",
        },
        "Tamil": {
            "title": "👨‍💼 நிர்வாக டாஷ்போர்டு",
            "username": "நிர்வாக பயனர் பெயர்",
            "password": "நிர்வாக கடவுச்சொல்",
            "login_required": "உள்நுழைவு தேவை",
            "no_reports": "அறிக்கைகள் இல்லை",
            "search": "🔍 அறிக்கை ஐடியை தேடுங்கள்",
            "manage": "📋 அறிக்கைகளை நிர்வகிக்கவும்",
            "report_id": "அறிக்கை ஐடி",
            "name": "பெயர்",
            "location": "இடம்",
            "issue": "சிக்கல் வகை",
            "description": "விளக்கம்",
            "severity": "தீவிரம்",
            "status": "தற்போதைய நிலை",
            "date": "தேதி",
            "update": "நிலையை மாற்றவும்",
            "save": "நிலையை சேமிக்கவும்",
            "updated": "நிலை புதுப்பிக்கப்பட்டது",
            "image_missing": "படம் கிடைக்கவில்லை",
            "download": "📥 அனைத்து அறிக்கைகளையும் பதிவிறக்கவும்",
        },
        "Kannada": {
            "title": "👨‍💼 ಆಡ್ಮಿನ್ ಡ್ಯಾಶ್‌ಬೋರ್ಡ್",
            "username": "ಆಡ್ಮಿನ್ ಬಳಕೆದಾರ ಹೆಸರು",
            "password": "ಆಡ್ಮಿನ್ ಪಾಸ್‌ವರ್ಡ್",
            "login_required": "ಲಾಗಿನ್ ಅಗತ್ಯವಿದೆ",
            "no_reports": "ಯಾವುದೇ ವರದಿಗಳು ಲಭ್ಯವಿಲ್ಲ",
            "search": "🔍 ವರದಿ ID ಹುಡುಕಿ",
            "manage": "📋 ವರದಿಗಳನ್ನು ನಿರ್ವಹಿಸಿ",
            "report_id": "ವರದಿ ID",
            "name": "ಹೆಸರು",
            "location": "ಸ್ಥಳ",
            "issue": "ಸಮಸ್ಯೆಯ ಪ್ರಕಾರ",
            "description": "ವಿವರಣೆ",
            "severity": "ತೀವ್ರತೆ",
            "status": "ಪ್ರಸ್ತುತ ಸ್ಥಿತಿ",
            "date": "ದಿನಾಂಕ",
            "update": "ಸ್ಥಿತಿಯನ್ನು ನವೀಕರಿಸಿ",
            "save": "ಸ್ಥಿತಿ ಉಳಿಸಿ",
            "updated": "ಸ್ಥಿತಿ ನವೀಕರಿಸಲಾಗಿದೆ",
            "image_missing": "ಚಿತ್ರ ಕಂಡುಬಂದಿಲ್ಲ",
            "download": "📥 ಎಲ್ಲಾ ವರದಿಗಳನ್ನು ಡೌನ್‌ಲೋಡ್ ಮಾಡಿ",
        },
    }

    t = texts.get(language, texts["English"])

    st.title(t["title"])

    username = st.text_input(t["username"])
    password = st.text_input(t["password"], type="password")

    if username != "admin" or password != "admin123":
        st.warning(t["login_required"])
        return

    reports = get_all_reports()

    if not reports:
        st.info(t["no_reports"])
        return

    search_id = st.text_input(t["search"])

    if search_id:
        reports = [r for r in reports if search_id.lower() in str(r[1]).lower()]

    st.subheader(t["manage"])

    for report in reports:
        st.markdown("---")

        col1, col2 = st.columns([3, 1])

        with col1:
            st.write(f"**{t['report_id']}:** {report[1]}")
            st.write(f"**{t['name']}:** {report[2]}")
            st.write(f"**{t['location']}:** {report[3]}")
            st.write(f"**{t['issue']}:** {report[4]}")
            st.write(f"**{t['description']}:** {report[5]}")
            st.write(f"**{t['severity']}:** {report[6]}")
            st.write(f"**{t['status']}:** {report[8]}")
            st.write(f"**{t['date']}:** {report[9]}")

            new_status = st.selectbox(
                f"{t['update']} {report[1]}",
                ["Pending", "In Progress", "Resolved"],
                key=f"status_{report[1]}",
            )

            if st.button(f"{t['save']} {report[1]}", key=f"btn_{report[1]}"):
                update_status(report[1], new_status)

                st.success(f"{t['updated']} {new_status}")

                st.rerun()

        with col2:
            image_path = report[7]

            if image_path:
                if os.path.exists(image_path):
                    st.image(image_path, width=250)
                else:
                    st.warning(t["image_missing"])

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

    csv = df.to_csv(index=False)

    st.download_button(t["download"], csv, "water_leakage_reports.csv", "text/csv")
