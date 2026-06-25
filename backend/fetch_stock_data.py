import yfinance as yf
import os

os.makedirs("../data", exist_ok=True)

stocks = {
    "RELIANCE": "RELIANCE.NS",
    "TCS": "TCS.NS",
    "INFY": "INFY.NS",
    "HDFCBANK": "HDFCBANK.NS",
    "ICICIBANK": "ICICIBANK.NS",
    "SBIN": "SBIN.NS",
    "WIPRO": "WIPRO.NS",
    "LT": "LT.NS"
}

for company, ticker in stocks.items():

    print(f"Downloading {company}...")

    data = yf.Ticker(ticker).history(period="2y")

    data.to_csv(
        f"../data/{company}.csv"
    )

    print(f"Saved {company}.csv")