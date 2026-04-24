import pandas as pd

df = pd.read_csv("data.csv")

print("Dataset:")
print(df)

print("\nTotal Sales:", df["Sales"].sum())
print("Total Profit:", df["Profit"].sum())
print("Average Customers:", df["Customers"].mean())

best_month = df.loc[df["Profit"].idxmax(), "Month"]
print("Best Profit Month:", best_month)
