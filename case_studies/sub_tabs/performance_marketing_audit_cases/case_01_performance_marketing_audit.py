import importlib.util
from pathlib import Path
import streamlit as st

BASE_DIR = Path(__file__).resolve().parent
ROOT_DIR = BASE_DIR.parent.parent


def load_render(relative_path: str, module_key: str, root_dir=BASE_DIR):
    module_path = root_dir / relative_path
    spec = importlib.util.spec_from_file_location(module_key, module_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.render


render_section_nav = load_render(
    "navigation/case_section_nav.py",
    "case_section_nav",
    ROOT_DIR,
)

render_strategic_audit = load_render(
    "case_01_sections/strategic_audit_process.py",
    "strategic_audit_process",
)
render_kpi = load_render(
    "case_01_sections/kpi_framework.py",
    "kpi_framework",
)
render_dashboard = load_render(
    "case_01_sections/dashboard_preview.py",
    "dashboard_preview",
)
render_ai = load_render(
    "case_01_sections/ai_insight_layer.py",
    "ai_insight_layer",
)
render_conclusion = load_render(
    "case_01_sections/strategic_conclusion.py",
    "strategic_conclusion",
)


def render():
    st.markdown(
        """
        <div style="display:grid;grid-template-columns:0.95fr 1.05fr;gap:28px;align-items:start;margin-top:10px;margin-bottom:18px;">
          <div style="padding:8px 2px 6px 2px;">
            <div class="num" style="margin-bottom:8px;">CASE 1</div>
            <div style="font-size:13px;color:#facc15;font-weight:900;margin-bottom:10px;line-height:1.45;">โจทย์: ทำไม Reach ดีแต่ยอดไม่มา</div>
            <div class="title" style="font-size:25px;margin-bottom:10px;">Medical Aesthetic Funnel Analysis</div>
            <div class="body" style="font-size:14px;line-height:1.65;color:#d7e8dd;max-width:500px;">
              <b>กิจการ:</b> Medical Aesthetic<br><br>
              <b>ปัญหาหลักที่ตรวจพบ</b>
            </div>
          </div>

          <div style="display:grid;grid-template-columns:repeat(2,1fr);gap:12px;">
            <div style="height:96px;min-height:96px;padding:12px 13px;border-radius:18px;border:1px solid rgba(239,68,68,.42);background:linear-gradient(135deg,rgba(127,29,29,.42),rgba(11,26,18,.55));box-sizing:border-box;overflow:hidden;">
              <div style="font-size:12px;font-weight:900;color:#fff;line-height:1.25;margin-bottom:13px;">❌ High Lead Cost</div>
              <div style="font-size:10.8px;color:#ffd5d5;line-height:1.45;">ค่า Lead สูง แต่คุณภาพไม่สม่ำเสมอ</div>
            </div>
            <div style="height:96px;min-height:96px;padding:12px 13px;border-radius:18px;border:1px solid rgba(249,115,22,.38);background:linear-gradient(135deg,rgba(154,52,18,.34),rgba(11,26,18,.55));box-sizing:border-box;overflow:hidden;">
              <div style="font-size:12px;font-weight:900;color:#fff;line-height:1.25;margin-bottom:13px;">❌ Weak Retargeting Structure</div>
              <div style="font-size:10.8px;color:#ffe1c7;line-height:1.45;">ไม่มีระบบ Follow-up สำหรับคนที่สนใจบริการ</div>
            </div>
            <div style="height:96px;min-height:96px;padding:12px 13px;border-radius:18px;border:1px solid rgba(245,158,11,.36);background:linear-gradient(135deg,rgba(146,64,14,.30),rgba(11,26,18,.55));box-sizing:border-box;overflow:hidden;">
              <div style="font-size:12px;font-weight:900;color:#fff;line-height:1.25;margin-bottom:13px;">❌ Creative Fatigue</div>
              <div style="font-size:10.8px;color:#ffe9bd;line-height:1.45;">ยิงโปรเดิมซ้ำจน CTR ตก และ Frequency สูง</div>
            </div>
            <div style="height:96px;min-height:96px;padding:12px 13px;border-radius:18px;border:1px solid rgba(234,179,8,.32);background:linear-gradient(135deg,rgba(113,63,18,.26),rgba(11,26,18,.55));box-sizing:border-box;overflow:hidden;">
              <div style="font-size:12px;font-weight:900;color:#fff;line-height:1.25;margin-bottom:13px;">❌ Poor Conversion Journey</div>
              <div style="font-size:10.8px;color:#fff1bd;line-height:1.45;">คนทักเยอะ แต่ไม่จองคิว</div>
            </div>
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    selected_section = render_section_nav()

    if selected_section == "strategic_audit":
        render_strategic_audit()

    elif selected_section == "kpi_framework":
        render_kpi()

    elif selected_section == "dashboard_preview":
        render_dashboard()

    elif selected_section == "ai_insight":
        render_ai()

    elif selected_section == "strategic_conclusion":
        render_conclusion()
