@echo off
chcp 65001 >nul
title Atla Auto-Clicker

echo ========================================
echo   Atla Butonu Auto-Clicker
echo ========================================
echo.

:: Gerekli kutuphaneler yuklu mu kontrol et
python -c "import pyautogui, cv2, PIL" 2>nul
if errorlevel 1 (
    echo [*] Gerekli kutuphaneler kuruluyor...
    pip install pyautogui opencv-python pillow
    echo.
)

:: Scripti calistir
echo [*] Baslatiliyor...
echo [!] Durdurmak icin: Ctrl+C veya fareyi sol ust koseye gotur
echo.
python auto_clicker.py

pause
