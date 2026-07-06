@echo off
title PyInstaller Build - Def Con
setlocal

:: ===============================
:: Virtual Environment Check
:: ===============================
if not exist ".venv\" (
    echo [*] Creating virtual environment...
    python -m venv venv

    if errorlevel 1 (
        echo [!] Failed to create venv
        pause
        exit /b 1
    )
)

:: ===============================
:: Activate venv
:: ===============================
call venv\Scripts\activate.bat

:: ===============================
:: Install Requirements
:: ===============================
if exist "requirements.txt" (
    echo [*] Installing requirements...
    python -m pip install --upgrade pip
    pip install -r requirements.txt
) else (
    echo [*] Installing PyInstaller...
    python -m pip install --upgrade pip
    pip install pyinstaller
)

:: ===============================
:: Clean old build
:: ===============================
echo [*] Cleaning old build...

if exist build rmdir /s /q build
if exist dist rmdir /s /q dist
if exist *.spec del /q *.spec

:: ===============================
:: Build EXE
:: ===============================
echo [*] Building EXE...

pyinstaller ^
    --onefile ^
    --console ^
    --clean ^
    --name "Def Con" ^
    --icon=rtlogo.ico ^
    main.py

:: ===============================
:: Done
:: ===============================
if errorlevel 1 (
    echo.
    echo [!] Build Failed!
) else (
    echo.
    echo [✓] Build Successful!
    echo EXE Location: dist\Def Con.exe
)

pause