#Polimorfismo con panes uwu

class Pan:
    def __init__(self, nombre):
        self.nombre = nombre

    def hacerSonido(self):
        pass

class Bolillo(Pan):
    def hacerSonido(self):
        print("Hola soy", self.nombre, "y hago crunch")

class Concha(Pan):
    def hacerSonido(self):
        print("Hola soy", self.nombre, "y hago ñam ñam suave")

class Cuernito(Pan):
    def hacerSonido(self):
        print("Hola soy", self.nombre, "y hago hojaldre")

#-----------------------------------------------------------
pan1 = Bolillo("Bolillo relleno")
pan2 = Concha("Concha de chocolate")
pan3 = Cuernito("Cuernito de mantequilla")

pan1.hacerSonido()
pan2.hacerSonido()
pan3.hacerSonido()
