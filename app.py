import streamlit as st
from utils.db import create_tables

# ---------------- SAFE AI IMPORT ----------------
try:
    from pages.ai_assistant import show_ai_page
    AI_AVAILABLE = True
except:
    AI_AVAILABLE = False

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Smart Water Leakage Reporting",
    page_icon="💧",
    layout="wide"
)

# ---------------- LANGUAGE SYSTEM ----------------
language = st.sidebar.selectbox(
    "🌐 Language / भाषा चुनें",
    ["English", "Hindi", "Telugu", "Tamil", "Kannada"]
)

texts = {
    "English": {
        "nav_home": "🏠 Home",
        "nav_report": "💧 Report Leakage",
        "nav_track": "📋 Track Reports",
        "nav_admin": "👨‍💼 Admin Dashboard",
        "nav_analytics": "📊 Analytics",
        "nav_title": "Navigation"
    },
    "Hindi": {
        "nav_home": "🏠 होम",
        "nav_report": "💧 लीकेज रिपोर्ट करें",
        "nav_track": "📋 रिपोर्ट ट्रैक करें",
        "nav_admin": "👨‍💼 एडमिन डैशबोर्ड",
        "nav_analytics": "📊 एनालिटिक्स",
        "nav_title": "नेविगेशन"
    },
    "Telugu": {
        "nav_home": "🏠 హోమ్",
        "nav_report": "💧 లీకేజ్ రిపోర్ట్ చేయండి",
        "nav_track": "📋 రిపోర్ట్ ట్రాక్ చేయండి",
        "nav_admin": "👨‍💼 అడ్మిన్ డ్యాష్‌బోర్డ్",
        "nav_analytics": "📊 విశ్లేషణలు",
        "nav_title": "నావిగేషన్"
    },
    "Tamil": {
        "nav_home": "🏠 முகப்பு",
        "nav_report": "💧 கசிவு புகாரளி",
        "nav_track": "📋 அறிக்கைகளை கண்காணிக்க",
        "nav_admin": "👨‍💼 நிர்வாகம்",
        "nav_analytics": "📊 பகுப்பாய்வு",
        "nav_title": "வழிசெலுத்தல்"
    },
    "Kannada": {
        "nav_home": "🏠 ಮನೆ",
        "nav_report": "💧 ಲೀಕೆಜ್ ವರದಿ ಮಾಡಿ",
        "nav_track": "📋 ವರದಿಗಳನ್ನು ಟ್ರ್ಯಾಕ್ ಮಾಡಿ",
        "nav_admin": "👨‍💼 ಆಡ್ಮಿನ್ ಡ್ಯಾಶ್‌ಬೋರ್ಡ್",
        "nav_analytics": "📊 ವಿಶ್ಲೇಷಣೆ",
        "nav_title": "ನ್ಯಾವಿಗೇಶನ್"
    }
}

# ---------------- CSS ----------------
def load_css():
    with open("assets/styles.css", "r", encoding="utf-8") as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )

load_css()

# ---------------- DB INIT ----------------
create_tables()

# 🔥 STEP 2 FORCE REDEPLOY TRIGGER (ADDED)
st.sidebar.info("FORCE REDEPLOY TRIGGER - AI FIX")

# ---------------- NAVIGATION ----------------
page = st.sidebar.radio(
    texts[language]["nav_title"],
    [
        texts[language]["nav_home"],
        texts[language]["nav_report"],
        texts[language]["nav_track"],
        texts[language]["nav_admin"],
        texts[language]["nav_analytics"],
        "🤖 AI Assistant"
    ]
)

# ---------------- ROUTING ----------------
if page == texts[language]["nav_home"]:
    from pages.home import show_home
    show_home(language)

elif page == texts[language]["nav_report"]:
    from pages.report_leakage import show_report_page
    show_report_page(language)

elif page == texts[language]["nav_track"]:
    from pages.track_reports import show_track_page
    show_track_page(language)

elif page == texts[language]["nav_admin"]:
    from pages.admin_dashboard import show_admin_page
    show_admin_page(language)

elif page == texts[language]["nav_analytics"]:
    from pages.analytics import show_analytics_page
    show_analytics_page(language)

# ---------------- AI PAGE ----------------
elif page == "🤖 AI Assistant":
    if AI_AVAILABLE:
        from pages.ai_assistant import show_ai_page
        ai_mode = st.sidebar.selectbox("AI Mode", ["Local AI (Ollama)", "BYOK (API Key)"])
        api_key = st.sidebar.text_input("API Key (if BYOK)", type="password")
        show_ai_page(language, ai_mode, api_key)
    else:
        st.error("❌ AI module missing. Please create pages/ai_assistant.py")