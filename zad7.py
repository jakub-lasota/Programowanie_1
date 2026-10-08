kwota_odkl = int(input("Wprowadz kwote odkladana co tydzien "))
liczba_tyg = int(input("Wprowadz liczbe tygodni "))
suma_p = 0

for i in range(1,liczba_tyg+1):
    suma_p += kwota_odkl
    print("tydzien nr. ",i, " oszczedzona suma ", suma_p)

print("Laczne oszczednosci: ", suma_p)
