import streamlit as st
from components.common import section


def render():
    section(
        "07. CONTACT",
        "Contact & Collaboration",
        "พร้อมร่วมงานด้าน Performance Marketing, AI Automation, Dashboard และ Business Intelligence"
    )

    st.markdown(
        """
        <div class='section'>
            <div class='title'>Contact Information</div>
            <div class='body'>
                Email: your@email.com<br><br>
                TikTok: @khunlungamer<br><br>
                Location: Chiang Mai, Thailand
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
