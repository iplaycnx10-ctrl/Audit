import streamlit as st


def render():
    st.markdown(
        """
        <div class="section">
          <div class="num">Case Study Sub Tab 01</div>
          <div class="title">📈 Performance Marketing Audit</div>
          <div class="body">
            หน้านี้จะใช้เล่าเคสการตรวจสอบ Performance Marketing แบบเป็นระบบ ตั้งแต่ปัญหาในตัวเลข ไปจนถึง Action ที่ควรทำจริง<br><br>
            โครงหลักของเคสนี้จะเน้น: Funnel Diagnostic, KPI Audit, ROAS / CPR Analysis, Creative Fatigue, Retargeting Quality และ Recommendation ที่อ่านรู้เรื่องสำหรับเจ้าของธุรกิจ
          </div>
          <div class="quote">
            Framework: Problem → Data Signal → Root Cause → Action → KPI Impact
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
