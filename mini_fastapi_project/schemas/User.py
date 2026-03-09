from pydantic import BaseModel


class UserPydantic(BaseModel):
    id: int
    name: str
    surname: str
    url: str
    age: int

class User():
    def __init__(self, name: str, surname: str, url: str, age: int, id: int):
        self.name = name
        self.surname = surname
        self.url = url
        try:
            self.age = int(age) #casting str -> number
            self.id = int(id)
        except (TypeError, ValueError) as e: 
            self.age = 0
            raise ValueError("Value age must be an Integer number") from e

    def return_obj(self):
        return {
                "name": self.name,
                "surname": self.surname,
                "url": self.url,
                "age": self.age,
                "id": self.id,
            }
        
        