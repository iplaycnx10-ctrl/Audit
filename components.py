import streamlit as st


def section(num, title, body_html):
    st.markdown(
        f"<div class='section'><div class='num'>{num}</div><div class='title'>{title}</div><div class='body'>{body_html}</div></div>",
        unsafe_allow_html=True,
    )


def metric(label, value, note):
    st.markdown(
        f"<div class='metric'><div class='metric-label'>{label}</div><div class='metric-value'>{value}</div><div class='metric-note'>{note}</div></div>",
        unsafe_allow_html=True,
    )


def card(title, body_html):
    st.markdown(
        f"<div class='card'><h3>{title}</h3><p>{body_html}</p></div>",
        unsafe_allow_html=True,
    )
