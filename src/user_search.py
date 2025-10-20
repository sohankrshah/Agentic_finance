import os
import pandas as pd
import yfinance as yf
from datetime import datetime

def ensure_folder_structure(symbol):
    base_path = f"data/{symbol.upper()}"
    daily_path = os.path.join(base_path, "daily")
    os.makedirs(daily_path, exist_ok=True)
    return base_path, daily_path

def update_overall_data(symbol, suffix=".NS"):
    ticker = yf.Ticker(f"{symbol}{suffix}")
    hist = ticker.history(period="max", interval="1d")

    base_path, _ = ensure_folder_structure(symbol)
    overall_path = os.path.join(base_path, "overall.csv")

    if os.path.exists(overall_path):
        existing = pd.read_csv(overall_path, index_col=0, parse_dates=True)
        combined = pd.concat([existing, hist])
        combined = combined[~combined.index.duplicated(keep="last")]
        combined.sort_index(inplace=True)
        combined.to_csv(overall_path)
    else:
        hist.to_csv(overall_path)

def update_intraday_data(symbol, suffix=".NS"):
    ticker = yf.Ticker(f"{symbol}{suffix}")
    intraday = ticker.history(period="1d", interval="1m")

    _, daily_path = ensure_folder_structure(symbol)
    today = datetime.now().strftime("%Y-%m-%d")
    intraday_path = os.path.join(daily_path, f"{today}.csv")

    intraday.to_csv(intraday_path)

def update_stock_history(symbol, suffix=".NS"):
    update_overall_data(symbol, suffix)
    update_intraday_data(symbol, suffix)
    print(f"✅ Data updated for {symbol.upper()} — overall + intraday")
