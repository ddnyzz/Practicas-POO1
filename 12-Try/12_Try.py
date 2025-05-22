#ejemplo de manejo de excepciones

try:
    cantidad = int(input("¿Cuántos panes quieres comprar? "))
    precio = 5  
    total = cantidad * precio
    print("El total a pagar es:", total, "pesos")
except ValueError:
    print("Por favor, ingresa un número válido.")
    

