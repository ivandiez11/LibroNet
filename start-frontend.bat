@echo off
echo ================================
echo   LibroNet - Iniciar Frontend
echo ================================
echo.

cd frontend

echo Verificando archivo .env...
if not exist ".env" (
    echo Copiando .env.example a .env...
    copy .env.example .env
)

echo.
echo Verificando node_modules...
if not exist "node_modules\" (
    echo Instalando dependencias...
    call npm install
)

echo.
echo ================================
echo   Iniciando servidor frontend...
echo ================================
echo Frontend disponible en: http://localhost:3000
echo.

call npm run dev
