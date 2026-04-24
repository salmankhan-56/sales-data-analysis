import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data.csv")

plt.plot(df["Month"], df["Sales"], marker="o")
plt.title("sales-data-analysis Sales Analysis")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.savefig("sales_chart.png")

print("Chart saved as sales_chart.png")
