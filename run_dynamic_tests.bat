@echo off

cd lib\
python -m unittest -v backend_dyn_test.py
cd ..

pause