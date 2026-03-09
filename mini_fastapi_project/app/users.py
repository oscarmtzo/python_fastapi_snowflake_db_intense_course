import json
from fastapi import FastAPI
from pydantic import BaseModel
from schemas.User import UserPydantic, User

app = FastAPI()

# Definir Entidad User
# BaseModel - da la capacidad de crear una entidad
"""
class UserPydantic(BaseModel):
    name: str
    surname: str
    url: str
    age: int
"""
"""
class User():
    def __init__(self, name: str, surname: str, url: str, age:int): #esta clase no tiene handler de casting de data types 
        self.name = name
        self.surname = surname
        self.url = url
        self.age = age
    def returnObj(self):
        return {
            "name": self.name,
            "surname" : self.surname,
            "url" : self.url,
            "age": self.age
        }
"""
#Definir una lista con diferentes usuarios
user_list = [
    #User("moore", "dev", "http://url.com", 24, 789).return_obj()

]
usersPydantic = [   
    UserPydantic( id = 1, name = "Moore", surname="dev", age=25, url="http://url.com"),
    UserPydantic( id = 2, name = "Moore", surname="dev", age=25, url="http://url.com"),
    UserPydantic( id = 3, name = "Moore", surname="dev", age=25, url="http://url.com")
]

user_list = [
    user
    for user
    in usersPydantic
]

@app.get("/users")
async def users():
    print(user_list)
    return user_list

#Obtener valor por Path /parameter selector / FastAPI ya lo resuelve
@app.get("/users/{id}")
async def user_id(id: int):
    """
    specific_user = [
        user 
        for user 
        in user_list 
        if(id == user.id)
    ][0]
    
    """
    #return specific_user
    users = filter(lambda user: user.id == id, user_list)
    try:
        print(list(users)[0])
        return list(users)[0]
    except:
        print("")
        return ""
    
#Obtener valor por Query selector
@app.get("/userquery")
async def queryuser(id: int): #Resuelve pydantic automaticamnte mediante BaseModel resuelve el query selector
    print(users)
    try:
        specific_user = [
            user
            for user
            in user_list
            if(id == user.id)
        ][0]
        return specific_user
    except:
        return {"error": f"no encontre ese usuario con el id: {id}"}