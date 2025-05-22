##Ejemplo de uso de JSON en Python
# ##27/03/25

import json
import requests

class GestorJson:
    def __init__(self, arch):
        self.arch = arch
        
    def leerjson(self):
        try:
            with open(self.arch, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            print(f"Error: El archivo no existe.")
            return {}
        except json.JSONDecodeError:
            print("Error: El archivo no es un JSON válido.")
            return {}
        
    def escribir(self, datos):
        with open(self.arch, 'w') as f:
            json.dump(datos, f, indent=4)
        
    def modificarJson(self, llave, valor):
        datos = self.leer_json()
        datos[llave] = valor
        self.escribir(datos)
        
    def obtenerPokemon(self, pokemon):
        try:
            url= f"https://pokeapi.co/api/v2/pokemon/{pokemon}"
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            self.escribir(data)
        except requests.exceptions.HTTPError:
            print("El enlace no existe")
        except requests.exceptions.RequestException:
            print("No se pudo realizar la solicitud")
        

            
#############################

gJason = GestorJson("pokemon.json")
gJason.obtenerPokemon("charizard")
pokemonInfo = gJason.leerjson()
print(pokemonInfo)