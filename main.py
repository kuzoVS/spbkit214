import math
from statistics import mean
#1
print('1 задание')
#a
a = (101 + 0) / 3
print(a)
#b
b = 3.0 * math.e - 6 * 10000000.1
print(b)
#c
c = True and True
print(c)
#d
d = True and False
print(d)
#e
e = (False and False) or (True and True)
print(e)
#f
f = (False or False) and (True and True)
print(f)
#2
print('2 задание')
def danet(a , b, c, d):
  if a == b and c == d and d == b:
    otvet = "Равно"
  else:
    otvet = "Не равно"
  return otvet

a = int(input('1 '))
b = int(input('2 '))
c = int(input('3 '))
d = int(input('4 '))
print(danet(a, b, c, d))
#3
print('3 задание')
mass = [1, 3, 5, 213, 534, 23, 56, 13 ,4, 5, 65, 43,2 ,234, 25,52, 452, 12,43,242, 3 ,4,23 ]
k = int(input("Сколько чисел из 9: "))
for i in range(k):
  mars = max(mass)
  mass.remove(mars)
  print(mars)
  
#4
print('4 задание')
k = int(input("Сколько чисел из 9: "))
for i in range(k):
  mars = min(mass)
  mass.remove(mars)
  print(mars)
#5
print('5 задание')
mass = [1, 3, 5, 213, 534, 23, 56, 13 ,4, 5, 65, 43,2 ,234, 25,52, 452, 12,43,242, 3 ,4,23 ]
for i in range(len(mass)):
  if mean(mass) < mass[i]:
    print(mass[i])
#6
print('6 задание')
a = int(input("1 "))
b = int(input("2 "))
resu = 0
for i in range(b):
  resu = a + resu
print(resu)
#7
print('7 задание')
mass = [1, 3, 5, 213, 534, 23, 56, 13 ,4, 5, 65, 43,2 ,234, 25,52, 452, 12,43,242, 3 ,4,23 ]
chet = []
nechet = []
for i in range(8):
  if mass[i] % 2 == 0:
    chet.append(mass[i])
  else:
    nechet.append(mass[i])
print("Четные ", chet[:])
print("Нечетные", nechet[:])
#8
print('8 задание')
a = float(input("Цельсий = "))
print("Фаренгейт = ", (a * (9/5) + 32))
#9
print('9 задание')
rost = float(input("Рост(m): "))
ves = float(input("Вес(kg): "))
print("ИМТ = ", ves / (rost**2))
#10
print('10 задание')
a = float(input("a = "))
print("a^2 = ", a**2)
print("a^3 = ", a**3)
print("a^4 = ", a**4)
#11
print('11 задание')
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
if a + b > c and a + c > b and  b + c > a:
  print("Треугольник существует")
else:
  print("Треугольник не существует")
