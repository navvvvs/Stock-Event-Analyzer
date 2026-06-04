import pandas as pd

df = pd.read_csv("../data/impact_dataset.csv")

print("\nSentiment Distribution:")
print(df["sentiment"].value_counts())

print("\nAverage Return by Sentiment:")
print(
    df.groupby("sentiment")["daily_return"]
      .mean()
      .sort_values(ascending=False)
)