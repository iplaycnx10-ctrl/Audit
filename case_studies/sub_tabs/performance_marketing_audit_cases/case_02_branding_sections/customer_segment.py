import streamlit as st


def render_customer_segment():
    st.markdown(
        """
        <div style="margin-top:20px;text-align:center;margin-bottom:18px;">
          <div style="font-size:13px;font-weight:950;letter-spacing:.16em;text-transform:uppercase;color:#52ff9a;margin-bottom:10px;">
            Customer Segment
          </div>
          <div style="font-size:24px;color:#fff;font-weight:950;letter-spacing:-.4px;">
            แยกกลุ่มลูกค้าตามรูปแบบพื้นที่และแรงจูงใจในการเช่า
          </div>
        </div>

        <div style="display:grid;grid-template-columns:repeat(2,1fr);gap:16px;margin-top:18px;margin-bottom:22px;">
          <div style="border-radius:22px;border:1px solid rgba(82,255,154,.20);background:linear-gradient(135deg,rgba(82,255,154,.055),rgba(255,255,255,.018));padding:22px 24px;box-sizing:border-box;box-shadow:0 14px 34px rgba(0,0,0,.10);">
            <div style="font-size:12px;color:#52ff9a;font-weight:950;letter-spacing:.12em;text-transform:uppercase;margin-bottom:10px;">Card 1</div>
            <div style="font-size:18px;color:#fff;font-weight:950;line-height:1.45;margin-bottom:6px;">Commercial Building Tenant</div>
            <div style="font-size:13px;color:#9fb5a8;font-weight:850;margin-bottom:18px;">ผู้เช่าตึก / ตึกพาณิชย์</div>

            <div style="display:grid;gap:12px;">
              <div style="padding:13px 14px;border-radius:15px;background:rgba(255,255,255,.026);border:1px solid rgba(255,255,255,.08);">
                <div style="font-size:11px;color:#52ff9a;font-weight:950;letter-spacing:.10em;text-transform:uppercase;margin-bottom:7px;">Profile</div>
                <div style="font-size:13.5px;color:#d7e8dd;line-height:1.65;">เจ้าของธุรกิจ, SME, ร้านอาหารจริงจัง, ธุรกิจบริการ หรือร้านที่ต้องการขยายสาขา</div>
              </div>
              <div style="padding:13px 14px;border-radius:15px;background:rgba(255,255,255,.026);border:1px solid rgba(255,255,255,.08);">
                <div style="font-size:11px;color:#facc15;font-weight:950;letter-spacing:.10em;text-transform:uppercase;margin-bottom:7px;">Need</div>
                <div style="font-size:13.5px;color:#d7e8dd;line-height:1.65;">ต้องการทำเลที่คุ้มค่า มีโอกาสสร้างรายได้ และเหมาะกับการเติบโตระยะยาว</div>
              </div>
              <div style="padding:13px 14px;border-radius:15px;background:rgba(255,255,255,.026);border:1px solid rgba(255,255,255,.08);">
                <div style="font-size:11px;color:#52ff9a;font-weight:950;letter-spacing:.10em;text-transform:uppercase;margin-bottom:7px;">Decision Factor</div>
                <div style="font-size:13.5px;color:#d7e8dd;line-height:1.65;">ทำเล, ค่าเช่า, ความน่าเชื่อถือ, จำนวนคนผ่าน, ศักยภาพทำกำไร</div>
              </div>
              <div style="padding:14px 15px;border-radius:16px;background:rgba(82,255,154,.055);border:1px solid rgba(82,255,154,.16);">
                <div style="font-size:11px;color:#52ff9a;font-weight:950;letter-spacing:.10em;text-transform:uppercase;margin-bottom:7px;">Key Message</div>
                <div style="font-size:14px;color:#fff;line-height:1.65;font-weight:850;">พื้นที่เช่าที่ไม่ใช่แค่ตึกว่าง แต่เป็นโอกาสในการขยายธุรกิจ</div>
              </div>
            </div>
          </div>

          <div style="border-radius:22px;border:1px solid rgba(250,204,21,.20);background:linear-gradient(135deg,rgba(250,204,21,.055),rgba(255,255,255,.018));padding:22px 24px;box-sizing:border-box;box-shadow:0 14px 34px rgba(0,0,0,.10);">
            <div style="font-size:12px;color:#facc15;font-weight:950;letter-spacing:.12em;text-transform:uppercase;margin-bottom:10px;">Card 2</div>
            <div style="font-size:18px;color:#fff;font-weight:950;line-height:1.45;margin-bottom:6px;">Retail & Event Space Tenant</div>
            <div style="font-size:13px;color:#9fb5a8;font-weight:850;margin-bottom:18px;">ร้านค้า / ร้านอาหาร / รถเข็น / บูธ / ลานกิจกรรม</div>

            <div style="display:grid;gap:12px;">
              <div style="padding:13px 14px;border-radius:15px;background:rgba(255,255,255,.026);border:1px solid rgba(255,255,255,.08);">
                <div style="font-size:11px;color:#52ff9a;font-weight:950;letter-spacing:.10em;text-transform:uppercase;margin-bottom:7px;">Profile</div>
                <div style="font-size:13.5px;color:#d7e8dd;line-height:1.65;">ร้านอาหารเล็ก, ร้านเครื่องดื่ม, รถเข็น, บูธขายของ, Pop-up Store หรือร้านค้าที่ต้องการเพิ่มจุดขาย</div>
              </div>
              <div style="padding:13px 14px;border-radius:15px;background:rgba(255,255,255,.026);border:1px solid rgba(255,255,255,.08);">
                <div style="font-size:11px;color:#facc15;font-weight:950;letter-spacing:.10em;text-transform:uppercase;margin-bottom:7px;">Need</div>
                <div style="font-size:13.5px;color:#d7e8dd;line-height:1.65;">ต้องการพื้นที่ขายที่เริ่มง่าย เห็นภาพชัด ค่าเช่าเข้าใจง่าย และเข้าถึงลูกค้าได้เร็ว</div>
              </div>
              <div style="padding:13px 14px;border-radius:15px;background:rgba(255,255,255,.026);border:1px solid rgba(255,255,255,.08);">
                <div style="font-size:11px;color:#52ff9a;font-weight:950;letter-spacing:.10em;text-transform:uppercase;margin-bottom:7px;">Decision Factor</div>
                <div style="font-size:13.5px;color:#d7e8dd;line-height:1.65;">คนเดิน, ค่าเช่า, ความง่ายในการจอง, ภาพพื้นที่, ความพร้อมในการเริ่มขาย</div>
              </div>
              <div style="padding:14px 15px;border-radius:16px;background:rgba(250,204,21,.055);border:1px solid rgba(250,204,21,.16);">
                <div style="font-size:11px;color:#facc15;font-weight:950;letter-spacing:.10em;text-transform:uppercase;margin-bottom:7px;">Key Message</div>
                <div style="font-size:14px;color:#fff;line-height:1.65;font-weight:850;">พื้นที่พร้อมขาย สำหรับร้านค้าที่อยากเริ่มหรือเพิ่มจุดขายทันที</div>
              </div>
            </div>
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
