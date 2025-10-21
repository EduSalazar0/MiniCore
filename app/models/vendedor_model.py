from sqlalchemy import Column, Integer, String, Float, Boolean
from ..database import Base

class Vendedor(Base):
    __tablename__ = "vendedores"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, index=True)
    ventas_totales = Column(Float)
    comision_obtenida = Column(Boolean, default=False)