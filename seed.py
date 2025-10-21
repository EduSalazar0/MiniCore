from app.database import SessionLocal, engine
from app.models.vendedor_model import Vendedor, Venta, Base
from datetime import date, timedelta
import random

# Crea las tablas si no existen
Base.metadata.create_all(bind=engine)

# Obtiene una sesión de la base de datos
db = SessionLocal()

def seed_data():
    print("Limpiando datos antiguos...")
    db.query(Venta).delete()
    db.query(Vendedor).delete()
    db.commit()

    print("Creando vendedores...")
    vendedores_nombres = ["Ana", "Juan", "Maria", "Pedro"]
    vendedores = []
    for nombre in vendedores_nombres:
        vendedor = Vendedor(nombre=nombre)
        vendedores.append(vendedor)
        db.add(vendedor)

    db.commit()
    for v in vendedores:
        db.refresh(v) # Refresca para obtener el ID asignado

    print("Generando ventas de ejemplo...")
    hoy = date.today()
    for _ in range(200): # Crear 200 ventas aleatorias
        vendedor_aleatorio = random.choice(vendedores)
        fecha_aleatoria = hoy - timedelta(days=random.randint(0, 90)) # Ventas en los últimos 3 meses
        monto_aleatorio = round(random.uniform(50.0, 300.0), 2)

        nueva_venta = Venta(
            monto=monto_aleatorio,
            fecha=fecha_aleatoria,
            vendedor_id=vendedor_aleatorio.id
        )
        db.add(nueva_venta)

    db.commit()
    print("¡Datos de ejemplo creados exitosamente!")

if __name__ == "__main__":
    seed_data()
    db.close()