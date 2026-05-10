import pandas as pd
import plotly.express as px
import streamlit as st

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
    .metric{border:1px solid rgba(82,255,154,.22);border-radius:20px;padding:16px;background:rgba(82,255,154,.06);height:130px;min-height:130px;box-sizing:border-box;}
    .metric-label{font-size:11px;color:var(--muted);font-weight:900;text-transform:uppercase;letter-spacing:.13em;margin-bottom:8px;}
    .metric-value{font-size:28px;color:#fff;font-weight:950;line-height:1.05;}
    .metric-note{font-size:12px;color:#9fb5a8;margin-top:8px;font-weight:750;line-height:1.4;}
    .skill-card{height:210px;border:1px solid rgba(82,255,154,.18);border-radius:18px;padding:18px;background:rgba(255,255,255,.035);box-sizing:border-box;margin-bottom:12px;overflow:hidden;}
    .skill-card h3{margin:0 0 9px 0;color:#fff;font-size:17px;line-height:1.2;}
    .skill-card p{color:#bfd1c5;font-size:13.5px;line-height:1.55;margin:0;}
    .tool-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:14px;margin-top:6px;}
    .tool-card{min-height:118px;border:1px solid rgba(82,255,154,.22);border-radius:20px;padding:16px;background:rgba(82,255,154,.055);box-sizing:border-box;}
    .tool-card-title{font-size:11px;color:var(--muted);font-weight:950;text-transform:uppercase;letter-spacing:.13em;margin-bottom:12px;}
    .tool-list{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:8px;align-items:center;}
    .tool-card.analytics .tool-list{grid-template-columns:repeat(2,minmax(0,1fr));}
    .tool-pill{display:flex;align-items:center;justify-content:center;height:34px;padding:0 10px;border:1px solid rgba(82,255,154,.22);border-radius:999px;background:rgba(82,255,154,.075);color:#d7ffe6;font-size:12px;font-weight:850;line-height:1;text-align:center;white-space:nowrap;box-sizing:border-box;}
    .ci-card{border:1px solid rgba(82,255,154,.20);border-radius:22px;padding:16px;background:rgba(255,255,255,.035);height:390px;box-sizing:border-box;overflow:hidden;margin-bottom:18px;}
    .ci-card h3{font-size:18px;color:#fff;margin:0 0 10px 0;line-height:1.2;}
    .ci-frame{height:250px;border:1px dashed rgba(82,255,154,.28);border-radius:16px;background:rgba(82,255,154,.045);display:flex;align-items:center;justify-content:center;text-align:center;color:#9fb5a8;font-size:12px;font-weight:800;line-height:1.4;padding:12px;box-sizing:border-box;overflow:hidden;margin-bottom:12px;}
    .ci-frame img{width:100%;height:100%;object-fit:cover;border-radius:13px;display:block;}
    .ci-desc{color:#bfd1c5;font-size:13px;line-height:1.45;margin:0 0 10px 0;}
    .ci-link{color:#52ff9a;font-size:13px;font-weight:900;text-decoration:none;}
    .ci-input-note{font-size:13px;color:#9fb5a8;margin:8px 0 14px 0;line-height:1.6;}
    @media(max-width:900px){.tool-grid{grid-template-columns:repeat(2,1fr)}.tool-list{grid-template-columns:repeat(2,minmax(0,1fr));}.cover h1{font-size:42px;white-space:normal;}}
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

def drive_image_url(url):
    url = str(url or '').strip()
    if 'drive.google.com' not in url:
        return url
    if '/file/d/' in url:
        file_id = url.split('/file/d/')[1].split('/')[0]
        return f'https://drive.google.com/uc?export=view&id={file_id}'
    if 'id=' in url:
        file_id = url.split('id=')[1].split('&')[0]
        return f'https://drive.google.com/uc?export=view&id={file_id}'
    return url

def ci_showcase(title, url, note):
    img_url = drive_image_url(url)
    if img_url:
        frame = f"<img src='{img_url}' alt='{title}' />"
        link = f"<a class='ci-link' href='{url}' target='_blank'>Open design →</a>"
    else:
        frame = "วาง Google Drive image link<br>ในช่องด้านบน แล้วกด Enter"
        link = "<span class='ci-link'>Waiting for Drive link</span>"
    st.markdown(f"<div class='ci-card'><div class='ci-frame'>{frame}</div><h3>{title}</h3><p class='ci-desc'>{note}</p>{link}</div>", unsafe_allow_html=True)

CI_DESIGN_LINK_1 = ""
CI_DESIGN_LINK_2 = ""
CI_DESIGN_LINK_3 = ""
CI_DESIGN_LINK_4 = ""

loan_data = pd.DataFrame([
    {"Campaign": "Campaign A", "Messages": 4902, "Spend": 38217.12, "Cost/Message": 7.80},
    {"Campaign": "Campaign B", "Messages": 1523, "Spend": 12559.22, "Cost/Message": 8.25},
    {"Campaign": "Campaign C", "Messages": 2181, "Spend": 18188.88, "Cost/Message": 8.34},
    {"Campaign": "Campaign D", "Messages": 867, "Spend": 7534.37, "Cost/Message": 8.69},
    {"Campaign": "Campaign E", "Messages": 1497, "Spend": 13322.62, "Cost/Message": 8.90},
    {"Campaign": "Campaign F", "Messages": 17480, "Spend": 212.27, "Cost/Message": 12.14},
    {"Campaign": "Campaign G", "Messages": 469, "Spend": 4648.82, "Cost/Message": 9.91},
    {"Campaign": "Campaign H", "Messages": 10902, "Spend": 140.64, "Cost/Message": 12.90},
    {"Campaign": "Campaign I", "Messages": 542, "Spend": 5698.00, "Cost/Message": 10.51},
    {"Campaign": "Campaign J", "Messages": 69, "Spend": 811.32, "Cost/Message": 11.76},
])

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

t1, t2, t3, t4, t5, t6, t7, t8, t9 = st.tabs([
    "01 Strategist", "02 Experience", "03 Loan Ads", "04 Retail", "05 Automation", "06 Content", "07 Tech Stack", "08 Dashboard", "09 Contact"
])

with t1:
    section(
        "01. STRATEGIST",
        "Technical & Performance Marketing",
        "ผมวางตัวเองเป็นสาย Performance Marketer ที่เชื่อมระหว่าง <span class='green'>Media Buying, Automation, AI Content และ Data Insight</span> เพื่อเปลี่ยนตัวเลขโฆษณาให้กลายเป็นการตัดสินใจทางธุรกิจที่เร็วและแม่นขึ้น"
    )

    st.markdown("<div class='num' style='margin-top:6px;'>TECHNICAL EXPERTISE</div>", unsafe_allow_html=True)
    s1, s2, s3, s4 = st.columns(4)
    with s1:
        st.markdown("<div class='skill-card'><h3>Advanced Media Buying</h3><p>วางโครงสร้างแคมเปญ Meta & TikTok แบบเน้นยอดขาย Conversion พร้อมกลยุทธ์การสเกลงบอย่างเป็นระบบ เพื่อรักษา ROAS และคุณภาพผลลัพธ์</p></div>", unsafe_allow_html=True)
    with s2:
        st.markdown("<div class='skill-card'><h3>Marketing Automation</h3><p>ออกแบบและเชื่อมต่อ Workflow ข้ามแพลตฟอร์มด้วย n8n และ Make เพื่อลดงาน Manual เพิ่มความเร็ว และทำให้ระบบการตลาดทำซ้ำได้</p></div>", unsafe_allow_html=True)
    with s3:
        st.markdown("<div class='skill-card'><h3>AI-Driven Content & Strategy</h3><p>ใช้ Prompt Engineering สร้าง Hook, Script และ Creative Angle สำหรับ TikTok/Reels ที่เน้นหยุดนิ้ว เพิ่มความสนใจ และต่อยอดการซื้อ</p></div>", unsafe_allow_html=True)
    with s4:
        st.markdown("<div class='skill-card'><h3>Data-Actionable Insights</h3><p>สร้าง Dashboard ด้วย Looker Studio อ่านจุดหลุด Drop-off points และแปลงข้อมูลเป็น Action ที่แก้ปัญหายอดขายได้ตรงจุด</p></div>", unsafe_allow_html=True)

    st.markdown(
        """
        <div class='section'>
          <div class='num'>TECH STACK & TOOLS</div>
          <div class='title'>Tool Stack ที่ใช้ทำงานจริง</div>
          <div class='tool-grid'>
            <div class='tool-card'>
              <div class='tool-card-title'>AD PLATFORMS</div>
              <div class='tool-list'><span class='tool-pill'>Meta Ads</span><span class='tool-pill'>TikTok Ads</span><span class='tool-pill'>Google Ads</span></div>
            </div>
            <div class='tool-card'>
              <div class='tool-card-title'>AUTOMATION</div>
              <div class='tool-list'><span class='tool-pill'>n8n</span><span class='tool-pill'>Make</span><span class='tool-pill'>Zapier</span></div>
            </div>
            <div class='tool-card'>
              <div class='tool-card-title'>AI TOOLS</div>
              <div class='tool-list'><span class='tool-pill'>Gemini API</span><span class='tool-pill'>ChatGPT</span><span class='tool-pill'>Midjourney</span></div>
            </div>
            <div class='tool-card analytics'>
              <div class='tool-card-title'>ANALYTICS</div>
              <div class='tool-list'><span class='tool-pill'>Looker Studio</span><span class='tool-pill'>GA4</span></div>
            </div>
          </div>
          <div class='quote'>“Efficiency is Intelligent Laziness”</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

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

    st.markdown("<div class='section'><div class='num'>CREATIVE DESIGN SHOWCASE</div><div class='title'>CI ที่เคยออกแบบ</div><div class='body'>วางลิงก์ Google Drive ในช่องด้านล่าง ระบบจะแสดงรูปทันทีใน session นี้ หากต้องการให้ค้างถาวร ให้ใส่ลิงก์ไว้ในโค้ดหรือ secrets ภายหลัง</div>", unsafe_allow_html=True)
    st.markdown("<div class='ci-input-note'>ตั้งค่าไฟล์ Drive เป็น Anyone with the link can view ก่อนวางลิงก์</div>", unsafe_allow_html=True)
    link_col1, link_col2 = st.columns(2)
    with link_col1:
        ci_input_1 = st.text_input("CI Design 01 Google Drive link", value=CI_DESIGN_LINK_1, key="ci_design_link_1")
        ci_input_3 = st.text_input("CI Design 03 Google Drive link", value=CI_DESIGN_LINK_3, key="ci_design_link_3")
    with link_col2:
        ci_input_2 = st.text_input("CI Design 02 Google Drive link", value=CI_DESIGN_LINK_2, key="ci_design_link_2")
        ci_input_4 = st.text_input("CI Design 04 Google Drive link", value=CI_DESIGN_LINK_4, key="ci_design_link_4")

    row1_col1, row1_col2 = st.columns(2)
    with row1_col1:
        ci_showcase("CI Design 01", ci_input_1, "Key Visual / Brand Direction")
    with row1_col2:
        ci_showcase("CI Design 02", ci_input_2, "Creative Layout / Campaign Visual")
    row2_col1, row2_col2 = st.columns(2)
    with row2_col1:
        ci_showcase("CI Design 03", ci_input_3, "Social Visual / Content Design")
    with row2_col2:
        ci_showcase("CI Design 04", ci_input_4, "Ad Creative / Performance Visual")
    st.markdown("</div>", unsafe_allow_html=True)

with t3:
    section("03. PERFORMANCE: BUSINESS LOAN ADS", "Message Funnel Performance Dashboard", "แปลงรายงาน Meta ฝั่งสินเชื่อธุรกิจให้เป็นชาร์ตพรีเซนต์ โดยเน้นจำนวนข้อความทัก ยอดจ่ายรวม และต้นทุนต่อข้อความ เพื่อแสดงการอ่าน Lead Quality จาก Message Funnel")
    m1, m2, m3, m4 = st.columns(4)
    with m1: metric("Total Messages", "39,254", "ข้อความทักรวมจากชุดแคมเปญ")
    with m2: metric("Total Spend", "฿106,776", "ยอดจ่ายรวมโดยประมาณ")
    with m3: metric("Avg Cost / Message", "฿2.72", "ต้นทุนเฉลี่ยต่อข้อความทัก")
    with m4: metric("Best Cost / Message", "฿7.80", "แคมเปญที่คุมต้นทุนดีที่สุด")

    st.markdown("<div class='section'><div class='num'>LOAN ADS PATTERN</div><div class='title'>ข้อความทักและยอดจ่ายรวม</div><div class='body'>กราฟแท่งสำหรับพรีเซนต์ Pattern ของแคมเปญสินเชื่อธุรกิจ โดยดูทั้ง Volume ของข้อความทักและ Cost Efficiency</div></div>", unsafe_allow_html=True)
    chart_col1, chart_col2 = st.columns(2)
    with chart_col1:
        fig_msg = px.bar(loan_data.sort_values('Messages', ascending=False), x='Campaign', y='Messages', text='Messages', title='Message Volume by Campaign')
        fig_msg.update_traces(textposition='outside')
        fig_msg.update_layout(height=430, template='plotly_dark', margin=dict(l=20, r=20, t=60, b=40))
        st.plotly_chart(fig_msg, use_container_width=True)
    with chart_col2:
        fig_cost = px.bar(loan_data.sort_values('Cost/Message'), x='Campaign', y='Cost/Message', text='Cost/Message', title='Cost per Message • Lower is Better')
        fig_cost.update_traces(texttemplate='฿%{text:.2f}', textposition='outside')
        fig_cost.update_layout(height=430, template='plotly_dark', margin=dict(l=20, r=20, t=60, b=40))
        st.plotly_chart(fig_cost, use_container_width=True)

    st.dataframe(loan_data, use_container_width=True, hide_index=True)

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
