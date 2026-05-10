import importlib.util
from pathlib import Path

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
    render_performance_audit()
