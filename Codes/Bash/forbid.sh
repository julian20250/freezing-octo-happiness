#!/bin/bash
echo "Hello, $USER"
#if [ $(whoami) == "root" ]
#then

echo "Your ip is..."

q=0
for x in $(ip route)
do
if [ $q == 2 ]
then
w=$x
fi
q=$(expr $q + 1)
done

echo $w

echo "Today's date is $(date), this is week $(date +%V)."
echo
echo "This is `uname -s` running on a `uname -m` processor."
echo "This is the uptime information:"
uptime

read -p "Do you want to have some fun? (y/n) > " a
if [ $a == "y" ]
then
	echo "I'd like it!"
	echo "Now see the people connected to the net. Look!"
	e=0
	for x in $(ip route)
	do
	if [ $e == 7 ]
	then
		r=$x
	fi
	e=$(expr $e + 1)
	done

	nmap -sP $r 

elif [ $a == "n" ]
then
	echo "Ok, it would be the next time"

else
	echo "$a is not an option :("
	exit
fi

echo
echo "That's all folks!"
