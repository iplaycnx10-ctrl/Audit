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

        <div style="display:grid;grid-template-columns:repeat(4,1fr);gap:18px;margin-top:14px;margin-bottom:22px;">
          <div style="height:112px;min-height:112px;padding:14px 15px;border-radius:20px;border:1px solid rgba(239,68,68,.42);background:linear-gradient(135deg,rgba(127,29,29,.42),rgba(11,26,18,.55));box-sizing:border-box;overflow:hidden;">
            <div style="font-size:13px;font-weight:900;color:#fff;line-height:1.3;margin-bottom:18px;">❌ High Lead Cost</div>
            <div style="font-size:11.5px;color:#ffd5d5;line-height:1.55;">ค่า Lead สูง แต่คุณภาพไม่สม่ำเสมอ</div>
          </div>
          <div style="height:112px;min-height:112px;padding:14px 15px;border-radius:20px;border:1px solid rgba(249,115,22,.38);background:linear-gradient(135deg,rgba(154,52,18,.34),rgba(11,26,18,.55));box-sizing:border-box;overflow:hidden;">
            <div style="font-size:13px;font-weight:900;color:#fff;line-height:1.3;margin-bottom:18px;">❌ Weak Retargeting Structure</div>
            <div style="font-size:11.5px;color:#ffe1c7;line-height:1.55;">ไม่มีระบบ Follow-up สำหรับคนที่สนใจบริการ</div>
          </div>
          <div style="height:112px;min-height:112px;padding:14px 15px;border-radius:20px;border:1px solid rgba(245,158,11,.36);background:linear-gradient(135deg,rgba(146,64,14,.30),rgba(11,26,18,.55));box-sizing:border-box;overflow:hidden;">
            <div style="font-size:13px;font-weight:900;color:#fff;line-height:1.3;margin-bottom:18px;">❌ Creative Fatigue</div>
            <div style="font-size:11.5px;color:#ffe9bd;line-height:1.55;">ยิงโปรเดิมซ้ำจน CTR ตก และ Frequency สูง</div>
          </div>
          <div style="height:112px;min-height:112px;padding:14px 15px;border-radius:20px;border:1px solid rgba(234,179,8,.32);background:linear-gradient(135deg,rgba(113,63,18,.26),rgba(11,26,18,.55));box-sizing:border-box;overflow:hidden;">
            <div style="font-size:13px;font-weight:900;color:#fff;line-height:1.3;margin-bottom:18px;">❌ Poor Conversion Journey</div>
            <div style="font-size:11.5px;color:#fff1bd;line-height:1.55;">คนทักเยอะ แต่ไม่จองคิว</div>
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
