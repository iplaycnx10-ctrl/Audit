import streamlit as st


def render_swot_cards():
    st.markdown(
        """
        <style>
        div[data-testid="stExpander"]{
            min-height: 352px !important;
            border-radius:18px !important;
            border:1px solid rgba(255,255,255,.12) !important;
            background:linear-gradient(135deg,rgba(255,255,255,.045),rgba(255,255,255,.018)) !important;
            overflow:hidden !important;
            box-shadow:0 14px 34px rgba(0,0,0,.10) !important;
        }
        div[data-testid="stExpander"] details{
            min-height: 352px !important;
        }
        div[data-testid="stExpander"] summary{
            min-height: 42px !important;
            background:rgba(255,255,255,.035) !important;
            border-bottom:1px solid rgba(255,255,255,.08) !important;
            font-size:13px !important;
            font-weight:900 !important;
            color:#f8fafc !important;
        }
        div[data-testid="stExpander"] summary:hover{
            background:rgba(250,204,21,.075) !important;
            color:#facc15 !important;
        }
        div[data-testid="stExpander"] summary p,
        div[data-testid="stExpander"] summary span,
        div[data-testid="stExpander"] summary svg{
            color:#f8fafc !important;
            fill:#f8fafc !important;
        }
        div[data-testid="stExpander"] summary:hover p,
        div[data-testid="stExpander"] summary:hover span,
        div[data-testid="stExpander"] summary:hover svg{
            color:#facc15 !important;
            fill:#facc15 !important;
        }
        div[data-testid="stExpander"] div[data-testid="stMarkdownContainer"] p,
        div[data-testid="stExpander"] div[data-testid="stMarkdownContainer"] li{
            font-size:12.5px !important;
            line-height:1.7 !important;
            color:#d7e8dd !important;
        }
        div[data-testid="stExpander"] ul{
            padding-left:18px !important;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    col1, col2, col3, col4 = st.columns(4, gap="small")

    with col1:
        with st.expander("✅ Strengths", expanded=True):
            st.markdown(
                """
                - แบรนด์อสังหาคอมมูนิตี้เชิงพาณิชย์ที่คนเชียงใหม่รู้จักดี มีหลายโครงการทั่วเมือง
                - ทำเลส่วนใหญ่เกาะเส้นเศรษฐกิจและ Community ระดับกำลังซื้อสูง
                - ภาพลักษณ์โครงการค่อนข้าง Modern / Premium เหมาะกับธุรกิจยุคใหม่
                - มีฐาน Traffic และ Community เดิมอยู่แล้วจากลูกบ้านและธุรกิจในโครงการ
                - จุดแข็งเรื่อง “Business Community” ชัดกว่าคู่แข่งอสังหาทั่วไป
                """
            )

    with col2:
        with st.expander("❌ Weaknesses", expanded=True):
            st.markdown(
                """
                - คนยังมองว่าเป็น “โครงการอาคารพาณิชย์” มากกว่า Lifestyle Brand
                - Branding ยังเน้นขายพื้นที่ มากกว่าสร้าง Emotional Connection
                - บางโครงการยังขาดกิจกรรมหรือ Experience ที่ทำให้คนอยากแวะมา
                - หาก Tenant Mix ไม่แข็ง อาจทำให้ภาพรวมโครงการดูไม่ Premium เท่าที่ควร
                """
            )

    with col3:
        with st.expander("🔥 Opportunities", expanded=True):
            st.markdown(
                """
                - เชียงใหม่กำลังโตด้าน Lifestyle, Wellness, Cafe และ Digital Nomad
                - สามารถพัฒนาเป็น Community Hub / Lifestyle Destination ได้
                - ดึงร้าน Premium, Co-working, Wellness, Cafe หรือธุรกิจ Creative เข้ามาเพิ่มได้
                - Event Marketing และ Community Activity สามารถเพิ่ม Traffic และ Brand Value ได้มหาศาล
                - สามารถ Rebrand จาก “Commercial Project” → “Urban Lifestyle Ecosystem” ได้ 🔥
                """
            )

    with col4:
        with st.expander("⚠️ Threats", expanded=True):
            st.markdown(
                """
                - คู่แข่งอสังหายุคใหม่เริ่มเล่น Branding + Experience มากขึ้น
                - ผู้บริโภคยุคใหม่เลือกพื้นที่ที่ “มีชีวิต” มากกว่าแค่ทำเล
                - หากเศรษฐกิจหรือท่องเที่ยวชะลอ อาจกระทบ Tenant และ Traffic
                - ถ้าขยายหลายโครงการเกินไปโดยไม่คุมภาพลักษณ์ อาจทำให้แบรนด์ Dilute
                """
            )
