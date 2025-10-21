from fastapi import FastAPI
from .database import engine
from .models import vendedor_model
from .controllers import vendedor_controller # Importa el controlador

# Crea las tablas en la base de datos
vendedor_model.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Incluye las rutas del controlador
app.include_router(vendedor_controller.router)

@app.get("/")
def read_root():
    return {"Hello": "World"}