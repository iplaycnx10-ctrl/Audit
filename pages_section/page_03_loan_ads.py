import plotly.express as px
import streamlit as st
from components.common import metric, section
from data.loan_data import loan_data, loan_summary


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


def render():
    section("03. PERFORMANCE: BUSINESS LOAN ADS", "Message Funnel Performance Dashboard", "ประวัติข้อมูล Meta Business Loan จริงจากที่ผ่านมา")
    m1, m2, m3, m4 = st.columns(4)
    with m1: metric("Total Spend", f"฿{loan_summary['total_spend']:,.0f}", "งบประมาณรวมจาก 2 ชุดข้อมูล")
    with m2: metric("Total Messages", f"{loan_summary['total_messages']:,.0f}", "ข้อความทักรวมโดยประมาณ")
    with m3: metric("Avg Cost / Message", f"฿{loan_summary['avg_cost']:,.2f}", "ต้นทุนเฉลี่ยต่อข้อความ")
    with m4: metric("Total Reach", f"{loan_summary['total_reach']:,.0f}", "จำนวนคนที่เข้าถึงรวม")

    k1, k2, k3, k4 = st.columns(4)
    with k1: metric("Impressions", f"{loan_summary['total_impressions']:,.0f}", "จำนวนครั้งที่แสดงผลรวม")
    with k2: metric("Avg CTR", f"{loan_summary['avg_ctr']:.2f}%", "CTR เฉลี่ยโดยประมาณ")
    with k3: metric("Avg CPM", f"฿{loan_summary['avg_cpm']:.2f}", "CPM เฉลี่ยโดยประมาณ")
    with k4: metric("Avg CPC", f"฿{loan_summary['avg_cpc']:.2f}", "CPC เฉลี่ยโดยประมาณ")

    st.markdown("<div style='height:22px;'></div>", unsafe_allow_html=True)

    chart_col1, chart_col2 = st.columns(2, gap="large")
    with chart_col1:
        fig_msg = px.bar(loan_data.sort_values('Messages', ascending=False), x='Ad', y='Messages', text='Messages', color='Messages', color_continuous_scale='Viridis', title='Message Volume Heat Pattern')
        fig_msg.update_traces(texttemplate='%{text:,.0f}', textposition='outside')
        style_chart(fig_msg)
        fig_msg.update_layout(xaxis_title='', coloraxis_showscale=False)
        st.plotly_chart(fig_msg, use_container_width=True)
    with chart_col2:
        fig_cost = px.bar(loan_data.sort_values('Cost/Message'), x='Ad', y='Cost/Message', text='Cost/Message', color='Cost/Message', color_continuous_scale='Turbo', title='Cost per Message Heat Pattern • Lower is Better')
        fig_cost.update_traces(texttemplate='฿%{text:.2f}', textposition='outside')
        style_chart(fig_cost)
        fig_cost.update_layout(xaxis_title='', coloraxis_showscale=False)
        st.plotly_chart(fig_cost, use_container_width=True)

    st.markdown("<div style='height:16px;'></div>", unsafe_allow_html=True)

    chart_col3, chart_col4 = st.columns(2, gap="large")
    with chart_col3:
        fig_spend = px.pie(loan_data, values='Spend', names='Ad', hole=.55, title='Spend Distribution by Ad Set')
        style_chart(fig_spend)
        fig_spend.update_layout(showlegend=True)
        st.plotly_chart(fig_spend, use_container_width=True)
    with chart_col4:
        efficiency_data = loan_data[['Ad', 'CTR', 'CPM', 'CPC', 'Frequency']].sort_values('CTR', ascending=False)
        fig_eff = px.bar(efficiency_data, x='Ad', y=['CTR', 'CPC', 'Frequency'], barmode='group', title='Engagement & Efficiency Snapshot')
        style_chart(fig_eff)
        fig_eff.update_layout(xaxis_title='')
        st.plotly_chart(fig_eff, use_container_width=True)
