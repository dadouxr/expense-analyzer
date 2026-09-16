def get_total(df):
    return df["amount"].sum()


def get_category_totals(df):
    return df.groupby("category")["amount"].sum().sort_values(ascending=False)


def get_top_category(df):
    category_totals = get_category_totals(df)
    return category_totals.index[0]
