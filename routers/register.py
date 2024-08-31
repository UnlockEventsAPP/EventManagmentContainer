from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from crud import create_register, get_register, update_register, delete_register, get_all_registers
from schemas import RegistroCreate, Registro as RegistroSchema
from database import get_db

router = APIRouter()

@router.post("/registros/", response_model=RegistroSchema)
def create_register_endpoint(registro: RegistroCreate, db: Session = Depends(get_db)):
    db_registro = create_register(db, registro)
    return db_registro

@router.get("/registros/{registro_id}", response_model=RegistroSchema)
def read_register_endpoint(registro_id: int, db: Session = Depends(get_db)):
    db_registro = get_register(db, registro_id)
    if not db_registro:
        raise HTTPException(status_code=404, detail="Registro not found")
    return db_registro

@router.get("/registros/", response_model=list[RegistroSchema])
def read_all_events(db: Session = Depends(get_db)):
    registros = get_all_registers(db)
    return registros


@router.put("/registros/{registro_id}", response_model=RegistroSchema)
def update_register_endpoint(registro_id: int, registro: RegistroCreate, db: Session = Depends(get_db)):
    db_registro = update_register(db, registro_id, registro)
    if not db_registro:
        raise HTTPException(status_code=404, detail="Registro not found")
    return db_registro

@router.delete("/registros/{registro_id}", response_model=RegistroSchema)
def delete_register_endpoint(registro_id: int, db: Session = Depends(get_db)):
    db_registro = delete_register(db, registro_id)
    if not db_registro:
        raise HTTPException(status_code=404, detail="Registro not found")
    return db_registro
