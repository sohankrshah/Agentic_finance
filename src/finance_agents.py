import yfinance as yf
import pandas as pd
import os
from datetime import datetime

class StockDataFetcher:
    def __init__(self, exchange_suffix=".NS"):
        self.exchange_suffix = exchange_suffix

    def get_company_info(self, symbol):
        ticker = yf.Ticker(f"{symbol}{self.exchange_suffix}")
        info = ticker.info

        name = info.get("longName") or info.get("shortName") or symbol.upper()
        sector = info.get("sector") or "Unknown"
        industry = info.get("industry") or "Unknown"
        website = info.get("website") or "N/A"
        description = info.get("longBusinessSummary") or "Description not available."

        return {
            "name": name,
            "sector": sector,
            "industry": industry,
            "website": website,
            "description": description
        }

    def get_fundamentals(self, symbol):
        ticker = yf.Ticker(f"{symbol}{self.exchange_suffix}")
        info = ticker.info

        # Manual fallback using historical data
        hist = ticker.history(period="1y", interval="1d")
        today_data = ticker.history(period="1d", interval="1m")

        week_52_high = hist["High"].max() if not hist.empty else None
        week_52_low = hist["Low"].min() if not hist.empty else None
        day_high = today_data["High"].max() if not today_data.empty else None
        day_low = today_data["Low"].min() if not today_data.empty else None
        current_price = info.get("currentPrice") or today_data["Close"].iloc[-1] if not today_data.empty else None

        return {
            "price": current_price,
            "fiftyTwoWeekHigh": week_52_high,
            "fiftyTwoWeekLow": week_52_low,
            "dayHigh": day_high,
            "dayLow": day_low,
            "marketCap": info.get("marketCap"),
            "volume": info.get("volume"),
            "peRatio": info.get("trailingPE"),
            "eps": info.get("trailingEps"),
            "dividendYield": info.get("dividendYield"),
            "beta": info.get("beta"),
            "netIncome": info.get("netIncomeToCommon"),
            "profitMargins": info.get("profitMargins"),
            "returnOnEquity": info.get("returnOnEquity"),
            "freeCashFlow": info.get("freeCashflow"),
            "revenue": info.get("totalRevenue"),
            "revenueGrowth": info.get("revenueGrowth"),
            "epsGrowth": info.get("earningsGrowth"),
            "debtToEquity": info.get("debtToEquity"),
            "enterpriseValue": info.get("enterpriseValue")
        }

    def get_price_history(self, symbol, period="6mo", interval="1d"):
        ticker = yf.Ticker(f"{symbol}{self.exchange_suffix}")
        return ticker.history(period=period, interval=interval)

    def update_local_data(self, symbol):
        base_path = f"data/{symbol.upper()}"
        os.makedirs(f"{base_path}/daily", exist_ok=True)

        ticker = yf.Ticker(f"{symbol}{self.exchange_suffix}")

        # Save overall historical data
        hist = ticker.history(period="max", interval="1d")
        hist.to_csv(f"{base_path}/overall.csv")

        # Save today's intraday data
        today = datetime.now().strftime("%Y-%m-%d")
        intraday = ticker.history(period="1d", interval="1m")
        intraday.to_csv(f"{base_path}/daily/{today}.csv")

        print(f"✅ Updated local data for {symbol}")
