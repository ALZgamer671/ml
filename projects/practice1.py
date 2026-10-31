import pandas as pd

df = pd.DataFrame(
    {
        "area": [35, 52, 80, 45, 67],
        "rooms": [1, 2, 3, 2, 3],
        "district": ["Center", "North", "Center", "South", "North"],
        "price": [7000000, 8500000, 14000000, 6800000, 10000000],
    }
)

# Твой код ниже:
X = df[:, :-1]
Y = df[:, -1]

X.head()
Y.head()
