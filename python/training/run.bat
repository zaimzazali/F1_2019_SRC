@echo off

rem To activate the Conda Environment
call activate F1_2019_SRC_Env

rem This section is highly dependant on your Computer Workspace Storage
rem Initially, the Workspace is in Local D
rem Please change your working directory to suit your computer settings
d:
cd D:\GitClones\F1_2019_SRC\python\training

rem To run the Main Python script
python main.py

echo.
pause
