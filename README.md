# LibroNet - Sistema de Gestión de Biblioteca

Sistema completo de gestión de biblioteca con arquitectura desacoplada: backend con FastAPI y frontend con React.

## 📁 Estructura del Proyecto

```
LibroNet/
├── backend/              # API REST con FastAPI
│   ├── app/
│   │   ├── database.py   # Conexión a MySQL
│   │   ├── models.py     # Modelos Pydantic
│   │   └── routes.py     # Endpoints API
│   ├── docs/
│   │   └── init_db.sql   # Script de BD
│   ├── main.py           # Punto de entrada
│   └── requirements.txt  # Dependencias Python
│
└── frontend/             # Aplicación React
    ├── src/
    │   ├── components/   # Componentes React
    │   ├── services/     # Cliente API
    │   └── styles/       # Estilos CSS
    └── package.json      # Dependencias Node

```

## 🚀 Inicio Rápido

### 1. Configurar Backend

```bash
cd backend

# Crear entorno virtual
python -m venv venv
venv\Scripts\activate  # Windows
# source venv/bin/activate  # Linux/Mac

# Instalar dependencias
pip install -r requirements.txt

# Configurar variables de entorno
cp .env.example .env
# Editar .env con tus credenciales de MySQL

# Ejecutar
python main.py
```

El backend estará disponible en `http://localhost:8000`
- Documentación API: `http://localhost:8000/docs`

### 2. Configurar Frontend

```bash
cd frontend

# Instalar dependencias
npm install

# Configurar variables de entorno (opcional)
cp .env.example .env

# Ejecutar en modo desarrollo
npm run dev
```

El frontend estará disponible en `http://localhost:3000`

## 📋 Requisitos

### Backend
- Python 3.8+
- MySQL 5.7+

### Frontend
- Node.js 16+
- npm o yarn

## 🔧 Base de Datos

Ejecutar el script SQL en MySQL:

```bash
mysql -u root -p < backend/docs/init_db.sql
```

## 📚 API Endpoints

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET | `/api/libros` | Listar todos los libros |
| GET | `/api/libros/{id}` | Obtener un libro |
| POST | `/api/libros` | Crear un libro |
| PUT | `/api/libros/{id}` | Actualizar un libro |
| DELETE | `/api/libros/{id}` | Eliminar un libro |

## 🎨 Características

- ✅ Arquitectura desacoplada Backend/Frontend
- ✅ API REST completa con FastAPI
- ✅ Interfaz moderna con React
- ✅ Diseño responsive
- ✅ CRUD completo de libros
- ✅ Validación de datos
- ✅ Manejo de errores
- ✅ Documentación automática (Swagger)

## 🔐 Variables de Entorno

### Backend (.env)
```env
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=tu_password
DB_NAME=LibroNet
DB_PORT=3306
```

### Frontend (.env)
```env
VITE_API_URL=http://localhost:8000
```

## 📖 Documentación Detallada

- [Backend README](backend/README.md)
- [Frontend README](frontend/README.md)

## 🤝 Contribuir

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📝 Licencia

Este proyecto está bajo la Licencia MIT.

---

Desarrollado con ❤️ usando FastAPI y React
