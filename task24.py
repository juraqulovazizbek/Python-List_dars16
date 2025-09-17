matn = input("matn: ")
soz = input("qaysi so'z izlamoqchisiz: ")
result = matn.lower().count(soz.lower())
print( f"matnda  shuncha {soz} {result}ta bor")