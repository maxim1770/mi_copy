#!/bin/bash

# Пункт 1
echo First part

get_num_recent_files() {
  # Функция возвращает кол. недавно (за последний день) созданных/измененных файлов

  path=
  recent_files=$(find $path -maxdepth 1 -type f -mtime -1) # подробнее тут: https://translated.turbopages.org/proxy_u/en-ru.ru.b441ad4c-6322398d-209b430b-74722d776562/https/stackoverflow.com/questions/16085958/find-the-files-that-have-been-changed-in%20-last-24-hours%20

  # Подсчитываем кол. файлов и записываем это значение в переменную num_recent_files
  num_recent_files=0
  for file_data in $recent_files; do

    ((num_recent_files++))
  done

  echo "Number of recent files = " $num_recent_files
  echo $recent_files # Если нужно показать какие файлы/папки были недавно созданы/изменены

}

echo $(get_num_recent_files)

# Пункт 2
echo Second part

create_files() {

  touch test_dirs/usr/bin/bin_file.
  chmod g-rw test_dirs/usr/bin/bin_file.

  touch test_dirs/usr/lib/lib.lib
  touch test_dirs/usr/share/doc/surname/doc.doc

  ls -l test_dirs/usr/bin
}

echo $(create_files)

# Пункт 3
echo Third part

path=test_dir
size_N_MB=2
## OR
#path=$1
#size_N_MB=$2

echo -e "Unzip these files from archive.tar.gz to $path/"
tar -xvf archive.tar.gz

big_files=$(find $path -maxdepth 1 -type f -size +"$size_N_MB"M)
echo -e "Files with size > $size_N_MB M\n$big_files" >test_dirs/var/log/surname.log

echo -e "\nCreate archive.tar.gz with files" >>test_dirs/var/log/surname.log
tar -cvf archive.tar.gz $big_files >>test_dirs/var/log/surname.log

echo -e "\nRemove files from the $path/" >>test_dirs/var/log/surname.log
rm $big_files
echo -e "$big_files" >>test_dirs/var/log/surname.log

echo -e "\nCreate empty files with the same names" >>test_dirs/var/log/surname.log
touch $big_files >>test_dirs/var/log/surname.log
echo -e "$big_files" >>test_dirs/var/log/surname.log
