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
                Name: Chayanon Nantavijan<br><br>
                Email: <a href='mailto:iplaycnx.10@gmail.com' style='color:#52ff9a;font-weight:950;text-decoration:none;'>iplaycnx.10@gmail.com</a><br><br>
                Phone: <a href='tel:0980935022' style='color:#52ff9a;font-weight:950;text-decoration:none;'>0980935022</a><br><br>
                TikTok: @khunlungamer<br><br>
                Location: Chiang Mai, Thailand
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
