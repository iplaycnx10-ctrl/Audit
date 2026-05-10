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
    .experience-timeline{display:grid;grid-template-columns:repeat(4,1fr);gap:44px;align-items:center;margin:4px 8px 14px 8px;}
    .timeline-step{position:relative;min-height:46px;display:flex;align-items:center;justify-content:center;}
    .timeline-badge{width:34px;height:34px;border-radius:999px;background:rgba(82,255,154,.13);border:1px solid rgba(82,255,154,.55);color:#52ff9a;font-weight:950;display:flex;align-items:center;justify-content:center;box-shadow:0 0 24px rgba(82,255,154,.18);z-index:2;}
    .timeline-step:not(:last-child)::after{content:"";position:absolute;left:calc(50% + 20px);right:calc(-50% - 24px);top:50%;height:1px;background:linear-gradient(90deg,rgba(82,255,154,.8),rgba(82,255,154,.18));}
    .timeline-step:not(:last-child)::before{content:"›";position:absolute;right:calc(-50% - 34px);top:calc(50% - 17px);color:#52ff9a;font-size:30px;font-weight:950;line-height:1;}
    .timeline-year{position:absolute;top:-10px;left:50%;transform:translateX(-50%);font-size:10px;letter-spacing:.12em;color:#9fb5a8;font-weight:950;white-space:nowrap;text-transform:uppercase;}
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
    .ci-card{border:1px solid rgba(82,255,154,.20);border-radius:22px;padding:12px;background:rgba(255,255,255,.035);height:300px;box-sizing:border-box;overflow:hidden;margin-bottom:18px;}
    .ci-frame{height:274px;border:1px dashed rgba(82,255,154,.28);border-radius:16px;background:rgba(82,255,154,.045);display:flex;align-items:center;justify-content:center;box-sizing:border-box;overflow:hidden;}
    .ci-frame img{width:100%;height:100%;object-fit:cover;border-radius:13px;display:block;}
    @media(max-width:900px){.tool-grid,.experience-timeline{grid-template-columns:repeat(2,1fr)}.timeline-step:before,.timeline-step:after{display:none}.tool-list{grid-template-columns:repeat(2,minmax(0,1fr));}.cover h1{font-size:42px;white-space:normal;}}
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

def exp_card(title, body, link_text=None, link_url=None):
    link_html = ""
    if link_text and link_url:
        link_html = f"<p style='margin-top:12px;'><a href='{link_url}' target='_blank' style='color:#52ff9a;font-weight:900;text-decoration:none;'>{link_text} →</a></p>"
    st.markdown(f"<div class='card'><h3>{title}</h3><p>{body}</p>{link_html}</div>", unsafe_allow_html=True)

def drive_image_url(url):
    url = str(url or '').strip()
    if 'drive.google.com' not in url:
        return url
    if '/file/d/' in url:
        file_id = url.split('/file/d/')[1].split('/')[0]
        return f'https://drive.google.com/thumbnail?id={file_id}&sz=w1600'
    if 'id=' in url:
        file_id = url.split('id=')[1].split('&')[0]
        return f'https://drive.google.com/thumbnail?id={file_id}&sz=w1600'
    return url

def ci_showcase(title, url, note):
    img_url = drive_image_url(url)
    if img_url:
        frame = f"<img src='{img_url}' alt='{title}' referrerpolicy='no-referrer' />"
    else:
        frame = ""
    st.markdown(f"<div class='ci-card'><div class='ci-frame'>{frame}</div></div>", unsafe_allow_html=True)

CI_DESIGN_LINK_1 = "https://drive.google.com/file/d/1rbL0PhE85Pu2Y_VjCY7RzWBAuDjG8jEM/view?usp=sharing"
CI_DESIGN_LINK_2 = "https://drive.google.com/file/d/1rgcXSo4Z-7HGjNfNBY8ni2vb1HKZM7OT/view?usp=sharing"
CI_DESIGN_LINK_3 = "https://drive.google.com/file/d/1NFSGbKlcF51OHJ29vPYchoOXh9GDkfyq/view?usp=sharing"
CI_DESIGN_LINK_4 = "https://drive.google.com/file/d/1_fOiOGm8v3qBLntLcSYGH87gBQcmgJsQ/view?usp=sharing"

loan_summary = {
    "total_spend": 283904.06,
    "total_messages": 36023,
    "total_reach": 323081,
    "total_impressions": 1385069,
    "avg_ctr": 11.30,
    "avg_cpm": 204.36,
    "avg_cpc": 6.71,
}
loan_summary["avg_cost"] = loan_summary["total_spend"] / loan_summary["total_messages"]

loan_data = pd.DataFrame([
    {"Ad": "A", "Messages": 5359, "Spend": 42093.85, "Cost/Message": 7.85, "Reach": 87347, "Impressions": 277656, "CTR": 11.70, "CPM": 151.60, "CPC": 5.04, "Frequency": 3.18},
    {"Ad": "B", "Messages": 4902, "Spend": 38217.12, "Cost/Message": 7.80, "Reach": 84774, "Impressions": 261303, "CTR": 13.44, "CPM": 146.25, "CPC": 4.82, "Frequency": 3.08},
    {"Ad": "C", "Messages": 1523, "Spend": 12559.22, "Cost/Message": 8.25, "Reach": 33642, "Impressions": 89869, "CTR": 10.54, "CPM": 139.75, "CPC": 7.20, "Frequency": 2.67},
    {"Ad": "D", "Messages": 2181, "Spend": 18188.88, "Cost/Message": 8.34, "Reach": 24193, "Impressions": 84516, "CTR": 13.13, "CPM": 215.21, "CPC": 6.89, "Frequency": 3.49},
    {"Ad": "E", "Messages": 867, "Spend": 7534.37, "Cost/Message": 8.69, "Reach": 23080, "Impressions": 47283, "CTR": 9.39, "CPM": 159.35, "CPC": 5.86, "Frequency": 2.05},
    {"Ad": "F", "Messages": 1497, "Spend": 13322.62, "Cost/Message": 8.90, "Reach": 19891, "Impressions": 46390, "CTR": 11.44, "CPM": 287.19, "CPC": 7.90, "Frequency": 2.33},
    {"Ad": "G", "Messages": 469, "Spend": 4648.82, "Cost/Message": 9.91, "Reach": 17321, "Impressions": 30289, "CTR": 8.88, "CPM": 153.48, "CPC": 5.60, "Frequency": 1.75},
    {"Ad": "H", "Messages": 542, "Spend": 5698.00, "Cost/Message": 10.51, "Reach": 10026, "Impressions": 23721, "CTR": 10.28, "CPM": 240.21, "CPC": 6.48, "Frequency": 2.37},
    {"Ad": "I", "Messages": 69, "Spend": 811.32, "Cost/Message": 11.76, "Reach": 9133, "Impressions": 11788, "CTR": 10.40, "CPM": 68.82, "CPC": 8.11, "Frequency": 1.29},
    {"Ad": "J", "Messages": 17480, "Spend": 212.27, "Cost/Message": 12.14, "Reach": 17480, "Impressions": 17480, "CTR": 12.14, "CPM": 12.14, "CPC": 6.82, "Frequency": 1.00},
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
    st.markdown("""
    <div class='experience-timeline'>
      <div class='timeline-step'><div class='timeline-year'>2018-2024</div><div class='timeline-badge'>1</div></div>
      <div class='timeline-step'><div class='timeline-year'>2024-2025</div><div class='timeline-badge'>2</div></div>
      <div class='timeline-step'><div class='timeline-year'>2026</div><div class='timeline-badge'>3</div></div>
      <div class='timeline-step'><div class='timeline-year'>2026</div><div class='timeline-badge'>4</div></div>
    </div>
    """, unsafe_allow_html=True)
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        exp_card("Financial Services", "Lead Generation สำหรับสินเชื่อธุรกิจ วางระบบคัดกรองผ่าน Message Funnel และอ่านสัญญาณความพร้อมจากพฤติกรรมแชท", "View Loan Ads", "#")
    with c2:
        exp_card("Streamer & Gaming Content Creator", "มีประสบการณ์ทำคอนเทนต์และไลฟ์สตรีมบน TikTok ในนาม KhunlunGamer เข้าใจ Real-time Engagement และ Audience Relationship", "View TikTok Profile", "https://www.tiktok.com/@khunlungamer?is_from_webapp=1&sender_device=pc")
    with c3:
        exp_card("Hotel & Hospitality Marketing", "วางแผนการสื่อสารและกระตุ้นยอดจองห้องพักสำหรับธุรกิจโรงแรม โดยใช้ดาต้าเพื่อหาช่วงเวลาที่ Demand ตลาดสูงที่สุด", "View Hospitality", "#")
    with c4:
        exp_card("Retail & High-Ticket Electronics", "บริหารกลยุทธ์ Online-to-Offline สำหรับสินค้ากลุ่ม Premium Gadgets และเครื่องใช้ไฟฟ้ามูลค่าสูง เพื่อดึงทราฟฟิกออนไลน์เข้าสู่หน้าร้าน", "View Retail", "#")
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<div class='section'><div class='num'>CREATIVE DESIGN SHOWCASE</div><div class='title'>CI ที่เคยออกแบบ</div>", unsafe_allow_html=True)

    row1_col1, row1_col2 = st.columns(2)
    with row1_col1:
        ci_showcase("CI Design 01", CI_DESIGN_LINK_1, "Key Visual / Brand Direction")
    with row1_col2:
        ci_showcase("CI Design 02", CI_DESIGN_LINK_2, "Creative Layout / Campaign Visual")
    row2_col1, row2_col2 = st.columns(2)
    with row2_col1:
        ci_showcase("CI Design 03", CI_DESIGN_LINK_3, "Social Visual / Content Design")
    with row2_col2:
        ci_showcase("CI Design 04", CI_DESIGN_LINK_4, "Ad Creative / Performance Visual")
    st.markdown("</div>", unsafe_allow_html=True)

with t3:
    section("03. PERFORMANCE: BUSINESS LOAN ADS", "Message Funnel Performance Dashboard", "พอร์ตผลงานแคมเปญสินเชื่อธุรกิจจากข้อมูล Meta Ads รวม 2 ชุด ใช้เพื่อโชว์การอ่านภาพรวม Funnel, Cost Efficiency และ Volume Pattern")
    m1, m2, m3, m4 = st.columns(4)
    with m1: metric("Total Spend", f"฿{loan_summary['total_spend']:,.0f}", "งบประมาณรวมจาก 2 ชุดข้อมูล")
    with m2: metric("Total Messages", f"{loan_summary['total_messages']:,.0f}", "ข้อความทักรวมโดยประมาณ")
    with m3: metric("Avg Cost / Message", f"฿{loan_summary['avg_cost']:,.2f}", "ต้นทุนเฉลี่ยต่อข้อความ")
    with m4: metric("Total Reach", f"{loan_summary['total_reach']:,.0f}", "จำนวนคนที่เข้าถึงรวม")

    k1, k2, k3, k4 = st.columns(4)
    with k1: metric("Impressions", f"{loan_summary['total_impressions']:,.0f}", "จำนวนครั้งที่แสดงผลรวม")
    with k2: metric("Avg CTR", f"{loan_summary['avg_ctr']:.2f}%", "CTR เฉลี่ยโดยประมาณ")
    with k3: metric("Avg CPM", f"฿{loan_summary['avg_cpm']:.2f}", "CPM เฉลี่ยโดยประมาณ")
    with k4: metric("Avg CPC", f"฿{loan_summary['avg_cpc']:.2f}", "CPC เฉลี่ยโดยประมาณ")

    chart_col1, chart_col2 = st.columns(2)
    with chart_col1:
        fig_msg = px.bar(loan_data.sort_values('Messages', ascending=False), x='Ad', y='Messages', text='Messages', color='Messages', color_continuous_scale='Viridis', title='Message Volume Heat Pattern')
        fig_msg.update_traces(texttemplate='%{text:,.0f}', textposition='outside')
        fig_msg.update_layout(height=430, template='plotly_dark', margin=dict(l=20, r=20, t=60, b=40), xaxis_title='', coloraxis_showscale=False)
        st.plotly_chart(fig_msg, use_container_width=True)
    with chart_col2:
        fig_cost = px.bar(loan_data.sort_values('Cost/Message'), x='Ad', y='Cost/Message', text='Cost/Message', color='Cost/Message', color_continuous_scale='Turbo', title='Cost per Message Heat Pattern • Lower is Better')
        fig_cost.update_traces(texttemplate='฿%{text:.2f}', textposition='outside')
        fig_cost.update_layout(height=430, template='plotly_dark', margin=dict(l=20, r=20, t=60, b=40), xaxis_title='', coloraxis_showscale=False)
        st.plotly_chart(fig_cost, use_container_width=True)

    chart_col3, chart_col4 = st.columns(2)
    with chart_col3:
        fig_spend = px.pie(loan_data, values='Spend', names='Ad', hole=.55, title='Spend Distribution by Ad Set')
        fig_spend.update_layout(height=430, template='plotly_dark', margin=dict(l=20, r=20, t=60, b=40), showlegend=True)
        st.plotly_chart(fig_spend, use_container_width=True)
    with chart_col4:
        efficiency_data = loan_data[['Ad', 'CTR', 'CPM', 'CPC', 'Frequency']].sort_values('CTR', ascending=False)
        fig_eff = px.bar(efficiency_data, x='Ad', y=['CTR', 'CPC', 'Frequency'], barmode='group', title='Engagement & Efficiency Snapshot')
        fig_eff.update_layout(height=430, template='plotly_dark', margin=dict(l=20, r=20, t=60, b=40), xaxis_title='')
        st.plotly_chart(fig_eff, use_container_width=True)

with t4:
    section("04. STRATEGY: HIGH-VALUE RETAIL", "The Hybrid Closing Model", "วางระบบ Multi-touchpoint Funnel สำหรับสินค้ากลุ่มเครื่องใช้ไฟฟ้ามูลค่าสูง เชื่อมจากแอด → แชท → เว็บไซต์/หน้าร้าน และใช้ข้อมูลเพื่อดู Pattern ของแคมเปญ")

with t5:
    automation_img = drive_image_url(AUTOMATION_ARCHITECTURE_LINK)
    with t5:
    with t5:
    section(
        "05. AUTOMATION ARCHITECTURE",
        "Marketing Brain with AI Agent Workflows",
        "ออกแบบ Workflow เชื่อม n8n, AI API, Google Sheets และ Dashboard เพื่อเปลี่ยนข้อมูลโฆษณาเป็น Insight และ Action แบบอัตโนมัติ"
    )

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
