@echo off
setlocal

python -m venv .venv
if errorlevel 1 exit /b %errorlevel%

.venv\Scripts\python.exe -m pip install -e ".[test]"
if errorlevel 1 exit /b %errorlevel%

.venv\Scripts\python.exe -m pytest -v
if errorlevel 1 exit /b %errorlevel%

.venv\Scripts\hello.exe
if errorlevel 1 exit /b %errorlevel%
