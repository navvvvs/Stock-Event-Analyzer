import pandas as pd

stock_df = pd.read_csv("../data/TCS_ANALYZED.csv")
stock_df["Date"] = pd.to_datetime(stock_df["Date"])

print("Stock Min:", stock_df["Date"].min())
print("Stock Max:", stock_df["Date"].max())

news_df = pd.read_csv("../data/tcs_news_sentiment.csv")
news_df["publishedAt"] = pd.to_datetime(news_df["publishedAt"])

print("\nNews Min:", news_df["publishedAt"].min())
print("News Max:", news_df["publishedAt"].max())