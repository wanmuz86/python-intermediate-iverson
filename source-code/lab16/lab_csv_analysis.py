import pandas as pd
import matplotlib.pyplot as plt



print("=== Lab: CSV Data Analysis with Pandas ===")

# # We create the data as an Object Dictionary
# data = {
#     # Aina IT 5000 2022-01-10
#     # Ali HR 4000 2021-05-20
#     # 
#     "name": ["Aina", "Ali", "Mira", "John", "Sara"], # Imagine this is a column
#     "department": ["IT", "HR", "IT", "Finance", "HR"],
#     "salary": [5000, 4000, None, 6000, 4500],
#     "hire_date": [
#         "2022-01-10",
#         "2021-05-20",
#         "2023-03-15",
#         "2020-07-01",
#         None
#     ]
# }
# # Transform the Python Object into a DataFrame
# # Once you transform it you can run the Data Science Operation
# df = pd.DataFrame(data)
# # Save the data into .csv filr
# # df.to_csv -> Transform to CSV, index=False 
# # (not saved as an extra/normally when read ignore the first column)
# df.to_csv("employees.csv", index=False)


print("\n--- Part 1: Load CSV ---")

# load the data from employees.csv
df = pd.read_csv("employees.csv")

# show the data
print(df)

print(df.head(2)) # get the first 5 datas # specify wanted number in argument
print(df.tail(2)) # get the last 5 datas

# show the data type of each column
print("\nData Types:")
print(df.dtypes)


print("\n--- Missing Data ---")
# How many missing values are there in the dataframe / data
# you will retrieve the number of mssing value by column
print(df.isnull().sum())

# Fix the missing data
# For salary, we replace missing data with average salary

avg_salary = df["salary"].mean()
df["salary"] = df["salary"].fillna(avg_salary)

print("\nAfter filling salary:")
print(df)

#convert the hire_date comlumn (it thinks it is a string/object)
#  to panda datetime format
# error coerce -> If error just translate NaT (error handling in Panda)
df["hire_date"] = pd.to_datetime(df["hire_date"], errors="coerce")

# Group i & Aggregate

print("\n--- Average Salary by Department ---")

# Group the data by department, and get the average salary by department
grouped = df.groupby("department")["salary"].mean()
print(grouped)

print("\n--- Employee Count by Department ---")
# Group the data by department, and get how many employees are there by department
count = df.groupby("department")["name"].count()
print(count)

# Plot it as a graph using mathplotlib
print("\n--- Chart: Average Salary by Department ---")

# Type of graph - bar
ax = grouped.sort_values(ascending=False).plot(kind="bar")
# Title of the chart
ax.set_title("Average Salary by Department")
# x label
ax.set_xlabel("Department")
# y label
ax.set_ylabel("Average Salary")
# make sure all fix the graph
plt.tight_layout()
# save the graph
plt.savefig("avg_salary_by_department.png")
# show the graph
plt.show()

print("✅ Saved chart: avg_salary_by_department.png")


# Analayze data by year
# Group it by year
# Count the number of employee for each year

df["hire_year"] = df["hire_date"].dt.year

print("\n--- Employees by Hire Year ---")
print(df.groupby("hire_year")["name"].count())

#Export the department by salary analyzed data into a JSON file
grouped.to_json("salary_report.json")

