import streamlit as st


def render_market_positioning():
    st.markdown(
        """
        <div style="margin-top:26px;border-radius:22px;border:1px solid rgba(250,204,21,.20);background:linear-gradient(135deg,rgba(250,204,21,.055),rgba(255,255,255,.018));padding:22px 24px;box-sizing:border-box;box-shadow:0 14px 34px rgba(0,0,0,.10);">
          <div style="font-size:13px;font-weight:950;letter-spacing:.16em;text-transform:uppercase;color:#facc15;margin-bottom:12px;">
            Market Positioning
          </div>
          <div style="font-size:15px;color:#fff;font-weight:900;line-height:1.55;margin-bottom:12px;">
            แบรนด์มี Awareness สูงอยู่แล้ว
          </div>
          <div style="font-size:14px;color:#d7e8dd;line-height:1.85;max-width:980px;margin-bottom:14px;">
            ดังนั้นความท้าทายหลักไม่ใช่การสร้างการรับรู้ แต่คือการสร้าง “Investment Confidence” ให้ลูกค้าเชื่อว่าพื้นที่นี้สามารถสร้างโอกาสและผลตอบแทนทางธุรกิจได้จริง
          </div>
          <div style="font-size:14px;color:#bfd1c5;line-height:1.85;max-width:980px;">
            กลยุทธ์การตลาดจึงควรโฟกัสที่การสร้างความเชื่อมั่น สื่อสารศักยภาพของพื้นที่ และสร้างภาพลักษณ์ให้โครงการเป็น Business & Lifestyle Ecosystem ของเชียงใหม่ 🔥
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
