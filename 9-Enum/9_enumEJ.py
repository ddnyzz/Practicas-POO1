'''
4.1 - enum
4.2 - typing
4.3 - exceptions
'''

from enum import Enum
class consecutiva(Enum):
    lunes = 1
    martes = 2
    miercoles = 3
    jueves = 4
    viernes = 5
    sabado = 6
    domingo = 7
    
print(consecutiva.lunes)
print(consecutiva.lunes.value)
print(type(consecutiva.lunes))
print(type(consecutiva.lunes.value))