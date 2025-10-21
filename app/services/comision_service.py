from typing import Dict

def calcular_comision_por_ventas(total_ventas: float) -> Dict[str, float]:
    """
    Calcula el porcentaje y el monto de la comisión basado en un total de ventas.
    """
    porcentaje = 0.0

    if total_ventas >= 1000:
        porcentaje = 1.15
    elif total_ventas >= 800:
        porcentaje = 0.10
    elif total_ventas >= 600:
        porcentaje = 0.08
    elif total_ventas >= 400:
        porcentaje = 0.06

    monto_comision = total_ventas * (porcentaje / 100)

    return {
        "porcentaje_comision": porcentaje,
        "monto_comision": round(monto_comision, 2)
    }