list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7]

umumiy = []
for son in list1:
    if son in list2 and son not in umumiy:
        umumiy.append(son)

print(umumiy)