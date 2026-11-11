import numpy as np
from sklearn.metrics import confusion_matrix
from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import (
    recall_score,
    precision_score,
    f1_score,
    roc_auc_score,
    accuracy_score,
)
from sklearn.model_selection import train_test_split

X, y = make_classification(
    n_samples=600,
    n_features=6,
    n_informative=4,
    n_redundant=0,
    weights=[0.8, 0.2],
    random_state=42,
)
print(X.shape, y.shape)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
pol = (y == 1).sum()
otr = (y == 0).sum()
print(pol, otr)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

probabilites = model.predict_proba(X_test)

predictions = (probabilites >= 0.5).astype(int)[:, 1]
acc = accuracy_score(y_test, predictions)
prescision = precision_score(y_test, predictions)
recall = recall_score(y_test, predictions)
f1 = f1_score(y_test, predictions)
roc = roc_auc_score(y_test, probabilites[:, 1])
print("порог 0.5")
cm = confusion_matrix(y_test, predictions)
print(cm)
print(acc)
print(prescision)
print(recall)
print(f1)
print(roc)

predictions = (probabilites >= 0.3).astype(int)[:, 1]
acc = accuracy_score(y_test, predictions)
prescision = precision_score(y_test, predictions)
recall = recall_score(y_test, predictions)
f1 = f1_score(y_test, predictions)
roc = roc_auc_score(y_test, probabilites[:, 1])
print("порог 0.3")
cm = confusion_matrix(y_test, predictions)
print(cm)
print(acc)
print(prescision)
print(recall)
print(f1)
print(roc)
