import matplotlib.pyplot as plt
nazwiska = []
pkt = []
liczba_s = int(input("podaj liczbe studentow"))
zaliczeni = 0
suma = 0
for i in range(1,liczba_s+1):
    nazwisko = str(input("podaj nazwisko studenta "))
    punkty = int(input("Podaj ocene: "))
    suma += punkty
    nazwiska.append(nazwisko)
    if punkty >= 50:
        zaliczeni = zaliczeni + 1
    print("Liczba punktow: ", punkty)
    if punkty <= 100 and punkty >= 90:
        print("Ocena: 5.0"," ",nazwisko)
        pkt.append(5.0)
    elif punkty <= 89 and punkty >= 80:
        print("Ocena: 4.5"," ",nazwisko)
        pkt.append(4.5)
    elif punkty <= 79 and punkty >= 70:
        print("Ocena: 4.0"," ",nazwisko)
        pkt.append(4.0)
    elif punkty <= 69 and punkty >= 60:
        print("Ocena: 3.5"," ",nazwisko)
        pkt.append(3.5)
    elif punkty <= 59 and punkty >= 50:
        print("Ocena: 3.0"," ",nazwisko)
        pkt.append(3.0)
    else:
        print("Ocena: 2.0"," ",nazwisko)
        pkt.append(2.0)

print("srednia: ",suma/liczba_s)
print("zdalo: ",zaliczeni)
plt.bar(nazwiska,pkt)
plt.title("wyniki egzaminu")
plt.xlabel("student")
plt.ylabel("ocena")
plt.ylim(0,5.5)
plt.show()