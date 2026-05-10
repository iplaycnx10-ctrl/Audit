import streamlit as st


def render_tracking_validation():
    st.markdown(
        """
        <div style="border-radius:22px;border:1px solid rgba(250,204,21,.22);background:linear-gradient(135deg,rgba(250,204,21,.055),rgba(255,255,255,.018));padding:22px 24px;margin:0 0 22px 0;box-sizing:border-box;box-shadow:0 14px 34px rgba(0,0,0,.10);">
          <div style="font-size:15px;color:#fff;font-weight:950;margin-bottom:8px;">5. Tracking Validation Check</div>
          <div style="font-size:13px;color:#facc15;font-weight:950;margin-bottom:14px;">ตรวจสอบ GA4 + Pixel ก่อนใช้วัดผล</div>
          <div style="font-size:14px;color:#d7e8dd;line-height:1.8;margin-bottom:16px;">
            หลังจากปรับแคมเปญและเส้นทางลูกค้าแล้ว ต้องตรวจสอบว่า GA4 และ Meta Pixel เก็บ Event สำคัญได้ถูกต้องหรือไม่ เพื่อให้ข้อมูลที่ใช้วัดผลและ Optimize แคมเปญไม่คลาดเคลื่อน
          </div>
          <div style="display:grid;grid-template-columns:repeat(2,1fr);gap:12px;margin-bottom:16px;">
            <div style="padding:14px 16px;border-radius:16px;border:1px solid rgba(250,204,21,.18);background:rgba(250,204,21,.045);">
              <div style="font-size:12px;color:#facc15;font-weight:950;letter-spacing:.10em;text-transform:uppercase;margin-bottom:8px;">ควรใช้ตอนไหน</div>
              <div style="font-size:13.5px;color:#d7e8dd;line-height:1.65;">ช่วง 3–7 วันแรกหลังเริ่มรันแคมเปญใหม่<br><span style="color:#9fb5a8;">เช็คว่า Event ถูกยิงครบ ก่อนนำข้อมูลไปตัดสินผลในรอบ 7–14 วัน</span></div>
            </div>
            <div style="padding:14px 16px;border-radius:16px;border:1px solid rgba(82,255,154,.16);background:rgba(82,255,154,.04);">
              <div style="font-size:12px;color:#52ff9a;font-weight:950;letter-spacing:.10em;text-transform:uppercase;margin-bottom:8px;">สิ่งที่ต้องวัด</div>
              <div style="font-size:13.5px;color:#d7e8dd;line-height:1.65;">Page View, View Content, Add LINE, Lead, Booking หรือ Purchase<br><span style="color:#9fb5a8;">ดูว่า GA4 / Pixel / หลังบ้าน มีทิศทางสอดคล้องกันหรือไม่</span></div>
            </div>
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
