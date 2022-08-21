@echo off
setlocal
echo - server turned ON -

:: path to python.exe
set ruta=C:\Users\larry\Desktop\fx\cp310\python.exe

call %ruta% ..\going_merry\luffy.py spy

echo - server turned OFF -
pause>nul
