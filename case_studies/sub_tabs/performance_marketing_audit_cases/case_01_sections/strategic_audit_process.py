import streamlit as st


def render():
    st.markdown(
        """
        <div style="padding:16px 18px;border-radius:18px;border:1px solid rgba(82,255,154,.16);background:rgba(255,255,255,.025);margin-top:12px;">
          <div style="font-size:13px;font-weight:900;color:#52ff9a;letter-spacing:.12em;text-transform:uppercase;margin-bottom:8px;">Strategic Audit Process</div>
          <div style="font-size:13px;line-height:1.65;color:#9fb5a8;">Coming soon — audit flow, diagnosis steps, and decision logic.</div>
        </div>
        """,
        unsafe_allow_html=True,
    )
