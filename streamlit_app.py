import streamlit as st

from pages_section.page_01_strategist import render as render_strategist
from pages_section.page_02_experience import render as render_experience
from pages_section.page_03_loan_ads import render as render_loan_ads
from pages_section.page_04_retail import render as render_retail
from pages_section.page_05_automation import render as render_automation
from pages_section.page_06_content import render as render_content
from pages_section.page_07_contact import render as render_contact

st.set_page_config(
    page_title="Strategic Portfolio | Chayanon Nantawijan",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown(
    """
    <style>
    :root{--bg:#07110c;--panel:#0b1a12;--green:#52ff9a;--text:#f8fafc;--muted:#9fb5a8;--line:rgba(82,255,154,.22);}
    .stApp{background:radial-gradient(circle at top right,rgba(82,255,154,.12),transparent 26%),linear-gradient(180deg,#050806 0%,#07110c 42%,#030504 100%);color:var(--text);}
    .block-container{padding-top:2.2rem;max-width:1180px;}
    [data-testid="stHeader"]{background:transparent;}
    .cover{min-height:420px;border:1px solid var(--line);border-radius:32px;padding:44px 44px;background:linear-gradient(135deg,rgba(9,28,18,.96),rgba(3,8,5,.96));box-shadow:0 24px 70px rgba(0,0,0,.34);position:relative;overflow:hidden;margin-bottom:24px;}
    .cover:after{content:"";position:absolute;width:360px;height:360px;border-radius:999px;background:rgba(82,255,154,.10);right:-140px;top:-120px;filter:blur(10px);}
    .kicker{font-size:12px;letter-spacing:.42em;text-transform:uppercase;font-weight:950;color:var(--green);margin-bottom:74px;position:relative;z-index:2;}
    .cover h1{font-size:56px;line-height:1;margin:0;color:#fff;letter-spacing:-2px;max-width:900px;position:relative;z-index:2;white-space:nowrap;}
    .role{font-size:21px;line-height:1.35;color:#d7ffe6;font-weight:800;margin-top:22px;max-width:620px;position:relative;z-index:2;}
    .est{position:absolute;left:44px;bottom:36px;color:var(--green);font-size:11px;font-weight:950;letter-spacing:.24em;z-index:2;}
    .section{border:1px solid var(--line);border-radius:28px;padding:28px;background:rgba(11,26,18,.72);box-shadow:0 20px 70px rgba(0,0,0,.22);margin:16px 0 20px 0;}
    .num{font-size:12px;letter-spacing:.22em;text-transform:uppercase;color:var(--green);font-weight:950;margin-bottom:10px;}
    .title{font-size:30px;font-weight:950;color:#fff;letter-spacing:-.7px;margin-bottom:14px;}
    .body{font-size:16px;line-height:1.7;color:#d7e8dd;}
    .metric{border:1px solid rgba(82,255,154,.18);border-radius:18px;padding:13px 14px;background:rgba(82,255,154,.045);min-height:102px;height:102px;box-sizing:border-box;}
    .metric-label{font-size:9.5px;color:var(--muted);font-weight:900;text-transform:uppercase;letter-spacing:.12em;margin-bottom:7px;line-height:1.2;}
    .metric-value{font-size:23px;color:#fff;font-weight:950;line-height:1.02;letter-spacing:-.4px;}
    .metric-note{font-size:11px;color:#9fb5a8;margin-top:7px;font-weight:750;line-height:1.35;}
    .stTabs [data-baseweb="tab-list"]{gap:8px;flex-wrap:wrap;background:rgba(255,255,255,.035);border:1px solid rgba(82,255,154,.18);border-radius:20px;padding:10px;margin-bottom:18px;}
    .stTabs [data-baseweb="tab"]{height:44px;border-radius:14px;color:#bfd1c5;background:rgba(255,255,255,.035);font-weight:900;padding:0 14px;}
    .stTabs [aria-selected="true"]{background:rgba(82,255,154,.16);color:#52ff9a;border:1px solid rgba(82,255,154,.28);}
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="cover">
      <div class="kicker">Strategic Portfolio</div>
      <h1>CHAYANON NANTAWIJAN</h1>
      <div class="role">Performance Marketing &<br>AI Automation Specialist</div>
      <div class="est">ESTABLISHED 2026 | PERFORMANCE-DRIVEN</div>
    </div>
    """,
    unsafe_allow_html=True,
)

t1, t2, t3, t4, t5, t6, t7 = st.tabs([
    "01 Strategist",
    "02 Experience",
    "03 Loan Ads",
    "04 Retail",
    "05 Automation",
    "06 Content",
    "07 Contact",
])

with t1:
    render_strategist()

with t2:
    render_experience()

with t3:
    render_loan_ads()

with t4:
    render_retail()

with t5:
    render_automation()

with t6:
    render_content()

with t7:
    render_contact()
