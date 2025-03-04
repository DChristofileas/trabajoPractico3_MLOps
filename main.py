from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message":"¡Hola! Esta es mi API con FastAPI y Docker"}
@app.get("/ping")
def ping():
    return {"message": "pong"}
