import streamlit as st


def render():
    st.markdown(
        """
        <div style="height:24px;"></div>
        """,
        unsafe_allow_html=True,
    )

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
