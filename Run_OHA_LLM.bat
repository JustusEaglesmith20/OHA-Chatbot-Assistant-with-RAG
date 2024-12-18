@echo off
REM Navigate to the directory of your Flask app
cd "C:\Users\justu\OneDrive\Documents\Data_science\Portfolio\OHP LLM\OHA_LLM.py"

REM Set Flask environment variables
set FLASK_APP=OHA_LLM.py
set FLASK_ENV=development

REM Launch Flask app
python -m flask run

pause
