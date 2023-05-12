#Scrivere un programma python per la gestione di un registro vendite. Il programma deve permettere di aggiungere le vendite di diversi prodotti e calcolare il totale delle vendite (per ogni prodotto)
flag = True
diz = {}
while flag:
    a = input("Premere 1 per aggiungere una vendita\nPremere 2 per visualizzare le vendite\nScrivere exit per uscire\nInserire opzione: ")

    if a == 'exit':
        flag = False
        print("Arrivederci")
    elif a == '1':
        nome = input("Inserire nome: ")
        quant = int(input("Inserire quantita vendute: "))
        prezzo = float(input("Inserire prezzo di vendita: "))
        diz[nome]= [quant,prezzo]
        print(diz)
    elif a == '2':
        for nome in diz.keys():
            print("Il fatturato di",nome,"risulta", diz[nome][0]*diz[nome][1])
    else:
        print("Scelta non disponibile")