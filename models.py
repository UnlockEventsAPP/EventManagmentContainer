from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Registro(Base):
    __tablename__ = "registros"

    id = Column(Integer, primary_key=True, index=True)
    id_evento = Column(Integer, ForeignKey("eventos.id"), nullable=False)
    fecha_registro = Column(DateTime, nullable=False)
    estado_pago = Column(String(50), nullable=False)

    evento = relationship("Evento", back_populates="registros")


class Evento(Base):
    __tablename__ = "eventos"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), index=True)
    aforo_evento = Column(Integer)  # Cambiar de aforo_evento a aforo
    estado = Column(String(50))
    ciudad = Column(String(50))
    fecha_hora = Column(DateTime)

    registros = relationship("Registro", back_populates="evento")
