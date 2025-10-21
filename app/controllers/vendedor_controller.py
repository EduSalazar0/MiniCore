# app/controllers/vendedor_controller.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from .. import database
from ..services import comision_service
from ..models import vendedor_model
from ..views import vendedor_schema

router = APIRouter(
    prefix="/vendedores",
    tags=["Vendedores"]
)

@router.post("/", response_model=vendedor_schema.Vendedor)
def crear_vendedor(vendedor: vendedor_schema.VendedorCreate, db: Session = Depends(database.get_db)):
    # 1. Usamos el servicio para obtener la lógica de negocio
    resultado_comision = comision_service.calcular_comision(
        total_facturado=vendedor.total_facturado,
        total_cobrado=vendedor.total_cobrado,
        porcentaje_comision=vendedor.porcentaje_comision
    )

    # 2. Creamos el objeto del modelo con todos los datos
    db_vendedor = vendedor_model.Vendedor(
        nombre=vendedor.nombre,
        total_facturado=vendedor.total_facturado,
        total_cobrado=vendedor.total_cobrado,
        porcentaje_comision=vendedor.porcentaje_comision,
        pago_realizado=resultado_comision["pago_realizado"],
        comision_calculada=resultado_comision["comision_calculada"]
    )

    # 3. Guardamos en la base de datos
    db.add(db_vendedor)
    db.commit()
    db.refresh(db_vendedor)
    return db_vendedor

@router.get("/", response_model=List[vendedor_schema.Vendedor])
def obtener_vendedores(skip: int = 0, limit: int = 100, db: Session = Depends(database.get_db)):
    vendedores = db.query(vendedor_model.Vendedor).offset(skip).limit(limit).all()
    return vendedores