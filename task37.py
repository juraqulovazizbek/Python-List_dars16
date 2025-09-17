list1 = input("1-ro‘yxat elementlarini vergul bilan kiriting: ").split(',')
list2 = input("2-ro‘yxat elementlarini vergul bilan kiriting: ").split(',')

# Har ikkala ro‘yxatni tozalash (bo'sh joylarni olib tashlash)
list1 = [i.strip() for i in list1]
list2 = [i.strip() for i in list2]

# Uzunliklari tengligini tekshirish
if len(list1) != len(list2):
    print("Ro‘yxatlar uzunligi teng emas!")
else:
    for i in range(len(list1)):
        list1[i], list2[i] = list2[i], list1[i]

    print("Yangi 1-ro‘yxat:", list1)
    print("Yangi 2-ro‘yxat:", list2)