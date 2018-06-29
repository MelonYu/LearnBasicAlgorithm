#!/bin/sh

for IP in 10.217.253.20 10.217.253.3
do
	echo "-----------"
	echo "$IP:" 
	MEM=`ssh $IP free -m | awk '/Mem:/{print $3/$2*100}'`
	echo "Memory: $MEM %"
	DISK=`ssh $IP df -h | awk 'NR==2 {print $1 ": " $5}'`
	echo "$DISK"
#	ssh $IP cat /proc/stat | grep cpu
	ssh $IP top -n1 -b | awk 'NR==3{print $1,$2}'
done

