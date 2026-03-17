import requests

API_URL = "https://api.github.com/search/repositories"
params = {}
gh_headers = {
    "Accept": "application/vnd.github+json",
    "X-GitHub-Api-Version": "2026-03-10"
}

url_params = {
    "q": "stars",
    "type": "Repositories"
}
def repos_with_most_stars():
    print("iniciando programa ...")
    gh_api_url = API_URL
    try:
        def peticion_gh():
            print("Making request ...")
            return requests.get(gh_api_url, headers=gh_headers, params=url_params)
        # with open("gh_response.json", "w") as gh_response:
        #    print("Writting response on new file ...")
        #    gh_response.write(peticion_gh())
        peticion_gh()
    except Exception as e:
        print(e)

if __name__ == "__main__":
    #   1)  "Realizar request a GitHub para obtener los top repos"
    #podemos pasar 'params' opcionales como segundo parametro del metodo .get()
    print("Iniciando ejecucion de funcion principal...")
    repos_with_most_stars()
    pass
    




#   2)  "Ordernarlos por numero de estrallas de mayor a menor"

#   3)  "Imprimir los resultados en la terminal"