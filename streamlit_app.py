import streamlit as st

from data.loan_data import loan_data, loan_summary
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
    .quote{margin-top:18px;padding:16px 20px;border-left:4px solid var(--green);background:rgba(82,255,154,.08);border-radius:16px;color:#effff5;font-size:16px;font-weight:850;line-height:1.55;}
    .card{height:310px;min-height:310px;border:1px solid rgba(82,255,154,.18);border-radius:24px;padding:22px;background:rgba(255,255,255,.035);box-sizing:border-box;display:flex;flex-direction:column;justify-content:flex-start;overflow:hidden;}
    .card h3{margin:0 0 14px 0;color:#fff;font-size:20px;line-height:1.25;min-height:58px;}
    .card p,.card li{color:#bfd1c5;font-size:14.5px;line-height:1.62;margin:0;}
    .experience-timeline{display:grid;grid-template-columns:repeat(4,1fr);gap:44px;align-items:center;margin:4px 8px 14px 8px;}
    .timeline-step{position:relative;min-height:46px;display:flex;align-items:center;justify-content:center;}
    .timeline-badge{width:34px;height:34px;border-radius:999px;background:rgba(82,255,154,.13);border:1px solid rgba(82,255,154,.55);color:#52ff9a;font-weight:950;display:flex;align-items:center;justify-content:center;box-shadow:0 0 24px rgba(82,255,154,.18);z-index:2;}
    .timeline-step:not(:last-child)::after{content:"";position:absolute;left:calc(50% + 20px);right:calc(-50% - 24px);top:50%;height:1px;background:linear-gradient(90deg,rgba(82,255,154,.8),rgba(82,255,154,.18));}
    .timeline-step:not(:last-child)::before{content:"›";position:absolute;right:calc(-50% - 34px);top:calc(50% - 17px);color:#52ff9a;font-size:30px;font-weight:950;line-height:1;}
    .timeline-year{position:absolute;top:-10px;left:50%;transform:translateX(-50%);font-size:10px;letter-spacing:.12em;color:#9fb5a8;font-weight:950;white-space:nowrap;text-transform:uppercase;}
    .metric{border:1px solid rgba(82,255,154,.18);border-radius:18px;padding:13px 14px;background:rgba(82,255,154,.045);min-height:102px;height:102px;box-sizing:border-box;}
    .metric-label{font-size:9.5px;color:var(--muted);font-weight:900;text-transform:uppercase;letter-spacing:.12em;margin-bottom:7px;line-height:1.2;}
    .metric-value{font-size:23px;color:#fff;font-weight:950;line-height:1.02;letter-spacing:-.4px;}
    .metric-note{font-size:11px;color:#9fb5a8;margin-top:7px;font-weight:750;line-height:1.35;}
    .skill-card{height:210px;border:1px solid rgba(82,255,154,.18);border-radius:18px;padding:18px;background:rgba(255,255,255,.035);box-sizing:border-box;margin-bottom:12px;overflow:hidden;}
    .skill-card h3{margin:0 0 9px 0;color:#fff;font-size:17px;line-height:1.2;}
    .skill-card p{color:#bfd1c5;font-size:13.5px;line-height:1.55;margin:0;}
    .tool-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:14px;margin-top:6px;}
    .tool-card{min-height:118px;border:1px solid rgba(82,255,154,.22);border-radius:20px;padding:16px;background:rgba(82,255,154,.055);box-sizing:border-box;}
    .tool-card-title{font-size:11px;color:var(--muted);font-weight:950;text-transform:uppercase;letter-spacing:.13em;margin-bottom:12px;}
    .tool-list{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:8px;align-items:center;}
    .tool-card.analytics .tool-list{grid-template-columns:repeat(2,minmax(0,1fr));}
    .tool-pill{display:flex;align-items:center;justify-content:center;height:34px;padding:0 10px;border:1px solid rgba(82,255,154,.22);border-radius:999px;background:rgba(82,255,154,.075);color:#d7ffe6;font-size:12px;font-weight:850;line-height:1;text-align:center;white-space:nowrap;box-sizing:border-box;}
    .ci-card{border:1px solid rgba(82,255,154,.20);border-radius:22px;padding:12px;background:rgba(255,255,255,.035);height:300px;box-sizing:border-box;overflow:hidden;margin-bottom:18px;}
    .ci-frame{height:274px;border:1px dashed rgba(82,255,154,.28);border-radius:16px;background:rgba(82,255,154,.045);display:flex;align-items:center;justify-content:center;box-sizing:border-box;overflow:hidden;}
    .ci-frame img{width:100%;height:100%;object-fit:cover;border-radius:13px;display:block;}
    @media(max-width:900px){.tool-grid,.experience-timeline{grid-template-columns:repeat(2,1fr)}.timeline-step:before,.timeline-step:after{display:none}.tool-list{grid-template-columns:repeat(2,minmax(0,1fr));}.cover h1{font-size:42px;white-space:normal;}.metric{min-height:96px;height:96px}.metric-value{font-size:21px}}
    .green{color:var(--green);font-weight:950;}
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
    render_loan_ads(loan_summary, loan_data)

with t4:
    render_retail()

with t5:
    render_automation()

with t6:
    render_content()

with t7:
    render_contact()
