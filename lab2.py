#1)
def first_task():
    x = int(input("Введите год = "))
    if x % 4 == 0 or (x % 100 == 0 and x % 400 == 0):
        res = "Високосный"
    else:
        res = "Не високосный"
    print(res)
#2)
def second_task():
    num = int(input("Введите сумму = "))
    if num % 10 == 1 and num % 100 != 11:
        res = str(num) + ' копейка'
    elif num % 10 in [2, 3, 4] and num % 100 not in [12, 13, 14]:
        res = str(num) + ' копейки'
    else:
        res = str(num) + ' копеек'
    print(res)
#3
def third_task():
    bitrth = str(input("Введите дату рождения в формате DD.MM: "))
    bitrth = bitrth.split(".")
    day = int(bitrth[0])
    mon = int(bitrth[1])
    if mon == 12:
        znak = 'Стрелец' if (day < 22) else 'Козерог'
    elif mon == 1:
        znak = 'Козерог' if (day < 20) else 'Водолей'
    elif mon == 2:
        znak = 'Водолей' if (day < 19) else 'Рыбы'
    elif mon == 3:
        znak = 'Рыбы' if (day < 21) else 'Овен'
    elif mon == 4:
        znak = 'Овен' if (day < 20) else 'Телец'
    elif mon == 5:
        znak = 'Телец' if (day < 21) else 'Близнецы'
    elif mon == 6:
        znak = 'Близнецы' if (day < 21) else 'Рак'
    elif mon == 7:
        znak = 'Рак' if (day < 23) else 'Лев'
    elif mon == 8:
        znak = 'Лев' if (day < 23) else 'Дева'
    elif mon == 9:
        znak = 'Дева' if (day < 23) else 'Весы'
    elif mon == 10:
        znak = 'Весы' if (day < 23) else 'Скорпион'
    elif mon == 11:
        znak = 'Скорпион' if (day < 22) else 'Стрелец'
    print("Твой знак зодиака: ", znak)

def fourth_task():
    d = int(input("Введите день: "))
    days = ["Null", "Пн", "Вт", "Ср", "Чт", "Пт", "Сб", "Вс"]
    md = d % 7
    print(str(days[md]))

