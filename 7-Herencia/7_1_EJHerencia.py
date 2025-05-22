# Clase base
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hacer_sonido(self):
        raise NotImplementedError("Este método debe ser implementado por las subclases")

# Clase derivada
class Perro(Animal):
    def hacer_sonido(self):
        return "Guau"

# Clase derivada
class Gato(Animal):
    def hacer_sonido(self):
        return "Miau"

# Crear instancias de las clases derivadas
mi_perro = Perro("Rex")
mi_gato = Gato("Luna")

# Llamar a los métodos 
print(f"{mi_perro.nombre} dice {mi_perro.hacer_sonido()}")
print(f"{mi_gato.nombre} dice {mi_gato.hacer_sonido()}")  