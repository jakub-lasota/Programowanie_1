napoje = ["Woda","Sok","Cola"]
cena = [3,5,6]
suma = 0
while True:
    print("1.",napoje[0]," - ",cena[0])
    print("2.",napoje[1]," - ",cena[1])
    print("3.",napoje[2]," - ",cena[2])
    dodaj = int(input("Wybierz opcje 1-3 || wyjscie = 0 "))
    if dodaj == 0:
        break
    suma += cena[dodaj-1]

print("laczna suma: ",suma)