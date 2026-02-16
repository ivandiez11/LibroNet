from fastapi import FastAPI, Request, HTTPException, Form, Body
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse, JSONResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from typing import Optional, List

from app.database import (
    fetch_all_libros,
    fetch_libro_by_id,
    create_libro,
    update_libro,
    delete_libro
)

# =========================
# FastAPI app initialization
app = FastAPI(title="LibroNet")
app.mount("/static", StaticFiles(directory="app/static"), name="static")
templates = Jinja2Templates(directory="app/templates")

# Habilitar CORS para permitir uso de la API desde clientes externos (ajusta orígenes en producción)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# MODELOS
# =========================

class LibroNet(BaseModel):
    id_libro: Optional[int]
    titulo: str
    autor: str
    editorial: Optional[str]
    isbn: Optional[str]
    anio_publicacion: Optional[int]
    categoria: Optional[str]
    ejemplares: int
    disponible: int

# =========================
# UTILIDADES
# =========================

def map_rows_to_libros(rows: List[dict]) -> List[LibroNet]:
    return [LibroNet(**row) for row in rows]

# =========================
# APP
# =========================

@app.get("/ping")
def ping():
    return {"message": "pong"}

# =========================
# API REST (JSON) - sin ORM ⚡
@app.get("/api/libros", response_model=List[LibroNet])
def api_list_libros():
    rows = fetch_all_libros()
    libros = map_rows_to_libros(rows)
    return libros

@app.get("/api/libros/{libro_id}", response_model=LibroNet)
def api_get_libro(libro_id: int):
    libro = fetch_libro_by_id(libro_id)
    if not libro:
        raise HTTPException(status_code=404, detail="Libro no encontrado")
    return LibroNet(**libro)

@app.post("/api/libros", response_model=LibroNet, status_code=201)
def api_create_libro(libro: LibroNet):
    data = libro.dict()
    data.pop("id_libro", None)
    new_id = create_libro(data)
    created = fetch_libro_by_id(new_id)
    return LibroNet(**created)

@app.put("/api/libros/{libro_id}", response_model=LibroNet)
def api_update_libro(libro_id: int, libro: LibroNet):
    data = libro.dict()
    data.pop("id_libro", None)
    updated = update_libro(libro_id, data)
    if not updated:
        raise HTTPException(status_code=404, detail="Libro no encontrado")
    updated_libro = fetch_libro_by_id(libro_id)
    return LibroNet(**updated_libro)


@app.delete("/api/libros/{libro_id}")
def api_delete_libro(libro_id: int):
    deleted = delete_libro(libro_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Libro no encontrado")
    return {"mensaje": "Libro eliminado correctamente"}

# =========================
# INDEX / LISTAR
# =========================

@app.get("/", response_class=HTMLResponse)
def get_index(request: Request):
    rows = fetch_all_libros()
    libros = map_rows_to_libros(rows)
    return templates.TemplateResponse(
        "pages/index.html",
        {
            "request": request,
            "libros": libros
        }
    )

# =========================
# CREAR LIBRO
# =========================

@app.post("/libros/crear")
def crear_libro(
    titulo: str = Form(...),
    autor: str = Form(...),
    editorial: Optional[str] = Form(None),
    isbn: Optional[str] = Form(None),
    anio_publicacion: Optional[str] = Form(None),
    categoria: Optional[str] = Form(None),
    ejemplares: str = Form("1"),
    disponible: str = Form("1"),
):
    try:
        anio = int(anio_publicacion) if anio_publicacion else None
        ejemplares_int = int(ejemplares)
        disponible_int = int(disponible)
    except ValueError:
        raise HTTPException(status_code=400, detail="Valores numéricos inválidos")

    data = {
        "titulo": titulo,
        "autor": autor,
        "editorial": editorial,
        "isbn": isbn,
        "anio_publicacion": anio,
        "categoria": categoria,
        "ejemplares": ejemplares_int,
        "disponible": disponible_int,
    }
    create_libro(data)
    return RedirectResponse("/", status_code=303)

# =========================
# EDITAR LIBRO
# =========================

@app.get("/libros/editar/{libro_id}", response_class=HTMLResponse)
def editar_libro_form(request: Request, libro_id: int):
    libro = fetch_libro_by_id(libro_id)
    if not libro:
        raise HTTPException(status_code=404, detail="Libro no encontrado")
    return templates.TemplateResponse(
        "pages/edit.html",
        {
            "request": request,
            "libro": libro
        }
    )

@app.post("/libros/editar/{libro_id}")
def editar_libro(
    libro_id: int,
    titulo: str = Form(...),
    autor: str = Form(...),
    editorial: Optional[str] = Form(None),
    isbn: Optional[str] = Form(None),
    anio_publicacion: Optional[str] = Form(None),
    categoria: Optional[str] = Form(None),
    ejemplares: str = Form("1"),
    disponible: str = Form("1"),
):
    try:
        anio = int(anio_publicacion) if anio_publicacion else None
        ejemplares_int = int(ejemplares)
        disponible_int = int(disponible)
    except ValueError:
        raise HTTPException(status_code=400, detail="Valores numéricos inválidos")

    data = {
        "titulo": titulo,
        "autor": autor,
        "editorial": editorial,
        "isbn": isbn,
        "anio_publicacion": anio,
        "categoria": categoria,
        "ejemplares": ejemplares_int,
        "disponible": disponible_int
    }

    actualizado = update_libro(libro_id, data)
    if not actualizado:
        raise HTTPException(status_code=404, detail="Libro no encontrado")

    return RedirectResponse("/", status_code=303)

# =========================
# ELIMINAR LIBRO
# =========================

@app.delete("/libros/{libro_id}")
def delete_libro_endpoint(libro_id: int):
    eliminado = delete_libro(libro_id)
    if not eliminado:
        raise HTTPException(status_code=404, detail="Libro no encontrado")
    return JSONResponse(
        content={"mensaje": "Libro eliminado correctamente"},
        status_code=200
    )
