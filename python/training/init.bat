@echo off 

set env=F1_2019_SRC_Env 

rem Check if the computer has Anaconda
echo -------------------------------------------
echo Does this computer has Anaconda installed?
echo -------------------------------------------
1>nul 2>nul call conda --version
if %errorlevel% neq 0 (
    echo Result: False
    echo Please download Anaconda from https://www.anaconda.com/products/individual
    echo Ensure that you 'tick' to add Conda to your PATH.
    GOTO completed
) else (
    echo Result: True
    echo.
) 

Rem Create conda environment, if not exist
echo -------------------------------------------
echo Creating Conda Environment
echo -------------------------------------------
call conda create env --name %env%
if %errorlevel% neq 0 (
    echo Has Conda been added to your computer's PATH list?
    GOTO completed
)

Rem Install relevant packages
echo -------------------------------------------
echo Install Relevant Packages
echo -------------------------------------------
echo Check for 'f1-2019-telemetry' package
call pip install f1-2019-telemetry
if %errorlevel% neq 0 (
    echo Has PIP been configured properly?
    GOTO completed
)

:completed
echo.
pause
