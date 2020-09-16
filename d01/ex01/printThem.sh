#!/bin/bash
i=0
while [ $i -le 100 ]
do
	echo -n "$i," >> numbers.txt
	i=$(( $i + 1))
done
