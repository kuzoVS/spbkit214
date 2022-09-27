import math

global a, b, c, num1, num2
def cacl():
    oper = input(""" 
        Выберите действие которое хотите совершить
        1 Сложение
        2 Вычитание
        3 Умножение
        4 Деление
        5 Квадратное уравнение
        """)

    if oper == '1' or oper == '2' or oper == '3' or oper == '3' or oper == '4':
        num1 = float(input("""Введите первое число: """))
        num2 = float(input("""Введите второе число: """))
    elif oper == '5':
        a = float(input("""Введите a: """))
        b = float(input("""Введите b: """))
        c = float(input("""Введите c: """))
    else:
        print('Выберите существущее действие из списка')

    if oper == '1':
        print(num1, '+', num2)
        print(num1 + num2)
    elif oper == '2':
        print(num1, '-', num2)
        print(num1 - num2)
    elif oper == '3':
        print(num1, '*', num2)
        print(num1 * num2)
    elif oper == '4':
        print(num1, '/', num2)
        print(num1 / num2)
    elif oper == '5':
        dscrmnt = b ** 2 - 4 * a * c
        if dscrmnt == 0:
            x1 = -b / (2 * a)
            print('x = ', x1)
        elif dscrmnt > 0:
            x1 = (-b + math.sqrt(dscrmnt)) / (2 * a)
            x2 = (-b - math.sqrt(dscrmnt)) / (2 * a)
            print('x1= ', x1, '\nx2= ', x2)
        else:
            print('Корней нет')

def snova():
    ysnt = input("""Вы хотите сосчитать еще что-то ?
    Если ДА нажмите Y
    Если НЕТ нажмите N
    """)
    if ysnt == 'Y' or ysnt == 'y':
        cacl()
        snova()
    elif ysnt == 'N' or ysnt == 'n':
        print('Пока...')

cacl()
snova()
