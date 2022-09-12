@echo off
setlocal
set ruta=C:\Users\larry\Desktop\fx\cp310\python.exe
set NOT_READY=1
set UPDATE=4
set COPY=33
set BUILD=69

call %ruta% tools\build.py setup

if %ERRORLEVEL% == %UPDATE% (
     echo Instruccion recibida. Actualizando...
     call %ruta% tools\build.py update
) else (echo not updated)

if %ERRORLEVEL% == %COPY% (
     echo Check if everything is good to be copied:
     for /f %%k in (tools\src.txt) do xcopy %%k build /L
     call %ruta% tools\build.py copy
) else (echo no copy)

set /p confirmacion=Good to go? [si/no] 

if %ERRORLEVEL% == %BUILD% (
     if "%confirmacion%"=="si" (
          echo Instruccion recibida. Copianding y building...
          for /f "delims=" %%k in (tools\_src.txt) do %%k
          call %ruta% tools\build.py build
     ) else (echo no build)
) else (echo no build)

:ned
