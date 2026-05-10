import streamlit as st


def render_segment_cards():
    st.markdown(
        """
        <div style="max-width:860px;margin:14px auto 0 auto;">
          <div style="display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:14px;">
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

          <div style="width:1px;height:26px;background:linear-gradient(180deg,rgba(250,204,21,.70),rgba(250,204,21,.10));margin:0 0 0 calc(25% - 0.5px);"></div>

          <div style="max-width:415px;margin:0 auto 0 0;padding:16px;border-radius:18px;border:1px solid rgba(250,204,21,.18);background:rgba(250,204,21,.035);">
            <div style="font-size:10px;letter-spacing:.18em;text-transform:uppercase;color:#facc15;font-weight:950;margin-bottom:12px;">
              แนวทางการสื่อสาร
            </div>

            <div style="padding:14px 15px;border-radius:15px;background:rgba(255,255,255,.030);border:1px solid rgba(250,204,21,.13);margin-bottom:10px;">
              <div style="font-size:15px;font-weight:950;color:#fff;margin-bottom:8px;">1. Location-Based Business</div>
              <div style="font-size:13px;line-height:1.62;color:#d7e8dd;margin-bottom:8px;">
                ทำการตลาดแบบเน้น <b>“ทำเลสร้างโอกาส”</b> ให้ผู้เช่าเห็นว่าพื้นที่นี้ช่วยเพิ่มโอกาสเจอลูกค้าใหม่และสร้างยอดขายจากคนผ่านจริง
              </div>
              <div style="font-size:12.5px;line-height:1.55;color:#fef3c7;background:rgba(250,204,21,.075);padding:10px 11px;border-radius:12px;">
                ตัวอย่างสาร: “ทำเลพร้อมเปิดหน้าร้าน เหมาะกับธุรกิจที่ต้องการคนเห็นจริง เดินผ่านจริง และมีโอกาสเปลี่ยนเป็นยอดขายจริง”
              </div>
            </div>

            <div style="padding:14px 15px;border-radius:15px;background:rgba(255,255,255,.030);border:1px solid rgba(250,204,21,.13);">
              <div style="font-size:15px;font-weight:950;color:#fff;margin-bottom:8px;">2. Office / Online-Based Business</div>
              <div style="font-size:13px;line-height:1.62;color:#d7e8dd;margin-bottom:8px;">
                ทำการตลาดแบบเน้น <b>“ฐานธุรกิจที่น่าเชื่อถือ”</b> ให้ผู้เช่าเห็นว่าพื้นที่นี้ช่วยเสริมภาพลักษณ์ ความเป็นมืออาชีพ และรองรับการเติบโตของธุรกิจ
              </div>
              <div style="font-size:12.5px;line-height:1.55;color:#fef3c7;background:rgba(250,204,21,.075);padding:10px 11px;border-radius:12px;">
                ตัวอย่างสาร: “พื้นที่สำหรับออฟฟิศหรือฐานธุรกิจออนไลน์ ที่ช่วยให้ธุรกิจดูน่าเชื่อถือ เป็นระบบ และพร้อมเติบโตระยะยาว”
              </div>
            </div>
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
