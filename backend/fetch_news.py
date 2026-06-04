import requests
import pandas as pd

API_KEY = "6d9a98e2ee44449f846f88fd38caf171"

query = "Reliance Industries"

url = (
    f"https://newsapi.org/v2/everything?"
    f"q={query}&"
    f"language=en&"
    f"sortBy=publishedAt&"
    f"apiKey={API_KEY}"
)

response = requests.get(url)

data = response.json()

articles = []

for article in data["articles"]:
    articles.append({
        "title": article["title"],
        "description": article["description"],
        "source": article["source"]["name"],
        "publishedAt": article["publishedAt"],
        "url": article["url"]
    })

df = pd.DataFrame(articles)

# Keep only Reliance-related news
keywords = [
    "Reliance",
    "Jio",
    "Reliance Industries"
]

filtered_df = df[
    df["title"].str.contains(
        "|".join(keywords),
        case=False,
        na=False
    )
]

filtered_df.to_csv(
    "../data/reliance_news_filtered.csv",
    index=False
)

print(filtered_df.head())

print(f"\nFiltered articles: {len(filtered_df)}")