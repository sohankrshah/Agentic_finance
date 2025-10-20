import streamlit as st
import pandas as pd
from src.finance_agents import StockDataFetcher
from src.user_search import update_stock_history  # ✅ New import
from ui.layout import render_header, apply_dark_theme
from ui.sidebar import render_sidebar
from ui.technical_chart import render_technical_chart
from ui.fundamental import render_fundamental_data

@st.cache_resource
def load_fetcher():
    return StockDataFetcher()

@st.cache_data
def get_cached_company_info(_fetcher, symbol):
    return _fetcher.get_company_info(symbol)

# 🔌 Initialize
fetcher = load_fetcher()
st.set_page_config(page_title="KARTS", page_icon="📈", layout="wide")
apply_dark_theme()

def main():
    render_header()
    sidebar = render_sidebar()
    stock_symbol = sidebar["company_name"]
    show_fundamental = sidebar["show_fundamental"]
    show_technical = sidebar["show_technical"]
    show_sentiment = sidebar["show_sentiment"]
    show_risks = sidebar["show_risks"]
    show_recommendation = sidebar["show_recommendation"]

    if stock_symbol:
        # 🗂️ Update local data lake
        update_stock_history(stock_symbol)

        # 🏢 Company Info
        st.subheader(f"📌 Analysis for: {stock_symbol.upper()}")
        info = get_cached_company_info(fetcher, stock_symbol)
        st.markdown("### 🏢 Company Profile")
        st.markdown(f"""**Name:** {info['name']} 
                     \n**Sector:** {info['sector']}  
                     \n**Industry:** {info['industry']} 
                     \n**Website:** [{info['website']}]({info['website']})""")
        st.markdown("### 🧠 Company Description")
        st.markdown(f"{info['description']}")

        # 📊 Fundamental Analysis
        if show_fundamental:
            render_fundamental_data(fetcher, stock_symbol)

        # 📈 Technical Chart
        if show_technical:
            render_technical_chart(stock_symbol)

        # 💬 Sentiment
        if show_sentiment:
            st.markdown("### 💬 Sentiment Analysis")
            st.write("Recent news sentiment: Positive\nSocial media buzz: High")

        # ⚠️ Risk
        if show_risks:
            st.markdown("### ⚠️ Risk Assessment")
            st.write("Volatility: Moderate\nDebt-to-equity ratio: Healthy\nRegulatory risk: Low")

        # 🤖 Recommendation
        if show_recommendation:
            st.markdown("### 🤖 AI Recommendations")
            st.write("Based on current fundamentals and sentiment, this stock is suitable for medium-term holding.")

if __name__ == "__main__":
    main()
