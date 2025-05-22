#Figureas y el calculo de un poligono regular


from math import radians, tan

class Figura:
    def area(nLados, vLado):
        if nLados > 0:
            angulo = radians(360 / (nLados * 2))
            apotema = vLado / (2 * tan(angulo))
            p = vLado * nLados
            areaFigura = (p * apotema) / 2
            print("El area de la figura es:", areaFigura)

    def perimetro(nLados, vLado):
        perimetroFigura = vLado * nLados
        print("El perimetro de la figura es:", perimetroFigura)

#--------------------------------------------------------
unaFigura = Figura
nLados = float(input("Dime el numero de lados "))
vLado = float(input("Dime el valor de un lado "))
Figura.area(nLados, vLado)
Figura.perimetro(nLados, vLado)
