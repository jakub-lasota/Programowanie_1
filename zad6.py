aktualna_temp = int(input("podaj aktualna temperature "))
ktos_w_domu = str(input("Czy ktos jest w domu "))
czy_okno_otwarte = str(input("Czy okno jest otwarte "))

if czy_okno_otwarte == "tak":
    print("Ogrzewanie WYLACZONE")
    print("Powod: otwarte okno")
elif czy_okno_otwarte == "nie" and ktos_w_domu == "tak" and aktualna_temp < 20:
    print("Ogrzewanie WLACZONE")
    print("Powod: temperatura ponizej 20" )
elif czy_okno_otwarte == "nie" and ktos_w_domu == "nie" and aktualna_temp < 16:
    print("Ogrzewanie WLACZONE")
    print("Powod: temperatura ponizej 16" )
else:
    print("Ogrzewanie WYLACZONE")

