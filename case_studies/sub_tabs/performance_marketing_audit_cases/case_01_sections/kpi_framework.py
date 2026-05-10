import streamlit as st


def render():
    file_id = "1aJZc22ss8ZUAsXy6Kv2o0tpRaDF7Z-PP"
    image_url = f"https://drive.google.com/thumbnail?id={file_id}&sz=w1600"

    st.markdown(
        """
        <div style="border-radius:22px;border:1px solid rgba(250,204,21,.22);background:linear-gradient(135deg,rgba(250,204,21,.055),rgba(255,255,255,.018));padding:22px 24px;margin:14px 0 24px 0;box-sizing:border-box;box-shadow:0 14px 34px rgba(0,0,0,.10);">
          <div style="font-size:13px;font-weight:950;letter-spacing:.16em;text-transform:uppercase;color:#facc15;margin-bottom:16px;">
            แนวทางแก้ไขเบื้องต้นและกลยุทธ์ที่จะปรับใช้
          </div>
          <div style="font-size:15px;color:#fff;font-weight:900;line-height:1.55;margin-bottom:10px;">
            ❌ High Lead Cost / Creative Fatigue / Poor Conversion Journey
          </div>
          <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:10px;margin-bottom:16px;">
            <div style="font-size:12.5px;color:#ffd5d5;line-height:1.55;padding:10px 12px;border-radius:14px;border:1px solid rgba(239,68,68,.22);background:rgba(239,68,68,.055);">
              <b style="color:#fff;">High Lead Cost</b><br>ค่า Lead สูง และคุณภาพ Lead ไม่สม่ำเสมอ
            </div>
            <div style="font-size:12.5px;color:#ffe9bd;line-height:1.55;padding:10px 12px;border-radius:14px;border:1px solid rgba(245,158,11,.22);background:rgba(245,158,11,.055);">
              <b style="color:#fff;">Creative Fatigue</b><br>ยิงโปรเดิมซ้ำจน CTR ตก และ Frequency สูง
            </div>
            <div style="font-size:12.5px;color:#fff1bd;line-height:1.55;padding:10px 12px;border-radius:14px;border:1px solid rgba(234,179,8,.22);background:rgba(234,179,8,.055);">
              <b style="color:#fff;">Poor Conversion Journey</b><br>คนทักเยอะ แต่ไม่จองคิว
            </div>
          </div>
          <div style="font-size:13px;color:#52ff9a;font-weight:950;letter-spacing:.08em;text-transform:uppercase;margin:16px 0 8px 0;">
            ✅ แนวทางกลยุทธ์
          </div>
          <div style="font-size:14px;color:#d7e8dd;line-height:1.8;margin-bottom:14px;">
            ปรับจากการยิงโฆษณาแบบกว้าง ไปสู่การคัดกรองกลุ่มเป้าหมายที่มี Intent สูงตั้งแต่ต้นทาง โดยใช้ Creative และ Message ที่เจาะ Pain Point ชัดเจน เช่น ปัญหาริ้วรอย กรอบหน้า หรือความกังวลเรื่องผลลัพธ์ เพื่อแยกคนที่ “แค่เห็นโฆษณา” ออกจากคนที่ “มีแนวโน้มใช้บริการจริง”
          </div>
          <div style="font-size:13px;color:#facc15;font-weight:950;letter-spacing:.08em;text-transform:uppercase;margin:16px 0 8px 0;">
            🎯 เป้าหมาย
          </div>
          <div style="font-size:14px;color:#bfd1c5;line-height:1.75;">
            ลด Reach ที่ไม่มีคุณภาพ ลดต้นทุนต่อ Lead และเพิ่มโอกาสได้ Lead ที่มีแนวโน้มจองจริงมากขึ้น.
          </div>
        </div>

        <div style="font-size:13px;font-weight:950;letter-spacing:.16em;text-transform:uppercase;color:#facc15;margin:0 0 14px 0;">
          Creative ที่แนะนำ
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        f"""
        <div style="border-radius:22px;border:1px solid rgba(250,204,21,.22);background:linear-gradient(135deg,rgba(255,255,255,.045),rgba(255,255,255,.018));padding:18px;box-sizing:border-box;box-shadow:0 14px 34px rgba(0,0,0,.10);">
          <img src="{image_url}" style="width:100%;border-radius:18px;display:block;object-fit:cover;">
        </div>
        """,
        unsafe_allow_html=True,
    )
