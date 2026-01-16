from fastapi import FastAPI, Request, Form, HTTPException
from fastapi.responses import HTMLResponse, RedirectResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel, EmailStr, field_validator, ValidationError
from typing import Optional, List
import re

# importar funciones de la base de datos
from app.database import (
    delete_libro,
    get_connection,
    fetch_all_libros
)


# Modelo para la Base de Datos
class LibroNet(BaseModel):
    id_libro: Optional[int]
    titulo: str
    autor: str
    editorial: str
    isbn: str
    anio_publicacion: int
    categoria: str
    ejemplares: int
    disponible: int

# Modelo para crear un nuevo libro (sin ID)
class LibroCreate(BaseModel):
    pass

# Modelo para actualiazar un nuevo libro (sin ID)
class LibroUpdate(BaseModel):
    pass

# Modelo completo de Libro (con ID)
class Libro(BaseModel):
    id: int


def map_rows_to_libros(rows: List[dict]) -> List[LibroNet]:
    libros = []
    for row in rows:
        libro = LibroNet(
            id_libro=row["id_libro"],
            titulo=row["titulo"],
            autor=row["autor"],
            editorial=row["editorial"],
            isbn=row["isbn"],
            anio_publicacion=row["anio_publicacion"],
            categoria=row["categoria"],
            ejemplares=row["ejemplares"],
            disponible=row["disponible"]
        )
        libros.append(libro)
    return libros




app = FastAPI(title = "LibroNet")

# Servir archivos estáticos
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Motor de plantillas
templates = Jinja2Templates(directory="app/templates")


@app.get("/ping")
def ping():
    return {"message": "pong"}

# --- Get principal ---
@app.get("/", response_class=HTMLResponse)
def get_index(request: Request):

    # 1 rObtenemos los libros de la base de datos
    rows = fetch_all_libros()

    # 2 Mapear las filas a instancias de LibroNet
    libros = map_rows_to_libros(rows)

    # 3 Enviamos la plantilla
    return templates.TemplateResponse(
        "pages/index.html",
        {
            "request": request,
            "libros": libros
        }
    )


# --- DELETE eliminar libros ---
@app.delete("/libros/{libro_id}")
def delete_libro_endpoint(libro_id: int):
    """
    Endpoint para eliminar un libro por su ID.
    """
    eliminado = delete_libro(libro_id)
    
    if not eliminado:
        raise HTTPException(status_code=404, detail="Libro no encontrado")
    
    return JSONResponse(
        content={"mensaje": "Libro eliminado exitosamente"},
        status_code=200
    )
