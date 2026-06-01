# app.py
import streamlit as st
from agent import DeepResearcherAgent
import os

st.set_page_config(
    page_title="Deep Research Agent",
    page_icon="🔎",
    layout="wide"
)

# --- Gradient Dark Background ---
st.markdown("""
<style>
body, .stApp {
    background: linear-gradient(135deg, #111111, #1f1f1f);
    color: white;
}
</style>
""", unsafe_allow_html=True)

# --- Header ---
st.markdown("""
<div style="text-align: center; padding: 30px 0;">
    <h1 style="font-size: 2.5rem;">🔎 Agentic Deep Searcher with <span style="color: #fb542c;">Agno</span> & <span style="color: #8564ff;">Scrapegraph</span></h1>
</div>
""", unsafe_allow_html=True)

# --- Sidebar for API Keys ---
with st.sidebar:
    st.title("🔐 API Keys")
    nebius_api_key = st.text_input("Nebius API Key", type="password")
    scrapegraph_api_key = st.text_input("Scrapegraph API Key", type="password")

    st.divider()

    st.subheader("ℹ️ About")
    st.markdown("""
This app uses `DeepResearcherAgent` which includes:
- 🔍 **Searcher**: Extracts information from the web  
- 🧠 **Analyst**: Understands and interprets research  
- ✍️ **Writer**: Summarizes into a polished report
""")
    st.markdown("---")
    st.markdown("Developed with ❤️ by Guneeth")

# --- Chat Interface ---
user_input = st.chat_input("💬 Ask a research question...")

if user_input:
    if not nebius_api_key or not scrapegraph_api_key:
        st.error("Please enter both API keys in the sidebar.")
    else:
        try:
            agent = DeepResearcherAgent(
                nebius_api_key=nebius_api_key,
                scrapegraph_api_key=scrapegraph_api_key,
            )

            with st.status("🚀 Executing research plan...", expanded=True) as status:
                status.write("🧠 **Phase 1: Researching** – Gathering info...")
                research_content = agent.searcher.run(user_input)

                status.write("🔬 **Phase 2: Analyzing** – Synthesizing insights...")
                analysis = agent.analyst.run(research_content.content)

                status.write("✍️ **Phase 3: Writing** – Generating report...")
                report_iterator = agent.writer.run(analysis.content, stream=True)

            full_report = ""
            report_container = st.empty()
            for chunk in report_iterator:
                if chunk.content:
                    full_report += chunk.content
                    report_container.markdown(full_report)

        except Exception as e:
            st.error(f"⚠️ Error: {e}")

