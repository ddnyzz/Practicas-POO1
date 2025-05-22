#Herencia

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def comer(self):
        print("Estoy comiendo")

    def presentarse(self):
        print("Soy", self.nombre, "y tengo", self.edad, "años")

class Panadero(Persona):
    def __init__(self, nombre, edad, especialidad):
        super().__init__(nombre, edad)
        self.especialidad = especialidad
    
    def trabajar(self):
        print("Estoy trabajando como panaderilla especializada en", self.especialidad)

#------------------------------------------------------
empleado = Panadero("Dni", 73, "pan artesanal")
empleado.comer()
empleado.presentarse()
empleado.trabajar()
