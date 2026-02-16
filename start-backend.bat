@echo off
echo ================================
echo   LibroNet - Iniciar Backend
echo ================================
echo.

cd backend

echo Verificando entorno virtual...
if not exist "venv\" (
    echo Creando entorno virtual...
    python -m venv venv
)

echo Activando entorno virtual...
call venv\Scripts\activate

echo.
echo Verificando archivo .env...
if not exist ".env" (
    echo ADVERTENCIA: No se encontro .env
    echo Copiando .env.example a .env...
    copy .env.example .env
    echo.
    echo POR FAVOR, edita backend\.env con tus credenciales de MySQL antes de continuar.
    pause
)

echo.
echo Instalando dependencias...
pip install -r requirements.txt

echo.
echo ================================
echo   Iniciando servidor backend...
echo ================================
echo Backend disponible en: http://localhost:8000
echo Documentacion API: http://localhost:8000/docs
echo.

python main.py
