#article=art11
#author=larisa
#direction=math
#magazine=vk
#year=2022
#
#declare -A criterias=(["author"]=$author ["direction"]=$direction ["magazine"]=$magazine ["year"]=$year)
## взял тут: https://stackoverflow.com/questions/1494178/how-to-define-hash-tables-in-bash


echo enter article:
read article

declare -A criterias

for criteria in $(ls base_catalog/part_2);
do
  echo enter $criteria:
  read criterias[$criteria]
done


if [ -d "base_catalog/part_1/$article" ]; then
 set -e
fi
mkdir base_catalog/part_1/$article

# ПОКА НЕ ПОНЯТНО ЧТО С ЭТИМ ДЕЛАТЬ
echo the text of the article... > base_catalog/part_1/$article/$article.txt

for criteria in "${!criterias[@]}";
do
  echo ${criterias[$criteria]} > base_catalog/part_1/$article/$criteria.txt
done


for criteria in "${!criterias[@]}";
do

  if [ ! -d "base_catalog/part_2/$criteria/${criterias[$criteria]}" ]; then
  mkdir base_catalog/part_2/$criteria/${criterias[$criteria]}
  fi
  # Подробнее про проверку тут: https://stackoverflow.com/questions/59838/how-do-i-check-if-a-directory-exists-in-a-bash-shell-script

  ln -s base_catalog/part_1/$article/$article.txt base_catalog/part_2/$criteria/${criterias[$criteria]}/$article
done
