import math

print("Введите координаты точки и радиус круга")
x_point = float(input("x = "))
y_point = float(input("y = "))
r_circle = float(input("R = "))

hypotenuse = math.sqrt(x_point ** 2 + y_point ** 2)

if hypotenuse <= r_circle:
    print("Монетка где-то рядом")
else:
    print("Монетки в области нет")