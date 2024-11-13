#!/bin/bash
count=0
IFS=$'\t'
rm -f *.details
while read name	email	city	birthday_day	birthday_month	birthday_year	country
do
    if test -z ${name} || test ${country} == "country"
       then continue
       else count=$(( count+1 )) 
            outputfile=${country// /}.younger.details
            if test ${birthday_year} -le 1980
               then outputfile=${country// /}.older.details
            fi
            echo -e "${name}\t${email}\t${birthday_year}\t${country}" >> ${outputfile}
    fi
done < example_people_data.tsv
unset IFS

