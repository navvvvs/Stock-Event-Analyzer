import pandas as pd

# Load stock data
df = pd.read_csv("../data/RELIANCE.csv")

# Convert Date column
df['Date'] = pd.to_datetime(df['Date'])

# Daily Return %
df['Daily_Return'] = df['Close'].pct_change() * 100
df['MA_7'] = df['Close'].rolling(window=7).mean()

df['MA_30'] = df['Close'].rolling(window=30).mean()

df['Volume_Change'] = df['Volume'].pct_change() * 100

print(df[['Date', 'Close', 'Daily_Return', 'MA_7', 'MA_30', 'Volume_Change']].tail())

# Save processed file
df.to_csv("../data/RELIANCE_ANALYZED.csv", index=False)