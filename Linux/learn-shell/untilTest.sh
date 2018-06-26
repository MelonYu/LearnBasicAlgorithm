#!/bin/sh
#untilTest
#to test the method of until
IS_ROOT=`who|grep root`
until [ "IS_ROOT" ]
do
	IS_ROOT=`who|grep root`
	echo "not root now"
	sleep 5
done
echo "Watch it.root in"
