import importlib.util
from pathlib import Path

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
    render_intro_hero()
