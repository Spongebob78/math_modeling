print('1 - прямоугольник, 2 - треугольник, 3 - круг')
what = input('Фигура: ')

def pram(a, b):
    return a * b

def treg(a, b, c):
    p = (a + b + c) / 2
    return 0.5 * (p * (p -a) * (p - b) * (p - c))

def crug(r):
    return 3,14 * r**2

if what == '1':
    a = float(input())
    b = float(input())
    print('Площадь прямоугольника: ', pram(a, b))
elif what == '2':
    a = float(input())
    b = float(input())
    c = float(input())
    print('Площадь треугольника: ', treg(a, b, c))
elif what == '3':
    r = float(input())
    print('Площадь круга: ', crug(r))
else:
    print('Ошибка')
