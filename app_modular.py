import streamlit as st

from sections import cover
from sections import strategist
from sections import experience
from sections import content_gallery


st.set_page_config(
    page_title="Strategic Portfolio | Chayanon Nantavicharn",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown("""
<style>
:root{--green:#52ff9a;--text:#f8fafc;--muted:#9fb5a8;--line:rgba(82,255,154,.22);}
.stApp{background:radial-gradient(circle at top right,rgba(82,255,154,.12),transparent 26%),linear-gradient(180deg,#050806 0%,#07110c 42%,#030504 100%);color:var(--text);}
.block-container{padding-top:2.2rem;max-width:1180px;}
[data-testid="stHeader"]{background:transparent;}
.cover{min-height:560px;border:1px solid var(--line);border-radius:36px;padding:54px 48px;background:linear-gradient(135deg,rgba(9,28,18,.96),rgba(3,8,5,.96));box-shadow:0 28px 90px rgba(0,0,0,.38);position:relative;overflow:hidden;margin-bottom:28px;}
.cover:after{content:"";position:absolute;width:420px;height:420px;border-radius:999px;background:rgba(82,255,154,.10);right:-150px;top:-130px;filter:blur(10px);}
.kicker{font-size:13px;letter-spacing:.42em;text-transform:uppercase;font-weight:950;color:var(--green);margin-bottom:96px;position:relative;z-index:2;}
.cover h1{font-size:64px;line-height:.95;margin:0;color:#fff;letter-spacing:-3px;max-width:760px;position:relative;z-index:2;}
.role{font-size:24px;line-height:1.35;color:#d7ffe6;font-weight:800;margin-top:24px;max-width:620px;position:relative;z-index:2;}
.est{position:absolute;left:48px;bottom:42px;color:var(--green);font-size:12px;font-weight:950;letter-spacing:.24em;z-index:2;}
.section{border:1px solid var(--line);border-radius:32px;padding:34px;background:rgba(11,26,18,.72);box-shadow:0 20px 70px rgba(0,0,0,.22);margin:18px 0 24px 0;}
.num{font-size:13px;letter-spacing:.22em;text-transform:uppercase;color:var(--green);font-weight:950;margin-bottom:10px;}
.title{font-size:34px;font-weight:950;color:#fff;letter-spacing:-.7px;margin-bottom:18px;}
.body{font-size:17px;line-height:1.82;color:#d7e8dd;}
.quote{margin-top:20px;padding:20px 22px;border-left:4px solid var(--green);background:rgba(82,255,154,.08);border-radius:18px;color:#effff5;font-size:17px;font-weight:850;line-height:1.65;}
.card{height:270px;min-height:270px;border:1px solid rgba(82,255,154,.18);border-radius:24px;padding:24px;background:rgba(255,255,255,.035);box-sizing:border-box;display:flex;flex-direction:column;justify-content:flex-start;}
.card h3{margin:0 0 16px 0;color:#fff;font-size:21px;line-height:1.25;min-height:58px;}
.card p,.card li{color:#bfd1c5;font-size:15px;line-height:1.72;margin:0;}
.metric{border:1px solid rgba(82,255,154,.22);border-radius:22px;padding:20px;background:rgba(82,255,154,.06);height:160px;min-height:160px;box-sizing:border-box;}
.metric-label{font-size:12px;color:var(--muted);font-weight:900;text-transform:uppercase;letter-spacing:.13em;margin-bottom:8px;}
.metric-value{font-size:32px;color:#fff;font-weight:950;line-height:1.05;}
.metric-note{font-size:13px;color:#9fb5a8;margin-top:8px;font-weight:750;line-height:1.45;}
.green{color:var(--green);font-weight:950;}
.stTabs [data-baseweb="tab-list"]{gap:8px;flex-wrap:wrap;background:rgba(255,255,255,.035);border:1px solid rgba(82,255,154,.18);border-radius:20px;padding:10px;margin-bottom:18px;}
.stTabs [data-baseweb="tab"]{height:44px;border-radius:14px;color:#bfd1c5;background:rgba(255,255,255,.035);font-weight:900;padding:0 14px;}
.stTabs [aria-selected="true"]{background:rgba(82,255,154,.16);color:#52ff9a;border:1px solid rgba(82,255,154,.28);}
</style>
""", unsafe_allow_html=True)

cover.render()

tabs = st.tabs([
    "01 Strategist",
    "02 Experience",
    "03 Loan Ads",
    "04 Retail",
    "05 Automation",
    "06 Content",
    "07 Tech Stack",
    "08 Dashboard",
    "09 Contact",
])

with tabs[0]:
    strategist.render()

with tabs[1]:
    experience.render()

with tabs[2]:
    st.info("Loan Ads module กำลังแยกจากไฟล์หลัก")

with tabs[3]:
    st.info("Retail module กำลังแยกจากไฟล์หลัก")

with tabs[4]:
    st.info("Automation module กำลังแยกจากไฟล์หลัก")

with tabs[5]:
    st.markdown("<div class='section'><div class='num'>06. CONTENT FACTORY</div><div class='title'>Organic Growth & TikTok Strategy</div></div>", unsafe_allow_html=True)
    content_gallery.render()

with tabs[6]:
    st.info("Tech Stack module กำลังแยกจากไฟล์หลัก")

with tabs[7]:
    st.info("Dashboard module กำลังแยกจากไฟล์หลัก")

with tabs[8]:
    st.info("Contact module กำลังแยกจากไฟล์หลัก")
