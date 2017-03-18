color  1e
if %1.==. ( goto :pad)
del /q file.txt
copy %1% file.txt
:pad
cls
@echo off
python smartEminem.py
exit