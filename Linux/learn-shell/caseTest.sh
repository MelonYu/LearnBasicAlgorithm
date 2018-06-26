#!/bin/sh
#caseTest
#to test the method of case
USER=`whoami`

case $USER in
	root)echo "You can do all the operations"
		;;
	amelia)echo "You can do some operations"
		;;
	*)echo "sorry, you can do nothing"
		;;
esac
