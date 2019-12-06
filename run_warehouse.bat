@echo off

for /f "usebackq tokens=*" %%a in ('where python') do "lib/warehouse.py" %%a

pause