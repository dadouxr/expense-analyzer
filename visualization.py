import matplotlib.pyplot as plt


def show_category_chart(category_totals):
    category_totals.plot(kind="bar")

    plt.title("Expenses by Category")
    plt.xlabel("Category")
    plt.ylabel("Amount (€)")

    plt.tight_layout()
    plt.show()
