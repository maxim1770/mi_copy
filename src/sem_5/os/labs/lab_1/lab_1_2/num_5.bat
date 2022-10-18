::Вариант 5 2022
@echo off

:: Пункт 1
::1. Напишите ВАТ-файл, принимающий на вход в качестве параметра имя каталога и подсчитывающий
::в нем количество пользовательских подкаталогов, имя которых
::начинается с "User", с рекурсивной обработкой каждого из них.

set dir_path=%1

set /a number_user_subdirectories = 0

for /f "tokens=*" %%i in ('dir /a:D /s /b %dir_path%\User*') do (
    echo %dir_path%\%%~i
    set /a number_user_subdirectories = number_user_subdirectories + 1
)

echo Number of user subdirectories = %number_user_subdirectories%

echo -------------------------------


:: Пункт 2
::2. Напишите ВАТ-файл, принимающий на вход в качестве параметра имя каталога и подсчитывающий
::в нем количество файлов размером меньше 1Kb с выводом полного пути к каждому из них.

set /a number_files_smaller_one_kb = 0

for /r %dir_path% %%i in (*.*) do (
    rem Если размер файла < 1 кб == 1024 байт
    rem %%~zi - размер в байтах
    rem lss - знак <
    if %%~zi lss 1024 (
        echo %%~fi - %%~zi Kb
        set /a number_files_smaller_one_kb = number_files_smaller_one_kb + 1
    )
)

echo Number of files smaller than 1Kb = %number_files_smaller_one_kb%
