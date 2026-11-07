def wyswietl():
        print("========== KALKULATOR ==========")
        print("1. Dodawanie")
        print("2. Odejmowanie")
        print("3. Mnozenie")
        print("4. Dzielenie")
        print("5. Potegowanie")
        print("6. Srednia z podanych liczb")
        print("0. Zakoncz")
        print("================================")
def dodawanie():
          a = int(input("podaj liczbe a: "))
          b = int(input("podaj liczbe b: "))
          print(a," + ",b," = ",a+b)
def odejmowanie():
          a = int(input("podaj liczbe a: "))
          b = int(input("podaj liczbe b: "))
          print(a," - ",b," = ",a-b)
def mnozenie():
         a = int(input("podaj liczbe a: "))
         b = int(input("podaj liczbe b: "))
         print(a," x ",b," = ",a*b)
def dzielenie():
         a = int(input("podaj liczbe a: "))
         b = int(input("podaj liczbe b: "))
         if b != 0:
             print(a," / ",b," = ",a/b)
def potega():
         a = int(input("podaj liczbe a: "))
         b = int(input("podaj liczbe b: "))
         print(a," ^ ",b," = ",a**b)
def srednia():
        ile = int(input("ile liczb: "))
        if type(ile) == int:
            suma = 0
            for i in range(1,ile+1):
                print("podaj cyfre nr: ",i)
                cyfra = input(" ")
                suma += int(cyfra)
        print("srednia: ",suma/ile)
        

            

while True:
        wyswietl()
        opcja = int(input("podaj opcje"))
        if opcja == 1:
            dodawanie()
        if opcja == 2:
            odejmowanie()
        if opcja == 3:
            mnozenie()
        if opcja == 4:
            dzielenie()
        if opcja == 5:
            potega()
        if opcja == 6:
            srednia()
        if opcja == 0:
              break      
