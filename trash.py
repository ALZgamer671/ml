import pandas as pd

df = pd.DataFrame(
    {
        "user_id": [1, 1, 2, 3, 3, 3],
        "category": ["A", "A", "A", "B", "B", "A"],
        "amount": [100, 200, 150, 300, 100, 50],
    }
)

ans = df.groupby("category").agg(
    total_amount=("amount", "sum"), unique_users=("user_id", "nunique")
)
ans.reset_index()
print(ans)
