import streamlit as st


HERO_IMAGE_PATH = "assets/hero_profile.png.png"


def render():
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
        st.markdown(
            """
            <div style="height:520px;border:1px solid rgba(82,255,154,.22);border-radius:36px;background:radial-gradient(circle at center,rgba(82,255,154,.14),rgba(255,255,255,.035));display:flex;align-items:flex-end;justify-content:center;overflow:hidden;padding:0 18px;box-shadow:0 28px 90px rgba(0,0,0,.32);">
            """,
            unsafe_allow_html=True,
        )
        st.image(HERO_IMAGE_PATH, use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)
