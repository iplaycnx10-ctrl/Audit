import streamlit as st


def _mini_block(label, text, label_color="#52ff9a"):
    st.markdown(
        f"""
        <div style="padding:13px 14px;border-radius:15px;background:rgba(255,255,255,.026);border:1px solid rgba(255,255,255,.08);margin-bottom:12px;">
          <div style="font-size:11px;color:{label_color};font-weight:950;letter-spacing:.10em;text-transform:uppercase;margin-bottom:7px;">{label}</div>
          <div style="font-size:13.5px;color:#d7e8dd;line-height:1.65;">{text}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def _key_message(text, color="#52ff9a"):
    st.markdown(
        f"""
        <div style="padding:14px 15px;border-radius:16px;background:rgba(82,255,154,.055);border:1px solid rgba(82,255,154,.16);">
          <div style="font-size:11px;color:{color};font-weight:950;letter-spacing:.10em;text-transform:uppercase;margin-bottom:7px;">Key Message</div>
          <div style="font-size:14px;color:#fff;line-height:1.65;font-weight:850;">{text}</div>
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
        with st.container(border=True):
            st.markdown("""
            <div style="font-size:12px;color:#52ff9a;font-weight:950;letter-spacing:.12em;text-transform:uppercase;margin-bottom:10px;">Card 1</div>
            <div style="font-size:18px;color:#fff;font-weight:950;line-height:1.45;margin-bottom:6px;">Commercial Building Tenant</div>
            <div style="font-size:13px;color:#9fb5a8;font-weight:850;margin-bottom:18px;">ผู้เช่าตึก / ตึกพาณิชย์</div>
            """, unsafe_allow_html=True)
            _mini_block("Profile", "เจ้าของธุรกิจ, SME, ร้านอาหารจริงจัง, ธุรกิจบริการ หรือร้านที่ต้องการขยายสาขา")
            _mini_block("Need", "ต้องการทำเลที่คุ้มค่า มีโอกาสสร้างรายได้ และเหมาะกับการเติบโตระยะยาว", "#facc15")
            _mini_block("Decision Factor", "ทำเล, ค่าเช่า, ความน่าเชื่อถือ, จำนวนคนผ่าน, ศักยภาพทำกำไร")
            _key_message("พื้นที่เช่าที่ไม่ใช่แค่ตึกว่าง แต่เป็นโอกาสในการขยายธุรกิจ")

    with col2:
        with st.container(border=True):
            st.markdown("""
            <div style="font-size:12px;color:#facc15;font-weight:950;letter-spacing:.12em;text-transform:uppercase;margin-bottom:10px;">Card 2</div>
            <div style="font-size:18px;color:#fff;font-weight:950;line-height:1.45;margin-bottom:6px;">Retail & Event Space Tenant</div>
            <div style="font-size:13px;color:#9fb5a8;font-weight:850;margin-bottom:18px;">ร้านค้า / ร้านอาหาร / รถเข็น / บูธ / ลานกิจกรรม</div>
            """, unsafe_allow_html=True)
            _mini_block("Profile", "ร้านอาหารเล็ก, ร้านเครื่องดื่ม, รถเข็น, บูธขายของ, Pop-up Store หรือร้านค้าที่ต้องการเพิ่มจุดขาย")
            _mini_block("Need", "ต้องการพื้นที่ขายที่เริ่มง่าย เห็นภาพชัด ค่าเช่าเข้าใจง่าย และเข้าถึงลูกค้าได้เร็ว", "#facc15")
            _mini_block("Decision Factor", "คนเดิน, ค่าเช่า, ความง่ายในการจอง, ภาพพื้นที่, ความพร้อมในการเริ่มขาย")
            _key_message("พื้นที่พร้อมขาย สำหรับร้านค้าที่อยากเริ่มหรือเพิ่มจุดขายทันที", "#facc15")
