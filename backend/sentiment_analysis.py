import pandas as pd
from transformers import pipeline

# Load news
df = pd.read_csv("../data/reliance_news_filtered.csv")

# Sentiment model
classifier = pipeline(
    "sentiment-analysis",
    model="ProsusAI/finbert"
)

# Analyze first 10 articles initially
results = []

for _, row in df.iterrows():

    sentiment = classifier(str(row["title"]))[0]

    results.append({
    "title": row["title"],
    "publishedAt": row["publishedAt"],
    "label": sentiment["label"],
    "score": sentiment["score"]
    })

results_df = pd.DataFrame(results)

print(results_df.head())

results_df.to_csv(
    "../data/reliance_news_sentiment.csv",
    index=False
)
print(f"\nTotal Articles Analyzed: {len(results_df)}")
print("Sentiment analysis completed")