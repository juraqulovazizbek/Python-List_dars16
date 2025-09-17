son = [1, 2, 3, 7, 8, 9] 
sonlar = []

for az in range(len(son)):
    for af in range (az+1 , len (son)):
        if son[az]+son[af] == 10:
            sonlar.append((son[az], son[af]))

print(sonlar)