from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import func
from .. import database
from ..services import comision_service
from ..models.vendedor_model import Vendedor, Venta
from ..views.vendedor_schema import CalculadoraRequest, CalculadoraResponse

router = APIRouter(
    prefix="/calculadora",
    tags=["Calculadora de Comisiones"]
)

@router.post("/", response_model=CalculadoraResponse)
def calcular(request: CalculadoraRequest, db: Session = Depends(database.get_db)):
    # 1. Sumar las ventas del vendedor en el rango de fechas
    total_ventas = db.query(func.sum(Venta.monto)).join(Vendedor).filter(
        Vendedor.nombre == request.vendedor_nombre,
        Venta.fecha >= request.fecha_inicio,
        Venta.fecha <= request.fecha_fin
    ).scalar()

    # Si no hay ventas, el total será None. Lo convertimos a 0.
    total_ventas = total_ventas or 0.0

    # 2. Usar el servicio para obtener la comisión
    resultado_comision = comision_service.calcular_comision_por_ventas(total_ventas)

    return CalculadoraResponse(
        total_ventas=round(total_ventas, 2),
        porcentaje_comision=resultado_comision["porcentaje_comision"],
        monto_comision=resultado_comision["monto_comision"]
    )