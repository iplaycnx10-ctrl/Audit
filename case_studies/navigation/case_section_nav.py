import streamlit as st


SECTIONS = {
    "strategic_audit": "Strategic Audit Process",
    "kpi_framework": "KPI Framework",
    "dashboard_preview": "Dashboard Preview",
    "ai_insight": "AI Insight Layer",
    "strategic_conclusion": "Strategic Conclusion",
}


def render():
    if "selected_case_section" not in st.session_state:
        st.session_state["selected_case_section"] = "strategic_audit"

    st.markdown(
        """
        <style>
        button[data-testid="stBaseButton-secondary"],
        div.stButton > button,
        div.stButton > button[kind="secondary"] {
            height: 32px !important;
            min-height: 32px !important;
            padding: 0 12px !important;
            border-radius: 10px !important;
            font-size: 12px !important;
            font-weight: 850 !important;
            white-space: nowrap !important;
            background: rgba(255,255,255,.035) !important;
            background-color: rgba(255,255,255,.035) !important;
            color: #f8fafc !important;
            border: 1px solid rgba(255,255,255,.10) !important;
            box-shadow: none !important;
        }
        button[data-testid="stBaseButton-secondary"]:hover,
        div.stButton > button:hover,
        div.stButton > button[kind="secondary"]:hover {
            color: #facc15 !important;
            border-color: rgba(250,204,21,.55) !important;
            background: rgba(250,204,21,.08) !important;
            background-color: rgba(250,204,21,.08) !important;
        }
        button[data-testid="stBaseButton-secondary"] p,
        div.stButton > button p,
        div.stButton > button[kind="secondary"] p {
            color: inherit !important;
            font-size: 12px !important;
            font-weight: 850 !important;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    cols = st.columns([1, 1, 1, 1, 1], gap="small")
    keys = list(SECTIONS.keys())

    for col, section_key in zip(cols, keys):
        with col:
            label = SECTIONS[section_key]
            if st.session_state["selected_case_section"] == section_key:
                label = "🟡 " + label
            if st.button(label, key=f"case_section_nav_{section_key}", use_container_width=True):
                st.session_state["selected_case_section"] = section_key
                st.rerun()

    return st.session_state["selected_case_section"]
