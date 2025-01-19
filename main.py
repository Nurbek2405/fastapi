from fastapi import FastAPI

app = FastAPI()

@app.get("/Users")
def home() -> dict[str,str]:
    return {"data": "message"}

@app.get("/contacts")
def contacts() -> int:
    return 34