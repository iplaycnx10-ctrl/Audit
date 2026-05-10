import streamlit as st
from components.common import metric, section


TIKTOK_PROFILE = "https://www.tiktok.com/@khunlungamer?is_from_webapp=1&sender_device=pc"
TIKTOK_VIDEO_45M = "https://www.tiktok.com/@khunlungamer/video/7469287547366067474?is_from_webapp=1&sender_device=pc&web_id=7526276357015258642"
TIKTOK_VIDEO_800K = "https://www.tiktok.com/@khunlungamer/video/7469287547366067474?is_from_webapp=1&sender_device=pc&web_id=7526276357015258642"


def tiktok_card(title, stat, body, url):
    st.markdown(
        f"""
        <div class='section' style='height:260px;display:flex;flex-direction:column;justify-content:space-between;'>
            <div>
                <div class='num'>TIKTOK SHOWCASE</div>
                <div class='title' style='font-size:24px;'>{title}</div>
                <div style='font-size:34px;font-weight:950;color:#fff;line-height:1;margin:12px 0;'>{stat}</div>
                <div class='body'>{body}</div>
            </div>
            <a href='{url}' target='_blank' style='color:#52ff9a;font-weight:950;text-decoration:none;'>View TikTok Video →</a>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render():
    section(
        "06. CONTENT FACTORY",
        "Organic Growth & TikTok Strategy",
        "เป็น Partner ค่าเกมส์แห่งนึงในประเทศไทย และเป็น Partner กับบริษัทเกมส์ต่างชาติในช่วงที่ทำ พร้อมประสบการณ์ทำ TikTok / Streaming / Content Workflow เพื่อเข้าใจ Attention, Engagement, Hook และ Audience Retention"
    )

    c1, c2, c3 = st.columns(3)
    with c1:
        metric("TikTok Growth", "0 → 8,000+", "Followers ภายใน 9 เดือน")
    with c2:
        metric("Content", "Organic 100%", "พิสูจน์ความเข้าใจ Algorithm")
    with c3:
        metric("Workflow", "AI + API", "วางโครงสร้างสคริปต์และ video automation")

    st.markdown("<div style='height:22px;'></div>", unsafe_allow_html=True)

    showcase_1, showcase_2 = st.columns(2, gap="large")
    with showcase_1:
        tiktok_card(
            "Viral Content Proof",
            "4.5M Views",
            "ตัวอย่างคอนเทนต์ที่สร้าง Organic Reach สูงมาก สะท้อนความเข้าใจ Hook, Timing, Retention และพฤติกรรมผู้ชมจริง",
            TIKTOK_VIDEO_45M,
        )
    with showcase_2:
        tiktok_card(
            "High Reach Content",
            "800K Views",
            "ตัวอย่างคอนเทนต์ที่ทำยอดเข้าถึงสูง ใช้เป็นหลักฐานว่ามีประสบการณ์อ่านแพตเทิร์น Algorithm และ Attention จริง",
            TIKTOK_VIDEO_800K,
        )

    st.markdown(
        f"""
        <div class='section'>
            <div class='num'>PROFILE</div>
            <div class='title'>KhunlunGamer TikTok Channel</div>
            <div class='body'>ช่อง Organic Content / Gaming / Streaming ที่ใช้ทดลอง Hook, Audience Retention, Real-time Engagement และ Content Pattern จากการทำจริง</div>
            <br>
            <a href='{TIKTOK_PROFILE}' target='_blank' style='color:#52ff9a;font-weight:950;text-decoration:none;'>View TikTok Profile →</a>
        </div>
        """,
        unsafe_allow_html=True,
    )
