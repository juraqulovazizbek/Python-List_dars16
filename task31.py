sonlar = [3, 5, 3, 2, 5, 5, 1]

eng_kop = 0
eng_kop_element = None

for element in sonlar:
    miqdor = sonlar.count(element)
    if miqdor > eng_kop:
        eng_kop = miqdor
        eng_kop_element = element

print(eng_kop_element)