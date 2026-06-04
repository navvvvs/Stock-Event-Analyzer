import pandas as pd

# Load stock data
stock_df = pd.read_csv("../data/RELIANCE_ANALYZED.csv")

# Load sentiment data
news_df = pd.read_csv("../data/reliance_news_sentiment.csv")

# Convert date columns
stock_df["Date"] = pd.to_datetime(stock_df["Date"])
news_df["publishedAt"] = pd.to_datetime(news_df["publishedAt"])

results = []

for _, news in news_df.iterrows():

    news_date = news["publishedAt"].date()

    # Find stock rows on or after the news date
    matching_rows = stock_df[
        stock_df["Date"].dt.date >= news_date
    ]

    # Need at least current day + next trading day
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

# Create DataFrame
impact_df = pd.DataFrame(results)

# Save output
impact_df.to_csv(
    "../data/advanced_impact_dataset.csv",
    index=False
)

print("\nAdvanced Impact Dataset")
print(impact_df.head())

print(f"\nTotal Rows Created: {len(impact_df)}")
print("\nFile saved as: advanced_impact_dataset.csv")