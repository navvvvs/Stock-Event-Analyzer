import pandas as pd

stock_df = pd.read_csv("../data/RELIANCE_ANALYZED.csv")

print("First Date:", stock_df["Date"].min())
print("Last Date:", stock_df["Date"].max())
print("Total Rows:", len(stock_df))