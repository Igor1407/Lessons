# Задача-3: Напишите алгоритм, заполняющий список произвольными целыми числами
# в диапазоне от -100 до 100. В списке должно быть n - элементов.
# Подсказка:
# для получения случайного числа используйте функцию randint() модуля random
import random
list1 = []
n = int(input("введите число элементов списка\n"))
for dig in range (n):
    list1.append(random.randint(-100,100))

print(list1)







