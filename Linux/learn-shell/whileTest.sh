#!/bin/sh
#whileTest
#to test the method of while
COUNTER=0
while [ "$COUNTER" -lt "10" ]
do
	echo $COUNTER
	COUNTER=`expr $COUNTER + 1`
done
