liczba = int(input("podaj liczbe pomiarow"))
pomiar = []
for i in range(0,liczba):
    ob = int(input("Podaj pomiar"))
    pomiar.append(ob)
print("pierwszy pomiar: ",pomiar[0])
print("ostatni pomiar: ",pomiar[len(pomiar)-1])
print("trzy pierwsze: ",pomiar[:3])
print("trzy ostatnie: ",pomiar[-3:])
print("co drugi pomiar",pomiar[::2])
print("odwrocona", pomiar[::-1])
kopia_pomiar = pomiar.copy()
kopia_pomiar[0] = 0
print("oryginal: ",pomiar)
print("kopiad: ",kopia_pomiar)

