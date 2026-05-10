import importlib.util
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
ROOT_DIR = BASE_DIR.parent


def load_render(base_dir: Path, relative_path: str, module_key: str):
    module_path = base_dir / relative_path
    spec = importlib.util.spec_from_file_location(module_key, module_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.render


render_case_nav = load_render(
    ROOT_DIR,
    "navigation/case_nav.py",
    "case_nav",
)

render_case_01 = load_render(
    BASE_DIR,
    "performance_marketing_audit_cases/case_01_performance_marketing_audit.py",
    "case_01_performance_marketing_audit",
)

render_case_02 = load_render(
    BASE_DIR,
    "performance_marketing_audit_cases/case_02_branding_strategy_analysis.py",
    "case_02_branding_strategy_analysis",
)

render_case_03 = load_render(
    BASE_DIR,
    "performance_marketing_audit_cases/case_03_journey_traffic_leak_analysis.py",
    "case_03_journey_traffic_leak_analysis",
)


def render():
    selected_case = render_case_nav()

    if selected_case == "case_01":
        render_case_01()

    elif selected_case == "case_02":
        render_case_02()

    elif selected_case == "case_03":
        render_case_03()
