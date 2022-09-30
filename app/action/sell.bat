@echo off
setlocal
:: path to python.exe
set pydist=..\pydist\python.exe
call %pydist% ..\going_merry\luffy.py sell
pause>nul
