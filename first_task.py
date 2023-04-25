
# Задание №1: FizzBuzz
# for i in range(1, 101):
#     if i % 3 == 0 and i % 5 == 0:
#         print("FizzBuzz")
#     elif i % 3 == 0:
#         print("Fizz")
#     elif i % 5 == 0:
#         print("Buzz")
#     else:
#         print(i)


# ------------------------------------------------------
# Задание №2: Отсортировать 1-й список по элементам 2-го
# a = [1, 4, 6]
# b = [11, 33, 22]

# a = [v for v, _ in sorted(zip(a, b), key=lambda x: x[1])]

# print(a)  # [1, 6, 4]
# print(b)  # [11, 33, 22]


# ------------------------------------------------------
# Задание №3: Дан список строк. Нужно вывести все буквы, 
# которые встречаются в каждой из строк списка (включая дубликаты).
# list1 = ['bella', 'label', 'roller']
# list2 = ['cool', 'lock', 'cook']

# def common_chars(lst: list[str]) -> list[str]:
#     if not lst:
#         return []
    
#     result = []
    
#     for char in set(lst[0]):
#         count = min(s.count(char) for s in lst)
#         result.extend([char] * count)

#     return sorted(result)

# print(common_chars(list1))  # ['e', 'l', 'l']
# print(common_chars(list2))  # ['c', 'o']


# ---------------------------------------------------------------
# Задание №4: Дана римская цифра, преобразовать ее в целое число.
# costs = {
#     'I': 1,
#     'V': 5,
#     'X': 10,
#     'L': 50,
#     'C': 100,
#     'D': 500,
#     'M': 1000
# }

# def roman_to_int(s: str) -> int:
#     total_sum = 0

#     for l, r in zip(s, s[1:]):
#         if costs[l] < costs[r]:
#             total_sum -= costs[l]
#         else:
#             total_sum += costs[l]

#     total_sum += costs[s[-1]]  # последний символ
#     return total_sum


# print(roman_to_int('IV'))  # 4
# print(roman_to_int('DLV'))  # 555
# print(roman_to_int('MCMXC'))  # 1990
# print(roman_to_int('MMXIV'))  # 2014


