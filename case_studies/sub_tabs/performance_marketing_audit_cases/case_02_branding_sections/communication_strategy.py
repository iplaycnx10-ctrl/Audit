import streamlit as st


def render_communication_strategy():
    st.markdown(
        """
        <div class="section" style="margin-top:18px;">
          <div class="num">Communication Strategy</div>
          <div class="title">Customer Segment & Communication Insight</div>

          <div class="card" style="height:auto;min-height:auto;margin-top:18px;padding:26px;">
            <h3 style="min-height:auto;margin-bottom:16px;">แนวทางการทำการตลาดสำหรับพื้นที่เช่า</h3>
            <p style="font-size:15.5px;line-height:1.85;color:#d7e8dd;margin-bottom:14px;">
              การทำการตลาดสำหรับพื้นที่เช่าไม่ควรมองผู้เช่าทุกกลุ่มเป็นกลุ่มเดียวกัน เพราะแต่ละกลุ่มมีมูลค่าทางธุรกิจ เหตุผลในการตัดสินใจ และระยะเวลาปิดการขายไม่เหมือนกัน
            </p>
            <p style="font-size:15.5px;line-height:1.85;color:#d7e8dd;margin-bottom:14px;">
              กลุ่มเช่าตึก / ตึกพาณิชย์ เป็นกลุ่มที่มีมูลค่าระยะยาวสูงกว่า แต่ต้องใช้เวลาในการสร้างความเชื่อมั่นมากกว่า การสื่อสารจึงไม่ควรเป็นเพียงการลงรูปพื้นที่ว่าง แต่ควรนำเสนอให้เห็นว่า <b>“ทำเลนี้เหมาะกับธุรกิจของเขาอย่างไร”</b> เช่น โอกาสจาก Location ความคุ้มค่าระยะยาว และศักยภาพในการสร้างรายได้
            </p>
            <p style="font-size:15.5px;line-height:1.85;color:#d7e8dd;margin-bottom:14px;">
              ในกลุ่มตึกพาณิชย์เองยังสามารถแยกมุมสื่อสารได้อีก 2 แบบ คือ <b>ธุรกิจที่ต้องการหน้าร้าน</b> ซึ่งควรเน้นทำเล คนผ่าน และโอกาสจากพื้นที่จริง กับ <b>ธุรกิจที่ใช้ตึกเป็นออฟฟิศหรือฐานออนไลน์</b> ซึ่งควรเน้นภาพลักษณ์ ความสะดวก ความคุ้มค่า และการรองรับการเติบโต
            </p>
            <p style="font-size:15.5px;line-height:1.85;color:#d7e8dd;margin-bottom:14px;">
              ขณะเดียวกัน ยังมีกลุ่มร้านค้า บูธ รถเข็น Pop-up Store และลานกิจกรรม ซึ่งทำหน้าที่เป็น <b>Cashflow Support Segment</b> ช่วยสร้างรายได้ระหว่างทาง ลดพื้นที่ว่าง และทำให้พื้นที่มีความเคลื่อนไหวระหว่างรอผู้เช่ารายใหญ่
            </p>
            <p style="font-size:15.5px;line-height:1.85;color:#d7e8dd;margin:0;">
              ดังนั้นแนวทางการซื้อสื่อควรทำมากกว่าการประกาศว่า <b>“มีพื้นที่ให้เช่า”</b> แต่ควรออกแบบ Message ให้ตรงกับบทบาทของผู้เช่าแต่ละกลุ่ม ทั้งกลุ่มที่สร้าง LTV ระยะยาว และกลุ่มที่ช่วยเติม Cashflow ระหว่างทาง
            </p>
          </div>

          <div class="quote" style="margin-top:18px;">
            Core Idea: ไม่ได้ขายแค่พื้นที่ว่าง แต่ต้องสื่อสารว่า “พื้นที่นี้ช่วยให้ธุรกิจของผู้เช่าเติบโตได้อย่างไร”
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
