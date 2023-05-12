flag = True

while flag:
    a = input("Premere 0 se si vuole accedere\nPremere 1 se si vuole uscire\n")
    if a == '0':
        pippo = True
        while pippo:
            b = input("Scegliere il tipo di operazione:\n1 per addizione\n2 per sottrazione\n3 per moltiplicazione\n4 per divisione\n5 per tornare indietro\n")
            if b=='5':
                pippo = False
            elif b not in '1234':
                print('Riprovare')
            else:
                x = float(input("Scegliere primo numero: "))
                y = float(input("Scegliere secondo numero: "))

                if b=='1':
                    print("Il risultato dell'addizione tra",x,"e",y,"viene:",x+y)
                elif b=='2':
                    print("Il risultato della sottrazione tra",x,"e",y,"viene:",x-y)
                elif b=='3':
                    print("Il risultato della moltiplicazione tra",x,"e",y,"viene:",x*y)
                elif b=='4':
                    if y==0:   
                        print("Non puoi dividere per zero!")
                    else:
                        print("Il risultato della sottrazione tra",x,"e",y,"viene:",x/y)
                pippo = False
    if a == '1':
        print("Arrivederci\n")
        flag = False
    else:
        print("Riprovare\n")