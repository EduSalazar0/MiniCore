# app/services/comision_service.py
from typing import Dict, Any

def calcular_comision(total_facturado: float, total_cobrado: float, porcentaje_comision: float) -> Dict[str, Any]:
    """
    Calcula la comisión y determina si se debe pagar.
    Regla de negocio: La comisión se paga solo si el total cobrado
    es igual o mayor al total facturado.
    """
    pago_realizado = False
    comision_calculada = 0.0

    if total_cobrado >= total_facturado:
        pago_realizado = True
        # La comisión se calcula sobre el monto cobrado
        comision_calculada = total_cobrado * (porcentaje_comision / 100)
    
    return {
        "pago_realizado": pago_realizado,
        "comision_calculada": round(comision_calculada, 2) # Redondeamos a 2 decimales
    }