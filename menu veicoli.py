# Crea un sistema con menu che permetta di scegliere se creare una moto o un auto con due carrateristiche marca e modello,
# e che obligatoriamente usi l'ereditarietà da veicolo ai figli

# classe madre
class Veicolo:
    def __init__(self, marca, modello):
        self.marca = marca
        self.modello = modello

    def visualizza_info(self):
        print("Marca:", self.marca)
        print("Modello:", self.modello)

#classi figlie
class Moto(Veicolo):
    def __init__(self, marca, modello):
        super().__init__(marca, modello)
        self.tipo = "Moto"

    def visualizza_info(self):
        super().visualizza_info()
        print("Tipo:", self.tipo)

class Auto(Veicolo):
    def __init__(self, marca, modello):
        super().__init__(marca, modello)
        self.tipo = "Auto"

    def visualizza_info(self):
        super().visualizza_info()
        print("Tipo:", self.tipo)

# funzioni per creare moto e auto
def crea_moto():
    marca = input("Inserire marca della moto: ")
    modello = input("Inserire modello della moto: ")
    moto = Moto(marca, modello)
    return moto

def crea_auto():
    marca = input("Inserire marca dell'auto': ")
    modello = input("Inserire modello dell'auto': ")
    auto = Auto(marca, modello)
    return auto

# menù
def switch_accesso():
    while True:
        print("Scegliere cosa creare:\n1. Moto\n2. Auto\n0. Esci")
        scelta = input("Inserire la tua scelta: ")
        if scelta == '0':
            print("Arrivederci!")
            break
        elif scelta == '1':
            veicolo = crea_moto()
            veicolo.visualizza_info()
        elif scelta == '2':
            veicolo = crea_auto()
            veicolo.visualizza_info()
        else:
            print("Scelta non valida! Riprova:")


# chiamata al menù
print("Benvenuto!")
switch_accesso()
