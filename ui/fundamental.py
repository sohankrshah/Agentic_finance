import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

@st.cache_data
def get_cached_fundamentals(_fetcher, symbol):
    return _fetcher.get_fundamentals(symbol)

def draw_gauge(title, low, high, value):
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=value,
        title={'text': title},
        gauge={
            'axis': {'range': [low, high]},
            'bar': {'color': "darkblue"},
            'steps': [
                {'range': [low, (low + high) / 2], 'color': "red"},
                {'range': [(low + high) / 2, high], 'color': "green"}
            ],
            'threshold': {
                'line': {'color': "black", 'width': 4},
                'thickness': 0.75,
                'value': value
            }
        }
    ))
    return fig

def render_fundamental_data(fetcher, symbol):
    data = get_cached_fundamentals(fetcher, symbol)

    current_price = data.get("price")
    week_52_high = data.get("fiftyTwoWeekHigh")
    week_52_low = data.get("fiftyTwoWeekLow")
    today_high = data.get("dayHigh")
    today_low = data.get("dayLow")

    # 📆 52-Week Gauge
    st.markdown("### 📆 52-Week Price Position")
    if None not in (current_price, week_52_low, week_52_high):
        fig_52 = draw_gauge("52W Range", week_52_low, week_52_high, current_price)
        st.plotly_chart(fig_52, use_container_width=True)
        st.caption(f"📉 Low: ₹{week_52_low:.2f} | 📍 Current: ₹{current_price:.2f} | 📈 High: ₹{week_52_high:.2f}")
    else:
        st.warning("⚠️ 52-week data not available.")

    # 📅 Today’s Gauge
    st.markdown("### 📅 Today's Price Position")
    if None not in (current_price, today_low, today_high):
        fig_today = draw_gauge("Today’s Range", today_low, today_high, current_price)
        st.plotly_chart(fig_today, use_container_width=True)
        st.caption(f"📉 Low: ₹{today_low:.2f} | 📍 Current: ₹{current_price:.2f} | 📈 High: ₹{today_high:.2f}")
    else:
        st.warning("⚠️ Today's high/low data not available.")

    # 📊 Valuation Metrics
    st.markdown("### 📊 Valuation Metrics")
    valuation_df = pd.DataFrame({
        "Metric": ["Price (₹)", "Market Cap", "Volume", "P/E Ratio", "EPS", "Dividend Yield", "Beta"],
        "Value": [
            data.get("price"), data.get("marketCap"), data.get("volume"),
            data.get("peRatio"), data.get("eps"), data.get("dividendYield"), data.get("beta")
        ]
    })
    st.dataframe(valuation_df, use_container_width=True)

    # 💰 Profitability Metrics
    st.markdown("### 💰 Profitability Metrics")
    profit_df = pd.DataFrame({
        "Metric": ["Net Income", "Profit Margin", "Return on Equity", "Free Cash Flow"],
        "Value": [
            data.get("netIncome"), data.get("profitMargins"),
            data.get("returnOnEquity"), data.get("freeCashFlow")
        ]
    })
    st.dataframe(profit_df, use_container_width=True)

    # 📈 Growth Metrics
    st.markdown("### 📈 Growth Metrics")
    growth_df = pd.DataFrame({
        "Metric": ["Revenue", "Revenue Growth", "EPS Growth"],
        "Value": [
            data.get("revenue"), data.get("revenueGrowth"), data.get("epsGrowth")
        ]
    })
    st.dataframe(growth_df, use_container_width=True)

    # 📉 Risk & Leverage
    st.markdown("### 📉 Risk & Leverage")
    risk_df = pd.DataFrame({
        "Metric": ["Debt-to-Equity Ratio", "Enterprise Value"],
        "Value": [
            data.get("debtToEquity"), data.get("enterpriseValue")
        ]
    })
    st.dataframe(risk_df, use_container_width=True)

    # 📊 Revenue vs Net Income Chart
    revenue = data.get("revenue")
    net_income = data.get("netIncome")
    if revenue is not None and net_income is not None:
        st.markdown("### 📊 Revenue vs Net Income")
        fig = px.bar(
            x=["Revenue", "Net Income"],
            y=[revenue, net_income],
            labels={"x": "Metric", "y": "Amount (₹)"},
            color=["Revenue", "Net Income"],
            template="plotly_dark"
        )
        st.plotly_chart(fig, use_container_width=True)
