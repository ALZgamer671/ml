import numpy as np

# fmt: off
scores = np.array([
    [85, 90, 78],
    [60, 75, 80],
    [95, 88, 92],
    [45, 55, 60],
    [70, 80, 85]
])
# fmt: on

#  Найти средний балл по каждому экзамену.

# Найти средний балл каждого студента.

# Найти студентов, у которых средний балл выше 80.

# Найти максимальный балл среди всех студентов и экзаменов.

exams_mean = scores.mean(axis=0)

stu_mean = scores.mean(axis=1)

print(np.where(stu_mean > 80))

max_stu = scores.max()
