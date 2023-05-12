menu = {}
ordine = {}

pippo = True #flag

while pippo:
    print("\nSelezionare\n1 Aggiungi un piatto al menù\n2 Visualizza il menù\n3 Cancella un piatto dal menù\n4 Ordina un piatto\n5 Richiedi il conto\n0 Esci\n")
    scelta = input("Inserisci la tua scelta: ")

    if scelta == '0': 
        #esco         
        print("Arrivederci!")
        pippo = False

    elif scelta == '1':
        # Aggiungi un piatto al menù
        nome_piatto = input("Inserisci il nome del piatto da inserire: ")
        prezzo = float(input("Inserisci il prezzo del piatto da inserire: € "))
        
        if prezzo < 0:
            print("\nIl prezzo non può essere negativo.")
        else:
            menu[nome_piatto] = prezzo
            print("Piatto registrato correttamente")
    
    elif scelta == '2':
        print(menu)

    elif scelta == '3':
        nome_piatto = input("Inserisci il nome del piatto da cancellare: ")
        if nome_piatto in menu.keys():
            menu.pop(nome_piatto)
            print("Piatto rimosso correttamente")
        else:
            print("Errore, il piatto da te inserito è non presente nel menù")

    elif scelta == '4':
        nome_piatto = input("Inserisci il nome del piatto da ordinare: ")
        quantita = int(input("Inserisci la quantità da ordinare: "))

        if nome_piatto not in menu.keys():
            print("Errore, il piatto da te inserito non è presente nel menù")
        else:
            if nome_piatto in ordine.keys():
                ordine[nome_piatto] += quantita
            else:
                ordine[nome_piatto] = quantita

    elif scelta == '5':
        # Richiedi il conto
        totale = 0.0
        for nome, quantita in ordine.items():
            totale += (menu[nome] * quantita)
        print("Totale: €", totale)
        ordine = {} #azzero l'ordine

    else:
        print("Errore, l'opzione da te selezionata non esiste")