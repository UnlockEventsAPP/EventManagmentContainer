from fastapi import FastAPI
from routers import events, register  # Importamos los routers de eventos y registros
from database import create_tables

app = FastAPI()

@app.on_event("startup")
def on_startup():
    create_tables()

app.include_router(events.router, prefix="/events", tags=["Events"])
app.include_router(register.router, prefix="/events", tags=["Registers"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the API"}


