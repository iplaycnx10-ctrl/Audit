import base64
from pathlib import Path

import streamlit as st


HERO_IMAGE_PATH = Path("assets/hero_profile.png.png")


def _image_as_base64(path: Path) -> str:
    if not path.exists():
        return ""
    return base64.b64encode(path.read_bytes()).decode("utf-8")


def render():
    hero_base64 = _image_as_base64(HERO_IMAGE_PATH)

    left, right = st.columns([1.15, 0.85])

    with left:
        st.markdown(
            """
            <div class="cover" style="min-height:520px;">
              <div class="kicker">Strategic Portfolio</div>
              <h1>CHAYANON<br>NANTAVICHARN</h1>
              <div class="role">Performance Marketing &<br>AI Automation Specialist</div>
              <div class="est">ESTABLISHED 2026 | PERFORMANCE-DRIVEN</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with right:
        if hero_base64:
            st.markdown(
                f"""
                <div style="height:520px;border:1px solid rgba(82,255,154,.22);border-radius:36px;background:radial-gradient(circle at center,rgba(82,255,154,.14),rgba(255,255,255,.035));display:flex;align-items:flex-end;justify-content:center;overflow:hidden;padding:0 18px;box-shadow:0 28px 90px rgba(0,0,0,.32);">
                    <img src="data:image/png;base64,{hero_base64}" style="width:100%;max-height:500px;object-fit:contain;object-position:center bottom;display:block;" />
                </div>
                """,
                unsafe_allow_html=True,
            )
        else:
            st.markdown(
                """
                <div style="height:520px;border:1px solid rgba(82,255,154,.22);border-radius:36px;background:radial-gradient(circle at center,rgba(82,255,154,.14),rgba(255,255,255,.035));display:flex;align-items:center;justify-content:center;overflow:hidden;padding:0 18px;box-shadow:0 28px 90px rgba(0,0,0,.32);color:#8ea99a;font-weight:900;text-align:center;line-height:1.7;">
                    Missing hero image<br>assets/hero_profile.png.png
                </div>
                """,
                unsafe_allow_html=True,
            )
