import streamlit as st


def render_customer_segment():
    st.markdown(
        """
        <div style="margin-top:18px;padding:26px;border-radius:22px;border:1px dashed rgba(82,255,154,.18);background:rgba(255,255,255,.018);text-align:center;">
          <div style="font-size:13px;font-weight:950;letter-spacing:.16em;text-transform:uppercase;color:#52ff9a;margin-bottom:12px;">
            Customer Segment
          </div>
          <div style="font-size:14px;color:#bfd1c5;line-height:1.7;">
            Coming Soon
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
