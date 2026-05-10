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
        """,
        unsafe_allow_html=True,
    )

    col1, col2 = st.columns(2)

    with col1:
        st.markdown(
            """
            <div class="card" style="height:150px;min-height:150px;padding:18px;">
              <h3 style="font-size:18px;min-height:auto;margin-bottom:10px;">❌ High Lead Cost</h3>
              <p style="font-size:14px;color:#9fb5a8;">ค่า Lead สูง แต่คุณภาพไม่สม่ำเสมอ</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.markdown(
            """
            <div class="card" style="height:150px;min-height:150px;padding:18px;">
              <h3 style="font-size:18px;min-height:auto;margin-bottom:10px;">❌ Creative Fatigue</h3>
              <p style="font-size:14px;color:#9fb5a8;">ยิงโปรเดิมซ้ำจน CTR ตก และ Frequency สูง</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col2:
        st.markdown(
            """
            <div class="card" style="height:150px;min-height:150px;padding:18px;">
              <h3 style="font-size:18px;min-height:auto;margin-bottom:10px;">❌ Weak Retargeting Structure</h3>
              <p style="font-size:14px;color:#9fb5a8;">ไม่มีระบบ Follow-up สำหรับคนที่สนใจบริการ</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.markdown(
            """
            <div class="card" style="height:150px;min-height:150px;padding:18px;">
              <h3 style="font-size:18px;min-height:auto;margin-bottom:10px;">❌ Poor Conversion Journey</h3>
              <p style="font-size:14px;color:#9fb5a8;">คนทักเยอะ แต่ไม่จองคิว</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
