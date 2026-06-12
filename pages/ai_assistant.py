import streamlit as st
import requests

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
        return "❌ Ollama not running. Start with: ollama run llama3"


# ---------------- AI PAGE ----------------
def show_ai_page(language, ai_mode, api_key):

    st.title("🤖 AI Assistant (Smart Civic AI)")

    st.info("Ask questions about reports, analytics, or system insights")

    # better UI
    user_input = st.text_area("💬 Enter your query", height=120)

    col1, col2 = st.columns(2)

    with col1:
        run_btn = st.button("🚀 Run AI")

    with col2:
        clear_btn = st.button("🧹 Clear")

    if clear_btn:
        st.rerun()

    if run_btn:

        if not user_input.strip():
            st.warning("Please enter a query first")
            return

        # ---------------- LOCAL AI ----------------
        if ai_mode == "Local AI (Ollama)":
            with st.spinner("Thinking with Local AI..."):
                result = run_ollama(user_input)
            st.success("AI Response")
            st.write(result)

        # ---------------- BYOK MODE ----------------
        elif ai_mode == "BYOK (API Key)":

            if not api_key:
                st.error("Please enter API key in sidebar")
                return

            st.info("BYOK mode is ready (OpenAI/Gemini integration can be added next)")

            st.write("Your Query:")
            st.code(user_input)

        # ---------------- NONE ----------------
        else:
            st.warning("Select AI mode from sidebar first")