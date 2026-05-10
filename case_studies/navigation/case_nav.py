import streamlit as st


CASES = {
    "case_01": "CASE 1 — Performance Marketing Audit",
    "case_02": "CASE 2 — Branding Strategy Analysis",
}


def render():
    if "selected_case_study" not in st.session_state:
        st.session_state["selected_case_study"] = "case_01"

    if st.session_state["selected_case_study"] == "case_03":
        st.session_state["selected_case_study"] = "case_01"

    st.markdown(
        """
        <style>
        button[data-testid="stBaseButton-secondary"],
        div.stButton > button,
        div.stButton > button[kind="secondary"] {
            height: 32px !important;
            min-height: 32px !important;
            padding: 0 14px !important;
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

    col1, col2 = st.columns([1, 1], gap="small")

    with col1:
        label = CASES["case_01"]
        if st.session_state["selected_case_study"] == "case_01":
            label = "🟡 " + label
        if st.button(label, key="case_nav_01", use_container_width=True):
            st.session_state["selected_case_study"] = "case_01"
            st.rerun()

    with col2:
        label = CASES["case_02"]
        if st.session_state["selected_case_study"] == "case_02":
            label = "🟡 " + label
        if st.button(label, key="case_nav_02", use_container_width=True):
            st.session_state["selected_case_study"] = "case_02"
            st.rerun()

    return st.session_state["selected_case_study"]
