#Common Pandas Operations

# read.csv()
# read_json()
# head()
# info()
# describe()

# import pandas as pd
# df = pd.read_csv("employees.csv")

# # Select a single column
# df["Salary"]

# # Filter rows
# df[df["Salary"] > 60000]

# # Multiple conditions
# df[(df["Age"]> 25) & (df["Salary"]> 50000)]

# # Grouping Data
# df.groupby("Department")["Salary"].mean()

# # Other Aggregations
# df.groupby("Department").sum()
# df.groupby("Department").count()
# df.groupby("Department").max()

# # Check for Missing Values
# df.isnull()
# df.isnull().sum()

# # Drop Missing Values
# df.dropna()

# # Fill Missing Values
# df.fillna(0)
# df["Salary"].fillna(df["Salary"].mean())

# # Common Cleaning Operations

# # Remove Duplicates
# df.drop_duplicates()

# # Rename Columns
# df.rename(columns={"Emp_Name": "EmployeeName"})

# # Change Data Types
# df["Salary"] = df["Salary"].astype(float)

# # Sort Data
# df.sort_values("Salary", ascending=False)






