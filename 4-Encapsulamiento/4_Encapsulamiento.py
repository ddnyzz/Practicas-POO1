#Ejemplo de encapsulamiento

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre       #público
        self.__edad = edad         #privado
    
    def mostrarEdad(self):
        return self.__edad

#---------------------------------------
persona1 = Persona("Ana", 30)
print(persona1.nombre)
print(persona1.mostrarEdad())
print(persona1.__edad)
