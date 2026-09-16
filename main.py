import pandas as pd
from analyzer import get_total, get_category_totals, get_top_category

# Load the expenses
df = pd.read_csv("data/expenses.csv")

# Analyze the expenses
total = get_total(df)
category_totals = get_category_totals(df)
top_category = get_top_category(df)

# Display the results
print("===== EXPENSE ANALYZER =====")
print(f"Total expenses: {total:.2f} €")

print("\nExpenses by category:")
print(category_totals)

print(f"\nTop category: {top_category}")
