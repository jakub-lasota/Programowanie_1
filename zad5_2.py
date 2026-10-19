haslo = "Python123"
proby = 3
cnt = 1
while True:

    log = str(input("Podaj haslo: "))
    if log == haslo:
        print("Logowanie udane ")
        break
    else: 
        print("Niepoprawne haslo, pozostale proby: ",proby-cnt)
        cnt += 1
        if cnt > 3:
            print("Konto zablokowane ")
            break

        