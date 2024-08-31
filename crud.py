from sqlalchemy.orm import Session
from models import Registro, Evento
from schemas import RegistroCreate, EventoCreate

# Operaciones CRUD para Registro

def create_register(db: Session, registro: RegistroCreate):
    db_registro = Registro(**registro.dict())
    db.add(db_registro)
    db.commit()
    db.refresh(db_registro)
    return db_registro

def get_register(db: Session, registro_id: int):
    return db.query(Registro).filter(Registro.id == registro_id).first()

def get_all_registers(db: Session):
    return db.query(Registro).all()

def update_register(db: Session, registro_id: int, registro: RegistroCreate):
    db_registro = get_register(db, registro_id)
    if db_registro:
        for key, value in registro.dict().items():
            setattr(db_registro, key, value)
        db.commit()
        db.refresh(db_registro)
    return db_registro

def delete_register(db: Session, registro_id: int):
    db_registro = get_register(db, registro_id)
    if db_registro:
        db.delete(db_registro)
        db.commit()
    return db_registro

# Operaciones CRUD para Evento (opcional)

def create_event(db: Session, event: EventoCreate):
    db_evento = Evento(**event.dict())
    db.add(db_evento)
    db.commit()
    db.refresh(db_evento)
    return db_evento

def get_event(db: Session, event_id: int):
    return db.query(Evento).filter(Evento.id == event_id).first()

def get_all_events(db: Session):
    return db.query(Evento).all()

def update_event(db: Session, event_id: int, event: EventoCreate):
    db_evento = get_event(db, event_id)
    if db_evento:
        for key, value in event.dict().items():
            setattr(db_evento, key, value)
        db.commit()
        db.refresh(db_evento)
    return db_evento

def delete_event(db: Session, event_id: int):
    db_evento = get_event(db, event_id)
    if db_evento:
        db.delete(db_evento)
        db.commit()
    return db_evento
