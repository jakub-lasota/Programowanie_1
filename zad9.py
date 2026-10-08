pocz = int(input("Podaj poczatek zakresu "))
kon = int(input("Podaj koniec zakresu "))

for i in range(pocz,kon+1):
    if i % 2 == 0:
        print("Liczba ",i," jest parzysta ")
    else:
        print("Liczba ",i," jest nieparzysta ")
