
from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey
from sqlalchemy.orm import relationship
from ..database import Base

class Vendedor(Base):
    __tablename__ = "vendedores"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, unique=True, index=True)

    # Relación: Un vendedor puede tener muchas ventas
    ventas = relationship("Venta", back_populates="vendedor")

class Venta(Base):
    __tablename__ = "ventas"
    id = Column(Integer, primary_key=True, index=True)
    monto = Column(Float, nullable=False)
    fecha = Column(Date, nullable=False)

    # Clave foránea para conectar con el vendedor
    vendedor_id = Column(Integer, ForeignKey("vendedores.id"))

    # Relación inversa
    vendedor = relationship("Vendedor", back_populates="ventas")