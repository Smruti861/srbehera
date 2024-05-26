#!/bin/bash
#
pro=1

for (( i=1;i<=30;i++ ))
do
   pro=$((pro * i))
done
echo "$pro"
