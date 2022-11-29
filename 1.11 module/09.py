import math

a = float(input())
b = float(input())
c = float(input())

D = b ** 2 - 4 * a * c

if D == 0:
    x1 = (-b - math.sqrt(D)) / (2*a)
    print(x1)
elif D > 0:
    x1 = (-b - math.sqrt(D)) / (2*a)
    x2 = (-b + math.sqrt(D)) / (2*a)

    if x1 > x2:
        print(x2, x1)
    else:
        print(x1, x2)