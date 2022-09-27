@echo off

if "p"=="%1" call %pyDevDist% %2 %3 %4 %5

if ""=="%PENV%" (goto settingPaths) else goto ned

:settingPaths
	rem Set this to your python interpreter
	echo 4
	set pyDevDist="C:\Users\larry\Documents\mygit\CriptoSapo\tools\pydist\cp310\python.exe"
	set path=%path%;%cd%\tools
	set PENV=ok
	echo added project dev tools to path
	echo %path%

:ned
