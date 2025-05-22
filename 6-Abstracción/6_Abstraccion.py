#Ejemplo de abstracción

class Empleado:
    def __init__(self, nombre, rol):
        self.nombre = nombre
        self.rol = rol
    
    def decirDialogo(self):
        pass

class Panadero(Empleado):
    def decirDialogo(self):
        print("Hola, soy", self.nombre, "y soy la", self.rol, "de la panadería.")

class Cajero(Empleado):
    def decirDialogo(self):
        print("Hola, soy", self.nombre, "y soy el", self.rol, "de la panadería.")


#-----------------------------------------------------------
empleado1 = Panadero("Dani", "panadera principal")
empleado2 = Cajero("Beto", "cajero")

empleado1.decirDialogo()
empleado2.decirDialogo()
