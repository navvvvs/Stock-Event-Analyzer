import pandas as pd
from transformers import pipeline

# Companies to process
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

print("Loading FinBERT model...")

classifier = pipeline(
    "sentiment-analysis",
    model="ProsusAI/finbert"
)

for company in companies:

    print(f"\nProcessing {company.upper()} news...")

    # Load news
    df = pd.read_csv(
        f"../data/{company}_news_filtered.csv"
    )

    results = []

    for _, row in df.iterrows():

        sentiment = classifier(
            str(row["title"])
        )[0]

        results.append({
            "title": row["title"],
            "publishedAt": row["publishedAt"],
            "label": sentiment["label"],
            "score": sentiment["score"]
        })

    results_df = pd.DataFrame(results)

    # Save results
    results_df.to_csv(
        f"../data/{company}_news_sentiment.csv",
        index=False
    )

    print(
        f"Saved {company}_news_sentiment.csv"
    )

    print(
        f"Articles analyzed: {len(results_df)}"
    )

print("\nAll sentiment files created successfully!")