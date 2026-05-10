import importlib.util
from pathlib import Path
import streamlit as st

BASE_DIR = Path(__file__).resolve().parent / "case_02_branding_sections"


def load_component(filename: str, function_name: str):
    module_path = BASE_DIR / filename
    spec = importlib.util.spec_from_file_location(filename, module_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return getattr(module, function_name)


render_swot_cards = load_component("swot_cards.py", "render_swot_cards")
render_market_positioning = load_component("market_positioning.py", "render_market_positioning")
render_brand_positioning_communication = load_component("brand_positioning_communication.py", "render_brand_positioning_communication")


def render():
    st.markdown(
        """
        <div style="text-align:center;padding:18px 12px 8px 12px;margin-top:6px;">
            <div style="font-size:15px;color:#facc15;font-weight:900;margin-bottom:12px;">
                โจทย์: สร้าง Branding + หา Lead จริง
            </div>
            <div class="title" style="font-size:34px;margin-bottom:14px;">
                บริษัทอสังหาริมทรัพย์
            </div>
            <div class="body" style="font-size:15px;color:#d7e8dd;max-width:760px;margin:0 auto;line-height:1.8;">
                <b>กิจการ:</b> Real Estate
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    render_swot_cards()
    render_market_positioning()

    brand_tab = st.tabs(["Brand Positioning & Communication"])[0]
    with brand_tab:
        render_brand_positioning_communication()
