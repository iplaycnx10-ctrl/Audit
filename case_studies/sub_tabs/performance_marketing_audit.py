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


render_case_01 = load_render(
    "performance_marketing_audit_cases/case_01_performance_marketing_audit.py",
    "case_01_performance_marketing_audit",
)

render_case_02 = load_render(
    "performance_marketing_audit_cases/case_02_branding_strategy_analysis.py",
    "case_02_branding_strategy_analysis",
)

render_case_03 = load_render(
    "performance_marketing_audit_cases/case_03_journey_traffic_leak_analysis.py",
    "case_03_journey_traffic_leak_analysis",
)


def render():
    c1, c2, c3 = st.tabs([
        "CASE 1 — Performance Marketing Audit",
        "CASE 2 — Branding Strategy Analysis",
        "CASE 3 — Journey Traffic Leak Analysis",
    ])

    with c1:
        render_case_01()

    with c2:
        render_case_02()

    with c3:
        render_case_03()
