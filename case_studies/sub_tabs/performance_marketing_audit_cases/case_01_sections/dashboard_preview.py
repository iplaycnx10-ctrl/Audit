import streamlit as st


def render():
    st.markdown(
        """
        <div style="border-radius:22px;border:1px solid rgba(250,204,21,.22);background:linear-gradient(135deg,rgba(250,204,21,.055),rgba(255,255,255,.018));padding:24px 26px;margin:14px 0 22px 0;box-sizing:border-box;box-shadow:0 14px 34px rgba(0,0,0,.10);">
          <div style="font-size:13px;font-weight:950;letter-spacing:.16em;text-transform:uppercase;color:#facc15;margin-bottom:12px;">
            ระยะวัดผลหลังปรับกลยุทธ์
          </div>
          <div style="font-size:14.5px;color:#d7e8dd;line-height:1.75;max-width:920px;">
            หลังจากปรับแคมเปญด้วย Intent Filtering Creative, Low-Ticket Booking Offer และ LINE CRM Capture ขั้นตอนถัดไปคือการวัดผลว่าแนวทางที่ใช้ช่วยให้ Traffic และ Lead มีคุณภาพขึ้นจริงหรือไม่
          </div>
        </div>

        <div style="font-size:13px;font-weight:950;letter-spacing:.16em;text-transform:uppercase;color:#52ff9a;margin:22px 0 12px 0;">
          การวัดผลและกำหนด KPI
        </div>

        <div style="border-radius:22px;border:1px solid rgba(82,255,154,.18);background:linear-gradient(135deg,rgba(255,255,255,.045),rgba(255,255,255,.018));padding:22px 24px;margin:0 0 22px 0;box-sizing:border-box;box-shadow:0 14px 34px rgba(0,0,0,.10);">
          <div style="font-size:15px;color:#fff;font-weight:950;margin-bottom:14px;">
            1. Traffic Quality Check
          </div>
          <div style="font-size:14px;color:#d7e8dd;line-height:1.8;margin-bottom:16px;">
            หลังจากเปลี่ยน CI / Creative ใหม่ จะวัดผลจากความสามารถในการเปลี่ยน “คนคลิก” ให้กลายเป็น “Action ที่มี Intent จริง” เช่น แอด LINE, ทักถามรายละเอียด, กดจอง หรือจ่ายมัดจำ
          </div>

          <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:12px;margin-bottom:16px;">
            <div style="padding:14px 16px;border-radius:16px;border:1px solid rgba(82,255,154,.16);background:rgba(82,255,154,.04);">
              <div style="font-size:12px;color:#52ff9a;font-weight:950;letter-spacing:.10em;text-transform:uppercase;margin-bottom:8px;">KPI หลัก</div>
              <div style="font-size:13.5px;color:#d7e8dd;line-height:1.65;">Intent Action Rate<br><span style="color:#9fb5a8;">สัดส่วนของคนที่คลิกแล้วเกิด Action ต่อ</span></div>
            </div>
            <div style="padding:14px 16px;border-radius:16px;border:1px solid rgba(250,204,21,.18);background:rgba(250,204,21,.045);">
              <div style="font-size:12px;color:#facc15;font-weight:950;letter-spacing:.10em;text-transform:uppercase;margin-bottom:8px;">เกณฑ์ตัดสิน</div>
              <div style="font-size:13.5px;color:#d7e8dd;line-height:1.65;">7–14 วัน<br><span style="color:#9fb5a8;">ต้องเพิ่มขึ้นอย่างน้อย 20–30% จากค่าเดิม</span></div>
            </div>
            <div style="padding:14px 16px;border-radius:16px;border:1px solid rgba(239,68,68,.18);background:rgba(239,68,68,.045);">
              <div style="font-size:12px;color:#ffb4b4;font-weight:950;letter-spacing:.10em;text-transform:uppercase;margin-bottom:8px;">Action ถ้าไม่ผ่าน</div>
              <div style="font-size:13.5px;color:#d7e8dd;line-height:1.65;">เปลี่ยน Creative Angle ใหม่<br><span style="color:#9fb5a8;">CI / Message / Hook ยังไม่สามารถคัด Intent ได้ดีพอ</span></div>
            </div>
          </div>

          <div style="font-size:13px;color:#facc15;font-weight:950;letter-spacing:.08em;text-transform:uppercase;margin:16px 0 8px 0;">
            🎯 เป้าหมาย
          </div>
          <div style="font-size:14px;color:#bfd1c5;line-height:1.75;">
            เพิ่มคุณภาพ Traffic ไม่ใช่แค่เพิ่มจำนวนคลิก โดยต้องทำให้คนที่เข้ามามีแนวโน้มกลายเป็น Lead หรือ Booking มากขึ้นจริง.
          </div>
        </div>

        <div style="border-radius:22px;border:1px solid rgba(82,255,154,.18);background:linear-gradient(135deg,rgba(255,255,255,.045),rgba(255,255,255,.018));padding:22px 24px;margin:0 0 22px 0;box-sizing:border-box;box-shadow:0 14px 34px rgba(0,0,0,.10);">
          <div style="font-size:15px;color:#fff;font-weight:950;margin-bottom:14px;">
            2. Lead Intent Check
          </div>
          <div style="font-size:14px;color:#d7e8dd;line-height:1.8;margin-bottom:16px;">
            หลังจากปรับข้อเสนอและเส้นทางให้ลูกค้าเข้าสู่ LINE / Booking จะวัดผลจากคุณภาพของ Lead ว่าเป็นคนที่มีความตั้งใจจริงมากขึ้นหรือไม่ ไม่ใช่วัดแค่จำนวน Lead ที่เข้ามา
          </div>

          <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:12px;margin-bottom:16px;">
            <div style="padding:14px 16px;border-radius:16px;border:1px solid rgba(82,255,154,.16);background:rgba(82,255,154,.04);">
              <div style="font-size:12px;color:#52ff9a;font-weight:950;letter-spacing:.10em;text-transform:uppercase;margin-bottom:8px;">KPI หลัก</div>
              <div style="font-size:13.5px;color:#d7e8dd;line-height:1.65;">Lead-to-Intent Action Rate<br><span style="color:#9fb5a8;">สัดส่วนของ Lead ที่เกิด Action ต่อ เช่น แอด LINE, ถามรายละเอียดจริง, กดจอง หรือจ่ายมัดจำ</span></div>
            </div>
            <div style="padding:14px 16px;border-radius:16px;border:1px solid rgba(250,204,21,.18);background:rgba(250,204,21,.045);">
              <div style="font-size:12px;color:#facc15;font-weight:950;letter-spacing:.10em;text-transform:uppercase;margin-bottom:8px;">เกณฑ์ตัดสิน</div>
              <div style="font-size:13.5px;color:#d7e8dd;line-height:1.65;">7–14 วัน<br><span style="color:#9fb5a8;">ต้องเพิ่มขึ้นอย่างน้อย 20–30% จากค่าเดิม</span></div>
            </div>
            <div style="padding:14px 16px;border-radius:16px;border:1px solid rgba(239,68,68,.18);background:rgba(239,68,68,.045);">
              <div style="font-size:12px;color:#ffb4b4;font-weight:950;letter-spacing:.10em;text-transform:uppercase;margin-bottom:8px;">Action ถ้าไม่ผ่าน</div>
              <div style="font-size:13.5px;color:#d7e8dd;line-height:1.65;">ปรับ Offer / Message / Lead Flow ใหม่<br><span style="color:#9fb5a8;">ยังไม่สามารถคัดกรอง Lead คุณภาพได้ดีพอ</span></div>
            </div>
          </div>

          <div style="font-size:13px;color:#facc15;font-weight:950;letter-spacing:.08em;text-transform:uppercase;margin:16px 0 8px 0;">
            🎯 เป้าหมาย
          </div>
          <div style="font-size:14px;color:#bfd1c5;line-height:1.75;">
            ลด Lead ที่เข้ามาแบบไม่มีความต้องการจริง และเพิ่มสัดส่วน Lead ที่มีแนวโน้มจอง ใช้บริการ หรือเข้าสู่ระบบ CRM เพื่อติดตามต่อได้จริง.
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
