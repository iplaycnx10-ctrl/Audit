import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(
    page_title="Strategic Portfolio | Chayanon Nantavicharn",
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
    .cover{min-height:520px;border:1px solid var(--line);border-radius:36px;padding:54px 48px;background:linear-gradient(135deg,rgba(9,28,18,.96),rgba(3,8,5,.96));box-shadow:0 28px 90px rgba(0,0,0,.38);position:relative;overflow:hidden;margin-bottom:28px;}
    .cover:after{content:"";position:absolute;width:420px;height:420px;border-radius:999px;background:rgba(82,255,154,.10);right:-150px;top:-130px;filter:blur(10px);}
    .kicker{font-size:13px;letter-spacing:.42em;text-transform:uppercase;font-weight:950;color:var(--green);margin-bottom:96px;position:relative;z-index:2;}
    .cover h1{font-size:78px;line-height:.92;margin:0;color:#fff;letter-spacing:-3px;max-width:760px;position:relative;z-index:2;}
    .role{font-size:24px;line-height:1.35;color:#d7ffe6;font-weight:800;margin-top:24px;max-width:620px;position:relative;z-index:2;}
    .est{position:absolute;left:48px;bottom:42px;color:var(--green);font-size:12px;font-weight:950;letter-spacing:.24em;z-index:2;}
    .section{border:1px solid var(--line);border-radius:32px;padding:34px;background:rgba(11,26,18,.72);box-shadow:0 20px 70px rgba(0,0,0,.22);margin:18px 0 24px 0;}
    .num{font-size:13px;letter-spacing:.22em;text-transform:uppercase;color:var(--green);font-weight:950;margin-bottom:10px;}
    .title{font-size:34px;font-weight:950;color:#fff;letter-spacing:-.7px;margin-bottom:18px;}
    .body{font-size:17px;line-height:1.82;color:#d7e8dd;}
    .quote{margin-top:20px;padding:20px 22px;border-left:4px solid var(--green);background:rgba(82,255,154,.08);border-radius:18px;color:#effff5;font-size:17px;font-weight:850;line-height:1.65;}
    .card{height:240px;min-height:240px;border:1px solid rgba(82,255,154,.18);border-radius:24px;padding:24px;background:rgba(255,255,255,.035);box-sizing:border-box;display:flex;flex-direction:column;justify-content:flex-start;}
    .card h3{margin:0 0 16px 0;color:#fff;font-size:22px;line-height:1.25;min-height:58px;}
    .card p,.card li{color:#bfd1c5;font-size:15.5px;line-height:1.72;margin:0;}
    .metric{border:1px solid rgba(82,255,154,.22);border-radius:22px;padding:20px;background:rgba(82,255,154,.06);height:160px;min-height:160px;box-sizing:border-box;}
    .metric-label{font-size:12px;color:var(--muted);font-weight:900;text-transform:uppercase;letter-spacing:.13em;margin-bottom:8px;}
    .metric-value{font-size:32px;color:#fff;font-weight:950;line-height:1.05;}
    .metric-note{font-size:13px;color:#9fb5a8;margin-top:8px;font-weight:750;line-height:1.45;}
    .green{color:var(--green);font-weight:950;}
    .stTabs [data-baseweb="tab-list"]{gap:8px;flex-wrap:wrap;background:rgba(255,255,255,.035);border:1px solid rgba(82,255,154,.18);border-radius:20px;padding:10px;margin-bottom:18px;}
    .stTabs [data-baseweb="tab"]{height:44px;border-radius:14px;color:#bfd1c5;background:rgba(255,255,255,.035);font-weight:900;padding:0 14px;}
    .stTabs [aria-selected="true"]{background:rgba(82,255,154,.16);color:#52ff9a;border:1px solid rgba(82,255,154,.28);}
    </style>
    """,
    unsafe_allow_html=True,
)

def section(num, title, body_html):
    st.markdown(f"<div class='section'><div class='num'>{num}</div><div class='title'>{title}</div><div class='body'>{body_html}</div></div>", unsafe_allow_html=True)

def metric(label, value, note):
    st.markdown(f"<div class='metric'><div class='metric-label'>{label}</div><div class='metric-value'>{value}</div><div class='metric-note'>{note}</div></div>", unsafe_allow_html=True)

st.markdown(
    """
    <div class="cover">
      <div class="kicker">Strategic Portfolio</div>
      <h1>CHAYANON<br>NANTAVICHARN</h1>
      <div class="role">Performance Marketing &<br>AI Automation Specialist</div>
      <div class="est">ESTABLISHED 2026 | PERFORMANCE-DRIVEN</div>
    </div>
    """,
    unsafe_allow_html=True,
)

t1, t2, t3, t4, t5, t6, t7, t8, t9 = st.tabs([
    "01 Strategist", "02 Experience", "03 Loan Ads", "04 Retail", "05 Automation", "06 Content", "07 Tech Stack", "08 Dashboard", "09 Contact"
])

with t1:
    section("01. THE STRATEGIST", "Performance Marketer Who Builds Revenue Engine", "ผมคือ Performance Marketer ที่เชี่ยวชาญการใช้ <span class='green'>AI และ Automation</span> มาแก้ปัญหาธุรกิจในระดับโครงสร้าง ไม่ได้มองโฆษณาเป็นแค่การจ่ายเงินซื้อคลิก แต่มองเป็น Revenue Engine ที่ต้องปรับจูนด้วยข้อมูล พฤติกรรมลูกค้า และสัญญาณความต้องการจริง<div class='quote'>“Efficiency is Intelligent Laziness.” ผมสร้างระบบอัตโนมัติเพื่อให้คนทำงานน้อยลง แต่ได้ผลลัพธ์ที่แม่นยำและเสถียรกว่าเดิม</div>")

with t2:
    st.markdown("<div class='section'><div class='num'>02. INDUSTRY EXPERIENCE</div><div class='title'>Industry Experience</div>", unsafe_allow_html=True)
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.markdown("<div class='card'><h3>Retail & High-Ticket Electronics</h3><p>บริหารกลยุทธ์ Online-to-Offline สำหรับสินค้ากลุ่ม Premium Gadgets และเครื่องใช้ไฟฟ้ามูลค่าสูง เพื่อดึงทราฟฟิกออนไลน์เข้าสู่หน้าร้าน</p></div>", unsafe_allow_html=True)
    with c2:
        st.markdown("<div class='card'><h3>Financial Services</h3><p>Lead Generation สำหรับสินเชื่อธุรกิจ วางระบบคัดกรองผ่าน Message Funnel และอ่านสัญญาณความพร้อมจากพฤติกรรมแชท</p></div>", unsafe_allow_html=True)
    with c3:
        st.markdown("<div class='card'><h3>Hotel & Hospitality Marketing</h3><p>วางแผนการสื่อสารและกระตุ้นยอดจองห้องพักสำหรับธุรกิจโรงแรม โดยใช้ดาต้าเพื่อหาช่วงเวลาที่ Demand ตลาดสูงที่สุด</p></div>", unsafe_allow_html=True)
    with c4:
        st.markdown("<div class='card'><h3>Streamer & Gaming Content Creator</h3><p>มีประสบการณ์ทำคอนเทนต์และไลฟ์สตรีมบน TikTok ในนาม <b>KhunlunGamer</b> เข้าใจ Real-time Engagement และ Audience Relationship</p><p style='margin-top:12px;'><a href='https://www.tiktok.com/@khunlungamer?is_from_webapp=1&sender_device=pc' target='_blank' style='color:#52ff9a;font-weight:900;text-decoration:none;'>View TikTok Profile →</a></p></div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

with t3:
    section("03. PERFORMANCE: BUSINESS LOAN ADS", "Message Funnel Performance Dashboard", "แปลงรายงาน Meta ฝั่งสินเชื่อธุรกิจให้เป็นชาร์ตพรีเซนต์ โดยเน้นจำนวนข้อความทัก ยอดจ่ายรวม และต้นทุนต่อข้อความ เพื่อแสดงการอ่าน Lead Quality จาก Message Funnel")
    m1, m2, m3, m4 = st.columns(4)
    with m1: metric("Total Messages", "39,254", "ข้อความทักรวมจากชุดแคมเปญ")
    with m2: metric("Total Spend", "฿106,776", "ยอดจ่ายรวมโดยประมาณ")
    with m3: metric("Avg Cost / Message", "฿2.72", "ต้นทุนเฉลี่ยต่อข้อความทัก")
    with m4: metric("Best Cost / Message", "฿7.80", "แคมเปญที่คุมต้นทุนดีที่สุด")

with t4:
    section("04. STRATEGY: HIGH-VALUE RETAIL", "The Hybrid Closing Model", "วางระบบ Multi-touchpoint Funnel สำหรับสินค้ากลุ่มเครื่องใช้ไฟฟ้ามูลค่าสูง เชื่อมจากแอด → แชท → เว็บไซต์/หน้าร้าน และใช้ข้อมูลเพื่อดู Pattern ของแคมเปญ")

with t5:
    section("05. AUTOMATION ARCHITECTURE", "Marketing Brain with AI Agent Workflows", "ออกแบบ Workflow เชื่อม n8n, AI API, Google Sheets และ Dashboard เพื่อเปลี่ยนข้อมูลโฆษณาเป็น Insight และ Action แบบอัตโนมัติ")

with t6:
    section("06. CONTENT FACTORY", "Organic Growth & TikTok Strategy", "ประสบการณ์ทำ TikTok / Streaming / Content Workflow เพื่อเข้าใจ Attention, Engagement, Hook และ Audience Retention")
    c1, c2, c3 = st.columns(3)
    with c1: metric("TikTok Growth", "0 → 8,000+", "Followers ภายใน 9 เดือน")
    with c2: metric("Content", "Organic 100%", "พิสูจน์ความเข้าใจ Algorithm")
    with c3: metric("Workflow", "AI + API", "วางโครงสร้างสคริปต์และ video automation")

with t7:
    section("07. TECH STACK", "Tools & Platforms", "Meta Ads, TikTok Ads, Google Ads, GA4, Looker Studio, Google Sheets, n8n, Webhooks, Gemini API, Prompt Engineering")

with t8:
    section("08. DASHBOARD THINKING", "Demo Performance Intelligence", "ออกแบบ Dashboard เพื่ออ่าน Funnel, Campaign Pattern, Cost Efficiency และ Business Signal ให้เจ้าของธุรกิจเข้าใจง่าย")

with t9:
    section("09. PORTFOLIO NOTE", "Built for Recruiter Review", "หน้าเว็บนี้ใช้เป็นลิงก์ Portfolio สำหรับสมัครงาน แสดงวิธีคิดด้าน Performance Marketing, Dashboard, AI Automation และการแปลงข้อมูลให้เป็น Action โดยใช้ข้อมูลตัวอย่างเพื่อไม่เปิดเผยข้อมูลลูกค้าจริง")
