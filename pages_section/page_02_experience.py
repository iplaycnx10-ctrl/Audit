import streamlit as st
from components.common import exp_card, ci_showcase

CI_DESIGN_LINK_1 = "https://drive.google.com/file/d/1rbL0PhE85Pu2Y_VjCY7RzWBAuDjG8jEM/view?usp=sharing"
CI_DESIGN_LINK_2 = "https://drive.google.com/file/d/1rgcXSo4Z-7HGjNfNBY8ni2vb1HKZM7OT/view?usp=sharing"
CI_DESIGN_LINK_3 = "https://drive.google.com/file/d/1NFSGbKlcF51OHJ29vPYchoOXh9GDkfyq/view?usp=sharing"
CI_DESIGN_LINK_4 = "https://drive.google.com/file/d/1_fOiOGm8v3qBLntLcSYGH87gBQcmgJsQ/view?usp=sharing"


def render():
    st.markdown("<div class='section'><div class='num'>02. INDUSTRY EXPERIENCE</div><div class='title'>Industry Experience</div>", unsafe_allow_html=True)
    st.markdown("""
    <div class='experience-timeline'>
      <div class='timeline-step'><div class='timeline-year'>2018-2024</div><div class='timeline-badge'>1</div></div>
      <div class='timeline-step'><div class='timeline-year'>2024-2025</div><div class='timeline-badge'>2</div></div>
      <div class='timeline-step'><div class='timeline-year'>2026</div><div class='timeline-badge'>3</div></div>
      <div class='timeline-step'><div class='timeline-year'>2026</div><div class='timeline-badge'>4</div></div>
    </div>
    """, unsafe_allow_html=True)
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        exp_card("Financial Services", "Lead Generation สำหรับสินเชื่อธุรกิจ วางระบบคัดกรองผ่าน Message Funnel และอ่านสัญญาณความพร้อมจากพฤติกรรมแชท", "View Loan Ads", "#")
    with c2:
        exp_card("Streamer & Gaming Content Creator", "มีประสบการณ์ทำคอนเทนต์และไลฟ์สตรีมบน TikTok ในนาม KhunlunGamer เข้าใจ Real-time Engagement และ Audience Relationship", "View TikTok Profile", "https://www.tiktok.com/@khunlungamer?is_from_webapp=1&sender_device=pc")
    with c3:
        exp_card("Hotel & Hospitality Marketing", "วางแผนการสื่อสารและกระตุ้นยอดจองห้องพักสำหรับธุรกิจโรงแรม โดยใช้ดาต้าเพื่อหาช่วงเวลาที่ Demand ตลาดสูงที่สุด", "View Hospitality", "#")
    with c4:
        exp_card("Retail & High-Ticket Electronics", "บริหารกลยุทธ์ Online-to-Offline สำหรับสินค้ากลุ่ม Premium Gadgets และเครื่องใช้ไฟฟ้ามูลค่าสูง เพื่อดึงทราฟฟิกออนไลน์เข้าสู่หน้าร้าน", "View Retail", "#")
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<div class='section'><div class='num'>CREATIVE DESIGN SHOWCASE</div><div class='title'>CI ที่เคยออกแบบ</div>", unsafe_allow_html=True)
    row1_col1, row1_col2 = st.columns(2)
    with row1_col1:
        ci_showcase("CI Design 01", CI_DESIGN_LINK_1, "Key Visual / Brand Direction")
    with row1_col2:
        ci_showcase("CI Design 02", CI_DESIGN_LINK_2, "Creative Layout / Campaign Visual")
    row2_col1, row2_col2 = st.columns(2)
    with row2_col1:
        ci_showcase("CI Design 03", CI_DESIGN_LINK_3, "Social Visual / Content Design")
    with row2_col2:
        ci_showcase("CI Design 04", CI_DESIGN_LINK_4, "Ad Creative / Performance Visual")
    st.markdown("</div>", unsafe_allow_html=True)
