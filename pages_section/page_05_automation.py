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

    row1 = st.columns(3, gap="medium")
    for col, link in zip(row1, APP_IMAGE_LINKS[:3]):
        with col:
            st.image(drive_image_url(link), use_container_width=True)

    row2 = st.columns(2, gap="medium")
    for col, link in zip(row2, APP_IMAGE_LINKS[3:]):
        with col:
            st.image(drive_image_url(link), use_container_width=True)


def render():
    section(
        "05. AUTOMATION ARCHITECTURE",
        "Marketing Brain with AI Agent Workflows",
        "ออกแบบ Workflow เชื่อม n8n, AI API, Google Sheets และ Dashboard เพื่อเปลี่ยนข้อมูลโฆษณาเป็น Insight และ Action แบบอัตโนมัติ"
    )

    automation_img = drive_image_url(AUTOMATION_LINK)

    left_col, right_col = st.columns(2, gap="large")
    with left_col:
        st.image(automation_img, use_container_width=True)

    with right_col:
        st.markdown(
            """
            <div class='section' style='min-height:360px;display:flex;align-items:center;justify-content:center;text-align:center;'>
                <div>
                    <div class='num'>NEXT VISUAL SLOT</div>
                    <div class='title'>ใส่รูปเพิ่มเติมตรงนี้</div>
                    <div class='body'>พื้นที่ครึ่งขวาสำหรับใส่ภาพ Workflow / Dashboard / Result เพิ่มเติม</div>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    render_app_gallery()
