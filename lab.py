# 1 Чуствителен
# 2 Можно,lower(). В верхний upper()
# 3 "#"
# 4 int, float, complex, string, list, tuple, dict, bool
# 5 input()
# 6 a='2421' a = int(a)
# 7 len(a)
# 8 break
# 9 Последовательно
from datetime import datetime

#1)
def first_task():
    x = float(input("Введите x = "))
    y = float(input("Введите y = "))
    if x <= y <= 1 <= x + y:
        res = "В зоне"
    else:
        res = "Вне зоны"
    return res
#2)
def second_task():
    t = input("Начало (H:MM) = ")
    t = t.split(":")
    tm = float(t[1]
    t = float(t[0]) + (float(t[1]) / 60)
    s = int(input("Стоимость = "))
    d = int(input("День(1-7) = "))
    dt = int(input("Длительность = "))
    for i in range(dt):
        if 7 < t < 22 and d < 6:
            st = s
        elif 7 < t < 22 and d >= 6:
            st = s
            st = st - st * 0.1
        elif (22 <= t <= 23 or 0 <= t <= 7) and d < 6:
            st = s
            st = st - st * 0.2
        elif (22 <= t <= 23 or 0 <= t <= 7) and d >= 6:
            st = s
            st = st - st * 0.2
            st = st - st * 0.1

        tm += 1
        if tm == 60:
            t += 1
        else:
            t = t
        res = res + st
    return res
    # curent_date = datetime.now()
    # t = curent_date.hour
    # d = curent_date.weekday()
#3
def third_task():
    choice = int(input("1. Только одно четное \n"
                       "2. 3 числа кратны трем \n"))

    if choice == 1:
        a = int(input("Введите число a = "))
        b = int(input("Введите число b = "))
        if a % 2 == 0 and b % 2 == 0 or a % 2 == 1 and b % 2 == 1:
            res = "Неверно"
        else:
            res = "Верно"

    elif choice == 2:
        a = int(input("Введите число a = "))
        b = int(input("Введите число b = "))
        c = int(input("Введите число c = "))
        if a % 3 == 0 and b % 3 == 0 and c % 3 == 0:
            res = "Верно"
        else:
            res = "Неверно"
    return res
