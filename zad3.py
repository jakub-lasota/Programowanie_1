cena_produktu = int(input("Podaj cene produktu "))
rabat = int(input("Podaj rabat "))
kwota_rabatu = cena_produktu*(rabat/100)

print("Cena produktu: ",cena_produktu)
print("Kwota rabatu: ",kwota_rabatu)
print("Cena po rabacie: ",cena_produktu-kwota_rabatu)
if rabat >= 20:
    print("Duza promocja")