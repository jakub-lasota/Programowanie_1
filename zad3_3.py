biblioteka = [["dzieci z bullerbyn","michael jackson",False]]
print(biblioteka[0][2])
while True:
        print("========== BIBLIOTEKA ==========")
        print("1. Dodaj ksiazke")
        print("2. Wyswietl wszystkie ksiazki")
        print("3. Wypozycz ksiazke")
        print("4. Zwroc ksiazke")
        print("5. Usun ksiazke")
        print("0. Zakoncz")
        print("===============================")
        print("Wybierz opcje: ")
        opcja = int(input("podaj opcje: "))
        if opcja == 1:
            autor = str(input("podaj autora: "))
            tytul = str(input("podaj tytul: "))
            biblioteka.append([autor,tytul,True])
        if opcja == 2:
              for wyraz in biblioteka:
                    print(wyraz)
        if opcja == 3:
              nr_k = int(input("podaj numer ksiazki: "))
              if biblioteka[nr_k][2] == True:
                    biblioteka[nr_k][2] = False
                    print("Wypozyczono ksiazke: ")
              else:
                    print("nie ma tej ksiazki na stanie")
        if opcja == 4:
              nr_k = int(input("podaj numer ksiazki: "))
              if biblioteka[nr_k] in biblioteka:
                    biblioteka[nr_k][2] = True
        if opcja == 5:
              nr_k = int(input("podaj numer ksiazki: "))
              if biblioteka[nr_k] in biblioteka:
                    biblioteka.pop(nr_k)
        if opcja == 0:
              break
        if opcja > 5:
              print("blad wyboru")