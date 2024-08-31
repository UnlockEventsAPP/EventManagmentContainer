from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from crud import create_event, get_event, update_event, delete_event, get_all_events
from schemas import EventoCreate, Evento as EventoSchema
from database import get_db

router = APIRouter()

@router.post("/eventos/", response_model=EventoSchema)
def create_event_endpoint(evento: EventoCreate, db: Session = Depends(get_db)):
    db_evento = create_event(db, evento)
    return db_evento

@router.get("/eventos/{evento_id}", response_model=EventoSchema)
def read_event_endpoint(evento_id: int, db: Session = Depends(get_db)):
    db_evento = get_event(db, evento_id)
    if not db_evento:
        raise HTTPException(status_code=404, detail="Evento not found")
    return db_evento

@router.get("/eventos/", response_model=list[EventoSchema])
def read_all_events(db: Session = Depends(get_db)):
    eventos = get_all_events(db)
    return eventos

@router.put("/eventos/{evento_id}", response_model=EventoSchema)
def update_event_endpoint(evento_id: int, evento: EventoCreate, db: Session = Depends(get_db)):
    db_evento = update_event(db, evento_id, evento)
    if not db_evento:
        raise HTTPException(status_code=404, detail="Evento not found")
    return db_evento

@router.delete("/eventos/{evento_id}", response_model=EventoSchema)
def delete_event_endpoint(evento_id: int, db: Session = Depends(get_db)):
    db_evento = delete_event(db, evento_id)
    if not db_evento:
        raise HTTPException(status_code=404, detail="Evento not found")
    return db_evento
