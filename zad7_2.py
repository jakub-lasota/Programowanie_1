magazyn = {"Mysz": 5, "Klawiatura": 3, "Monitor": 2}

while True:
    print("-----------------")
    print("1. Stan magazynu")
    print("2. Przyjecie towaru")
    print("3. Wydanie towaru")
    print("0 - Zakoncz")
    print("-----------------")
    opcja = int(input("Podaj opcje "))
    if opcja == 1:
        for key,value in magazyn.items():
            print("Nazwa produktu: ",key)
            print("Liczba sztuk: ",value)
    if opcja == 2:
        towar = str(input("Podaj typ towaru: "))
        ilosc = int(input("Podaj jego ilosc: "))
        if towar in magazyn:
            magazyn[towar] += ilosc
        else:
            magazyn[towar] = ilosc
    if opcja == 3:
        usun = str(input("podaj co usunac: "))
        ile_us = int(input("podaj ile usunac: "))
        if usun in magazyn:
            if magazyn[usun] >= ile_us:
                magazyn[usun] -= ile_us
            else:
                print("Nie ma tyle sztuk")
        else:
            print("Nie ma tego w magazynie")
    if opcja == 0:
        break