def func1(x, y, z):
    print('X=', x,'\nY=', y,'\nZ=', z )

def func2(name: str, age):
    print('Name:', name,'(', age,' y.o)')

def func3(x1: int, y1:int, x2:int, y2:int):
    if abs(x1-x2) <= 1 and abs(y1-y2) <= 1:
        print("YES")
    else:
        print("NO")

def func4(a: list, b:list):
    c = []
    if len(a) > len(b):
        x = len(a)
    else:
        x = len(b)
    for i in range(x):
        print(i)
        try:
            c.append([a[i], b[i]])
            if i > (len(a)-1):
                c.append(b[i])
            if i > (len(b)-1):
                c.append(a[i])
        except:
            if i > (len(a)-1):
                c.append(b[i])
            if i > (len(b)-1):
                c.append(a[i])
        
    print(c)

def calculation(x, y):
    print("+:", x+y, "\n-:", x-y)

