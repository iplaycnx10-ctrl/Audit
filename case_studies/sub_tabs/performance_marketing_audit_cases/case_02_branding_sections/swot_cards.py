import streamlit as st


def render_swot_cards():
    st.markdown(
        """
        <style>
        .swot-wrap{
            display:grid;
            grid-template-columns:repeat(4,1fr);
            gap:14px;
            margin-top:22px;
            margin-bottom:18px;
        }
        .swot-card{
            border-radius:18px;
            border:1px solid rgba(255,255,255,.10);
            background:linear-gradient(135deg,rgba(255,255,255,.045),rgba(255,255,255,.018));
            overflow:hidden;
        }
        .swot-card details{
            padding:0;
        }
        .swot-card summary{
            list-style:none;
            cursor:pointer;
            padding:16px 18px;
            font-size:13px;
            font-weight:900;
            color:#fff;
            display:flex;
            align-items:center;
            justify-content:space-between;
            letter-spacing:.02em;
        }
        .swot-card summary::-webkit-details-marker{display:none;}
        .swot-content{
            padding:0 18px 18px 18px;
            font-size:12px;
            line-height:1.72;
            color:#d7e8dd;
        }
        .swot-s{border-color:rgba(82,255,154,.24);}
        .swot-w{border-color:rgba(239,68,68,.24);}
        .swot-o{border-color:rgba(250,204,21,.24);}
        .swot-t{border-color:rgba(249,115,22,.24);}
        </style>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="swot-wrap">

            <div class="swot-card swot-s">
                <details>
                    <summary>✅ Strengths <span>+</span></summary>
                    <div class="swot-content">
                    • แบรนด์อสังหาคอมมูนิตี้เชิงพาณิชย์ที่คนเชียงใหม่รู้จักดี มีหลายโครงการทั่วเมือง<br><br>
                    • ทำเลส่วนใหญ่เกาะเส้นเศรษฐกิจและ Community ระดับกำลังซื้อสูง<br><br>
                    • ภาพลักษณ์โครงการค่อนข้าง Modern / Premium เหมาะกับธุรกิจยุคใหม่<br><br>
                    • มีฐาน Traffic และ Community เดิมอยู่แล้วจากลูกบ้านและธุรกิจในโครงการ<br><br>
                    • จุดแข็งเรื่อง “Business Community” ชัดกว่าคู่แข่งอสังหาทั่วไป
                    </div>
                </details>
            </div>

            <div class="swot-card swot-w">
                <details>
                    <summary>❌ Weaknesses <span>+</span></summary>
                    <div class="swot-content">
                    • คนยังมองว่าเป็น “โครงการอาคารพาณิชย์” มากกว่า Lifestyle Brand<br><br>
                    • Branding ยังเน้นขายพื้นที่ มากกว่าสร้าง Emotional Connection<br><br>
                    • บางโครงการยังขาดกิจกรรมหรือ Experience ที่ทำให้คนอยากแวะมา<br><br>
                    • หาก Tenant Mix ไม่แข็ง อาจทำให้ภาพรวมโครงการดูไม่ Premium เท่าที่ควร
                    </div>
                </details>
            </div>

            <div class="swot-card swot-o">
                <details>
                    <summary>🔥 Opportunities <span>+</span></summary>
                    <div class="swot-content">
                    • เชียงใหม่กำลังโตด้าน Lifestyle, Wellness, Cafe และ Digital Nomad<br><br>
                    • สามารถพัฒนาเป็น Community Hub / Lifestyle Destination ได้<br><br>
                    • ดึงร้าน Premium, Co-working, Wellness, Cafe หรือธุรกิจ Creative เข้ามาเพิ่มได้<br><br>
                    • Event Marketing และ Community Activity สามารถเพิ่ม Traffic และ Brand Value ได้มหาศาล<br><br>
                    • สามารถ Rebrand จาก “Commercial Project” → “Urban Lifestyle Ecosystem” ได้ 🔥
                    </div>
                </details>
            </div>

            <div class="swot-card swot-t">
                <details>
                    <summary>⚠️ Threats <span>+</span></summary>
                    <div class="swot-content">
                    • คู่แข่งอสังหายุคใหม่เริ่มเล่น Branding + Experience มากขึ้น<br><br>
                    • ผู้บริโภคยุคใหม่เลือกพื้นที่ที่ “มีชีวิต” มากกว่าแค่ทำเล<br><br>
                    • หากเศรษฐกิจหรือท่องเที่ยวชะลอ อาจกระทบ Tenant และ Traffic<br><br>
                    • ถ้าขยายหลายโครงการเกินไปโดยไม่คุมภาพลักษณ์ อาจทำให้แบรนด์ Dilute
                    </div>
                </details>
            </div>

        </div>
        """,
        unsafe_allow_html=True,
    )
