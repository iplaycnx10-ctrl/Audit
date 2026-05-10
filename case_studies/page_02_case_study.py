import streamlit as st


def render():
    st.markdown(
        """
        <div class="section">
          <div class="num">02 Case Study</div>
          <div class="title">Case Studies — Performance Thinking in Action</div>
          <div class="body">
            พื้นที่นี้จะใช้เล่าเคสแบบมนุษย์อ่านง่าย: ปัญหา → สิ่งที่วิเคราะห์ → สิ่งที่ทำ → ผลลัพธ์ → KPI<br><br>
            ตอนนี้วางโครงไว้ก่อน เพื่อแยกข้อมูลเคสออกจากไฟล์หลัก เพราะรายละเอียดส่วนนี้จะเยอะและต้องขยายต่อได้โดยไม่กระทบหน้าอื่น
          </div>
          <div class="quote">
            เป้าหมายของหน้านี้ไม่ใช่โชว์ Dashboard ก่อน แต่คือทำให้คนอ่านเข้าใจว่าเราแก้ปัญหาธุรกิจด้วย Data, Funnel Logic และ Performance Strategy ยังไง
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    col1, col2 = st.columns(2)

    with col1:
        st.markdown(
            """
            <div class="card">
              <h3>Case Study Template</h3>
              <p><b>ปัญหา:</b> ลูกค้ามีงบโฆษณา แต่ไม่รู้ว่าเงินรั่วตรง Funnel ไหน</p>
              <p><b>สิ่งที่วิเคราะห์:</b> CTR, CPM, CPR, ROAS, Frequency, VC → ATC → IC → Purchase</p>
              <p><b>สิ่งที่ทำ:</b> แยก Cold / Warm / Retarget และวาง Action ตาม Funnel Stage</p>
              <p><b>ผลลัพธ์:</b> รอสรุปจากเคสจริงหรือข้อมูลจำลองที่เลือกใช้</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col2:
        st.markdown(
            """
            <div class="card">
              <h3>Next Content Plan</h3>
              <p>• Beauty / Clinic Funnel Audit</p>
              <p>• Retail Performance Dashboard</p>
              <p>• AI Ads Audit Workflow</p>
              <p>• Retargeting & Repeat Purchase System</p>
              <p>• Branding + Performance Diagnostic</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
