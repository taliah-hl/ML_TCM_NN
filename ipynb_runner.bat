@echo off

REM Run the first command
set PYTHONPATH=%CD%

echo Start running notebook
echo running sympton_only.ipynb
jupyter nbconvert --to notebook --execute sympton_only.ipynb

REM Check the exit status of the first command
if %errorlevel% neq 0 (
    echo Error occurred in 1st nb
    exit /b 1
)

echo running sympton_only_2.ipynb
jupyter nbconvert --to notebook --execute sympton_only_2.ipynb

REM Check the exit status of the second command
if %errorlevel% neq 0 (
    echo Error occurred in 2nd nb
    exit /b 1
)

echo All commands completed successfully.
