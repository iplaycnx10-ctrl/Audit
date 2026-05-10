import streamlit as st


def load_css(path: str = "styles/portfolio.css") -> None:
    with open(path, "r", encoding="utf-8") as file:
        st.markdown(f"<style>{file.read()}</style>", unsafe_allow_html=True)


def section(num: str, title: str, body_html: str) -> None:
    st.markdown(
        f"<div class='section'><div class='num'>{num}</div><div class='title'>{title}</div><div class='body'>{body_html}</div></div>",
        unsafe_allow_html=True,
    )


def metric(label: str, value: str, note: str) -> None:
    st.markdown(
        f"<div class='metric'><div class='metric-label'>{label}</div><div class='metric-value'>{value}</div><div class='metric-note'>{note}</div></div>",
        unsafe_allow_html=True,
    )
