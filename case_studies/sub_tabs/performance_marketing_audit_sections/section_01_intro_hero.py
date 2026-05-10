import streamlit as st


def render():
    st.markdown(
        """
        <div class="section" style="padding:24px 26px;">
          <div class="num">🟢 Section 1 — Intro Hero</div>
          <div class="title" style="font-size:28px;margin-bottom:10px;">Performance Marketing Audit</div>
          <div class="body" style="font-size:15.5px;line-height:1.65;max-width:820px;">
            Identifying where businesses are leaking budget through data, funnel analysis, and performance signals.
          </div>
          <div class="body" style="font-size:14px;line-height:1.65;max-width:840px;color:#9fb5a8;margin-top:14px;">
            A strategic analysis framework focused on ROAS efficiency, funnel leakage, audience quality, creative fatigue, and growth bottlenecks.
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
