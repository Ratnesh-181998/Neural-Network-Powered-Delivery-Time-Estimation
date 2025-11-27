# Porter NN - Quick Run Script
# Starts both backend and frontend servers

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  Porter NN - Starting Servers" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Function to check if port is in use
function Test-Port {
    param($Port)
    $connection = Test-NetConnection -ComputerName localhost -Port $Port -InformationLevel Quiet -WarningAction SilentlyContinue
    return $connection
}

# Check if backend port is available
if (Test-Port 8000) {
    Write-Host "⚠ Port 8000 is already in use!" -ForegroundColor Yellow
    Write-Host "Please stop the existing process or use a different port." -ForegroundColor Yellow
    Write-Host ""
}

# Check if frontend port is available
if (Test-Port 5173) {
    Write-Host "⚠ Port 5173 is already in use!" -ForegroundColor Yellow
    Write-Host "Vite will automatically use the next available port." -ForegroundColor Yellow
    Write-Host ""
}

Write-Host "Starting Backend API..." -ForegroundColor Yellow
Write-Host "Location: http://localhost:8000" -ForegroundColor Gray
Write-Host "API Docs: http://localhost:8000/docs" -ForegroundColor Gray
Write-Host ""

# Start backend in new window
Start-Process powershell -ArgumentList "-NoExit", "-Command", "cd '$PWD\backend'; ..\\.venv\Scripts\Activate.ps1; uvicorn main:app --reload --port 8000"

# Wait a bit for backend to start
Start-Sleep -Seconds 3

Write-Host "Starting Frontend..." -ForegroundColor Yellow
Write-Host "Location: http://localhost:5173" -ForegroundColor Gray
Write-Host ""

# Start frontend in new window
Start-Process powershell -ArgumentList "-NoExit", "-Command", "cd '$PWD\frontend'; npm run dev"

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  Servers Started!" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

Write-Host "✓ Backend running at: http://localhost:8000" -ForegroundColor Green
Write-Host "✓ Frontend running at: http://localhost:5173" -ForegroundColor Green
Write-Host "✓ API Docs at: http://localhost:8000/docs" -ForegroundColor Green
Write-Host ""

Write-Host "Two new PowerShell windows have been opened." -ForegroundColor Yellow
Write-Host "Close those windows to stop the servers." -ForegroundColor Yellow
Write-Host ""

Write-Host "Opening browser..." -ForegroundColor Yellow
Start-Sleep -Seconds 2
Start-Process "http://localhost:5173"

Write-Host ""
Write-Host "Happy predicting! 🚚💨" -ForegroundColor Green
