import numpy

lista1 = ["bollito", "galletas", "ojaldre", "pan de muerto", "pan de elote"]
#lista2 = numpy.array([12, 15, 8, 12, 10])

tupla1 = tuple(lista1)
conjunto1 = set(lista1)
diccionario1 = {
    "Nombre": "Panadería Pancito",
    "Productos disponibles": 5,
    "Producto favorito": "bollito",
    "Abierto": True,
    "Años en funcionamiento": 10,
}

print(lista1)
print(tupla1)
print(conjunto1)
print(diccionario1)

#añadir elementos *lista.append(elemento)
#insertar un elemento en una posición *lista.insert(posición, elemento)
#eliminar un elemento *lista.remove(elemento)
#contar los valores *lista.count()
# #contar valores específicos *lista.count(elemento)
