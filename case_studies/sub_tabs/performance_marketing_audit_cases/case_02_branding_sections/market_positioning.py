import streamlit as st


def render_market_positioning():
    st.markdown(
        """
        <div style="margin-top:26px;border-radius:22px;border:1px solid rgba(250,204,21,.20);background:linear-gradient(135deg,rgba(250,204,21,.055),rgba(255,255,255,.018));padding:22px 24px;box-sizing:border-box;box-shadow:0 14px 34px rgba(0,0,0,.10);">
          <div style="font-size:13px;font-weight:950;letter-spacing:.16em;text-transform:uppercase;color:#facc15;margin-bottom:12px;">
            Market Positioning
          </div>
          <div style="font-size:15px;color:#fff;font-weight:900;line-height:1.55;margin-bottom:10px;">
            วางตำแหน่งแบรนด์จาก “พื้นที่เชิงพาณิชย์” ไปสู่ “Urban Lifestyle & Business Community”
          </div>
          <div style="font-size:14px;color:#d7e8dd;line-height:1.8;max-width:980px;">
            จุดยืนของแบรนด์ควรไม่ใช่แค่การขายพื้นที่หรือทำเล แต่ควรถูกสื่อสารให้เป็นระบบนิเวศของธุรกิจและไลฟ์สไตล์เมืองเชียงใหม่ ที่รวมผู้ประกอบการ ร้านค้า คาเฟ่ Wellness และ Community คุณภาพไว้ในพื้นที่เดียวกัน
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
