import numpy as np

from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    confusion_matrix,
)

# Создаём данные с редким положительным классом
X, y = make_classification(
    n_samples=1000,
    n_features=2,
    n_informative=2,
    n_redundant=0,
    weights=[0.9, 0.1],
    class_sep=1.0,
    random_state=42,
)

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.3,
    stratify=y,
    random_state=42,
)

# Масштабирование + логистическая регрессия
model = make_pipeline(
    StandardScaler(),
    LogisticRegression(random_state=42),
)

model.fit(X_train, y_train)

# Вероятности принадлежности к классу 1
probabilities = model.predict_proba(X_test)[:, 1]
for threshold in [0.5, 0.9]:
    y_pred = (probabilities >= threshold).astype(int)

    print(f"\nПорог: {threshold}")
    print("Accuracy:", accuracy_score(y_test, y_pred))
    print("Precision:", precision_score(y_test, y_pred, zero_division=0))
    print("Recall:", recall_score(y_test, y_pred, zero_division=0))
    print("Confusion matrix:")
    print(confusion_matrix(y_test, y_pred))
print("Первые 10 вероятностей:", probabilities[:10])
print("Первые 10 истинных меток:", y_test[:10])
