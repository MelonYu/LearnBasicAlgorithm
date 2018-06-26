#!/bin/sh
#Operator
#Basic operator between two integer
SUM=`expr $1 + $2`
SUB=`expr $1 - $2`
PRODUCT=`expr $1 \* $2`
DIV=`expr $1 / $2`
echo "$1+$2=$SUM"
echo "$1-$2=$SUB"
echo "$1*$2=$PRODUCT"
echo "$1/$2=$DIV"
