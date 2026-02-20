from fastapi import APIRouter, HTTPException
from typing import List
from .models import LibroNet, LibroCreate, LibroUpdate
from .database import (
    fetch_all_libros,
    fetch_libro_by_id,
    create_libro,
    update_libro,
    delete_libro
)

router = APIRouter()

# =========================
# UTILIDADES
# =========================

def map_rows_to_libros(rows: List[dict]) -> List[LibroNet]:
    return [LibroNet(**row) for row in rows]

# =========================
# API REST ENDPOINTS
# =========================

@router.get("/ping")
def ping():
    """Endpoint de prueba"""
    return {"message": "pong"}

@router.get("/libros", response_model=List[LibroNet])
def api_list_libros():
    """Obtener todos los libros"""
    rows = fetch_all_libros()
    libros = map_rows_to_libros(rows)
    return libros

@router.get("/libros/{libro_id}", response_model=LibroNet)
def api_get_libro(libro_id: int):
    """Obtener un libro por ID"""
    libro = fetch_libro_by_id(libro_id)
    if not libro:
        raise HTTPException(status_code=404, detail="Libro no encontrado")
    return LibroNet(**libro)

@router.post("/libros", response_model=LibroNet, status_code=201)
def api_create_libro(libro: LibroCreate):
    """Crear un nuevo libro"""
    data = libro.dict()
    new_id = create_libro(data)
    created = fetch_libro_by_id(new_id)
    return LibroNet(**created)

@router.put("/libros/{libro_id}", response_model=LibroNet)
def api_update_libro(libro_id: int, libro: LibroUpdate):
    """Actualizar un libro existente"""
    data = libro.dict(exclude_unset=True)
    updated = update_libro(libro_id, data)
    if not updated:
        raise HTTPException(status_code=404, detail="Libro no encontrado")
    updated_libro = fetch_libro_by_id(libro_id)
    return LibroNet(**updated_libro)

@router.delete("/libros/{libro_id}")
def api_delete_libro(libro_id: int):
    """Eliminar un libro"""
    deleted = delete_libro(libro_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Libro no encontrado")
    return {"mensaje": "Libro eliminado correctamente"}
