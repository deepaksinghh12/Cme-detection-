@echo off
echo Starting CME Detection Phased Project...
echo.

echo Starting Backend Server...
start "Backend Server" cmd /k "cd /d %~dp0backend && python main.py"

timeout /t 3 /nobreak >nul

echo Starting Frontend Server...
start "Frontend Server" cmd /k "cd /d %~dp0frontend && npm run dev"

echo.
echo Both servers are starting in separate windows!
echo Backend: http://localhost:8002
echo Frontend: http://localhost:5173
echo.
echo Access Phase 1 at: http://localhost:5173/phase1
echo.
pause


