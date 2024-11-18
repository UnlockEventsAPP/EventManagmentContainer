from pydantic import BaseModel
from datetime import datetime

# Esquemas para Evento
class EventoBase(BaseModel):
    nombre: str
    aforo_evento: int
    estado: str
    ciudad: str
    fecha_hora: datetime
    precio: float
    status: str
    imagen_url: str

class EventoCreate(EventoBase):
    pass

class Evento(EventoBase):
    id: int

    class Config:
        from_attributes = True

# Esquemas para Registro
class RegistroBase(BaseModel):
    id_evento: int
    fecha_registro: datetime
    estado_pago: str
    cantidad_personas: int

class RegistroCreate(RegistroBase):
    pass

class Registro(RegistroBase):
    id: int

    class Config:
        from_attributes = True

