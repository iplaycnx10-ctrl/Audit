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
    st.image(automation_img, use_container_width=True)
