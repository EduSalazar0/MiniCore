from fastapi import FastAPI
from .database import engine
from .models import vendedor_model # Mantenemos esto para que cree las tablas
from .controllers import calculadora_controller # <--- CAMBIO
from fastapi.middleware.cors import CORSMiddleware

# Crea las tablas Vendedor y Venta
vendedor_model.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = ["https://minicore-api-xgnc.onrender.com",
           "https://minicore-h30e.onrender.com",
           "http://localhost:3000"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Incluye las nuevas rutas de la calculadora
app.include_router(calculadora_controller.router) # <--- CAMBIO

@app.get("/")
def read_root():
    return {"Hello": "World"}