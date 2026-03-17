#import env 

#1) importar biblioteca de requests para hacer requests como cliente
import requests

#2) definir la vairable de la URL del endpoint a consultar
API_URL = "https://pokeapi.co/api/v2/pokemon/ditto"

# 3) utilizar el metodo .get() de la Biblioteca requests
get_response = requests.get(API_URL) # ya estamos recibiendo aqui el objeto JSON

#   4) recuperar el HTTP status code en una variable
get_status_code_from_response = get_response.status_code
# nos aseguramos de que provenga del response que recibimos

print(f"codigo de estado HTTP de la peticion: ${get_status_code_from_response}")


# 5) podemos convertir el payload / body de la respuesta utilizando su metodo .json() para retornar un dict, list o cualquiera que sea el tipo de dato de la respuesta y sus estructura
#print(f"payload de respuesta:\n{get_response.json()}")
get_response_json = get_response.json() # respuesta convertida a JSON
print(get_response_json['abilities'][0]["ability"])
