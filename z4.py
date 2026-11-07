warsztat_python = set()
warsztat_ai = set()
while True:
     print("1 - zapisz na python")
     print("2 - zapisz na aj")
     print("3 - wypisz uczestnikow")
     print("4 - uczestnicy obu warsztatow")
     print("5 - wszyscy unikalni klienci")
     print("0 - zakoncz")
     opcja = int(input("podaj opcje "))
     if opcja == 1:
          imie = str(input("podaj imie "))
          nazwisko = str(input("podaj nazwisko "))
          info = (imie,nazwisko)
          if info not in warsztat_python:
            warsztat_python.add(info)
          else:
               print("nie mozna")
     if opcja == 2:
              imie = str(input("podaj imie "))
              nazwisko = str(input("podaj nazwisko "))
              info = (imie,nazwisko)
              if info not in warsztat_ai:
                warsztat_ai.add(info)
              else:
                   print("nie mozna")
     if opcja == 3:
          print(warsztat_ai | warsztat_python)
     if opcja == 4:
          print(warsztat_ai & warsztat_python)
     if opcja == 5:
          for wyraz in warsztat_python:
               if wyraz not in warsztat_ai:
                    print(wyraz)
          for wyraz in warsztat_ai:
               if wyraz not in warsztat_python:
                    print(wyraz)
