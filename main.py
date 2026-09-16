import pandas as pd

# Load the expenses
df = pd.read_csv("data/expenses.csv")

# Calculate total expenses
total = df["amount"].sum()

print("===== EXPENSE ANALYZER =====")
print(f"Total expenses: {total:.2f} €")

# Expenses by category
print("\nExpenses by category:")
print(df.groupby("category")["amount"].sum())
