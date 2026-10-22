while True: 
    print("========== KALKULATOR ==========")
    print("1. Dodawanie")
    print("2. Odejmowanie")
    print("3. Mnozenie")
    print("4. Dzielenie")
    print("5. Potegowanie")
    print("6. Srednia z podanych liczb")
    print("0. Zakoncz")
    print("================================")
    print("Wybierz opcje:")
    opcja = int(input("Podaj opcje: "))
    if opcja > 6:
        print("niepoprawna opcja")
    if opcja == 1:
        
        a = int(input("podaj liczbe a: "))
        b = int(input("podaj liczbe b: "))
        if type(a) == int and type(b) == int:
            print(a," + ",b," = ",a+b)
        else:
              print("nie podano cyfry")
    if opcja == 2:
        a = int(input("podaj liczbe a: "))
        b = int(input("podaj liczbe b: "))
        if type(a) == int and type(b) == int:
            print(a," - ",b," = ",a-b)
        else:
                      print("nie podano cyfry")
    if opcja == 3:
            a = int(input("podaj liczbe a: "))
            b = int(input("podaj liczbe b: "))
            if type(a) == int and type(b) == int:
                print(a," x ",b," = ",a*b)
            else:
                          print("nie podano cyfry")
    if opcja == 4:
            a = int(input("podaj liczbe a: "))
            b = int(input("podaj liczbe b: "))
            if type(a) == int and type(b) == int:
                if b!= 0:
                    
                    print(a," / ",b," = ",a/b)
                else:
                    print("dzielnik nie moze byc 0 ")
            else:
                          print("nie podano cyfry")
    if opcja == 5:
                a = int(input("podaj liczbe a: "))
                b = int(input("podaj liczbe b: "))
                if type(a) == int and type(b) == int:
                    print(a," ^ ",b," = ",a**b)
                else:
                              print("nie podano cyfry")
    if opcja == 6:
                ile = int(input("ile liczb: "))
                if type(ile) == int:
                    suma = 0
                    for i in range(1,ile+1):
                        print("podaj cyfre nr: ",i)
                        cyfra = input(" ")
                        suma += int(cyfra)
                    print("srednia: ",suma/ile)
    if opcja == 0:
           break 
   
                       


