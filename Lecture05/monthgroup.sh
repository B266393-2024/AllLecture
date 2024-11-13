#!/bin/bash
count=0
IFS=$'\t'

while read name email city birthday_day birthday_month birthday_year country
do
    if test -z ${name} || test ${birthday_month} ==  "birthday_month"
       then echo "Ignoring"
    else count=$(($count+1))
         echo -e "${name}\t${email}\t${country}\t${birthday_month}" >> ${birthday_month}.details
    fi
done < example_people_data.tsv

unset IFS
