#  обмен значений между двумя переменными, не используя третьей
a =int(input('введите a'))
b = int(input('введите b'))
print('было')
print('a = ', a)
print('b = ', b)

# 1 способ
a,b =b,a
print('стало')
print('a =', a)
print('b = ', b)

# 2 способ
a = a + b
b = a - b
a = a - b
print('стало по второму способу')
print('a =', a)
print('b = ', b)

