import streamlit as st
from portfolio_assets import add_asset, clear_assets, load_assets


def render_gallery_form():
    with st.expander("เพิ่มรูปผลงานจาก Google Drive", expanded=False):
        title = st.text_input("ชื่อผลงาน", placeholder="เช่น TikTok Video Performance / Live Stream Clip / Creative Showcase")
        url = st.text_input("Google Drive image link", placeholder="วางลิงก์รูปจาก Google Drive")
        note = st.text_area("คำอธิบายสั้น ๆ", placeholder="อธิบายผลงานนี้สั้น ๆ ว่าโชว์อะไร", height=90)

        c1, c2 = st.columns([1, 1])
        with c1:
            if st.button("Save to Portfolio Gallery", use_container_width=True):
                if not url.strip():
                    st.warning("ใส่ลิงก์ Google Drive ก่อนนะ")
                else:
                    add_asset(title, url, note)
                    st.success("บันทึกผลงานเข้า Gallery แล้ว")
                    st.rerun()

        with c2:
            if st.button("Clear Gallery", use_container_width=True):
                clear_assets()
                st.warning("ล้าง Gallery แล้ว")
                st.rerun()


def render_gallery_grid():
    assets = load_assets()

    if not assets:
        st.markdown(
            """
            <div class='quote'>
                ยังไม่มีรูปผลงานใน Gallery — อัปโหลดรูปไว้ใน Google Drive แล้วนำลิงก์มาวางที่ฟอร์มด้านบน ระบบจะบันทึกไว้ในไฟล์ JSON และแสดงผลซ้ำได้ทุกครั้งที่เปิดเว็บ
            </div>
            """,
            unsafe_allow_html=True,
        )
        return

    cols = st.columns(3)
    for index, asset in enumerate(assets):
        with cols[index % 3]:
            st.markdown(
                f"""
                <div class='card' style='height:auto;min-height:360px;margin-bottom:18px;'>
                    <h3>{asset.get('title', 'Portfolio Asset')}</h3>
                    <img src='{asset.get('url', '')}' style='width:100%;border-radius:18px;border:1px solid rgba(82,255,154,.18);margin:10px 0 14px 0;' />
                    <p>{asset.get('note', '')}</p>
                </div>
                """,
                unsafe_allow_html=True,
            )


def render():
    st.markdown(
        """
        <div class='section'>
            <div class='num'>CONTENT PORTFOLIO GALLERY</div>
            <div class='title'>อัปโหลดลิงก์รูปผลงานจาก Google Drive</div>
            <div class='body'>
                ใช้ส่วนนี้สำหรับเก็บรูปผลงานวิดีโอ, ภาพหน้าจอคอนเทนต์, ผลงานสตรีม, Dashboard Screenshot หรือ Creative Showcase
                โดยอัปโหลดไฟล์จริงไว้ที่ Google Drive แล้วนำลิงก์มาใส่ ระบบจะบันทึกไว้และแสดงเป็น Gallery บนหน้า Portfolio
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    render_gallery_form()
    render_gallery_grid()
