import streamlit as st
from utils.report_manager import submit_report

def show_report_page(language):

    texts = {
        "English": {
            "title": "💧 Report Water Leakage",
            "name": "Name",
            "location": "Location",
            "desc": "Description",
            "submit": "Submit Report",
            "success": "Report submitted successfully!"
        },
        "Hindi": {
            "title": "💧 पानी रिसाव रिपोर्ट करें",
            "name": "नाम",
            "location": "स्थान",
            "desc": "विवरण",
            "submit": "रिपोर्ट जमा करें",
            "success": "रिपोर्ट सफलतापूर्वक जमा हुई!"
        },
        "Telugu": {
            "title": "💧 నీటి లీకేజ్ నివేదించండి",
            "name": "పేరు",
            "location": "స్థానం",
            "desc": "వివరణ",
            "submit": "సమర్పించండి",
            "success": "రిపోర్ట్ విజయవంతంగా పంపబడింది!"
        },
        "Tamil": {
            "title": "💧 நீர் கசிவு புகார்",
            "name": "பெயர்",
            "location": "இடம்",
            "desc": "விவரம்",
            "submit": "சமர்ப்பிக்கவும்",
            "success": "அறிக்கை வெற்றிகரமாக அனுப்பப்பட்டது!"
        },
        "Kannada": {
            "title": "💧 ನೀರಿನ ಸೋರಿಕೆ ವರದಿ",
            "name": "ಹೆಸರು",
            "location": "ಸ್ಥಳ",
            "desc": "ವಿವರಣೆ",
            "submit": "ಸಲ್ಲಿಸು",
            "success": "ವರದಿ ಯಶಸ್ವಿಯಾಗಿ ಸಲ್ಲಿಸಲಾಗಿದೆ!"
        }
    }

    t = texts[language]

    st.title(t["title"])

    name = st.text_input(t["name"])
    location = st.text_input(t["location"])
    description = st.text_area(t["desc"])

    if st.button(t["submit"]):
        submit_report(name, location, description)
        st.success(t["success"])