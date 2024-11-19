from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware  # Importar CORSMiddleware
from routers import events, register  # Importamos los routers de eventos y registros
from database import create_tables

app = FastAPI()

# Configuración de CORS
origins = [
    "https://front-unlock-patrones.vercel.app",  # Dominio de tu frontend
    "http://localhost:4200",  # Si estás probando en Angular localmente
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Permitir estos orígenes
    allow_credentials=True,
    allow_methods=["*"],  # Permitir todos los métodos HTTP
    allow_headers=["*"],  # Permitir todos los encabezados
)

@app.on_event("startup")
def on_startup():
    create_tables()

app.include_router(events.router, prefix="/events", tags=["Events"])
app.include_router(register.router, prefix="/events", tags=["Registers"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the API"}
