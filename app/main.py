# app/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .database import engine, SessionLocal
from .models import vendedor_model
from .controllers import calculadora_controller

# Imports para el script de seeding
from .models.vendedor_model import Vendedor, Venta
from datetime import date, timedelta
import random

app = FastAPI()

# --- Evento de Arranque para Crear Tablas y Poblar la Base de Datos ---
@app.on_event("startup")
def on_startup():
    # 1. Mueve la creación de tablas aquí dentro
    vendedor_model.Base.metadata.create_all(bind=engine)

    db = SessionLocal()
    # 2. Revisa si la tabla de Vendedores ya tiene datos
    vendedor_existente = db.query(Vendedor).first()
    if not vendedor_existente:
        print("Base de datos vacía. Poblando con datos de ejemplo...")

        # Crear Vendedores
        vendedores_nombres = ["Ana", "Juan", "Maria", "Pedro"]
        vendedores = []
        for nombre in vendedores_nombres:
            vendedor = Vendedor(nombre=nombre)
            vendedores.append(vendedor)
            db.add(vendedor)

        db.commit()
        for v in vendedores:
            db.refresh(v)

        # Crear Ventas de Ejemplo
        hoy = date.today()
        for _ in range(200):
            vendedor_aleatorio = random.choice(vendedores)
            fecha_aleatoria = hoy - timedelta(days=random.randint(0, 90))
            monto_aleatorio = round(random.uniform(50.0, 300.0), 2)
            nueva_venta = Venta(
                monto=monto_aleatorio,
                fecha=fecha_aleatoria,
                vendedor_id=vendedor_aleatorio.id
            )
            db.add(nueva_venta)

        db.commit()
        print("¡Datos de ejemplo creados exitosamente!")
    else:
        print("La base de datos ya contiene datos. Omitiendo el poblado.")

    db.close()
# --------------------------------------------------------------------

origins = [
   "https://minicore-api-xgnc.onrender.com",
    "https://minicore-h30e.onrender.com",
    "http://localhost:3000"
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(calculadora_controller.router)

@app.get("/")
def read_root():
    return {"Hello": "World"}