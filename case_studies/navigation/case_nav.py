import streamlit as st


def render():
    st.markdown(
        """
        <div style="display:flex;justify-content:center;gap:10px;flex-wrap:nowrap;background:#020302;border:1px solid rgba(250,204,21,.34);border-radius:14px;padding:8px 10px;margin:8px auto 18px auto;max-width:900px;box-sizing:border-box;box-shadow:0 10px 28px rgba(0,0,0,.22);">
          <div style="height:30px;display:flex;align-items:center;padding:0 13px;border-radius:10px;border:1px solid rgba(250,204,21,.72);background:rgba(250,204,21,.13);color:#facc15;font-size:12px;font-weight:900;white-space:nowrap;">CASE 1 — Performance Marketing Audit</div>
          <div style="height:30px;display:flex;align-items:center;padding:0 13px;border-radius:10px;border:1px solid rgba(250,204,21,.22);background:#050806;color:#f8fafc;font-size:12px;font-weight:850;white-space:nowrap;">CASE 2 — Branding Strategy Analysis</div>
          <div style="height:30px;display:flex;align-items:center;padding:0 13px;border-radius:10px;border:1px solid rgba(250,204,21,.22);background:#050806;color:#f8fafc;font-size:12px;font-weight:850;white-space:nowrap;">CASE 3 — Journey Traffic Leak Analysis</div>
        </div>
        """,
        unsafe_allow_html=True,
    )
