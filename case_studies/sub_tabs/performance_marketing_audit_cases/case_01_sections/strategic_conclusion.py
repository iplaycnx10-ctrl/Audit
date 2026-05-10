import streamlit as st


def render():
    st.markdown(
        """
        <div style="margin-top:18px;padding:28px;border-radius:22px;border:1px dashed rgba(250,204,21,.18);background:rgba(255,255,255,.018);text-align:center;">
          <div style="font-size:13px;font-weight:950;letter-spacing:.16em;text-transform:uppercase;color:#facc15;margin-bottom:12px;">
            Strategic Conclusion
          </div>
          <div style="font-size:14px;color:#bfd1c5;line-height:1.7;">
            Coming Soon
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
