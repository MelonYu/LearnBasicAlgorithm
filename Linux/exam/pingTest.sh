#!/bin/sh
#pingTest
#use ping to test the host is up or not
for IP in 10.217.253.{5..35}
do
	ping -c 2 -i 0.5 $IP >/dev/null && echo "$IP 在线" || echo "$IP 离线"
done
