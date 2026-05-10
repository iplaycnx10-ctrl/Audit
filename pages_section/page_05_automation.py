import streamlit as st
from components.common import drive_image_url, section


AUTOMATION_LINK = "https://drive.google.com/file/d/1IpqUubvu9G4xOnWd_XKIbz00XAMwzyG7/view?usp=sharing"


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
