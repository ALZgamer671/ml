import pandas as pd
from sklearn.datasets import fetch_california_housing
from sklearn.preprocessing import StandardScaler
import numpy as np
import matplotlib.pyplot as plt  # ← было matplotlib as plt

data = fetch_california_housing(as_frame=True).frame
learn = data[:15000]
test = data[15000:]


X = learn.iloc[:, :-1]
Y = learn.iloc[:, -1]


scaler = StandardScaler()
X = scaler.fit_transform(X)


def error(y1, y2, w, a):
    mse = np.mean((y1 - y2) ** 2)
    reg = a * np.sum(w**2)
    return mse + reg


def grad(X, y1, y2, w, a):
    n = X.shape[0]
    return (2 / n) * (X.T @ (y1 - y2)) + 2 * a * w


def gradb(y1, y2):
    n = len(y1)
    return (2 / n) * np.sum(y1 - y2)


def lin_reg(X, Y, w, b, a, LL, lr):
    y_pred = X @ w + b
    loss = error(Y, y_pred, w, a)
    LL.append(loss)

    G = grad(X, y_pred, Y, w, a)
    Gb = gradb(y_pred, Y)

    w = w - lr * G
    b = b - lr * Gb
    return w, b


LossList = []

w = np.zeros(X.shape[1])
b = np.mean(Y)
lr = 0.01
alpha = 0.1

for epoch in range(500):
    w, b = lin_reg(X, Y, w, b, alpha, LossList, lr)


plt.plot(LossList)
plt.xlabel("Эпоха")
plt.ylabel("Loss")
plt.title("Сходимость обучения")
plt.grid(True)
plt.savefig("loss.png", dpi=150)
plt.show()


X_test = scaler.transform(test.iloc[:, :-1])
Y_test = test.iloc[:, -1].values

y_pred = X_test @ w + b
mse_test = np.mean((y_pred - Y_test) ** 2)
ss_res = np.sum((Y_test - y_pred) ** 2)
ss_tot = np.sum((Y_test - np.mean(Y_test)) ** 2)
r2 = 1 - ss_res / ss_tot
print(f"Test R²: {r2:.4f}")
print(mse_test)

plt.figure(figsize=(6, 6))
plt.scatter(Y_test, y_pred, s=2, alpha=0.3)
plt.plot(
    [Y_test.min(), Y_test.max()],
    [Y_test.min(), Y_test.max()],
    "r--",
    lw=2,
    label="идеал",
)
plt.xlabel("Истинные значения")
plt.ylabel("Предсказания")
plt.title("Предсказания vs Истина")
plt.legend()
plt.grid(True)
plt.savefig("pred_vs_true.png", dpi=150)
plt.show()
