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


render_intro_hero = load_render(
    "performance_marketing_audit_sections/section_01_intro_hero.py",
    "section_01_intro_hero",
)


def render():
    st.markdown(
        """
        <div class="section">
          <div class="num">Case Study Sub Tab 01</div>
          <div class="title">📈 Performance Marketing Audit</div>
          <div class="body">
            หน้านี้จะใช้เล่าเคสการตรวจสอบ Performance Marketing แบบเป็นระบบ ตั้งแต่ปัญหาในตัวเลข ไปจนถึง Action ที่ควรทำจริง<br><br>
            โครงหลักของเคสนี้จะเน้น: Funnel Diagnostic, KPI Audit, ROAS / CPR Analysis, Creative Fatigue, Retargeting Quality และ Recommendation ที่อ่านรู้เรื่องสำหรับเจ้าของธุรกิจ
          </div>
          <div class="quote">
            Framework: Problem → Data Signal → Root Cause → Action → KPI Impact
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    render_intro_hero()
