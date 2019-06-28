list = [2, 8, 3, 6, 1,5,1]
new_list =[]
for dig in list:
    if dig % 2 == 0:
        new_list.append(dig/4)
    else:
        new_list.append(dig*2)

print(new_list)

