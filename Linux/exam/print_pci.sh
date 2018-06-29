#!/bin/sh
#print_pci

ETH=`ifconfig | cut -d' ' -f1 | awk -F':' '{print $1}'`
for E in $ETH
do 
	if [ $E != lo ]
	then
		PCINO=`ethtool -i $E | awk -F' ' 'NR==5{print $2}'`
		echo "$E: $PCINO"
	fi
done 
