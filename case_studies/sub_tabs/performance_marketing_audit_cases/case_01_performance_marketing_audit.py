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
        <div style="border:1px solid rgba(82,255,154,.15);border-radius:26px;background:linear-gradient(135deg,rgba(4,10,7,.72),rgba(11,26,18,.46));padding:24px 26px;margin-top:12px;margin-bottom:18px;box-shadow:0 18px 48px rgba(0,0,0,.18);">
          <div style="display:grid;grid-template-columns:0.95fr 1.05fr;gap:28px;align-items:start;">
            <div style="padding:4px 2px 2px 2px;">
              <div class="num" style="margin-bottom:8px;">CASE 1</div>
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
        </div>
        """,
        unsafe_allow_html=True,
    )

    t1, t2, t3, t4, t5 = st.tabs([
        "Strategic Audit Process",
        "KPI Framework",
        "Dashboard Preview",
        "AI Insight Layer",
        "Strategic Conclusion",
    ])

    with t1:
        render_strategic_audit()

    with t2:
        render_kpi()

    with t3:
        render_dashboard()

    with t4:
        render_ai()

    with t5:
        render_conclusion()
