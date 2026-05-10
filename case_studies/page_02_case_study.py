import importlib.util
from pathlib import Path
import streamlit as st

BASE_DIR = Path(__file__).resolve().parent


def load_render(relative_path: str, module_key: str):
    module_path = BASE_DIR / relative_path
    spec = importlib.util.spec_from_file_location(module_key, module_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.render


render_performance_audit = load_render(
    "sub_tabs/performance_marketing_audit.py",
    "performance_marketing_audit",
)


def render():
    st.markdown(
        """
        <div class="section">
          <div class="num">02 Case Study</div>
          <div class="title">Case Studies — Performance Thinking in Action</div>
          <div class="body">
            พื้นที่นี้จะใช้เล่าเคสแบบมนุษย์อ่านง่าย: ปัญหา → สิ่งที่วิเคราะห์ → สิ่งที่ทำ → ผลลัพธ์ → KPI
          </div>
          <div class="quote">
            เป้าหมายของหน้านี้ไม่ใช่โชว์ Dashboard ก่อน แต่คือทำให้คนอ่านเข้าใจว่าเราแก้ปัญหาธุรกิจด้วย Data, Funnel Logic และ Performance Strategy ยังไง
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    s1, s2, s3, s4, s5 = st.tabs([
        "📈 Performance Marketing Audit",
        "🧠 AI Audit Workflow",
        "🛒 E-Commerce Funnel",
        "🎯 Retarget Strategy",
        "📊 Dashboard & BI",
    ])

    with s1:
        render_performance_audit()

    with s2:
        st.info("AI Audit Workflow — Coming Soon")

    with s3:
        st.info("E-Commerce Funnel — Coming Soon")

    with s4:
        st.info("Retarget Strategy — Coming Soon")

    with s5:
        st.info("Dashboard & BI — Coming Soon")
