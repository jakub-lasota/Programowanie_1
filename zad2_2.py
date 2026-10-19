lista = []
ile_zdalo = 0
l_stud = int(input("Podaj liczbe studentow "))
for i in range (1,l_stud+1):
    wynik = int(input("Podaj wynik studenta nr. "+str(i)+" "))
    lista.append(wynik)
for i in range(0,l_stud):
    if lista[i] >= 50:
        ile_zdalo += 1

srednia = sum(lista)/len(lista)
print("srednia wynosi: ",srednia)
print("najwyzszy wynik wynosi: ",max(lista))
print("najnizszy wynik wynosi: ",min(lista))
print("Posortowana lista: ",sorted(lista))
print("zdalo ",ile_zdalo," osob/y")