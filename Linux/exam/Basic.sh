#!/bin/sh
#Basic
#For exam test No.1
NETINFO=`ifconfig | awk '/net /{print $2}' ORS=","` 
echo $NETINFO

FILE=`find /home -name Daily_Archive.sh -print`
echo $FILE

FILETAIL=`tail -10 $FILE`
echo $FILETAIL

FILEHEAD=`head -10 $FILE`
echo $FILEHEAD

`find ./ -name Daily_Archive.sh | xargs sed -i "s/does not exist/don\'t exist/g"`

