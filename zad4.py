wiek = int(input("Podaj wiek: "))
opiekun = str(input("Opiekun? "))
dowod = str(input("Dowod? "))

if wiek >= 18 and dowod == "tak":
    print("Wypożyczenie możliwe")
elif wiek <= 17 and wiek >= 13 and dowod == "tak" and opiekun == "tak":
        print("Wypożyczenie możliwe")
else:
      print("Wypożeczenie niemożliwe") 