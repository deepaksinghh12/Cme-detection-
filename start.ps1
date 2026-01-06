# PowerShell Script to Start Both Backend and Frontend

Write-Host "Starting CME Detection Phased Project..." -ForegroundColor Green
Write-Host ""

# Start Backend in new window
Write-Host "Starting Backend Server..." -ForegroundColor Yellow
Start-Process powershell -ArgumentList "-NoExit", "-Command", "cd '$PSScriptRoot\backend'; python main.py"

# Wait a bit for backend to start
Start-Sleep -Seconds 3

# Start Frontend in new window
Write-Host "Starting Frontend Server..." -ForegroundColor Yellow
Start-Process powershell -ArgumentList "-NoExit", "-Command", "cd '$PSScriptRoot\frontend'; npm run dev"

Write-Host ""
Write-Host "Both servers are starting in separate windows!" -ForegroundColor Green
Write-Host "Backend: http://localhost:8002" -ForegroundColor Cyan
Write-Host "Frontend: http://localhost:5173" -ForegroundColor Cyan
Write-Host ""
Write-Host "Access Phase 1 at: http://localhost:5173/phase1" -ForegroundColor Magenta
Write-Host ""
Write-Host "Press any key to exit this window (servers will keep running)..." -ForegroundColor Gray
$null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")


