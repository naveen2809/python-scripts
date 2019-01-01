#!/bin/bash 

count=0

while :
do
echo "Iteration $count"
python3 telnet_example.py
count=`expr $count + 1`
sleep 60
done
