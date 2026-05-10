import streamlit as st


def render():
    st.markdown(
        """
        <div class="section" style="padding:22px 24px;">
          <div class="num">CASE 1</div>
          <div class="title" style="font-size:24px;margin-bottom:8px;">Performance Marketing Audit</div>
          <div class="body" style="font-size:14.5px;line-height:1.65;color:#9fb5a8;">
            Case content placeholder. This page will contain the full audit story, data signals, funnel diagnosis, root cause, and action plan.
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
