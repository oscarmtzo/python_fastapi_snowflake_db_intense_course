import requests
import json
from app_solution_1 import API_URL
API_URL = API_URL

def top_repos(languages="", sort="stars", order="desc"):
    query_params = {
        "q": "Q" + query_params_formatter(languages),
        "per_page": 8,
        "sort": sort,
        "order": order
    }
    
    api_headers = {
        "Accept": "application/vnd.github+json", 
        "X-GitHub-Api-Version": "2026-03-10" 
    }
    response_status_code = ""
    try:
        response = requests.get(API_URL, params=query_params, headers=api_headers)
        response_status_code = response.status_code
        repo_names = dict()
        if response.status_code == 200:
            dict_response_json = response.json()
            #print(dict_response_json.keys()) #dict_keys(['total_count', 'incomplete_results', 'items'])
            #print(dict_response_json['items'])
            for repo in dict_response_json['items']:
                aux_dict = {
                    f"{repo["name"]}": f"{
                        {
                            "stars": repo["stargazers_count"],
                            "language": repo["language"]
                        }
                    }"
                }
                #print(repo_names)
                repo_names.update(aux_dict)
            #format_to_json = json.dump(repo_names)
            #deformat_to_str = json.load(format_to_json)
            #print(format_to_json)
            
            
            print(json.dumps(repo_names))
            
        else: 
            raise RuntimeError("Un error ocurrio")
            
    except:
        print(f"Algo salio mal {response_status_code}")

def query_params_formatter(input_languages="") -> dict:
    query_str = ""
    try:
        query_str = " "
        for language in input_languages:
            query_str = query_str + f"language: {language} "
        return query_str
    except NameError as e:
        print(e)
    finally:
        return query_str
    


if __name__ == "__main__":
    language_list = ["Javascript", "Ruby"]
    
    top_repos()