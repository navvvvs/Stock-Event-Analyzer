import pandas as pd

# Load stock data
stock_df = pd.read_csv("../data/RELIANCE_ANALYZED.csv")

# Load news sentiment data
news_df = pd.read_csv("../data/reliance_news.csv")

# Convert stock dates
stock_df['Date'] = pd.to_datetime(stock_df['Date']).dt.date

# Convert news dates
news_df['publishedAt'] = pd.to_datetime(
    news_df['publishedAt']
).dt.date

# Daily Return if not already present
if 'Daily_Return' not in stock_df.columns:
    stock_df['Daily_Return'] = (
        stock_df['Close'].pct_change() * 100
    )

results = []

for _, article in news_df.iterrows():

    news_date = article['publishedAt']

    matching_day = stock_df[
        stock_df['Date'] == news_date
    ]

    if len(matching_day) > 0:

        results.append({
            "title": article["title"],
            "news_date": news_date,
            "daily_return":
                matching_day.iloc[0]["Daily_Return"]
        })

impact_df = pd.DataFrame(results)

print(impact_df.head())

impact_df.to_csv(
    "../data/event_impact.csv",
    index=False
)

print("\nEvent impact file created!")