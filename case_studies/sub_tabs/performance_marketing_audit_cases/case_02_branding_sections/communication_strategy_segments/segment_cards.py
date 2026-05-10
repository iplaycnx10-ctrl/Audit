import streamlit as st


def render_segment_cards():
    st.markdown(
        """
        <div style="max-width:860px;margin:14px auto 0 auto;display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:14px;">
          <div style="padding:18px 20px;border-radius:18px;border:1px solid rgba(250,204,21,.20);background:rgba(250,204,21,.045);min-height:150px;">
            <div style="font-size:10px;letter-spacing:.18em;text-transform:uppercase;color:#facc15;font-weight:950;margin-bottom:10px;">
              Segment 01
            </div>
            <div style="font-size:17px;font-weight:950;color:#fff;line-height:1.35;margin-bottom:10px;">
              Motivation & Trust Segment
            </div>
            <div style="font-size:13.5px;line-height:1.65;color:#d7e8dd;">
              กลุ่มที่ต้องสร้างแรงจูงใจ / ความเชื่อมั่น / LTV ระยะยาว เช่น ผู้เช่าตึกหรือธุรกิจที่ต้องใช้ทำเลเป็นฐานเติบโต เหมาะกับ Message ที่เน้น Location, Business Potential และ Investment Confidence
            </div>
          </div>

          <div style="padding:18px 20px;border-radius:18px;border:1px solid rgba(82,255,154,.18);background:rgba(255,255,255,.028);min-height:150px;">
            <div style="font-size:10px;letter-spacing:.18em;text-transform:uppercase;color:#52ff9a;font-weight:950;margin-bottom:10px;">
              Segment 02
            </div>
            <div style="font-size:17px;font-weight:950;color:#fff;line-height:1.35;margin-bottom:10px;">
              Lead Capture Segment
            </div>
            <div style="font-size:13.5px;line-height:1.65;color:#d7e8dd;">
              กลุ่มที่เน้นสร้าง Lead / ปิดไว / หมุน Cashflow เช่น ร้านค้า บูธ รถเข็น Pop-up Store และลานกิจกรรม เหมาะกับ Message ที่ชัด กระตุ้นการติดต่อ และลด friction ในการตัดสินใจ
            </div>
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
