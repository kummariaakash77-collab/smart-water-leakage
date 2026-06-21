import streamlit as st
from utils.report_manager import get_report_counts


def show_home(language):

    total, pending, resolved = get_report_counts()
    high_severity = pending

    # ---------------- TRANSLATIONS ----------------
    texts = {
        "English": {
            "title": "💧 Smart Water Leakage Reporting System",
            "desc": "Report water leakages quickly and help authorities resolve issues faster.",
            "total": "💧 Total Reports",
            "pending": "⚠️ Pending Issues",
            "resolved": "✅ Resolved Issues",
            "high": "🚨 High Priority",
            "success": "Welcome to the Smart Water Leakage Reporting Portal",
            "info": "Use the sidebar to report leakages, track reports, manage updates, and view analytics.",
        },
        "Hindi": {
            "title": "💧 स्मार्ट वाटर लीकेज रिपोर्टिंग सिस्टम",
            "desc": "पानी के रिसाव की तुरंत रिपोर्ट करें और अधिकारियों की मदद करें।",
            "total": "💧 कुल रिपोर्ट",
            "pending": "⚠️ लंबित मामले",
            "resolved": "✅ समाधान किए गए मामले",
            "high": "🚨 उच्च प्राथमिकता",
            "success": "स्मार्ट वाटर लीकेज पोर्टल में आपका स्वागत है",
            "info": "लीकेज रिपोर्ट करने, ट्रैक करने और एनालिटिक्स देखने के लिए साइडबार का उपयोग करें।",
        },
        "Telugu": {
            "title": "💧 స్మార్ట్ వాటర్ లీకేజ్ రిపోర్టింగ్ సిస్టమ్",
            "desc": "నీటి లీకేజీలను త్వరగా నివేదించండి మరియు సహాయం చేయండి.",
            "total": "💧 మొత్తం రిపోర్టులు",
            "pending": "⚠️ పెండింగ్ సమస్యలు",
            "resolved": "✅ పరిష్కరించినవి",
            "high": "🚨 అధిక ప్రాధాన్యత",
            "success": "స్వాగతం",
            "info": "సైడ్‌బార్ ద్వారా రిపోర్ట్ చేయండి మరియు ట్రాక్ చేయండి.",
        },
        "Tamil": {
            "title": "💧 ஸ்மார்ட் நீர் கசிவு அறிக்கை அமைப்பு",
            "desc": "நீர் கசிவுகளை விரைவாக புகாரளிக்கவும்.",
            "total": "💧 மொத்த அறிக்கைகள்",
            "pending": "⚠️ நிலுவையில் உள்ளவை",
            "resolved": "✅ தீர்க்கப்பட்டவை",
            "high": "🚨 உயர் முன்னுரிமை",
            "success": "வரவேற்கிறோம்",
            "info": "சைட்பார் மூலம் புகாரளிக்கவும் மற்றும் கண்காணிக்கவும்.",
        },
        "Kannada": {
            "title": "💧 ಸ್ಮಾರ್ಟ್ ನೀರಿನ ಸೋರಿಕೆ ವರದಿ ವ್ಯವಸ್ಥೆ",
            "desc": "ನೀರಿನ ಸೋರಿಕೆಯನ್ನು ತ್ವರಿತವಾಗಿ ವರದಿ ಮಾಡಿ.",
            "total": "💧 ಒಟ್ಟು ವರದಿಗಳು",
            "pending": "⚠️ ಬಾಕಿ ಇರುವ ಸಮಸ್ಯೆಗಳು",
            "resolved": "✅ ಪರಿಹರಿಸಲಾಗಿದೆ",
            "high": "🚨 ಹೆಚ್ಚಿನ ಪ್ರಾಮುಖ್ಯತೆ",
            "success": "ಸ್ವಾಗತ",
            "info": "ಸೈಡ್‌ಬಾರ್ ಬಳಸಿ ವರದಿ ಮಾಡಿ ಮತ್ತು ಟ್ರ್ಯಾಕ್ ಮಾಡಿ.",
        },
    }

    t = texts[language]

    # ---------------- UI ----------------
    st.title(t["title"])
    st.markdown(t["desc"])

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(t["total"], total)

    with col2:
        st.metric(t["pending"], pending)

    with col3:
        st.metric(t["resolved"], resolved)

    with col4:
        st.metric(t["high"], high_severity)

    st.success(t["success"])
    st.info(t["info"])
