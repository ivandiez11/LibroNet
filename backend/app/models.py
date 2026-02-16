from pydantic import BaseModel, Field
from typing import Optional

class LibroBase(BaseModel):
    """Modelo base para libros"""
    titulo: str = Field(..., min_length=1, max_length=255)
    autor: str = Field(..., min_length=1, max_length=255)
    editorial: Optional[str] = Field(None, max_length=255)
    isbn: Optional[str] = Field(None, max_length=20)
    anio_publicacion: Optional[int] = Field(None, ge=1000, le=9999)
    categoria: Optional[str] = Field(None, max_length=100)
    ejemplares: int = Field(default=1, ge=0)
    disponible: int = Field(default=1, ge=0)

class LibroCreate(LibroBase):
    """Modelo para crear un libro"""
    pass

class LibroUpdate(LibroBase):
    """Modelo para actualizar un libro"""
    titulo: Optional[str] = Field(None, min_length=1, max_length=255)
    autor: Optional[str] = Field(None, min_length=1, max_length=255)
    ejemplares: Optional[int] = Field(None, ge=0)
    disponible: Optional[int] = Field(None, ge=0)

class LibroNet(LibroBase):
    """Modelo completo de libro con ID"""
    id_libro: int
    
    class Config:
        from_attributes = True
