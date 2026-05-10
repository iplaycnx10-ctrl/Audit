import streamlit as st


def render():
    file_id = "1aJZc22ss8ZUAsXy6Kv2o0tpRaDF7Z-PP"
    image_url = f"https://drive.google.com/thumbnail?id={file_id}&sz=w1600"

    st.markdown(
        """
        <div style="border-radius:22px;border:1px solid rgba(250,204,21,.22);background:linear-gradient(135deg,rgba(250,204,21,.055),rgba(255,255,255,.018));padding:22px 24px;margin:14px 0 24px 0;box-sizing:border-box;box-shadow:0 14px 34px rgba(0,0,0,.10);">
          <div style="font-size:13px;font-weight:950;letter-spacing:.16em;text-transform:uppercase;color:#facc15;margin-bottom:14px;">
            แนวทางแก้ไขเบื้องต้นและกลยุทธ์ที่จะปรับใช้
          </div>
          <div style="font-size:14px;color:#bfd1c5;line-height:1.75;">
            เตรียมพื้นที่สำหรับสรุปแนวทางแก้ไขเชิงกลยุทธ์ เช่น การปรับ Creative, การคัดกรอง Intent, การวาง Retargeting และการออกแบบ Funnel เพื่อเพิ่มคุณภาพของ Traffic ก่อนเข้าสู่ขั้นตอน Conversion
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
