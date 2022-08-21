@echo off

setlocal
set ruta=C:\Users\larry\Desktop\fx\cp310\python.exe
pushd tools

:: calling modules
rem call %ruta% ..\going_merry\luffy.py buy
rem call %ruta% ..\going_merry\luffy.py sell
rem call %ruta% ..\going_merry\luffy.py ship
rem call %ruta% ..\going_merry\luffy.py spy
rem call %ruta% ..\going_merry\luffy.py pete

:: Injected tools
rem copy t.py ..\going_merry\_t.py
rem call %ruta% ..\going_merry\_t.py

popd
pause
