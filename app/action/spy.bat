@echo off
setlocal
echo - server turned ON -

:: path to python.exe
set pydist=..\pydist\python.exe

call %pydist% ..\going_merry\luffy.py spy

echo - server turned OFF -
pause>nul
