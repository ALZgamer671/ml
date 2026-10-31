import pandas as pd

url = "C:/Users/murze/Downloads/titanic.csv"
df = pd.read_csv(url)

# Проверяем, что все загрузилось
print(df.head())
ans = df.groupby(["Sex", "Pclass"])["Age"].mean()
print(ans)
