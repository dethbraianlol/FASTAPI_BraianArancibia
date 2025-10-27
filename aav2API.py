from fastapi import FastAPI

app = FastAPI()
users = ["hola", "roger", "josep oriol roca", "Veronica"]

@app.get("/")
def read_root():
    return {"mensaje": "¡FastAPI funcionando correctamente!"}

@app.post("/api/users", response_model=dict, tags=["CRUD sense DB"])
def addNewItem():
    # Afegir nou item a la llista users
    users.append("Ariadna")
    # Transformar list a dict
    users_dict = dict(zip(range(len(users)), users))
    return users_dict

@app.get("/api/users/{id}", response_model=dict, tags=["CRUD sense DB"])
def readOneItem(id: int):
    # Buscar item a la llista users
    item_r = users[id]
    # Retornar un diccionari amb l'item buscat
    return {id: item_r}

@app.get("/api/users", response_model=dict, tags=["CRUD sense DB"])
def readAllItems():
    # Transformar la llista a diccionari
    user_dict = dict(zip(range(len(users)), users))
    return user_dict

@app.put("/api/users/{id}", response_model=dict, tags=["CRUD sense DB"])
def updateItem(id: int):
    # Actualitzar item
    update_Item = "Carla"
    users[id] = update_Item
    user_dict = dict(zip(range(len(users)), users))
    return user_dict

@app.delete("/api/users/{id}", response_model=dict, tags=["CRUD sense DB"])
async def deleteItem(id: int):
    # Eliminar item
    del users[id]
    users_dict = dict(zip(range(len(users)), users))
    return users_dict
