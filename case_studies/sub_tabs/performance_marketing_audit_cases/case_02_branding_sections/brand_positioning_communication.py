import streamlit as st


def render_brand_positioning_communication():
    st.markdown(
        """
        <div style="margin-top:26px;text-align:center;">
          <div style="font-size:13px;font-weight:950;letter-spacing:.16em;text-transform:uppercase;color:#52ff9a;margin-bottom:10px;">
            Brand Positioning & Communication
          </div>
          <div style="font-size:28px;color:#fff;font-weight:950;letter-spacing:-.5px;margin-bottom:18px;">
            Business Ecosystem
          </div>
        </div>

        <div style="display:grid;grid-template-columns:repeat(4,1fr);gap:14px;margin-top:12px;margin-bottom:22px;">
          <div style="min-height:160px;border-radius:20px;border:1px solid rgba(82,255,154,.20);background:linear-gradient(135deg,rgba(82,255,154,.06),rgba(255,255,255,.018));padding:18px 18px;box-sizing:border-box;box-shadow:0 14px 34px rgba(0,0,0,.10);">
            <div style="font-size:12px;color:#52ff9a;font-weight:950;letter-spacing:.12em;text-transform:uppercase;margin-bottom:12px;">01 — Business & Lifestyle Ecosystem</div>
            <div style="font-size:14px;color:#d7e8dd;line-height:1.75;">ที่ช่วยเพิ่มโอกาสทางธุรกิจ</div>
          </div>

          <div style="min-height:160px;border-radius:20px;border:1px solid rgba(250,204,21,.20);background:linear-gradient(135deg,rgba(250,204,21,.06),rgba(255,255,255,.018));padding:18px 18px;box-sizing:border-box;box-shadow:0 14px 34px rgba(0,0,0,.10);">
            <div style="font-size:12px;color:#facc15;font-weight:950;letter-spacing:.12em;text-transform:uppercase;margin-bottom:12px;">02 — Investment Mindset</div>
            <div style="font-size:14px;color:#d7e8dd;line-height:1.75;">การเข้ามาอยู่ที่นี่<br>คือการลงทุน ไม่ใช่ค่าใช้จ่าย</div>
          </div>

          <div style="min-height:160px;border-radius:20px;border:1px solid rgba(82,255,154,.20);background:linear-gradient(135deg,rgba(82,255,154,.055),rgba(255,255,255,.018));padding:18px 18px;box-sizing:border-box;box-shadow:0 14px 34px rgba(0,0,0,.10);">
            <div style="font-size:12px;color:#52ff9a;font-weight:950;letter-spacing:.12em;text-transform:uppercase;margin-bottom:12px;">03 — Long-Term Value</div>
            <div style="font-size:14px;color:#d7e8dd;line-height:1.75;">พื้นที่ที่สร้างมูลค่าระยะยาว<br>ให้กับธุรกิจและผู้ลงทุน</div>
          </div>

          <div style="min-height:160px;border-radius:20px;border:1px solid rgba(250,204,21,.20);background:linear-gradient(135deg,rgba(250,204,21,.06),rgba(255,255,255,.018));padding:18px 18px;box-sizing:border-box;box-shadow:0 14px 34px rgba(0,0,0,.10);">
            <div style="font-size:12px;color:#facc15;font-weight:950;letter-spacing:.12em;text-transform:uppercase;margin-bottom:12px;">04 — Growth Opportunity</div>
            <div style="font-size:14px;color:#d7e8dd;line-height:1.75;">โอกาสในการเติบโต<br>และสร้างกำไรในอนาคต 🔥</div>
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
