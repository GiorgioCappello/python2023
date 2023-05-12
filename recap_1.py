#Scrivi un programma che richieda all'utente di inserire una stringa e che conti quante volte ogni lettera appare nella stringa. 

dizionario = {}                                 
stringa = input("Inserisci una stringa: ")      
for lettera in stringa:                         #scorro le lettere della sringa
    if lettera in dizionario:                   
        dizionario[lettera] += 1                #se la lettera è presente nel dizionario aumento il conto
    else:                                       
        dizionario[lettera] = 1                 #altrimenti la inserisco

print("Risultato:", dizionario)
