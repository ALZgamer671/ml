import pandas as pd
import numpy as np

# fmt off
employees = pd.DataFrame(
    {
        "employee_id": [101, 102, 103, 104, 105, 106, 107],
        "name": ["Anna", "Bob", "Charlie", "David", "Eva", "Frank", "Grace"],
        "department_id": [1, 2, 1, 3, 2, 3, 1],
        "salary": [120, 90, 150, np.nan, 110, 100, 130],
        "experience": [2, 5, 4, 3, 1, 6, 2],
    }
)


departments = pd.DataFrame(
    {"department_id": [1, 2, 3], "department_name": ["IT", "HR", "Sales"]}
)
# fmt on

employees["salary"] = employees["salary"].fillna(employees["salary"].median())
df = pd.merge(
    employees, departments, on="department_id", how="left", validate="many_to_one"
)
full_df = df
df = df[(df["salary"] >= 100) & (df["experience"] >= 2)][
    ["name", "salary", "experience", "department_name"]
]
df2 = full_df.groupby("department_name").agg(
    mean_sal=("salary", "mean"), max_sal=("salary", "max"), emp=("name", "count")
)

df = df.sort_values(["salary", "experience"], ascending=[False, True])

df = df.set_index("name")
best_emp = df.loc[df.index[0]]
df = df.reset_index()


print(df)
