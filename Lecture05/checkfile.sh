#!/bin/bash
count=0
IFS=$'\t'
while read name	email	city	birthday_day	birthday_month	birthday_year	country
do
if test -z ${name}
   then echo -e "X\tblank line found"
else
   if test ${name} == "name"
      then echo -e "X\theadline found"
   else count=$((count+1))
      echo -e "${count}\t${country}"
   fi
fi
done < example_people_data.tsv
unset IFS
