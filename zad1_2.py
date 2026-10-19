tab = []
ile_p = int(input("Podaj ile produktow chcesz dodac: "))
for i in range(0,ile_p):
    produkt = str(input("Podaj produkt: "))
    tab.append(produkt)
print(tab)
print("ilosc elementow: ",len(tab))
usun = str(input("Podaj produkt do usuniecia: "))
if usun not in tab:
    print("produkt nie istnieje ")
else:
    tab.remove(usun)
    print(tab)



    

