import streamlit as st


def render():
    st.markdown(
        """
        <div class="section" style="padding:22px 24px;">
          <div class="num">CASE 1</div>
          <div class="title" style="font-size:24px;margin-bottom:8px;">Medical Aesthetic Funnel Analysis</div>
          <div class="body" style="font-size:14.5px;line-height:1.65;color:#d7e8dd;max-width:860px;">
            <b>กิจการ:</b> Medical Aesthetic<br><br>
            <b>ปัญหาหลักที่ตรวจพบ</b>
          </div>
          <div class="body" style="font-size:14px;line-height:1.7;color:#9fb5a8;max-width:880px;margin-top:10px;">
            <b style="color:#d7ffe6;">Traffic Quality Problem</b> → คนคลิกมา แต่ไม่ได้สนใจจริง<br>
            <b style="color:#d7ffe6;">Conversion Friction Problem</b> → สนใจ แต่ติดตอนทัก / จอง / กรอกฟอร์ม<br>
            <b style="color:#d7ffe6;">Offer-Market Mismatch</b> → โฆษณาดี แต่ข้อเสนอไม่แรงพอให้ตัดสินใจ
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
