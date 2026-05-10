import streamlit as st
from components.common import section


def render():
    section(
        "01. STRATEGIST",
        "Technical & Performance Marketing",
        "ผมวางตัวเองเป็นสาย Performance Marketer ที่เชื่อมระหว่าง <span class='green'>Media Buying, Automation, AI Content และ Data Insight</span> เพื่อเปลี่ยนตัวเลขโฆษณาให้กลายเป็นการตัดสินใจทางธุรกิจที่เร็วและแม่นขึ้น"
    )

    st.markdown("<div class='num' style='margin-top:6px;'>TECHNICAL EXPERTISE</div>", unsafe_allow_html=True)
    s1, s2, s3, s4 = st.columns(4)
    with s1:
        st.markdown("<div class='skill-card'><h3>Advanced Media Buying</h3><p>วางโครงสร้างแคมเปญ Meta & TikTok แบบเน้นยอดขาย Conversion พร้อมกลยุทธ์การสเกลงบอย่างเป็นระบบ เพื่อรักษา ROAS และคุณภาพผลลัพธ์</p></div>", unsafe_allow_html=True)
    with s2:
        st.markdown("<div class='skill-card'><h3>Marketing Automation</h3><p>ออกแบบและเชื่อมต่อ Workflow ข้ามแพลตฟอร์มด้วย n8n และ Make เพื่อลดงาน Manual เพิ่มความเร็ว และทำให้ระบบการตลาดทำซ้ำได้</p></div>", unsafe_allow_html=True)
    with s3:
        st.markdown("<div class='skill-card'><h3>AI-Driven Content & Strategy</h3><p>ใช้ Prompt Engineering สร้าง Hook, Script และ Creative Angle สำหรับ TikTok/Reels ที่เน้นหยุดนิ้ว เพิ่มความสนใจ และต่อยอดการซื้อ</p></div>", unsafe_allow_html=True)
    with s4:
        st.markdown("<div class='skill-card'><h3>Data-Actionable Insights</h3><p>สร้าง Dashboard ด้วย Looker Studio อ่านจุดหลุด Drop-off points และแปลงข้อมูลเป็น Action ที่แก้ปัญหายอดขายได้ตรงจุด</p></div>", unsafe_allow_html=True)

    st.markdown("""
        <div class='section'>
          <div class='num'>TECH STACK & TOOLS</div>
          <div class='title'>Tool Stack ที่ใช้ทำงานจริง</div>
          <div class='tool-grid'>
            <div class='tool-card'><div class='tool-card-title'>AD PLATFORMS</div><div class='tool-list'><span class='tool-pill'>Meta Ads</span><span class='tool-pill'>TikTok Ads</span><span class='tool-pill'>Google Ads</span></div></div>
            <div class='tool-card'><div class='tool-card-title'>AUTOMATION</div><div class='tool-list'><span class='tool-pill'>n8n</span><span class='tool-pill'>Make</span><span class='tool-pill'>Zapier</span></div></div>
            <div class='tool-card'><div class='tool-card-title'>AI TOOLS</div><div class='tool-list'><span class='tool-pill'>Gemini API</span><span class='tool-pill'>ChatGPT</span><span class='tool-pill'>Midjourney</span></div></div>
            <div class='tool-card analytics'><div class='tool-card-title'>ANALYTICS</div><div class='tool-list'><span class='tool-pill'>Looker Studio</span><span class='tool-pill'>GA4</span></div></div>
          </div>
          <div class='quote'>“Efficiency is Intelligent Laziness”</div>
        </div>
        """, unsafe_allow_html=True)
