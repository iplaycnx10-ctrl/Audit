import streamlit as st


def render():
    st.markdown(
        """
        <div style="font-size:13px;font-weight:950;letter-spacing:.16em;text-transform:uppercase;color:#52ff9a;margin:14px 0 10px 0;">
          ประเมิน Volume + Interest + Intent ก่อน
        </div>
        """,
        unsafe_allow_html=True,
    )

    left_col, right_col = st.columns(2)

    with left_col:
        st.markdown(
            """
            <div style="display:grid;grid-template-columns:1fr;gap:13px;margin-top:12px;">
              <div style="padding:17px 18px;border-radius:20px;border:1px solid rgba(82,255,154,.18);background:linear-gradient(135deg,rgba(255,255,255,.045),rgba(255,255,255,.018));min-height:116px;box-sizing:border-box;display:grid;grid-template-columns:118px 34px 1fr;gap:12px;align-items:center;box-shadow:0 14px 34px rgba(0,0,0,.10);">
                <div>
                  <div style="font-size:10px;color:#9fb5a8;font-weight:950;letter-spacing:.16em;text-transform:uppercase;margin-bottom:10px;">CTR</div>
                  <div style="font-size:25px;color:#fff;font-weight:950;line-height:1;">0.74%</div>
                </div>
                <div style="font-size:18px;color:#52ff9a;font-weight:950;text-align:center;">→</div>
                <div style="font-size:12.3px;color:#bfd1c5;line-height:1.62;">คุณภาพของรูปภาพหรือวิดีโอยังไม่สามารถดึงความสนใจของกลุ่มเป้าหมายได้มากพอ ทำให้ผู้ชมยังไม่เกิดความสนใจต่อบริการเท่าที่ควร</div>
              </div>
              <div style="padding:17px 18px;border-radius:20px;border:1px solid rgba(82,255,154,.18);background:linear-gradient(135deg,rgba(255,255,255,.045),rgba(255,255,255,.018));min-height:116px;box-sizing:border-box;display:grid;grid-template-columns:118px 34px 1fr;gap:12px;align-items:center;box-shadow:0 14px 34px rgba(0,0,0,.10);">
                <div>
                  <div style="font-size:10px;color:#9fb5a8;font-weight:950;letter-spacing:.16em;text-transform:uppercase;margin-bottom:10px;">CPM</div>
                  <div style="font-size:25px;color:#fff;font-weight:950;line-height:1;">฿248</div>
                </div>
                <div style="font-size:18px;color:#52ff9a;font-weight:950;text-align:center;">→</div>
                <div style="font-size:12.3px;color:#bfd1c5;line-height:1.62;">ตลาดมีการแข่งขันค่อนข้างสูง และมีผู้ลงโฆษณาในกลุ่มบริการลักษณะเดียวกันจำนวนมาก ส่งผลให้ต้นทุนการเข้าถึงสูงขึ้น</div>
              </div>
              <div style="padding:17px 18px;border-radius:20px;border:1px solid rgba(82,255,154,.18);background:linear-gradient(135deg,rgba(255,255,255,.045),rgba(255,255,255,.018));min-height:116px;box-sizing:border-box;display:grid;grid-template-columns:118px 34px 1fr;gap:12px;align-items:center;box-shadow:0 14px 34px rgba(0,0,0,.10);">
                <div>
                  <div style="font-size:10px;color:#9fb5a8;font-weight:950;letter-spacing:.16em;text-transform:uppercase;margin-bottom:10px;">Reach</div>
                  <div style="font-size:25px;color:#fff;font-weight:950;line-height:1;">186,420</div>
                </div>
                <div style="font-size:18px;color:#52ff9a;font-weight:950;text-align:center;">→</div>
                <div style="font-size:12.3px;color:#bfd1c5;line-height:1.62;">แม้โฆษณาจะเข้าถึงผู้คนได้จำนวนมาก แต่ยังพบว่ากลุ่มที่เข้าถึงส่วนใหญ่ไม่ได้มีความต้องการตรงกับบริการมากพอ</div>
              </div>
              <div style="padding:17px 18px;border-radius:20px;border:1px solid rgba(82,255,154,.18);background:linear-gradient(135deg,rgba(255,255,255,.045),rgba(255,255,255,.018));min-height:116px;box-sizing:border-box;display:grid;grid-template-columns:118px 34px 1fr;gap:12px;align-items:center;box-shadow:0 14px 34px rgba(0,0,0,.10);">
                <div>
                  <div style="font-size:10px;color:#9fb5a8;font-weight:950;letter-spacing:.16em;text-transform:uppercase;margin-bottom:10px;">Frequency</div>
                  <div style="font-size:25px;color:#fff;font-weight:950;line-height:1;">5.6</div>
                </div>
                <div style="font-size:18px;color:#52ff9a;font-weight:950;text-align:center;">→</div>
                <div style="font-size:12.3px;color:#bfd1c5;line-height:1.62;">ผู้ชม 1 คน เห็นโฆษณาซ้ำเฉลี่ยมากกว่า 5 ครั้ง แต่ยังไม่เกิดการตอบสนองหรือความสนใจเพิ่มเติม</div>
              </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with right_col:
        st.markdown(
            """
            <div style="min-height:512px;margin-top:12px;border-radius:20px;border:1px dashed rgba(82,255,154,.16);background:rgba(255,255,255,.015);"></div>
            """,
            unsafe_allow_html=True,
        )
