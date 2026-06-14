import streamlit as st
import os
from utils.report_manager import submit_report
from utils.translations import get_texts


def show_report_page(language):

    t = get_texts(language)

    st.title(t["report_title"])

    name = st.text_input(t["name"])

    location = st.text_input(t["location"])

    issue_type = st.selectbox(
        t["issue_type"],
        [
            t["water_leakage"],
            t["pipe_burst"],
            t["drain_overflow"],
            t["water_waste"]
        ]
    )

    severity = st.selectbox(
        t["severity"],
        [
            t["low"],
            t["medium"],
            t["high"]
        ]
    )

    description = st.text_area(t["description"])

    uploaded_file = st.file_uploader(
        t["upload"],
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

    if st.button(t["submit"]):

        report_id = submit_report(
            reporter_name=name,
            location=location,
            issue_type=issue_type,
            description=description,
            severity=severity,
            image_path=image_path
        )

        st.success(f"{t['success']}{report_id}")