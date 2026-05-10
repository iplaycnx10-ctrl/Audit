import streamlit as st


def render_segment_cards():
    html = """
    <div style="max-width:860px;margin:14px auto 0 auto;">
      <div style="display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:14px;">
        <div style="padding:18px 20px;border-radius:18px;border:1px solid rgba(250,204,21,.20);background:rgba(250,204,21,.045);min-height:150px;">
          <div style="font-size:10px;letter-spacing:.18em;text-transform:uppercase;color:#facc15;font-weight:950;margin-bottom:10px;">Segment 01</div>
          <div style="font-size:17px;font-weight:950;color:#fff;line-height:1.35;margin-bottom:10px;">Motivation & Trust Segment</div>
          <div style="font-size:13.5px;line-height:1.65;color:#d7e8dd;">กลุ่มที่ต้องสร้างแรงจูงใจ / ความเชื่อมั่น / LTV ระยะยาว เช่น ผู้เช่าตึกหรือธุรกิจที่ต้องใช้ทำเลเป็นฐานเติบโต เหมาะกับ Message ที่เน้น Location, Business Potential และ Investment Confidence</div>
        </div>

        <div style="padding:18px 20px;border-radius:18px;border:1px solid rgba(82,255,154,.18);background:rgba(255,255,255,.028);min-height:150px;">
          <div style="font-size:10px;letter-spacing:.18em;text-transform:uppercase;color:#52ff9a;font-weight:950;margin-bottom:10px;">Segment 02</div>
          <div style="font-size:17px;font-weight:950;color:#fff;line-height:1.35;margin-bottom:10px;">Lead Capture Segment</div>
          <div style="font-size:13.5px;line-height:1.65;color:#d7e8dd;">กลุ่มที่เน้นสร้าง Lead / ปิดไว / หมุน Cashflow เช่น ร้านค้า บูธ รถเข็น Pop-up Store และลานกิจกรรม เหมาะกับ Message ที่ชัด กระตุ้นการติดต่อ และลด friction ในการตัดสินใจ</div>
        </div>
      </div>

      <div style="display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:14px;">
        <div>
          <div style="width:1px;height:24px;background:rgba(250,204,21,.55);margin:0 auto;"></div>
          <div style="padding:16px 17px;border-radius:16px;background:rgba(250,204,21,.035);border:1px solid rgba(250,204,21,.16);">
            <div style="font-size:10px;letter-spacing:.16em;text-transform:uppercase;color:#facc15;font-weight:950;margin-bottom:8px;">กลยุทธ์</div>
            <div style="font-size:16px;font-weight:950;color:#fff;margin-bottom:10px;">Motivation & Trust Segment</div>
            <div style="font-size:13px;line-height:1.62;color:#d7e8dd;margin-bottom:10px;">กลุ่มนี้ควรใช้โฆษณาแบบ <b>2 Funnel</b> คือใช้คอนเทนต์ช่วงบนเพื่อสร้างการรับรู้ ความน่าเชื่อถือ และทำให้เห็นโอกาสทางธุรกิจ ก่อนตามด้วยคอนเทนต์ช่วงล่างเพื่อกระตุ้นให้กลับมาพิจารณาและติดต่อสอบถาม</div>
            <div style="font-size:13px;line-height:1.62;color:#d7e8dd;margin-bottom:10px;">แนวทางหลักคือ <b>เห็นซ้ำ → เข้าใจมากขึ้น → เชื่อมั่นมากขึ้น → พร้อมทักมากขึ้น</b> เพราะกลุ่มเช่าตึกมักไม่ได้ตัดสินใจทันที แต่ต้องใช้เวลาในการเห็นความคุ้มค่าและความน่าเชื่อถือของพื้นที่</div>
            <div style="font-size:13px;line-height:1.62;color:#fef3c7;background:rgba(250,204,21,.070);padding:10px 11px;border-radius:12px;margin-bottom:8px;"><b>1. Location-Based Business</b><br>ใช้กลยุทธ์สื่อสารแบบ <b>Location Opportunity</b> เน้นทำเล คนผ่าน การมองเห็น และโอกาสในการสร้างยอดขายจากหน้าร้าน<br><br><b>Hook:</b> “ทำเลที่ไม่ได้แค่ตั้งร้าน แต่ช่วยเพิ่มโอกาสให้คนเห็นและเข้าถึงธุรกิจมากขึ้น”</div>
            <div style="font-size:13px;line-height:1.62;color:#fef3c7;background:rgba(250,204,21,.070);padding:10px 11px;border-radius:12px;"><b>2. Office / Online-Based Business</b><br>ใช้กลยุทธ์สื่อสารแบบ <b>Business Base & Trust</b> เน้นภาพลักษณ์ ความน่าเชื่อถือ ความคุ้มค่า และการใช้พื้นที่เป็นฐานรองรับการเติบโต<br><br><b>Hook:</b> “พื้นที่ที่ช่วยให้ธุรกิจดูเป็นระบบ น่าเชื่อถือ และพร้อมเติบโตในระยะยาว”</div>
          </div>
        </div>

        <div>
          <div style="width:1px;height:24px;background:rgba(82,255,154,.45);margin:0 auto;"></div>
          <div style="padding:16px 17px;border-radius:16px;background:rgba(82,255,154,.030);border:1px solid rgba(82,255,154,.15);">
            <div style="font-size:10px;letter-spacing:.16em;text-transform:uppercase;color:#52ff9a;font-weight:950;margin-bottom:8px;">กลยุทธ์</div>
            <div style="font-size:16px;font-weight:950;color:#fff;margin-bottom:10px;">Lead Capture Segment</div>
            <div style="font-size:13px;line-height:1.62;color:#d7e8dd;margin-bottom:10px;">กลุ่มนี้ควรใช้โฆษณาแบบ <b>Lead Focus</b> เพราะเป็นกลุ่มที่ตัดสินใจได้เร็วกว่า ต้นทุนในการเริ่มเช่าหรือทดลองพื้นที่ไม่สูงเท่ากลุ่มเช่าตึก จึงควรสื่อสารให้เข้าใจง่าย เห็นราคา เห็นพื้นที่ และทักสอบถามได้ทันที</div>
            <div style="font-size:13px;line-height:1.62;color:#d7e8dd;margin-bottom:10px;">สามารถใช้ <b>LINE OA / Inbox Flow</b> ช่วยตอบคำถามเบื้องต้น เช่น ราคา พื้นที่ว่าง เงื่อนไขการเช่า และวันเริ่มใช้งาน เพื่อคัดกรอง Lead และลดภาระการตอบซ้ำ</div>
            <div style="font-size:13px;line-height:1.62;color:#d9ffe8;background:rgba(82,255,154,.065);padding:10px 11px;border-radius:12px;"><b>3. General Space / Short-Term Rental</b><br>ทำการตลาดแบบเน้น <b>“พื้นที่พร้อมใช้ ปิดง่าย เริ่มไว”</b> ให้ผู้เช่าเห็นว่าสามารถนำพื้นที่ไปใช้ขายของ ออกบูธ ทำกิจกรรม หรือทดลองตลาดได้ทันที โดยไม่ต้องผูกมัดระยะยาว<br><br>“พื้นที่เช่าพร้อมขาย เหมาะสำหรับร้านค้า บูธ กิจกรรม และแบรนด์ที่ต้องการทดลองตลาดหรือเพิ่มจุดขายแบบเริ่มได้ทันที”</div>
          </div>
        </div>
      </div>
    </div>
    """
    st.html(html)
