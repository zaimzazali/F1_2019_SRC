@echo off

set env=F1_2019_SRC_Env 
set mainFile=main.py

rem This section is highly dependant to your Computer Workspace Settings
rem Initially, the Workspace is set to be in 'Local D'
rem Please change the values to suit your computer settings
set workingLocal=d:
set workingDir=d:\GitClones\F1_2019_SRC\python\training

rem To activate the Conda Environment
call activate %env%

rem To navigate to Working Directory
%workingLocal%
cd %workingDir%

rem To run the Main Python script
python %mainFile%

echo.
pause
