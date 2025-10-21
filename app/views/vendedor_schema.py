from pydantic import BaseModel

class VendedorBase(BaseModel):
    nombre: str
    total_facturado: float
    total_cobrado: float
    porcentaje_comision: float

class VendedorCreate(VendedorBase):
    pass

class Vendedor(VendedorBase):
    id: int
    comision_calculada: float
    pago_realizado: bool

    class Config:
        from_attributes = True