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
        </div>

        <div style="display:grid;grid-template-columns:repeat(4,1fr);gap:12px;margin-top:12px;margin-bottom:18px;">
          <div class="card" style="height:120px;min-height:120px;padding:16px;">
            <h3 style="font-size:15px;min-height:auto;margin-bottom:10px;line-height:1.25;">❌ High Lead Cost</h3>
            <p style="font-size:12.5px;color:#9fb5a8;line-height:1.45;">ค่า Lead สูง แต่คุณภาพไม่สม่ำเสมอ</p>
          </div>
          <div class="card" style="height:120px;min-height:120px;padding:16px;">
            <h3 style="font-size:15px;min-height:auto;margin-bottom:10px;line-height:1.25;">❌ Weak Retargeting Structure</h3>
            <p style="font-size:12.5px;color:#9fb5a8;line-height:1.45;">ไม่มีระบบ Follow-up สำหรับคนที่สนใจบริการ</p>
          </div>
          <div class="card" style="height:120px;min-height:120px;padding:16px;">
            <h3 style="font-size:15px;min-height:auto;margin-bottom:10px;line-height:1.25;">❌ Creative Fatigue</h3>
            <p style="font-size:12.5px;color:#9fb5a8;line-height:1.45;">ยิงโปรเดิมซ้ำจน CTR ตก และ Frequency สูง</p>
          </div>
          <div class="card" style="height:120px;min-height:120px;padding:16px;">
            <h3 style="font-size:15px;min-height:auto;margin-bottom:10px;line-height:1.25;">❌ Poor Conversion Journey</h3>
            <p style="font-size:12.5px;color:#9fb5a8;line-height:1.45;">คนทักเยอะ แต่ไม่จองคิว</p>
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
