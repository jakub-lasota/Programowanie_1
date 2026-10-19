temperatury = []
print("podaj temperatury ")
for i in range(1,8):
   el = int(input("Dzien "+str(i)+": "))
   temperatury.append(el)

avg_t = sum(temperatury)/len(temperatury)
powyzej_sredniej = []
for ele in temperatury:
   if ele > avg_t:
      powyzej_sredniej.append(ele)
print("Najnizsza temperatura: ",min(temperatury)," C")
print("Najwyzsza temperatura: ",max(temperatury)," C")
print("srednia temperatura: ",avg_t," C")
print("Powyzej sredniej: ",powyzej_sredniej)
print("liczba dni: ",len(powyzej_sredniej))

