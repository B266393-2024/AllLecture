#!/bin/bash
count=0
IFS=$'\t'
while read name	email city birthday_day birthday_month birthday_year country
      if -z test ${name} = "" || test ${country} == "country"
         then echo "Ignoring"
      else count=$(( ${count}+1 ))
           echo -e "${name}\t${email}\t${city}\t${country}}" >> ${country// /}.details
      fi
done < example_people_data.tsv
unset IFS
