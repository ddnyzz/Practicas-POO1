#06/02/2025
#realizar un arreglo usando insertar, eliminar y modificar //array //np.array


class arreglos:
    def __init__(self):
        self.lista= []
        
    def insertar(self):
        if op==1:
            dato= input(int("Valor: "))
            self.arreglo.append(dato)
        
    def eliminar(self):
        if op==2:
            eliminar= input(int("Posición a eliminar: "))
            self.arreglo.pop(eliminar)
            
    def modificar(self):
        if op==3:
            mod= input()      
        
        
l = arreglos()
op = input("Opción: 1-Insertar 2-Eliminar 3-Modificar")
l.insertar(op)
l.eliminar(op)
l.modificar(op)