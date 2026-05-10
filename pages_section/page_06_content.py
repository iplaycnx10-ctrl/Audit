import streamlit as st
from components.common import metric, section


def render():
    section(
        "06. CONTENT FACTORY",
        "Organic Growth & TikTok Strategy",
        "ประสบการณ์ทำ TikTok / Streaming / Content Workflow เพื่อเข้าใจ Attention, Engagement, Hook และ Audience Retention"
    )

    c1, c2, c3 = st.columns(3)
    with c1:
        metric("TikTok Growth", "0 → 8,000+", "Followers ภายใน 9 เดือน")
    with c2:
        metric("Content", "Organic 100%", "พิสูจน์ความเข้าใจ Algorithm")
    with c3:
        metric("Workflow", "AI + API", "วางโครงสร้างสคริปต์และ video automation")
