import pandas as pd

companies = [
    "RELIANCE",
    "TCS",
    "INFY",
    "HDFCBANK",
    "ICICIBANK",
    "SBIN",
    "WIPRO",
    "LT"
]

for company in companies:

    print(f"\nProcessing {company}...")

    df = pd.read_csv(
        f"../data/{company}.csv"
    )

    df["Date"] = pd.to_datetime(
        df["Date"]
    )

    # Daily Return %
    df["Daily_Return"] = (
        df["Close"].pct_change() * 100
    )

    # Moving Averages
    df["MA_7"] = (
        df["Close"]
        .rolling(window=7)
        .mean()
    )

    df["MA_30"] = (
        df["Close"]
        .rolling(window=30)
        .mean()
    )

    # Volume Change %
    df["Volume_Change"] = (
        df["Volume"].pct_change() * 100
    )

    df.to_csv(
        f"../data/{company}_ANALYZED.csv",
        index=False
    )

    print(
        f"Saved {company}_ANALYZED.csv"
    )

print("\nAll stock files analyzed successfully!")