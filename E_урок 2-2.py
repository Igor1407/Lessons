# с помощью множества выделяем отличие
list1 =['один', 'три', 'пять', 'семь','восемь']
list2 = ['три','пять','шесть']
u = set(list2).difference(set(list1))
b = set(list1).difference(set(list2))
list3 = list(u)
list4 = list (b)
a = list3+list4
print (a)

# с помощью методов списка  выделяем отличия
list1 =['один', 'три', 'пять', 'семь','восемь']
list2 = ['три','пять','шесть']
list3 =[]
list4 = []
for a in list1:
    if a not in list2:
        list3.append(a)

for a in list2:
    if a not in  list1:
        list4.append(a)

a = list4+list3
print(a)





