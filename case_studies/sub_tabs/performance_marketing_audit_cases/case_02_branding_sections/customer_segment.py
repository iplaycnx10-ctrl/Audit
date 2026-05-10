import streamlit as st


def _segment_card(card_no, title, subtitle, profile, need, decision, key_message, accent="#52ff9a"):
    st.markdown(
        f"""
        <div style="min-height:445px;height:445px;border-radius:22px;border:1px solid rgba(255,255,255,.10);background:linear-gradient(135deg,rgba(255,255,255,.045),rgba(255,255,255,.018));padding:22px 24px;box-sizing:border-box;box-shadow:0 14px 34px rgba(0,0,0,.10);overflow:hidden;">
          <div style="font-size:12px;color:{accent};font-weight:950;letter-spacing:.12em;text-transform:uppercase;margin-bottom:10px;">{card_no}</div>
          <div style="font-size:18px;color:#fff;font-weight:950;line-height:1.45;margin-bottom:6px;">{title}</div>
          <div style="font-size:13px;color:#9fb5a8;font-weight:850;margin-bottom:18px;">{subtitle}</div>

          <div style="font-size:13.5px;color:#d7e8dd;line-height:1.85;">
            <span style="color:#52ff9a;font-weight:950;letter-spacing:.06em;text-transform:uppercase;">Profile:</span><br>
            {profile}<br><br>
            <span style="color:#facc15;font-weight:950;letter-spacing:.06em;text-transform:uppercase;">Need:</span><br>
            {need}<br><br>
            <span style="color:#52ff9a;font-weight:950;letter-spacing:.06em;text-transform:uppercase;">Decision Factor:</span><br>
            {decision}<br><br>
            <span style="color:{accent};font-weight:950;letter-spacing:.06em;text-transform:uppercase;">Key Message:</span><br>
            <span style="color:#fff;font-weight:900;">{key_message}</span>
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_customer_segment():
    st.markdown(
        """
        <div style="margin-top:20px;text-align:center;margin-bottom:18px;">
          <div style="font-size:13px;font-weight:950;letter-spacing:.16em;text-transform:uppercase;color:#52ff9a;margin-bottom:10px;">Customer Segment</div>
          <div style="font-size:24px;color:#fff;font-weight:950;letter-spacing:-.4px;">แยกกลุ่มลูกค้าตามรูปแบบพื้นที่และแรงจูงใจในการเช่า</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    col1, col2 = st.columns(2, gap="large")

    with col1:
        _segment_card(
            "Card 1",
            "Commercial Building Tenant",
            "ผู้เช่าตึก / ตึกพาณิชย์",
            "เจ้าของธุรกิจ, SME, ร้านอาหารจริงจัง, ธุรกิจบริการ หรือร้านที่ต้องการขยายสาขา",
            "ต้องการทำเลที่คุ้มค่า มีโอกาสสร้างรายได้ และเหมาะกับการเติบโตระยะยาว",
            "ทำเล, ค่าเช่า, ความน่าเชื่อถือ, จำนวนคนผ่าน, ศักยภาพทำกำไร",
            "พื้นที่เช่าที่ไม่ใช่แค่ตึกว่าง แต่เป็นโอกาสในการขยายธุรกิจ",
            "#52ff9a",
        )

    with col2:
        _segment_card(
            "Card 2",
            "Retail & Event Space Tenant",
            "ร้านค้า / ร้านอาหาร / รถเข็น / บูธ / ลานกิจกรรม",
            "ร้านอาหารเล็ก, ร้านเครื่องดื่ม, รถเข็น, บูธขายของ, Pop-up Store หรือร้านค้าที่ต้องการเพิ่มจุดขาย",
            "ต้องการพื้นที่ขายที่เริ่มง่าย เห็นภาพชัด ค่าเช่าเข้าใจง่าย และเข้าถึงลูกค้าได้เร็ว",
            "คนเดิน, ค่าเช่า, ความง่ายในการจอง, ภาพพื้นที่, ความพร้อมในการเริ่มขาย",
            "พื้นที่พร้อมขาย สำหรับร้านค้าที่อยากเริ่มหรือเพิ่มจุดขายทันที",
            "#facc15",
        )

    st.markdown(
        """
        <div style="margin-top:22px;border-radius:22px;border:1px solid rgba(250,204,21,.20);background:linear-gradient(135deg,rgba(250,204,21,.055),rgba(255,255,255,.018));padding:22px 24px;box-sizing:border-box;box-shadow:0 14px 34px rgba(0,0,0,.10);">
          <div style="font-size:13px;font-weight:950;letter-spacing:.16em;text-transform:uppercase;color:#facc15;margin-bottom:12px;">Customer Segment Insight</div>
          <div style="font-size:14px;color:#d7e8dd;line-height:1.85;max-width:1000px;margin-bottom:14px;">
            ผู้เช่าแต่ละกลุ่มมีมูลค่าทางธุรกิจและรอบการตัดสินใจไม่เหมือนกัน กลุ่มเช่าตึกเป็นกลุ่ม High LTV ที่ต้องใช้เวลาในการสร้างความเชื่อมั่นและมองเห็นโอกาสทำกำไร ส่วนกลุ่มร้านค้า บูธ และลานกิจกรรมเป็นกลุ่ม Fast Lead ที่ช่วยสร้าง Cashflow ระหว่างทางและลดพื้นที่ว่าง
          </div>
          <div style="font-size:14px;color:#bfd1c5;line-height:1.85;max-width:1000px;">
            ดังนั้นการตลาดไม่ควรใช้ข้อความเดียวกันกับทุกกลุ่ม แต่ควรออกแบบ Message และ Funnel ตามบทบาทของผู้เช่าแต่ละประเภท เพื่อให้แคมเปญไม่ได้แค่สร้าง Lead แต่สร้าง Lead ที่สัมพันธ์กับรายได้จริงของธุรกิจ
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
