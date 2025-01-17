# вычисляем формулу
import math

print("Введите коэффициенты для квадратного уравнения (ax^2 + bx + c = 0):")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

discr = b ** 2 - 4 * a * c
print("Дискриминант D = ",  discr)

if discr > 0:
    x1 = (-b + math.sqrt(discr)) / (2 * a)
    x2 = (-b - math.sqrt(discr)) / (2 * a)
    print("x1 = %0.2f" % x1)
    print("x2 = %0.2f "% x2)
elif discr == 0:
    x = -b / (2 * a)
    print("x = ", x)
else:
    print("Корней нет")