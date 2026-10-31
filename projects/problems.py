# Найди длину самого длинного непрерывного участка, на котором каждое следующее число строго больше предыдущего
# a = [4, 1, 2, 3, 0, 5, 6, 7, 8, 2, 3]
# ans = 0
# last = a[0]
# l = 1
# for i in range(1, len(a)):
#     if a[i] > last:
#         l += 1
#     else:
#         ans = max(ans, l)
#         l = 1
#     last = a[i]
# print(max(l, ans))

# Найди второе по величине различное число.
# a = [2, 2, 2]

# m = a[0]
# ans = None

# for i in range(1, len(a)):
#     if a[i] > m:
#         ans = m
#         m = a[i]
#     elif a[i] < m and (ans is None or a[i] > ans):
#         ans = a[i]

# print(ans)

# Нужно посчитать количество элементов, которые строго больше обоих своих соседей

# a = [-2, -1, -3]
# c = 0
# for i in range(1, len(a) - 1):
#     if a[i - 1] < a[i] and a[i + 1] < a[i]:
#         c += 1
# print(c)

# Найди длину самого длинного непрерывного участка, на котором каждое следующее число строго больше предыдущего + индексы начала и конца
# a = [3, 4, 1, 2, 5, 7, 2, 3, 4, 5, 1]

# ans = 1
# length = 1

# lm = rm = 0
# lc = rc = 0

# last = a[0]

# for i in range(1, len(a)):
#     if a[i] > last:
#         length += 1
#         rc = i
#     else:
#         length = 1
#         lc = rc = i

#     if length >= ans:
#         ans = length
#         lm = lc
#         rm = rc

#     last = a[i]

# print(ans, f"от {lm} до {rm}")

# Напиши алгоритм, который находит индексы двух различных элементов, сумма которых равна
# a = [2, 4, 5, 7, 9, 1, 1]
# target = 16
# r = len(a) - 1
# l = 0
# while a[l] + a[r] != target and l < r:
#     if a[l] + a[r] > target:
#         r -= 1
#     elif a[l] + a[r] < target:
#         l += 1
# if l >= r:
#     print("Пара не найдена")
# else:
#     print(l, r)

# проверить является ли строка палиндромом
# s = "А роза упала на лапу Азора"
# s = s.replace(" ", "")
# r = len(s) - 1
# l = 0
# pal = True
# while l != r and l < r:
#     if pal == False:
#         break
#     if s[r].lower() != s[l].lower():
#         pal = False
#     else:
#         r -= 1
#         l += 1
# if pal == True:
#     print("Палиндром")
# else:
#     print("не палиндром")

# a = [4, -2, 7, -5, 3, 6]

# pref = [0]
# for x in a:
#     pref.append(pref[-1] + x)

# print(pref[4] - pref[1])
# print(pref[6] - pref[2])
# print(pref[6] - pref[0])

# a = [4, 2, 7, 1, 8, 3, 5]
# k = 3
# s = 0
# rm = lm = lc = 0
# rc = k - 1
# for x in range(k):
#     s += a[x]
# m = s
# j = 0
# for i in range(k, len(a)):
#     s = s - a[j] + a[i]
#     lc += 1
#     rc += 1
#     if s > m:
#         m = s
#         lm = lc
#         rm = rc
#     j += 1
# print(m, lm, rm)

# Найди минимальную длину непрерывного участка, сумма которого не меньше target
a = [1, 2, 3, 4, 5]
target = 8
