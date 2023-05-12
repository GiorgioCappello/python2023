# 1.Scrivi un programma che richieda all'utente di inserire una stringa e che conti quante volte ogni lettera appare nella stringa. 

dizionario = {}                                 
stringa = input("Inserisci una stringa: ") 
for lettera in stringa:                         # scorro le lettere della sringa
    if lettera in dizionario:                   
        dizionario[lettera] += 1                # se la lettera è presente nel dizionario aumento il conto
    else:                                       
        dizionario[lettera] = 1                 # altrimenti la inserisco

print("Risultato:", dizionario)

# 2.Creare un dizionario che conta le parole in una frase

diz = {}
frase = input("Inserire frase: ")
par = frase.split()                     # divido la frase nelle sue parole (senza trattare la punteggiatura)

for parola in par:                      # controllo le parole
    if parola in diz:                   
        diz[parola] += 1                # se la parola è presente nel dizionario aumento il conto
    else:                                       
        diz[parola] = 1                 # altrimenti la inserisco
print(diz)