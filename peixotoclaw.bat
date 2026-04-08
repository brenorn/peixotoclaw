@echo off
TITLE PeixotoClaw Runner
:: Desabilita echo para evitar poluição visual

echo ================================================================
echo            PeixotoClaw: Monster Edition 
echo ================================================================
echo.

:: 0. Bootstrap e Organizacao
if not exist "projects\" (
    echo [INFO] Ambiente virgem detectado. Iniciando Bootstrap...
    python scripts\bootstrap.py
)

:: 1. Verificacao de .env
if not exist ".env" (
    echo [INFO] Configurando .env...
    python scripts\bootstrap.py
)

:: 2. Verificacao de dependencias
if not exist "node_modules\" (
    echo [INFO] Instalando dependencias do Core...
    call npm install
)

if not exist "dashboard\node_modules\" (
    echo [INFO] Instalando dependencias do Dashboard...
    cd dashboard
    call npm install
    cd ..
)

echo [OK] Iniciando o sistema completo...
echo [!] O Chrome deve abrir automaticamente em alguns segundos.
echo [!] Se nao abrir, acesse manualmente: http://localhost:5173
echo.
echo Pressione CTRL+C para encerrar o servidor.
echo ----------------------------------------------------------------

:: Executa o comando principal
call npm run ui:dev

if %errorlevel% neq 0 (
    echo.
    echo [ERRO] Ocorreu um erro ao iniciar o PeixotoClaw.
    echo Verifique se as portas 3001 e 5173 estao livres.
    pause
)

pause
