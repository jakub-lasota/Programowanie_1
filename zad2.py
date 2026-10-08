punkty = int(input("Podaj ocene: "))
print("Liczba punktow: ", punkty)
if punkty <= 100 and punkty >= 90:
    print("Ocena: 5.0")
elif punkty <= 89 and punkty >= 80:
    print("Ocena: 4.5")
elif punkty <= 79 and punkty >= 70:
    print("Ocena: 4.0")
elif punkty <= 69 and punkty >= 60:
    print("Ocena: 3.5")
elif punkty <= 59 and punkty >= 50:
    print("Ocena: 3.0")
else:
    print("Ocena: 2.0")





