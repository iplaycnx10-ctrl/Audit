import streamlit as st


def render():
    left_col, right_col = st.columns(2)

    with left_col:
        st.markdown(
            """
            <div style="display:grid;grid-template-columns:1fr;gap:12px;margin-top:12px;">
              <div style="padding:14px 16px;border-radius:18px;border:1px solid rgba(82,255,154,.20);background:rgba(255,255,255,.035);min-height:86px;box-sizing:border-box;display:flex;align-items:center;justify-content:space-between;gap:18px;">
                <div style="font-size:11px;color:#9fb5a8;font-weight:900;letter-spacing:.12em;text-transform:uppercase;">CTR</div>
                <div style="font-size:22px;color:#fff;font-weight:950;line-height:1;">0.74%</div>
              </div>
              <div style="padding:14px 16px;border-radius:18px;border:1px solid rgba(82,255,154,.20);background:rgba(255,255,255,.035);min-height:86px;box-sizing:border-box;display:flex;align-items:center;justify-content:space-between;gap:18px;">
                <div style="font-size:11px;color:#9fb5a8;font-weight:900;letter-spacing:.12em;text-transform:uppercase;">CPM</div>
                <div style="font-size:22px;color:#fff;font-weight:950;line-height:1;">฿248</div>
              </div>
              <div style="padding:14px 16px;border-radius:18px;border:1px solid rgba(82,255,154,.20);background:rgba(255,255,255,.035);min-height:86px;box-sizing:border-box;display:flex;align-items:center;justify-content:space-between;gap:18px;">
                <div style="font-size:11px;color:#9fb5a8;font-weight:900;letter-spacing:.12em;text-transform:uppercase;">Reach</div>
                <div style="font-size:22px;color:#fff;font-weight:950;line-height:1;">186,420</div>
              </div>
              <div style="padding:14px 16px;border-radius:18px;border:1px solid rgba(82,255,154,.20);background:rgba(255,255,255,.035);min-height:86px;box-sizing:border-box;display:flex;align-items:center;justify-content:space-between;gap:18px;">
                <div style="font-size:11px;color:#9fb5a8;font-weight:900;letter-spacing:.12em;text-transform:uppercase;">Frequency</div>
                <div style="font-size:22px;color:#fff;font-weight:950;line-height:1;">5.6</div>
              </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with right_col:
        st.markdown(
            """
            <div style="min-height:380px;margin-top:12px;border-radius:18px;border:1px dashed rgba(82,255,154,.16);background:rgba(255,255,255,.015);"></div>
            """,
            unsafe_allow_html=True,
        )
