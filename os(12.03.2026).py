import pandas as pd
import plotly.express as px

data = {
   "product": ["A", "B", "C", "D"],
   "sales": [120, 200, 150, 300]
}

df = pd.DataFrame(data)

fig = px.bar(df, x="product", y="sales",
            title="Sales by Product")

fig.show()

#Line Chart (Trend Visualization)
# fig = px.line(
#     df,
#     x="product",
#     y="sales",
#     title="Sales Trend by Product",
#     markers=True
# )

# fig.show()

# Task (10–15 min)
#  Use Plotly to explore and visualize a simple dataset.
# 📊 Create a Dataset
# Import the required libraries and create a small dataset.
# import pandas as pd
# import plotly.express as px
# data = {
#    "product": ["A", "B", "C", "D"],
#    "sales": [120, 200, 150, 300]
# }
# df = pd.DataFrame(data)
# 📈 Create an Interactive Chart
# Create a bar chart visualization.
# fig = px.bar(df, x="product", y="sales",
#             title="Sales by Product")
# fig.show()

# Line Chart (Trend Visualization)
# fig = px.line(
#     df,
#     x="product",
#     y="sales",
#     title="Sales Trend by Product",
#     markers=True
# )

# fig.show()

# 🔵 Scatter Plot (Relationship View)
# fig = px.scatter(
#     df,
#     x="product",
#     y="sales",
#     title="Sales Scatter Plot",
#     size="sales"
# )

# fig.show()

# 🥧 Pie Chart (Proportion of Sales)
# fig = px.pie(
#     df,
#     names="product",
#     values="sales",
#     title="Sales Distribution"
# )

# fig.show()