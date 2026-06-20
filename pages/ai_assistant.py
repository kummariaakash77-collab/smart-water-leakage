import streamlit as st
import requests
import pandas as pd
import google.generativeai as genai

from utils.report_manager import get_report_counts, get_all_reports

from agents.water_agent.tools import (
    get_water_reports,
    get_pending_reports,
    get_resolved_reports,
    get_summary,
)


# ---------------- LOCAL AI (OLLAMA) ----------------
def run_ollama(prompt):
    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "llama3",
                "prompt": prompt,
                "stream": False
            }
        )
        return response.json().get("response", "")
    except:
        return "❌ Ollama not running. Start: ollama run llama3"


# ---------------- SYSTEM CONTEXT BUILDER ----------------
def build_system_context():

    total, pending, resolved = get_report_counts()
    reports = get_all_reports()

    df = pd.DataFrame(reports, columns=[
        "ID", "Report ID", "Name", "Location", "Issue Type",
        "Description", "Severity", "Image", "Status", "Date"
    ])

    top_locations = "No data"
    if not df.empty:
        top_locations = df["Location"].value_counts().head(5).to_string()

    context = f"""
You are a Smart Civic Water Leakage AI Assistant.

SYSTEM DATA:
- Total Reports: {total}
- Pending Reports: {pending}
- Resolved Reports: {resolved}

Top Affected Locations:
{top_locations}

Rules:
- Use ONLY this system data
- Be short, accurate, and helpful
- If asked about counts, use given values
"""

    return context


# ---------------- AI PAGE ----------------
def show_ai_page(language, ai_mode, api_key):

    st.title("🤖 Data Intelligent Civic AI")

    st.info("Ask: pending reports, locations, summaries, insights")

    user_input = st.text_area("💬 Ask your question", height=120)

    if st.button("🚀 Get Answer"):

        if not user_input.strip():
            st.warning("Please enter a question")
            return

        # ---------------- LOCAL AI (OLLAMA) ----------------
        if ai_mode == "Local AI (Ollama)":

            context = build_system_context()

            full_prompt = f"""
{context}

User Question:
{user_input}
"""

            with st.spinner("Analyzing civic data with Ollama..."):
                result = run_ollama(full_prompt)

            st.success("AI Response")
            st.write(result)

        # ---------------- BYOK (GEMINI) ----------------
        elif ai_mode == "BYOK (API Key)":

            if not api_key:
                st.error("Please enter Gemini API Key in sidebar")
                return

            try:
                genai.configure(api_key=api_key)

                models = genai.list_models()

                model_name = None
                for m in models:
                    if "generateContent" in m.supported_generation_methods:
                        model_name = m.name
                        break

                if not model_name:
                    st.error("No compatible Gemini model found")
                    return

                model = genai.GenerativeModel(model_name)

                chat = model.start_chat()

                context = build_system_context()

                prompt = f"""
{context}

User Question:
{user_input}
"""

                with st.spinner("Analyzing civic data with Gemini AI..."):
                    response = chat.send_message(prompt)

                st.success("AI Response")
                st.write(response.text)

            except Exception as e:
                st.error(f"Gemini Error: {str(e)}")

        # ---------------- GOOGLE ADK AGENT ----------------
        elif ai_mode == "Google ADK Agent":

            question = user_input.lower()

            if "pending" in question:

                result = get_pending_reports()

                st.success("🤖 ADK Agent Response")
                st.write(
                    f"Pending Reports: {result['pending_reports']}"
                )

            elif "resolved" in question:

                result = get_resolved_reports()

                st.success("🤖 ADK Agent Response")
                st.write(
                    f"Resolved Reports: {result['resolved_reports']}"
                )

            elif (
                "summary" in question
                or "statistics" in question
                or "report" in question
            ):

                result = get_summary()

                st.success("🤖 ADK Agent Response")
                st.text(result)

            else:

                result = get_water_reports()

                st.success("🤖 ADK Agent Response")

                st.json({
                    "total_reports": result["total_reports"],
                    "pending_reports": result["pending_reports"],
                    "resolved_reports": result["resolved_reports"]
                })

        # ---------------- NONE ----------------
        else:
            st.warning("Select AI mode first")