# PowerShell script to set up the MCP environment and install the test server

# Check if uv is installed
try {
    $uvVersion = uv --version
    Write-Host "uv version $uvVersion is installed." -ForegroundColor Green
} catch {
    Write-Host "uv is not installed. Please install it from https://github.com/astral-sh/uv" -ForegroundColor Red
    Write-Host "You can install it with: pip install uv" -ForegroundColor Yellow
    exit 1
}

# Check if Python is installed
try {
    $pythonVersion = python --version
    Write-Host "Python $pythonVersion is installed." -ForegroundColor Green
} catch {
    Write-Host "Python is not installed. Please install Python 3.10 or higher." -ForegroundColor Red
    exit 1
}

# Create and activate virtual environment
Write-Host "Creating virtual environment..." -ForegroundColor Cyan
uv venv

# Activate the virtual environment
Write-Host "Activating virtual environment..." -ForegroundColor Cyan
& .\.venv\Scripts\Activate.ps1

# Install dependencies
Write-Host "Installing dependencies..." -ForegroundColor Cyan
uv pip install -r requirements.txt

# Check if Claude Desktop is installed
$claudeDesktopPath = "$env:LOCALAPPDATA\Programs\Claude\Claude.exe"
if (Test-Path $claudeDesktopPath) {
    Write-Host "Claude Desktop is installed." -ForegroundColor Green
} else {
    Write-Host "Claude Desktop might not be installed. Please download it from https://claude.ai/download" -ForegroundColor Yellow
}

# Install the test server in Claude Desktop
Write-Host "Installing test server in Claude Desktop..." -ForegroundColor Cyan
mcp install test_server.py

Write-Host "`nSetup complete!" -ForegroundColor Green
Write-Host "You can now open Claude Desktop and use the Test Server." -ForegroundColor Green
Write-Host "`nTo try the advanced example, run:" -ForegroundColor Cyan
Write-Host "mcp install examples/advanced_server.py" -ForegroundColor White 