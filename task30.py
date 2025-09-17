matn =[]

for az in range (5):
    soz = input(f"{az+1}-so'zlarni kiriting: ")
    matn.append(soz)
palindrom = []
for af in matn:
 if af == af[::-1]:
    palindrom.append(af)

print("Kiritilgan so‘zlar:", matn)
print("Palindrom so‘zlar:", palindrom)