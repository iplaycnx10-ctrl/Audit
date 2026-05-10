import streamlit as st
from components.common import drive_image_url, section


AUTOMATION_LINK = "https://drive.google.com/file/d/1IpqUubvu9G4xOnWd_XKIbz00XAMwzyG7/view?usp=sharing"
APP_DEMO_LINK = "https://support-tickets-hh2c21kgwad.streamlit.app/"

APP_IMAGE_LINKS = [
    "https://drive.google.com/file/d/1hkNiMzAh16b9VBMjTihwzVsaLQPy6Yjz/view?usp=sharing",
    "https://drive.google.com/file/d/1-jFfqNbBk9Lt-xA2s1LnUd18ybHMv1Y1/view?usp=sharing",
    "https://drive.google.com/file/d/1Eo3tla4gfcinMGZMqin6ERs2Xkq2XIve/view?usp=sharing",
    "https://drive.google.com/file/d/1oJlA6u7mm7qYqr8u2Ow4O11x6cvZ1x9c/view?usp=sharing",
    "https://drive.google.com/file/d/1W1gxhSDC7CAdPUQnpBVh7UhY0Hi7MuTe/view?usp=sharing",
]


def inject_gallery_style():
    st.markdown(
        """
        <style>
        .app-zoom-card{border:1px solid rgba(82,255,154,.20);border-radius:22px;padding:10px;background:rgba(255,255,255,.035);box-shadow:0 18px 54px rgba(0,0,0,.20);height:250px;display:flex;align-items:center;justify-content:center;overflow:hidden;box-sizing:border-box;margin-bottom:18px;cursor:zoom-in;transition:transform .22s ease,border-color .22s ease,box-shadow .22s ease;}
        .app-zoom-card:hover{transform:scale(1.035);border-color:rgba(82,255,154,.55);box-shadow:0 22px 80px rgba(82,255,154,.12),0 18px 54px rgba(0,0,0,.35);z-index:5;}
        .app-zoom-card img{width:100%;height:100%;object-fit:cover;border-radius:15px;display:block;transition:transform .22s ease;}
        .app-zoom-card:hover img{transform:scale(1.04);}
        .app-zoom-card:active{position:fixed;inset:5vh 5vw;width:90vw;height:90vh;z-index:9999;background:rgba(3,8,5,.96);cursor:zoom-out;padding:16px;}
        .app-zoom-card:active img{object-fit:contain;transform:none;}
        .app-demo-btn{display:inline-flex;align-items:center;gap:10px;margin-top:18px;padding:12px 18px;border:1px solid rgba(82,255,154,.35);border-radius:999px;background:rgba(82,255,154,.10);color:#52ff9a!important;font-weight:950;text-decoration:none!important;box-shadow:0 14px 40px rgba(82,255,154,.08);}
        .app-demo-btn:hover{background:rgba(82,255,154,.16);border-color:rgba(82,255,154,.65);}
        @media(max-width:900px){.app-zoom-card{height:210px;}.app-zoom-card:active{inset:6vh 4vw;width:92vw;height:88vh;}}
        </style>
        """,
        unsafe_allow_html=True,
    )


def app_image_card(link, alt="APP Preview"):
    img = drive_image_url(link)
    st.markdown(
        f"""
        <div class="app-zoom-card">
            <img src="{img}" alt="{alt}" referrerpolicy="no-referrer" />
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_app_gallery():
    inject_gallery_style()

    st.markdown(
        f"""
        <div class='section' style='margin-top:28px;'>
            <div class='num'>APP</div>
            <div class='title'>ประเมิน APP Marketing AI intel <span style='font-size:18px;color:#9fb5a8;'>(อยู่ในช่วงกำลังพัฒนา)</span></div>
            <div class='body'>ตัวอย่างหน้าจอระบบ AI Marketing Intelligence สำหรับประเมินผลและต่อยอดการวิเคราะห์<br>มีแอปจริงให้เปิดดูได้ แต่ยังติดหน้า Login เพื่อป้องกันข้อมูลและระบบหลังบ้าน</div>
            <a class='app-demo-btn' href='{APP_DEMO_LINK}' target='_blank'>View Prototype / Login Page →</a>
        </div>
        """,
        unsafe_allow_html=True,
    )

    row1 = st.columns(3, gap="large")
    for col, link in zip(row1, APP_IMAGE_LINKS[:3]):
        with col:
            app_image_card(link)

    row2 = st.columns(3, gap="large")
    for index, col in enumerate(row2):
        with col:
            if index < 2:
                app_image_card(APP_IMAGE_LINKS[index + 3])
            else:
                st.markdown(
                    """
                    <div style="border:1px dashed rgba(82,255,154,.18);border-radius:22px;height:250px;background:rgba(255,255,255,.018);margin-bottom:18px;"></div>
                    """,
                    unsafe_allow_html=True,
                )


def render():
    section(
        "05. AUTOMATION ARCHITECTURE",
        "Marketing Brain with AI Agent Workflows",
        "ออกแบบ Workflow เชื่อม n8n, AI API, Google Sheets และ Dashboard เพื่อเปลี่ยนข้อมูลโฆษณาเป็น Insight และ Action แบบอัตโนมัติ"
    )

    automation_img = drive_image_url(AUTOMATION_LINK)
    st.image(automation_img, use_container_width=True)

    render_app_gallery()
