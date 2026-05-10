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


def exp_card(title: str, body: str, link_text: str | None = None, link_url: str | None = None) -> None:
    link_html = ""
    if link_text and link_url:
        link_html = f"<p style='margin-top:12px;'><a href='{link_url}' target='_blank' style='color:#52ff9a;font-weight:900;text-decoration:none;'>{link_text} →</a></p>"

    st.markdown(
        f"<div class='card'><h3>{title}</h3><p>{body}</p>{link_html}</div>",
        unsafe_allow_html=True,
    )


def drive_image_url(url: str) -> str:
    url = str(url or '').strip()

    if 'drive.google.com' not in url:
        return url

    if '/file/d/' in url:
        file_id = url.split('/file/d/')[1].split('/')[0]
        return f'https://drive.google.com/thumbnail?id={file_id}&sz=w1600'

    if 'id=' in url:
        file_id = url.split('id=')[1].split('&')[0]
        return f'https://drive.google.com/thumbnail?id={file_id}&sz=w1600'

    return url


def ci_showcase(title: str, url: str) -> None:
    img_url = drive_image_url(url)
    frame = ""
    if img_url:
        frame = f"<img src='{img_url}' alt='{title}' referrerpolicy='no-referrer' />"

    st.markdown(
        f"<div class='ci-card'><div class='ci-frame'>{frame}</div></div>",
        unsafe_allow_html=True,
    )
