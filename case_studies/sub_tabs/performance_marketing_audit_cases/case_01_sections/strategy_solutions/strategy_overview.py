import streamlit as st


def render():
    st.markdown(
        """
        <div style="margin-top:14px;padding:24px;border-radius:22px;border:1px dashed rgba(250,204,21,.22);background:rgba(255,255,255,.018);min-height:220px;display:flex;align-items:center;justify-content:center;">
          <div style="text-align:center;">
            <div style="font-size:13px;font-weight:950;letter-spacing:.16em;text-transform:uppercase;color:#facc15;margin-bottom:14px;">
              Strategy & Solution Layer
            </div>
            <div style="font-size:15px;color:#d7e8dd;line-height:1.7;max-width:520px;">
              Placeholder สำหรับส่วน “กลยุทธ์และแนวทางแก้ไข”<br>
              เตรียมรองรับ Strategic Recommendation, Funnel Fix, Creative Direction และ Scaling Framework
            </div>
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
