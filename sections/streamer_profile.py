import streamlit as st


TIKTOK_URL = "https://www.tiktok.com/@khunlungamer?is_from_webapp=1&sender_device=pc"


def render():
    st.markdown(
        """
        <div class='section'>
            <div class='num'>STREAMER BACKGROUND · KHUNLUNGAMER</div>
            <div class='title'>จากสตรีมเมอร์สู่ Performance Marketer ที่เข้าใจ Audience จริง</div>
            <div class='body'>
                ก่อนเข้าสู่สาย Performance Marketing ผมมีประสบการณ์ทำคอนเทนต์และไลฟ์สตรีมบน TikTok
                ในฐานะ <span class='green'>KhunlunGamer</span> ทำให้เข้าใจพฤติกรรมคนดูแบบ Real-time,
                การดึงความสนใจในช่วงเวลาสั้น ๆ, การคุยกับผู้ชม, การสร้าง Community และการเปลี่ยนผู้ชมให้กลายเป็นฐาน Audience ที่กลับมาติดตามซ้ำ
            </div>
            <div class='quote'>
                ประสบการณ์สตรีมเมอร์ทำให้ผมไม่ได้มอง Content เป็นแค่ Creative แต่เห็นเป็นระบบ Attention → Engagement → Trust → Conversion
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    c1, c2, c3 = st.columns(3)

    with c1:
        st.markdown(
            """
            <div class='card'>
                <h3>Real-time Audience Reading</h3>
                <p>เข้าใจวิธีอ่านพฤติกรรมผู้ชมขณะไลฟ์ เช่น ช่วงที่คนสนใจ ช่วงที่คนหลุด และจังหวะที่ควรเปลี่ยนเรื่องหรือเร่งพลังคอนเทนต์</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with c2:
        st.markdown(
            """
            <div class='card'>
                <h3>Community Engagement</h3>
                <p>มีประสบการณ์สื่อสารกับผู้ชมโดยตรง สร้างความสัมพันธ์ ความคุ้นเคย และความรู้สึกเป็นส่วนหนึ่งของคอมมูนิตี้</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with c3:
        st.markdown(
            f"""
            <div class='card'>
                <h3>TikTok Content Profile</h3>
                <p>ประสบการณ์ทำคอนเทนต์เกมและไลฟ์สตรีม ช่วยต่อยอดสู่การคิด Creative Angle, Hook, Retention และ Organic Growth</p>
                <p style='margin-top:12px;'><a href='{TIKTOK_URL}' target='_blank' style='color:#52ff9a;font-weight:900;text-decoration:none;'>View TikTok Profile →</a></p>
            </div>
            """,
            unsafe_allow_html=True,
        )
