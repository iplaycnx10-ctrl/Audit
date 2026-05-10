import streamlit as st


CASES = {
    "case_01": "CASE 1 — Performance Marketing Audit",
    "case_02": "CASE 2 — Branding Strategy Analysis",
    "case_03": "CASE 3 — Journey Traffic Leak Analysis",
}


def render():
    if "selected_case_study" not in st.session_state:
        st.session_state["selected_case_study"] = "case_01"

    st.markdown(
        """
        <style>
        div[data-testid="column"] .stButton > button {
            height: 30px !important;
            min-height: 30px !important;
            padding: 0 13px !important;
            border-radius: 10px !important;
            font-size: 12px !important;
            font-weight: 850 !important;
            white-space: nowrap !important;
            background: #050806 !important;
            color: #f8fafc !important;
            border: 1px solid rgba(250,204,21,.22) !important;
            box-shadow: none !important;
        }
        div[data-testid="column"] .stButton > button:hover {
            color: #facc15 !important;
            border-color: rgba(250,204,21,.55) !important;
            background: rgba(250,204,21,.08) !important;
        }
        </style>
        <div style="background:#020302;border:1px solid rgba(250,204,21,.34);border-radius:14px;padding:8px 10px;margin:8px auto 8px auto;max-width:900px;box-sizing:border-box;box-shadow:0 10px 28px rgba(0,0,0,.22);"></div>
        """,
        unsafe_allow_html=True,
    )

    col1, col2, col3 = st.columns([1, 1, 1], gap="small")

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

    with col3:
        label = CASES["case_03"]
        if st.session_state["selected_case_study"] == "case_03":
            label = "🟡 " + label
        if st.button(label, key="case_nav_03", use_container_width=True):
            st.session_state["selected_case_study"] = "case_03"
            st.rerun()

    return st.session_state["selected_case_study"]
