import streamlit as st


def render_communication_strategy():
    st.markdown(
        """
        <div class="section" style="margin-top:18px;">
          <div class="num">Communication Strategy</div>
          <div class="title">แนวทางการทำการตลาด</div>
          <div class="body" style="max-width:920px;">
            การทำการตลาดสำหรับพื้นที่เช่าไม่ควรมองผู้เช่าทุกกลุ่มเป็นกลุ่มเดียวกัน เพราะแต่ละกลุ่มมีมูลค่าทางธุรกิจ เหตุผลในการตัดสินใจ และระยะเวลาปิดการขายไม่เหมือนกัน
          </div>
        </div>

        <div style="display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:16px;margin-top:16px;">
          <div class="card" style="height:auto;min-height:260px;">
            <h3>01 — Long-term Tenant Segment</h3>
            <p>
              กลุ่มเช่าตึก / ตึกพาณิชย์ เป็นกลุ่มที่มีมูลค่าระยะยาวสูงกว่า แต่ต้องใช้เวลาในการสร้างความเชื่อมั่นมากกว่า การสื่อสารจึงไม่ควรเป็นเพียงการลงรูปพื้นที่ว่าง แต่ควรนำเสนอให้เห็นว่า <b>“ทำเลนี้เหมาะกับธุรกิจของเขาอย่างไร”</b> เช่น โอกาสจาก Location ความคุ้มค่าระยะยาว และศักยภาพในการสร้างรายได้
            </p>
          </div>

          <div class="card" style="height:auto;min-height:260px;">
            <h3>02 — Commercial Building Message Split</h3>
            <p>
              ในกลุ่มตึกพาณิชย์เองยังสามารถแยกมุมสื่อสารได้อีก 2 แบบ คือ <b>ธุรกิจที่ต้องการหน้าร้าน</b> ซึ่งควรเน้นทำเล คนผ่าน และโอกาสจากพื้นที่จริง กับ <b>ธุรกิจที่ใช้ตึกเป็นออฟฟิศหรือฐานออนไลน์</b> ซึ่งควรเน้นภาพลักษณ์ ความสะดวก ความคุ้มค่า และการรองรับการเติบโต
            </p>
          </div>

          <div class="card" style="height:auto;min-height:260px;">
            <h3>03 — Cashflow Support Segment</h3>
            <p>
              ขณะเดียวกัน ยังมีกลุ่มร้านค้า บูธ รถเข็น Pop-up Store และลานกิจกรรม ซึ่งทำหน้าที่เป็น <b>Cashflow Support Segment</b> ช่วยสร้างรายได้ระหว่างทาง ลดพื้นที่ว่าง และทำให้พื้นที่มีความเคลื่อนไหวระหว่างรอผู้เช่ารายใหญ่
            </p>
          </div>

          <div class="card" style="height:auto;min-height:260px;">
            <h3>04 — Media Buying Direction</h3>
            <p>
              ดังนั้นแนวทางการซื้อสื่อควรทำมากกว่าการประกาศว่า <b>“มีพื้นที่ให้เช่า”</b> แต่ควรออกแบบ Message ให้ตรงกับบทบาทของผู้เช่าแต่ละกลุ่ม ทั้งกลุ่มที่สร้าง LTV ระยะยาว และกลุ่มที่ช่วยเติม Cashflow ระหว่างทาง
            </p>
          </div>
        </div>

        <div class="quote" style="margin-top:18px;">
          Core Idea: ไม่ได้ขายแค่พื้นที่ว่าง แต่ต้องสื่อสารว่า “พื้นที่นี้ช่วยให้ธุรกิจของผู้เช่าเติบโตได้อย่างไร”
        </div>
        """,
        unsafe_allow_html=True,
    )
