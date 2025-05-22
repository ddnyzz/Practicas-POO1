##27/03/25
##Colecciones/listas/tuplas/conjuntos/diccionarios/numpy array
'''
-Crear una lista de 5 valores mixtos
-Crear una lista de 5 valores del mismo tipo
-Las listas anteriores convertirlas a tablas y conj
-Crear un diccionario de 5 elementos con valores de distinto tipo
'''
########################################################################
import numpy as np

lista1 = [1, "hola", 3.5, True, 5]
lista2 = np.array([1,2,3,4,5])
tabla= tuple(lista1)
tabla2= tuple(lista2)
conj = set(lista1)
diccionario = {"uno":1, "dos":2, "tres":3, "cuatro":4, "cinco":5}
print(tabla2)