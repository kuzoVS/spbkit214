# 1 Чуствителен
# 2 Можно,lower(). В верхний upper
# 3 "#"
# 4 int, float, complex, string, list, tuple, dict, bool
# 5 input()
# 6 a='2421' int(a)
# 7 len(a)
# 8 break
# 9 Последовательно
from datetime import datetime

print("1")

x = float(input("Введите x = "))
y = float(input("Введите y = "))
if x <= y <= 1 <= x + y:
    print("В зоне")
else:
    print("Вне зоны")

print("2")


def strazg(t, dt, s, d):

    while tt == 0:
        if t >= 22 or t <= 8:
            if d == 6 or d == 7:
                print("1")
                res = (dt * s) - ((dt * s) * 0.2)
                res = res - (res * 0.1)
            else:
                res = (dt * s) - ((dt * s) * 0.2)
        else:
            if d == 6 or d == 7:
                print("2")
                res = (dt * s) - ((dt * s) * 0.1)
            else:
                print("3")
                res = dt * s
    return res


# curent_date = datetime.now()
# t = curent_date.hour
# d = curent_date.weekday()
t = input("Начало ")
t = t.split(":")
t = float(t[0]) + (float(t[1]) / 60)
print(t)
s = int(input("Стоимость "))
d = int(input("День "))
dt = int(input("Длительность "))
print(strazg(t, dt, s, d))
