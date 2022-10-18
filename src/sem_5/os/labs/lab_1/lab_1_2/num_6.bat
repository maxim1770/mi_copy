@echo off

:: Пункт 1

set dir_path=C:\

set /a number_hidden_subdirectories = 0

for /f "tokens=*" %%i in ('dir /a:DH /b %dir_path%') do (
    echo %dir_path%\%%~i
    set /a number_hidden_subdirectories = number_hidden_subdirectories + 1
)

echo Number of hidden subdirectories = %number_hidden_subdirectories%


:: Пункт 2
echo -------------------------------

set /a number_text_files = 0

for /f "tokens=*" %%i in ('dir /b %dir_path%*.txt') do (
    echo %dir_path%\%%~i
    set /a number_text_files = number_text_files + 1
)

echo Number of text files = %number_text_files%
