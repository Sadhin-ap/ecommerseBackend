from fastapi import FastAPI
from app.database import engine

app = FastAPI(title="E-commerce API")

@app.get("/")
def home():
    return {"message": "E-commerce Backend Running "}
