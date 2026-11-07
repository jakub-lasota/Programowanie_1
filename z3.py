liczby = [10, 20, 30, 40]
ile = int(input("podaj liczbe pomiarow "))
for i in range(0,ile):
    pomiar = int(input("podaj pomiar "))
    liczby.append(pomiar)
prog = 50
wieksze = [x for x in liczby if x > 50]
double = [x*2 for x in liczby]
print("wieksze od 50 ",wieksze,"podwojone pomiary ",double)
print(any(x>50 for x in liczby))
print(all(x>50 for x in liczby))