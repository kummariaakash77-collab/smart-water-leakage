import streamlit as st
from datetime import datetime
from utils.report_manager import add_report
import os

def show_report_page():

    st.title("💧 Report Water Leakage")

    reporter_name = st.text_input("Your Name")

    location = st.text_input("Location")

    issue_type = st.selectbox(
        "Leakage Type",
        [
            "Pipe Leakage",
            "Water Tank Overflow",
            "Broken Tap",
            "Underground Leak"
        ]
    )

    description = st.text_area("Description")

    severity = st.selectbox(
        "Severity",
        ["Low", "Medium", "High"]
    )

    uploaded_file = st.file_uploader(
        "Upload Leakage Photo",
        type=["jpg", "jpeg", "png"]
    )

    if uploaded_file is not None:
        st.image(
            uploaded_file,
            caption="Leakage Image Preview",
            use_container_width=True
        )

    if st.button("Submit Report"):

        report_id = f"WL{int(datetime.now().timestamp())}"

        image_path = ""

        if uploaded_file:

            os.makedirs("uploads/images", exist_ok=True)

            image_path = f"uploads/images/{report_id}_{uploaded_file.name}"

            with open(image_path, "wb") as f:
                f.write(uploaded_file.getbuffer())

        add_report(
            report_id,
            reporter_name,
            location,
            issue_type,
            description,
            severity,
            image_path,
            "Pending",
            str(datetime.now())
        )

        st.success(
            f"✅ Report Submitted Successfully! ID: {report_id}"
        )