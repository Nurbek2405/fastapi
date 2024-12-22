# - endpoints
'''def hell():
    pass'''

# path указываем на стороне фронта путь, для какой то функции

# parametrs какие данные вы отправляете со стороны фронта к бэку

# schemas - validation схемы нужны для валидировать и прааметры которые уходят, проверить

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class DataInput(BaseModel):
    name: str
    age: int

class DataOutput(BaseModel):
    name: str

@app.get("/hello")  # API  # принимает только гет запрос
def hello():
    return {
        "hello": "Hello World!",
    }

@app.get("/hello1")  # API  # принимает только гет запрос
def hello():пше
    return {
        "hello": "Hello World1!",
    }

@app.get("/hello2")  # API  # принимает только гет запрос
def hello():
    return {
        "hello": "Hello World2!",
    }

@app.get("/hello4")  # API  # принимает только гет запрос
def hello():
    return {
        "hello": "Hello World4!",
    }


@app.post("/hello-post", response_model=DataOutput)
def hello_post(data: DataInput): # был тут dict[str,str]

    return {
        "name": data.name, # ['name'] был
        "age": data.age,
    }