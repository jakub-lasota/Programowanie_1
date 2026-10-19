zadania = []
while True:
    
    print("-----------------")
    print("1. Dodaj zadanie")
    print("2. Wyswietl zadanie")
    print("3. Usun zadanie")
    print("4. Liczba zadan")
    print("0 - Zakoncz")
    print("-----------------")
    pol = int(input("Podaj nr polecenia: "))
    if pol == 1:
        el = str(input("Podaj zadanie: "))
        zadania.append(el)
    if pol == 2:
        for i in range(0,len(zadania)):
            print(str(i+1)+". "+zadania[i])
    if pol == 3:
        usun = int(input("Podaj nr zadania do usuniecia "))
        if usun >= 0 and usun <= len(zadania):
            usun -= 1
            zadania.pop(usun)
        else: 
            print("Nieprawidlowy element ")
    if pol == 4:
        if len(zadania) > 0:
            print("Liczba zadan: ",len(zadania))
        else:
            print("Brak zadan")
    if pol == 0:
        print("do widzenia ")
        break
