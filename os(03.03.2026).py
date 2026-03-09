# import matplotlib.pyplot as plt

# plt.plot([1,2,3],[4,5,6])
# plt.title("Simple Line Plot")
# plt.xlabel("x-axis")
# plt.ylabel("y-axis")
# plt.show()

# from matplotlib import pyplot

# x = [1,2,3,4,5,]
# y = [6,7,8,9,10]

# pyplot.figure(figsize=(10,5))
# pyplot.plot(x,y,marker=0,color='green')
# pyplot.show()

# Bar charts for comparisons
# Line charts for trends
# Pie charts for proportions
# Histograms for distributions
# Scatter plots for relationships

# 1000 rows → 1000 individual records (like 1000 customers, 1000 products, 1000 transactions)
# 5 columns → 5 variables or features (like price, sales, category, date, etc.)
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 1000 entries, 0 to 999
# Data columns (total 5 columns):
#  product     1000 non-null object
#  price       1000 non-null int64
#  sales       1000 non-null int64
#  category    950 non-null object
#  rating      900 non-null float64


# df["sales"].hist()
# df.iloc[0]   # first row
# df.iloc[1]   # second row
# df = df.set_index("product")

# df[df["price"] < 500]
# df[df["product"] == "Phone"]
# df[df["sales"] != 0]
# df[df["category"].isna()]

# df["revenue"] = df["price"] * df["sales"]
# df.groupby("product")["revenue"].sum().sort_values(ascending=False)

# df[["price","sales"]].corr()