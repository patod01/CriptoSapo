@echo off
setlocal
echo - server turned ON -

set ruta=C:\Users\larry\Desktop\fx\cp310\python.exe
call %ruta% ..\luffy.py spy

echo - server turned OFF -
pause>nul
