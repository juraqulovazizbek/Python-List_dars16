sozlar = input("So‘zlarni vergul bilan kiriting: ").split(',')

qisqa = []
orta = []
uzun = []

for soz in sozlar:
    soz = soz.strip()
    if len(soz) <= 3:
        qisqa.append(soz)
    elif 4 <= len(soz) <= 6:
        orta.append(soz)
    else:
        uzun.append(soz)

print("<=3 harfli:", qisqa)
print("4-6 harfli:", orta)
print(">6 harfli:", uzun)