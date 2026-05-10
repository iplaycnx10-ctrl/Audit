import streamlit as st


def render():
    st.markdown(
        """
        <div style="display:flex;justify-content:center;gap:10px;flex-wrap:nowrap;background:#030504;border:1px solid rgba(255,255,255,.10);border-radius:14px;padding:8px 10px;margin:8px auto 18px auto;max-width:900px;box-sizing:border-box;">
          <div style="height:30px;display:flex;align-items:center;padding:0 13px;border-radius:10px;border:1px solid rgba(250,204,21,.55);background:rgba(250,204,21,.14);color:#facc15;font-size:12px;font-weight:900;white-space:nowrap;">CASE 1 — Performance Marketing Audit</div>
          <div style="height:30px;display:flex;align-items:center;padding:0 13px;border-radius:10px;border:1px solid rgba(255,255,255,.08);background:rgba(255,255,255,.035);color:#f8fafc;font-size:12px;font-weight:850;white-space:nowrap;">CASE 2 — Branding Strategy Analysis</div>
          <div style="height:30px;display:flex;align-items:center;padding:0 13px;border-radius:10px;border:1px solid rgba(255,255,255,.08);background:rgba(255,255,255,.035);color:#f8fafc;font-size:12px;font-weight:850;white-space:nowrap;">CASE 3 — Journey Traffic Leak Analysis</div>
        </div>
        """,
        unsafe_allow_html=True,
    )
