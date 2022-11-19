import math
from random import randint
print("\n #1")
array1 = []
array2 = []
newarray = []
for i in range(10):
    a = randint(0, 100)
    b = randint(0, 100)
    array1.append(a)
    array2.append(b)
for i in range(len(array1)):
    if array2[i] % 2 == 0:
        newarray.append(array2[i])
    elif array1[i] % 2 != 0:
        newarray.append(array1[i])
print(array1)
print(array2)
print(newarray)

print("\n #2")
s1=10
for i in range(1, s1+1):
     print(*range(i, i*s1+1, i), sep='\t')

print('#3')

f = open('123.txt')
lines = f.readlines()
my_file = open("File.txt", "w+")
five = lines[4]
lines.remove(five)
for i in lines:
    my_file.write(str(i))
my_file.close()
f.close()

print('#4')
f = open('4.txt','r')
for i, line in enumerate(f):
    if i == 3:
        print(line)
print('#5')
otv = 0
n = int(input("впишите число: "))
if n == 0:
    n = int(input("впишите число не равное 0: "))
for i in range(1, n + 1):
    otv +=i
print(otv)

print('#6')

array = [321032103, 130013, 31398213, 328382, 4389843, 4389483,4327, 43, 43, 213]
for i in reversed(array):
    print(i)

print('#7')

lower = int(input("Введите нижний предел: "))
upper = int(input("Введите верхний предел: "))
print("В числа простые числа этого диапазона: ")
for number in range(lower, upper + 1):
    if number > 1:
        for i in range(2, number):
            if (number % i) == 0:
                break
        else:
            print(number)
