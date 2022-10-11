@echo off
setlocal
:: path to python.exe
set pydist=pydist\python.exe
echo Running app...
call %pydist% going_merry\robin.py
echo App closed.
