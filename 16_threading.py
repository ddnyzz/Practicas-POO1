## 06/05/2025
# Threading in Python
# Threading is a way to run multiple threads (smaller units of a process) at the same time.

import threading
import time 

class Hilo(threading.Thread):
    def __init__(self, nombre, intervalo):
        super().__init__()
        self.nombre = nombre
        self.intervalo = intervalo

    def run(self):
        print("El hilo {self.nombre} ha comenzado.")
        for i in range(5):
            print(f"El hilo {self.nombre} está en la iteración {i}.")
            time.sleep(self.intervalo)
        print(f"El hilo {self.nombre} ha terminado.")
        
#crear hilos
hilo1 = Hilo("Hilo 1", 2)   
hilo2 = Hilo("Hilo 2", 4)
hilo1.start()
hilo2.start()
hilo1.join()   
hilo2.join()