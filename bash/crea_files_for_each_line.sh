#!/bin/bash
file=$1
echo $file
#declare -i counter=1
while read line
do
   filename=$(echo $line|awk '{print $4}'| cut -c2-| rev | cut -c3- | rev)
   echo "$line" >> temp/$filename.json
#  echo "$counter.json"
#   counter=$((counter+1))
done<$file
