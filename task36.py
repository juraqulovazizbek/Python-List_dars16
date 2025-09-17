sozlar = input("So‘zlarni vergul bilan kiriting: ").split(',')

eng_uzun = ""
for soz in sozlar:
    soz = soz.strip()
    if len(soz) > len(eng_uzun):
        eng_uzun = soz

print("Eng uzun so‘z:", eng_uzun)