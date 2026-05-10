import streamlit as st
from components.common import drive_image_url, section


AUTOMATION_LINK = "https://drive.google.com/file/d/1IpqUubvu9G4xOnWd_XKIbz00XAMwzyG7/view?usp=sharing"

APP_IMAGE_LINKS = [
    "https://drive.google.com/file/d/1hkNiMzAh16b9VBMjTihwzVsaLQPy6Yjz/view?usp=sharing",
    "https://drive.google.com/file/d/1-jFfqNbBk9Lt-xA2s1LnUd18ybHMv1Y1/view?usp=sharing",
    "https://drive.google.com/file/d/1Eo3tla4gfcinMGZMqin6ERs2Xkq2XIve/view?usp=sharing",
    "https://drive.google.com/file/d/1oJlA6u7mm7qYqr8u2Ow4O11x6cvZ1x9c/view?usp=sharing",
    "https://drive.google.com/file/d/1W1gxhSDC7CAdPUQnpBVh7UhY0Hi7MuTe/view?usp=sharing",
]


def app_image_card(link, alt="APP Preview"):
    img = drive_image_url(link)
    st.markdown(
        f"""
        <div style="
            border:1px solid rgba(82,255,154,.20);
            border-radius:22px;
            padding:10px;
            background:rgba(255,255,255,.035);
            box-shadow:0 18px 54px rgba(0,0,0,.20);
            height:250px;
            display:flex;
            align-items:center;
            justify-content:center;
            overflow:hidden;
            box-sizing:border-box;
            margin-bottom:18px;
        ">
            <img src="{img}" alt="{alt}" referrerpolicy="no-referrer" style="
                width:100%;
                height:100%;
                object-fit:cover;
                border-radius:15px;
                display:block;
            " />
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_app_gallery():
    st.markdown(
        """
        <div class='section' style='margin-top:28px;'>
            <div class='num'>APP</div>
            <div class='title'>ประเมิน APP Marketing AI intel <span style='font-size:18px;color:#9fb5a8;'>(อยู่ในช่วงกำลังพัฒนา)</span></div>
            <div class='body'>ตัวอย่างหน้าจอระบบ AI Marketing Intelligence สำหรับประเมินผลและต่อยอดการวิเคราะห์</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    row1 = st.columns(3, gap="large")
    for col, link in zip(row1, APP_IMAGE_LINKS[:3]):
        with col:
            app_image_card(link)

    row2 = st.columns(3, gap="large")
    for index, col in enumerate(row2):
        with col:
            if index < 2:
                app_image_card(APP_IMAGE_LINKS[index + 3])
            else:
                st.markdown(
                    """
                    <div style="
                        border:1px dashed rgba(82,255,154,.18);
                        border-radius:22px;
                        height:250px;
                        background:rgba(255,255,255,.018);
                        margin-bottom:18px;
                    "></div>
                    """,
                    unsafe_allow_html=True,
                )


def render():
    section(
        "05. AUTOMATION ARCHITECTURE",
        "Marketing Brain with AI Agent Workflows",
        "ออกแบบ Workflow เชื่อม n8n, AI API, Google Sheets และ Dashboard เพื่อเปลี่ยนข้อมูลโฆษณาเป็น Insight และ Action แบบอัตโนมัติ"
    )

    automation_img = drive_image_url(AUTOMATION_LINK)
    st.image(automation_img, use_container_width=True)

    render_app_gallery()
