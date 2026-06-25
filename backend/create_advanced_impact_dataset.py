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

    # Load stock data
    stock_df = pd.read_csv(
        f"../data/{company}_ANALYZED.csv"
    )

    # Load sentiment data
    news_df = pd.read_csv(
        f"../data/{company.lower()}_news_sentiment.csv"
    )

    # Convert dates
    stock_df["Date"] = pd.to_datetime(
        stock_df["Date"]
    )

    news_df["publishedAt"] = pd.to_datetime(
        news_df["publishedAt"]
    )

    results = []

    for _, news in news_df.iterrows():

        news_date = news["publishedAt"].date()

        matching_rows = stock_df[
            stock_df["Date"].dt.date >= news_date
        ]

        if len(matching_rows) >= 2:

            current_close = matching_rows.iloc[0]["Close"]

            next_close = matching_rows.iloc[1]["Close"]

            next_day_return = (
                (next_close - current_close)
                / current_close
            ) * 100

            results.append({
                "title": news["title"],
                "publishedAt": news["publishedAt"],
                "sentiment": news["label"],
                "sentiment_score": news["score"],
                "current_close": current_close,
                "next_close": next_close,
                "next_day_return": next_day_return
            })

    impact_df = pd.DataFrame(results)

    impact_df.to_csv(
        f"../data/{company.lower()}_impact.csv",
        index=False
    )

    print(
        f"Saved {company.lower()}_impact.csv"
    )

    print(
        f"Rows Created: {len(impact_df)}"
    )

print("\nAll impact datasets created successfully!")