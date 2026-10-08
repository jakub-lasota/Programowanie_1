cena_produktu = int(input(" Podaj cene produktu "))
liczba_produktow = int(input(" Podaj liczbe produktow "))
koszt_dostawy = 12

wartosc_produktu = cena_produktu*liczba_produktow
if wartosc_produktu >= 100:
    koszt_dostawy = 0

laczna_wartosc = koszt_dostawy + wartosc_produktu
print("wartosc produktow: ",wartosc_produktu," koszt dostawy: ",koszt_dostawy," laczna wartosc: ", laczna_wartosc)
