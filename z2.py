ile = int(input("podaj ile produktow "))
produkty = []
ceny = []
for i in range (0,ile):
        produkt = str(input("podaj produkt"))
        produkty.append(produkt)
        cena = int(input("podaj cene"))
        ceny.append(cena)

for numer,wyraz in enumerate(produkty, start=1):
    print(numer,wyraz)
for produkt,cena in zip(produkty,ceny):
    print(produkt,cena)
print(sum(ceny))
print("najdrozszy produkt ",produkty[ceny.index(max(ceny))]," cena ", max(ceny))

