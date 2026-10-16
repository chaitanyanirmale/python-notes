import pandas as pd

# Series — one-dimensional
# Think of a Series as a single column of data.

ages = pd.Series([24, 26, 23, 25])
# print(ages)

# DataFrame — two-dimensional
# Think of a DataFrame as a table containing rows and columns.

data = {
  "Name": ["Rahul", "Priya", "Amit"],
  "Age": [24, 26, 23],
  "Salary": [30000, 45000, 28000]
}
df = pd.DataFrame(data)
print(df)

#------------------------------------------------
student_data = {
    "Student": ["Rahul", "Priya", "Amit", "Sneha"],
    "Marks": [85, 92, 76, 88],
    "City": ["Pune", "Mumbai", "Pune", "Nashik"]
}

stu_df = pd.DataFrame(student_data)
print(stu_df)
print(stu_df["Marks"].mean())


#------------------------------------------------

product_data = {
  "Product": ["Laptop", "Mouse", "Keyboard", "Monitor"],
  "Price": [50000, 500, 1500, 12000],
  "Quantity": [2, 5, 4, 3] 
}
pr_df = pd.DataFrame(product_data)
print(pr_df)
print(pr_df["Product"])
print(pr_df["Price"].mean())

#--------------------------------------------------
emp_data = {
    "Name": ["Rahul", "Priya", "Amit", "Sneha", "Raj"],
    "Age": [24, 26, 23, 25, 28],
    "Salary": [30000, 45000, 28000, 40000, 55000],
    "Department": ["IT", "HR", "IT", "Finance", "HR"]
}

emp_df = pd.DataFrame(emp_data)
print(emp_df)
print(emp_df.head()) # View the first rows. Displays the first five rows by default. 
# You can specify how many rows to display:
print(emp_df.head(2))
print(emp_df.tail(2)) # View the last rows
print(emp_df.shape) # Count rows and columns
print(emp_df.columns) # Get column names
print(emp_df.dtypes) # Check data types
emp_df.info() # Get a dataset summary
print(emp_df.describe()) # Summarize numerical data

print(emp_df["Name"]) # Select a single column
print(emp_df[["Name", "Salary"]]) # Select multiple columns
#--------------------------------------------------

# Select rows using .iloc[]
# .iloc[] selects rows and columns by their integer positions, starting at zero.

print(emp_df.iloc[0]) # Select the first row
print(emp_df.iloc[2]) # Select the third row
print(emp_df.iloc[0:3]) # Select the first three rows
print(df.iloc[0:3, 0:2]) # Select specific rows and columns df.iloc[row_positions, column_positions]

#----------------------------------------------------
# Select rows using .loc[]
# .loc[] selects data using index labels and column names.
print(emp_df.loc[0]) # This returns the row whose index label is 0
print(emp_df.loc[0, ["Name", "Salary"]]) # Select specific columns for that row

print(emp_df.loc[0:2, ["Name", "Salary"]]) # select multiple rows and columns
# Unlike ordinary Python slicing, .loc[0:2] includes both index labels 0 and 2
