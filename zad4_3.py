wydatki = [["biedronka",50,"w"],["praca",200,"p"],["cos",500,"p"]]

while True:
    print("========= MOJ BUDZET =========")
    print("1. Dodaj przychod")
    print("2. Dodaj wydatek")
    print("3. Wyswietl historie operacji")
    print("4. Wyswietl stan konta")
    print("5. Podsumowanie finansowe")
    print("6. Usun operacje")
    print("0. Zakoncz")
    print("==============================")
    print("Wybierz opcje:")
    opcja = int(input("podaj opcje: "))
    if opcja == 1:
        tytul = input("podaj tytul: ")
        kwota = int(input("podaj kwote: "))
        if kwota > 0:
            wydatki.append([tytul,kwota,"p"])
            print("dodano przychod")
        else:
            print("Nieprawidlowe dane ")
    if opcja == 2:
            tytul = input("podaj tytul: ")
            kwota = input("podaj kwote: ")
            if kwota > 0:
                wydatki.append([tytul,kwota,"w"])
                print("dodano wydatek")
            else:
                print("Nieprawidlowe dane ")
    if opcja == 3:
            for wyraz in wydatki:
                 print(wyraz)
    if opcja == 4:
         bilans = 0
         for i in range(0,len(wydatki)):
              if wydatki[i][2] == "p":
                   bilans += wydatki[i][1]
              if wydatki[i][2] == "w":
                    bilans -= wydatki[i][1]
         print(bilans)
    if opcja == 5:
         bilans_p = 0
         bilans_w = 0
         w_max = 0
         p_max = 0
         for i in range(0,len(wydatki)):
                       if wydatki[i][2] == "p":
                            bilans_p += wydatki[i][1]
                            if wydatki[i][1] > p_max:
                                  p_max = wydatki[i][1]
                       if wydatki[i][2] == "w":
                             bilans_w += wydatki[i][1]
                             if wydatki[i][1] > w_max:
                                   w_max = wydatki[i][1]
         print("bilans przychodow: ",bilans_p)
         if p_max > 0:
               print("maks przychod: ",p_max)
         else:
               print("brak przychodow")
         print("bilans wydatkow: ",bilans_w)
         if w_max > 0:
                        print("maks wydatkow: ",w_max)
         else:
                        print("brak wydatkow")
    if opcja == 6:
           usun = int(input("podaj numer operacji: "))
           if usun < len(wydatki):
                  wydatki.pop(usun)
           else:
                  print("nie ma takiego elementu")
    if opcja ==0:
           break
    if opcja > 6:
           print("blad wyboru")
               
         