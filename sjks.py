from random import randint
spisok = []
i = 0
plus = 0
minus = 0
print("15 чисел ")
while len(spisok) != 15:
    a = randint (-100, 100)
    if a == 0:
        a = randint (-100, 100)
    else:
        spisok.append(a)
while i < len(spisok):
    if spisok[i] > 0:
        plus = plus + spisok[i]
        i += 1
    elif spisok[i] < 0:
        minus = minus + spisok[i]
        i += 1
print('Сумма положительных = ', plus)
print('Сумма отрицательных = ', minus)