@echo off
set ts=%date:~10,4%%date:~4,2%%date:~7,2%_%time:~0,2%%time:~3,2%
set ts=%ts: =0%
python -m pytest -m regression --self-contained-html --html=reports/regression_report_%ts%.html -v
pause