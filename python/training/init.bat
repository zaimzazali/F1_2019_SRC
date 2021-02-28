@echo off 

set hasConda=false 
set env=F1_2019_SRC_Env 

rem Check if the computer has Anaconda
echo -------------------------------------------
echo Does this computer has Anaconda installed?
echo -------------------------------------------
1>nul 2>nul call conda --version
if %errorlevel% neq 0 (
    echo False
    echo Please download Anaconda from https://www.anaconda.com/products/individual
    GOTO completed
) else (
    echo True
    echo.
) 

Rem Create conda environment, if not exist
echo -------------------------------------------
echo Creating Conda Environment
echo -------------------------------------------
call conda create env --name F1_2019_SRC_Env

Rem Install relevant packages
echo -------------------------------------------
echo Install Relevant Packages
echo -------------------------------------------
echo Check for 'f1-2019-telemetry' package
call pip install f1-2019-telemetry

:completed
echo.
pause
