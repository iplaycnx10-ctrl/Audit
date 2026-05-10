import streamlit as st


HERO_IMAGE_PATH = "assets/hero_profile.png.png"


def render():
    st.markdown(
        """
        <div style="height:24px;"></div>
        """,
        unsafe_allow_html=True,
    )

    left, right = st.columns([1.05, 0.95], vertical_alignment="top")

    with left:
        st.markdown(
            """
            <div class="cover" style="min-height:430px;margin-top:0;">
              <div class="kicker" style="margin-bottom:70px;">Strategic Portfolio</div>
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
            <div style="height:430px;display:flex;align-items:flex-start;justify-content:center;overflow:visible;padding:0 10px;margin-top:0;">
            """,
            unsafe_allow_html=True,
        )
        st.image(HERO_IMAGE_PATH, use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)
