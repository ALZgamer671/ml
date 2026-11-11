import pandas as pd
import numpy as np

customers = pd.DataFrame(
    {
        "customer_id": [101, 102, 103, 104, 105, 106, 107],
        "region": ["North", "South", "North", "West", "South", "West", "North"],
        "age": [25, 34, np.nan, 45, 29, 38, 31],
    }
)

products = pd.DataFrame(
    {
        "product_id": [1, 2, 3, 4, 5],
        "category": [
            "Electronics",
            "Accessories",
            "Electronics",
            "Accessories",
            "Electronics",
        ],
        "price": [1000, 200, 1500, 300, 800],
    }
)

orders = pd.DataFrame(
    {
        "order_id": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
        "customer_id": [101, 102, 101, 103, 104, 105, 106, 101, 107, 102, 103, 105],
        "product_id": [1, 2, 3, 2, 4, 1, 5, 2, 3, 4, 5, 2],
        "quantity": [1, 3, 1, 2, 4, 1, 2, 5, 1, 2, 3, 1],
    }
)
# orders.info()
# customers.info()
# products.info()


# print(orders.isna())
# print(customers.isna())
# print(products.isna())

customers = customers.fillna(customers["age"].median())
# для возраста лучше взять медиану или среднее по всем пользователям потому что оценить возраст пользователя по остальным данным не получается
total_orders = orders.merge(customers, on="customer_id")

total_orders = total_orders.merge(products, on="product_id")

print(
    f"уникальных заказов: {total_orders['order_id'].nunique()}. всего заказов :{total_orders['order_id'].count()}, заказов до объединения: {orders['order_id'].count()}"
)
total_orders["revenue"] = total_orders["quantity"] * total_orders["price"]

categories = total_orders.groupby("category").agg(
    total_revenue=("revenue", "sum"), total_quantity=("quantity", "sum")
)

regions = total_orders.groupby("region").agg(
    total_revenue=("revenue", "sum"),
    unique_customers=("customer_id", "nunique"),
    avg_order_value=("revenue", "mean"),
)

customers_taskC = (
    total_orders.groupby("customer_id")
    .agg(
        total_spent=("revenue", "sum"),
        orders_count=("order_id", "nunique"),
    )
    .sort_values("total_spent", ascending=False)
)
big_orders = total_orders[total_orders["revenue"] > total_orders["revenue"].mean()][
    ["order_id", "customer_id", "region", "revenue"]
]

scores = np.array(
    [
        [0.82, 0.75, 0.91],
        [0.85, 0.78, 0.88],
        [0.79, 0.81, 0.90],
        [0.88, 0.76, 0.93],
        [0.84, 0.80, 0.89],
    ]
)
mean_metrics = scores.mean(axis=0)
print(mean_metrics)
m = scores.mean(axis=1).max()
print(np.where(scores.mean(axis=1) == m)[0][0])
ans = scores - mean_metrics
print(ans)


def counter(ids):
    if len(ids) == 0:
        return None
    ans = {}
    for i in ids:
        if i in ans:
            ans[i] += 1
        else:
            ans[i] = 1
    return [i for i in ans if ans[i] == max(ans.values())][0], ans[
        [i for i in ans if ans[i] == max(ans.values())][0]
    ]
