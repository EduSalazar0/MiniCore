from fastapi import FastAPI
from .database import engine
from .models import vendedor_model

# Crea las tablas en la base de datos
vendedor_model.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}