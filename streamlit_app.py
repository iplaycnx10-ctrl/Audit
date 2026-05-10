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
    :root{--bg:#07110c;--panel:#0b1a12;--green:#52ff9a;--green2:#21d66b;--text:#f8fafc;--muted:#9fb5a8;--line:rgba(82,255,154,.22);}
    .stApp{background:radial-gradient(circle at top right,rgba(82,255,154,.12),transparent 26%),linear-gradient(180deg,#050806 0%,#07110c 42%,#030504 100%);color:var(--text);}
    .block-container{padding-top:2.2rem;max-width:1180px;}
    [data-testid="stHeader"]{background:transparent;}
    .cover{min-height:560px;border:1px solid var(--line);border-radius:36px;padding:54px 48px;background:linear-gradient(135deg,rgba(9,28,18,.96),rgba(3,8,5,.96));box-shadow:0 28px 90px rgba(0,0,0,.38);position:relative;overflow:hidden;margin-bottom:28px;}
    .cover:after{content:"";position:absolute;width:420px;height:420px;border-radius:999px;background:rgba(82,255,154,.10);right:-150px;top:-130px;filter:blur(10px);}
    .kicker{font-size:13px;letter-spacing:.42em;text-transform:uppercase;font-weight:950;color:var(--green);margin-bottom:96px;position:relative;z-index:2;}
    .cover h1{font-size:78px;line-height:.92;margin:0;color:#fff;letter-spacing:-3px;max-width:760px;position:relative;z-index:2;}
    .role{font-size:24px;line-height:1.35;color:#d7ffe6;font-weight:800;margin-top:24px;max-width:620px;position:relative;z-index:2;}
    .est{position:absolute;left:48px;bottom:42px;color:var(--green);font-size:12px;font-weight:950;letter-spacing:.24em;z-index:2;}
    .section{border:1px solid var(--line);border-radius:32px;padding:34px 34px;background:rgba(11,26,18,.72);box-shadow:0 20px 70px rgba(0,0,0,.22);margin:18px 0 24px 0;}
    .num{font-size:13px;letter-spacing:.22em;text-transform:uppercase;color:var(--green);font-weight:950;margin-bottom:10px;}
    .title{font-size:34px;font-weight:950;color:#fff;letter-spacing:-.7px;margin-bottom:18px;}
    .body{font-size:17px;line-height:1.82;color:#d7e8dd;}
    .quote{margin-top:20px;padding:20px 22px;border-left:4px solid var(--green);background:rgba(82,255,154,.08);border-radius:18px;color:#effff5;font-size:17px;font-weight:850;line-height:1.65;}
    .card{height:100%;border:1px solid rgba(82,255,154,.18);border-radius:24px;padding:24px;background:rgba(255,255,255,.035);}
    .card h3{margin:0 0 10px 0;color:#fff;font-size:22px;line-height:1.25;}
    .card p,.card li{color:#bfd1c5;font-size:15.5px;line-height:1.72;margin:0;}
    .bullet{margin:0;padding-left:20px;}
    .metric{border:1px solid rgba(82,255,154,.22);border-radius:22px;padding:20px;background:rgba(82,255,154,.06);height:100%;}
    .metric-label{font-size:12px;color:var(--muted);font-weight:900;text-transform:uppercase;letter-spacing:.13em;margin-bottom:8px;}
    .metric-value{font-size:32px;color:#fff;font-weight:950;line-height:1.05;}
    .metric-note{font-size:13px;color:#9fb5a8;margin-top:8px;font-weight:750;line-height:1.45;}
    .contact{border:1px solid var(--line);border-radius:36px;padding:48px;background:linear-gradient(135deg,rgba(82,255,154,.12),rgba(2,6,4,.95));text-align:center;margin:18px 0 6px 0;}
    .contact h2{font-size:46px;color:#fff;margin:0 0 10px 0;letter-spacing:-1.2px;}
    .contact p{color:#d7ffe6;font-size:18px;line-height:1.8;margin:6px 0;}
    .small{font-size:12px;color:#7f9688;letter-spacing:.18em;text-transform:uppercase;font-weight:900;text-align:center;margin-top:20px;}
    .green{color:var(--green);font-weight:950;}
    .stDataFrame{border-radius:20px;overflow:hidden;}
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


sample = pd.DataFrame([
    {"Campaign": "Loan Lead Gen", "Spend": 42000, "Leads": 186, "Signal": "Chat Intent", "Decision": "Scale Carefully"},
    {"Campaign": "High AOV Retail", "Spend": 68000, "Leads": 124, "Signal": "O2O Store Visit", "Decision": "Optimize Trust"},
    {"Campaign": "Hotel Booking Push", "Spend": 18000, "Leads": 52, "Signal": "Seasonal Demand", "Decision": "Hold / Burst"},
])

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

(t1, t2, t3, t4, t5, t6, t7, t8, t9) = st.tabs([
    "01 Strategist", "02 Experience", "03 Loan Ads", "04 Retail", "05 Automation", "06 Content", "07 Tech Stack", "08 Dashboard", "09 Contact"
])

with t1:
    section(
        "01. THE STRATEGIST",
        "Performance Marketer Who Builds Revenue Engine",
        "ผมคือ Performance Marketer ที่เชี่ยวชาญการใช้ <span class='green'>AI และ Automation</span> มาแก้ปัญหาธุรกิจในระดับโครงสร้าง ไม่ได้มองโฆษณาเป็นแค่การจ่ายเงินซื้อคลิก แต่มองเป็น Revenue Engine ที่ต้องปรับจูนด้วยข้อมูล พฤติกรรมลูกค้า และสัญญาณความต้องการจริง<div class='quote'>“Efficiency is Intelligent Laziness.” ผมสร้างระบบอัตโนมัติเพื่อให้คนทำงานน้อยลง แต่ได้ผลลัพธ์ที่แม่นยำและเสถียรกว่าเดิม</div>",
    )

with t2:
    st.markdown("<div class='section'><div class='num'>02. INDUSTRY EXPERIENCE</div><div class='title'>Industry Experience</div>", unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown("<div class='card'><h3>Retail & High-Ticket Electronics</h3><p>บริหารกลยุทธ์ Online-to-Offline สำหรับสินค้ากลุ่ม Premium Gadgets และเครื่องใช้ไฟฟ้ามูลค่าสูง เพื่อดึงทราฟฟิกออนไลน์เข้าสู่หน้าร้าน</p></div>", unsafe_allow_html=True)
    with c2:
        st.markdown("<div class='card'><h3>Financial Services</h3><p>Lead Generation สำหรับสินเชื่อธุรกิจ วางระบบคัดกรองผ่าน Message Funnel และอ่านสัญญาณความพร้อมจากพฤติกรรมแชท</p></div>", unsafe_allow_html=True)
    with c3:
        st.markdown("<div class='card'><h3>Hospitality & Tourism</h3><p>วางแผนการสื่อสารและกระตุ้นยอดจองห้องพักโดยใช้ดาต้าเพื่อหาช่วงเวลาที่ Demand ตลาดสูงที่สุด</p></div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

with t3:
    st.markdown("<div class='section'><div class='num'>03. PERFORMANCE: LOAN ADS</div><div class='title'>Data-Driven Lead Acquisition</div>", unsafe_allow_html=True)
    m1, m2, m3 = st.columns(3)
    with m1: metric("Focus", "Qualified Leads", "เน้นคุณภาพ Lead มากกว่าจำนวนคลิก")
    with m2: metric("Method", "Chat Signal", "ใช้พฤติกรรมการทักแชทประเมิน intent")
    with m3: metric("Action", "Scale Control", "ขยายงบเมื่อ signal และคุณภาพ lead รองรับ")
    st.markdown("<div class='body' style='margin-top:18px;'>บริหารแคมเปญที่มีความท้าทายสูงในกลุ่ม Financial Services โดยแยก Audience Intent ตามความต้องการสินเชื่อ และใช้ข้อมูลเชิงพฤติกรรมเพื่อประเมินว่าควร Scale, Hold หรือ Rebuild</div></div>", unsafe_allow_html=True)

with t4:
    st.markdown("<div class='section'><div class='num'>04. STRATEGY: HIGH-VALUE RETAIL</div><div class='title'>The Hybrid Closing Model</div>", unsafe_allow_html=True)
    r1, r2, r3 = st.columns(3)
    with r1:
        st.markdown("<div class='card'><h3>Multi-Touchpoint Funnel</h3><p>เห็นแอด → ทักแชทสอบถาม → จบการซื้อที่ร้านหรือหน้าเว็บ</p></div>", unsafe_allow_html=True)
    with r2:
        st.markdown("<div class='card'><h3>Frequency Logic</h3><p>ควบคุมการเห็นซ้ำให้พอดี เพื่อสร้างความมั่นใจโดยไม่ทำให้เกิด creative fatigue</p></div>", unsafe_allow_html=True)
    with r3:
        st.markdown("<div class='card'><h3>AOV Optimization</h3><p>วิเคราะห์โอกาสเพิ่มยอดขายต่อหัวผ่าน bundle, set, warranty และ value-added offer</p></div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

with t5:
    st.markdown("<div class='section'><div class='num'>05. AUTOMATION ARCHITECTURE</div><div class='title'>Marketing Brain with AI Agent Workflows</div>", unsafe_allow_html=True)
    a1, a2 = st.columns([1, 1])
    with a1:
        st.markdown("<div class='card'><h3>AI Agent Workflow</h3><ul class='bullet'><li>เชื่อม n8n กับ Gemini/GPT ผ่าน Webhook/API</li><li>วิเคราะห์แคมเปญแบบหลายชั้นเชิงกลยุทธ์</li><li>เปลี่ยนตัวเลขดิบเป็น Insight ภาษาธุรกิจ</li><li>ช่วยตรวจ conflict ระหว่าง AI output กับ raw data</li></ul></div>", unsafe_allow_html=True)
    with a2:
        st.markdown("<div class='quote'>เปลี่ยนงานวิเคราะห์ที่ต้องใช้เวลาหลายชั่วโมง ให้เสร็จภายในไม่กี่วินาที และลดการตัดสินใจจากความรู้สึก</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

with t6:
    st.markdown("<div class='section'><div class='num'>06. CONTENT FACTORY</div><div class='title'>Organic Growth & TikTok Strategy</div>", unsafe_allow_html=True)
    cf1, cf2, cf3 = st.columns(3)
    with cf1: metric("TikTok Growth", "0 → 8,000+", "Followers ภายใน 9 เดือน")
    with cf2: metric("Content", "Organic 100%", "พิสูจน์ความเข้าใจ Algorithm")
    with cf3: metric("Workflow", "AI + API", "วางโครงสร้างสคริปต์และ video automation")
    st.markdown("</div>", unsafe_allow_html=True)

with t7:
    st.markdown("<div class='section'><div class='num'>07. TECH STACK</div><div class='title'>Tools & Platforms</div>", unsafe_allow_html=True)
    tech = pd.DataFrame([
        {"Category": "Ads Platforms", "Tools & Platforms": "Meta Ads, TikTok Ads, Google Ads"},
        {"Category": "AI & Logic", "Tools & Platforms": "Gemini API, Prompt Engineering, ChatGPT"},
        {"Category": "Automation", "Tools & Platforms": "n8n, Webhooks, API Integrations"},
        {"Category": "Data Analysis", "Tools & Platforms": "Looker Studio, Google Sheets, Query/App Script"},
        {"Category": "Media Production", "Tools & Platforms": "CapCut, AI Video Gen, Canva"},
    ])
    st.dataframe(tech, use_container_width=True, hide_index=True)
    st.markdown("</div>", unsafe_allow_html=True)

with t8:
    st.markdown("<div class='section'><div class='num'>08. DASHBOARD THINKING</div><div class='title'>Demo Performance Intelligence</div>", unsafe_allow_html=True)
    chart_col, table_col = st.columns([1.1, .9])
    with chart_col:
        fig = px.bar(sample, x="Campaign", y="Spend", text="Decision", title="Budget Context by Campaign Type")
        fig.update_layout(height=390, paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)", font_color="#d7e8dd", margin=dict(l=10, r=10, t=48, b=10))
        st.plotly_chart(fig, use_container_width=True)
    with table_col:
        st.dataframe(sample, use_container_width=True, hide_index=True)
    st.markdown("</div>", unsafe_allow_html=True)

with t9:
    st.markdown("<div class='section'><div class='num'>09. PORTFOLIO NOTE</div><div class='title'>Built for Recruiter Review</div><div class='body'>หน้าเว็บนี้ออกแบบเพื่อใช้เป็นลิงก์ Portfolio สำหรับสมัครงาน แสดงวิธีคิดด้าน Performance Marketing, Dashboard, AI Automation และการแปลงข้อมูลให้เป็น Action โดยใช้ข้อมูลตัวอย่างเพื่อความปลอดภัยและไม่เปิดเผยข้อมูลลูกค้าจริง</div></div>", unsafe_allow_html=True)
    st.markdown(
        """
        <div class="contact">
          <div class="num">LET'S WORK TOGETHER</div>
          <h2>ยกระดับการตลาดด้วยข้อมูลและระบบอัตโนมัติ</h2>
          <p><b>ชญานนท์ นันทวิจารณ์ (Bas)</b></p>
          <p>โทร: 098-093-5022 · อีเมล: iPlaycnx.10@gmail.com</p>
          <p>เชียงใหม่ | รีโมททั่วประเทศ</p>
        </div>
        <div class="small">PORTFOLIO RE-ENGINEERED FOR 2026</div>
        """,
        unsafe_allow_html=True,
    )
