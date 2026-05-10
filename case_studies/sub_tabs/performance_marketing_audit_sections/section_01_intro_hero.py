import streamlit as st


def render():
    st.markdown(
        """
        <div class="section">
          <div class="num">🟢 Section 1 — Intro Hero</div>
          <div class="title">Performance Marketing Audit Case Study</div>
          <div class="body">
            เคสนี้ออกแบบมาเพื่อแสดงวิธีคิดในการตรวจสอบ Performance Marketing จากข้อมูลจริง ไม่ใช่แค่ดู ROAS แล้วตัดสินว่าแคมเปญดีหรือแย่<br><br>
            จุดสำคัญคือการอ่านสัญญาณทั้ง Funnel: ต้นน้ำ กลางน้ำ และปลายน้ำ เพื่อหาให้เจอว่าเงินโฆษณากำลังรั่วตรงไหน และควรแก้ด้วย Action แบบไหนก่อนเพิ่มงบ
          </div>
          <div class="quote">
            Core Idea: ไม่ได้ Optimize เพื่อให้ตัวเลขสวย แต่ Optimize เพื่อให้ธุรกิจตัดสินใจถูกขึ้นจากข้อมูลจริง
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
