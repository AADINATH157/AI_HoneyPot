@echo off
echo ========================================
echo AI Honeypot System - Startup Script
echo ========================================
echo.

echo [1/4] Checking dependencies...
pip show flask >nul 2>&1
if errorlevel 1 (
    echo Installing dependencies...
    pip install -r requirements.txt
)

echo [2/4] Training ML model...
if not exist model.pkl (
    python train_model.py
) else (
    echo Model already exists. Skipping training.
)

echo [3/4] Starting Flask server on port 8000...
start "Flask Server" cmd /k python server.py

timeout /t 3 /nobreak >nul

echo [4/4] Starting Honeypot on port 9999...
start "Honeypot" cmd /k python honeypot.py

echo.
echo ========================================
echo System started successfully!
echo Web Dashboard: http://localhost:8000
echo Honeypot listening on port 9999
echo ========================================
echo.
echo Press any key to exit this window...
pause >nul
