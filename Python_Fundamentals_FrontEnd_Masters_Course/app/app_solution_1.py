import requests #importar biblioteca requests
import json

API_URL = "https://api.github.com/search/repositories" #definir endpoint
headers = {"Accept": "application/vnd.github+json", "X-GitHub-Api-Version": "2026-03-10"} #definir headers
url_params = {
    "q": "stars:>5000", #buscar repos con extrellas mayores a 5000, parametros especificos para esta API, no son propios de python
    "type": "Repositories", #query param pra obtener innformacion de repos
    "sort": "stars", #filtrar por numeor de stars en el repo
    "order": "desc", #query param - orden descendente
    "per_page": 2#traer dos repos

} # Definir query parameters

def repos_with_most_starts():
    response = requests.get(API_URL, headers= headers, params = url_params )

    print(response.text)
    print(
        
        json.dumps(response.text)# convertir respuesta de texto a json
    )
    try: 
        with open("./app/response.json","w") as text_file: #open(<nombre_archivo.file>,<w>-operacion de escritura)
            text_file.write(response.text)
    except OSError as e:
        print(e)


if __name__ == "__main__": #ejecutar funcion solo si es ejecutado el archivo directamente y no por importacion como biblioteca
    repos_with_most_starts()

    pass #no hacer nada