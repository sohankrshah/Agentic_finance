import streamlit as st
import plotly.graph_objects as go
import yfinance as yf

def render_technical_chart(symbol):
    st.markdown("### 📈 Technical Chart Options")

    timeframe = st.selectbox("Select Timeframe", ["1 Day", "1 Week", "1 Month", "3 Months", "6 Months", "1 Year"])
    chart_type = st.radio("Select Chart Type", ["Candlestick", "Line", "OHLC"])

    timeframe_map = {
        "1 Day": ("1d", "5m"),
        "1 Week": ("7d", "30m"),
        "1 Month": ("1mo", "1h"),
        "3 Months": ("3mo", "1d"),
        "6 Months": ("6mo", "1d"),
        "1 Year": ("1y", "1d")
    }
    period, interval = timeframe_map[timeframe]

    ticker = yf.Ticker(f"{symbol}.NS")
    hist = ticker.history(period=period, interval=interval)

    if hist.empty:
        st.warning("No historical data available.")
        return

    if chart_type == "Candlestick":
        fig = go.Figure(data=[go.Candlestick(
            x=hist.index,
            open=hist['Open'],
            high=hist['High'],
            low=hist['Low'],
            close=hist['Close'],
            increasing_line_color='green',
            decreasing_line_color='red'
        )])
    elif chart_type == "Line":
        fig = go.Figure(data=[go.Scatter(
            x=hist.index,
            y=hist["Close"],
            mode="lines",
            line=dict(color="cyan"),
            name="Close Price"
        )])
    elif chart_type == "OHLC":
        fig = go.Figure(data=[go.Ohlc(
            x=hist.index,
            open=hist['Open'],
            high=hist['High'],
            low=hist['Low'],
            close=hist['Close'],
            increasing_line_color='green',
            decreasing_line_color='red'
        )])

    fig.update_layout(
        title=f"{symbol.upper()} Price History ({timeframe})",
        xaxis_title="Date",
        yaxis_title="Price (₹)",
        xaxis_rangeslider_visible=False,
        template="plotly_dark",
        paper_bgcolor="#0e1117",
        plot_bgcolor="#0e1117",
        font=dict(color="white")
    )

    st.plotly_chart(fig, use_container_width=True)
