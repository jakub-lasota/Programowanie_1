slownik = {"777666555": ("jan","nowak")}
while True:
    print("========== KSIAZKA KONTAKTOW ==========")
    print("1. Dodaj kontakt")
    print("2. Wyswietl wszystkie kontakty")
    print("3. Wyszukaj kontakt")
    print("4. Edytuj kontakt")
    print("5. Usun kontakt")
    print("0. Zakoncz")
    print("=======================================")
    print("Wybierz opcje:")
    opcja = int(input("wybierz opcje: "))
    if opcja == 1:
        tel = str(input("podaj numer telefonu: "))
        imie = str(input("podaj imie: "))
        nazwisko = str(input("podaj nazwisko: "))
        if tel in slownik.keys():
            print("juz jest ten numer")
        else:
            slownik[tel] = [imie,nazwisko]
    if opcja == 2:
        for key,value in slownik.items():
            print(key,value)
    if opcja == 3:
        w_tel = str(input("podaj nr do wyszukania: "))
        print(slownik[w_tel])
    if opcja == 4:
        e_tel = str(input("podaj numer do edycji: "))
        if e_tel in slownik:
            n_imie = str(input("podaj nowe imie: "))
            n_nazwisko = str(input("podaj nowe nazwisko: "))
            slownik[e_tel] = [n_imie,n_nazwisko]
        else:
            print("nie ma takiego telefonu")
    if opcja == 5:
        u_tel = str(input("podaj numer do usuniecia: "))
        if u_tel not in slownik.keys():
            print("nie ma takiego numeru")
        else:
            slownik.pop(u_tel)
    if opcja == 0:
        break
    if opcja > 5:
        print("blad wyboru")