import requests
from app_solution_1 import API_URL
from app_solution_1 import headers
from app_solution_1 import url_params

github_api_url = API_URL
headers_github_api = dict()
headers_github_api.update(headers)
#print(headers_github_api.keys())

url_params_github_api = dict()
url_params_github_api.update(url_params)
#print(url_params_github_api)

def update_query_to_specific_language(language_choices , old_params :dict):
    language_query = ""
    try:
        language_query = ""
        for language in language_choices:
            language_query = language_query + f" language:{language} "
        old_params.update(
                {
                    "q": f"{old_params["q"] + " " + language_query}"
                }
            )

    except:
        old_params

def repos_with_most_starts_github_api():
    update_query_to_specific_language(["javascript", "python", "ruby"],url_params_github_api)
    print(f"primeros params: {url_params}")
    print(f"segundos params: {url_params_github_api}")
    response = requests.get(github_api_url, params=url_params_github_api, headers=headers_github_api)
    print(response.url)
    print(response.text)
    dict_response_json = response.json()
    print(dict_response_json.keys()) #dict_keys(['total_count', 'incomplete_results', 'items'])
    print(dict_response_json['items'])
    repo_names = dict()
    for repo in dict_response_json['items']:
        aux_dict = {
            f"{repo["name"]}": f"{
                {
                    "stars": repo["stargazers_count"],
                    "language": repo["language"]
                }
            }"
        }
    
        repo_names.update(aux_dict)

    def name_printer(list_of_items):
        print(f"the repository names are:")
        #for index, item in enumerate(list_of_items):
        #    print(f"{index + 1}: {item}")
        print(list_of_items)

    name_printer(repo_names)





if __name__ == "__main__":
    repos_with_most_starts_github_api()
    pass