#ejemplo de encapsulamiento 12/02/2025



class Pisto:
    def __init__(self, hielera, hielera2):
        self.__hielera = hielera
        self.hielera2 = hielera2
        
    def pistear(self):
        self.__hielera = "vaciar"
        return self.__hielera
    
    def pistear2(self):
        self.hielera2 = "vacia"
        return self.hielera2
    
    
fiesta = Pisto("Cartón en hielera", "Unas frías")
print(fiesta.pistear())
print(fiesta.pistear2())