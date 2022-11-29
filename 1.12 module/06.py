X_min = -1
X_max = 1
Y_min = -1
Y_max = 1
x = float(input('Введите x: '))
y = float(input('Введите y: '))

def check_point(x, y):
    if (X_max > x > X_min) and (Y_max > y > Y_min):
        print('Монетка где-то рядом')
    else:
        print('Монетки в области нет')

check_point(x, y)