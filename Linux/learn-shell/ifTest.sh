#!/bin/sh
#ifTest
#To show the method of if
echo -e "Enter the first integer:\c"
read FIRST
echo -n "Enter the second interger:"
read SECOND
if [ "$FIRST" -gt "$SECOND" ]
then
	echo "$FIRST is greater than $SECOND"
elif [ "$FIRST" -lt "$SECOND" ]
then
	echo "$FIRST is less than $SECOND"
else
	echo "$FIRST is equal to $SECOND"
fi
