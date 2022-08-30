@echo off
setlocal
set ruta=C:\Users\larry\Desktop\fx\cp310\python.exe

call %ruta% tools\build.py setup

if %ERRORLEVEL% == 69 (
	echo Instruccion recibida. Copianding...
	call %ruta% tools\build.py build
) else (
	echo no
)

