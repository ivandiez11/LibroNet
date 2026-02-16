# Backend - LibroNet API

API REST desarrollada con FastAPI para la gestión de una biblioteca.

## Requisitos

- Python 3.8+
- MySQL

## Instalación

1. Crear un entorno virtual:
```bash
python -m venv venv
```

2. Activar el entorno virtual:
```bash
# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

3. Instalar dependencias:
```bash
pip install -r requirements.txt
```

4. Configurar variables de entorno:
```bash
cp .env.example .env
```
Editar `.env` con tus credenciales de base de datos.

5. Inicializar la base de datos:
```bash
# Ejecutar el script SQL en docs/init_db.sql en tu servidor MySQL
```

## Ejecución

### Modo desarrollo
```bash
python main.py
```

o

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

### Modo producción
```bash
uvicorn main:app --host 0.0.0.0 --port 8000
```

## API Endpoints

- `GET /` - Información de la API
- `GET /docs` - Documentación interactiva (Swagger UI)
- `GET /api/ping` - Endpoint de prueba
- `GET /api/libros` - Listar todos los libros
- `GET /api/libros/{id}` - Obtener un libro por ID
- `POST /api/libros` - Crear un libro
- `PUT /api/libros/{id}` - Actualizar un libro
- `DELETE /api/libros/{id}` - Eliminar un libro

## Estructura del Proyecto

```
backend/
├── app/
│   ├── __init__.py
│   ├── database.py      # Conexión y operaciones de BD
│   ├── models.py        # Modelos Pydantic
│   └── routes.py        # Endpoints de la API
├── docs/
│   └── init_db.sql      # Script de inicialización de BD
├── main.py              # Punto de entrada de la aplicación
├── requirements.txt     # Dependencias
└── .env.example         # Ejemplo de variables de entorno
```
