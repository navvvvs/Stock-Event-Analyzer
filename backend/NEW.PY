import pandas as pd

news = pd.read_csv("../data/reliance_news.csv")

print(news["publishedAt"].head())