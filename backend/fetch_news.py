import requests
import pandas as pd
import os

API_KEY = "6d9a98e2ee44449f846f88fd38caf171"

os.makedirs("../data", exist_ok=True)

companies = {

    "RELIANCE": {
        "query": "Reliance Industries",
        "keywords": [
            "Reliance",
            "Jio",
            "Reliance Industries"
        ]
    },

    "TCS": {
        "query": "TCS",
        "keywords": [
            "TCS",
            "Tata Consultancy Services"
        ]
    },

    "INFY": {
        "query": "Infosys",
        "keywords": [
            "Infosys",
            "INFY"
        ]
    },

    "HDFCBANK": {
        "query": "HDFC Bank",
        "keywords": [
            "HDFC Bank",
            "HDFCBANK"
        ]
    },

    "ICICIBANK": {
        "query": "ICICI Bank",
        "keywords": [
            "ICICI Bank",
            "ICICIBANK"
        ]
    },

    "SBIN": {
        "query": "State Bank of India",
        "keywords": [
            "State Bank of India",
            "SBI",
            "SBIN"
        ]
    },

    "WIPRO": {
        "query": "Wipro",
        "keywords": [
            "Wipro"
        ]
    },

    "LT": {
        "query": "Larsen & Toubro",
        "keywords": [
            "Larsen",
            "L&T",
            "Larsen & Toubro"
        ]
    }
}

for company, info in companies.items():

    print(f"\nFetching news for {company}...")

    url = (
        f"https://newsapi.org/v2/everything?"
        f"q={info['query']}&"
        f"language=en&"
        f"sortBy=publishedAt&"
        f"pageSize=100&"
        f"apiKey={API_KEY}"
    )

    response = requests.get(url)

    data = response.json()

    articles = []

    for article in data.get("articles", []):

        articles.append({
            "title": article["title"],
            "description": article["description"],
            "source": article["source"]["name"],
            "publishedAt": article["publishedAt"],
            "url": article["url"]
        })

    df = pd.DataFrame(articles)

    filtered_df = df[
        df["title"].str.contains(
            "|".join(info["keywords"]),
            case=False,
            na=False
        )
    ]

    filtered_df.to_csv(
        f"../data/{company.lower()}_news_filtered.csv",
        index=False
    )

    print(
        f"Saved {company.lower()}_news_filtered.csv"
    )

    print(
        f"Articles found: {len(filtered_df)}"
    )

print("\nAll news files created successfully!")