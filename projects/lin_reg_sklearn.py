import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

rng = np.random.default_rng(42)
n = 300

df = pd.DataFrame(
    {
        "area": rng.uniform(25, 150, n),
        "rooms": rng.integers(1, 6, n),
        "metro_distance": rng.uniform(100, 5000, n),
    }
)

noise = rng.normal(0, 1.5, n)

df["price"] = (
    0.18 * df["area"] + 0.7 * df["rooms"] - 0.0008 * df["metro_distance"] + 3 + noise
)
# print(df.shape)
# print(df.isna().sum())
# df.info()
X = df.iloc[:, :-1]
y = df.loc[:, "price"]
X_train, X_test, y_train, y_test = train_test_split(
    X, y, train_size=0.8, random_state=42
)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
model = LinearRegression()
model.fit(X_train, y_train)
predictions = model.predict(X_test)
mse = mean_squared_error(y_test, predictions)
mae = mean_absolute_error(y_test, predictions)
r2 = r2_score(y_test, predictions)
print(mse, mae, r2)
print(model.coef_, model.intercept_)

model_scaled = LinearRegression()
model_scaled.fit(X_train_scaled, y_train)
predictions_scaled = model_scaled.predict(X_test_scaled)
mse_scaled = mean_squared_error(y_test, predictions_scaled)
mae_scaled = mean_absolute_error(y_test, predictions_scaled)
r2_scaled = r2_score(y_test, predictions_scaled)
print(mse_scaled, mae_scaled, r2_scaled)
print(model_scaled.coef_, model_scaled.intercept_)
# после стандартизации лучше всего можно оценить коэффициенты. Видно, что коэффициент при площади самый болльшой, значит этот показатель влияет на стоимость сильнее всего и его увеличеине на одно стандартное отклоение увеличит значение предсказания сильнее чем увеличение любого другого, по отрицательности коэффициента при расстоянии до метро можно понять, что увеличение этого признака уменьшает стоимость квартиры при постоянстве остальных признаков
# по показателем ошибок и коэффициента детерминации можно сказать что можель справилась неплохо, если бы я не стандартизировал признаки можно было бы посмотреть на близость коэффииентов получившихся у модели к твоим
# по не стандартизированным коэффициентам видно что модель почти угадала заданные тобой коэффициенты и свободный член
