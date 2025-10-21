from pydantic import BaseModel
from datetime import date

# Schema para la petición que recibiremos del frontend
class CalculadoraRequest(BaseModel):
    vendedor_nombre: str
    fecha_inicio: date
    fecha_fin: date

# Schema para la respuesta que enviaremos al frontend
class CalculadoraResponse(BaseModel):
    total_ventas: float
    porcentaje_comision: float
    monto_comision: float