import pandas as pd

# Load stock data
stock_df = pd.read_csv("../data/RELIANCE_ANALYZED.csv")

# Load sentiment data
sentiment_df = pd.read_csv("../data/reliance_news_sentiment.csv")

# Convert dates
stock_df["Date"] = pd.to_datetime(stock_df["Date"]).dt.date

sentiment_df["publishedAt"] = pd.to_datetime(
    sentiment_df["publishedAt"]
).dt.date

results = []

for _, news in sentiment_df.iterrows():

    news_date = news["publishedAt"]

    stock_match = stock_df[
        stock_df["Date"] == news_date
    ]

    if len(stock_match) > 0:

        results.append({
            "title": news["title"],
            "date": news_date,
            "sentiment": news["label"],
            "sentiment_score": news["score"],
            "daily_return":
                stock_match.iloc[0]["Daily_Return"]
        })

impact_df = pd.DataFrame(results)

print(impact_df.head())

impact_df.to_csv(
    "../data/impact_dataset.csv",
    index=False
)

print("\nImpact dataset created!")
print(f"Total rows: {len(impact_df)}")