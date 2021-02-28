@echo off

set env=F1_2019_SRC_Env 
set mainFile=main.py

rem To activate the Conda Environment
call activate %env%

rem To run the Main Python script
python %mainFile%

echo.
pause
