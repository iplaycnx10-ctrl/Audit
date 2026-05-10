import streamlit as st


def render():
    st.markdown(
        """
        <div style="display:grid;grid-template-columns:0.95fr 1.05fr;gap:28px;align-items:start;margin-top:10px;margin-bottom:18px;">
          <div style="padding:8px 2px 6px 2px;">
            <div class="num" style="margin-bottom:8px;">CASE 1</div>
            <div style="font-size:13px;color:#facc15;font-weight:900;margin-bottom:10px;line-height:1.45;">โจทย์: สร้าง Branding + หา Lead จริง</div>
            <div class="title" style="font-size:25px;margin-bottom:10px;">Medical บริษัทอสังหาริมทรัพย์</div>
            <div class="body" style="font-size:14px;line-height:1.65;color:#d7e8dd;max-width:500px;">
              <b>กิจการ:</b> Real Estate<br><br>
              <b>ปัญหาหลักที่ตรวจพบ</b>
            </div>
          </div>

          <div style="display:grid;grid-template-columns:repeat(2,1fr);gap:12px;">
            <div style="height:96px;min-height:96px;padding:12px 13px;border-radius:18px;border:1px solid rgba(239,68,68,.42);background:linear-gradient(135deg,rgba(127,29,29,.42),rgba(11,26,18,.55));box-sizing:border-box;overflow:hidden;">
              <div style="font-size:12px;font-weight:900;color:#fff;line-height:1.25;margin-bottom:13px;">❌ Branding Message Gap</div>
              <div style="font-size:10.8px;color:#ffd5d5;line-height:1.45;">แบรนด์ยังสื่อสารคุณค่าไม่ชัดพอ</div>
            </div>
            <div style="height:96px;min-height:96px;padding:12px 13px;border-radius:18px;border:1px solid rgba(249,115,22,.38);background:linear-gradient(135deg,rgba(154,52,18,.34),rgba(11,26,18,.55));box-sizing:border-box;overflow:hidden;">
              <div style="font-size:12px;font-weight:900;color:#fff;line-height:1.25;margin-bottom:13px;">❌ Weak Lead Intent</div>
              <div style="font-size:10.8px;color:#ffe1c7;line-height:1.45;">คนเห็นเยอะ แต่ยังไม่พร้อมทักจริง</div>
            </div>
            <div style="height:96px;min-height:96px;padding:12px 13px;border-radius:18px;border:1px solid rgba(245,158,11,.36);background:linear-gradient(135deg,rgba(146,64,14,.30),rgba(11,26,18,.55));box-sizing:border-box;overflow:hidden;">
              <div style="font-size:12px;font-weight:900;color:#fff;line-height:1.25;margin-bottom:13px;">❌ Trust Barrier</div>
              <div style="font-size:10.8px;color:#ffe9bd;line-height:1.45;">ลูกค้ายังต้องการความน่าเชื่อถือก่อนตัดสินใจ</div>
            </div>
            <div style="height:96px;min-height:96px;padding:12px 13px;border-radius:18px;border:1px solid rgba(234,179,8,.32);background:linear-gradient(135deg,rgba(113,63,18,.26),rgba(11,26,18,.55));box-sizing:border-box;overflow:hidden;">
              <div style="font-size:12px;font-weight:900;color:#fff;line-height:1.25;margin-bottom:13px;">❌ Conversion Gap</div>
              <div style="font-size:10.8px;color:#fff1bd;line-height:1.45;">Branding ยังไม่เชื่อมไปสู่ Lead Action ชัดเจน</div>
            </div>
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
