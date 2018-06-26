#!/bin/sh
#forTest
#Totest the method of for
COUNTER=0
for FILES in *
do
	COUNTER=`expr $COUNTER + 1`
done
echo "There are $COUNTER files in `pwd`"
