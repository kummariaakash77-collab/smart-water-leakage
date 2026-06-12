import streamlit as st
import os
from utils.report_manager import submit_report

def show_report_page(language):

    st.title("💧 Report Water Leakage")

    name = st.text_input("👤 Name")

    location = st.text_input("📍 Location")

    issue_type = st.selectbox(
        "🚰 Issue Type",
        [
            "Water Leakage",
            "Pipe Burst",
            "Drain Overflow",
            "Water Waste"
        ]
    )

    severity = st.selectbox(
        "⚠️ Severity",
        [
            "Low",
            "Medium",
            "High"
        ]
    )

    description = st.text_area("📝 Description")

    uploaded_file = st.file_uploader(
        "📸 Upload Image",
        type=["jpg", "jpeg", "png"]
    )

    image_path = ""

    if uploaded_file is not None:

        os.makedirs("uploads", exist_ok=True)

        image_path = os.path.join(
            "uploads",
            uploaded_file.name
        )

        with open(image_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        st.image(image_path, width=300)

    if st.button("📤 Submit Report"):

        report_id = submit_report(
            reporter_name=name,
            location=location,
            issue_type=issue_type,
            description=description,
            severity=severity,
            image_path=image_path
        )

        st.success(
            f"Report Submitted Successfully! Report ID: {report_id}"
        )