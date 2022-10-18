#!/bin/bash
# Пункт 1
echo First part

# Создания файла, нужно для Пункта 3, для теста
rm new_file.txt
touch old.txt

echo Enter path to the dir:
read path

ls -ghsR $path >log_before.log
ls -ghsR $path

# Пункт 2
echo Second part

#touch test_app/conf.conf
#touch test_app/lib.lib
#touch test_app/bin_file.

cp_files() {

  cp test_app/conf.conf test_dirs/etc/surname/

  cp test_app/lib.lib test_dirs/usr/lib/surname/
  echo "test_dirs/usr/lib/surname/" >test_dirs/etc/surname/conf.conf

  cp test_app/bin_file. test_dirs/usr/bin/
  echo "test_dirs/usr/bin/" >>test_dirs/etc/surname/conf.conf

  chmod 711 test_dirs/usr/bin/bin_file.
  ls -l test_dirs/usr/bin

}

echo $(cp_files)

# Пункт 3
echo Third part

# Изменяем/удаляем файлы в каталоге
touch new_file.txt
rm old.txt

ls -ghsR $path >log_after.log

diff -y log_before.log log_after.log >test_dirs/var/log/surname.log

echo Please, look at the file test_dirs/var/log/surname.log
