import streamlit as st


def drive_image_url(url: str) -> str:
    url = str(url or '').strip()
    if 'drive.google.com' not in url:
        return url
    if '/file/d/' in url:
        file_id = url.split('/file/d/')[1].split('/')[0]
        return f'https://drive.google.com/uc?export=view&id={file_id}'
    if 'id=' in url:
        file_id = url.split('id=')[1].split('&')[0]
        return f'https://drive.google.com/uc?export=view&id={file_id}'
    return url


def ci_showcase(title: str, url: str, note: str) -> None:
    img_url = drive_image_url(url)
    if img_url:
        frame = f"<img src='{img_url}' alt='{title}' />"
        link = f"<a class='ci-link' href='{url}' target='_blank'>Open design →</a>"
    else:
        frame = "วาง Google Drive image link<br>ในช่องด้านบน แล้วกด Enter"
        link = "<span class='ci-link'>Waiting for Drive link</span>"

    st.markdown(
        f"<div class='ci-card'><div class='ci-frame'>{frame}</div><h3>{title}</h3><p class='ci-desc'>{note}</p>{link}</div>",
        unsafe_allow_html=True,
    )


def render_ci_showcase(default_links: list[str]) -> None:
    st.markdown(
        "<div class='section'><div class='num'>CREATIVE DESIGN SHOWCASE</div><div class='title'>CI ที่เคยออกแบบ</div><div class='body'>วางลิงก์ Google Drive ในช่องด้านล่าง ระบบจะแสดงรูปทันที</div>",
        unsafe_allow_html=True,
    )
    st.markdown(
        "<div class='ci-input-note'>ตั้งค่าไฟล์ Drive เป็น Anyone with the link can view ก่อนวางลิงก์</div>",
        unsafe_allow_html=True,
    )

    link_col1, link_col2 = st.columns(2)
    with link_col1:
        ci_input_1 = st.text_input("CI Design 01 Google Drive link", value=default_links[0], key="ci_design_link_1")
        ci_input_3 = st.text_input("CI Design 03 Google Drive link", value=default_links[2], key="ci_design_link_3")
    with link_col2:
        ci_input_2 = st.text_input("CI Design 02 Google Drive link", value=default_links[1], key="ci_design_link_2")
        ci_input_4 = st.text_input("CI Design 04 Google Drive link", value=default_links[3], key="ci_design_link_4")

    row1_col1, row1_col2 = st.columns(2)
    with row1_col1:
        ci_showcase("CI Design 01", ci_input_1, "Key Visual / Brand Direction")
    with row1_col2:
        ci_showcase("CI Design 02", ci_input_2, "Creative Layout / Campaign Visual")

    row2_col1, row2_col2 = st.columns(2)
    with row2_col1:
        ci_showcase("CI Design 03", ci_input_3, "Social Visual / Content Design")
    with row2_col2:
        ci_showcase("CI Design 04", ci_input_4, "Ad Creative / Performance Visual")

    st.markdown("</div>", unsafe_allow_html=True)
