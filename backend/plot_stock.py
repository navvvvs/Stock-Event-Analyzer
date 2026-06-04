import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../data/RELIANCE_ANALYZED.csv")

df['Date'] = pd.to_datetime(df['Date'])

plt.figure(figsize=(12,6))

plt.plot(df['Date'], df['Close'], label='Close')
plt.plot(df['Date'], df['MA_7'], label='7-Day MA')
plt.plot(df['Date'], df['MA_30'], label='30-Day MA')

plt.legend()
plt.title("Reliance Stock Price Analysis")

plt.xticks(rotation=45)

plt.tight_layout()

plt.show()