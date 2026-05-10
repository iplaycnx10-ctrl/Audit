import streamlit as st


def render():
    st.markdown("<div class='section'><div class='num'>02. INDUSTRY EXPERIENCE</div><div class='title'>Industry Experience</div>", unsafe_allow_html=True)

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.markdown("<div class='card'><h3>Retail & High-Ticket Electronics</h3><p>บริหารกลยุทธ์ Online-to-Offline สำหรับสินค้ากลุ่ม Premium Gadgets และเครื่องใช้ไฟฟ้ามูลค่าสูง เพื่อดึงทราฟฟิกออนไลน์เข้าสู่หน้าร้าน</p></div>", unsafe_allow_html=True)

    with c2:
        st.markdown("<div class='card'><h3>Financial Services</h3><p>Lead Generation สำหรับสินเชื่อธุรกิจ วางระบบคัดกรองผ่าน Message Funnel และอ่านสัญญาณความพร้อมจากพฤติกรรมแชท</p></div>", unsafe_allow_html=True)

    with c3:
        st.markdown("<div class='card'><h3>Hotel & Hospitality Marketing</h3><p>วางแผนการสื่อสารและกระตุ้นยอดจองห้องพักสำหรับธุรกิจโรงแรม โดยใช้ดาต้าเพื่อหาช่วงเวลาที่ Demand ตลาดสูงที่สุด</p></div>", unsafe_allow_html=True)

    with c4:
        st.markdown("<div class='card'><h3>Streamer & Gaming Content Creator</h3><p>มีประสบการณ์ทำคอนเทนต์และไลฟ์สตรีมบน TikTok ในนาม <b>KhunlunGamer</b> เข้าใจการดึงความสนใจแบบ Real-time, Community Engagement และ Audience Relationship</p><p style='margin-top:12px;'><a href='https://www.tiktok.com/@khunlungamer?is_from_webapp=1&sender_device=pc' target='_blank' style='color:#52ff9a;font-weight:900;text-decoration:none;'>View TikTok Profile →</a></p></div>", unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)
