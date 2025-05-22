#30/01/2025
#class/def
#Mostrar el area y perimetro de una figura 
# identificandola por sus lados(cuadrado, triangulo y penatagono) usando el numero de lados y su medida (todos equilateros)

import math
class Figura:
    def area(nLados, vLado):
        #Triangulo
        if nLados == 3:
            h = (vLado * math.sqrt(3)) / 2
            b = vLado
            areaFigura = (b * h) / 2
            print("El area del triangulo es: ", areaFigura)

        #cuadrado
        if nLados == 4:
            b = vLado
            h = vLado
            areaFigura = b * h
            print("El area del cuadrado es: ", areaFigura)
        
        #pentagono
        if nLados == 5:
            angulo = math.pi / nLados
            apotema = vLado / (2 * math.tan(angulo))
            p = vLado * nLados
            areaFigura = (p * apotema) / 2
            print("El area del pentagono es: ", areaFigura)

#--------------------------------------------------------
unaFigura = Figura
nLados = float(input("Dime el numero de lados "))
vLado = float(input("Dime el valor de un lado "))
Figura.area(nLados, vLado)
