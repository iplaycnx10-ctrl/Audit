import streamlit as st


def render():
    st.markdown(
        """
        <div style="border-radius:22px;border:1px solid rgba(250,204,21,.22);background:linear-gradient(135deg,rgba(250,204,21,.055),rgba(255,255,255,.018));padding:24px 26px;margin:14px 0 22px 0;box-sizing:border-box;box-shadow:0 14px 34px rgba(0,0,0,.10);">
          <div style="font-size:13px;font-weight:950;letter-spacing:.16em;text-transform:uppercase;color:#facc15;margin-bottom:12px;">
            ระยะวัดผลหลังปรับกลยุทธ์
          </div>
          <div style="font-size:14.5px;color:#d7e8dd;line-height:1.75;max-width:920px;">
            หลังจากปรับแคมเปญด้วย Intent Filtering Creative, Low-Ticket Booking Offer และ LINE CRM Capture ขั้นตอนถัดไปคือการวัดผลว่าแนวทางที่ใช้ช่วยให้ Traffic และ Lead มีคุณภาพขึ้นจริงหรือไม่
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
