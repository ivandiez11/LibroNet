from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/ping")
def ping():
    return {"message": "pong"}

@app.get("/")
def hola():
    return {"message": "Hola"}