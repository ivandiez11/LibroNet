# Frontend - LibroNet

Aplicación web desarrollada con React + Vite para la gestión de una biblioteca.

## Tecnologías

- React 18
- Vite (build tool)
- Axios (HTTP client)
- CSS3 (estilos personalizados)

## Requisitos

- Node.js 16+
- npm o yarn

## Instalación

1. Instalar dependencias:
```bash
npm install
```

2. Configurar variables de entorno:
```bash
cp .env.example .env
```
Editar `.env` si es necesario (la URL del backend está por defecto en `http://localhost:8000`).

## Ejecución

### Modo desarrollo
```bash
npm run dev
```
La aplicación estará disponible en `http://localhost:3000`

### Build para producción
```bash
npm run build
```

### Preview del build
```bash
npm run preview
```

## Estructura del Proyecto

```
frontend/
├── src/
│   ├── components/
│   │   ├── LibroForm.jsx      # Formulario crear/editar libro
│   │   └── LibrosList.jsx     # Lista de libros
│   ├── services/
│   │   └── api.js             # Cliente API con Axios
│   ├── styles/
│   │   ├── index.css          # Estilos globales
│   │   ├── App.css            # Estilos del componente principal
│   │   ├── LibroForm.css      # Estilos del formulario
│   │   └── LibrosList.css     # Estilos de la lista
│   ├── App.jsx                # Componente principal
│   └── main.jsx               # Punto de entrada
├── index.html                 # HTML base
├── vite.config.js             # Configuración Vite
├── package.json               # Dependencias
└── .env.example               # Variables de entorno ejemplo
```

## Funcionalidades

- ✅ Listar todos los libros
- ✅ Ver detalles de cada libro
- ✅ Crear nuevos libros
- ✅ Editar libros existentes
- ✅ Eliminar libros
- ✅ Diseño responsive
- ✅ Validación de formularios
- ✅ Manejo de errores
- ✅ Estados de carga

## Configuración del Proxy

El archivo `vite.config.js` incluye un proxy configurado para redirigir las peticiones `/api` al backend en `http://localhost:8000`. Esto evita problemas de CORS durante el desarrollo.
