from fastapi import FastAPI

"""
entrara al contexto de fastapi creadno una variables
"""
app = FastAPI() # esto es el contexto de FastAPI

@app.get("/") #utilizamos el contexto de fastAPPI con este decorador
async def root(): # siempre que utilizamos un servidor debe de ser una operacion asincrona - espera por una respuesta 
    return "hola fastAPI"

@app.get("/url")
async def url():
    return {"msg": "hola mundo desde json del curso"}

@app.post("")#contexto de fastapi para utilizar post (actualizar muchos camps de un usurario o crear uno nuevo)
async def create_user(): #actualizar datos en bloque
    return {"msg": "nuevo"}