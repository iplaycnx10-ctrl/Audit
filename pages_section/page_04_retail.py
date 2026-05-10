import plotly.express as px
import streamlit as st
from components.common import metric, section

CHART_BG = "rgba(11,26,18,0)"
PAPER_BG = "rgba(11,26,18,0)"
FONT_COLOR = "#d7e8dd"
GRID_COLOR = "rgba(215,232,221,0.14)"


def style_chart(fig, height=430):
    fig.update_layout(
        height=height,
        template="plotly_dark",
        paper_bgcolor=PAPER_BG,
        plot_bgcolor=CHART_BG,
        font=dict(color=FONT_COLOR),
        title=dict(font=dict(color="#ffffff", size=15), x=0.02),
        margin=dict(l=20, r=20, t=58, b=38),
        legend=dict(font=dict(color=FONT_COLOR)),
    )
    fig.update_xaxes(gridcolor=GRID_COLOR, zerolinecolor=GRID_COLOR, color=FONT_COLOR)
    fig.update_yaxes(gridcolor=GRID_COLOR, zerolinecolor=GRID_COLOR, color=FONT_COLOR)
    return fig


def render(retail_summary, retail_data):
    section(
        "04. STRATEGY: HIGH-VALUE RETAIL",
        "The Hybrid Closing Model",
        "ลักษณะงานที่ทำ<br>> ตรวจสอบความผิดพลาดใน Tracking พฤติกรรมลูกค้า > วางแผนทำแนวทางยิง Ads แบบ Funnel > Direct Creative > บริหารงบโฆษณา > ติดตามผลและรายงานผล > วางแผนตามโครงสร้าง Midday / Double Day / Payday"
    )

    m1, m2, m3, m4 = st.columns(4)
    with m1: metric("Total Spend", f"฿{retail_summary['total_spend']:,.0f}", "งบยิงรวมทุกแคมเปญ")
    with m2: metric("Total Purchase", f"{retail_summary['total_purchase']:,.0f}", "ยอด Purchase รวม")
    with m3: metric("Revenue", f"฿{retail_summary['total_revenue']:,.0f}", "รายได้รวมจาก Ads")
    with m4: metric("Avg ROAS", f"{retail_summary['avg_roas']:.2f}x", "ROAS เฉลี่ยรวม")

    k1, k2, k3, k4 = st.columns(4)
    with k1: metric("Reach", f"{retail_summary['total_reach']:,.0f}", "จำนวน Reach รวม")
    with k2: metric("Impressions", f"{retail_summary['total_impressions']:,.0f}", "Impression รวม")
    with k3: metric("Avg CPR", f"฿{retail_summary['avg_cpr']:,.0f}", "ต้นทุนต่อ Purchase")
    with k4: metric("Avg CTR", f"{retail_summary['avg_ctr_click']:.2f}%", "CTR Click เฉลี่ย")

    st.markdown("<div style='height:22px;'></div>", unsafe_allow_html=True)

    chart_col1, chart_col2 = st.columns(2, gap="large")

    with chart_col1:
        fig_roas = px.bar(
            retail_data.sort_values('ROAS', ascending=False),
            x='Campaign',
            y='ROAS',
            text='ROAS',
            color='ROAS',
            color_continuous_scale='Viridis',
            title='ROAS Performance by Campaign'
        )
        fig_roas.update_traces(texttemplate='%{text:.2f}x', textposition='outside')
        style_chart(fig_roas)
        fig_roas.update_layout(xaxis_title='', coloraxis_showscale=False)
        st.plotly_chart(fig_roas, use_container_width=True)

    with chart_col2:
        fig_cpr = px.bar(
            retail_data.sort_values('CPR'),
            x='Campaign',
            y='CPR',
            text='CPR',
            color='CPR',
            color_continuous_scale='Turbo',
            title='Cost per Purchase Efficiency'
        )
        fig_cpr.update_traces(texttemplate='฿%{text:,.0f}', textposition='outside')
        style_chart(fig_cpr)
        fig_cpr.update_layout(xaxis_title='', coloraxis_showscale=False)
        st.plotly_chart(fig_cpr, use_container_width=True)

    st.markdown("<div style='height:16px;'></div>", unsafe_allow_html=True)

    chart_col3, chart_col4 = st.columns(2, gap="large")

    with chart_col3:
        fig_spend = px.pie(
            retail_data,
            values='Spend',
            names='Campaign',
            hole=.55,
            title='Spend Distribution by Campaign'
        )
        style_chart(fig_spend)
        fig_spend.update_layout(showlegend=True)
        st.plotly_chart(fig_spend, use_container_width=True)

    with chart_col4:
        fig_mix = px.bar(
            retail_data.sort_values('Purchase', ascending=False),
            x='Campaign',
            y=['Purchase', 'ROAS', 'Frequency'],
            barmode='group',
            title='Purchase / ROAS / Frequency Snapshot'
        )
        style_chart(fig_mix)
        fig_mix.update_layout(xaxis_title='')
        st.plotly_chart(fig_mix, use_container_width=True)
