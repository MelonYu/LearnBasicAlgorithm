#!/bin/sh
#TraverseDir
#Traverse the directory
function read_dir(){
	for FILE in `ls $1`
	do
		if [ -d $1"/"$FILE ]
		then
			read_dir $1"/"$FILE
		else
			echo $1"/"$FILE
		fi
	done
}

read_dir $1
