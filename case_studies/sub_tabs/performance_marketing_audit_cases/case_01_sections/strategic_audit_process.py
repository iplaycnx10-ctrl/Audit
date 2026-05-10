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
            <div style="display:grid;grid-template-columns:1fr;gap:13px;margin-top:12px;">
              <div style="min-height:242px;border-radius:20px;border:1px solid rgba(82,255,154,.18);background:linear-gradient(135deg,rgba(255,255,255,.045),rgba(255,255,255,.018));padding:22px 24px;box-sizing:border-box;box-shadow:0 14px 34px rgba(0,0,0,.10);">
                <div style="font-size:12px;color:#52ff9a;font-weight:950;letter-spacing:.16em;text-transform:uppercase;margin-bottom:16px;">Insight</div>
                <div style="font-size:13px;color:#d7e8dd;line-height:1.75;margin-bottom:16px;">
                  แม้แคมเปญจะสามารถเข้าถึงผู้คนได้ในวงกว้าง แต่คุณภาพของ Traffic ที่ได้รับยังไม่สอดคล้องกับกลุ่มลูกค้าที่มีความต้องการใช้บริการจริง โดยพบว่าโฆษณายังไม่สามารถสร้างแรงจูงใจหรือดึงความสนใจได้มากพอที่จะผลักดันให้เกิดการตัดสินใจใช้งานบริการ
                </div>
                <div style="font-size:13px;color:#bfd1c5;line-height:1.75;margin-bottom:18px;">
                  หลักฐานสำคัญคือ ผู้ชม 1 คน เห็นโฆษณาซ้ำเฉลี่ยมากกว่า 5 ครั้ง แต่ยังไม่เกิดการตอบสนองเพิ่มเติม สะท้อนว่า Audience ที่เข้าถึงอาจยังไม่ตรงกับความต้องการของธุรกิจ และ Creative ที่ใช้ยังไม่สามารถสร้าง Intent ได้ดีเพียงพอ
                </div>
                <div style="font-size:12px;color:#9fb5a8;line-height:1.7;padding-top:16px;border-top:1px solid rgba(82,255,154,.12);">
                  <b style="color:#facc15;">หมายเหตุ:</b> การประเมินนี้เป็นเพียงการวิเคราะห์เบื้องต้นในส่วนของ Traffic Signal เท่านั้น โดยยังไม่ได้เปรียบเทียบกับข้อมูลเชิงลึกในส่วนของ Funnel, Conversion และ Performance Efficiency ในขั้นตอนถัดไป
                </div>
              </div>

              <div style="min-height:242px;border-radius:20px;border:1px solid rgba(250,204,21,.20);background:linear-gradient(135deg,rgba(250,204,21,.055),rgba(255,255,255,.018));padding:22px 24px;box-sizing:border-box;box-shadow:0 14px 34px rgba(0,0,0,.10);">
                <div style="font-size:12px;color:#facc15;font-weight:950;letter-spacing:.16em;text-transform:uppercase;margin-bottom:16px;">สรุปปัญหาที่ตรวจพบ</div>
                <div style="font-size:13px;color:#d7e8dd;line-height:1.75;margin-bottom:15px;">
                  ลักษณะการรันแคมเปญในปัจจุบันเป็นการกระจายโฆษณาในวงกว้าง เพื่อเน้นการเข้าถึง (Reach) เป็นหลัก แต่ยังไม่ได้มีการคัดกรองกลุ่มเป้าหมายที่มีความต้องการใช้งานบริการอย่างชัดเจนตั้งแต่ต้นทาง
                </div>
                <div style="font-size:13px;color:#bfd1c5;line-height:1.75;margin-bottom:15px;">
                  รวมถึง Creative ที่ใช้ยังไม่สามารถทำหน้าที่คัดกรองหรือกระตุ้น Intent ของกลุ่มลูกค้าได้มากพอ ส่งผลให้ระบบสามารถสร้าง Reach ได้ในปริมาณสูง แต่คุณภาพของ Traffic ที่ได้รับยังไม่สอดคล้องกับกลุ่มลูกค้าที่มีโอกาสเปลี่ยนเป็นลูกค้าจริง
                </div>
                <div style="font-size:13px;color:#9fb5a8;line-height:1.75;">
                  นอกจากนี้ยังพบว่าแคมเปญมีการรันต่อเนื่องเป็นเวลานานโดยอิงจากตัวเลข Reach เป็นหลัก ทั้งที่ในความเป็นจริง Reach ที่เพิ่มขึ้นไม่ได้สะท้อนถึงคุณภาพของ Audience หรือความสนใจที่แท้จริงต่อบริการ
                </div>
              </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
