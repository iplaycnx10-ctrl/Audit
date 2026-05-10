import importlib.util
from pathlib import Path
import streamlit as st

BASE_DIR = Path(__file__).resolve().parent


def load_component(relative_path: str, module_key: str, function_name: str):
    module_path = BASE_DIR / relative_path
    spec = importlib.util.spec_from_file_location(module_key, module_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return getattr(module, function_name)


render_segment_cards = load_component(
    "communication_strategy_segments/segment_cards.py",
    "segment_cards",
    "render_segment_cards"
)


def render_communication_strategy():
    st.markdown(
        """
        <div style="max-width:860px;margin:16px auto 0 auto;padding:22px 24px;border-radius:22px;border:1px solid rgba(82,255,154,.20);background:rgba(11,26,18,.66);box-shadow:0 14px 44px rgba(0,0,0,.18);">
          <div style="font-size:10px;letter-spacing:.24em;text-transform:uppercase;color:#52ff9a;font-weight:950;margin-bottom:8px;">
            Communication Strategy
          </div>
          <div style="font-size:24px;font-weight:950;color:#fff;letter-spacing:-.4px;margin-bottom:16px;line-height:1.25;">
            Customer Segment & Communication Insight
          </div>

          <div style="padding:20px 22px;border-radius:18px;border:1px solid rgba(82,255,154,.16);background:rgba(255,255,255,.028);">
            <div style="font-size:17px;font-weight:950;color:#fff;margin-bottom:12px;">
              แนวทางการทำการตลาดสำหรับพื้นที่เช่า
            </div>
            <p style="font-size:14px;line-height:1.72;color:#d7e8dd;margin:0 0 10px 0;">
              การทำการตลาดสำหรับพื้นที่เช่าไม่ควรมองผู้เช่าทุกกลุ่มเป็นกลุ่มเดียวกัน เพราะแต่ละกลุ่มมีมูลค่าทางธุรกิจ เหตุผลในการตัดสินใจ และระยะเวลาปิดการขายไม่เหมือนกัน
            </p>
            <p style="font-size:14px;line-height:1.72;color:#d7e8dd;margin:0 0 10px 0;">
              กลุ่มเช่าตึก / ตึกพาณิชย์ เป็นกลุ่มที่มีมูลค่าระยะยาวสูงกว่า แต่ต้องใช้เวลาในการสร้างความเชื่อมั่นมากกว่า การสื่อสารจึงไม่ควรเป็นเพียงการลงรูปพื้นที่ว่าง แต่ควรนำเสนอให้เห็นว่า <b>“ทำเลนี้เหมาะกับธุรกิจของเขาอย่างไร”</b>
            </p>
            <p style="font-size:14px;line-height:1.72;color:#d7e8dd;margin:0;">
              ดังนั้นแนวทางการซื้อสื่อควรทำมากกว่าการประกาศว่า <b>“มีพื้นที่ให้เช่า”</b> แต่ควรออกแบบ Message ให้ตรงกับบทบาทของผู้เช่าแต่ละกลุ่ม ทั้งกลุ่มที่สร้าง LTV ระยะยาว และกลุ่มที่ช่วยเติม Cashflow ระหว่างทาง
            </p>
          </div>

          <div style="margin-top:14px;padding:12px 16px;border-left:4px solid #52ff9a;border-radius:14px;background:rgba(82,255,154,.08);color:#effff5;font-size:13.5px;font-weight:850;line-height:1.55;">
            Core Idea: ไม่ได้ขายแค่พื้นที่ว่าง แต่ต้องสื่อสารว่า “พื้นที่นี้ช่วยให้ธุรกิจของผู้เช่าเติบโตได้อย่างไร”
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    render_segment_cards()
