@echo off

setlocal
set ruta=C:\Users\larry\Desktop\fx\cp310\python.exe
pushd tools
rem call %ruta% ..\luffy.py buy
rem call %ruta% ..\luffy.py sell
rem call %ruta% ..\luffy.py spy
call %ruta% ..\luffy.py ship
rem call %ruta% ..\luffy.py pete

popd
pause
