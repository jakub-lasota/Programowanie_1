czas = int(input("Podaj czas parkowania: "))
if czas <=0:
    print("nieprawidlowe dane")
elif czas == 1:
    oplata = 10
elif czas > 1 and czas <= 3:
    oplata = 12
elif czas > 3 and czas <= 6:
    oplata = 20
elif czas > 6:
    oplata = 30
print("czas postoju: ",czas," h")
print("oplata za parking ", oplata)
